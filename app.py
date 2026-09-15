import streamlit as st

st.set_page_config(
    page_title="ExamSafe",
    page_icon="🛡️",
    layout="wide"
)

# ================= SYSTEM STATE =================
if "active_page" not in st.session_state:
    st.session_state.active_page = "landing"

if "toast" not in st.session_state:
    st.session_state.toast = None

if "simulation" not in st.session_state:
    st.session_state.simulation = False


def go(page):
    st.session_state.active_page = page
    st.rerun()


# ================= DEMO BANNER =================
st.info(
    "🎓 Academic Demo | Automated Rollback for Online Examination System"
)


# ================= NAVBAR =================
st.markdown("""
# 🛡️ ExamSafe
**DevOps Examination Reliability**
""")

nav = st.columns(8)

buttons = [
    ("Home", "landing"),
    ("Register", "register"),
    ("Login", "login"),
    ("Student", "dashboard"),
    ("Exam", "exam"),
    ("Recovery", "recovery"),
    ("DevOps", "devops"),
    ("Admin", "admin")
]

for col, (name, page) in zip(nav, buttons):
    with col:
        if st.button(name, use_container_width=True):
            go(page)

st.divider()


# ================= TOAST =================
if st.session_state.toast:
    st.success(st.session_state.toast)
    st.session_state.toast = None


# ================= PAGE RENDERING =================
page = st.session_state.active_page


# -------- LANDING --------
if page == "landing":
    st.title("🛡️ ExamSafe")
    st.header("DevOps Examination Reliability System")

    st.write(
        "Automated Blue/Green & Canary Rollback Engine "
        "with Zero Student Data Loss."
    )

    c1, c2, c3 = st.columns(3)

    c1.metric("System Health", "98%")
    c2.metric("Active Exams", "5")
    c3.metric("Rollback Ready", "YES")

    if st.button("🚀 Get Started"):
        go("login")


# -------- REGISTER --------
elif page == "register":
    st.title("📝 Student Registration")

    st.text_input("Full Name")
    st.text_input("Email")
    st.text_input("Password", type="password")

    if st.button("Register"):
        st.session_state.toast = "Registration successful!"
        st.rerun()


