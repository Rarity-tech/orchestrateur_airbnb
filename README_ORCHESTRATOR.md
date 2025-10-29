# 🚀 Orchestrateur Airbnb - Guide Complet

## 📋 Vue d'ensemble

Ce système automatise **complètement** le scraping d'Airbnb en 2 phases :
1. **Phase 1** : Scraping des annonces (Python + Playwright)
2. **Phase 2** : Scraping des profils hôtes (Node.js + Puppeteer)

**Résultat** : Un fichier CSV unifié avec toutes les données !

---

## 🎯 Avantages

✅ **Automatique** : Lancez et oubliez (4-6h d'exécution)  
✅ **Résilient** : Continue même si une page échoue  
✅ **Intelligent** : Évite les doublons d'hôtes  
✅ **Page par page** : Pas de timeout GitHub Actions  
✅ **Complet** : Fusionne automatiquement toutes les données  

---

## 📂 Structure des fichiers

```
votre-repo/
├── .github/
│   └── workflows/
│       ├── scrape.yml              # Workflow Phase 1 (existant)
│       ├── scrape-airbnb.yml       # Workflow Phase 2 (existant)
│       └── orchestrator.yml        # 🆕 Nouveau workflow orchestrateur
├── scrape_airbnb.py                # Script Python (existant)
├── scraper.js                      # Script Node.js (existant)
├── requirements.txt                # (existant)
├── package.json                    # (existant)
├── merge_results.py                # 🆕 Script de fusion
├── search_urls.txt                 # 🆕 Votre liste d'URLs
└── README_ORCHESTRATOR.md          # 🆕 Cette documentation
```

---

## 🚀 Installation

### Étape 1 : Ajoutez les nouveaux fichiers

1. Créez `.github/workflows/orchestrator.yml`
2. Créez `merge_results.py` à la racine
3. Créez `search_urls.txt` à la racine

### Étape 2 : Mettez à jour `requirements.txt`

Ajoutez cette ligne si elle n'existe pas :
```
pandas>=2.0.0
```

### Étape 3 : Committez et pushez

```bash
git add .
git commit -m "Ajout orchestrateur automatique"
git push
```

---

## 📝 Utilisation

### 1️⃣ Préparez vos URLs

Éditez le fichier `search_urls.txt` et ajoutez vos URLs de pages de recherche :

```
https://www.airbnb.com/s/Dubai/homes
https://www.airbnb.com/s/Dubai/homes?items_offset=18
https://www.airbnb.com/s/Dubai/homes?items_offset=36
...
```

**💡 Astuce** : Pour obtenir les URLs des pages 2, 3, 4... :
- Allez sur Airbnb
- Faites votre recherche
- Cliquez sur "Page 2", copiez l'URL
- Répétez pour les pages suivantes

### 2️⃣ Lancez l'orchestrateur

1. Allez sur GitHub → Votre repo
2. Cliquez sur **Actions**
3. Sélectionnez **"Orchestrateur Airbnb Complet"**
4. Cliquez sur **"Run workflow"**
5. Cliquez sur **"Run workflow"** (confirmation)

### 3️⃣ Partez dormir 💤

Le workflow va :
- Traiter chaque page l'une après l'autre
- Scraper les annonces (Phase 1)
- Scraper les profils hôtes (Phase 2)
- Fusionner automatiquement les résultats

**Durée estimée** : ~30-45 minutes par page  
**Durée totale (8 pages)** : ~4-6 heures

### 4️⃣ Téléchargez les résultats

Une fois terminé :
1. Allez dans l'onglet **Actions**
2. Cliquez sur votre run terminé
3. Scrollez en bas vers **"Artifacts"**
4. Téléchargez **"final-complete-results"** 🎉

---

## 📊 Format du CSV final

Le fichier `final_complete_results.csv` contient :

| Colonne | Description | Source |
|---------|-------------|--------|
| `url_annonce` | URL de l'annonce | Phase 1 |
| `titre` | Titre de l'annonce | Phase 1 |
| `licence` | Code de licence | Phase 1 |
| `host_url` | URL du profil hôte | Phase 1 |
| `host_name_from_listing` | Nom hôte (depuis annonce) | Phase 1 |
| `host_name_detailed` | Nom hôte (depuis profil) | Phase 2 |
| `host_rating_from_listing` | Rating (depuis annonce) | Phase 1 |
| `host_rating_detailed` | Rating (depuis profil) | Phase 2 |
| `host_joined_from_listing` | Année inscription (annonce) | Phase 1 |
| `host_joined_year` | Année inscription (profil) | Phase 2 |
| `host_years_active` | Années d'activité | Phase 2 |
| `host_listing_count` | Nombre d'annonces | Phase 2 |
| `host_scrape_notes` | Notes/erreurs | Phase 2 |
| `scraped_at` | Date du scraping | Phase 1 |

**💡 Pourquoi des colonnes en double ?**  
Parce que Phase 1 et Phase 2 utilisent des méthodes différentes. Vous avez ainsi les deux versions pour vérifier la cohérence !

---

## 🔍 Gestion des doublons

Le système est **intelligent** :
- Si un hôte apparaît sur plusieurs pages, il est scrapé **une seule fois**
- Économise du temps et évite les blocages Airbnb

---

## ⚠️ Gestion des erreurs

### Si une page échoue :
✅ Le workflow **continue** avec les pages suivantes  
✅ Vous obtenez les résultats des pages qui ont réussi  
✅ Les erreurs sont loggées dans les artifacts "debug-info"

### Si Phase 1 échoue pour une page :
- Phase 2 est **sautée** pour cette page
- Le workflow continue avec la page suivante

### Si Phase 2 échoue pour une page :
- Les données Phase 1 sont **conservées**
- Le CSV final contiendra ces annonces (sans détails hôtes)
- Le workflow continue avec la page suivante

---

## 🐛 Debugging

Si vous avez des problèmes :

1. **Téléchargez les artifacts de debug**
   - `phase1-listings` : Résultats Phase 1 par page
   - `phase2-hosts` : Résultats Phase 2 par page
   - `debug-info` : Logs et informations détaillées

2. **Vérifiez les logs du workflow**
   - Allez dans Actions → Votre run
   - Cliquez sur "orchestrate"
   - Regardez les logs détaillés

3. **Testez individuellement**
   - Testez d'abord "Airbnb Scrape" (Phase 1)
   - Puis "Scrape Airbnb Hosts" (Phase 2)
   - Si les deux fonctionnent, l'orchestrateur fonctionnera !

---

## 🔧 Personnalisation

### Modifier le nombre max d'annonces par page

Dans `orchestrator.yml`, ligne ~60 :
```yaml
export MAX_LISTINGS="20"  # Changez cette valeur
```

### Modifier la durée max par page

Dans `orchestrator.yml`, ligne ~61 :
```yaml
export MAX_MINUTES="15"  # Changez cette valeur (en minutes)
```

### Ajouter un délai entre les pages

Dans `orchestrator.yml`, ligne ~184 :
```bash
sleep 10  # Changez cette valeur (en secondes)
```

---

## 📈 Statistiques

À la fin de l'exécution, vous verrez :
```
📊 RÉSUMÉ DES RÉSULTATS
======================================
Phase 1 (annonces): 8 fichiers
Phase 2 (hôtes): 8 fichiers
Résultat final: 144 lignes de données
✅ Fichier: output_final/final_complete_results.csv
```

---

## ❓ FAQ

### Q : Puis-je scraper plus de 8 pages ?
**R :** Oui ! Ajoutez simplement plus d'URLs dans `search_urls.txt`. Attention au timeout de 7h max.

### Q : Puis-je scraper plusieurs villes en même temps ?
**R :** Oui ! Mettez toutes les URLs (toutes villes) dans `search_urls.txt`.

### Q : Le workflow est trop long, que faire ?
**R :** Réduisez le nombre de pages, ou lancez plusieurs runs séparés avec différents `search_urls.txt`.

### Q : Je veux garder mes anciens workflows, c'est possible ?
**R :** Oui ! L'orchestrateur utilise vos workflows existants. Vous pouvez toujours les lancer manuellement.

### Q : Les données sont-elles dedupliquées ?
**R :** Les **hôtes** sont dedupliqués (scrapés une seule fois). Les **annonces** ne sont pas dedupliquées (normal, chaque page peut avoir des annonces différentes).

---

## 🎉 C'est tout !

Vous avez maintenant un système **100% automatique** pour scraper Airbnb !

**Workflow :**
1. Créez `search_urls.txt`
2. Lancez l'orchestrateur
3. Partez dormir
4. Téléchargez le CSV final

**Profitez ! 🚀**

---

## 📞 Support

Si vous avez des questions ou des problèmes, vérifiez :
1. Les logs du workflow dans GitHub Actions
2. Les artifacts de debug
3. Que vos URLs dans `search_urls.txt` sont valides

---

**Fait avec ❤️ pour automatiser votre scraping Airbnb**
