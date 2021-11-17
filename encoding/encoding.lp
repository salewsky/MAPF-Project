% Transforming Input ----------------------------
#include "./input.lp".

% Calculating Moves -----------------------------
#include "./action.lp".

% Goal Condition --------------------------------
#include "./goal.lp".

% Transforming Output ---------------------------
occurs(object(robot,R),action(move,D),T) :- move(R,D,T).
#show occurs/3.

