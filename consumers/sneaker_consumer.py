import pika
import psycopg2
import json

# Fonction pour insérer des données dans la table sneaker
def insert_sneaker(data):
    try:
        # Établir une connexion avec la base de données
        conn = psycopg2.connect(
            dbname='sneakersinventory',
            user='root',
            password='root',
            host='db'
        )
        cursor = conn.cursor()

        # Insérer des données dans la table sneaker
        cursor.execute("INSERT INTO sneaker (name, brand, size, color, price) VALUES (%s, %s, %s, %s, %s)",
                       (data['name'], data['brand'], data['size'], data['color'], data['price']))

        # Valider la transaction
        conn.commit()

        print("Data inserted successfully into sneaker table")

    except psycopg2.Error as e:
        print("Error inserting data into sneaker table:", e)

    finally:
        # Fermer la connexion à la base de données
        if conn:
            conn.close()

# Fonction pour insérer des données dans la table location
def insert_location(data):
    try:
        # Établir une connexion avec la base de données
        conn = psycopg2.connect(
            dbname='sneakersinventory',
            user='root',
            password='root',
            host='db'
        )
        cursor = conn.cursor()

        # Insérer des données dans la table location
        cursor.execute("INSERT INTO location (name, address, city, state, zip, temperature) VALUES (%s, %s, %s, %s, %s, %s)",
                       (data['name'], data['address'], data['city'], data['state'], data['zip'], data['temperature']))

        # Valider la transaction
        conn.commit()

        print("Data inserted successfully into location table")

    except psycopg2.Error as e:
        print("Error inserting data into location table:", e)

    finally:
        # Fermer la connexion à la base de données
        if conn:
            conn.close()

# Fonction pour insérer des données dans la table sneaker_location
def insert_sneaker_location(quantity):
    try:
        # Établir une connexion avec la base de données
        conn = psycopg2.connect(
            dbname='sneakersinventory',
            user='root',
            password='root',
            host='db'
        )
        cursor = conn.cursor()

        # Récupérer l'ID de la sneaker insérée
        cursor.execute("SELECT id FROM sneaker ORDER BY id DESC LIMIT 1")
        sneaker_id = cursor.fetchone()[0]

        # Récupérer l'ID de la location insérée
        cursor.execute("SELECT id FROM location ORDER BY id DESC LIMIT 1")
        location_id = cursor.fetchone()[0]

        # Insérer des données dans la table sneaker_location
        cursor.execute("INSERT INTO sneaker_location (sneaker_id, location_id, quantity) VALUES (%s, %s, %s)",
                       (sneaker_id, location_id, quantity))

        # Valider la transaction
        conn.commit()

        print("Data inserted successfully into sneaker_location table")

    except psycopg2.Error as e:
        print("Error inserting data into sneaker_location table:", e)

    finally:
        # Fermer la connexion à la base de données
        if conn:
            conn.close()




# Fonction de rappel pour traiter les messages reçus
def callback(ch, method, properties, body):
    message = json.loads(body.decode('utf-8'))
    print(f" [x] Received {message}")

    # Insérer les données dans la base de données
    insert_sneaker(message['sneaker'])
    insert_location(message['location'])
    insert_sneaker_location(message['quantity'])

# Fonction principale pour démarrer le consommateur
def run():
    connection = pika.BlockingConnection(pika.ConnectionParameters('broker'))
    channel = connection.channel()

    channel.queue_declare(queue='sneakers_queue')

    channel.basic_consume(queue='sneakers_queue',
                          on_message_callback=callback,
                          auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

    connection.close()

if __name__ == '__main__':
    run()
