"""Comprehensive Question Bank — 88 items across 5 question types.

Source: Comprehensive_Question_Bank_Psychometric.docx. Measures 24 competencies
(see competencies.py); competency totals are projected onto the 70-career space
via the derived mapping matrix built in career_matrix.py from the
"careers_influenced" hints attached to each question/option below.

Users are not required to answer every question — scoring.py normalizes each
competency by the maximum achievable score from only the questions actually
answered, so partial completion still produces a fair, comparable profile.
"""

# ---------------------------------------------------------------------------
# Section A — Likert-Scale Statements (Q1-Q35), rated 1 (strongly disagree)
# to 5 (strongly agree). Rating multiplies directly against competency weights.
# ---------------------------------------------------------------------------
LIKERT_QUESTIONS = [
    {"id": "likert_q1", "text": "I enjoy breaking a complicated problem into smaller, logical steps.",
     "competencies": {"LR": 5, "SYS": 3}, "careers_influenced": ["BWD", "DS", "CYB", "SA", "BA"]},
    {"id": "likert_q2", "text": "I often find myself double-checking my work for small mistakes others might miss.",
     "competencies": {"DET": 5, "ORG": 3}, "careers_influenced": ["QA", "DBA", "DE", "TW", "DAN"]},
    {"id": "likert_q3", "text": "I like imagining how something could look or feel before it exists.",
     "competencies": {"CR": 5, "VT": 4}, "careers_influenced": ["UX", "PDS", "GD", "MG", "ANI"]},
    {"id": "likert_q4", "text": "I would rather work through a problem alone than in a group discussion.",
     "competencies": {"IND": 4}, "careers_influenced": ["BWD", "DE", "SR", "ETH", "DS"]},
    {"id": "likert_q5", "text": "I enjoy explaining things to people who don't understand a topic yet.",
     "competencies": {"TEACH": 5, "COM": 3}, "careers_influenced": ["TT", "ID", "TS", "ITS", "TR"]},
    {"id": "likert_q6", "text": "I get excited when I discover a new tool, app, or piece of technology.",
     "competencies": {"TCUR": 5, "CUR": 4}, "careers_influenced": ["AIA", "AAD", "PE", "NCD", "LCD"]},
    {"id": "likert_q7", "text": "I like persuading people to see things from my point of view.",
     "competencies": {"COM": 4, "BUS": 2}, "careers_influenced": ["DM", "CPW", "BD", "TSL", "PM"]},
    {"id": "likert_q8", "text": "I feel comfortable taking the lead when a group has no clear direction.",
     "competencies": {"LEAD": 5}, "careers_influenced": ["PM", "PJM", "BD", "TEN", "SA"]},
    {"id": "likert_q9", "text": "I enjoy spotting patterns in numbers or data that others might overlook.",
     "competencies": {"NR": 5, "ANA": 4}, "careers_influenced": ["DAN", "DS", "BI", "DE", "ML"]},
    {"id": "likert_q10", "text": "I would rather fix something that's broken than build something new.",
     "competencies": {"PER": 3, "DET": 3}, "careers_influenced": ["QA", "ITS", "TS", "SYSA", "NET"]},
    {"id": "likert_q11", "text": "I like coming up with original ideas, even if they seem unconventional.",
     "competencies": {"CR": 5, "INNOV": 4}, "careers_influenced": ["GD", "MG", "ANI", "TEN", "AIC"]},
    {"id": "likert_q12", "text": "I feel a strong urge to understand exactly how something works internally.",
     "competencies": {"SYS": 5, "TCUR": 4}, "careers_influenced": ["ESD", "IOT", "ROB", "ETH", "SA"]},
    {"id": "likert_q13", "text": "I enjoy writing in a way that makes complicated ideas simple for readers.",
     "competencies": {"WR": 5, "TEACH": 3}, "careers_influenced": ["TW", "CW", "ID", "CPW", "MR"]},
    {"id": "likert_q14", "text": "I prefer situations with a clear plan over ones that are open-ended.",
     "competencies": {"ORG": 5}, "careers_influenced": ["PJM", "ERP", "CRM", "DBA", "QA"]},
    {"id": "likert_q15", "text": "I find it easy to notice how someone else might be feeling, even if they don't say it.",
     "competencies": {"EMP": 5, "COM": 3}, "careers_influenced": ["UXR", "CSU", "ID", "TR", "TS"]},
    {"id": "likert_q16", "text": "I like researching a topic deeply before forming an opinion about it.",
     "competencies": {"RES": 5, "CUR": 3}, "careers_influenced": ["MR", "UXR", "SR", "DS", "BA"]},
    {"id": "likert_q17", "text": "I'm comfortable making a decision even without having all the information.",
     "competencies": {"RISK": 4, "ADAPT": 3}, "careers_influenced": ["TEN", "BD", "PM", "TSL", "AIC"]},
    {"id": "likert_q18", "text": "I enjoy visually organising information — charts, diagrams, layouts.",
     "competencies": {"VT": 5, "ORG": 3}, "careers_influenced": ["UX", "PDS", "GIS", "BI", "DAN"]},
    {"id": "likert_q19", "text": "I like the idea of starting something of my own rather than joining something existing.",
     "competencies": {"ENTP": 5, "RISK": 3}, "careers_influenced": ["TEN", "ITC", "AIC", "BD", "TT"]},
    {"id": "likert_q20", "text": "I enjoy working with numbers and calculations more than words or images.",
     "competencies": {"NR": 5}, "careers_influenced": ["DAN", "DE", "BI", "ERP", "DS"]},
    {"id": "likert_q21", "text": "I would rather troubleshoot a technical issue than write a report about it.",
     "competencies": {"SYS": 4, "PER": 3}, "careers_influenced": ["ITS", "TS", "NET", "SYSA", "QA"]},
    {"id": "likert_q22", "text": "I enjoy collaborating closely with a team rather than working independently most of the time.",
     "competencies": {"COLLAB": 5}, "careers_influenced": ["PJM", "PM", "CM", "TR", "BD"]},
    {"id": "likert_q23", "text": "I like designing things that are both attractive and easy to use.",
     "competencies": {"CR": 4, "VT": 4}, "careers_influenced": ["UX", "PDS", "GD", "MG", "WP"]},
    {"id": "likert_q24", "text": "I get satisfaction from optimizing a process to make it faster or more efficient.",
     "competencies": {"SYS": 4, "BUS": 3}, "careers_influenced": ["DVO", "BA", "BI", "ERP", "CLD"]},
    {"id": "likert_q25", "text": "I enjoy keeping track of many small details across a long project.",
     "competencies": {"DET": 5, "ORG": 4}, "careers_influenced": ["PJM", "QA", "DBA", "ERP", "CRM"]},
    {"id": "likert_q26", "text": "I like exploring how businesses make money and grow.",
     "competencies": {"BUS": 5}, "careers_influenced": ["BD", "PM", "BA", "TEN", "MR"]},
    {"id": "likert_q27", "text": "I would rather write persuasive content than technical documentation.",
     "competencies": {"WR": 4, "COM": 4}, "careers_influenced": ["CPW", "DM", "EM", "SMM", "CM"]},
    {"id": "likert_q28", "text": "I enjoy adapting quickly when plans change unexpectedly.",
     "competencies": {"ADAPT": 5}, "careers_influenced": ["TEN", "PJM", "CSU", "TS", "BD"]},
    {"id": "likert_q29", "text": "I like the challenge of trying to secure or break into a system (ethically).",
     "competencies": {"SYS": 4, "RISK": 3}, "careers_influenced": ["CYB", "ETH", "SR", "NET", "CLD"]},
    {"id": "likert_q30", "text": "I enjoy mentoring or guiding someone through learning a new skill.",
     "competencies": {"TEACH": 5, "EMP": 3}, "careers_influenced": ["TT", "ID", "TR", "CSU", "TS"]},
    {"id": "likert_q31", "text": "I like using visual storytelling — video, animation, motion — to communicate ideas.",
     "competencies": {"CR": 5, "VT": 4}, "careers_influenced": ["VE", "MG", "ANI", "3DD", "GD"]},
    {"id": "likert_q32", "text": "I enjoy identifying inefficiencies in how a team or company operates.",
     "competencies": {"BUS": 4, "ANA": 3}, "careers_influenced": ["BA", "PM", "ERP", "CRM", "BI"]},
    {"id": "likert_q33", "text": "I like automating repetitive tasks so I never have to do them manually again.",
     "competencies": {"SYS": 4, "TCUR": 4}, "careers_influenced": ["AIA", "DVO", "NCD", "LCD", "AAD"]},
    {"id": "likert_q34", "text": "I enjoy following up with people to make sure they're satisfied with what they received.",
     "competencies": {"EMP": 4, "COM": 4}, "careers_influenced": ["CSU", "ITS", "TS", "CM", "VA"]},
    {"id": "likert_q35", "text": "I like keeping up with the latest developments in artificial intelligence.",
     "competencies": {"TCUR": 5, "CUR": 4}, "careers_influenced": ["AI", "ML", "AIA", "AAD", "PE"]},
]

