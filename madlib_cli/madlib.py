import time, sys, re, os


def read_template(file):
    
    print("Current directory:", os.getcwd())
    
    """
    Reads the given text file, returns it as a string and checks to see if the file exists
    
    Parameters:
    file is a str, this is the path to the file location relative to the function call.
    
    Returns:
    A str with the contents of the file
    
    Raises:
    FileNotFoundError: If the file is not at the given location    
    """
    try:
        with open(file, 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        raise FileNotFoundError(f"Pstt...hey boss I can't find the script at {file}. . !")

    
def parse_template(template):
    
    """
    Parses the template to identify and remove placeholders
    
    Parameters:
    template is a str, a file containing text and placeholders
    
    Returns:
    tuple containing the placeholder and placeholder strings replaced by '{}'
    """
    
    parts = re.findall(r'\{(.*?)\}', template)
    stripped_template = re.sub(r'\{.*?\}', '{}', template)
    return stripped_template, tuple(parts)
    

def merge(stripped_template, user_inputs):
    
    """
    Merges the stripped templates with user-provided inputs(not currently)
    
    Parameters:
    stripped_template is a str, this contains the template {} placeholders
    user_inputs is a list of str, this contains the users_inputs to be entered into the template {} placeholders
    
    Returns:
    A str with the completed template
    """
    
    return stripped_template.format(*user_inputs)

    
def display_and_save_madlib(completed_madlib, output_file):
    print(completed_madlib)
    with open(output_file, 'w') as file:
        file.write(completed_madlib)
        
    """
    _summary_
    
    """


## Below is code I wish to work on to allow user inputs to affect the story

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
        delay_print_fast("HELL YEAH THAT'S RIGHT WE'RE GONNA PLAY MADLIB, WOOHOO\n\n")

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

def storytemplate(template):
    
    delay_print("Ok friend here is what we got to work with!\n\n")
    print(template)
    delay_print("Let's fill in those {Adjectives} and the like, with words shall we!\n\n")

def incompletestory(template, parts):
    
    delay_print("Alright friend I got a story for you.\n")
    delay_print("Let's start filling in this story with your own words.\n")
    print("I'll keep track of what you currently here after each input, I GOT YOU.")
    
    user_inputs = []
    
    while True:
        
        print(template)
        
        for word in parts:
            
            print("Ok friend it looks like I'm going to need a/an ," , word , "for this one!")
            user_input = input("What do you have for us?: ")
            user_inputs.append(user_input)
            delay_print("Here's how it's looking right now friend! \n")
            current_story = merge(template, user_inputs + list(parts[len(user_inputs):]))
            print(current_story)
            exit()
            
        

def main():
    skipped = start()
    intro(skipped)
    rules()
    
    template = read_template('madlib_cli\madlib_template.txt')
    
    storytemplate(template)
    
    stripped_template, parts = parse_template(template)
    
    print(stripped_template, parts)
    incompletestory(template, parts)
    # user_inputs = [input(f"Enter a {part}: ") for part in parts]
    # completed_madlib = merge(stripped_template, user_inputs)
    # display_and_save_madlib(completed_madlib, 'output_file.txt')

if __name__ == "__main__":
    main()