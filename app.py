
import os
import gradio as gr
import pandas as pd
import numpy as np
import joblib

regressor = joblib.load("models/scoresync_regression.pkl")
classifier = joblib.load("models/scoresync_classification.pkl")


def predict_student(
    branch, semester, age, gender, previous_cgpa, attendance,
    internal_marks, assignment_score, practical_score, study_hours,
    classes_attended, assignment_completion, backlogs
):
    student = pd.DataFrame([{
        "branch": branch,
        "semester": int(semester),
        "age": int(age),
        "gender": gender,
        "previous_cgpa": float(previous_cgpa),
        "attendance": float(attendance),
        "internal_marks": float(internal_marks),
        "assignment_score": float(assignment_score),
        "practical_score": float(practical_score),
        "study_hours": float(study_hours),
        "classes_attended": float(classes_attended),
        "assignment_completion": float(assignment_completion),
        "backlogs": int(backlogs)
    }])

    percentage = float(regressor.predict(student)[0])
    percentage = float(np.clip(percentage, 0, 100))
    outcome = str(classifier.predict(student)[0])

    return round(percentage, 1), outcome


with gr.Blocks(title="ScoreSync") as demo:
    gr.Markdown("# ScoreSync — Student Performance Prediction")
    gr.Markdown(
        "Enter a student's academic details to estimate their "
        "final percentage and predicted outcome."
    )

    with gr.Row():
        branch = gr.Dropdown(
            ["Civil Engineering", "Computer Engineering",
             "Information Technology", "Mechanical Engineering",
             "Electrical Engineering", "Electronics Engineering"],
            value="Computer Engineering",
            label="Engineering Branch"
        )
        semester = gr.Dropdown(
            [4, 5, 6, 7], value=6, label="Semester"
        )

    with gr.Row():
        age = gr.Slider(17, 30, value=21, step=1, label="Age")
        gender = gr.Dropdown(
            ["Male", "Female", "Other"],
            value="Male", label="Gender"
        )

    gr.Markdown("### Academic Information")

    with gr.Row():
        previous_cgpa = gr.Slider(
            0, 10, value=7, step=0.1, label="Previous CGPA"
        )
        attendance = gr.Slider(
            0, 100, value=75, step=1, label="Attendance (%)"
        )

    with gr.Row():
        internal_marks = gr.Slider(
            0, 30, value=20, step=1, label="Internal Marks"
        )
        assignment_score = gr.Slider(
            0, 100, value=75, step=1, label="Assignment Score"
        )

    with gr.Row():
        practical_score = gr.Slider(
            0, 100, value=75, step=1, label="Practical Score"
        )
        backlogs = gr.Slider(
            0, 10, value=0, step=1, label="Current Backlogs"
        )

    gr.Markdown("### Study and Participation")

    with gr.Row():
        study_hours = gr.Slider(
            0, 12, value=2, step=0.5, label="Study Hours per Day"
        )
        classes_attended = gr.Slider(
            0, 100, value=75, step=1, label="Classes Attended (%)"
        )

    assignment_completion = gr.Slider(
        0, 100, value=75, step=1,
        label="Assignment Completion (%)"
    )

    predict_button = gr.Button(
        "Predict Student Performance", variant="primary"
    )

    with gr.Row():
        predicted_percentage = gr.Number(
            label="Predicted Final Percentage (%)", precision=1
        )
        predicted_outcome = gr.Textbox(
            label="Predicted Outcome", interactive=False
        )

    predict_button.click(
        fn=predict_student,
        inputs=[
            branch, semester, age, gender, previous_cgpa, attendance,
            internal_marks, assignment_score, practical_score,
            study_hours, classes_attended, assignment_completion,
            backlogs
        ],
        outputs=[predicted_percentage, predicted_outcome]
    )

    gr.Markdown(
        "**Project note:** The model uses synthetically generated "
        "demonstration data. Predictions are estimates, not official "
        "GTU results or validated assessments of actual students."
    )


if __name__ == "__main__":
    demo.launch()