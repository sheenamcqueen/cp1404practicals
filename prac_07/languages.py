
from prac_07.programming_language import ProgrammingLanguage


def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", True, 1991)
    print(python)

    print("The dynamically typed languages are:")
    languages = [ruby, python, visual_basic]
    for language in languages:
        if language.is_dynamic():
            print(language.name)


main()