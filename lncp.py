#Created by Jackson Hoagland on 1/27/2018

welcome_message = "Welcome to Line Complete. This program will complete repetitive typing tasks for you.\n\n" \
                  "To begin, type your text pattern as follows using \"[]\" to indicate a variable location:\n" \
                  "[Your text 1 here][][Your text 2 here][]\n" \
                  "Once you have entered your pattern, enter the comma separated variables you wish to fill the pattern with.\n\n" \
                  "For example:\n" \
                  "My favorite color is [] and my favorite number is [].\n" \
                  "Green, Blue\n" \
                  "9,100\n\n" \
                  "Will output:\n" \
                  "My favorite color is Green and my favorite number is 9\n" \
                  "My favorite color is Blue and my favorite number is 100\n"

enter_pattern_message = "Please enter your text pattern:\n"

#enter_filedir_message = "Please enter the file you want to save the text to. Leave blank to output on terminal.\n"

enter_delimiter_message = "Please enter a string or character delimiter for your input data.\n"

enter_variables_message = "Please enter the variables, separated by commas.\n"

empty_values_warning_message = "WARNING: Not all variable lists are the same length. Empty values have been inserted at the missing locations.\n"

delimiter = ','

def main():
    trailing_variable = False
    print(welcome_message)

    while(True):
        rawTextPattern = input(enter_pattern_message)

        if(rawTextPattern.endswith("[]")):
            trailing_variable=True

        textPattern = rawTextPattern.split("[]")

        numVariables = len(textPattern)-1

        variablesList = list()

        delimiter = input(enter_delimiter_message)

        for i in range(0,numVariables):
            variablesList.append(input(enter_variables_message).split(delimiter))

        numRows = longest(variablesList)

        print("\nOutput:")

        emptyValuesWarning = False

        for i in range(0,numRows):
            output = ""
            for j in range(0,len(variablesList)):
                output += textPattern[j]

                if(i>=len(variablesList[j])):
                    emptyValuesWarning=True
                    output+=''
                else:
                    output += variablesList[j][i]

            output+=textPattern[j+1]
            print(output)

        print("\n")
        if(emptyValuesWarning):
            print(empty_values_warning_message)

def longest(l): #https://stackoverflow.com/questions/30902558/finding-the-longest-list-in-a-list-of-lists-in-python
    if(not isinstance(l, list)): return(0)
    return(max([len(l),] + [len(subl) for subl in l if isinstance(subl, list)] +
               [longest(subl) for subl in l]))

if __name__ == '__main__':
    main()