# ---------------------------------------------------------------------------
# Section B — Forced-Choice (Q1-Q20). Only the chosen option's weights score.
# ---------------------------------------------------------------------------
FORCED_CHOICE_QUESTIONS = [
    {"id": "fc_q1", "text": "Which activity would you enjoy more?", "options": {
        "A": {"text": "Debugging why a program crashes", "competencies": {"SYS": 4, "PER": 3}, "careers_influenced": ["BWD", "QA", "NET"]},
        "B": {"text": "Designing a poster for an event", "competencies": {"CR": 4, "VT": 4}, "careers_influenced": ["GD", "MG", "UX"]}}},
    {"id": "fc_q2", "text": "Which role sounds more appealing?", "options": {
        "A": {"text": "Analysing survey data to find hidden trends", "competencies": {"NR": 4, "ANA": 4}, "careers_influenced": ["DAN", "DS", "BI"]},
        "B": {"text": "Presenting those findings to a room of executives", "competencies": {"COM": 5, "LEAD": 3}, "careers_influenced": ["BA", "PM", "MR"]}}},
    {"id": "fc_q3", "text": "Which would you rather do?", "options": {
        "A": {"text": "Write the technical manual for a new app", "competencies": {"WR": 4, "DET": 3}, "careers_influenced": ["TW", "ID"]},
        "B": {"text": "Write the marketing copy that sells the same app", "competencies": {"WR": 4, "COM": 4}, "careers_influenced": ["CPW", "DM", "CW"]}}},
    {"id": "fc_q4", "text": "Which sounds more like you?", "options": {
        "A": {"text": "Building a robot that performs a physical task", "competencies": {"SYS": 4, "TCUR": 4}, "careers_influenced": ["ROB", "ESD", "IOT"]},
        "B": {"text": "Building software that predicts what that robot should do next", "competencies": {"NR": 4, "ANA": 4}, "careers_influenced": ["AI", "ML", "DS"]}}},
    {"id": "fc_q5", "text": "Pick one.", "options": {
        "A": {"text": "Managing a team's sprint and deadlines", "competencies": {"LEAD": 4, "ORG": 4}, "careers_influenced": ["PJM", "PM"]},
        "B": {"text": "Writing the actual code the team ships", "competencies": {"SYS": 4, "TCUR": 3}, "careers_influenced": ["BWD", "FSD", "FWD"]}}},
    {"id": "fc_q6", "text": "Which excites you more?", "options": {
        "A": {"text": "Finding a security hole before attackers do", "competencies": {"SYS": 4, "RISK": 3}, "careers_influenced": ["CYB", "ETH", "SR"]},
        "B": {"text": "Building the cloud servers the app runs on", "hint": "\"Cloud\" just means renting computers over the internet (like the ones behind Netflix or Instagram) instead of owning physical machines.", "competencies": {"SYS": 4, "TCUR": 3}, "careers_influenced": ["CLD", "DVO", "SA"]}}},
    {"id": "fc_q7", "text": "Which task would you volunteer for?", "options": {
        "A": {"text": "Interviewing users to learn what frustrates them about an app", "competencies": {"EMP": 4, "RES": 4}, "careers_influenced": ["UXR", "MR"]},
        "B": {"text": "Redesigning the app based on that feedback", "competencies": {"CR": 4, "VT": 4}, "careers_influenced": ["UX", "PDS"]}}},
    {"id": "fc_q8", "text": "Choose one.", "options": {
        "A": {"text": "Setting up a company's email marketing automation", "competencies": {"ORG": 3, "BUS": 3}, "careers_influenced": ["EM", "DM"]},
        "B": {"text": "Growing a brand's social media following organically", "competencies": {"CR": 3, "COM": 4}, "careers_influenced": ["SMM", "CM"]}}},
    {"id": "fc_q9", "text": "Which would you rather be known for?", "options": {
        "A": {"text": "Being the person who always finds the bug no one else can find", "competencies": {"DET": 5, "PER": 4}, "careers_influenced": ["QA", "SR"]},
        "B": {"text": "Being the person who always has a creative idea no one else thought of", "competencies": {"CR": 5, "INNOV": 4}, "careers_influenced": ["GD", "MG", "TEN"]}}},
    {"id": "fc_q10", "text": "Pick one.", "options": {
        "A": {"text": "Setting up databases so information is well organized", "hint": "A database is just an organized digital filing system — like a giant, searchable spreadsheet.", "competencies": {"ORG": 4, "DET": 4}, "careers_influenced": ["DBA", "DE"]},
        "B": {"text": "Setting up dashboards so people can see that information visually", "hint": "A dashboard is a screen of charts and summaries at a glance — like a car dashboard, but for data.", "competencies": {"VT": 4, "ANA": 3}, "careers_influenced": ["BI", "DAN"]}}},
    {"id": "fc_q11", "text": "Which sounds better?", "options": {
        "A": {"text": "Selling a technical product to a business client", "competencies": {"COM": 4, "BUS": 3}, "careers_influenced": ["TSL", "BD"]},
        "B": {"text": "Supporting that same client after they've bought it", "competencies": {"EMP": 4, "COM": 3}, "careers_influenced": ["CSU", "TS", "ITS"]}}},
    {"id": "fc_q12", "text": "Choose one.", "options": {
        "A": {"text": "Building a chatbot that automatically answers customer questions", "competencies": {"TCUR": 4, "SYS": 3}, "careers_influenced": ["AAD", "AIA", "PE"]},
        "B": {"text": "Writing the actual conversation scripts the chatbot uses", "competencies": {"WR": 4, "EMP": 3}, "careers_influenced": ["PE", "ID", "CW"]}}},
    {"id": "fc_q13", "text": "Which would you rather do?", "options": {
        "A": {"text": "Build a business website from scratch using code", "competencies": {"SYS": 4, "TCUR": 3}, "careers_influenced": ["FWD", "FSD", "WP"]},
        "B": {"text": "Build the same website using a no-code tool", "hint": "A \"no-code tool\" lets you build a working website by dragging and dropping, like building with LEGO instead of writing instructions from scratch.", "competencies": {"ORG": 3, "BUS": 3}, "careers_influenced": ["NCD", "LCD", "WP"]}}},
    {"id": "fc_q14", "text": "Pick one.", "options": {
        "A": {"text": "Mapping out where things are located using geographic data", "hint": "Think Google Maps, but layered with extra data — like which neighbourhoods have the most deliveries.", "competencies": {"ANA": 4, "VT": 3}, "careers_influenced": ["GIS", "DAN"]},
        "B": {"text": "Mapping out how a business's internal processes flow", "competencies": {"BUS": 4, "ORG": 3}, "careers_influenced": ["BA", "ERP", "CRM"]}}},
    {"id": "fc_q15", "text": "Which excites you more?", "options": {
        "A": {"text": "Training an AI model on a dataset", "hint": "This means showing a computer program thousands of examples (a \"dataset\") so it learns to recognise patterns on its own — like showing it 1,000 cat photos so it learns what a cat looks like.", "competencies": {"NR": 4, "ANA": 4}, "careers_influenced": ["ML", "AI", "DS"]},
        "B": {"text": "Writing clear prompts to get useful answers from an existing AI model", "competencies": {"WR": 3, "CUR": 4}, "careers_influenced": ["PE", "AAD", "AIC"]}}},
    {"id": "fc_q16", "text": "Choose one.", "options": {
        "A": {"text": "Recruiting and interviewing candidates for tech roles", "competencies": {"COM": 4, "EMP": 3}, "careers_influenced": ["TR"]},
        "B": {"text": "Actually doing the tech role yourself", "competencies": {"TCUR": 4, "SYS": 3}, "careers_influenced": ["FSD", "BWD", "DVO"]}}},
    {"id": "fc_q17", "text": "Which is more you?", "options": {
        "A": {"text": "Editing raw video footage into a polished, final story", "competencies": {"VT": 4, "CR": 3}, "careers_influenced": ["VE"]},
        "B": {"text": "Designing the 3D models and animations that go inside that video", "competencies": {"VT": 5, "CR": 4}, "careers_influenced": ["3DD", "ANI", "MG"]}}},
    {"id": "fc_q18", "text": "Pick one.", "options": {
        "A": {"text": "Advising a company on their overall IT strategy", "competencies": {"BUS": 4, "COM": 3}, "careers_influenced": ["ITC", "AIC", "SA"]},
        "B": {"text": "Actually implementing that strategy hands-on", "competencies": {"SYS": 4, "TCUR": 3}, "careers_influenced": ["DVO", "CLD", "NET"]}}},
    {"id": "fc_q19", "text": "Which sounds more satisfying?", "options": {
        "A": {"text": "Designing the curriculum that teaches people a new skill", "competencies": {"ORG": 4, "CR": 3}, "careers_influenced": ["ID"]},
        "B": {"text": "Actually standing in front of people teaching it", "competencies": {"TEACH": 5, "COM": 4}, "careers_influenced": ["TT", "TR"]}}},
    {"id": "fc_q20", "text": "Choose one.", "options": {
        "A": {"text": "Managing someone's calendar, inbox, and daily admin tasks remotely", "competencies": {"ORG": 4, "COLLAB": 3}, "careers_influenced": ["VA", "MOF"]},
        "B": {"text": "Managing a company's customer database and CRM system", "hint": "A CRM is just software that keeps track of a company's customers and conversations with them — think of it as a very organized contacts app for a whole business.", "competencies": {"ORG": 4, "DET": 4}, "careers_influenced": ["CRM", "ERP"]}}},
]

