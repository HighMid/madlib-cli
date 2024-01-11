import time, sys, re


def delay_print(a):
    for b in a:
        sys.stdout.write(b)
        sys.stdout.flush()
        time.sleep(0.05)

def delay_print_fast(a):
    for b in a:
        sys.stdout.write(b)
        sys.stdout.flush()
        time.sleep(0.001)

def pause(option):
    if option == 1:
        time.sleep(0.5)

    if option == 2:
        time.sleep(1)
        
    if option == 3:
        time.sleep(2)

def start():
    print("Skip intro?")
    while True:
        try:
            choice = input("Yes/No : ")
            if choice.lower() in ['y', 'yes']:
                return True
            elif choice.lower() in ['n', 'no']:
                return False
            else:
                print("Ah don't worry about it, you'll like the intro guy!")
                return False
        except ValueError:
            print("It's ok, I get too lost in the sauce as well, I'll just send you to the intro guy.")
            return True

def intro(skipped):
    
    if not skipped:
        delay_print(". . .\n")
        pause(1)
        delay_print("It seems it's just us here.\n")
        pause(1)
        delay_print("With no one else around . . . who knows what could happen here . . .\n")
        pause(1)
        print("I hope you're understanding what I'm getting at", end=' ')
        delay_print(". . . =) \n")
        pause(3)
        delay_print_fast("HELL YEAH THAT'S RIGHT WE'RE GONNA PLAY MADLIB, WOOHOO\n\n")

    if skipped:
        delay_print_fast(". . .\n")
        delay_print_fast("It seems it's just us here.\n")
        delay_print_fast("With no one else around . . . who knows what could happen here . . .\n")
        delay_print_fast("I hope you're understanding what I'm getting at . . . =) \n")
        delay_print_fast("HELL YEAH THAT'S RIGHT WE'RE GONNA PLAY MADLIB, WOOHOO\n")

def rules():
    
    choice = input("Do you know the rules? Yes/No: ")
    
    while True:
        
        if choice.lower() in ['y', "yes"]:
            
            delay_print_fast("Oh hell yeah save me the trouble!\n")
            return
            
        if choice.lower() in ['n', 'no']: 
            delay_print("Yeah I got you don't worry, it's simple\n")
            delay_print("Now watch as I word vomit the rules!\n\n")
            pause(1)
            print("Madlibs is a fun word game where players create a story by providing words (typically nouns, verbs, adjectives, etc.)")
            print("to fill in blanks in a pre-written story or sentence. I will prompt you with the appropriate words when needed! ")
            pause(3)
            return
        
        else:
            print("Mhm yes, so what you're saying is that you want the rules, got it, NO PROBLEM.")
            print("Madlibs is a fun word game where players create a story by providing words (typically nouns, verbs, adjectives, etc.)")
            print("to fill in blanks in a pre-written story or sentence. I will prompt you with the appropriate words when needed! ")
            pause(3)
            return

def read_template(file):
    try:
        with open(file, 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        raise FileNotFoundError(f"Pstt...hey boss I can't find the script at {file}. . !")

def parse_template(template):
    parts = re.findall(r'\{(.*?)\}', template)
    stripped_template = re.sub(r'\{.*?\}', '{}', template)
    return stripped_template, tuple(parts)

def merge(stripped_template, user_inputs):
    return stripped_template.format(*user_inputs)

def display_and_save_madlib(completed_madlib, output_file):
    print(completed_madlib)
    with open(output_file, 'w') as file:
        file.write(completed_madlib)

def main():
    skipped = start()
    intro(skipped)
    rules()

    template = read_template('madlib_template.txt')
    stripped_template, parts = parse_template(template)
    user_inputs = [input(f"Enter a {part}: ") for part in parts]
    completed_madlib = merge(stripped_template, user_inputs)
    display_and_save_madlib(completed_madlib, 'output_file.txt')

if __name__ == "__main__":
    main()