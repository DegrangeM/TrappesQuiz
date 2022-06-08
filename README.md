# TrappesQuiz

TrappesQuiz est un outil basé sur le jeu télévisé [Money Drop](https://fr.wikipedia.org/wiki/Money_Drop).

Python doit être installé pour que TrappesQuiz fonctionne.

## Principe

Les élèves commencent le jeu avec 1 000 000€.

Des questions (avec une unique réponse) leurs sont posées. Les élèves doivent alors miser leur argent sur la réponse qu'ils pensent être la bonne.

Lorsque la réponse est dévoilée, l'argent misée sur les mauvaises réponses est perdues (dans le jeu télévisée, l'argent est posée physiquement sur des trappes qui s'ouvrent).

Le jeu continue ainsi de question en question en perdant de l'argent à chaque mauvaise réponses.

A chaque question, plusieurs stratégies sont possibles :

- Soit l'élève est sûr de sa réponse et il peut miser tout son argent sur sa réponse

- Soit l'élève n'est pas sûr et doute entre plusieurs réponses et il peut répartir son argent sur les différentes réponses.

Avec la première stratégie, en cas d'erreur l'élève perd tout son argent. Avec la deuxième, il peut éviter de faire faillite, mais va assurément perdre de l'argent.

A noter qu'avec la seconde stratégie, il peut par exemple répartir équitablement l'argent entre toutes les réponses, ou bien en fonction de son intuition.
Par exemple, s'il est presque sûr que la bonne réponse est la A mais a un petit doute avec la réponse B, il peut miser 80% de son argent sur la réponse A et 20% de son argent sur la réponse B.

## Utilisation

Le fichier `trappequiz.py` doit être envoyé aux élèves. Le fichier `generer_mdp.py` ne doit pas être communiqué aux élèves mais gardé sur l'ordinateur de l'enseignant.

L'enseignant prépare ensuite sa grille de question/réponse (il peut aussi les inventer au fur et à mesure). Chaque question doit avoir quatre réponse (au moins, les élèves n'auront juste à ne pas miser sur les réponses inexistantes).

Les élèves doivent exécuter le fichier `trappequiz.py`. Une fenêtre en mode console s'ouvre (ou bien un logiciel pour programmer en python en fonction des logiciels installés sur l'ordinateur. Dans ce dernier cas les élèves doivent exécuter le programme). Le programme demande alors aux élèves de saisir le mot de passe de la question.

![image](https://user-images.githubusercontent.com/53106394/172583875-13d1b24e-8103-4149-b091-bcdd96fda346.png)

L'enseignant de son côté, exécute le fichier `generer_mdp.py` et tape le numéro de la question suivi de la lettre de la bonne réponse. Puisqu'il s'agit ici de la première question, l'enseignant devra taper 1A, 1B, 1C ou 1D. Le logiciel lui communique alors un code qu'il doit alors communiquer aux élèves (attention les majuscules et minuscules sont importantes !). Les élèves doivent alors saisir ce code sur leur ordinateur.

L'enseignant communique alors aux élèves la question et les réponses possibles (à l'écrit au tableau, à l'oral, etc.). Les élèves peuvent alors miser leur argent selon la répartition de leur choix.

Pendant ce temps, l'enseignant tape de son côté, le numéro de la question suivante suivi de la lettre de la bonne réponse, à savoir 2A, 2B, 2C ou 2D. Lorsqu'il juge que les élèves ont eu suffisement de temps pour miser leur argent, il peut éventuellement passer dans les rangs vérifier que tous les élèves ont bien validé leur mise (pour éviter la triche), puis corriger la question au tableau (ou à l'oral, etc.). Il communique alors le second code aux élèves qui le saisissent. Le logiciel indique alors à l'élève combien d'argent il a perdu sur cette question et combien il lui reste. Le jeu se poursuit ainsi de question en question.

Si jamais des élèves perdent tout leur argent, un "prêt" de 100€ leur est foruni afin qu'ils puissent continuer à jouer.

Lorsque l'enseignant souhaite arrêter le jeu, il saisi sur son logiciel le numéro de la question suivi de trois F. Par exemple 3FFF pour arrêter après avoir effectuer deux questions. Le jeu indique alors combien d'argent l'élève à réussi à conserver ainsi que le nombre de prêt contractés.