# -------- LOGIN --------
elif page == "login":
    st.title("🔐 Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        st.session_state.toast = "Login successful!"
        go("dashboard")


# -------- STUDENT DASHBOARD --------
elif page == "dashboard":
    st.title("🎓 Student Dashboard")

    a, b, c = st.columns(3)
    a.metric("Available Exams", "5")
    b.metric("Completed Exams", "3")
    c.metric("Average Score", "82%")

    st.subheader("Upcoming Exams")
    st.write("• Python Programming")
    st.write("• Database Management System")
    st.write("• Operating Systems")

    if st.button("📊 View Results"):
        go("student_results")


# -------- STUDENT RESULTS --------
elif page == "student_results":
    st.title("📊 Student Results")

    st.table({
        "Exam": ["Python", "DBMS", "Operating Systems"],
        "Score": ["85%", "78%", "83%"],
        "Status": ["Passed", "Passed", "Passed"]
    })


# -------- PROFILE --------
elif page in ["profile", "admin_profile"]:
    st.title("👤 Profile")

    st.text_input("Name", "Student")
    st.text_input("Email", "student@example.com")

    if st.button("Update Profile"):
        st.success("Profile updated successfully!")


# -------- EXAM --------
elif page == "exam":
    st.title("📝 Online Examination")

    questions = [
        "Which language is widely used for AI?",
        "Which database language is SQL?",
        "Which OS manages computer resources?"
    ]

    answers = []

    for i, q in enumerate(questions):
        answers.append(
            st.radio(
                f"Q{i+1}. {q}",
                ["Python", "Java", "C++", "HTML"],
                key=f"q{i}"
            )
        )

    if st.button("Submit Exam"):
        st.success("Exam submitted successfully!")


# -------- SYSTEM RECOVERY --------
elif page == "recovery":
    st.title("🔄 System Recovery")

    st.success("🟢 System Status: Healthy")
    st.progress(0.98)

    st.write("Recovery Engine: Ready")
    st.write("Database Backup: Available")
    st.write("Stable Version: v2.1")

    if st.button("🚀 Start Recovery"):
        st.success("System recovery completed successfully!")


# -------- DEVOPS --------
elif page == "devops":
    st.title("⚙️ DevOps Dashboard")

    a, b, c = st.columns(3)
    a.metric("Deployment", "Blue")
    b.metric("System Health", "98%")
    c.metric("Rollback Ready", "YES")

    st.subheader("Deployment Status")
    st.write("🟢 Blue Version — Stable")
    st.write("🟡 Green Version — Testing")
    st.write("🔵 Canary — Monitoring")


# -------- ROLLBACK HISTORY --------
elif page == "rollback_history":
    st.title("🔄 Rollback History")

    st.table({
        "Version": ["v3.0", "v2.1", "v2.0"],
        "Status": ["Rolled Back", "Stable", "Stable"],
        "Reason": [
            "System Failure",
            "Normal Deployment",
            "Initial Release"
        ]
    })


# -------- ADMIN DASHBOARD --------
elif page in ["admin", "admin_dashboard"]:
    st.title("👨‍💼 Admin Dashboard")

    a, b, c, d = st.columns(4)

    a.metric("Students", "250")
    b.metric("Exams", "12")
    c.metric("Active Exams", "4")
    d.metric("System", "Healthy")

    st.subheader("Admin Controls")

    if st.button("📚 Manage Exams"):
        go("admin_exams")

    if st.button("👥 Manage Enrollment"):
        go("admin_enrollments")

    if st.button("📡 System Monitoring"):
        go("admin_monitoring")

    if st.button("📊 View Results"):
        go("admin_results")

    if st.button("📜 Audit Logs"):
        go("admin_audit_logs")


# -------- ADMIN EXAMS --------
elif page == "admin_exams":
    st.title("📚 Admin — Exam Management")

    st.text_input("Exam Name")
    st.number_input("Duration (minutes)", 1, 300, 60)

    if st.button("➕ Create Exam"):
        st.success("Exam created successfully!")


# -------- ADMIN ENROLLMENT --------
elif page == "admin_enrollments":
    st.title("👥 Admin — Enrollment")

    st.table({
        "Student": ["Student 01", "Student 02", "Student 03"],
        "Exam": ["Python", "DBMS", "OS"],
        "Status": ["Enrolled", "Enrolled", "Pending"]
    })


# -------- ADMIN MONITORING --------
elif page == "admin_monitoring":
    st.title("📡 Admin — System Monitoring")

    a, b, c = st.columns(3)

    a.metric("Server", "🟢 Online")
    b.metric("Database", "🟢 Healthy")
    c.metric("Application", "🟢 Running")

    st.progress(0.98)


# -------- ADMIN RESULTS --------
elif page == "admin_results":
    st.title("📊 Admin — Results")

    st.table({
        "Student": ["Student 01", "Student 02", "Student 03"],
        "Score": ["85%", "78%", "91%"],
        "Status": ["Passed", "Passed", "Passed"]
    })


# -------- AUDIT LOGS --------
elif page == "admin_audit_logs":
    st.title("📜 Admin — Audit Logs")

    st.code("""
10:30  Student Login
10:32  Exam Started
10:55  Exam Submitted
10:56  Result Generated
10:57  Backup Created
11:00  System Monitoring
""")


# -------- HOW IT WORKS --------
elif page == "how_it_works":
    st.title("⚙️ How It Works")

    st.write("""
    1️⃣ Monitor examination system

    2️⃣ Detect system failure

    3️⃣ Identify affected deployment

    4️⃣ Trigger automated rollback

    5️⃣ Restore stable version

    6️⃣ Verify student data

    7️⃣ Continue examination service
    """)


# -------- ARCHITECTURE --------
elif page == "architecture":
    st.title("🏗️ System Architecture")

    st.code("""
        STUDENT
           ↓
   ONLINE EXAMINATION
           ↓
   MONITORING ENGINE
           ↓
    FAILURE DETECTION
           ↓
     ROLLBACK ENGINE
           ↓
    STABLE VERSION
           ↓
     DATA VERIFICATION
    """)


# -------- ABOUT --------
elif page == "about":
    st.title("ℹ️ About ExamSafe")

    st.write(
        "ExamSafe is a DevOps-based examination reliability "
        "system that automatically detects failures and "
        "rolls back to a stable version while protecting "
        "student examination data."
    )


# ================= SIMULATION =================
st.sidebar.divider()
st.sidebar.subheader("🧪 Rollback Simulation")

if st.sidebar.button("🚨 Simulate Failure"):
    st.session_state.simulation = True

if st.session_state.simulation:
    st.error("🚨 SYSTEM FAILURE DETECTED!")
    st.warning("Automated rollback has been initiated.")

    if st.button("🔄 Execute Automated Rollback"):
        st.session_state.simulation = False
        st.success(
            "✅ Rollback successful! "
            "Stable version restored with zero student data loss."
        )


# ================= FOOTER =================
st.divider()

st.markdown("""
### 🛡️ ExamSafe
**DevOps Examination Reliability**

Automated Blue/Green & Canary Rollback Engine  
with Zero Student Data Loss

`Final Year Engineering Project`
""")

f1, f2, f3, f4, f5 = st.columns(5)

with f1:
    if st.button("Viva Defense Guide"):
        go("about")

with f2:
    if st.button("System Architecture"):
        go("architecture")

with f3:
    if st.button("System Recovery"):
        go("recovery")

with f4:
    if st.button("DevOps Monitor"):
        go("devops")

with f5:
    if st.button("Rollback History"):
        go("rollback_history")
