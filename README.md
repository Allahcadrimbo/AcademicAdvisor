# AcademicAdvisor
This program is an Eliza inspired academic advisor.

## Description:
In this PA we are attempting to create an Eliza inspired Academic Advisor that can have a continuous and relatively plausible discourse with a student looking for help. The Advisor doesn't have to actually provide any real information but the discussion should continue progressing through redirection on the part of the Advisor.

## Example Input and Output:
To run pa1.py: `python3 pa1.py' \
Advisor: Hey, I am an academic advisor. What is your name? \
Student: My name is Grant. \
Advisor: Nice to meet you Grant! What is your major? \
Student: I am majoring in Chemistry. \
Advisor: Awesome! Why did you choose Chemistry?

## Algorithm:
- Give the initial advisor response
- Take the student input
- Check that the student input isn't "quit"
    - If it is stop the program else continue
- Check the student input for obscenities
    - If there are no obscenities respond with canned response else check to see if it matches a pattern we created
- If it matches a pattern before responding make sure the advisor's response isn't the same as the last response
    - If it is respond with a conversation changer else respond with the pattern response
