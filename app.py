from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# ── FAQ Knowledge Base ────────────────────────────────────────────────────────
faqs = {
    # Admission
    "admission": "Admissions for the B.Sc. in Computer Science and Engineering (CSE) at Premier University (PU) in Chattogram open twice a year for two main sessions: Spring and Fall.Spring Session: Applications typically open in December/January, with admission tests generally held between January and April.Fall Session: Applications typically open in July/August, with admission tests generally held in September. Visit the admission office or apply online at our website.",
    "apply": "You can apply for the B.Sc. in Computer Science & Engineering (CSE) programs online through the official Premier University Admission Portal.Offline Application: Collect and submit the form in person at the Information Desk or Admission Office (541, O.R. Nizam Road, GEC Circle, Chattogram).",
    "eligibility": "Ensure you have a minimum GPA of 2.5 in both SSC and HSC (or equivalent), or an aggregate GPA of 6.0 . Candidates must have a science background in both SSC and HSC.",
    "admission test": "Eligible applicants must sit for the written admission test at the Engineering Faculty campus.",
    "deadline": " Contact accounts office for full details.",
    "documents": "Required documents:Original Admit Card from the Premier University Admission Test, NID/Birth Certificate, SSC and HSC Certificates & Transcripts, passport-size photos and application fee receipt.",

    # Fees
    "fee": " The total estimated cost for the 4-year degree generally ranges between Tk. 3.5 Lakh to Tk. 4.5 Lakh, depending on waivers and total credit hours completed.Contact accounts office for full details.",
    "tuition": "First Semester Cost: Tk. 61,120 (includes admission and first-semester fees).The total estimated tuition averaging roughly Tk. 43,000 to Tk. 45,000 per semester. Contact accounts office for full details.",
    "scholarship": "Scholarships are available for meritorious and financially needy students. Apply at the scholarship office within first month of admission.",
    "payment": "Payment Method: Must be deposited at any United Commercial Bank Ltd. (UCB) branch.",
    "waiver": "Tuition fee waivers are available based on SSC and HSC results, which can significantly lower your overall semester expenses Contact the scholarship committee for details.",

    # Academic
    "result": "Results are published within 4 weeks after exams on the student portal.",
    "exam": "The Midterm exams typically occur 1.5 to 2 months into the semester, while the Final exams occur roughly 3.5 to 4 months after classes begin. Exact dates are subject to the specific batch and session schedules published by the department.",
    "cgpa": "CGPA of 2.20 out of 4.00 to successfully pass each semester and ultimately graduate.Any GPA below 2.20 is considered probation status, as you require an aggregate of 2.20 or higher to earn your degree. ",
    "credit": "Students normally enroll in 16-21 credits per semester to maintain a smooth pace toward graduation.Completing the B.Sc. in CSE program requires a minimum of 150 credits.",
    "transcript": "Official transcripts can be collected from the registrar office within 7 working days after submitting the request form.",
    "certificate": "Certificates at Premier University (including CSE graduates) are issued by the Office of the Controller of Examinations, located at the GEC Campus.Location: 541, O.R. Nizam Road, GEC Circle, Chattogram.Processing Times: Regular certificates and transcripts take ~ 23 working days, while urgent requests take ~ 5 working days.",

    # Campus
    "library": "The library is open Saturday to Wednesday, 8.30 am - 5.30 pm. It has CSE textbooks, Printed Journals, Online E-books and online journal access.Students can borrow general books for a set period. Lost or damaged books incur a replacement fee of twice the current market value.",
    "cafeteria": "The cafeteria is open 8:30 AM to 5:30 PM on all working days. It offers affordable snacks starting from 5 BDT.",
    "hostel": "Separate hostels are NOT available. ",
    "transport": "University transport system is NOT available.",
    "wifi": "Free WiFi is available across the campus. Use your student ID as username and phone number as password to log in.",

    # Contact
    "contact": "You can reach us at info@puc.ac.bd or call +8801313044515-17. Office hours are 8:30 AM to 5:30 PM.",
    "office": "The main office is open Saturday to Wednesday, 8:30 AM to 5:30 PM. It is closed on Thursday, Friday and public holidays.",
    "location": "The university is located at Academic Building#4, 44, HazariLane, Kotwali, Chattogram, Bangladesh. ",

    # General
    "hello": "Hello! I am the Premier University, CSE department FAQ Bot. Ask me anything about admissions, fees, exams, hostel or campus life!",
    "hi": "Hi there! How can I help you today? You can ask about admissions, fees, results, library, hostel and more.",
    "help": "I can answer questions about: Admissions, Fees & Scholarships, Exams & Results, Library, Hostel, Transport and Contact info.",
    "bye": "Goodbye! Feel free to come back if you have more questions. Have a great day!",
    "thank": "You are welcome! Is there anything else I can help you with?",
    "thanks": "You are welcome! Is there anything else I can help you with?",
}

def get_response(user_input):
    user_input = user_input.lower().strip()

    # Check if any keyword matches
    for keyword, response in faqs.items():
        if keyword in user_input:
            return response

    # Default response
    return ("I'm sorry, I don't have information on that topic yet. "
            "Please contact the Premier University, CSE department directly at info@puc.ac.bd "
            "or call +8801313044515-17. You can also type 'help' to see what I can answer.")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "")
    response     = get_response(user_message)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)