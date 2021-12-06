new_init(object(node,N),value(at,(X,Y)),N)  		:- imp_position(_,(X,Y),N), init(object(node,N),value(at,(X,Y))).
new_init(object(node,N),value(at,(X,Y))) 			:- init(object(pickingStation,P),value(at,(X,Y))), init(object(node,N),value(at,(X,Y))).
new_init(object(robot,R),value(at,(X,Y))) 			:- init(object(robot,R),value(at,(X,Y))).
new_init(object(shelf,S),value(at,(X,Y))) 			:- init(object(shelf,S),value(at,(X,Y))).
new_init(object(order,O),value(line,(T,U))) 		:- init(object(order,O),value(line,(T,U))).
new_init(object(order,O),value(pickingStation,P)) 	:- init(object(order,O),value(pickingStation,P)).
new_init(object(product,P),value(on,(T,U))) 		:- init(object(product,P),value(on,(T,U))).
new_init(object(pickingStation,P),value(at,(X,Y))) 	:- init(object(pickingStation,P),value(at,(X,Y))).

#show new_init/3.
#show new_init/2.