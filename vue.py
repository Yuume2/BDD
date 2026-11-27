from typing import List
from rich.panel import Panel
from rich.columns import Columns
from rich.layout import Layout
from typing import Callable
from affichage import Affichage
from game import Character, Enemy, Item
from model import SaveDB, ScoreDB
OPTIONS_TOUR = ["Attaquer", "Utiliser un objet", "Passer"]
OPTIONS_ECRAN_TITRE = ["Nouvelle Partie",
                       "Charger Partie", "Leaderboard", "Quitter"]
OPTIONS_GAME_OVER = ["Retour à l'écran titre", "Quitter"]


def create_columns(cols) -> Layout:
	layout = Layout()

	# Ratios selon le nombre de colonnes (1, 2 ou 3)
	ratios = {1: [1], 2: [1, 1], 3: [2, 3, 2]}[len(cols)]

	layout.split_row(
		*[Layout(name=f"col{i}", ratio=r) for i, r in enumerate(ratios)]
	)
	# Assigner les colonnes aux différentes sections
	for i, col in enumerate(cols):
		layout[f"col{i}"].update(col)

	return layout


def details_objet(objet: Item) -> str:
	lignes = [
		objet.name,
		objet.description,
		f"Type : {objet.item_type}",
		f"Rareté : {objet.rarity}",
	]
	for stat, valeur in objet.stats.items():
		lignes.append(f"{stat} : {valeur:+d}")
	return "\n".join(lignes)


def details_sauvegarde(sauvegarde: SaveDB) -> str:
	lignes = [f"Joueur : {sauvegarde.player_name}", f"Score : {sauvegarde.score}"]
	lignes += ["", "Characters"]
	lignes += [f"{perso.name} - PV {perso.hp}" for perso in sauvegarde.equipe]
	lignes += ["", "Monstres"]
	lignes += [f"{monstre.name} - PV {monstre.hp}" for monstre in sauvegarde.monsters]
	lignes += ["", "Inventaire"]
	lignes += [objet.name for objet in sauvegarde.inventaire] or ["Vide"]
	return "\n".join(lignes)


def vue_inventaire(inventaire: List[Item], team: List[Character]) -> Callable:
	def create_details_info(index: int) -> str:
		if not inventaire:
			return "Inventaire vide"
		return details_objet(inventaire[index])

	def inner_vue_inventaire(index: int):
		selected_box = Affichage.create_select_box(
			titre="Inventaire",
			items=inventaire,
			index=index,
			box_color="blue",
			text_color="white",
			hover_color="yellow"
		)

		details = Affichage.create_info_box(
			titre="Détails",
			info=create_details_info(index),
			box_color="magenta",
			text_color="white"

		)
		team_box = Affichage.create_info_box(
			titre="Characters",
			info="\n".join(str(member) for member in team),
			box_color="green",
			text_color="white"
		)

		return create_columns([
			selected_box,
			details,
			team_box
		])

	return inner_vue_inventaire


def vue_selection_cible_objet(objet: Item, team: List[Character]) -> Callable:
	def inner_vue_selection_cible_objet(index: int):

		selected_box = Affichage.create_select_box(
			titre=f"Choisir une cible pour {objet}",
			items=team,
			index=index,
			box_color="blue",
			text_color="white",
			hover_color="yellow"
		)
		details = Affichage.create_info_box(
			titre="Détails de l'objet",
			info=details_objet(objet),
			box_color="magenta",
			text_color="white"
		)

		return create_columns([
			selected_box,
			details
		])

	return inner_vue_selection_cible_objet


def vue_tour_joueur(team: List[Character], perso: Character, ennemis: List[Enemy]) -> Callable:

	def inner_vue_tour_joueur(index: int):
		selected_box = Affichage.create_info_box(
			titre=f"Tour du personnage : {perso.name}",
			info="\n".join(str(member) for member in team),
			box_color="blue",
			text_color="white",
		)

		details = Affichage.create_select_box(
			titre="Choix d'action",
			items=OPTIONS_TOUR,
			index=index,
			box_color="magenta",
			text_color="white",
			hover_color="yellow"
		)

		ennemis_box = Affichage.create_info_box(
			titre="Ennemis",
			info="\n".join(str(enemy) for enemy in ennemis),
			box_color="red",
			text_color="white"
		)

		return create_columns([
			selected_box,
			details,
			ennemis_box
		])

	return inner_vue_tour_joueur


