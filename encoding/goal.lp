processed(A,R) :- ordered(O,A), shelved(S,A), isRobot(robot(R)), position(S,C,0),
                  position(R,C,Horizon), Horizon == #max{X: time(X)}.
processed(A)   :- processed(A,R).
:- ordered(O,A), not processed(A).