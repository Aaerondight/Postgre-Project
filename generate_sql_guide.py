from fpdf import FPDF


class SQLGuidePDF(FPDF):
    def header(self):
        self.set_font("Helvetica", "B", 12)
        self.set_text_color(50, 50, 150)
        self.cell(0, 10, "SQL for Test Automation Engineers", align="C", new_x="LMARGIN", new_y="NEXT")
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(4)

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(128, 128, 128)
        self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="C")

    def section_title(self, title):
        self.set_font("Helvetica", "B", 14)
        self.set_text_color(30, 30, 120)
        self.ln(6)
        self.cell(0, 10, title, new_x="LMARGIN", new_y="NEXT")
        self.ln(2)

    def sub_title(self, title):
        self.set_font("Helvetica", "B", 11)
        self.set_text_color(60, 60, 60)
        self.cell(0, 8, title, new_x="LMARGIN", new_y="NEXT")
        self.ln(1)

    def body_text(self, text):
        self.set_font("Helvetica", "", 10)
        self.set_text_color(0, 0, 0)
        self.multi_cell(0, 6, text)
        self.ln(2)

    def code_block(self, code):
        self.set_font("Courier", "", 9)
        self.set_fill_color(240, 240, 240)
        self.set_text_color(0, 0, 0)
        x = self.get_x()
        self.set_x(x + 5)
        self.multi_cell(180, 5, code, fill=True)
        self.ln(3)

    def result_label(self):
        self.set_font("Helvetica", "B", 9)
        self.set_text_color(0, 120, 0)
        self.cell(0, 6, "Result:", new_x="LMARGIN", new_y="NEXT")
        self.ln(1)

    def result_table(self, headers, rows, col_widths=None):
        """Draw a result table with headers and rows."""
        if col_widths is None:
            total = 180
            col_widths = [total // len(headers)] * len(headers)
            # Adjust last column to fill remaining space
            col_widths[-1] = total - sum(col_widths[:-1])

        x_start = self.get_x() + 5
        self.set_x(x_start)

        # Header row
        self.set_font("Courier", "B", 8)
        self.set_fill_color(30, 30, 120)
        self.set_text_color(255, 255, 255)
        for i, h in enumerate(headers):
            self.cell(col_widths[i], 6, f" {h}", fill=True)
        self.ln()

        # Data rows
        self.set_font("Courier", "", 8)
        self.set_text_color(0, 0, 0)
        for row_idx, row in enumerate(rows):
            self.set_x(x_start)
            if row_idx % 2 == 0:
                self.set_fill_color(235, 245, 235)
            else:
                self.set_fill_color(255, 255, 255)
            for i, val in enumerate(row):
                self.cell(col_widths[i], 6, f" {val}", fill=True)
            self.ln()
        self.ln(4)

    def bullet(self, text):
        self.set_font("Helvetica", "", 10)
        self.set_text_color(0, 0, 0)
        x = self.get_x()
        self.set_x(x + 5)
        self.cell(5, 6, chr(8226))
        self.multi_cell(175, 6, text)
        self.ln(1)


pdf = SQLGuidePDF()
pdf.alias_nb_pages()
pdf.set_auto_page_break(auto=True, margin=20)

# ── Title Page ──
pdf.add_page()
pdf.ln(40)
pdf.set_font("Helvetica", "B", 28)
pdf.set_text_color(30, 30, 120)
pdf.cell(0, 15, "SQL Queries Guide", align="C", new_x="LMARGIN", new_y="NEXT")
pdf.set_font("Helvetica", "", 16)
pdf.set_text_color(80, 80, 80)
pdf.cell(0, 12, "For Test Automation Engineers", align="C", new_x="LMARGIN", new_y="NEXT")
pdf.ln(10)
pdf.set_font("Helvetica", "I", 11)
pdf.cell(0, 10, "From basics to advanced - with real query results", align="C", new_x="LMARGIN", new_y="NEXT")

# Show the sample data tables
pdf.ln(15)
pdf.set_font("Helvetica", "B", 13)
pdf.set_text_color(30, 30, 120)
pdf.cell(0, 10, "Sample Database Used in This Guide", align="C", new_x="LMARGIN", new_y="NEXT")
pdf.ln(5)

pdf.sub_title("users table")
pdf.result_table(
    ["id", "name"],
    [
        ["1", "Jaime"],
        ["2", "Jon Snow"],
        ["3", "Theon Greyjoy"],
    ],
    col_widths=[30, 60],
)

pdf.sub_title("swords table")
pdf.result_table(
    ["id", "name", "attack", "owner_id"],
    [
        ["1", "Oathkeeper", "200", "1"],
        ["2", "Wolf Bane", "214", "2"],
        ["3", "KrakenSlayer", "185", "3"],
    ],
    col_widths=[20, 50, 30, 30],
)

# ══════════════════════════════════════════════════════════
# SECTION 1: MUST-KNOW (Daily Use)
# ══════════════════════════════════════════════════════════
pdf.add_page()
pdf.section_title("1. Must-Know Queries (Daily Use)")

# SELECT
pdf.sub_title("SELECT with WHERE, AND/OR, IN, BETWEEN, LIKE")
pdf.body_text(
    "SELECT is the most fundamental SQL command. It retrieves data from tables. "
    "As a test automation engineer, you will use SELECT constantly to verify that "
    "your application stored or returned the correct data."
)

pdf.code_block("-- Basic SELECT: get all columns from users\nSELECT * FROM users;")
pdf.result_label()
pdf.result_table(
    ["id", "name"],
    [["1", "Jaime"], ["2", "Jon Snow"], ["3", "Theon Greyjoy"]],
    col_widths=[30, 60],
)

pdf.code_block("-- Select specific columns\nSELECT name FROM users;")
pdf.result_label()
pdf.result_table(
    ["name"],
    [["Jaime"], ["Jon Snow"], ["Theon Greyjoy"]],
    col_widths=[60],
)

pdf.code_block("-- WHERE clause filters rows\nSELECT * FROM users WHERE name = 'Jaime';")
pdf.result_label()
pdf.result_table(
    ["id", "name"],
    [["1", "Jaime"]],
    col_widths=[30, 60],
)

pdf.code_block("-- IN checks against a list of values\nSELECT * FROM users WHERE name IN ('Jaime', 'Jon Snow');")
pdf.result_label()
pdf.result_table(
    ["id", "name"],
    [["1", "Jaime"], ["2", "Jon Snow"]],
    col_widths=[30, 60],
)

pdf.code_block("-- LIKE for pattern matching (% = any chars, _ = one char)\nSELECT * FROM users WHERE name LIKE 'J%';")
pdf.result_label()
pdf.result_table(
    ["id", "name"],
    [["1", "Jaime"], ["2", "Jon Snow"]],
    col_widths=[30, 60],
)

pdf.body_text(
    "Other WHERE operators you should know:\n"
    "  AND / OR  - combine conditions: WHERE age > 18 AND status = 'active'\n"
    "  BETWEEN   - range filter: WHERE attack BETWEEN 185 AND 210\n"
    "  != or <>  - not equal: WHERE name != 'Jaime'"
)

pdf.code_block("-- BETWEEN filters a range (inclusive)\nSELECT * FROM swords WHERE attack BETWEEN 185 AND 210;")
pdf.result_label()
pdf.result_table(
    ["id", "name", "attack", "owner_id"],
    [["1", "Oathkeeper", "200", "1"], ["3", "KrakenSlayer", "185", "3"]],
    col_widths=[20, 50, 30, 30],
)

# JOIN
pdf.add_page()
pdf.sub_title("JOIN - INNER, LEFT, RIGHT")
pdf.body_text(
    "JOINs combine rows from two or more tables based on a related column. "
    "Understanding JOINs is critical for verifying relationships between entities."
)

pdf.code_block(
    "-- INNER JOIN: only matching rows from both tables\n"
    "SELECT users.name, swords.name AS sword, swords.attack\n"
    "FROM users\n"
    "INNER JOIN swords ON users.id = swords.owner_id;"
)
pdf.result_label()
pdf.result_table(
    ["name", "sword", "attack"],
    [
        ["Jaime", "Oathkeeper", "200"],
        ["Jon Snow", "Wolf Bane", "214"],
        ["Theon Greyjoy", "KrakenSlayer", "185"],
    ],
    col_widths=[45, 50, 30],
)

pdf.code_block(
    "-- LEFT JOIN: all rows from left table + matches from right\n"
    "-- If a user had no sword, sword columns would show NULL\n"
    "SELECT users.name, swords.name AS sword\n"
    "FROM users\n"
    "LEFT JOIN swords ON users.id = swords.owner_id;"
)
pdf.result_label()
pdf.result_table(
    ["name", "sword"],
    [
        ["Jaime", "Oathkeeper"],
        ["Jon Snow", "Wolf Bane"],
        ["Theon Greyjoy", "KrakenSlayer"],
    ],
    col_widths=[50, 50],
)
pdf.body_text(
    "RIGHT JOIN is the opposite of LEFT JOIN - it keeps all rows from the right table. "
    "In practice, LEFT JOIN is used far more often."
)

# INSERT, UPDATE, DELETE
pdf.sub_title("INSERT, UPDATE, DELETE")
pdf.body_text(
    "These commands modify data. In test automation, you use them for test data "
    "setup (INSERT), modifying state (UPDATE), and cleanup (DELETE)."
)

pdf.code_block(
    "-- INSERT a new row\n"
    "INSERT INTO users (name) VALUES ('Arya Stark');"
)
pdf.result_label()
pdf.body_text("After INSERT, the users table now contains:")
pdf.result_table(
    ["id", "name"],
    [["1", "Jaime"], ["2", "Jon Snow"], ["3", "Theon Greyjoy"], ["4", "Arya Stark"]],
    col_widths=[30, 60],
)

pdf.code_block(
    "-- UPDATE existing rows (always use WHERE!)\n"
    "UPDATE users SET name = 'Jaime Lannister' WHERE id = 1;"
)
pdf.result_label()
pdf.body_text("After UPDATE:")
pdf.result_table(
    ["id", "name"],
    [["1", "Jaime Lannister"], ["2", "Jon Snow"], ["3", "Theon Greyjoy"], ["4", "Arya Stark"]],
    col_widths=[30, 60],
)

pdf.code_block(
    "-- DELETE rows (always use WHERE!)\n"
    "DELETE FROM users WHERE id = 4;"
)
pdf.result_label()
pdf.body_text("After DELETE, Arya is removed. Table is back to original 3 rows.")
pdf.body_text(
    "WARNING: UPDATE and DELETE without WHERE will affect ALL rows in the table. "
    "Always double-check your WHERE clause."
)

# ORDER BY, LIMIT, DISTINCT
pdf.add_page()
pdf.sub_title("ORDER BY, LIMIT, DISTINCT")
pdf.body_text("These clauses help you sort, limit, and deduplicate results.")

pdf.code_block("-- ORDER BY sorts results (ASC = ascending, DESC = descending)\nSELECT * FROM users ORDER BY name ASC;")
pdf.result_label()
pdf.result_table(
    ["id", "name"],
    [["1", "Jaime"], ["2", "Jon Snow"], ["3", "Theon Greyjoy"]],
    col_widths=[30, 60],
)

pdf.code_block("-- ORDER BY descending\nSELECT * FROM swords ORDER BY attack DESC;")
pdf.result_label()
pdf.result_table(
    ["id", "name", "attack", "owner_id"],
    [["2", "Wolf Bane", "214", "2"], ["1", "Oathkeeper", "200", "1"], ["3", "KrakenSlayer", "185", "3"]],
    col_widths=[20, 50, 30, 30],
)

pdf.code_block("-- LIMIT restricts number of rows returned\nSELECT * FROM users LIMIT 2;")
pdf.result_label()
pdf.result_table(
    ["id", "name"],
    [["1", "Jaime"], ["2", "Jon Snow"]],
    col_widths=[30, 60],
)

pdf.code_block("-- DISTINCT removes duplicate values\nSELECT DISTINCT attack FROM swords;")
pdf.result_label()
pdf.result_table(
    ["attack"],
    [["200"], ["214"], ["185"]],
    col_widths=[40],
)

# Aggregate functions
pdf.sub_title("Aggregate Functions: COUNT, SUM, AVG, MIN, MAX")
pdf.body_text(
    "Aggregate functions calculate a single value from multiple rows. Essential "
    "for verifying data counts and totals in your tests."
)

pdf.code_block("-- COUNT: how many rows?\nSELECT COUNT(*) FROM users;")
pdf.result_label()
pdf.result_table(["count"], [["3"]], col_widths=[30])

pdf.code_block("-- SUM: total of a numeric column\nSELECT SUM(attack) FROM swords;")
pdf.result_label()
pdf.result_table(["sum"], [["599"]], col_widths=[30])

pdf.code_block("-- AVG: average value\nSELECT AVG(attack) FROM swords;")
pdf.result_label()
pdf.result_table(["avg"], [["199.67"]], col_widths=[30])

pdf.code_block("-- MIN / MAX: smallest / largest value\nSELECT MIN(attack), MAX(attack) FROM swords;")
pdf.result_label()
pdf.result_table(["min", "max"], [["185", "214"]], col_widths=[30, 30])

# GROUP BY + HAVING
pdf.add_page()
pdf.sub_title("GROUP BY + HAVING")
pdf.body_text(
    "GROUP BY groups rows that share a value, then you can run aggregates on each group. "
    "HAVING filters groups (like WHERE but for aggregated results)."
)

pdf.code_block(
    "-- Count swords per owner\n"
    "SELECT owner_id, COUNT(*) as sword_count\n"
    "FROM swords\n"
    "GROUP BY owner_id;"
)
pdf.result_label()
pdf.result_table(
    ["owner_id", "sword_count"],
    [["1", "1"], ["2", "1"], ["3", "1"]],
    col_widths=[40, 40],
)

pdf.code_block(
    "-- Find owners with attack power > 200\n"
    "SELECT owner_id, SUM(attack) as total_attack\n"
    "FROM swords\n"
    "GROUP BY owner_id\n"
    "HAVING SUM(attack) > 200;"
)
pdf.result_label()
pdf.result_table(
    ["owner_id", "total_attack"],
    [["2", "214"]],
    col_widths=[40, 40],
)

# NULL handling
pdf.sub_title("NULL Handling: IS NULL, IS NOT NULL, COALESCE")
pdf.body_text(
    "NULL means 'no value' - not zero, not empty string. You cannot compare NULL "
    "with = or !=. You must use IS NULL / IS NOT NULL."
)

pdf.code_block(
    "-- Assume we add a user with no sword:\n"
    "-- INSERT INTO users (id, name) VALUES (4, 'Bran');\n"
    "-- (Bran has no matching row in swords)\n\n"
    "SELECT u.name, s.name AS sword\n"
    "FROM users u\n"
    "LEFT JOIN swords s ON u.id = s.owner_id\n"
    "WHERE s.name IS NULL;"
)
pdf.result_label()
pdf.result_table(
    ["name", "sword"],
    [["Bran", "NULL"]],
    col_widths=[50, 50],
)

pdf.code_block(
    "-- COALESCE: return first non-NULL value (great for defaults)\n"
    "SELECT u.name, COALESCE(s.name, 'No sword') AS weapon\n"
    "FROM users u\n"
    "LEFT JOIN swords s ON u.id = s.owner_id;"
)
pdf.result_label()
pdf.result_table(
    ["name", "weapon"],
    [["Jaime", "Oathkeeper"], ["Jon Snow", "Wolf Bane"],
     ["Theon Greyjoy", "KrakenSlayer"], ["Bran", "No sword"]],
    col_widths=[50, 50],
)

# ══════════════════════════════════════════════════════════
# SECTION 2: IMPORTANT (Validation & Debugging)
# ══════════════════════════════════════════════════════════
pdf.add_page()
pdf.section_title("2. Important Queries (Validation & Debugging)")

# Subqueries
pdf.sub_title("Subqueries")
pdf.body_text(
    "A subquery is a query inside another query. Useful when you need to filter "
    "based on the results of another query."
)

pdf.code_block(
    "-- Find users who own a sword\n"
    "SELECT * FROM users\n"
    "WHERE id IN (SELECT owner_id FROM swords);"
)
pdf.result_label()
pdf.result_table(
    ["id", "name"],
    [["1", "Jaime"], ["2", "Jon Snow"], ["3", "Theon Greyjoy"]],
    col_widths=[30, 60],
)

pdf.code_block(
    "-- Find users whose sword has attack > 200\n"
    "SELECT * FROM users\n"
    "WHERE id IN (\n"
    "  SELECT owner_id FROM swords WHERE attack > 200\n"
    ");"
)
pdf.result_label()
pdf.result_table(
    ["id", "name"],
    [["2", "Jon Snow"]],
    col_widths=[30, 60],
)

# EXISTS
pdf.sub_title("EXISTS / NOT EXISTS")
pdf.body_text(
    "EXISTS checks if a subquery returns any rows. Often faster than IN for large datasets."
)

pdf.code_block(
    "-- Find users who own a sword\n"
    "SELECT * FROM users u\n"
    "WHERE EXISTS (\n"
    "  SELECT 1 FROM swords s WHERE s.owner_id = u.id\n"
    ");"
)
pdf.result_label()
pdf.result_table(
    ["id", "name"],
    [["1", "Jaime"], ["2", "Jon Snow"], ["3", "Theon Greyjoy"]],
    col_widths=[30, 60],
)

pdf.code_block(
    "-- Find users who do NOT own a sword\n"
    "-- (If Bran was added with id=4, he'd appear here)\n"
    "SELECT * FROM users u\n"
    "WHERE NOT EXISTS (\n"
    "  SELECT 1 FROM swords s WHERE s.owner_id = u.id\n"
    ");"
)
pdf.result_label()
pdf.body_text("(empty result - all users currently have swords)")

# UNION
pdf.sub_title("UNION / UNION ALL")
pdf.body_text(
    "UNION combines results from two queries. UNION removes duplicates, "
    "UNION ALL keeps them (faster)."
)

pdf.code_block(
    "-- Combine user names and sword names into one list\n"
    "SELECT name FROM users\n"
    "UNION ALL\n"
    "SELECT name FROM swords;"
)
pdf.result_label()
pdf.result_table(
    ["name"],
    [["Jaime"], ["Jon Snow"], ["Theon Greyjoy"],
     ["Oathkeeper"], ["Wolf Bane"], ["KrakenSlayer"]],
    col_widths=[60],
)

# CASE WHEN
pdf.add_page()
pdf.sub_title("CASE WHEN")
pdf.body_text(
    "CASE WHEN adds conditional logic inside a query - like an if/else in SQL."
)

pdf.code_block(
    "SELECT name, attack,\n"
    "  CASE\n"
    "    WHEN attack >= 210 THEN 'Legendary'\n"
    "    WHEN attack >= 195 THEN 'Epic'\n"
    "    ELSE 'Common'\n"
    "  END AS rarity\n"
    "FROM swords;"
)
pdf.result_label()
pdf.result_table(
    ["name", "attack", "rarity"],
    [
        ["Oathkeeper", "200", "Epic"],
        ["Wolf Bane", "214", "Legendary"],
        ["KrakenSlayer", "185", "Common"],
    ],
    col_widths=[50, 30, 40],
)

# Aliases
pdf.sub_title("Aliases (AS)")
pdf.body_text(
    "Aliases give temporary names to columns or tables, making queries more readable."
)

pdf.code_block(
    "-- Column alias\n"
    "SELECT COUNT(*) AS total_users FROM users;"
)
pdf.result_label()
pdf.result_table(["total_users"], [["3"]], col_widths=[40])

pdf.code_block(
    "-- Table alias (essential for JOINs)\n"
    "SELECT u.name, s.name AS sword, s.attack\n"
    "FROM users AS u\n"
    "JOIN swords AS s ON u.id = s.owner_id;"
)
pdf.result_label()
pdf.result_table(
    ["name", "sword", "attack"],
    [
        ["Jaime", "Oathkeeper", "200"],
        ["Jon Snow", "Wolf Bane", "214"],
        ["Theon Greyjoy", "KrakenSlayer", "185"],
    ],
    col_widths=[45, 50, 30],
)

# Transactions
pdf.sub_title("Transactions: BEGIN, COMMIT, ROLLBACK")
pdf.body_text(
    "Transactions group multiple operations into one atomic unit. Critical for test "
    "isolation - you can set up data, run your test, then ROLLBACK to undo everything."
)

pdf.code_block(
    "-- Basic transaction\n"
    "BEGIN;\n"
    "  INSERT INTO users (name) VALUES ('Test User');\n"
    "  INSERT INTO swords (name, attack, owner_id)\n"
    "    VALUES ('Test Sword', 100, 4);\n"
    "COMMIT;  -- saves both changes\n\n"
    "-- Rollback: undo everything if something goes wrong\n"
    "BEGIN;\n"
    "  DELETE FROM swords WHERE owner_id = 1;\n"
    "  -- Oops, wrong user!\n"
    "ROLLBACK;  -- nothing was deleted"
)
pdf.body_text(
    "Test automation tip: Wrap your test data setup in a transaction. After assertions, "
    "ROLLBACK to leave the database clean for the next test."
)

# ══════════════════════════════════════════════════════════
# SECTION 3: GOOD TO KNOW (Advanced)
# ══════════════════════════════════════════════════════════
pdf.add_page()
pdf.section_title("3. Good to Know (Advanced Verification)")

# Window functions
pdf.sub_title("Window Functions: ROW_NUMBER(), RANK()")
pdf.body_text(
    "Window functions perform calculations across rows related to the current row "
    "without collapsing them into groups (unlike GROUP BY)."
)

pdf.code_block(
    "-- Rank swords by attack power\n"
    "SELECT name, attack,\n"
    "  ROW_NUMBER() OVER (ORDER BY attack DESC) as rank\n"
    "FROM swords;"
)
pdf.result_label()
pdf.result_table(
    ["name", "attack", "rank"],
    [
        ["Wolf Bane", "214", "1"],
        ["Oathkeeper", "200", "2"],
        ["KrakenSlayer", "185", "3"],
    ],
    col_widths=[50, 30, 30],
)

# CTEs
pdf.sub_title("CTEs (Common Table Expressions)")
pdf.body_text(
    "CTEs let you define temporary named result sets using WITH. "
    "They make complex queries much more readable."
)

pdf.code_block(
    "-- Find users with powerful swords (attack > 190)\n"
    "WITH powerful_swords AS (\n"
    "  SELECT owner_id, name AS sword, attack\n"
    "  FROM swords\n"
    "  WHERE attack > 190\n"
    ")\n"
    "SELECT u.name, ps.sword, ps.attack\n"
    "FROM users u\n"
    "JOIN powerful_swords ps ON u.id = ps.owner_id;"
)
pdf.result_label()
pdf.result_table(
    ["name", "sword", "attack"],
    [
        ["Jaime", "Oathkeeper", "200"],
        ["Jon Snow", "Wolf Bane", "214"],
    ],
    col_widths=[45, 50, 30],
)

# EXPLAIN
pdf.sub_title("EXPLAIN / EXPLAIN ANALYZE")
pdf.body_text(
    "EXPLAIN shows how the database plans to execute your query. "
    "EXPLAIN ANALYZE actually runs it and shows real timing. Useful when "
    "debugging slow test suites caused by slow queries."
)

pdf.code_block(
    "-- See the query plan (does NOT execute the query)\n"
    "EXPLAIN SELECT * FROM users WHERE name = 'Jaime';\n\n"
    "-- See plan + actual execution time\n"
    "EXPLAIN ANALYZE SELECT * FROM users WHERE name = 'Jaime';"
)
pdf.result_label()
pdf.body_text(
    "Returns a query plan showing: Seq Scan on users, cost, rows, width, "
    "and actual time/loops if using ANALYZE. Look for 'Seq Scan' (slow on big tables) "
    "vs 'Index Scan' (fast)."
)

# Schema commands
pdf.sub_title("CREATE, DROP, ALTER TABLE")
pdf.body_text(
    "Schema commands define the structure of your database. Understanding them "
    "helps you read migration files and set up test databases."
)

pdf.code_block(
    "-- Create a table\n"
    "CREATE TABLE users (\n"
    "  id SERIAL PRIMARY KEY,\n"
    "  name TEXT NOT NULL\n"
    ");\n\n"
    "-- Create swords table with foreign key\n"
    "CREATE TABLE swords (\n"
    "  id SERIAL PRIMARY KEY,\n"
    "  name TEXT NOT NULL,\n"
    "  attack INTEGER NOT NULL,\n"
    "  owner_id INTEGER REFERENCES users(id)\n"
    ");\n\n"
    "-- Add a column\n"
    "ALTER TABLE users ADD COLUMN email TEXT;\n\n"
    "-- Drop (delete) a table\n"
    "DROP TABLE IF EXISTS swords;"
)

# Constraints
pdf.sub_title("Constraints: PRIMARY KEY, FOREIGN KEY, UNIQUE, NOT NULL")
pdf.body_text(
    "Constraints enforce rules on your data. Knowing them helps you write tests "
    "that verify data integrity."
)

pdf.code_block(
    "-- PRIMARY KEY: unique identifier for each row (id in users)\n"
    "-- FOREIGN KEY: links to another table (owner_id -> users.id)\n"
    "-- UNIQUE: no duplicate values allowed\n"
    "-- NOT NULL: value is required\n\n"
    "-- Example: try inserting a sword with invalid owner_id\n"
    "INSERT INTO swords (name, attack, owner_id)\n"
    "VALUES ('Ghost Blade', 300, 999);\n"
    "-- ERROR: insert violates foreign key constraint\n"
    "-- (user with id=999 does not exist)"
)

# ══════════════════════════════════════════════════════════
# SECTION 4: TEST AUTOMATION SPECIFIC
# ══════════════════════════════════════════════════════════
pdf.add_page()
pdf.section_title("4. Test Automation Specific Patterns")

pdf.sub_title("Verify data after an API call")
pdf.body_text("After your test calls POST /api/users to create 'Arya', verify it was saved:")
pdf.code_block(
    "SELECT * FROM users WHERE name = 'Arya';"
)
pdf.result_label()
pdf.result_table(
    ["id", "name"],
    [["4", "Arya"]],
    col_widths=[30, 60],
)

pdf.sub_title("Set up test data")
pdf.body_text("Insert known data before your test runs:")
pdf.code_block(
    "INSERT INTO users (name) VALUES ('Test User')\n"
    "RETURNING id;  -- get the generated ID back"
)
pdf.result_label()
pdf.result_table(["id"], [["4"]], col_widths=[30])

pdf.sub_title("Clean up after tests")
pdf.body_text("Remove test data to keep the database clean:")
pdf.code_block(
    "-- Delete specific test data\n"
    "DELETE FROM swords WHERE owner_id = 4;\n"
    "DELETE FROM users WHERE name = 'Test User';\n\n"
    "-- Or use TRUNCATE to remove ALL rows (faster, resets IDs)\n"
    "TRUNCATE TABLE swords CASCADE;"
)

pdf.sub_title("Validate no duplicates exist")
pdf.body_text("Check for data integrity issues after a test run:")
pdf.code_block(
    "SELECT name, COUNT(*) as count\n"
    "FROM users\n"
    "GROUP BY name\n"
    "HAVING COUNT(*) > 1;"
)
pdf.result_label()
pdf.body_text("(empty result - no duplicates found)")
pdf.body_text("If this returns rows, you have duplicate data that needs investigation.")

pdf.sub_title("Check data integrity (find orphaned records)")
pdf.body_text("Find swords that reference non-existent users:")
pdf.code_block(
    "SELECT s.*\n"
    "FROM swords s\n"
    "LEFT JOIN users u ON s.owner_id = u.id\n"
    "WHERE u.id IS NULL;"
)
pdf.result_label()
pdf.body_text("(empty result - no orphaned swords found)")

pdf.sub_title("Compare before/after state")
pdf.body_text("Count records before and after a test action:")
pdf.code_block(
    "-- Before test: 3 users\n"
    "SELECT COUNT(*) as user_count FROM users;"
)
pdf.result_label()
pdf.result_table(["user_count"], [["3"]], col_widths=[40])

pdf.code_block(
    "-- After test inserts a user: 4 users\n"
    "SELECT COUNT(*) as user_count FROM users;"
)
pdf.result_label()
pdf.result_table(["user_count"], [["4"]], col_widths=[40])

# ══════════════════════════════════════════════════════════
# SECTION 5: PYTHON + SQL
# ══════════════════════════════════════════════════════════
pdf.add_page()
pdf.section_title("5. Using SQL in Python (psycopg2)")

pdf.body_text(
    "In test automation with Python, you typically use a library like psycopg2 "
    "to execute SQL queries. Here are common patterns:"
)

pdf.sub_title("Basic query with parameterization")
pdf.code_block(
    "import psycopg2\n\n"
    "conn = psycopg2.connect(DATABASE_URL)\n"
    "with conn.cursor() as cur:\n"
    "    # SAFE: parameterized query\n"
    "    cur.execute(\n"
    '        "SELECT * FROM users WHERE name = %s;",\n'
    '        ("Jaime",)\n'
    "    )\n"
    "    result = cur.fetchone()\n"
    "    # result = (1, 'Jaime')\n\n"
    "    # NEVER do this (SQL injection risk):\n"
    '    # cur.execute(f"SELECT * FROM users WHERE name = \'{name}\'")'
)

pdf.sub_title("Fetch methods")
pdf.code_block(
    'cur.execute("SELECT * FROM users;")\n\n'
    "# fetchone()  - returns single row as tuple\n"
    "row = cur.fetchone()\n"
    "# row = (1, 'Jaime')\n\n"
    "# fetchall()  - returns all rows as list of tuples\n"
    "rows = cur.fetchall()\n"
    "# rows = [(1, 'Jaime'), (2, 'Jon Snow'), (3, 'Theon Greyjoy')]\n\n"
    "# fetchmany(n) - returns n rows\n"
    "some = cur.fetchmany(2)\n"
    "# some = [(1, 'Jaime'), (2, 'Jon Snow')]"
)

pdf.sub_title("Assert query results in tests")
pdf.code_block(
    "def test_user_has_sword(db_cursor):\n"
    "    db_cursor.execute(\n"
    '        "SELECT u.name, s.name FROM users u "\n'
    '        "JOIN swords s ON u.id = s.owner_id "\n'
    '        "WHERE u.name = %s",\n'
    '        ("Jaime",)\n'
    "    )\n"
    "    result = db_cursor.fetchone()\n"
    "    # result = ('Jaime', 'Oathkeeper')\n\n"
    '    assert result is not None, "User not found"\n'
    '    assert result[0] == "Jaime"\n'
    '    assert result[1] == "Oathkeeper"'
)

pdf.sub_title("Transaction rollback for test cleanup")
pdf.code_block(
    "import pytest\n\n"
    "@pytest.fixture\n"
    "def db_conn():\n"
    "    conn = psycopg2.connect(DATABASE_URL)\n"
    "    yield conn\n"
    "    conn.rollback()  # undo all changes after each test\n"
    "    conn.close()\n\n"
    "def test_insert_user(db_conn):\n"
    "    with db_conn.cursor() as cur:\n"
    '        cur.execute("INSERT INTO users (name) VALUES (%s)", ("Test",))\n'
    '        cur.execute("SELECT COUNT(*) FROM users")\n'
    "        assert cur.fetchone()[0] == 4  # original 3 + 1\n"
    "    # After test: db_conn.rollback() runs automatically\n"
    "    # The inserted user is removed - database stays clean!"
)

# ── Quick Reference ──
pdf.add_page()
pdf.section_title("Quick Reference Cheat Sheet")

commands = [
    ("SELECT", "Retrieve data from table(s)"),
    ("WHERE", "Filter rows by condition"),
    ("JOIN", "Combine rows from multiple tables"),
    ("INSERT INTO", "Add new rows"),
    ("UPDATE ... SET", "Modify existing rows"),
    ("DELETE FROM", "Remove rows"),
    ("ORDER BY", "Sort results"),
    ("LIMIT", "Restrict number of results"),
    ("DISTINCT", "Remove duplicate values"),
    ("GROUP BY", "Group rows for aggregation"),
    ("HAVING", "Filter groups (after GROUP BY)"),
    ("COUNT/SUM/AVG", "Aggregate functions"),
    ("IS NULL", "Check for missing values"),
    ("COALESCE", "Return first non-NULL value"),
    ("IN / NOT IN", "Match against a list"),
    ("BETWEEN", "Match within a range"),
    ("LIKE", "Pattern matching (% and _)"),
    ("EXISTS", "Check if subquery has results"),
    ("UNION", "Combine two result sets"),
    ("CASE WHEN", "Conditional logic"),
    ("BEGIN/COMMIT", "Transaction control"),
    ("ROLLBACK", "Undo transaction changes"),
    ("EXPLAIN ANALYZE", "Query performance analysis"),
    ("ROW_NUMBER()", "Window function - row numbering"),
    ("WITH ... AS", "CTE - named subquery"),
]

pdf.set_font("Helvetica", "B", 10)
pdf.set_fill_color(30, 30, 120)
pdf.set_text_color(255, 255, 255)
pdf.cell(60, 8, "  Command", fill=True)
pdf.cell(130, 8, "  Description", fill=True, new_x="LMARGIN", new_y="NEXT")

for i, (cmd, desc) in enumerate(commands):
    pdf.set_text_color(0, 0, 0)
    if i % 2 == 0:
        pdf.set_fill_color(245, 245, 255)
    else:
        pdf.set_fill_color(255, 255, 255)
    pdf.set_font("Courier", "B", 9)
    pdf.cell(60, 7, f"  {cmd}", fill=True)
    pdf.set_font("Helvetica", "", 9)
    pdf.cell(130, 7, f"  {desc}", fill=True, new_x="LMARGIN", new_y="NEXT")

output_path = "SQL_Guide_For_Test_Automation_Engineers.pdf"
pdf.output(output_path)
print(f"PDF generated: {output_path}")
