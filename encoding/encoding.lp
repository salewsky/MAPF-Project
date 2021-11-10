#include "./input.lp".

time(1..horizon).

dir((X,Y)) :- X=-1..1, Y=-1..1, |X+Y|=1.

nextto((X,Y),(DX,DY),(X',Y')) :- dir((DX,DY)), position((X,Y)), position((X',Y')),
                                 (X,Y)=(X'-DX,Y'-DY), (X',Y')=(X+DX,Y+DY).
								 
0 { move(R,D,T) : dir(D) } 1 :- isRobot(robot(R)), time(T).

position(R,C,T) :- move(R,D,T), position(R,C',T-1),     nextto(C',D,C).
                :- move(R,D,T), position(R,C ,T-1), not nextto(C ,D,_).
				
position(R,C,T) :- position(R,C,T-1), not move(R,_,T), isRobot(robot(R)), time(T).



goal(R,C) :- isRobot(robot(R)), isShelf(shelf(S)), position(shelf(S),C,0), R=S.
:- isRobot(robot(R)), position(R,C1,horizon), goal(R,C2), C1!=C2.

#minimize {1,(_,D,T): occurs(R,D,T)}.

occurs(object(robot,R),action(move,D),T) :- move(R,D,T).
#show occurs/3.

