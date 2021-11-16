#include "./input.lp".

time(1..Horizon) :- Horizon == #sum{1,X: init(object(node,X),_)}.


dir((X,Y)) :- X=-1..1, Y=-1..1, |X+Y|=1.

nextto((X,Y),(DX,DY),(X',Y')) :- dir((DX,DY)), position((X,Y)), position((X',Y')),
                                 (X,Y)=(X'-DX,Y'-DY), (X',Y')=(X+DX,Y+DY).
								 
0 {move(R,D,T) : dir(D)} 1 :- isRobot(robot(R)), time(T).

position(R,C,T) :- move(R,D,T), position(R,C',T-1),     nextto(C',D,C).
                :- move(R,D,T), position(R,C ,T-1), not nextto(C ,D,_).
position(R,C,T) :- position(R,C,T-1), not move(R,_,T), isRobot(robot(R)), time(T).



goal(R,C) :- isRobot(robot(R)), isShelf(shelf(S)), position(shelf(S),C,0), R=S.
:- isRobot(robot(R)), position(R,C1,Horizon), Horizon == #max{X: time(X)}, goal(R,C2), C1!=C2.

:- move(R,_,T1), not move(R,_,T2), time(T2), isRobot(robot(R)), T2<T1.
#minimize {1,T: move(_,_,T)}.

occurs(object(robot,R),action(move,D),T) :- move(R,D,T).
#show occurs/3.

