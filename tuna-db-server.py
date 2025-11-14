from flask import Flask, jsonify, request
import pyodbc
import logging
from datetime import datetime

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# SQL Config
SQL_SERVER = '10.4.4.178'
SQL_DATABASE = 'TUNAAKS'
SQL_USER = 'aconnect'
SQL_PASSWORD = 'ene60yr1L2Vmns'

# Connection string
connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SQL_SERVER};DATABASE={SQL_DATABASE};UID={SQL_USER};PWD={SQL_PASSWORD}'


# ==================== ARACLAR ====================
@app.route('/hello', methods=['GET'])
def get_araclar_hello():
    try:
        logger.info("Fetching Araclar...")

        return jsonify({
            'success': True,
            'hello': 'hello aconnect',
        })

    except Exception as err:
        logger.error(f"Error: {err}")
        return jsonify({'error': str(err)}), 500

# ==================== ARACLAR ====================
@app.route('/araclar', methods=['GET'])
def get_araclar():
    try:
        logger.info("Fetching Araclar...")

        conn = pyodbc.connect(connection_string, timeout=10)
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM Araclar')

        columns = [desc[0] for desc in cursor.description]
        rows = [dict(zip(columns, row)) for row in cursor.fetchall()]

        cursor.close()
        conn.close()

        logger.info(f"Araclar fetched: {len(rows)} records")

        return jsonify({
            'success': True,
            'totalRecords': len(rows),
            'data': rows
        })

    except Exception as err:
        logger.error(f"Error: {err}")
        return jsonify({'error': str(err)}), 500


@app.route('/araclar', methods=['POST'])
def create_araclar():
    try:
        data = request.get_json()

        conn = pyodbc.connect(connection_string, timeout=10)
        cursor = conn.cursor()

        cursor.execute("SELECT TOP 0 * FROM Araclar")
        columns = [desc[0] for desc in cursor.description]

        insert_columns = [col for col in columns if col in data]
        placeholders = ','.join(['?' for _ in insert_columns])
        column_names = ','.join(insert_columns)
        values = [data[col] for col in insert_columns]

        query = f"INSERT INTO Araclar ({column_names}) VALUES ({placeholders})"
        cursor.execute(query, values)
        conn.commit()

        cursor.close()
        conn.close()

        logger.info("Record inserted to Araclar")
        return jsonify({'success': True, 'message': 'Record created successfully'}), 201

    except Exception as err:
        logger.error(f"Error: {err}")
        return jsonify({'error': str(err)}), 500


# ==================== SOFORLER ====================
@app.route('/soforler', methods=['GET'])
def get_soforler():
    try:
        logger.info("Fetching Soforler...")

        conn = pyodbc.connect(connection_string, timeout=10)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Soforler')

        columns = [desc[0] for desc in cursor.description]
        rows = [dict(zip(columns, row)) for row in cursor.fetchall()]

        cursor.close()
        conn.close()

        logger.info(f"Soforler fetched: {len(rows)} records")
        return jsonify({'success': True, 'totalRecords': len(rows), 'data': rows})

    except Exception as err:
        logger.error(f"Error: {err}")
        return jsonify({'error': str(err)}), 500


@app.route('/soforler', methods=['POST'])
def create_soforler():
    try:
        data = request.get_json()

        conn = pyodbc.connect(connection_string, timeout=10)
        cursor = conn.cursor()

        cursor.execute("SELECT TOP 0 * FROM Soforler")
        columns = [desc[0] for desc in cursor.description]

        insert_columns = [col for col in columns if col in data]
        placeholders = ','.join(['?' for _ in insert_columns])
        column_names = ','.join(insert_columns)
        values = [data[col] for col in insert_columns]

        query = f"INSERT INTO Soforler ({column_names}) VALUES ({placeholders})"
        cursor.execute(query, values)
        conn.commit()

        cursor.close()
        conn.close()

        logger.info("Record inserted to Soforler")
        return jsonify({'success': True, 'message': 'Record created successfully'}), 201

    except Exception as err:
        logger.error(f"Error: {err}")
        return jsonify({'error': str(err)}), 500


# ==================== TEMPDATA ====================
@app.route('/tempdata', methods=['GET'])
def get_tempdata():
    try:
        logger.info("Fetching Tempdata...")

        conn = pyodbc.connect(connection_string, timeout=10)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Tempdata')

        columns = [desc[0] for desc in cursor.description]
        rows = [dict(zip(columns, row)) for row in cursor.fetchall()]

        cursor.close()
        conn.close()

        logger.info(f"Tempdata fetched: {len(rows)} records")
        return jsonify({'success': True, 'totalRecords': len(rows), 'data': rows})

    except Exception as err:
        logger.error(f"Error: {err}")
        return jsonify({'error': str(err)}), 500


