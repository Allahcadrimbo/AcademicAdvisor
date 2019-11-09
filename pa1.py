# Author: Grant Mitchell
# Date: 9/20/19
# PA #1 NLP
""" In this PA we are attempting to create an Eliza inspired Academic Advisor that can have a continuous and relatively
 plausible discourse with a student looking for help. The Advisor doesn't have to actually provide any real information
 but the discussion should continue progressing through redirection on the part of the Advisor. The following is example
 input and output for the program:

 Advisor: Hey, I am an academic advisor. What is your name?
 Student: My name is Grant.
 Advisor: Nice to meet you Grant! What is your major?
 Student: I am majoring in Chemistry.
 Advisor: Awesome! Why did you choose Chemistry?

Algorithm:
- Give the initial advisor response
- Take the student input
- Check that the student input isn't "quit"
    - If it is stop the program else continue
- Check the student input for obscenities
    - If there are no obscenities respond with canned response else check to see if it matches a pattern we created
- If it matches a pattern before responding make sure the advisor's response isn't the same as the last response
    - If it is respond with a conversation changer else respond with the pattern response
"""

import re

# Array of "bad words" to check for
obscenities = {
    "jerk", "punk", "scum", "idiot", "moron", "loser"
}

# List of patterns to compare the input against
patterns = [  # Comments are referring to the expression below them
    # Looks for "name is" and responds to them by asking their major
    [r'.*\bname is\b (\w+).*', r'Nice to meet you \1! What is your major?'],
    # Looks for "majoring in" and responds by asking them if they like their major
    [r'.*\bmajoring in\b (\w+).*', r'Awesome! What made you want to major in \1?'],
    # Looks for "a <major> major" and responds by asking them if they like it
    [r'.*\ba\b (\w+) \bmajor\b.*', r'Awesome! Do you like \1?'],
    # Looking for "I feel x"
    [r'.*\b[Ii] feel\b ([\w\s]+).*', r'Why do you feel \1?'],
    # Word matching for "like" and asks them why do/don't like whatever they say
    [r'.* ([\w\'-]+)\s\blike\b ([\w\s]+).*', r'Tell me more about why you \1 like \2?'],
    # Looks for "I want" and asks them why they want xyz
    [r'.*I want ([\w\s]+).*', r'Why do you want \1?'],
    # Looks for "You <word> me" and responds with why do you say xyz
    [r'^.*\b[Yy]ou\b (.*) \bme\b.*', r"Why do you say I \1 you?"],
    # Looks for "He <word> me" and responds with why do you say xyz
    [r'.*\b[Hh]e\b (\w+) \bme\b ([\w\s]+).*', r"Why do you say he \1 you \2?"],
    # Looks for "She <word> me" and responds with why do you say xyz
    [r'^\b[Ss]he\b (\w+) \bme\b (\w+).*', r"Why do you say she \1 you \2?"],
    # Looks for "I <word> me" and responds with why do you say xyz
    [r'^\b[Ii]\b (\w+) \bmy\b (\w+).*', r"What makes you say you \1 your \2?"],
    # Looks for "on track for/to" and responds with asking if they think they are
    [r'.*\bon track (for|to)\b (\w+).*', r'Do you think you are on track \1 \2?'],
    # Looks for x really x and responds asking them why that x is really x
    [r'.*really (\w+).*', r'What about it is really \1?'],
    # Looking for "have enough x"
    [r'.*\bhave enough\b ([\w\s]+).*', r'Do you think you have enough \1?'],
    # Looking for "how many x"
    [r'.*\b[Hh]ow many\b ([\w\s]+).*', r'I do not know how many \1. You tell me!'],
    # Looking for not sure
    [r'.*\bnot sure\b.*', r'Why are you not sure?'],
    # Looking for "am sure"
    [r'.*\bam sure\b.*', r'I am glad to hear you are sure. It is good to be confident in our beliefs.'],
    # Looking for the phrase "What classes do I need to x"
    [r'.*\b[Ww]hat classes do I need to\b ([\w\s]+).*', r'The classes you need to \1 depend on your goals! What are your goals?'],
    # Word matching for "goal"
    [r'.*\bgoal\b.*', r'That is a terrific goal! Is there anything else I can help you with?'],
    # Looking for "drop out"
    [r'.*\bdrop out\b.*', r'You really want to dropout? Why?'],
    # Looking for "I always"
    [r'.*\b[Ii] always\b ([\w\s]+).*', r'Why do you always \1?'],
    # Looking for "Bye" or "Goodbye"
    [r'.*\b([Bb]ye|[Gg]oodbye)\b.*', r'\1.'],
    # Looking for "going to x"
    [r'.*\bgoing to\b ([\w\s]+).*', r'Do you really think you are going to \1?'],
    # Looking for "I think x" and the responding accordingly
    [r'.*\b[Ii] think\b ([\w\s]+).*', r'Are you sure you think \1?'],
    # Word matches for "question"
    [r'.*\bquestion\b.*', "You have a question? What is it?"]
]


# This function scans the student input for any "bad words"
def check_for_obscenities(student_input):
    has_obscenities = False

    # Loop through all of the "bad words" in the obscenities array, and if there is a match then has_obscenities is true
    for bad_words in obscenities:
        if bad_words in student_input:
            has_obscenities = True

    # If there aren't any bad words try to match their input to our patterns else tell them to watch their language
    if not has_obscenities:
        return check_for_response(student_input)
    else:
        return "Don't use those kinds of words here. Please try again using appropriate language."


# Used to keep track of what you last said by the advisor
last_response = ""


# This function takes the students input and see if it fits any of our patterns. If it does it returns the corresponding
# response and if it doesn't it tells the user to expand on their statement.
def check_for_response(student_input):
    global last_response

    # Patterns is a list of lists. So we loop through each sub list. Each sublist has two element hence the two variable
    # for loop. If there is a match we print the response pattern with info pulled fom the input patter.
    for input_pattern, response_pattern in patterns:
        if re.match(input_pattern, student_input):

            # If the next response is going to be the same as the last response then pivot the conversation becuase it
            # going in a circle
            if last_response != re.sub(input_pattern, response_pattern, student_input):
                last_response = re.sub(input_pattern, response_pattern, student_input)
                return last_response
            else:
                return "Can I help you with anything else?"

    return "Expand on that."


# Starts the program up and handles initial behavior
def main():
    print("This is Eliza the Academic Advisor, programmed by Grant Mitchell.\n")

    # Give the initial greeting to the advisee
    print("Hey, I am an academic advisor. What is your name?\n")
    student_input = ''

    # Continue to converse until the advisee enters exit
    while student_input != "exit":
        student_input = input()

        if student_input != "exit":
            print(check_for_obscenities(student_input))


if __name__ == "__main__":
    main()