# ---------------------------------------------------------------------------
# Section C — Scenario-Based (Q1-Q15). Pick the closest natural reaction.
# ---------------------------------------------------------------------------
SCENARIO_QUESTIONS = [
    {"id": "scenario_q1", "text": "A laptop suddenly won't turn on, and the owner needs it working before a meeting in an hour. What do you do first?", "options": {
        "A": {"text": "Methodically check each possible cause, one at a time", "competencies": {"DET": 4, "PER": 3}, "careers_influenced": ["ITS", "TS", "NET"]},
        "B": {"text": "Look up the exact error online and follow a tested fix", "competencies": {"RES": 4, "ADAPT": 3}, "careers_influenced": ["ITS", "TS"]},
        "C": {"text": "Reassure the owner while you work, keeping them calm", "competencies": {"EMP": 4, "COM": 3}, "careers_influenced": ["CSU", "ITS"]},
        "D": {"text": "Suggest a backup plan while you continue troubleshooting", "competencies": {"ADAPT": 4, "BUS": 2}, "careers_influenced": ["TS", "CSU"]}}},
    {"id": "scenario_q2", "text": "A client says they 'just want the website to look better' with no specifics. What's your first move?", "options": {
        "A": {"text": "Ask detailed questions to understand what 'better' means to them", "competencies": {"COM": 4, "RES": 3}, "careers_influenced": ["UXR", "UX"]},
        "B": {"text": "Show them three visual mockups and let them react", "competencies": {"CR": 4, "VT": 4}, "careers_influenced": ["GD", "UX", "PDS"]},
        "C": {"text": "Look at competitor websites for inspiration first", "competencies": {"RES": 4, "CUR": 3}, "careers_influenced": ["MR", "UXR"]},
        "D": {"text": "Just start redesigning based on your own best judgment", "competencies": {"IND": 4, "CR": 3}, "careers_influenced": ["GD", "UX"]}}},
    {"id": "scenario_q3", "text": "You notice a spreadsheet of sales numbers has a pattern no one else has mentioned. What do you do?", "options": {
        "A": {"text": "Dig deeper into the data to confirm the pattern is real", "competencies": {"ANA": 5, "DET": 4}, "careers_influenced": ["DAN", "DS", "BI"]},
        "B": {"text": "Immediately tell your manager what you found", "competencies": {"COM": 4, "BUS": 3}, "careers_influenced": ["BA", "PM"]},
        "C": {"text": "Build a chart or dashboard to show the pattern clearly", "competencies": {"VT": 4, "ANA": 3}, "careers_influenced": ["BI", "DAN"]},
        "D": {"text": "Wonder if there's a way to automate detecting patterns like this", "competencies": {"TCUR": 4, "SYS": 3}, "careers_influenced": ["AI", "ML", "AIA"]}}},
    {"id": "scenario_q4", "text": "Your team's project is behind schedule and everyone is stressed. What's your instinct?", "options": {
        "A": {"text": "Reorganise the task list and deadlines to get back on track", "competencies": {"ORG": 5, "LEAD": 4}, "careers_influenced": ["PJM", "PM"]},
        "B": {"text": "Check in with each team member to see how they're coping", "competencies": {"EMP": 4, "COLLAB": 3}, "careers_influenced": ["PM", "CSU", "TR"]},
        "C": {"text": "Dive into the technical work yourself to speed things up", "competencies": {"TCUR": 4, "PER": 3}, "careers_influenced": ["BWD", "FWD", "FSD"]},
        "D": {"text": "Step back and question whether the plan itself needs to change", "competencies": {"ADAPT": 4, "INNOV": 3}, "careers_influenced": ["TEN", "BA"]}}},
    {"id": "scenario_q5", "text": "You're asked to write about a technical product for engineers and for everyday customers. Which do you enjoy more?", "options": {
        "A": {"text": "Writing precisely and technically for the engineers", "competencies": {"WR": 4, "DET": 4}, "careers_influenced": ["TW"]},
        "B": {"text": "Writing simply and persuasively for the customers", "competencies": {"WR": 4, "COM": 4}, "careers_influenced": ["CW", "CPW", "DM"]},
        "C": {"text": "Both equally, translating between the two", "competencies": {"WR": 4, "TEACH": 3}, "careers_influenced": ["TW", "ID"]},
        "D": {"text": "Neither — I'd rather build the product than describe it", "competencies": {"TCUR": 4}, "careers_influenced": ["FSD", "BWD"]}}},
    {"id": "scenario_q6", "text": "You're testing a new mobile app before launch. What's your natural approach?", "options": {
        "A": {"text": "Try to break it in every possible way you can imagine", "competencies": {"PER": 5, "DET": 4}, "careers_influenced": ["QA", "SR", "ETH"]},
        "B": {"text": "Focus on whether it feels intuitive and pleasant to use", "competencies": {"VT": 4, "EMP": 3}, "careers_influenced": ["UX", "UXR"]},
        "C": {"text": "Check whether it performs well under heavy load", "hint": "\"Heavy load\" means lots of people using the app at the exact same time, like a shopping app on Black Friday.", "competencies": {"SYS": 4, "ANA": 3}, "careers_influenced": ["DVO", "CLD"]},
        "D": {"text": "Check whether user data is being handled securely", "competencies": {"SYS": 4, "RISK": 3}, "careers_influenced": ["CYB", "ETH"]}}},
    {"id": "scenario_q7", "text": "A small business owner wants more online customers, on a tight budget. What do you suggest first?", "options": {
        "A": {"text": "Improve their visibility on Google search results", "competencies": {"RES": 4, "ANA": 3}, "careers_influenced": ["SEO"]},
        "B": {"text": "Run a small, targeted social media campaign", "competencies": {"CR": 3, "COM": 4}, "careers_influenced": ["SMM", "DM"]},
        "C": {"text": "Set up an email list to stay in touch with existing customers", "competencies": {"ORG": 4, "BUS": 3}, "careers_influenced": ["EM", "DM"]},
        "D": {"text": "Redesign their website so visitors convert into customers more easily", "competencies": {"VT": 4, "CR": 3}, "careers_influenced": ["UX", "PDS"]}}},
    {"id": "scenario_q8", "text": "You're exploring public data on traffic accidents in a city. What draws you in?", "options": {
        "A": {"text": "Mapping where accidents cluster geographically", "competencies": {"VT": 4, "ANA": 4}, "careers_influenced": ["GIS", "DAN"]},
        "B": {"text": "Finding statistical patterns in when and why they happen", "competencies": {"NR": 5, "ANA": 4}, "careers_influenced": ["DAN", "DS", "BI"]},
        "C": {"text": "Thinking about how a system could predict and prevent them", "competencies": {"TCUR": 4, "SYS": 4}, "careers_influenced": ["AI", "ML"]},
        "D": {"text": "Writing a report explaining the findings to city officials", "competencies": {"WR": 4, "COM": 3}, "careers_influenced": ["TW", "BA"]}}},
    {"id": "scenario_q9", "text": "You've built a small tool that automates a task you used to do manually. What's your next thought?", "options": {
        "A": {"text": "How can I make this handle more edge cases?", "competencies": {"DET": 4, "PER": 3}, "careers_influenced": ["AIA", "DVO"]},
        "B": {"text": "Could other people use this too?", "competencies": {"BUS": 4, "ENTP": 3}, "careers_influenced": ["TEN", "NCD"]},
        "C": {"text": "Can I teach someone else to build something like this?", "competencies": {"TEACH": 4, "COM": 3}, "careers_influenced": ["TT", "ID"]},
        "D": {"text": "What else can I automate next?", "competencies": {"CUR": 4, "TCUR": 4}, "careers_influenced": ["AIA", "AAD"]}}},
    {"id": "scenario_q10", "text": "During a group project, a disagreement breaks out about which approach to take. What role do you naturally play?", "options": {
        "A": {"text": "The mediator, helping both sides understand each other", "competencies": {"EMP": 4, "COM": 4}, "careers_influenced": ["PM", "TR"]},
        "B": {"text": "The decision-maker, picking a direction so the team can move forward", "competencies": {"LEAD": 5}, "careers_influenced": ["PM", "PJM"]},
        "C": {"text": "The researcher, gathering evidence to settle the debate objectively", "competencies": {"RES": 4, "ANA": 3}, "careers_influenced": ["BA", "MR"]},
        "D": {"text": "The quiet one, waiting to see what's decided before contributing", "competencies": {"IND": 4}, "careers_influenced": ["BWD", "DS"]}}},
    {"id": "scenario_q11", "text": "A friend asks you to help set up their online store. What part interests you most?", "options": {
        "A": {"text": "Making sure products are well organised and easy to find", "competencies": {"ORG": 4, "DET": 3}, "careers_influenced": ["NCD", "WP", "ERP"]},
        "B": {"text": "Designing how the store looks and feels", "competencies": {"CR": 4, "VT": 4}, "careers_influenced": ["UX", "GD"]},
        "C": {"text": "Making sure the store shows up when people search for similar products", "competencies": {"RES": 3, "ANA": 3}, "careers_influenced": ["SEO"]},
        "D": {"text": "Setting up the backend so payments and inventory work correctly", "hint": "The \"backend\" is everything happening behind the scenes that customers never see — like the system that actually processes a payment when you click \"Buy.\"", "competencies": {"SYS": 4, "DET": 3}, "careers_influenced": ["BWD", "DBA"]}}},
    {"id": "scenario_q12", "text": "You're handed a messy, undocumented codebase (a large existing pile of computer code someone else wrote, with no explanation of how it works) and asked to fix a bug. What's your approach?", "options": {
        "A": {"text": "Read through methodically until you understand the structure", "competencies": {"PER": 4, "SYS": 4}, "careers_influenced": ["BWD", "QA"]},
        "B": {"text": "Search for how others have solved similar bugs before", "competencies": {"RES": 4, "ADAPT": 3}, "careers_influenced": ["ITS", "QA"]},
        "C": {"text": "Rewrite the confusing part properly while you're in there", "competencies": {"INNOV": 3, "DET": 4}, "careers_influenced": ["FSD", "SA"]},
        "D": {"text": "Document what you find so the next person doesn't struggle", "competencies": {"WR": 4, "ORG": 3}, "careers_influenced": ["TW"]}}},
    {"id": "scenario_q13", "text": "You're asked to imagine what technology will look like in 10 years. What do you focus on?", "options": {
        "A": {"text": "How AI will automate tasks humans currently do", "competencies": {"TCUR": 4, "CUR": 4}, "careers_influenced": ["AI", "AIA", "AAD"]},
        "B": {"text": "How new businesses and jobs will emerge from these changes", "competencies": {"BUS": 4, "ENTP": 3}, "careers_influenced": ["TEN", "ITC", "AIC"]},
        "C": {"text": "How people will need to be taught to use these new tools", "competencies": {"TEACH": 4, "COM": 3}, "careers_influenced": ["TT", "ID"]},
        "D": {"text": "How security risks will evolve alongside the technology", "competencies": {"RISK": 4, "SYS": 3}, "careers_influenced": ["CYB", "SR"]}}},
    {"id": "scenario_q14", "text": "You've just joined a company and don't know anyone yet. How do you settle in?", "options": {
        "A": {"text": "Focus on understanding the technical systems first", "competencies": {"TCUR": 4, "IND": 3}, "careers_influenced": ["BWD", "DVO", "SA"]},
        "B": {"text": "Focus on building relationships with your new colleagues first", "competencies": {"COLLAB": 4, "COM": 4}, "careers_influenced": ["PM", "TR", "CM"]},
        "C": {"text": "Focus on understanding how the business makes money first", "competencies": {"BUS": 4, "RES": 3}, "careers_influenced": ["BA", "PM"]},
        "D": {"text": "Focus on documenting how things currently work, for your own reference", "competencies": {"ORG": 4, "DET": 3}, "careers_influenced": ["TW", "BA"]}}},
    {"id": "scenario_q15", "text": "Which of these unsolved problems would you most want to work on?", "options": {
        "A": {"text": "Making AI models less biased and more trustworthy", "competencies": {"ANA": 4, "RISK": 3}, "careers_influenced": ["AI", "ML", "SR"]},
        "B": {"text": "Making websites accessible for people with disabilities", "competencies": {"EMP": 4, "VT": 3}, "careers_influenced": ["UX", "UXR"]},
        "C": {"text": "Making small businesses more visible online", "competencies": {"BUS": 4, "RES": 3}, "careers_influenced": ["SEO", "DM"]},
        "D": {"text": "Making complex software easier for non-technical people to use", "competencies": {"TEACH": 4, "CR": 3}, "careers_influenced": ["NCD", "LCD", "UX"]}}},
]

