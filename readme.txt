Task:2
NAME: Sai Parthish Mandumula.
UTA ID: 1002022847.

CODE STRUCTURE:
    IterateAvailableSlots  functions is to calculate  for available moves.

    ComputeBoardInstance  function is declare to know the  game board state.

    FetchMin and FetchMax functions calculate the subsequent of min and max values for each printGameBoardToFile

    FetchResultValue function calculates the utility value for the terminal nodes, description in eval_explanation.txt

    the maxConnect4.py is the driver and is used to toggle the interactive and one move mode.




COMPILATION AND EXECUTION:
    To compile for single move mode:
        python maxconnect4.py one-move input1.txt output1.txt

        Output is printed in output argument file

    To compile for interactive mode:
        python maxconnect4.py interactive [input_file] [computer-next/human-next] [depth]

        Output for computer player is in computer.txt
        Output for Human player is in human.txt

DEPTH TIME MAPPING:
    It is in depth-time map.pdf

    Have used the following Terminal command to generate the raw output in time.xlsx
