import ast
def isValid(stale, new, json):
    required_json = ast.literal_eval(json)
    current_cursor_position = 0
    temporary_string = stale
    if required_json:
        for dictionary in required_json :
            if dictionary and dictionary["op"] == "skip":
                 current_cursor_position+= dictionary["count"]
                 print("inside skip")
                 print(temporary_string)

            elif dictionary and dictionary["op"] == "delete":
                temporary_string = temporary_string[:current_cursor_position]+temporary_string[dictionary["count"]:]
                print("inside delete")
                print(temporary_string)

            elif dictionary and dictionary["op"]  == "insert":
                temporary_string=temporary_string[:current_cursor_position]+dictionary["chars"]+temporary_string[current_cursor_position+len(dictionary["chars"]):]
                current_cursor_position = current_cursor_position+len(dictionary["chars"])
                print("inside insert")
                print(temporary_string)


    print( temporary_string == new )









if __name__ == "__main__":

    # indexing is zero based
    # when you perform the insert operation
    # update the ending cursor position
    # when you perform the delete operation
    # do not update the cursor position
    # when you perforom the skip position update the cursor
    # you have to update cursor position after insert as well to the point
    # where your inserted character ends on the string

    isValid(
  'Repl.it uses operational transformations to keep everyone in a multiplayer repl in sync.',
  'We use operational transformations to keep everyone in a multiplayer repl in sync.',
  '[{"op": "delete", "count": 7}, {"op": "insert", "chars": "We"}, {"op": "skip", "count": 4}, {"op": "delete", "count": 1}]'
) # true
    #'Repl.it uses operational transformations to keep everyone in a multiplayer repl in sync.'
    #' uses operational transformations to keep everyone in a multiplayer repl in sync.'
    #'We uses operational transformations to keep everyone in a multiplayer repl in sync.'

