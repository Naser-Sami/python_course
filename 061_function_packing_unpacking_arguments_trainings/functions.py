# -----------------------------------------------------
# -- Function Packing, Unpacking Arguments Trainings --
# -----------------------------------------------------

_skills = ('Flutter', 'C#', 'Python', 'Dart', 'SQL')
d_skills = {
    'Html': "80%",
    'Css': "70%",
    'Js': "50%",
    'Python': "85%",
    "Go": "60%",
    "SQL": "89%",
    "Flutter": '94%',
    "C#": '90%'
}


def print_skills(name, *skills, **skills_dic):
    print(f'Hello, {name} your skills are:')
    for skill in skills:
        print(f' - {skill}')

    for key, value in skills_dic.items():
        print(f'{key} -> {value}')


# print_skills('Naser', 'Flutter', 'C#', 'Python', 'Dart', 'SQL')
# print_skills('Naser', *_skills)


print('=' * 40)


# Unpacking
print_skills('Naser')
print('=' * 40)
print_skills('Naser', *_skills)
print('=' * 40)
print_skills('Naser', **d_skills)
print('=' * 40)
print_skills('Naser', *_skills, **d_skills)
print('=' * 40)
