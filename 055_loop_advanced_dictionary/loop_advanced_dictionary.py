# ------------------------------
# -- Advanced Dictionary Loop --
# ------------------------------

skills = {
    'HTML': '80%',
    'CSS': '60%',
    'JS': "70%",
    'Dart': "95%",
    'Python': "90%"
}

print(skills.items())

for skill in skills:
    print(f"{skill} => {skills[skill]}")

for key, value in skills.items():
    print(f'key: {key}, value: {value}')


ultimate_skills = {
    "HTML": {
        "Main": "80%",
        "Pugjs": "80%"
    },
    "CSS": {
        "Main": "90%",
        "Sass": "70%"
    }
}

for key, value in ultimate_skills.items():
    print(f'{key} progress is: ')
    for k, v in value.items():
        print(f' - {k}, {v}')
