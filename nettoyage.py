


import pandas as pd
import unicodedata

# ============================================================
# 1. FONCTION : NETTOYER LES DATES
# ============================================================

def nettoyer_dates(df):
    dates_avant = df["date_commande"].copy()

    df["date_commande"] = pd.to_datetime(
        df["date_commande"],
        errors="coerce",
        format="mixed",
        dayfirst=True
    )
    return df


# ============================================================
# 2. FONCTION : RECUPERER COLONNES STRING
# ============================================================
def recuperer_colonnes_string(df):
    liste_colonnes_non_string = [
        "id_commande",
        "date_commande",
        "id_client",
        "id_produit",
        "quantite",
        "prix_unitaire"
    ]
    liste_colonnes_string = []
    for colonne in df.columns:
        if colonne not in liste_colonnes_non_string:
            liste_colonnes_string.append(colonne)
    return liste_colonnes_string


# ============================================================
# 3. FONCTION : NETTOYER COLONNES STRING
# ============================================================

def nettoyer_colonnes_string(df, liste_colonnes_string):
    for colonne in liste_colonnes_string:
        df[colonne] = (
            df[colonne]
                       .astype("string")
                       .str.upper()
                       .str.strip()
        )
        df[colonne] = df[colonne].apply(
            lambda texte: "".join(
                caractere
                for caractere in unicodedata.normalize("NFD", texte)
                if unicodedata.category(caractere) != "Mn"
            )
            if pd.notna(texte)
            else texte
        )
    return df