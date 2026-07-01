"""Question Bank v2.0 — Global Digital Skills Assessment.

Structure:
  Section 1 (Orientation): 8 questions, every user answers these. Scores six
  dimensions (CD, NC, CR, LG, PP, DT) used to route to Track A or Track B.

  Section 2A (Track A Deep-Dive): 12 questions, scores the 11 Track A categories.
  Section 2B (Track B Deep-Dive): 13 questions, scores the 13 Track B categories.
"""

TRACK_A_CATEGORIES = ["FE", "BE", "FS", "MOB", "DO", "CS", "DA", "AI", "GM", "QA", "BC"]
TRACK_B_CATEGORIES = ["UX", "GD", "VE", "MG", "VA", "DM", "SM", "CW", "SEO", "PM", "TW", "EC", "IT"]

ORIENTATION_QUESTIONS = [
    {
        "id": "orientation_q1",
        "text": "When you imagine your ideal workday, which sounds most appealing?",
        "options": {
            "A": {"text": "Sitting with code, solving a technical puzzle undisturbed", "scores": {"CD": 4, "NC": 0, "CR": 0, "LG": 3, "PP": 0, "DT": 0}},
            "B": {"text": "Designing or creating something visually engaging", "scores": {"CD": 0, "NC": 3, "CR": 4, "LG": 0, "PP": 0, "DT": 0}},
            "C": {"text": "Talking to clients or coordinating a team to get things done", "scores": {"CD": 0, "NC": 3, "CR": 0, "LG": 0, "PP": 4, "DT": 0}},
            "D": {"text": "Digging through numbers to find a pattern or insight", "scores": {"CD": 0, "NC": 2, "CR": 0, "LG": 2, "PP": 0, "DT": 4}},
        },
    },
    {
        "id": "orientation_q2",
        "text": "Which statement is closest to how you feel about learning new digital tools?",
        "options": {
            "A": {"text": "I want to understand exactly how it works underneath, not just use it", "scores": {"CD": 4, "NC": 0, "CR": 0, "LG": 3, "PP": 0, "DT": 0}},
            "B": {"text": "I want to use it to create something visually appealing quickly", "scores": {"CD": 0, "NC": 3, "CR": 4, "LG": 0, "PP": 0, "DT": 0}},
            "C": {"text": "I want to use it to communicate with or manage people better", "scores": {"CD": 0, "NC": 3, "CR": 0, "LG": 0, "PP": 4, "DT": 0}},
            "D": {"text": "I want to use it to analyse information and make better decisions", "scores": {"CD": 0, "NC": 2, "CR": 0, "LG": 0, "PP": 0, "DT": 4}},
        },
    },
    {
        "id": "orientation_q3",
        "text": "Which of these small projects would you pick first, given the choice?",
        "options": {
            "A": {"text": "Build a simple working app or automate a repetitive task", "scores": {"CD": 4, "NC": 0, "CR": 0, "LG": 2, "PP": 0, "DT": 0}},
            "B": {"text": "Design a logo, poster, or short video", "scores": {"CD": 0, "NC": 3, "CR": 4, "LG": 0, "PP": 0, "DT": 0}},
            "C": {"text": "Write a persuasive post or manage a social media page", "scores": {"CD": 0, "NC": 3, "CR": 0, "LG": 0, "PP": 3, "DT": 0}},
            "D": {"text": "Analyse a spreadsheet of sales data and summarise the findings", "scores": {"CD": 0, "NC": 2, "CR": 0, "LG": 2, "PP": 0, "DT": 4}},
        },
    },
    {
        "id": "orientation_q4",
        "text": "How do you feel about writing code specifically?",
        "options": {
            "A": {"text": "Excited — I want to learn to write code and understand programming logic", "scores": {"CD": 4, "NC": 0, "CR": 0, "LG": 3, "PP": 0, "DT": 0}},
            "B": {"text": "Neutral — I could learn it, but it isn't what excites me", "scores": {"CD": 1, "NC": 2, "CR": 0, "LG": 0, "PP": 0, "DT": 0}},
            "C": {"text": "Not interested — I'd rather build skills that don't require writing code", "scores": {"CD": 0, "NC": 4, "CR": 0, "LG": 0, "PP": 0, "DT": 0}},
            "D": {"text": "Curious but cautious — I'd try it if guided step by step", "scores": {"CD": 2, "NC": 2, "CR": 0, "LG": 1, "PP": 0, "DT": 0}},
        },
    },
    {
        "id": "orientation_q5",
        "text": "Which environment would you thrive in?",
        "options": {
            "A": {"text": "Deep focus, working through complex logical problems alone", "scores": {"CD": 4, "NC": 0, "CR": 0, "LG": 4, "PP": 0, "DT": 0}},
            "B": {"text": "A creative studio, bouncing ideas around visually", "scores": {"CD": 0, "NC": 3, "CR": 4, "LG": 0, "PP": 0, "DT": 0}},
            "C": {"text": "Client-facing, constantly communicating and coordinating", "scores": {"CD": 0, "NC": 3, "CR": 0, "LG": 0, "PP": 4, "DT": 0}},
            "D": {"text": "Research-driven, working with data and drawing conclusions", "scores": {"CD": 0, "NC": 2, "CR": 0, "LG": 0, "PP": 0, "DT": 4}},
        },
    },
    {
        "id": "orientation_q6",
        "text": "Which of these frustrates you the most?",
        "options": {
            "A": {"text": "Vague instructions with no clear structure or logic", "scores": {"CD": 2, "NC": 0, "CR": 0, "LG": 3, "PP": 0, "DT": 0}},
            "B": {"text": "Ugly, poorly designed visuals or interfaces", "scores": {"CD": 0, "NC": 2, "CR": 4, "LG": 0, "PP": 0, "DT": 0}},
            "C": {"text": "Poor communication or disorganised teams", "scores": {"CD": 0, "NC": 2, "CR": 0, "LG": 0, "PP": 4, "DT": 0}},
            "D": {"text": "Decisions made without looking at the data", "scores": {"CD": 0, "NC": 2, "CR": 0, "LG": 0, "PP": 0, "DT": 4}},
        },
    },
    {
        "id": "orientation_q7",
        "text": "If you had to describe your strength to a stranger in one sentence, which is closest?",
        "options": {
            "A": {"text": "“I'm good at figuring out how systems and logic work”", "scores": {"CD": 3, "NC": 0, "CR": 0, "LG": 4, "PP": 0, "DT": 0}},
            "B": {"text": "“I have a good eye for how things look and feel”", "scores": {"CD": 0, "NC": 2, "CR": 4, "LG": 0, "PP": 0, "DT": 0}},
            "C": {"text": "“I'm good with people and getting things organised”", "scores": {"CD": 0, "NC": 2, "CR": 0, "LG": 0, "PP": 4, "DT": 0}},
            "D": {"text": "“I'm good at making sense of information”", "scores": {"CD": 0, "NC": 1, "CR": 0, "LG": 0, "PP": 0, "DT": 4}},
        },
    },
    {
        "id": "orientation_q8",
        "text": "Which of these would you rather spend the next year mastering?",
        "options": {
            "A": {"text": "A programming language and how to build with it", "scores": {"CD": 4, "NC": 0, "CR": 0, "LG": 2, "PP": 0, "DT": 0}},
            "B": {"text": "A design tool and visual storytelling", "scores": {"CD": 0, "NC": 3, "CR": 4, "LG": 0, "PP": 0, "DT": 0}},
            "C": {"text": "Marketing, communication, or people-management skills", "scores": {"CD": 0, "NC": 3, "CR": 0, "LG": 0, "PP": 4, "DT": 0}},
            "D": {"text": "Data tools and analytical thinking", "scores": {"CD": 0, "NC": 2, "CR": 0, "LG": 1, "PP": 0, "DT": 4}},
        },
    },
]

