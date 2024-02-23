import pika
import psycopg2

def get_all_sneakers():
    conn = None
    try:
        # Établir une connexion avec la base de données
        conn = psycopg2.connect(
            dbname='sneakersinventory',
            user='root',
            password='root',
            host='db'
        )
        cursor = conn.cursor()

        # Récupérer toutes les données de la table sneaker
        cursor.execute("SELECT * FROM sneaker")
        sneakers = cursor.fetchall()

        return sneakers

    except psycopg2.Error as e:
        print("Error getting data from sneaker table:", e)

    finally:
        # Fermer la connexion à la base de données
        if conn:
            conn.close()
