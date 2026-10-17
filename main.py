# Set Operators
from pyscript import document, display

# Sets for each grade
grade_7 = {"Doctor Doom", "Iron Man"}
grade_8 = {"Khabib Nurmagomedov", "Islam Makhachev"}
grade_9 = {"Joshua Ortiz", "John Hizon"}
grade_10 = {"Logan Anaque", "Enzo Ruiz"}

# Combines all grade sets
all_members = grade_7 | grade_8 | grade_9 | grade_10

# Displays all members and the total
def show_members():
    members_list = "<br>".join(sorted(all_members))
    display(f"ALL MEMBERS:<br>{members_list} <br>TOTAL MEMBERS: {len(all_members)}", target="result")

show_members()

# Adds a new club member

def add_club_member(e):
    first_name = document.getElementById("first_name").value.strip().title()
    last_name = document.getElementById("last_name").value.strip().title()

    # Adds the full name to the set
    all_members.add(first_name + " " + last_name)

    # Updates the displayed results
    show_members()
