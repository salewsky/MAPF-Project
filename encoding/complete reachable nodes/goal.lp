processed(A,R) :- ordered(O,A), shelved(shelf(S),A), isRobot(robot(R)), position(shelf(S),C,0),
                  position(R,C,horizon), R=S.
processed(A)   :- processed(A,R).
:- ordered(O,A), not processed(A).



