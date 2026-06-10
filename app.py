from flask import Flask, render_template, request, jsonify
import os

_base_dir = os.path.dirname(__file__)
templates_path = os.path.join(_base_dir, "templates")
app = Flask(__name__, template_folder=templates_path)

# ── SITE DATA ──────────────────────────────────────────────────────────────────

GYM = {
    "name": "NV Fitness Time",
    "tagline": "Salt Lake's premier CrossFit & functional fitness gym",
    "rating": 4.9,
    "review_count": 160,
    "year_founded": 2020,
    "phone": "8798561817",
    "phone_raw": "8798561817",
    "address": "CK-149, CK Block, Sector II, Bidhannagar",
    "city": "Salt Lake, Kolkata – 700091",
    "whatsapp": "https://wa.me/8798561817",
    "maps_url": "https://maps.app.goo.gl/7hYfjve9MZLtZ4cE6",
    "instagram": "https://www.instagram.com/fitnesstime.nv?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw==",
}

PAGES = [
    {"nav": "Home",       "url": "/"},
    {"nav": "About",      "url": "/about"},
    {"nav": "Programs",   "url": "/programs"},
    {"nav": "Trainers",   "url": "/trainers"},
    {"nav": "Membership", "url": "/membership"},
    {"nav": "Gallery",    "url": "/gallery"},
    {"nav": "Contact",    "url": "/contact"},
]

HOURS = [
    {"day": "Monday",    "open": "6:00 AM", "close": "10:00 PM"},
    {"day": "Tuesday",   "open": "6:00 AM", "close": "10:00 PM"},
    {"day": "Wednesday", "open": "6:00 AM", "close": "10:00 PM"},
    {"day": "Thursday",  "open": "6:00 AM", "close": "10:00 PM"},
    {"day": "Friday",    "open": "6:00 AM", "close": "10:00 PM"},
    {"day": "Saturday",  "open": "6:00 AM", "close": "10:00 PM"},
    {"day": "Sunday",    "open": "6:00 AM", "close": "10:00 PM"},
]

FACILITIES = [
    {"icon": "⚡", "name": "CrossFit WODs",        "desc": "Daily workouts of the day designed for all levels. Scalable, intense, and coached every step of the way."},
    {"icon": "🏋️", "name": "Olympic Lifting",      "desc": "Full barbell setup with bumper plates and lifting platforms. Technical coaching for snatch and clean & jerk."},
    {"icon": "🤸", "name": "Functional Training",  "desc": "Gymnastics rings, pull-up bars, kettlebells, and open rig space for movement-based training."},
    {"icon": "💪", "name": "Strength Equipment",   "desc": "Squat racks, deadlift platforms, and a complete dumbbell range for classic strength work alongside CrossFit."},
    {"icon": "🥗", "name": "Nutrition Coaching",   "desc": "Personalised diet guidance from certified coaches. Fuel your performance and recovery the right way."},
    {"icon": "👥", "name": "Community Classes",    "desc": "Group WOD sessions that build camaraderie, accountability, and the push to go harder than you would alone."},
    {"icon": "🏆", "name": "Performance Tracking",  "desc": "Detailed progress monitoring, PR boards, and personalised goal-setting. Measure, track, and celebrate every victory."},
    {"icon": "⏱️", "name": "Flexible Scheduling",   "desc": "Multiple class times throughout the day to fit your lifestyle. Train before work, during lunch, or after hours."},
]

