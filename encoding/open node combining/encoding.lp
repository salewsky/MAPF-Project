% Transforming Input ----------------------------
#include "./input.lp".

% Calculating Moves -----------------------------
#include "./action.lp".

% Goal Condition --------------------------------
#include "./goal.lp".

% Transforming Output ---------------------------
new_init(object(node,N),value(at,(X,Y)))  :- imp_position((X,Y)), init(object(node,N),value(at,(X,Y))).
new_init(object(robot,R),value(at,(X,Y))) :- init(object(robot,R),value(at,(X,Y))).
new_init(object(shelf,S),value(at,(X,Y))) :- init(object(shelf,S),value(at,(X,Y))).

#show new_init/2.

