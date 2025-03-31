roditel(abraam, gomer).
roditel(mona, gomer).
roditel(klansi, marjd).
roditel(djekki, marjd).
roditel(gomer, bart).
roditel(gomer, liza).
roditel(gomer, meggi).
roditel(marjd, bart).
roditel(marjd, liza).
roditel(marjd, meggi).
roditel(klansi, patti).
roditel(djekki, patti).
roditel(klansi, selma).
roditel(djekki, selma).
roditel(selma, ling).
roditel(abraam, gerb).

male(abraam).
male(gomer).
male(klansi).
male(gerb).
male(bart). 

female(djekki).
female(mona).
female(marjd).
female(liza).
female(meggi).
female(patti).
female(selma).
female(ling).


father(X,Y) :- roditel(X,Y), male(X).
morter(X,Y) :- roditel(X,Y), female(X).

% Брат и сестра
brother(X, Y) :- male(X), roditel(Z, X), roditel(Z, Y), X \= Y.
sister(X, Y) :- female(X), roditel(Z, X), roditel(Z, Y), X \= Y.

% Дядя и тётя
uncle(X, Y) :- male(X), (brother(X, Z); sister(X, Z)), roditel(Z, Y).
aunt(X, Y) :- female(X), (brother(Z, X); sister(Z, X)), roditel(Z, Y).

% Племянник и племянница
nephew(X, Y) :- male(X), (brother(Y, Z); sister(Y, Z)), roditel(Z, X).
niece(X, Y) :- female(X), (brother(Y, Z); sister(Y, Z)), roditel(Z, X).

% Свекровь
mother_in_law(X, Y) :- female(X), (roditel(Z, Y), (husband(Z, Y); wife(Z, Y))).

husband(abraam, mona).
husband(klansi, djekki).
husband(gomer, marjd).

wife(mona, abraam).
wife(djekki, klansi).
wife(marjd, gomer).
