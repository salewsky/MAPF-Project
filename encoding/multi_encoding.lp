#program base.
robot(R)                     :- init(object(robot,R),_).
shelf(S)                     :- init(object(shelf,S),_).
station(P)                   :- init(object(pickingStation,P),_).
product(A)                   :- init(object(product,A),_).
order(O) 					 :- init(object(order,O),_).

isRobot(robot(R)) 		:- robot(R).
isShelf(shelf(S)) 		:- shelf(S).
isStation(station(T)) 	:- station(T).
isProduct(product(A)) 	:- product(A).
isOrder(order(O)) 		:- order(O).


ordered(order(O),product(A)) :- init(object(order,O),value(line,(A,_))).
target(order(O),station(P))  :- init(object(order,O),value(pickingStation,P)).
shelved(shelf(S),product(A)) :- init(object(product,A),value(on,(S,_))).        


position((X,Y))   				:- init(object(node,_),value(at,(X,Y))).
position(station(P),(X,Y))   	:- init(object(pickingStation,P), value(at,(X,Y))).
position(R,(X,Y),0) 			:- init(object(robot,R),value(at,(X,Y))).
position(shelf(S),(X,Y),0) 		:- init(object(shelf,S),value(at,(X,Y))).

dir((X,Y)) :- X=-1..1, Y=-1..1, |X+Y|=1.

nextto((X,Y),(DX,DY),(X',Y')) :- dir((DX,DY)), position((X,Y)), position((X',Y')),
                                 (X,Y)=(X'-DX,Y'-DY), (X',Y')=(X+DX,Y+DY).



occurs(object(robot,R),action(move,D),1) :- move(R,D,1).

#program check(t).
:- ordered(O,A), shelved(shelf(S),A), isRobot(robot(R)), position(shelf(S),C2,0),
   position(R,C1,t), C1!=C2, R=S, query(t).
   
#program step(t).
time(t).
0 {move(R,D,t) : dir(D)} 1 :- isRobot(robot(R)).

position(R,C,t) :- move(R,D,t), position(R,C',t-1),     nextto(C',D,C).
                :- move(R,D,t), position(R,C ,t-1), not nextto(C ,D,_).
occurs(object(robot,R),action(move,D),t) :- move(R,D,t).


#show occurs/3.