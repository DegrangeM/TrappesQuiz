import locale
from base64 import b64decode
locale.setlocale(locale.LC_ALL, 'fr_FR.UTF-8')
argent = 1000000
n = 1
mdpOK = False
prets = 0
pertes = 0
while True :
	while True :
		if mdpOK :
			break
		mdp = input("Mot de passe de la question ? ")
		try :
			mdp = int(b64decode(mdp))
			mdp = hex(mdp)
			if (mdp[-1:] in ('a','b','c','d') and int(mdp[2:-1]) == n) or (mdp[-3:] == 'fff' and int(mdp[2:-3]) == n) :
				reponse = mdp[-1].upper()
				break
			print("Erreur dans le mot de passe.")
			continue
		except :
			print("Erreur dans le mot de passe.")
			continue
		break
	if mdp[-3:] == 'fff' :
		break
	mdpOK = True
	if n > 1 :
		print("Les trappes des mauvaises réponses s'ouvrent et vous perdez {:n}€.".format(pertes))
	if argent == 0 :
		print("Vous n'avez plus d'argent ! Pour vous permettre de continuer à jouer, nous vous avons redonné 100€.")
		argent = 100
		prets += 1
	print("Vous avez {}€.".format(argent))
	print("Question n°{} :".format(n))
	total = 0
	try :
		rA = int(input("Combien d'argent souhaitez-vous mettre sur la réponse A ? Il vous reste {:n}€ à miser. ".format(argent-total)).replace(' ','') or "0")
	except :
		print("Erreur dans le montant.")
		continue
	if rA < 0 :
		print("Vous ne pouvez pas miser un montant négatif.")
		continue
	total += rA
	if total > argent :
		print("Vous ne pouvez pas miser plus d'argent que vous avez.")
		continue
	try :
		rB = int(input("Combien d'argent souhaitez-vous mettre sur la réponse B ? Il vous reste {:n}€ à miser. ".format(argent-total)).replace(' ','') or "0")
	except :
		print("Erreur dans le montant.")
		continue
	if rB < 0 :
		print("Vous ne pouvez pas miser un montant négatif.")
		continue
	total += rB
	if total > argent :
		print("Vous ne pouvez pas miser plus d'argent que vous avez.")
		continue
	try :
		rC = int(input("Combien d'argent souhaitez-vous mettre sur la réponse C ? Il vous reste {:n}€ à miser. ".format(argent-total)).replace(' ','') or "0")
	except :
		print("Erreur dans le montant.")
		continue
	if rC < 0 :
		print("Vous ne pouvez pas miser un montant négatif.")
		continue
	total += rC
	if total > argent :
		print("Vous ne pouvez pas miser plus d'argent que vous avez.")
		continue
	#rD = int(input("Combien d'argent souhaitez-vous mettre sur la réponse D ? Il vous reste {:n}€ à miser. ".format(argent-total)).replace(' ',''))
	#total += rD
	rD = argent - total
	total += rD
	#total = rA + rB + rC + rD
	#if rA < 0 or rB < 0 or rC < 0 or rD < 0 :
	#	print("Vous ne pouvez pas miser un nombre négatif d'argent !")
	#	continue
	#if total != argent :
	#	print("Vous avez misé {:n}€, or vous devez miser {:n}€ !".format(total, argent))
	#	continue
	pA = rA/total
	pB = rB/total
	pC = rC/total
	pD = rD/total
	print("Vous avez misez les montants suivant : ")
	print("Réponse A : {:n}€ ({:2.2%})".format(rA, pA))
	print("Réponse B : {:n}€ ({:2.2%})".format(rB, pB))
	print("Réponse C : {:n}€ ({:2.2%})".format(rC, pC))
	print("Réponse D : {:n}€ ({:2.2%})".format(rD, pD))
	while True :
		confirm = input("Confirmez vous la mise (Oui/Non) ? ")
		if confirm.lower() == 'oui' or confirm.lower() == 'non' :
			break
	if confirm.lower() == 'non' :
		continue
	n += 1
	if reponse == 'A' :
		argent = rA
	if reponse == 'B' :
		argent = rB
	if reponse == 'C' :
		argent = rC
	if reponse == 'D' :
		argent = rD
	pertes = total - argent
	mdpOK = False
print("FIN DU JEU")
print("Vous avez terminé le jeu avec {}€ en utilisant {} prêt(s).".format(argent, prets))
while input("Ecrire FIN pour terminer le jeu. ") != "FIN" :
	pass