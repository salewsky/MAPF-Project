init(object(node,N),value(at,(X,Y))) :- new_init(object(node,N),value(at,(X,Y)),A), A<=1.
init(object(robot,R),value(at,(X,Y))) :- new_init(object(robot,R),value(at,(X,Y))).
init(object(shelf,S),value(at,(X,Y))) :- new_init(object(shelf,S),value(at,(X,Y))).

#show init/2.