animal(cat).
animal(fox).
animal(hippopotamus).
animal(antelope).
animal(raccoon).
animal(capibara).
animal(manul).
animal(snowfinch).
animal(hedgehog).
animal(giraffe).

% Характеристики животных
diet(cat, carnivore).
diet(fox, carnivore).
diet(hippopotamus, herbivore).
diet(antelope, herbivore).
diet(raccoon, omnivore).
diet(capibara, herbivore).
diet(manul, carnivore).
diet(snowfinch, herbivore).
diet(hedgehog, insectivore).
diet(giraffe, herbivore).

habitat(cat, domestic).
habitat(fox, forest).
habitat(hippopotamus, river).
habitat(antelope, savanna).
habitat(raccoon, forest).
habitat(capibara, river).
habitat(manul, steppe).
habitat(snowfinch, mountain).
habitat(hedgehog, forest).
habitat(giraffe, savanna).

has_tail(cat).
has_tail(fox).
has_tail(hippopotamus).
has_tail(antelope).
has_tail(raccoon).
has_tail(capibara).
has_tail(manul).
has_tail(snowfinch).
has_tail(hedgehog).
has_tail(giraffe).

% Правила для определения животных по характеристикам
herbivore_in_savanna(X) :- diet(X, herbivore), habitat(X, savanna).
animal_with_tail(X) :- has_tail(X).
carnivore_in_forest(X) :- diet(X, carnivore), habitat(X, forest).
omnivore_in_ocean(X) :- diet(X, omnivore), habitat(X, ocean).
animal_in_river(X) :- habitat(X, river).
insectivore(X) :- diet(X, insectivore).