# ---------------------------------------------------------------------------
# Section D — Situational Judgment (Q1-Q10). Every option is descriptive,
# not evaluative — there is no "correct" answer.
# ---------------------------------------------------------------------------
SITUATIONAL_QUESTIONS = [
    {"id": "sjt_q1", "text": "Your manager gives you an ambiguous task with almost no instructions. What do you do?", "options": {
        "A": {"text": "Ask clarifying questions before starting", "competencies": {"COM": 4, "ORG": 3}, "careers_influenced": ["BA", "PM"]},
        "B": {"text": "Make reasonable assumptions and start immediately", "competencies": {"RISK": 4, "ADAPT": 3}, "careers_influenced": ["TEN", "FSD"]},
        "C": {"text": "Research how similar tasks are usually approached", "competencies": {"RES": 4, "CUR": 3}, "careers_influenced": ["MR", "UXR"]},
        "D": {"text": "Break the task into smaller pieces and tackle the clearest one first", "competencies": {"SYS": 4, "ORG": 3}, "careers_influenced": ["PJM", "BWD"]}}},
    {"id": "sjt_q2", "text": "A coworker takes credit for your idea in a meeting. What's your instinct?", "options": {
        "A": {"text": "Speak up immediately and clarify whose idea it was", "competencies": {"LEAD": 4, "COM": 4}, "careers_influenced": ["PM", "BD"]},
        "B": {"text": "Let it go this time, but raise it with them privately later", "competencies": {"EMP": 3, "COLLAB": 3}, "careers_influenced": ["TR", "CSU"]},
        "C": {"text": "Focus on making sure your next idea is even better", "competencies": {"PER": 4, "INNOV": 3}, "careers_influenced": ["TEN", "GD"]},
        "D": {"text": "Document your contributions going forward to avoid this happening again", "competencies": {"ORG": 4, "DET": 3}, "careers_influenced": ["BA", "TW"]}}},
    {"id": "sjt_q3", "text": "You realise midway through a project that your original approach won't work. What now?", "options": {
        "A": {"text": "Pivot immediately to a new approach, even if it means starting over", "competencies": {"ADAPT": 5, "RISK": 3}, "careers_influenced": ["TEN", "FSD"]},
        "B": {"text": "Analyse exactly what went wrong before deciding what to do next", "competencies": {"ANA": 4, "DET": 3}, "careers_influenced": ["QA", "BA"]},
        "C": {"text": "Ask your team or manager for input before changing direction", "competencies": {"COLLAB": 4, "COM": 3}, "careers_influenced": ["PM", "PJM"]},
        "D": {"text": "Push through with the original plan, adjusting small details as you go", "competencies": {"PER": 4, "ORG": 3}, "careers_influenced": ["DVO", "ERP"]}}},
    {"id": "sjt_q4", "text": "You're asked to present technical work to non-technical stakeholders. How do you prepare?", "options": {
        "A": {"text": "Simplify the language and focus on outcomes, not process", "competencies": {"TEACH": 4, "COM": 4}, "careers_influenced": ["TW", "BA", "PM"]},
        "B": {"text": "Prepare visuals and diagrams to make it easier to follow", "competencies": {"VT": 4, "CR": 3}, "careers_influenced": ["UX", "BI"]},
        "C": {"text": "Anticipate their questions and prepare data to back up your points", "competencies": {"ANA": 4, "RES": 3}, "careers_influenced": ["DAN", "DS"]},
        "D": {"text": "Ask a colleague to help translate the technical details", "competencies": {"COLLAB": 3, "IND": 2}, "careers_influenced": ["TR", "PM"]}}},
    {"id": "sjt_q5", "text": "You discover a critical bug the night before a major product launch. What do you do?", "options": {
        "A": {"text": "Fix it yourself immediately, even if it takes all night", "competencies": {"PER": 5, "TCUR": 4}, "careers_influenced": ["BWD", "QA", "DVO"]},
        "B": {"text": "Alert the team immediately so a decision can be made together", "competencies": {"COM": 4, "COLLAB": 3}, "careers_influenced": ["PM", "PJM"]},
        "C": {"text": "Assess how severe it really is before deciding how urgently to act", "competencies": {"ANA": 4, "RISK": 3}, "careers_influenced": ["QA", "SR"]},
        "D": {"text": "Look for a temporary workaround to buy time for a proper fix", "competencies": {"ADAPT": 4, "INNOV": 3}, "careers_influenced": ["DVO", "TS"]}}},
    {"id": "sjt_q6", "text": "A user complains that your product is confusing. What's your first reaction?", "options": {
        "A": {"text": "Ask them to walk you through exactly where they got confused", "competencies": {"EMP": 4, "RES": 3}, "careers_influenced": ["UXR", "CSU"]},
        "B": {"text": "Review the design yourself to spot the confusing part", "competencies": {"VT": 4, "DET": 3}, "careers_influenced": ["UX", "PDS"]},
        "C": {"text": "Check if other users have had the same complaint", "competencies": {"ANA": 4, "RES": 3}, "careers_influenced": ["MR", "UXR"]},
        "D": {"text": "Write clearer instructions or documentation to prevent future confusion", "competencies": {"WR": 4, "TEACH": 3}, "careers_influenced": ["TW", "ID"]}}},
    {"id": "sjt_q7", "text": "You're given two projects to choose from: one well-defined but boring, the other exciting but unclear. Which do you pick?", "options": {
        "A": {"text": "The well-defined one — I prefer clarity over excitement", "competencies": {"ORG": 4, "DET": 3}, "careers_influenced": ["DBA", "ERP", "QA"]},
        "B": {"text": "The exciting one — I'll figure out the details as I go", "competencies": {"RISK": 4, "ADAPT": 4}, "careers_influenced": ["TEN", "AIC"]},
        "C": {"text": "I'd ask for more information about the unclear one before deciding", "competencies": {"RES": 4, "COM": 3}, "careers_influenced": ["BA", "MR"]},
        "D": {"text": "I'd try to negotiate doing both, even partially", "competencies": {"COLLAB": 3, "ENTP": 3}, "careers_influenced": ["PM", "BD"]}}},
    {"id": "sjt_q8", "text": "Your work is publicly criticised online. How do you respond?", "options": {
        "A": {"text": "Ignore it and keep working", "competencies": {"IND": 4, "PER": 3}, "careers_influenced": ["BWD", "DS"]},
        "B": {"text": "Respond calmly and professionally, addressing the criticism directly", "competencies": {"COM": 4, "EMP": 3}, "careers_influenced": ["CM", "CSU"]},
        "C": {"text": "Analyse if there's a valid point you should actually fix", "competencies": {"ANA": 4, "ADAPT": 3}, "careers_influenced": ["QA", "UX"]},
        "D": {"text": "Discuss it with your team before deciding how to respond", "competencies": {"COLLAB": 4, "ORG": 3}, "careers_influenced": ["PM", "TR"]}}},
    {"id": "sjt_q9", "text": "You must choose between doing a task perfectly (but late) or acceptably (but on time). What do you choose?", "options": {
        "A": {"text": "On time — deadlines matter more than perfection", "competencies": {"ADAPT": 4, "ORG": 3}, "careers_influenced": ["PJM", "DVO"]},
        "B": {"text": "Perfect — quality matters more than speed", "competencies": {"DET": 5, "PER": 4}, "careers_influenced": ["QA", "TW", "DBA"]},
        "C": {"text": "It depends entirely on what the task is for", "competencies": {"ANA": 4, "BUS": 3}, "careers_influenced": ["BA", "PM"]},
        "D": {"text": "I'd try to negotiate a slightly later deadline to do it well", "competencies": {"COM": 3, "ORG": 3}, "careers_influenced": ["PJM", "PM"]}}},
    {"id": "sjt_q10", "text": "You're the only person on your team who understands a critical system. How does that make you feel?", "options": {
        "A": {"text": "Motivated — I like being the expert people rely on", "competencies": {"TCUR": 4, "IND": 3}, "careers_influenced": ["SA", "SR", "ETH"]},
        "B": {"text": "Uneasy — I'd want to document it so others can learn it too", "competencies": {"ORG": 4, "TEACH": 3}, "careers_influenced": ["TW", "ID"]},
        "C": {"text": "Excited to teach others so I'm not the only bottleneck", "competencies": {"TEACH": 4, "COLLAB": 3}, "careers_influenced": ["TT", "TR"]},
        "D": {"text": "Indifferent — as long as the work gets done", "competencies": {"IND": 4}, "careers_influenced": ["BWD", "SYSA"]}}},
]

