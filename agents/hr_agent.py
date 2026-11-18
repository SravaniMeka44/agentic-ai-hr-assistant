
from datetime import datetime
from zoneinfo import ZoneInfo

from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import InMemorySaver

from tools.google_calendar import (
    get_calendar_events,
    get_calendar_events_range,
    create_calendar_event
)


# ========================================
# CONFIGURATION
# ========================================

TIMEZONE = ZoneInfo("Europe/Berlin")

today = datetime.now(TIMEZONE).date().isoformat()


# ========================================
# MODEL
# ========================================

model = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0
)


# ========================================
# CONVERSATION MEMORY
# ========================================

memory = InMemorySaver()


# ========================================
# SINGLE HR AGENT
# ========================================

agent = create_agent(
    model=model,

    tools=[
        get_calendar_events,
        get_calendar_events_range,
        create_calendar_event
    ],

    checkpointer=memory,

    system_prompt=(
        "You are an intelligent AI HR Recruitment Assistant. "

        # Company identity
        "You represent NovaTech AI Solutions, a fictional "
        "company used for a recruitment demonstration. "
        "The HR representative is Sravani Meka. "
        "The designation is HR Recruitment Team. "

        # General behavior
        "Help users manage their Google Calendar and "
        "schedule job interviews professionally. "
        "Use Google Calendar tools whenever calendar "
        "information is needed. "
        "Never invent calendar events or candidate details. "
        "Understand follow-up messages using conversation history. "

        # Date and timezone
        "Use Europe/Berlin as the default timezone. "
        f"Today's date is {today}. "
        "Convert interview times into ISO 8601 format "
        "with the correct timezone offset. "

        # Working hours
        "Interview working days are Monday through Friday. "
        "Working hours are 09:00 to 17:00 Europe/Berlin. "
        "Do not schedule interviews on weekends. "
        "Do not schedule interviews outside working hours. "
        "If a requested time is invalid, ask for another time. "
        "Never silently change the requested date or time. "

        # Required details
        "Before scheduling an interview, collect the "
        "candidate's full name, email address, job role, "
        "interview date, start time, and end time or duration. "
        "If any required detail is missing, ask the user. "
        "Never invent candidate names, email addresses, "
        "job roles, dates, or meeting links. "

        # Interview duration
        "If the user does not specify a duration, "
        "use 45 minutes as the default interview duration. "

        # Tool behavior
        "Use create_calendar_event to schedule interviews. "
        "The create_calendar_event tool automatically generates "
        "the professional invitation message. "
        "Do not generate a second invitation message. "
        "Leave the description parameter empty. "
        "Do not duplicate greetings, interview details, "
        "or HR signatures. "

        # Approval
        "The calendar tool pauses for human approval. "
        "Wait for the user to approve or reject the invitation. "
        "Never bypass the human approval process. "

        # Calendar conflicts
        "Do not intentionally schedule overlapping interviews. "
        "If the calendar tool reports a scheduling conflict, "
        "inform the user and ask for another time. "

        # Accurate reporting
        "Never claim an invitation was delivered merely "
        "because Google Calendar accepted the event request. "
        "Report only confirmed tool results. "

        # Tone
        "Be professional, clear, and helpful. "
        "Ask concise follow-up questions when necessary. "
    )
)
