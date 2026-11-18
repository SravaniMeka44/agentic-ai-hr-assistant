
from dotenv import load_dotenv
from langgraph.types import Command

load_dotenv()

from agents.hr_agent import agent


# ========================================
# CONVERSATION CONFIGURATION
# ========================================

config = {
    "configurable": {
        "thread_id": "hr_conversation_1"
    }
}


# ========================================
# RUN HR AGENT
# ========================================

def run_agent(request):

    result = agent.invoke(
        request,
        config=config
    )

    # ------------------------------------
    # HANDLE HUMAN APPROVAL
    # ------------------------------------

    while result.get("__interrupt__"):

        pending_approvals = result["__interrupt__"]

        if len(pending_approvals) != 1:
            print(
                "Multiple simultaneous approvals "
                "are not supported yet."
            )
            return

        details = pending_approvals[0].value

        print("\n" + "=" * 55)
        print("INTERVIEW APPROVAL REQUIRED")
        print("=" * 55)

        print(
            "Candidate:",
            details.get("candidate_name", "")
        )

        print(
            "Job Role:",
            details.get("role", "")
        )

        print(
            "Candidate Email:",
            details.get("attendee_email", "")
        )

        print(
            "Event Title:",
            details.get("title", "")
        )

        print(
            "Start:",
            details.get("start_time", "")
        )

        print(
            "End:",
            details.get("end_time", "")
        )

        # --------------------------------
        # SHOW COMPLETE INVITATION
        # --------------------------------

        print("\n" + "-" * 55)
        print("INVITATION MESSAGE PREVIEW")
        print("-" * 55)

        print(details.get("description", ""))

        print("-" * 55)

        # --------------------------------
        # GET APPROVAL
        # --------------------------------

        while True:

            answer = input(
                "\nApprove and send invitation? "
                "(yes/no): "
            ).strip().lower()

            if answer in ("yes", "y"):
                decision = "approve"
                break

            if answer in ("no", "n"):
                decision = "reject"
                break

            print("Please enter yes or no.")

        # --------------------------------
        # RESUME AGENT
        # --------------------------------

        result = agent.invoke(
            Command(resume=decision),
            config=config
        )

    # ------------------------------------
    # DISPLAY RESPONSE
    # ------------------------------------

    if result.get("messages"):

        last_message = result["messages"][-1]

        print("\nHR Agent:")
        print(last_message.content)
        print()


# ========================================
# MAIN TERMINAL CHAT
# ========================================

print("\n" + "=" * 55)
print("NOVATECH AI SOLUTIONS")
print("AI HR RECRUITMENT ASSISTANT")
print("=" * 55)

print("\nHR Assistant started!")
print("Type 'exit' to quit.\n")


while True:

    user_input = input("You: ").strip()

    if user_input.lower() in ("exit", "quit"):
        print("\nHR Assistant: Goodbye!")
        break

    if not user_input:
        continue

    try:
        run_agent({
            "messages": [
                {
                    "role": "user",
                    "content": user_input
                }
            ]
        })

    except Exception as error:
        print(f"\nError: {error}\n")
