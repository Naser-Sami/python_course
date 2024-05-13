# ----------------------------------------------------
# -- Function Packing, Unpacking Arguments **KWArgs --
# ----------------------------------------------------

def print_skills(*skills):
    print(type(skills))     # 'tuple'

    for skill in skills:
        print(f' - {skill}')


print_skills('Flutter', 'Python', 'C#', 'C++')
print('='*20)


# keyword argument **
def dict_skills(**skills):
    print(type(skills))

    for key, value in skills.items():
        print(f'{key} : {value}')


dict_skills(Python='90%', Flutter='96%', CSharp='87%')
print('='*20)


d_skills = {
  'Html': "80%",
  'Css': "70%",
  'Js': "50%",
  'Python': "80%",
  "Go": "60%"
}

print(d_skills)
print('='*20)
dict_skills(**d_skills)
