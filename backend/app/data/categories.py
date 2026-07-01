"""Category taxonomy and content — 24 categories across Track A (code) and Track B (non-code).

Phase 1 launch categories (full curriculum + resources): FE, BE, UX, GD, DM, VA, VE, CS.
All others ship with a "coming soon" placeholder per the PRD's phased rollout strategy,
while scoring/routing works identically for all 24 categories from day one.
"""

PHASE_1_CATEGORIES = {"FE", "BE", "UX", "GD", "DM", "VA", "VE", "CS"}

CATEGORIES = {
    # ---------------- Track A — Code-Based (11) ----------------
    "FE": {
        "name": "Frontend Development",
        "track": "A",
        "focus": "Building the visual, interactive parts of websites and apps that users see and click.",
        "duration": "3–5 months",
        "curriculum": [
            "Phase 1: HTML, CSS, and responsive layout fundamentals",
            "Phase 2: JavaScript fundamentals and DOM manipulation",
            "Phase 3: A modern framework (React) and component-based thinking",
            "Phase 4: Version control (Git/GitHub) and deploying a real portfolio project",
        ],
        "resources": [
            "freeCodeCamp — Responsive Web Design & JavaScript certifications",
            "The Odin Project — Full-Stack JavaScript path",
            "Kevin Powell (YouTube) — CSS deep dives",
        ],
    },
    "BE": {
        "name": "Backend Development",
        "track": "A",
        "focus": "Building the server-side logic, databases, and APIs that power applications.",
        "duration": "4–6 months",
        "curriculum": [
            "Phase 1: A core language (Python or JavaScript) and programming fundamentals",
            "Phase 2: Building REST APIs (FastAPI, Django, or Express)",
            "Phase 3: Databases — relational (PostgreSQL/SQLite) and query design",
            "Phase 4: Authentication, deployment, and building a full backend project",
        ],
        "resources": [
            "freeCodeCamp — Backend Development & APIs certification",
            "Official FastAPI / Django documentation",
            "Corey Schafer (YouTube) — Python & Django tutorials",
        ],
    },
    "FS": {
        "name": "Full-Stack Development",
        "track": "A",
        "focus": "Combining frontend and backend skills to build complete, end-to-end applications.",
        "duration": "6–9 months",
    },
    "MOB": {
        "name": "Mobile App Development",
        "track": "A",
        "focus": "Building applications for iOS and Android using native or cross-platform tools.",
        "duration": "4–6 months",
    },
    "DO": {
        "name": "DevOps & Cloud Engineering",
        "track": "A",
        "focus": "Automating deployment, managing infrastructure, and keeping systems running reliably.",
        "duration": "5–7 months",
    },
    "CS": {
        "name": "Cybersecurity",
        "track": "A",
        "focus": "Protecting systems, networks, and data from unauthorised access and attacks.",
        "duration": "5–8 months",
        "curriculum": [
            "Phase 1: Networking and operating systems fundamentals",
            "Phase 2: Security fundamentals — CIA triad, common attack types",
            "Phase 3: Hands-on practice with vulnerable systems (labs)",
            "Phase 4: Specialising — penetration testing, SOC analysis, or GRC",
        ],
        "resources": [
            "TryHackMe — beginner-friendly hands-on labs",
            "CompTIA Security+ study materials",
            "Cybrary — free foundational courses",
        ],
    },
    "DA": {
        "name": "Data Analysis & Data Science",
        "track": "A",
        "focus": "Extracting insight from data to support decisions, using statistics and visualisation.",
        "duration": "4–6 months",
    },
    "AI": {
        "name": "AI / Machine Learning",
        "track": "A",
        "focus": "Building systems that learn patterns from data to make predictions or automate decisions.",
        "duration": "6–9 months",
    },
    "GM": {
        "name": "Game Development",
        "track": "A",
        "focus": "Designing and building interactive games for PC, mobile, or console.",
        "duration": "5–8 months",
    },
    "QA": {
        "name": "QA / Software Testing",
        "track": "A",
        "focus": "Ensuring software works correctly through manual and automated testing.",
        "duration": "3–5 months",
    },
    "BC": {
        "name": "Blockchain / Web3 Development",
        "track": "A",
        "focus": "Building decentralised applications and smart contracts on blockchain networks.",
        "duration": "5–7 months",
    },
    # ---------------- Track B — Non-Coding (13) ----------------
    "UX": {
        "name": "UI/UX Design",
        "track": "B",
        "focus": "Designing digital products that are both visually appealing and easy to use.",
        "duration": "3–5 months",
        "curriculum": [
            "Phase 1: Design fundamentals — colour, typography, layout",
            "Phase 2: User research and wireframing",
            "Phase 3: Prototyping in Figma",
            "Phase 4: Building a complete case-study portfolio project",
        ],
        "resources": [
            "Google UX Design Certificate (Coursera)",
            "Figma official tutorials and community files",
            "Dribbble & Behance — for studying real design work",
        ],
    },
    "GD": {
        "name": "Graphic Design",
        "track": "B",
        "focus": "Creating visual content — logos, branding, social graphics, and print material.",
        "duration": "2–4 months",
        "curriculum": [
            "Phase 1: Design principles and colour theory",
            "Phase 2: Tools — Canva for beginners, Adobe Illustrator/Photoshop for depth",
            "Phase 3: Branding and typography fundamentals",
            "Phase 4: Building a client-ready design portfolio",
        ],
        "resources": [
            "Canva Design School — free courses",
            "Adobe official tutorials",
            "Skillshare — graphic design classes",
        ],
    },
    "VE": {
        "name": "Video Editing",
        "track": "B",
        "focus": "Editing raw footage into polished videos for content, marketing, or film.",
        "duration": "2–4 months",
        "curriculum": [
            "Phase 1: Editing fundamentals — cuts, transitions, pacing",
            "Phase 2: A core tool (CapCut, Premiere Pro, or DaVinci Resolve)",
            "Phase 3: Colour grading and audio syncing",
            "Phase 4: Editing a portfolio reel across different content styles",
        ],
        "resources": [
            "YouTube Creator Academy — free official training",
            "DaVinci Resolve official tutorials (free software)",
            "Peter McKinnon (YouTube) — practical editing tips",
        ],
    },
    "MG": {
        "name": "Motion Graphics & Animation",
        "track": "B",
        "focus": "Creating animated visuals — explainer videos, kinetic typography, animated logos.",
        "duration": "3–5 months",
    },
    "VA": {
        "name": "Virtual Assistance",
        "track": "B",
        "focus": "Providing remote administrative, scheduling, and organisational support to businesses.",
        "duration": "1–3 months",
        "curriculum": [
            "Phase 1: Core tools — Google Workspace, calendar and email management",
            "Phase 2: Communication and client management skills",
            "Phase 3: Task and project tools (Trello, Notion, Asana)",
            "Phase 4: Building a service package and finding first clients",
        ],
        "resources": [
            "HubSpot Academy — free business and admin courses",
            "Google Workspace official training",
            "Udemy — Virtual Assistant foundational courses",
        ],
    },
    "DM": {
        "name": "Digital Marketing",
        "track": "B",
        "focus": "Promoting products and brands through online channels — ads, email, and content.",
        "duration": "2–4 months",
        "curriculum": [
            "Phase 1: Digital marketing fundamentals and funnels",
            "Phase 2: Paid advertising basics (Meta and Google Ads)",
            "Phase 3: Email marketing and content strategy",
            "Phase 4: Running a real small campaign as a portfolio piece",
        ],
        "resources": [
            "Google Digital Garage — free certification",
            "HubSpot Academy — Digital Marketing course",
            "Meta Blueprint — official Meta ads training",
        ],
    },
    "SM": {
        "name": "Social Media Management",
        "track": "B",
        "focus": "Planning, creating, and managing content and engagement across social platforms.",
        "duration": "1–3 months",
    },
    "CW": {
        "name": "Content Writing & Copywriting",
        "track": "B",
        "focus": "Writing persuasive or informative content for blogs, ads, and marketing.",
        "duration": "1–3 months",
    },
    "SEO": {
        "name": "SEO (Search Engine Optimisation)",
        "track": "B",
        "focus": "Improving how websites rank on search engines to drive organic traffic.",
        "duration": "2–3 months",
    },
    "PM": {
        "name": "Technical Project Management",
        "track": "B",
        "focus": "Planning, coordinating, and delivering tech projects on time and within scope.",
        "duration": "2–4 months",
    },
    "TW": {
        "name": "Technical Writing",
        "track": "B",
        "focus": "Writing clear documentation, guides, and manuals for technical products.",
        "duration": "2–3 months",
    },
    "EC": {
        "name": "E-commerce Management",
        "track": "B",
        "focus": "Running and growing online stores — from setup to marketing to fulfilment.",
        "duration": "2–4 months",
    },
    "IT": {
        "name": "IT Support / Technical Support",
        "track": "B",
        "focus": "Helping people and organisations resolve technical issues and maintain systems.",
        "duration": "2–4 months",
    },
}


def is_phase_1(category_key: str) -> bool:
    return category_key in PHASE_1_CATEGORIES


def get_category(category_key: str) -> dict:
    data = CATEGORIES[category_key]
    return {
        "key": category_key,
        "name": data["name"],
        "track": data["track"],
        "focus": data["focus"],
        "duration": data["duration"],
        "phase_1": is_phase_1(category_key),
        "curriculum": data.get("curriculum"),
        "resources": data.get("resources"),
    }
