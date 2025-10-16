import streamlit as st

st.set_page_config(page_title="CGPA Calculator")
st.title("CGPA & Grade Calculator")
st.write("Enter your GPA for each semester to calculate your overall CGPA and grade.")


semesters = st.number_input("Enter total number of semesters completed:", min_value=1, step=1)


gpa_list = []

for i in range(int(semesters)):
    gpa = st.number_input(f"Enter GPA for Semester {i+1}:")
    gpa_list.append(gpa)


def get_grade_and_remark(cgpa):
    if cgpa >= 3.7:
        return "A", "Excellent"
    elif cgpa >= 3.3:
        return "A-", "Very Good"
    elif cgpa >= 3.0:
        return "B+", "Good"
    elif cgpa >= 2.7:
        return "B", "Above Average"
    elif cgpa >= 2.3:
        return "B-", "Average"
    elif cgpa >= 2.0:
        return "C", "Satisfactory"
    elif cgpa >= 1.7:
        return "C-", "Needs Improvement"
    elif cgpa >= 1.3:
        return "D", "Poor"
    elif cgpa >= 1.0:
        return "D-", "Very Poor"
    else:
        return "F", "Fail"

if st.button("Calculate CGPA"):
    if semesters > 0:
        cgpa = sum(gpa_list) / semesters
        grade, remark = get_grade_and_remark(cgpa)

        st.success(f"🎯 Your CGPA after {int(semesters)} semester(s) is **{cgpa:.2f}**")
        st.write(f"**Grade:** {grade}")
        st.write(f"**Remark:** {remark}")
        st.progress(min(cgpa / 4, 1.0))
        st.caption("Progress toward 4.0 CGPA")
    else:
        st.warning("Please enter at least one GPA.")
