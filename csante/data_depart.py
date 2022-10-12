#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import json
import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as go
import population as popu
pio.renderers.default = "browser"

def data():
    df = pd.read_excel("./Data/equip-serv-sante-com-2020.xlsx", skiprows=[0, 1, 2, 3, 5])
    vardp = df.groupby('Département').sum()
    vardp = vardp.drop(['Région'], axis=1)
    vardp['id'] = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '2A', '2B', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49',
                '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '971', '972', '973', '974', '976']
    d={'01': 'Ain - Bourg-en-bresse','02': ' Aisne - Laon','03': ' Allier - Moulins','04': ' Alpes-de-Haute-Provence - Digne-les-bains','05': ' Hautes-alpes - Gap','06': ' Alpes-maritimes - Nice', '07': ' Ardèche - Privas','08': ' Ardennes - Charleville-mézières','09': ' Ariège - Foix','10': ' Aube - Troyes','11': ' Aude - Carcassonne','12': ' Aveyron - Rodez','13': ' Bouches-du-Rhône - Marseille','14': ' Calvados - Caen','15': ' Cantal - Aurillac','16': ' Charente - Angoulême','17': ' Charente-maritime - La rochelle','18': ' Cher - Bourges','19': ' Corrèze - Tulle','2A': ' Corse-du-sud - Ajaccio','2B': ' Haute-Corse - Bastia','21': "Côte-d'Or - Dijon",'22': "Côtes-d'Armor - Saint-brieuc",'23': ' Creuse - Guéret','24': ' Dordogne - Périgueux','25': ' Doubs - Besançon','26': ' Drôme - Valence','27': ' Eure - Évreux','28': ' Eure-et-loir - Chartres','29': ' Finistère - Quimper','30': ' Gard - Nîmes','31': ' Haute-garonne - Toulouse','32': ' Gers - Auch','33': ' Gironde - Bordeaux','34': ' Hérault - Montpellier','35': ' Ille-et-vilaine - Rennes','36': ' Indre - Châteauroux','37': ' Indre-et-loire - Tours','38': ' Isère - Grenoble','39': ' Jura - Lons-le-saunier','40': ' Landes - Mont-de-marsan','41': ' Loir-et-cher - Blois','42': ' Loire - Saint-étienne','43': ' Haute-loire - Le puy-en-velay','44': ' Loire-atlantique - Nantes','45': ' Loiret - Orléans','46': ' Lot - Cahors','47': ' Lot-et-garonne - Agen','48': ' Lozère - Mende','49': ' Maine-et-loire - Angers','50': ' Manche - Saint-lô','51': ' Marne - Châlons-en-champagne','52': ' Haute-marne - Chaumont','53': ' Mayenne - Laval','54': ' Meurthe-et-moselle - Nancy','55': ' Meuse - Bar-le-duc','56': ' Morbihan - Vannes','57': ' Moselle - Metz','58': ' Nièvre - Nevers','59': ' Nord - Lille','60': ' Oise - Beauvais','61': ' Orne - Alençon','62': ' Pas-de-calais - Arras','63': ' Puy-de-dôme - Clermont-ferrand','64': ' Pyrénées-atlantiques - Pau','65': ' Hautes-Pyrénées - Tarbes','66': ' Pyrénées-orientales - Perpignan','67': ' Bas-rhin - Strasbourg','68': ' Haut-rhin - Colmar','69': ' Rhône - Lyon','70': ' Haute-saône - Vesoul','71': ' Saône-et-loire - Mâcon','72': ' Sarthe - Le mans','73': ' Savoie - Chambéry','74': ' Haute-savoie - Annecy','75': ' Paris - Paris','76': ' Seine-maritime - Rouen','77': ' Seine-et-marne - Melun','78': ' Yvelines - Versailles','79': ' Deux-sèvres - Niort','80': ' Somme - Amiens','81': ' Tarn - Albi','82': ' Tarn-et-Garonne - Montauban','83': ' Var - Toulon','84': ' Vaucluse - Avignon','85': ' Vendée - La roche-sur-yon','86': ' Vienne - Poitiers','87': ' Haute-vienne - Limoges','88': 'Vosges - Épinal','89': 'Yonne - Auxerre','90': 'Territoire de belfort - Belfort','91': 'Essonne - Évry','92': 'Hauts-de-seine - Nanterre','93': 'Seine-Saint-Denis - Bobigny','94': 'Val-de-marne - Créteil','95': "Val-d'Oise - Cergy Pontoise",'971': 'Guadeloupe - Basse-terre','972': 'Martinique - Fort-de-france','973': 'Guyane - Cayenne','974': 'La réunion - Saint-denis','976': 'Mayotte - Mamoudzou'}
    s=list(d.values())
    vardp['Département_name']=s
    return vardp

print(data())
