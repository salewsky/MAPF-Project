% Declaring Time Array ------------------------------------------------------------------
time(1..Horizon) :- Horizon == #sum{1,C: comb_position(C,_,_)}.
horizon(Horizon) :- Horizon == #max{X: time(X)}.

% Declaring Directions ------------------------------------------------------------------
dir((X,Y)) :- X=-1..1, Y=-1..1, |X+Y|=1.

nextto((X,Y),(DX,DY),(X',Y')) :- dir((DX,DY)), comb_position((X,Y)), comb_position((X',Y')),
                                 (X,Y)=(X'-DX,Y'-DY), (X',Y')=(X+DX,Y+DY).
								 


% Calculating Moves and Positions -------------------------------------------------------
0 {move(R,D,T) : dir(D)} 1 :- isRobot(robot(R)), time(T).

comb_position(R,C,T) :- move(R,D,T), comb_position(R,C',T-1), nextto(C',D,C).
                :- move(R,D,T), comb_position(R,C ,T-1), not nextto(C ,D,_).
comb_position(R,C,T) :- comb_position(R,C,T-1), not move(R,_,T), isRobot(robot(R)), time(T).


imp_position(C') :- comb_position(R,C,_), comb_position(C,_,C').


% Minimizing Steps ----------------------------------------------------------------------
:- move(R,_,T1), not move(R,_,T2), time(T2), isRobot(robot(R)), T2<T1.
#minimize {1,T: move(_,_,T)}.



