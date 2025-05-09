from django.db import connection

def query(query="", params=[]):
    with connection.cursor() as cursor:
        cursor.execute(query, params)

        # Jika query adalah SELECT, ambil hasilnya
        if query.strip().lower().startswith("select"):
            return dictfetchall(cursor)
        else:
            return None  # Untuk DELETE/INSERT/UPDATE, kembalikan None

def dictfetchall(cursor):
    """
    Return all rows from a cursor as a dict.
    Assume the column names are unique.
    """
    columns = [col[0] for col in cursor.description]

    return [dict(zip(columns, row)) for row in cursor.fetchall()]