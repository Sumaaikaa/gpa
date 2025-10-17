import streamlit as st

st.set_page_config(page_title="CGPA Calculator")
st.title(" CGPA & Grade Calculator")
st.write("Enter your subject marks or GPAs per semester to calculate your overall CGPA and grade.")


semesters = st.number_input("Enter total number of semesters completed:")

semester_gpas = []
semester_credits = []

for i in range(int(semesters)):
    st.header(f" Semester {i+1}")

    subjects = st.number_input(f"Number of subjects in Semester {i+1}:")
    subject_grades = []
    subject_credits = []

    for j in range(int(subjects)):
        st.markdown(f"**Subject {j+1}**")
        mark = st.number_input(f"Enter marks (0–100) for Subject {j+1}:", min_value=0.0, max_value=100.0, step=1.0, key=f"mark_{i}_{j}")
        credit = st.number_input(f"Credit hours for Subject {j+1}:", min_value=0.5, step=0.5, key=f"credit_{i}_{j}")

        # Convert marks to GPA (you can adjust this mapping)
        if mark >= 85:
            gpa = 4.0
        elif mark >= 75:
            gpa = 3.66
        elif mark >= 70:
            gpa = 3.33
        elif mark >= 65:
            gpa = 3.0
        elif mark >= 60:
            gpa = 2.5
        elif mark >= 50:
            gpa = 2.0
        else:
            gpa = 0.0

        st.caption(f"GPA for Subject {j+1}: **{gpa:.2f}**")

        subject_grades.append(gpa)
        subject_credits.append(credit)
        st.divider()

    total_credits = sum(subject_credits)
    if total_credits > 0:
        sem_gpa = sum(g * c for g, c in zip(subject_grades, subject_credits)) / total_credits
        st.success(f"Semester {i+1} GPA: **{sem_gpa:.2f}**")
        semester_gpas.append(sem_gpa)
        semester_credits.append(total_credits)
    else:
        st.warning(f"Please enter valid credits for Semester {i+1}.")