TRACK_A_QUESTIONS = [
    {
        "id": "trackA_q1",
        "text": "Which type of application would you most enjoy building?",
        "options": {
            "A": {"text": "A visually rich, interactive web interface", "scores": {"FE": 4, "BE": 0, "FS": 2, "MOB": 1, "DO": 0, "CS": 0, "DA": 0, "AI": 0, "GM": 0, "QA": 0, "BC": 0}},
            "B": {"text": "A backend system that powers multiple apps", "scores": {"FE": 0, "BE": 4, "FS": 2, "MOB": 0, "DO": 0, "CS": 0, "DA": 0, "AI": 0, "GM": 0, "QA": 0, "BC": 1}},
            "C": {"text": "A mobile app for Android or iOS", "scores": {"FE": 1, "BE": 0, "FS": 1, "MOB": 4, "DO": 0, "CS": 0, "DA": 0, "AI": 0, "GM": 0, "QA": 0, "BC": 0}},
            "D": {"text": "An automated pipeline that deploys and monitors software", "scores": {"FE": 0, "BE": 1, "FS": 0, "MOB": 0, "DO": 4, "CS": 0, "DA": 0, "AI": 0, "GM": 0, "QA": 0, "BC": 0}},
        },
    },
    {
        "id": "trackA_q2",
        "text": "Which excites you more?",
        "options": {
            "A": {"text": "Making sure an app works identically across many devices and screens", "scores": {"FE": 3, "BE": 0, "FS": 0, "MOB": 4, "DO": 0, "CS": 0, "DA": 0, "AI": 0, "GM": 0, "QA": 0, "BC": 0}},
            "B": {"text": "Designing how data is stored and retrieved efficiently", "scores": {"FE": 0, "BE": 4, "FS": 0, "MOB": 0, "DO": 0, "CS": 0, "DA": 2, "AI": 0, "GM": 0, "QA": 0, "BC": 0}},
            "C": {"text": "Setting up systems that catch bugs before they reach users", "scores": {"FE": 0, "BE": 0, "FS": 0, "MOB": 0, "DO": 1, "CS": 0, "DA": 0, "AI": 0, "GM": 0, "QA": 4, "BC": 0}},
            "D": {"text": "Building smart contracts or decentralised apps", "scores": {"FE": 0, "BE": 1, "FS": 0, "MOB": 0, "DO": 0, "CS": 0, "DA": 0, "AI": 0, "GM": 0, "QA": 0, "BC": 4}},
        },
    },
    {
        "id": "trackA_q3",
        "text": "If a system goes down at 2am, which reaction sounds like you?",
        "options": {
            "A": {"text": "I want to trace exactly which server or deployment caused it", "scores": {"FE": 0, "BE": 1, "FS": 0, "MOB": 0, "DO": 4, "CS": 0, "DA": 0, "AI": 0, "GM": 0, "QA": 0, "BC": 0}},
            "B": {"text": "I want to check if it was a malicious attack", "scores": {"FE": 0, "BE": 0, "FS": 0, "MOB": 0, "DO": 1, "CS": 4, "DA": 0, "AI": 0, "GM": 0, "QA": 0, "BC": 0}},
            "C": {"text": "I want to check if a recent code change introduced a bug", "scores": {"FE": 0, "BE": 2, "FS": 0, "MOB": 0, "DO": 0, "CS": 0, "DA": 0, "AI": 0, "GM": 0, "QA": 4, "BC": 0}},
            "D": {"text": "I'm not that drawn to this scenario — I'd rather build something new", "scores": {"FE": 2, "BE": 0, "FS": 2, "MOB": 2, "DO": 0, "CS": 0, "DA": 0, "AI": 0, "GM": 0, "QA": 0, "BC": 0}},
        },
    },
    {
        "id": "trackA_q4",
        "text": "Which topic would you rather read an article about?",
        "options": {
            "A": {"text": "How to design clean, well-structured REST APIs", "scores": {"FE": 0, "BE": 4, "FS": 2, "MOB": 0, "DO": 0, "CS": 0, "DA": 0, "AI": 0, "GM": 0, "QA": 0, "BC": 0}},
            "B": {"text": "How attackers exploit poorly secured systems", "scores": {"FE": 0, "BE": 0, "FS": 0, "MOB": 0, "DO": 0, "CS": 4, "DA": 0, "AI": 0, "GM": 0, "QA": 0, "BC": 0}},
            "C": {"text": "How neural networks learn to recognise images", "scores": {"FE": 0, "BE": 0, "FS": 0, "MOB": 0, "DO": 0, "CS": 0, "DA": 2, "AI": 4, "GM": 0, "QA": 0, "BC": 0}},
            "D": {"text": "How blockchain consensus mechanisms actually work", "scores": {"FE": 0, "BE": 0, "FS": 0, "MOB": 0, "DO": 0, "CS": 0, "DA": 0, "AI": 0, "GM": 0, "QA": 0, "BC": 4}},
        },
    },
    {
        "id": "trackA_q5",
        "text": "Which skill sounds most satisfying to master?",
        "options": {
            "A": {"text": "Making an interface feel fast and smooth for users", "scores": {"FE": 4, "BE": 0, "FS": 0, "MOB": 2, "DO": 0, "CS": 0, "DA": 0, "AI": 0, "GM": 0, "QA": 0, "BC": 0}},
            "B": {"text": "Writing algorithms that learn from data", "scores": {"FE": 0, "BE": 0, "FS": 0, "MOB": 0, "DO": 0, "CS": 0, "DA": 2, "AI": 4, "GM": 0, "QA": 0, "BC": 0}},
            "C": {"text": "Automating infrastructure so deployments never fail", "scores": {"FE": 0, "BE": 0, "FS": 0, "MOB": 0, "DO": 4, "CS": 0, "DA": 0, "AI": 0, "GM": 0, "QA": 0, "BC": 0}},
            "D": {"text": "Finding and reporting vulnerabilities before attackers do", "scores": {"FE": 0, "BE": 0, "FS": 0, "MOB": 0, "DO": 0, "CS": 4, "DA": 0, "AI": 0, "GM": 0, "QA": 1, "BC": 0}},
        },
    },
    {
        "id": "trackA_q6",
        "text": "Which project would you be proudest to finish?",
        "options": {
            "A": {"text": "A polished mobile app published on an app store", "scores": {"FE": 1, "BE": 0, "FS": 0, "MOB": 4, "DO": 0, "CS": 0, "DA": 0, "AI": 0, "GM": 0, "QA": 0, "BC": 0}},
            "B": {"text": "A prediction model or trading bot that actually works", "scores": {"FE": 0, "BE": 0, "FS": 0, "MOB": 0, "DO": 0, "CS": 0, "DA": 3, "AI": 4, "GM": 0, "QA": 0, "BC": 0}},
            "C": {"text": "A game that real people enjoy playing", "scores": {"FE": 0, "BE": 0, "FS": 0, "MOB": 0, "DO": 0, "CS": 0, "DA": 0, "AI": 0, "GM": 4, "QA": 0, "BC": 0}},
            "D": {"text": "A smart contract deployed on a live blockchain network", "scores": {"FE": 0, "BE": 0, "FS": 0, "MOB": 0, "DO": 0, "CS": 0, "DA": 0, "AI": 0, "GM": 0, "QA": 0, "BC": 4}},
        },
    },
    {
        "id": "trackA_q7",
        "text": "What kind of thinking feels most natural to you?",
        "options": {
            "A": {"text": "Visual and spatial — imagining how screens and interactions flow", "scores": {"FE": 4, "BE": 0, "FS": 0, "MOB": 2, "DO": 0, "CS": 0, "DA": 0, "AI": 0, "GM": 2, "QA": 0, "BC": 0}},
            "B": {"text": "Structural — imagining how data and logic connect behind the scenes", "scores": {"FE": 0, "BE": 4, "FS": 3, "MOB": 0, "DO": 0, "CS": 0, "DA": 0, "AI": 0, "GM": 0, "QA": 0, "BC": 0}},
            "C": {"text": "Adversarial — imagining how something could be broken into", "scores": {"FE": 0, "BE": 0, "FS": 0, "MOB": 0, "DO": 0, "CS": 4, "DA": 0, "AI": 0, "GM": 0, "QA": 2, "BC": 0}},
            "D": {"text": "Statistical — imagining patterns and probabilities within data", "scores": {"FE": 0, "BE": 0, "FS": 0, "MOB": 0, "DO": 0, "CS": 0, "DA": 4, "AI": 3, "GM": 0, "QA": 0, "BC": 0}},
        },
    },
    {
        "id": "trackA_q8",
        "text": "Which excites you more: building something brand new, or making sure something existing never fails?",
        "options": {
            "A": {"text": "Building something completely new and creative", "scores": {"FE": 1, "BE": 0, "FS": 0, "MOB": 2, "DO": 0, "CS": 0, "DA": 0, "AI": 0, "GM": 4, "QA": 0, "BC": 0}},
            "B": {"text": "Making sure existing systems run without failure", "scores": {"FE": 0, "BE": 0, "FS": 0, "MOB": 0, "DO": 4, "CS": 0, "DA": 0, "AI": 0, "GM": 0, "QA": 2, "BC": 0}},
            "C": {"text": "Making sure existing systems are secure from attack", "scores": {"FE": 0, "BE": 0, "FS": 0, "MOB": 0, "DO": 0, "CS": 4, "DA": 0, "AI": 0, "GM": 0, "QA": 0, "BC": 0}},
            "D": {"text": "Making sure existing systems make accurate predictions", "scores": {"FE": 0, "BE": 0, "FS": 0, "MOB": 0, "DO": 0, "CS": 0, "DA": 4, "AI": 3, "GM": 0, "QA": 0, "BC": 0}},
        },
    },
    {
        "id": "trackA_q9",
        "text": "Which of these types of software have you personally been curious about?",
        "options": {
            "A": {"text": "Video games", "scores": {"FE": 0, "BE": 0, "FS": 0, "MOB": 0, "DO": 0, "CS": 0, "DA": 0, "AI": 0, "GM": 4, "QA": 0, "BC": 0}},
            "B": {"text": "The apps you use on your phone every day", "scores": {"FE": 1, "BE": 0, "FS": 0, "MOB": 4, "DO": 0, "CS": 0, "DA": 0, "AI": 0, "GM": 0, "QA": 0, "BC": 0}},
            "C": {"text": "The systems banks or crypto exchanges use to process transactions", "scores": {"FE": 0, "BE": 0, "FS": 0, "MOB": 0, "DO": 0, "CS": 1, "DA": 0, "AI": 0, "GM": 0, "QA": 0, "BC": 4}},
            "D": {"text": "Recommendation systems, like how Netflix suggests shows", "scores": {"FE": 0, "BE": 0, "FS": 0, "MOB": 0, "DO": 0, "CS": 0, "DA": 3, "AI": 4, "GM": 0, "QA": 0, "BC": 0}},
        },
    },
    {
        "id": "trackA_q10",
        "text": "When testing something you built, what do you naturally focus on?",
        "options": {
            "A": {"text": "Whether it looks and feels right to a user", "scores": {"FE": 3, "BE": 0, "FS": 0, "MOB": 2, "DO": 0, "CS": 0, "DA": 0, "AI": 0, "GM": 0, "QA": 0, "BC": 0}},
            "B": {"text": "Whether it handles unexpected or edge-case inputs correctly", "scores": {"FE": 0, "BE": 2, "FS": 0, "MOB": 0, "DO": 0, "CS": 0, "DA": 0, "AI": 0, "GM": 0, "QA": 4, "BC": 0}},
            "C": {"text": "Whether someone could exploit it maliciously", "scores": {"FE": 0, "BE": 0, "FS": 0, "MOB": 0, "DO": 0, "CS": 4, "DA": 0, "AI": 0, "GM": 0, "QA": 0, "BC": 0}},
            "D": {"text": "Whether the underlying logic and data are structured correctly", "scores": {"FE": 0, "BE": 3, "FS": 2, "MOB": 0, "DO": 0, "CS": 0, "DA": 2, "AI": 0, "GM": 0, "QA": 0, "BC": 0}},
        },
    },
    {
        "id": "trackA_q11",
        "text": "Which of these career descriptions excites you most?",
        "options": {
            "A": {"text": "“I build interfaces used by millions of people daily”", "scores": {"FE": 4, "BE": 0, "FS": 0, "MOB": 1, "DO": 0, "CS": 0, "DA": 0, "AI": 0, "GM": 0, "QA": 0, "BC": 0}},
            "B": {"text": "“I make sure the internet's infrastructure never goes down”", "scores": {"FE": 0, "BE": 0, "FS": 0, "MOB": 0, "DO": 4, "CS": 0, "DA": 0, "AI": 0, "GM": 0, "QA": 0, "BC": 0}},
            "C": {"text": "“I hunt for security flaws before criminals find them”", "scores": {"FE": 0, "BE": 0, "FS": 0, "MOB": 0, "DO": 0, "CS": 4, "DA": 0, "AI": 0, "GM": 0, "QA": 0, "BC": 0}},
            "D": {"text": "“I build AI models that solve real-world problems”", "scores": {"FE": 0, "BE": 0, "FS": 0, "MOB": 0, "DO": 0, "CS": 0, "DA": 1, "AI": 4, "GM": 0, "QA": 0, "BC": 0}},
        },
    },
    {
        "id": "trackA_q12",
        "text": "If you had unlimited free time for a hobby project, what would you build?",
        "options": {
            "A": {"text": "A small mobile game", "scores": {"FE": 0, "BE": 0, "FS": 0, "MOB": 2, "DO": 0, "CS": 0, "DA": 0, "AI": 0, "GM": 4, "QA": 0, "BC": 0}},
            "B": {"text": "A personal API or backend for a project idea", "scores": {"FE": 0, "BE": 4, "FS": 2, "MOB": 0, "DO": 0, "CS": 0, "DA": 0, "AI": 0, "GM": 0, "QA": 0, "BC": 0}},
            "C": {"text": "A home lab to practise ethical hacking", "scores": {"FE": 0, "BE": 0, "FS": 0, "MOB": 0, "DO": 0, "CS": 4, "DA": 0, "AI": 0, "GM": 0, "QA": 0, "BC": 0}},
            "D": {"text": "A decentralised app on a blockchain testnet", "scores": {"FE": 0, "BE": 1, "FS": 0, "MOB": 0, "DO": 0, "CS": 0, "DA": 0, "AI": 0, "GM": 0, "QA": 0, "BC": 4}},
        },
    },
]

