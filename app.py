from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

students = [
    {"roll": "101", "name": "Aarav Patil", "department": "CSE"},
    {"roll": "102", "name": "Mira Shah", "department": "IT"}
]

@app.route("/")
def home():
    return render_template("index.html", students=students)

@app.route("/add", methods=["POST"])
def add_student():
    roll = request.form.get("roll", "").strip()
    name = request.form.get("name", "").strip()
    department = request.form.get("department", "").strip()

    if roll and name and department:
        duplicate = any(student["roll"] == roll for student in students)
        if not duplicate:
            students.append({
                "roll": roll,
                "name": name,
                "department": department
            })

    return redirect(url_for("home"))

@app.route("/delete/<roll>", methods=["POST"])
def delete_student(roll):
    global students
    students = [student for student in students if student["roll"] != roll]
    return redirect(url_for("home"))

@app.route("/health")
def health():
    return {"status": "ok"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
