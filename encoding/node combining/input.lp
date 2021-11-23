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


max_X(A) :- A = #max{X: init(object(node,_),value(at,(X,_)))}.
max_Y(A) :- A = #max{Y: init(object(node,_),value(at,(_,Y)))}.


comb_position((1,1),1,(1..2,1..2)).
comb_position((2,1),2,(3..4,1..2)).
comb_position((3,1),3,(5..6,1..2)).
comb_position((4,1),4,(7..8,1..2)).
comb_position((1,2),5,(1..2,3..4)).
comb_position((2,2),6,(3..4,3..4)).
comb_position((3,2),7,(5..6,3..4)).
comb_position((4,2),8,(7..8,3..4)).
comb_position((1,3),9,(1..2,5..6)).
comb_position((2,3),10,(3..4,5..6)).
comb_position((3,3),11,(5..6,5..6)).
comb_position((4,3),12,(7..8,5..6)).
comb_position((1,4),13,(1..2,7..8)).
comb_position((2,4),14,(3..4,7..8)).
comb_position((3,4),15,(5..6,7..8)).
comb_position((4,4),16,(7..8,7..8)).


comb_position((X,Y)) :- comb_position((X,Y),_,_).


comb_position(R,C,0) :- position(R,C',0), comb_position(C,_,C').
comb_position(shelf(S),C,0) :- position(shelf(S),C',0), comb_position(C,_,C').

 



