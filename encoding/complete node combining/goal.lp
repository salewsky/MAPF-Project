goal(R,C) :- isRobot(robot(R)), comb_position(shelf(S),C,0), R=S.
:- isRobot(robot(R)), comb_position(R,C,horizon), goal(R,C'), C!=C'.

%processed(A,R) :- ordered(O,A), shelved(shelf(S),A), isRobot(robot(R)), comb_position(shelf(S),C,0),
%                  comb_position(R,C,horizon), R=S.
%processed(A)   :- processed(A,R).
%:- ordered(O,A), not processed(A).