def vue_choix_cible(perso: Character, ennemis: List[Enemy]) -> Callable:
	def inner_vue_choix_cible(index: int):

		perso_box = Affichage.create_info_box(
			titre="Personnage Attaquant",
			info=str(perso),
			box_color="magenta",
			text_color="white"
		)

		selected_box = Affichage.create_select_box(
			titre=f"Choisir une cible pour {perso.name}",
			items=ennemis,
			index=index,
			box_color="blue",
			text_color="white",
			hover_color="yellow"
		)

		details = Affichage.create_info_box(
			titre="Projection des degats pour la cible",
			info=str(perso.ProjectDamage(ennemis[index])),
			box_color="magenta",
			text_color="white"
		)

		return create_columns([
			perso_box,
			details,
			selected_box
		])

	return inner_vue_choix_cible


def vue_info_tour(team: List[Character], event: str, ennemis: List[Enemy]) -> Callable:
    def inner_vue_info_tour(index: int):
        team_box = Affichage.create_info_box(
            titre="Characters",
            info="\n".join(str(member) for member in team),
            box_color="blue",
            text_color="white"
        )

        event_box = Affichage.create_info_box(
            titre="Event",
            info=event,
            box_color="magenta",
            text_color="white"
        )

        ennemis_box = Affichage.create_info_box(
            titre="Ennemis",
            info="\n".join(str(enemy) for enemy in ennemis),
            box_color="red",
            text_color="white"
        )

        return create_columns([
            team_box,
            event_box,
            ennemis_box
        ])

    return inner_vue_info_tour


def vue_selection_equipe(team: List[Character], list_selection: List[Character]) -> Callable:
    def inner_vue_selection_equipe(index: int):
        team_box = Affichage.create_info_box(
            titre="Characters",
            info="\n".join(str(member) for member in team),
            box_color="blue",
            text_color="white"
        )

        selection_box = Affichage.create_select_box(
            titre="Sélection de l'équipe",
            items=list_selection,
            index=index,
            box_color="magenta",
            text_color="white",
            hover_color="yellow"
        )

        return create_columns([
            team_box,
            selection_box
        ])

    return inner_vue_selection_equipe


def vue_ecran_titre() -> Callable:

	def inner_vue_ecran_titre(index: int):
		return Affichage.create_select_box(
			titre="Écran Titre",
			items=OPTIONS_ECRAN_TITRE,
			index=index,
			box_color="cyan",
			text_color="white",
			hover_color="yellow"
		)

	return inner_vue_ecran_titre


def vue_leaderboard(scores: List[ScoreDB]) -> Callable:
	def inner_vue_leaderboard(index: int):
		if scores:
			info = "\n".join(
				f"{rang}. {score.player_name} - {score.score}"
				for rang, score in enumerate(scores, start=1)
			)
		else:
			info = "Aucun score enregistré"

		return Affichage.create_info_box(
			titre="Leaderboard",
			info=info,
			box_color="yellow",
			text_color="white"
		)

	return inner_vue_leaderboard


def vue_game_over() -> Callable:

	def inner_vue_game_over(index: int):
		return Affichage.create_select_box(
			titre="Game Over",
			items=OPTIONS_GAME_OVER,
			index=index,
			box_color="red",
			text_color="white",
			hover_color="yellow"
		)

	return inner_vue_game_over


def vue_charger_sauvegarde(sauvegardes: List[SaveDB]) -> Callable:
	def create_details_info(index: int) -> str:
		if not sauvegardes:
			return "Aucune sauvegarde disponible"
		return details_sauvegarde(sauvegardes[index])

	def inner_vue_charger_sauvegarde(index: int):
		selected_box = Affichage.create_select_box(
			titre="Charger une sauvegarde",
			items=[f"{save.player_name} - {save.score}" for save in sauvegardes],
			index=index,
			box_color="blue",
			text_color="white",
			hover_color="yellow"
		)

		details = Affichage.create_info_box(
			titre="Détails",
			info=create_details_info(index),
			box_color="magenta",
			text_color="white"
		)

		return create_columns([
			selected_box,
			details
		])

	return inner_vue_charger_sauvegarde


def vue_quitter() -> Callable:
	def inner_vue_quitter(index: int) -> Panel:
		return Panel("Quitter le jeu")

	return inner_vue_quitter