TRAINERS = [
    {
        "name": "Nikhil Verma",
        "role": "Head Coach",
        "speciality": "CrossFit & Olympic Weightlifting",
        "since": 2020,
        "emoji": "⚡",
        "bio": "Nikhil founded NV Fitness Time with a single conviction: that functional fitness changes lives. A CrossFit Level 2 certified coach with 10+ years of competitive experience, he brings elite-level programming to every WOD.",
    },
    {
        "name": "Kavitha Nair",
        "role": "Senior Coach",
        "speciality": "Body Transformation & Cardio",
        "since": 2020,
        "emoji": "🔥",
        "bio": "Kavitha specialises in body recomposition and conditioning work. Her metabolic training programs have helped hundreds of members drop body fat while building real athletic capacity.",
    },
    {
        "name": "Subhajit Das",
        "role": "Strength Coach",
        "speciality": "Powerlifting & Strength Cycles",
        "since": 2021,
        "emoji": "💪",
        "bio": "Subhajit's strength cycles are built around progressive overload and technical mastery. Whether you're chasing a new PR or building a base, his programming delivers consistent, trackable gains.",
    },
    {
        "name": "Ria Chatterjee",
        "role": "Certified Coach",
        "speciality": "Gymnastics & Mobility",
        "since": 2022,
        "emoji": "🤸",
        "bio": "Ria brings a gymnastics background to functional fitness — unlocking movement patterns most gym-goers never develop. Ring work, handstands, muscle-ups: she makes the impossible achievable.",
    },
    {
        "name": "Arnab Sen",
        "role": "Nutrition Coach",
        "speciality": "Sports Nutrition & Performance Diets",
        "since": 2021,
        "emoji": "🥗",
        "bio": "Arnab designs performance nutrition plans built around your WOD schedule, body composition goals, and food preferences. Real food, real results — no fad diets.",
    },
    {
        "name": "Priya Bose",
        "role": "Certified Coach",
        "speciality": "Beginner Onboarding & Foundations",
        "since": 2023,
        "emoji": "🌿",
        "bio": "Priya runs the Foundations program — the entry point for every new NV member. Patient, precise, and encouraging, she builds the movement literacy that makes every future WOD safer and more effective.",
    },
]

PROGRAMS = [
    {
        "icon": "⚡",
        "name": "CrossFit WOD",
        "level": "All Levels",
        "goal": "Fitness & Performance",
        "duration": "Ongoing",
        "desc": "Daily programmed group workouts covering strength, gymnastics, and metabolic conditioning. Scalable for every fitness level — from first-timers to competitive athletes.",
    },
    {
        "icon": "🔥",
        "name": "Body Transformation",
        "level": "All Levels",
        "goal": "Complete physique overhaul",
        "duration": "12 Weeks",
        "desc": "A structured 12-week program combining CrossFit methodology, targeted strength work, and a performance nutrition plan. Built for visible, lasting results.",
    },
    {
        "icon": "🏋️",
        "name": "Olympic Lifting",
        "level": "Intermediate – Advanced",
        "goal": "Snatch & Clean and Jerk",
        "duration": "8–12 Weeks",
        "desc": "Technical cycles focused on barbell efficiency, positional strength, and timing. Full coaching on the snatch and clean & jerk with video review.",
    },
    {
        "icon": "💪",
        "name": "Strength Cycle",
        "level": "Beginner – Advanced",
        "goal": "Maximal strength",
        "duration": "6–10 Weeks",
        "desc": "Linear and undulating periodisation for squat, deadlift, and press. Tracked, coached, and built to drive consistent personal records.",
    },
    {
        "icon": "🤸",
        "name": "Gymnastics & Mobility",
        "level": "All Levels",
        "goal": "Movement quality",
        "duration": "6 Weeks",
        "desc": "Ring work, pull-up progressions, handstands, and deep mobility drills. Move better. Perform better. Reduce injury risk.",
    },
    {
        "icon": "🌿",
        "name": "Foundations",
        "level": "Beginner",
        "goal": "Safe, confident start",
        "duration": "3 Weeks",
        "desc": "The mandatory onboarding program for new members. Learn the 9 foundational movements, proper scaling, and how to get the most out of every WOD before joining the open classes.",
    },
]

