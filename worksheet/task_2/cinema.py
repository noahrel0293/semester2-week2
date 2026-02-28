"""
This is where you should write your code and this is what you need to upload to Gradescope for autograding.

You must NOT change the function definitions (names, arguments).

You can run the functions you define in this file by using test.py (python test.py)
Please do not add any additional code underneath these functions.
"""

import sqlite3


def customer_tickets(conn, customer_id):
    """
    Return a list of tuples:
    (film_title, screen, price)

    Include only tickets purchased by the given customer_id.
    Order results by film title alphabetically.
    """
    customer_tickets_query = "SELECT films.title, screenings.screen, tickets.price FROM (tickets INNER JOIN screenings ON tickets.screening_id = screenings.screening_id) INNER JOIN films ON screenings.film_id = films.film_id WHERE customer_id = ?;"
    customer_tickets_cursor = conn.execute(customer_tickets_query, (customer_id,))
    customer_tickets_list = []
    for row in customer_tickets_cursor:
        customer_tickets_list.append(row)
    customer_tickets_list.sort(key=lambda customer_tickets_list:customer_tickets_list[0])
    return customer_tickets_list
    pass


def screening_sales(conn):
    """
    Return a list of tuples:
    (screening_id, film_title, tickets_sold)

    Include all screenings, even if tickets_sold is 0.
    Order results by tickets_sold descending.
    """
    screening_sales_query = "SELECT screenings.screening_id, films.title, COUNT(tickets.ticket_id) FROM (screenings LEFT JOIN tickets ON screenings.screening_id = tickets.screening_id) INNER JOIN films ON screenings.film_id = films.film_id GROUP BY screenings.screening_id;"
    screening_sales_cursor = conn.execute(screening_sales_query)
    screening_sales_list = []
    for row in screening_sales_cursor:
        screening_sales_list.append(row)
    screening_sales_list.sort(key=lambda screening_sales_list:screening_sales_list[2], reverse=True)
    return screening_sales_list
    pass


def top_customers_by_spend(conn, limit):
    """
    Return a list of tuples:
    (customer_name, total_spent)

    total_spent is the sum of ticket prices per customer.
    Only include customers who have bought at least one ticket.
    Order by total_spent descending.
    Limit the number of rows returned to `limit`.
    """
    top_customers_by_spend_query = "SELECT customers.customer_name, SUM(tickets.price) FROM tickets INNER JOIN customers ON tickets.customer_id = customers.customer_id GROUP BY tickets.customer_id ORDER BY SUM(tickets.price) DESC, customers.customer_name ASC LIMIT ?;"
    top_customers_by_spend_cursor = conn.execute(top_customers_by_spend_query, (limit,))
    top_customers_by_spend_list = []
    for row in top_customers_by_spend_cursor:
        top_customers_by_spend_list.append(row)
    return top_customers_by_spend_list
    pass