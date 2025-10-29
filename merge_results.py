#!/usr/bin/env python3
"""
Script de fusion des résultats Airbnb
Fusionne les données des annonces (Phase 1) avec les données des hôtes (Phase 2)
"""

import os
import csv
import glob
from pathlib import Path

def read_csv_safe(filepath):
    """Lit un CSV en gérant différents encodages"""
    encodings = ['utf-8-sig', 'utf-8', 'latin-1', 'cp1252']
    
    for encoding in encodings:
        try:
            with open(filepath, 'r', encoding=encoding, newline='') as f:
                reader = csv.DictReader(f)
                return list(reader)
        except (UnicodeDecodeError, Exception):
            continue
    
    print(f"⚠️ Impossible de lire {filepath}")
    return []

def merge_results():
    """Fusionne tous les résultats Phase 1 et Phase 2"""
    
    print("🔗 FUSION DES RÉSULTATS")
    print("=" * 60)
    
    # Créer le dossier de sortie
    output_dir = Path("output_final")
    output_dir.mkdir(exist_ok=True)
    
    # Lire tous les fichiers Phase 1 (annonces)
    phase1_files = sorted(glob.glob("output_phase1/page_*_listings.csv"))
    print(f"\n📄 Phase 1 : {len(phase1_files)} fichier(s) trouvé(s)")
    
    all_listings = []
    for f in phase1_files:
        data = read_csv_safe(f)
        print(f"  - {os.path.basename(f)}: {len(data)} annonce(s)")
        all_listings.extend(data)
    
    print(f"📊 Total annonces: {len(all_listings)}")
    
    # Lire tous les fichiers Phase 2 (hôtes)
    phase2_files = sorted(glob.glob("output_phase2/page_*_hosts.csv"))
    print(f"\n👥 Phase 2 : {len(phase2_files)} fichier(s) trouvé(s)")
    
    all_hosts = []
    for f in phase2_files:
        data = read_csv_safe(f)
        print(f"  - {os.path.basename(f)}: {len(data)} hôte(s)")
        all_hosts.extend(data)
    
    print(f"📊 Total hôtes: {len(all_hosts)}")
    
    # Créer un dictionnaire des hôtes indexé par URL
    hosts_dict = {}
    for host in all_hosts:
        url = host.get('url', '').strip()
        if url:
            hosts_dict[url] = host
    
    print(f"\n🔑 Index des hôtes créé: {len(hosts_dict)} entrée(s) unique(s)")
    
    # Fusionner les données
    print("\n🔗 Fusion en cours...")
    merged_data = []
    matched_count = 0
    
    for listing in all_listings:
        # Données de base de l'annonce
        merged_row = {
            'url_annonce': listing.get('url', ''),
            'titre': listing.get('title', ''),
            'licence': listing.get('license_code', ''),
            'host_url': listing.get('host_profile_url', ''),
            'host_name_from_listing': listing.get('host_name', ''),
            'host_rating_from_listing': listing.get('host_overall_rating', ''),
            'host_joined_from_listing': listing.get('host_joined', ''),
            'scraped_at': listing.get('scraped_at', ''),
        }
        
        # Chercher les infos détaillées de l'hôte
        host_url = listing.get('host_profile_url', '').strip()
        if host_url and host_url in hosts_dict:
            host_data = hosts_dict[host_url]
            merged_row.update({
                'host_name_detailed': host_data.get('name', ''),
                'host_rating_detailed': host_data.get('rating', ''),
                'host_joined_year': host_data.get('joined_year', ''),
                'host_years_active': host_data.get('years_active', ''),
                'host_listing_count': host_data.get('listing_count', ''),
                'host_scrape_notes': host_data.get('notes', ''),
            })
            matched_count += 1
        else:
            # Hôte non trouvé dans Phase 2
            merged_row.update({
                'host_name_detailed': '',
                'host_rating_detailed': '',
                'host_joined_year': '',
                'host_years_active': '',
                'host_listing_count': '',
                'host_scrape_notes': 'Hôte non scrapé en Phase 2',
            })
        
        merged_data.append(merged_row)
    
    print(f"✅ Fusion terminée: {matched_count}/{len(all_listings)} annonces avec données hôte complètes")
    
    # Écrire le fichier final
    output_file = output_dir / "final_complete_results.csv"
    
    if merged_data:
        fieldnames = [
            'url_annonce',
            'titre',
            'licence',
            'host_url',
            'host_name_from_listing',
            'host_name_detailed',
            'host_rating_from_listing',
            'host_rating_detailed',
            'host_joined_from_listing',
            'host_joined_year',
            'host_years_active',
            'host_listing_count',
            'host_scrape_notes',
            'scraped_at',
        ]
        
        with open(output_file, 'w', encoding='utf-8-sig', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(merged_data)
        
        print(f"\n✅ Fichier final créé: {output_file}")
        print(f"📊 Nombre total de lignes: {len(merged_data)}")
        
        # Statistiques
        complete_data = sum(1 for row in merged_data if row['host_name_detailed'])
        incomplete_data = len(merged_data) - complete_data
        
        print(f"\n📈 STATISTIQUES:")
        print(f"  - Données complètes (Phase 1 + Phase 2): {complete_data}")
        print(f"  - Données partielles (Phase 1 uniquement): {incomplete_data}")
        
        if incomplete_data > 0:
            print(f"\n⚠️ {incomplete_data} annonce(s) n'ont pas de données hôte détaillées")
            print("   (Hôtes possiblement déjà scrapés dans une page précédente ou erreurs)")
    else:
        print("❌ Aucune donnée à fusionner!")
    
    print("\n" + "=" * 60)
    print("✅ FUSION TERMINÉE")

if __name__ == "__main__":
    merge_results()