PLANS = [
    {
        "name": "Monthly",
        "price": "1,500",
        "period": "per month",
        "note": None,
        "featured": False,
        "features": [
            "Unlimited WOD access",
            "All equipment & rig",
            "Group class sessions",
            "Locker access",
        ],
    },
    {
        "name": "Quarterly",
        "price": "3,800",
        "period": "per 3 months",
        "note": "Save ₹700 vs monthly",
        "featured": True,
        "features": [
            "Unlimited WOD access",
            "All equipment & rig",
            "Group class sessions",
            "Locker access",
            "Nutrition consultation",
        ],
    },
    {
        "name": "Performance",
        "price": "6,000",
        "period": "per 3 months",
        "note": "Includes coaching add-ons",
        "featured": False,
        "features": [
            "Unlimited WOD access",
            "All equipment & rig",
            "Group class sessions",
            "Locker access",
            "Nutrition consultation",
            "Custom nutrition plan",
            "Body composition tracking",
        ],
    },
    {
        "name": "Half-Yearly",
        "price": "7,200",
        "period": "per 6 months",
        "note": "Save ₹1,800 vs monthly",
        "featured": False,
        "features": [
            "Unlimited WOD access",
            "All equipment & rig",
            "Group class sessions",
            "Locker access",
            "Nutrition consultation",
            "4 PT sessions",
        ],
    },
    {
        "name": "Annual",
        "price": "13,200",
        "period": "per year",
        "note": "Best value — Save ₹4,800",
        "featured": True,
        "features": [
            "Unlimited WOD access",
            "All equipment & rig",
            "Group class sessions",
            "Locker access",
            "Nutrition consultation",
            "Custom nutrition plan",
            "Body composition tracking",
        ],
    },
    {
        "name": "Personal Training",
        "price": "5,000",
        "period": "per month",
        "note": "1-on-1 coaching add-on",
        "featured": False,
        "features": [
            "One-on-one sessions",
            "Custom training plan",
            "Nutrition consultation",
            "Custom nutrition plan",
            "Body composition tracking",
            "Flexible scheduling",
        ],
    },
]

COMPARISON_FEATURES = [
    {"label": "Unlimited WOD Access",        "keywords": ["unlimited wod", "wod access"]},
    {"label": "All Equipment & Rig",          "keywords": ["all equipment", "equipment & rig"]},
    {"label": "Group Class Sessions",         "keywords": ["group class"]},
    {"label": "Locker Access",               "keywords": ["locker"]},
    {"label": "Nutrition Consultation",       "keywords": ["nutrition consultation"]},
    {"label": "Custom Nutrition Plan",        "keywords": ["custom nutrition", "nutrition plan"]},
    {"label": "Body Composition Tracking",    "keywords": ["body composition tracking"]},
]


def build_compare_matrix(plans, features):
    matrix = []
    for f in features:
        row = {"label": f["label"], "values": []}
        kws = [k.lower() for k in f.get("keywords", [])]
        for p in plans:
            pf = " ".join(p.get("features", [])).lower()
            has = any(kw in pf for kw in kws)
            row["values"].append(bool(has))
        matrix.append(row)
    return matrix

FAQS = [
    {
        "q": "Do I need CrossFit experience to join?",
        "a": "Not at all. All new members start with our 3-week Foundations program, where you learn the core movements at your own pace before joining open WOD classes. No experience needed.",
    },
    {
        "q": "What is a WOD?",
        "a": "WOD stands for Workout of the Day — a daily programmed session that varies in structure, movement, and intensity. Every WOD is coached and fully scalable to your current fitness level.",
    },
    {
        "q": "Can I try before committing?",
        "a": "Yes. We offer a free trial WOD session with no obligation. Come in, meet the coaches, try a session, and decide for yourself.",
    },
    {
        "q": "Is there a joining fee?",
        "a": "No joining or registration fee. You pay only the membership amount — nothing hidden, nothing extra.",
    },
    {
        "q": "Are sessions suitable for beginners?",
        "a": "Absolutely. Every movement in every WOD has a scaled option. Our coaches are trained to meet members at their level and build from there, safely and progressively.",
    },
    {
        "q": "Can women train here?",
        "a": "Yes. NV Fitness Time is fully co-ed and maintains a respectful, supportive atmosphere. Several of our members and coaches are women.",
    },
    {
        "q": "What are your hours?",
        "a": "We're open 7 days a week, 6 AM to 10 PM. Check the Contact page for specific class timings.",
    },
    {
        "q": "Do you offer personal training?",
        "a": "Yes. Personal training is available as a separate monthly add-on with one-on-one sessions, a fully custom program, and nutrition guidance.",
    },
]