TRACK_B_QUESTIONS = [
    {
        "id": "trackB_q1",
        "text": "Which task would you enjoy most?",
        "options": {
            "A": {"text": "Designing how an app's screens should look and flow", "scores": {"UX": 4, "GD": 2, "VE": 0, "MG": 0, "VA": 0, "DM": 0, "SM": 0, "CW": 0, "SEO": 0, "PM": 0, "TW": 0, "EC": 0, "IT": 0}},
            "B": {"text": "Creating a logo or brand visuals from scratch", "scores": {"UX": 1, "GD": 4, "VE": 0, "MG": 0, "VA": 0, "DM": 0, "SM": 0, "CW": 0, "SEO": 0, "PM": 0, "TW": 0, "EC": 0, "IT": 0}},
            "C": {"text": "Editing raw video footage into a polished final cut", "scores": {"UX": 0, "GD": 0, "VE": 4, "MG": 1, "VA": 0, "DM": 0, "SM": 0, "CW": 0, "SEO": 0, "PM": 0, "TW": 0, "EC": 0, "IT": 0}},
            "D": {"text": "Managing someone's email, calendar, and daily tasks", "scores": {"UX": 0, "GD": 0, "VE": 0, "MG": 0, "VA": 4, "DM": 0, "SM": 0, "CW": 0, "SEO": 0, "PM": 0, "TW": 0, "EC": 0, "IT": 0}},
        },
    },
    {
        "id": "trackB_q2",
        "text": "Which of these would you rather be responsible for?",
        "options": {
            "A": {"text": "Making sure a product is easy and intuitive to use", "scores": {"UX": 4, "GD": 0, "VE": 0, "MG": 0, "VA": 0, "DM": 0, "SM": 0, "CW": 0, "SEO": 0, "PM": 0, "TW": 0, "EC": 0, "IT": 0}},
            "B": {"text": "Making sure a brand looks consistent everywhere", "scores": {"UX": 0, "GD": 4, "VE": 0, "MG": 0, "VA": 0, "DM": 0, "SM": 0, "CW": 0, "SEO": 0, "PM": 0, "TW": 0, "EC": 0, "IT": 0}},
            "C": {"text": "Making sure a video tells a compelling story", "scores": {"UX": 0, "GD": 0, "VE": 4, "MG": 2, "VA": 0, "DM": 0, "SM": 0, "CW": 0, "SEO": 0, "PM": 0, "TW": 0, "EC": 0, "IT": 0}},
            "D": {"text": "Making sure a client's online store runs smoothly", "scores": {"UX": 0, "GD": 0, "VE": 0, "MG": 0, "VA": 1, "DM": 0, "SM": 0, "CW": 0, "SEO": 0, "PM": 0, "TW": 0, "EC": 4, "IT": 0}},
        },
    },
    {
        "id": "trackB_q3",
        "text": "Which type of content creation excites you?",
        "options": {
            "A": {"text": "Writing blog posts or ad copy that persuades people to act", "scores": {"UX": 0, "GD": 0, "VE": 0, "MG": 0, "VA": 0, "DM": 2, "SM": 0, "CW": 4, "SEO": 0, "PM": 0, "TW": 0, "EC": 0, "IT": 0}},
            "B": {"text": "Creating short animated clips or motion graphics", "scores": {"UX": 0, "GD": 0, "VE": 2, "MG": 4, "VA": 0, "DM": 0, "SM": 0, "CW": 0, "SEO": 0, "PM": 0, "TW": 0, "EC": 0, "IT": 0}},
            "C": {"text": "Planning what to post and when across social platforms", "scores": {"UX": 0, "GD": 0, "VE": 0, "MG": 0, "VA": 0, "DM": 1, "SM": 4, "CW": 0, "SEO": 0, "PM": 0, "TW": 0, "EC": 0, "IT": 0}},
            "D": {"text": "Writing clear, step-by-step guides for a product", "scores": {"UX": 0, "GD": 0, "VE": 0, "MG": 0, "VA": 0, "DM": 0, "SM": 0, "CW": 0, "SEO": 0, "PM": 0, "TW": 4, "EC": 0, "IT": 0}},
        },
    },
    {
        "id": "trackB_q4",
        "text": "Which of these problems would you enjoy solving?",
        "options": {
            "A": {"text": "“Why isn't this website showing up on Google?”", "scores": {"UX": 0, "GD": 0, "VE": 0, "MG": 0, "VA": 0, "DM": 1, "SM": 0, "CW": 0, "SEO": 4, "PM": 0, "TW": 0, "EC": 0, "IT": 0}},
            "B": {"text": "“Why isn't this ad campaign converting?”", "scores": {"UX": 0, "GD": 0, "VE": 0, "MG": 0, "VA": 0, "DM": 4, "SM": 0, "CW": 0, "SEO": 1, "PM": 0, "TW": 0, "EC": 0, "IT": 0}},
            "C": {"text": "“Why isn't this project on schedule?”", "scores": {"UX": 0, "GD": 0, "VE": 0, "MG": 0, "VA": 0, "DM": 0, "SM": 0, "CW": 0, "SEO": 0, "PM": 4, "TW": 0, "EC": 0, "IT": 0}},
            "D": {"text": "“Why hasn't this customer's technical issue been resolved yet?”", "scores": {"UX": 0, "GD": 0, "VE": 0, "MG": 0, "VA": 1, "DM": 0, "SM": 0, "CW": 0, "SEO": 0, "PM": 0, "TW": 0, "EC": 0, "IT": 4}},
        },
    },
    {
        "id": "trackB_q5",
        "text": "Which of these tasks feels most natural to you?",
        "options": {
            "A": {"text": "Organising a messy schedule into something clear and manageable", "scores": {"UX": 0, "GD": 0, "VE": 0, "MG": 0, "VA": 4, "DM": 0, "SM": 0, "CW": 0, "SEO": 0, "PM": 2, "TW": 0, "EC": 0, "IT": 0}},
            "B": {"text": "Making a rough idea look professional and polished visually", "scores": {"UX": 1, "GD": 4, "VE": 0, "MG": 0, "VA": 0, "DM": 0, "SM": 0, "CW": 0, "SEO": 0, "PM": 0, "TW": 0, "EC": 0, "IT": 0}},
            "C": {"text": "Explaining a technical process in plain, simple language", "scores": {"UX": 0, "GD": 0, "VE": 0, "MG": 0, "VA": 0, "DM": 0, "SM": 0, "CW": 1, "SEO": 0, "PM": 0, "TW": 4, "EC": 0, "IT": 0}},
            "D": {"text": "Troubleshooting why someone's computer or software isn't working", "scores": {"UX": 0, "GD": 0, "VE": 0, "MG": 0, "VA": 0, "DM": 0, "SM": 0, "CW": 0, "SEO": 0, "PM": 0, "TW": 0, "EC": 0, "IT": 4}},
        },
    },
    {
        "id": "trackB_q6",
        "text": "If you ran a small business's online presence for a month, what would you focus on first?",
        "options": {
            "A": {"text": "Making the website easier and more pleasant to use", "scores": {"UX": 4, "GD": 0, "VE": 0, "MG": 0, "VA": 0, "DM": 0, "SM": 0, "CW": 0, "SEO": 0, "PM": 0, "TW": 0, "EC": 0, "IT": 0}},
            "B": {"text": "Making the social media pages more active and engaging", "scores": {"UX": 0, "GD": 0, "VE": 0, "MG": 0, "VA": 0, "DM": 1, "SM": 4, "CW": 0, "SEO": 0, "PM": 0, "TW": 0, "EC": 0, "IT": 0}},
            "C": {"text": "Making sure people can actually find the business on Google", "scores": {"UX": 0, "GD": 0, "VE": 0, "MG": 0, "VA": 0, "DM": 0, "SM": 0, "CW": 0, "SEO": 4, "PM": 0, "TW": 0, "EC": 0, "IT": 0}},
            "D": {"text": "Making sure orders and products are well organised in the store", "scores": {"UX": 0, "GD": 0, "VE": 0, "MG": 0, "VA": 0, "DM": 0, "SM": 0, "CW": 0, "SEO": 0, "PM": 0, "TW": 0, "EC": 4, "IT": 0}},
        },
    },
    {
        "id": "trackB_q7",
        "text": "Which of these types of writing appeals to you most?",
        "options": {
            "A": {"text": "Persuasive ad copy designed to get people to click or buy", "scores": {"UX": 0, "GD": 0, "VE": 0, "MG": 0, "VA": 0, "DM": 2, "SM": 0, "CW": 4, "SEO": 0, "PM": 0, "TW": 0, "EC": 0, "IT": 0}},
            "B": {"text": "Clear documentation explaining how to use a tool or product", "scores": {"UX": 0, "GD": 0, "VE": 0, "MG": 0, "VA": 0, "DM": 0, "SM": 0, "CW": 0, "SEO": 0, "PM": 0, "TW": 4, "EC": 0, "IT": 0}},
            "C": {"text": "Engaging captions and posts for social media", "scores": {"UX": 0, "GD": 0, "VE": 0, "MG": 0, "VA": 0, "DM": 0, "SM": 3, "CW": 2, "SEO": 0, "PM": 0, "TW": 0, "EC": 0, "IT": 0}},
            "D": {"text": "None of these — I'd rather work visually or organisationally", "scores": {"UX": 0, "GD": 2, "VE": 0, "MG": 0, "VA": 2, "DM": 0, "SM": 0, "CW": 0, "SEO": 0, "PM": 0, "TW": 0, "EC": 0, "IT": 0}},
        },
    },
    {
        "id": "trackB_q8",
        "text": "Which skill would you rather spend the next few months mastering?",
        "options": {
            "A": {"text": "Video editing software and storytelling techniques", "scores": {"UX": 0, "GD": 0, "VE": 4, "MG": 1, "VA": 0, "DM": 0, "SM": 0, "CW": 0, "SEO": 0, "PM": 0, "TW": 0, "EC": 0, "IT": 0}},
            "B": {"text": "Project management tools and methodologies", "scores": {"UX": 0, "GD": 0, "VE": 0, "MG": 0, "VA": 0, "DM": 0, "SM": 0, "CW": 0, "SEO": 0, "PM": 4, "TW": 0, "EC": 0, "IT": 0}},
            "C": {"text": "Search engine optimisation and campaign analytics", "scores": {"UX": 0, "GD": 0, "VE": 0, "MG": 0, "VA": 0, "DM": 1, "SM": 0, "CW": 0, "SEO": 4, "PM": 0, "TW": 0, "EC": 0, "IT": 0}},
            "D": {"text": "Customer support tools and troubleshooting techniques", "scores": {"UX": 0, "GD": 0, "VE": 0, "MG": 0, "VA": 1, "DM": 0, "SM": 0, "CW": 0, "SEO": 0, "PM": 0, "TW": 0, "EC": 0, "IT": 4}},
        },
    },
    {
        "id": "trackB_q9",
        "text": "Which of these achievements would make you proudest?",
        "options": {
            "A": {"text": "A brand identity you designed being used across a real business", "scores": {"UX": 1, "GD": 4, "VE": 0, "MG": 0, "VA": 0, "DM": 0, "SM": 0, "CW": 0, "SEO": 0, "PM": 0, "TW": 0, "EC": 0, "IT": 0}},
            "B": {"text": "A video you edited being widely watched and shared", "scores": {"UX": 0, "GD": 0, "VE": 4, "MG": 1, "VA": 0, "DM": 0, "SM": 0, "CW": 0, "SEO": 0, "PM": 0, "TW": 0, "EC": 0, "IT": 0}},
            "C": {"text": "A marketing campaign you ran leading to real sales growth", "scores": {"UX": 0, "GD": 0, "VE": 0, "MG": 0, "VA": 0, "DM": 4, "SM": 0, "CW": 0, "SEO": 1, "PM": 0, "TW": 0, "EC": 0, "IT": 0}},
            "D": {"text": "A messy project you organised being delivered on time and on budget", "scores": {"UX": 0, "GD": 0, "VE": 0, "MG": 0, "VA": 1, "DM": 0, "SM": 0, "CW": 0, "SEO": 0, "PM": 4, "TW": 0, "EC": 0, "IT": 0}},
        },
    },
    {
        "id": "trackB_q10",
        "text": "Which of these working styles suits you best?",
        "options": {
            "A": {"text": "Working closely with visuals, colour, and layout all day", "scores": {"UX": 2, "GD": 4, "VE": 0, "MG": 1, "VA": 0, "DM": 0, "SM": 0, "CW": 0, "SEO": 0, "PM": 0, "TW": 0, "EC": 0, "IT": 0}},
            "B": {"text": "Working closely with people's schedules, messages, and requests", "scores": {"UX": 0, "GD": 0, "VE": 0, "MG": 0, "VA": 4, "DM": 0, "SM": 0, "CW": 0, "SEO": 0, "PM": 0, "TW": 0, "EC": 0, "IT": 0}},
            "C": {"text": "Working closely with numbers, click-through rates, and campaign data", "scores": {"UX": 0, "GD": 0, "VE": 0, "MG": 0, "VA": 0, "DM": 3, "SM": 0, "CW": 0, "SEO": 4, "PM": 0, "TW": 0, "EC": 0, "IT": 0}},
            "D": {"text": "Working closely with product listings, pricing, and store setup", "scores": {"UX": 0, "GD": 0, "VE": 0, "MG": 0, "VA": 0, "DM": 0, "SM": 0, "CW": 0, "SEO": 0, "PM": 0, "TW": 0, "EC": 4, "IT": 0}},
        },
    },
    {
        "id": "trackB_q11",
        "text": "A friend says their online store isn't making sales. What's your first instinct?",
        "options": {
            "A": {"text": "Check if the store's design and checkout flow are confusing", "scores": {"UX": 3, "GD": 0, "VE": 0, "MG": 0, "VA": 0, "DM": 0, "SM": 0, "CW": 0, "SEO": 0, "PM": 0, "TW": 0, "EC": 3, "IT": 0}},
            "B": {"text": "Check if their social media and ads are reaching the right people", "scores": {"UX": 0, "GD": 0, "VE": 0, "MG": 0, "VA": 0, "DM": 4, "SM": 2, "CW": 0, "SEO": 0, "PM": 0, "TW": 0, "EC": 0, "IT": 0}},
            "C": {"text": "Check if their product pages are optimised to appear in search results", "scores": {"UX": 0, "GD": 0, "VE": 0, "MG": 0, "VA": 0, "DM": 0, "SM": 0, "CW": 0, "SEO": 4, "PM": 0, "TW": 0, "EC": 0, "IT": 0}},
            "D": {"text": "Check if their day-to-day order and customer management is organised", "scores": {"UX": 0, "GD": 0, "VE": 0, "MG": 0, "VA": 1, "DM": 0, "SM": 0, "CW": 0, "SEO": 0, "PM": 0, "TW": 0, "EC": 4, "IT": 0}},
        },
    },
    {
        "id": "trackB_q12",
        "text": "Which of these would you enjoy teaching someone else how to do?",
        "options": {
            "A": {"text": "How to use design software to create visuals", "scores": {"UX": 1, "GD": 4, "VE": 0, "MG": 0, "VA": 0, "DM": 0, "SM": 0, "CW": 0, "SEO": 0, "PM": 0, "TW": 0, "EC": 0, "IT": 0}},
            "B": {"text": "How to edit and export a professional-looking video", "scores": {"UX": 0, "GD": 0, "VE": 4, "MG": 2, "VA": 0, "DM": 0, "SM": 0, "CW": 0, "SEO": 0, "PM": 0, "TW": 0, "EC": 0, "IT": 0}},
            "C": {"text": "How to write clear instructions for using a product", "scores": {"UX": 0, "GD": 0, "VE": 0, "MG": 0, "VA": 0, "DM": 0, "SM": 0, "CW": 0, "SEO": 0, "PM": 0, "TW": 4, "EC": 0, "IT": 0}},
            "D": {"text": "How to manage their tasks and inbox more efficiently", "scores": {"UX": 0, "GD": 0, "VE": 0, "MG": 0, "VA": 4, "DM": 0, "SM": 0, "CW": 0, "SEO": 0, "PM": 1, "TW": 0, "EC": 0, "IT": 0}},
        },
    },
    {
        "id": "trackB_q13",
        "text": "Which of these best describes the kind of impact you want to have?",
        "options": {
            "A": {"text": "Making digital products beautiful and intuitive", "scores": {"UX": 4, "GD": 2, "VE": 0, "MG": 0, "VA": 0, "DM": 0, "SM": 0, "CW": 0, "SEO": 0, "PM": 0, "TW": 0, "EC": 0, "IT": 0}},
            "B": {"text": "Making content that grabs attention and tells a story", "scores": {"UX": 0, "GD": 0, "VE": 3, "MG": 3, "VA": 0, "DM": 0, "SM": 0, "CW": 1, "SEO": 0, "PM": 0, "TW": 0, "EC": 0, "IT": 0}},
            "C": {"text": "Making sure businesses are found, organised, and running efficiently", "scores": {"UX": 0, "GD": 0, "VE": 0, "MG": 0, "VA": 2, "DM": 0, "SM": 0, "CW": 0, "SEO": 2, "PM": 2, "TW": 0, "EC": 2, "IT": 0}},
            "D": {"text": "Making sure people get fast, patient help when technology confuses them", "scores": {"UX": 0, "GD": 0, "VE": 0, "MG": 0, "VA": 0, "DM": 0, "SM": 0, "CW": 0, "SEO": 0, "PM": 0, "TW": 0, "EC": 0, "IT": 4}},
        },
    },
]
