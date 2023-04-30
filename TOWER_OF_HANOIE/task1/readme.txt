Name : Sai Parthish Mandumula
ID : 1002022847

To Start with execute the following command:
  make graphplan

Tower of Hanoi:
  We have 2 objects :  Peg and a Disk
  Disks are labled : disk1, disk2, disk3, disk4, disk5
  Peg = A, B, C 

  Understanding the literals:
  1. clear <Disk> : Nothing on 'Disk'
  2. clear <Peg> : Nothing on a 'Peg'
  3. on <Disk-1> <Disk-2> : 'Disk-2' is placed on 'Disk=1'        
  4. on <Disk> <Peg> : 'Disk' is placed on 'Peg'

  There are four functions defined to move a Disk. They are:
  1. moveFromPegToPeg   - move disk from peg to another peg
  2. moveFromPegToDisk  - move disk to another peg which has disk
  3. moveFromDiskToPeg  - move disk to empty peg
  3. moveFromDiskToDisk - move disk to another disk (different pegs)

  To run the program :
    ./graphplan -o hanoi/hanoi_ops.txt -f hanoi/{your desired facts file}.txt


7 Puzzle:
  There are three objects defined. That is a Piece, an Empty and a Location
  Pieces are numbered 1234567
  'X' means empty

  Explanation
  1. on <Piece> <Location> : Piece 'x' is on Location 'y'
  2. adj <Location> <Location> : two locations are adjacent

  Functions:
  1. move - move piece to 'Empty' location

  to run program:
    ./graphplan -o 7puzzle/7puzzle_ops.txt -f 7puzzle/{your desired facts file}.txt