REVIEWS = [
    {
        "stars": 5,
        "text": "NV Fitness is a great gym. All the trainers are really nice and try to help you no matter what fitness level you're at. I really like how they give tips and tricks to get the most out of every workout. Would highly recommend!",
        "name": "Karishma A.",
        "tag": "Member · CrossFit",
    },
    {
        "stars": 5,
        "text": "I joined 10 days ago and it's already a very good gym. Supporting trainers and lots of equipment. The coaches actually care about your form and progress — not just going through the motions.",
        "name": "Sushant T.",
        "tag": "New Member",
    },
    {
        "stars": 5,
        "text": "If you want fitness, this is the best gym for you. The trainers are well educated and their guidance will help you transform. Some of the results they've helped members achieve are remarkable. Definitely recommend.",
        "name": "Garvit A.",
        "tag": "Member · Strength & CrossFit",
    },
    {
        "stars": 5,
        "text": "The community here is unlike any gym I've been to. Everyone supports each other during WODs, and the coaches know when to push you and when to back off. 5 stars without question.",
        "name": "Ananya S.",
        "tag": "Member since 2021",
    },
    {
        "stars": 5,
        "text": "Started here as a complete beginner with zero idea what CrossFit even was. Three months in, I'm hitting movements I thought were impossible. The Foundations program set me up perfectly.",
        "name": "Rohit B.",
        "tag": "Member · Foundations Graduate",
    },
]

# ── CONTEXT HELPER ─────────────────────────────────────────────────────────────

def base_ctx(page_title: str, current_page: str) -> dict:
    return {
        "gym": GYM,
        "pages": PAGES,
        "current_page": current_page,
        "page_title": page_title,
        "hours": HOURS,
        "trainers": TRAINERS,
    }

# ── ROUTES ─────────────────────────────────────────────────────────────────────

@app.route("/")
def index():
    ctx = base_ctx("Home", "/")
    ctx.update(facilities=FACILITIES, programs=PROGRAMS[:4], reviews=REVIEWS)
    return render_template("index.html", **ctx)

@app.route("/about")
def about():
    ctx = base_ctx("About Us", "/about")
    return render_template("about.html", **ctx)

@app.route("/programs")
def programs():
    ctx = base_ctx("Programs", "/programs")
    ctx.update(programs=PROGRAMS)
    return render_template("programs.html", **ctx)

@app.route("/trainers")
def trainers():
    ctx = base_ctx("Our Coaches", "/trainers")
    return render_template("trainers.html", **ctx)

@app.route("/membership")
def membership():
    ctx = base_ctx("Membership", "/membership")
    compare_plans = [p for p in PLANS if p["name"] != "Personal Training"]
    compare_matrix = build_compare_matrix(compare_plans, COMPARISON_FEATURES)
    ctx.update(plans=PLANS, faqs=FAQS, compare_plans=compare_plans, compare_matrix=compare_matrix)
    return render_template("membership.html", **ctx)

@app.route("/gallery")
def gallery():
    ctx = base_ctx("Gallery", "/gallery")
    return render_template("gallery.html", **ctx)

@app.route("/contact")
def contact():
    ctx = base_ctx("Contact", "/contact")
    return render_template("contact.html", **ctx)

@app.route("/api/trial", methods=["POST"])
def api_trial():
    data = request.get_json(silent=True) or {}
    name  = data.get("name", "").strip()
    phone = data.get("phone", "").strip()
    goal  = data.get("goal", "").strip()
    if not name or not phone:
        return jsonify({"ok": False, "error": "Name and phone are required."}), 400
    print(f"[TRIAL] {name} | {phone} | {goal}")
    return jsonify({"ok": True})

@app.route("/api/contact", methods=["POST"])
def api_contact():
    data     = request.get_json(silent=True) or {}
    first    = data.get("first", "").strip()
    last     = data.get("last", "").strip()
    phone    = data.get("phone", "").strip()
    interest = data.get("interest", "").strip()
    message  = data.get("message", "").strip()
    if not first or not phone:
        return jsonify({"ok": False, "error": "First name and phone are required."}), 400
    print(f"[CONTACT] {first} {last} | {phone} | {interest} | {message}")
    return jsonify({"ok": True})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
