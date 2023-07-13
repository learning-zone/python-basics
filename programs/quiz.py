from questions import Questions
question_prompts = [
    "Who killed the monster \'Minotaur\' in Greek mythology?\n(a) Hercules\n(b) Theseus\n(c) Hera\n(d) Zeus\n",
    "How many labors does Goddess Hera gave to Hercules?\n(a) 42\n(b) 7\n(c) 12\n(d) 32\n",
    "Who is the God of Underworld?\n(a) Hades\n(b) Persephone\n(c) Dionysus\n(d) Orpheus\n",
    "How many heads does cerberus has?\n(a) 1\n(b) 2\n(c) 3\n(d) None\n",
    "Who killed the serpent snake Orochi?\n(a) Aqua\n(b) Zoro\n(c) Poseidon\n(d) Susa-no-O\n"
]

questions = [
    Questions(question_prompts[0], "b"),
    Questions(question_prompts[1], "c"),
    Questions(question_prompts[2], "a"),
    Questions(question_prompts[3], "c"),
    Questions(question_prompts[4], "d")
]

def test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompts)
        if answer == question.answer:
            score += 1
    print(f"Your score is {score}/{len(questions)} correct")

test(questions)