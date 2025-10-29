# 🚀 GUIDE D'INSTALLATION RAPIDE - Orchestrateur Airbnb

## ✅ Fichiers créés pour vous

J'ai créé 4 fichiers essentiels :

1. **`.github_workflows_orchestrator.yml`** → À renommer et placer dans `.github/workflows/`
2. **`merge_results.py`** → À placer à la racine de votre repo
3. **`search_urls.txt`** → À placer à la racine de votre repo (et à personnaliser)
4. **`README_ORCHESTRATOR.md`** → Documentation complète

---

## 📥 INSTALLATION EN 5 ÉTAPES

### Étape 1 : Téléchargez les fichiers
Téléchargez tous les fichiers que je viens de créer.

### Étape 2 : Placez les fichiers dans votre repo GitHub

```
votre-repo/
├── .github/
│   └── workflows/
│       ├── scrape.yml                    ← (existant)
│       ├── scrape-airbnb.yml             ← (existant)
│       └── orchestrator.yml              ← 🆕 RENOMMEZ et placez ici
├── scrape_airbnb.py                      ← (existant)
├── scraper.js                            ← (existant)
├── merge_results.py                      ← 🆕 Placez à la racine
├── search_urls.txt                       ← 🆕 Placez à la racine
└── README_ORCHESTRATOR.md                ← 🆕 Placez à la racine
```

**IMPORTANT** : Renommez `.github_workflows_orchestrator.yml` en `orchestrator.yml`

### Étape 3 : Mettez à jour requirements.txt

Ouvrez votre fichier `requirements.txt` et ajoutez cette ligne (si elle n'existe pas) :
```
pandas>=2.0.0
```

### Étape 4 : Personnalisez search_urls.txt

Éditez `search_urls.txt` et remplacez les URLs d'exemple par VOS URLs de recherche Airbnb.

**Exemple :**
```
https://www.airbnb.com/s/Paris/homes
https://www.airbnb.com/s/Paris/homes?items_offset=18
https://www.airbnb.com/s/Paris/homes?items_offset=36
...
```

💡 **Comment obtenir les URLs des pages 2, 3, 4... ?**
1. Allez sur Airbnb
2. Faites votre recherche
3. Cliquez sur "Page suivante"
4. Copiez l'URL de la barre d'adresse
5. Répétez pour chaque page

### Étape 5 : Committez et pushez

```bash
git add .
git commit -m "Ajout orchestrateur automatique"
git push
```

---

## 🎯 UTILISATION

### 1. Lancez le workflow

1. Allez sur **GitHub** → Votre repo → **Actions**
2. Cliquez sur **"Orchestrateur Airbnb Complet"**
3. Cliquez sur **"Run workflow"** (bouton vert)
4. Confirmez en cliquant à nouveau sur **"Run workflow"**

### 2. Attendez (4-6 heures pour 8 pages)

Le système va automatiquement :
- ✅ Scraper chaque page d'annonces (Phase 1)
- ✅ Extraire les URLs des hôtes
- ✅ Scraper les profils des hôtes (Phase 2)
- ✅ Fusionner toutes les données
- ✅ Créer le CSV final

### 3. Téléchargez les résultats

Une fois terminé :
1. Allez dans **Actions** → Cliquez sur votre run terminé
2. Scrollez en bas vers **"Artifacts"**
3. Téléchargez **"final-complete-results"** 🎉

Le fichier `final_complete_results.csv` contient TOUTES vos données fusionnées !

---

## 📊 CE QUE VOUS OBTENEZ

Un fichier CSV avec :
- URLs et titres des annonces
- Codes de licence
- Informations complètes sur chaque hôte :
  - Nom
  - Rating
  - Année d'inscription
  - Années d'activité
  - Nombre d'annonces
  - Et plus !

**Tout est fusionné intelligemment pour vous ! 🎉**

---

## 🔍 AVANTAGES DU SYSTÈME

✅ **100% automatique** - Lancez et oubliez  
✅ **Résilient** - Continue même si une page échoue  
✅ **Intelligent** - Évite les doublons d'hôtes  
✅ **Sécurisé** - Pas de timeout GitHub (page par page)  
✅ **Complet** - Fusionne automatiquement Phase 1 + Phase 2  
✅ **Non-invasif** - Vos scrapers existants restent intacts  

---

## ⚠️ POINTS IMPORTANTS

1. **Vos scrapers existants ne sont PAS modifiés**
   - `scrape.yml` reste identique
   - `scrape-airbnb.yml` reste identique
   - L'orchestrateur les utilise tels quels

2. **Gestion intelligente des doublons**
   - Si un hôte apparaît sur plusieurs pages, il est scrapé UNE SEULE FOIS
   - Économise du temps et évite les blocages

3. **Gestion des erreurs**
   - Si une page échoue, le système continue avec les suivantes
   - Vous obtenez toujours un résultat final avec les pages qui ont réussi

4. **Durée d'exécution**
   - ~30-45 minutes par page
   - ~4-6 heures pour 8 pages
   - Bien en dessous de la limite GitHub de 7h

---

## 🆘 BESOIN D'AIDE ?

Consultez le fichier `README_ORCHESTRATOR.md` pour :
- Documentation complète
- FAQ
- Guide de debugging
- Personnalisation avancée

---

## 🎉 C'EST TOUT !

Vous avez maintenant un système d'orchestration automatique qui :
1. Prend vos URLs de pages
2. Scrappe tout automatiquement (Phase 1 + Phase 2)
3. Fusionne les résultats
4. Vous livre un CSV complet

**Plus besoin de copier-coller manuellement ! 🚀**

---

**Bon scraping ! 💪**