@app.route('/tempdata', methods=['POST'])
def create_tempdata():
    try:
        data = request.get_json()

        conn = pyodbc.connect(connection_string, timeout=10)
        cursor = conn.cursor()

        cursor.execute("SELECT TOP 0 * FROM Tempdata")
        columns = [desc[0] for desc in cursor.description]

        insert_columns = [col for col in columns if col in data]
        placeholders = ','.join(['?' for _ in insert_columns])
        column_names = ','.join(insert_columns)
        values = [data[col] for col in insert_columns]

        query = f"INSERT INTO Tempdata ({column_names}) VALUES ({placeholders})"
        cursor.execute(query, values)
        conn.commit()

        cursor.close()
        conn.close()

        logger.info("Record inserted to Tempdata")
        return jsonify({'success': True, 'message': 'Record created successfully'}), 201

    except Exception as err:
        logger.error(f"Error: {err}")
        return jsonify({'error': str(err)}), 500


# ==================== URETIM ====================
@app.route('/uretim', methods=['GET'])
def get_uretim():
    try:
        logger.info("Fetching Uretim...")

        conn = pyodbc.connect(connection_string, timeout=10)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Uretim')

        columns = [desc[0] for desc in cursor.description]
        rows = [dict(zip(columns, row)) for row in cursor.fetchall()]

        cursor.close()
        conn.close()

        logger.info(f"Uretim fetched: {len(rows)} records")
        return jsonify({'success': True, 'totalRecords': len(rows), 'data': rows})

    except Exception as err:
        logger.error(f"Error: {err}")
        return jsonify({'error': str(err)}), 500


@app.route('/uretim', methods=['POST'])
def create_uretim():
    try:
        data = request.get_json()

        conn = pyodbc.connect(connection_string, timeout=10)
        cursor = conn.cursor()

        cursor.execute("SELECT TOP 0 * FROM Uretim")
        columns = [desc[0] for desc in cursor.description]

        insert_columns = [col for col in columns if col in data]
        placeholders = ','.join(['?' for _ in insert_columns])
        column_names = ','.join(insert_columns)
        values = [data[col] for col in insert_columns]

        query = f"INSERT INTO Uretim ({column_names}) VALUES ({placeholders})"
        cursor.execute(query, values)
        conn.commit()

        cursor.close()
        conn.close()

        logger.info("Record inserted to Uretim")
        return jsonify({'success': True, 'message': 'Record created successfully'}), 201

    except Exception as err:
        logger.error(f"Error: {err}")
        return jsonify({'error': str(err)}), 500


# ==================== AYARLAR ====================
@app.route('/ayarlar', methods=['GET'])
def get_ayarlar():
    try:
        logger.info("Fetching Ayarlar...")

        conn = pyodbc.connect(connection_string, timeout=10)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Ayarlar')

        columns = [desc[0] for desc in cursor.description]
        rows = [dict(zip(columns, row)) for row in cursor.fetchall()]

        cursor.close()
        conn.close()

        logger.info(f"Ayarlar fetched: {len(rows)} records")
        return jsonify({'success': True, 'totalRecords': len(rows), 'data': rows})

    except Exception as err:
        logger.error(f"Error: {err}")
        return jsonify({'error': str(err)}), 500


@app.route('/ayarlar', methods=['POST'])
def create_ayarlar():
    try:
        data = request.get_json()

        conn = pyodbc.connect(connection_string, timeout=10)
        cursor = conn.cursor()

        cursor.execute("SELECT TOP 0 * FROM Ayarlar")
        columns = [desc[0] for desc in cursor.description]

        insert_columns = [col for col in columns if col in data]
        placeholders = ','.join(['?' for _ in insert_columns])
        column_names = ','.join(insert_columns)
        values = [data[col] for col in insert_columns]

        query = f"INSERT INTO Ayarlar ({column_names}) VALUES ({placeholders})"
        cursor.execute(query, values)
        conn.commit()

        cursor.close()
        conn.close()

        logger.info("Record inserted to Ayarlar")
        return jsonify({'success': True, 'message': 'Record created successfully'}), 201

    except Exception as err:
        logger.error(f"Error: {err}")
        return jsonify({'error': str(err)}), 500


@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    logger.info("✓ DB Server running on port 3000")
    app.run(host='0.0.0.0', port=3000, debug=False)