# ---------------------------------------------------------------------------
# Section E — Preference Ranking (Q1-Q8). User orders 4 items most-to-least
# appealing. Rank multiplier: 1st x1.0, 2nd x0.75, 3rd x0.5, 4th x0.25.
# ---------------------------------------------------------------------------
RANKING_QUESTIONS = [
    {"id": "ranking_q1", "text": "Rank these work activities from most to least enjoyable for you:", "items": {
        "1": {"text": "Writing code", "competencies": {"SYS": 4, "TCUR": 3}, "careers_influenced": ["BWD", "FWD", "FSD"]},
        "2": {"text": "Designing visuals", "competencies": {"CR": 4, "VT": 4}, "careers_influenced": ["GD", "UX"]},
        "3": {"text": "Analysing data", "competencies": {"NR": 4, "ANA": 4}, "careers_influenced": ["DAN", "DS"]},
        "4": {"text": "Talking to people or clients", "competencies": {"COM": 4, "EMP": 3}, "careers_influenced": ["BD", "CSU"]}}},
    {"id": "ranking_q2", "text": "Rank these types of problems from most to least interesting:", "items": {
        "1": {"text": "A broken system that needs fixing", "competencies": {"SYS": 4, "PER": 3}, "careers_influenced": ["ITS", "QA", "NET"]},
        "2": {"text": "A blank page that needs an original idea", "competencies": {"CR": 4, "INNOV": 3}, "careers_influenced": ["GD", "MG", "TEN"]},
        "3": {"text": "A pile of numbers that needs interpreting", "competencies": {"NR": 4, "ANA": 4}, "careers_influenced": ["DAN", "BI", "DS"]},
        "4": {"text": "A group of people who need to be organised", "competencies": {"ORG": 4, "LEAD": 3}, "careers_influenced": ["PJM", "PM"]}}},
    {"id": "ranking_q3", "text": "Rank these work environments from most to least appealing:", "items": {
        "1": {"text": "A quiet space where you focus alone for hours", "competencies": {"IND": 4}, "careers_influenced": ["DS", "BWD", "SR"]},
        "2": {"text": "A busy space full of collaboration and conversation", "competencies": {"COLLAB": 4, "COM": 3}, "careers_influenced": ["PM", "TR", "CM"]},
        "3": {"text": "A structured space with clear routines and processes", "competencies": {"ORG": 4, "DET": 3}, "careers_influenced": ["DBA", "ERP", "QA"]},
        "4": {"text": "An unpredictable space where every day looks different", "competencies": {"ADAPT": 4, "RISK": 3}, "careers_influenced": ["TEN", "BD", "AIC"]}}},
    {"id": "ranking_q4", "text": "Rank these outcomes from most to least satisfying to achieve:", "items": {
        "1": {"text": "Something you built works flawlessly", "competencies": {"SYS": 4, "DET": 3}, "careers_influenced": ["BWD", "DVO", "QA"]},
        "2": {"text": "Something you designed looks beautiful", "competencies": {"CR": 4, "VT": 4}, "careers_influenced": ["GD", "UX", "MG"]},
        "3": {"text": "Something you explained finally makes sense to someone", "competencies": {"TEACH": 4, "COM": 3}, "careers_influenced": ["TT", "ID", "TW"]},
        "4": {"text": "Something you sold or convinced someone to do", "competencies": {"BUS": 4, "COM": 3}, "careers_influenced": ["BD", "TSL", "DM"]}}},
    {"id": "ranking_q5", "text": "Rank these skills by how much you'd enjoy mastering them:", "items": {
        "1": {"text": "Programming logic", "competencies": {"LR": 4, "SYS": 3}, "careers_influenced": ["FSD", "AI", "ML"]},
        "2": {"text": "Visual design tools", "competencies": {"CR": 4, "VT": 4}, "careers_influenced": ["UX", "GD", "MG"]},
        "3": {"text": "Statistical analysis", "competencies": {"NR": 4, "ANA": 4}, "careers_influenced": ["DAN", "DS", "BI"]},
        "4": {"text": "Public speaking and persuasion", "competencies": {"COM": 4, "LEAD": 3}, "careers_influenced": ["BD", "TSL", "TEN"]}}},
    {"id": "ranking_q6", "text": "Rank these types of recognition from most to least motivating:", "items": {
        "1": {"text": "Being known as the most technically skilled person on the team", "competencies": {"TCUR": 4, "SYS": 3}, "careers_influenced": ["SA", "CYB", "DVO"]},
        "2": {"text": "Being known as the most creative person on the team", "competencies": {"CR": 4, "INNOV": 4}, "careers_influenced": ["GD", "MG", "TEN"]},
        "3": {"text": "Being known as the most reliable, detail-oriented person on the team", "competencies": {"DET": 4, "ORG": 3}, "careers_influenced": ["QA", "DBA", "ERP"]},
        "4": {"text": "Being known as the best communicator or leader on the team", "competencies": {"COM": 4, "LEAD": 4}, "careers_influenced": ["PM", "BD", "TR"]}}},
    {"id": "ranking_q7", "text": "Rank these learning styles from most to least natural for you:", "items": {
        "1": {"text": "Reading documentation and researching independently", "competencies": {"RES": 4, "IND": 3}, "careers_influenced": ["BWD", "DS", "SR"]},
        "2": {"text": "Watching someone demonstrate, then imitating", "competencies": {"TEACH": 3, "VT": 3}, "careers_influenced": ["ID", "TT", "GD"]},
        "3": {"text": "Experimenting hands-on through trial and error", "competencies": {"ADAPT": 4, "RISK": 3}, "careers_influenced": ["TEN", "AIC", "DVO"]},
        "4": {"text": "Discussing and learning through conversation with others", "competencies": {"COM": 4, "COLLAB": 3}, "careers_influenced": ["PM", "TR", "CM"]}}},
    {"id": "ranking_q8", "text": "Rank these long-term goals by how appealing they feel to you:", "items": {
        "1": {"text": "Becoming a deep technical expert in one specific area", "competencies": {"TCUR": 4, "PER": 3}, "careers_influenced": ["SA", "CYB", "ML"]},
        "2": {"text": "Becoming a well-rounded generalist who can do many things", "competencies": {"ADAPT": 4, "CUR": 3}, "careers_influenced": ["FSD", "BA", "ITC"]},
        "3": {"text": "Becoming a leader who manages people and projects", "competencies": {"LEAD": 4, "ORG": 3}, "careers_influenced": ["PM", "PJM", "TR"]},
        "4": {"text": "Becoming an entrepreneur who builds their own thing", "competencies": {"ENTP": 4, "RISK": 3}, "careers_influenced": ["TEN", "AIC", "BD"]}}},
]
