# Candidate Verification System
from pyscript import document, display

# Uses a list to group ICT club members
ict_club_members = [
    "Joshua Ortiz",
    "Enzo Ruiz",
    "Logan Anaque",
    "Doctor Doom",
    "John Hizon",
    "Khabib Nurmagomedov",
    "Islam Makhachev",
    "Iron Man"
]

grade_7 = {'Doctor Doom', 'Iron Man'}
grade_8 = {'Khabib Nurmagomedov', 'Islam Makhachev'}
grade_9 = {'Joshu Ortiz', 'John Hizon'}
grade_10 = {'Logan Anaque', 'Enzo Ruiz'}

members_list = "<br>".join(sorted(ict_club_members))
new_members_list = grade_7 | grade_8 | grade_9 | grade_10

display(f'members_list')
display(len('members_list'))

# Combines the first and last name inputted and checks if they are in the ICT club members list
def add_club_member(e):
    first_name = document.getElementById("first_name").value.strip()
    last_name = document.getElementById("last_name").value.strip()

    club_member_name = first_name + " " + last_name
    is_member = club_member_name in ict_club_members

# Different messages shown to the user depending on whether they are a member or not
    messages = [
        "Sorry " + club_member_name + ", your name is not on the list.",
        "Congratulations " + club_member_name + "! You are now part of the ICT club."
    ]

# Displays the Candidate Verification System
    document.getElementById("result").innerHTML = ""
    display(messages[is_member], target="result")