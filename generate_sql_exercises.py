from fpdf import FPDF


class ExercisePDF(FPDF):
    def header(self):
        self.set_font("Helvetica", "B", 12)
        self.set_text_color(50, 50, 150)
        self.cell(0, 10, "SQL Exercises for Test Automation Engineers", align="C", new_x="LMARGIN", new_y="NEXT")
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
        self.ln(4)
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

    def answer_block(self, code):
        self.set_font("Courier", "", 9)
        self.set_fill_color(230, 255, 230)
        self.set_text_color(0, 80, 0)
        x = self.get_x()
        self.set_x(x + 5)
        self.multi_cell(180, 5, code, fill=True)
        self.ln(3)

    def result_label(self):
        self.set_font("Helvetica", "B", 9)
        self.set_text_color(0, 120, 0)
        self.cell(0, 6, "Expected Result:", new_x="LMARGIN", new_y="NEXT")
        self.ln(1)

    def result_table(self, headers, rows, col_widths=None):
        if col_widths is None:
            total = 180
            col_widths = [total // len(headers)] * len(headers)
            col_widths[-1] = total - sum(col_widths[:-1])

        x_start = self.get_x() + 5
        self.set_x(x_start)

        self.set_font("Courier", "B", 8)
        self.set_fill_color(30, 30, 120)
        self.set_text_color(255, 255, 255)
        for i, h in enumerate(headers):
            self.cell(col_widths[i], 6, f" {h}", fill=True)
        self.ln()

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

    def question(self, number, text):
        self.set_font("Helvetica", "B", 10)
        self.set_text_color(30, 30, 120)
        self.cell(0, 7, f"Q{number}.", new_x="LMARGIN", new_y="NEXT")
        self.set_font("Helvetica", "", 10)
        self.set_text_color(0, 0, 0)
        self.multi_cell(0, 6, text)
        self.ln(2)

    def write_space(self, lines=3):
        """Blank lines for the student to write their answer."""
        self.set_font("Courier", "", 9)
        self.set_draw_color(200, 200, 200)
        for _ in range(lines):
            y = self.get_y()
            self.line(15, y, 195, y)
            self.ln(7)
        self.ln(2)

    def difficulty_badge(self, level):
        colors = {
            "Easy": (0, 150, 0),
            "Medium": (200, 150, 0),
            "Hard": (200, 0, 0),
        }
        r, g, b = colors.get(level, (0, 0, 0))
        self.set_font("Helvetica", "B", 8)
        self.set_text_color(r, g, b)
        self.cell(30, 5, f"[{level}]")
        self.set_text_color(0, 0, 0)
        self.ln(2)


pdf = ExercisePDF()
pdf.alias_nb_pages()
pdf.set_auto_page_break(auto=True, margin=20)

# ── Title Page ──
pdf.add_page()
pdf.ln(30)
pdf.set_font("Helvetica", "B", 28)
pdf.set_text_color(30, 30, 120)
pdf.cell(0, 15, "SQL Exercises", align="C", new_x="LMARGIN", new_y="NEXT")
pdf.set_font("Helvetica", "", 16)
pdf.set_text_color(80, 80, 80)
pdf.cell(0, 12, "Practice Problems with Answers", align="C", new_x="LMARGIN", new_y="NEXT")
pdf.ln(8)
pdf.set_font("Helvetica", "I", 11)
pdf.cell(0, 10, "30 exercises from Easy to Hard - based on your database tables", align="C", new_x="LMARGIN", new_y="NEXT")

pdf.ln(15)
pdf.set_font("Helvetica", "B", 13)
pdf.set_text_color(30, 30, 120)
pdf.cell(0, 10, "Your Database Tables", align="C", new_x="LMARGIN", new_y="NEXT")
pdf.ln(5)

pdf.sub_title("users")
pdf.result_table(
    ["id", "name"],
    [["1", "Jaime"], ["2", "Jon Snow"], ["3", "Theon Greyjoy"]],
    col_widths=[30, 60],
)

pdf.sub_title("swords")
pdf.result_table(
    ["id", "name", "attack", "owner_id"],
    [
        ["1", "Oathkeeper", "200", "1"],
        ["2", "Wolf Bane", "214", "2"],
        ["3", "KrakenSlayer", "185", "3"],
    ],
    col_widths=[20, 50, 30, 30],
)

pdf.body_text("Instructions: Write the SQL query that answers each question. Answers are at the end of the PDF.")

# ══════════════════════════════════════════════════════════
# EXERCISES SECTION
# ══════════════════════════════════════════════════════════

# ── EASY (1-10) ──
pdf.add_page()
pdf.section_title("Section A: Easy (SELECT, WHERE, ORDER BY)")

pdf.question(1, "Select all columns from the users table.")
pdf.difficulty_badge("Easy")
pdf.write_space(2)

pdf.question(2, "Select only the name column from the users table.")
pdf.difficulty_badge("Easy")
pdf.write_space(2)

pdf.question(3, "Find the user whose name is 'Jon Snow'.")
pdf.difficulty_badge("Easy")
pdf.write_space(2)

pdf.question(4, "Find all swords with an attack value greater than 190.")
pdf.difficulty_badge("Easy")
pdf.write_space(2)

pdf.question(5, "Select all users sorted by name in alphabetical order (A-Z).")
pdf.difficulty_badge("Easy")
pdf.write_space(2)

pdf.question(6, "Select all swords sorted by attack power from highest to lowest.")
pdf.difficulty_badge("Easy")
pdf.write_space(2)

pdf.question(7, "Find swords with attack between 185 and 200 (inclusive).")
pdf.difficulty_badge("Easy")
pdf.write_space(2)

pdf.question(8, "Find users whose name starts with 'J'.")
pdf.difficulty_badge("Easy")
pdf.write_space(2)

pdf.question(9, "Select only the first 2 users from the users table.")
pdf.difficulty_badge("Easy")
pdf.write_space(2)

pdf.question(10, "Find users whose name is either 'Jaime' or 'Theon Greyjoy' using IN.")
pdf.difficulty_badge("Easy")
pdf.write_space(2)

# ── MEDIUM (11-20) ──
pdf.add_page()
pdf.section_title("Section B: Medium (JOIN, Aggregates, GROUP BY)")

pdf.question(11, "Count the total number of users.")
pdf.difficulty_badge("Medium")
pdf.write_space(2)

pdf.question(12, "Find the sword with the highest attack value. Show only the name and attack.")
pdf.difficulty_badge("Medium")
pdf.write_space(2)

pdf.question(13, "Calculate the average attack power of all swords.")
pdf.difficulty_badge("Medium")
pdf.write_space(2)

pdf.question(14, "Find the total (SUM) of all sword attack values.")
pdf.difficulty_badge("Medium")
pdf.write_space(2)

pdf.question(15, "Join users and swords to show each user's name alongside their sword name.")
pdf.difficulty_badge("Medium")
pdf.write_space(3)

pdf.question(16, "Join users and swords, but only show users whose sword has attack > 200.")
pdf.difficulty_badge("Medium")
pdf.write_space(3)

pdf.question(17, "Show each user's name, sword name, and attack - sorted by attack descending.")
pdf.difficulty_badge("Medium")
pdf.write_space(3)

pdf.question(18, "Insert a new user named 'Arya Stark' into the users table.")
pdf.difficulty_badge("Medium")
pdf.write_space(2)

pdf.question(19, "Update the attack value of 'KrakenSlayer' to 195.")
pdf.difficulty_badge("Medium")
pdf.write_space(2)

pdf.question(20, "Delete the user named 'Arya Stark' from the users table.")
pdf.difficulty_badge("Medium")
pdf.write_space(2)

# ── HARD (21-30) ──
pdf.add_page()
pdf.section_title("Section C: Hard (Subqueries, CASE, Window Functions, CTEs)")

pdf.question(21, "Find the user who owns the sword with the highest attack value. Use a subquery.")
pdf.difficulty_badge("Hard")
pdf.write_space(3)

pdf.question(22, "Using CASE WHEN, label each sword as 'Legendary' if attack >= 210, 'Epic' if >= 195, or 'Common' otherwise. Show name, attack, and the label.")
pdf.difficulty_badge("Hard")
pdf.write_space(4)

pdf.question(23, "Use a CTE (WITH) to first find swords with attack > 190, then join with users to show the owner's name.")
pdf.difficulty_badge("Hard")
pdf.write_space(4)

pdf.question(24, "Use ROW_NUMBER() to rank all swords by attack power (highest first). Show name, attack, and rank.")
pdf.difficulty_badge("Hard")
pdf.write_space(3)

pdf.question(25, "Find users who own a sword using EXISTS (not JOIN or IN).")
pdf.difficulty_badge("Hard")
pdf.write_space(3)

pdf.question(26, "Combine user names and sword names into a single column called 'all_names' using UNION.")
pdf.difficulty_badge("Hard")
pdf.write_space(3)

pdf.question(27, "Find the owner_id that has the sword with the minimum attack, using a subquery in WHERE.")
pdf.difficulty_badge("Hard")
pdf.write_space(3)

pdf.question(28, "Using LEFT JOIN, find users who do NOT have a sword (assume some users might not). Show only users where the sword is NULL.")
pdf.difficulty_badge("Hard")
pdf.write_space(3)

pdf.question(29, "Write a query that shows each user's name, their sword's attack, and what percentage of the total attack their sword represents. (Hint: use a subquery for total.)")
pdf.difficulty_badge("Hard")
pdf.write_space(4)

pdf.question(30, "Write a transaction that inserts a new user 'Sansa Stark' (id=4) and a new sword 'Needle' (attack=150, owner_id=4), then commits.")
pdf.difficulty_badge("Hard")
pdf.write_space(4)

# ══════════════════════════════════════════════════════════
# ANSWERS SECTION
# ══════════════════════════════════════════════════════════
pdf.add_page()
pdf.section_title("ANSWERS")
pdf.body_text("Compare your queries with these solutions. Multiple correct answers may exist!")

# ── EASY ANSWERS ──
pdf.sub_title("Section A: Easy")

pdf.set_font("Helvetica", "B", 10)
pdf.set_text_color(30, 30, 120)
pdf.cell(0, 7, "Q1. Select all columns from users", new_x="LMARGIN", new_y="NEXT")
pdf.answer_block("SELECT * FROM users;")
pdf.result_label()
pdf.result_table(
    ["id", "name"],
    [["1", "Jaime"], ["2", "Jon Snow"], ["3", "Theon Greyjoy"]],
    col_widths=[30, 60],
)

pdf.set_font("Helvetica", "B", 10)
pdf.set_text_color(30, 30, 120)
pdf.cell(0, 7, "Q2. Select only the name column", new_x="LMARGIN", new_y="NEXT")
pdf.answer_block("SELECT name FROM users;")
pdf.result_label()
pdf.result_table(["name"], [["Jaime"], ["Jon Snow"], ["Theon Greyjoy"]], col_widths=[60])

pdf.set_font("Helvetica", "B", 10)
pdf.set_text_color(30, 30, 120)
pdf.cell(0, 7, "Q3. Find Jon Snow", new_x="LMARGIN", new_y="NEXT")
pdf.answer_block("SELECT * FROM users WHERE name = 'Jon Snow';")
pdf.result_label()
pdf.result_table(["id", "name"], [["2", "Jon Snow"]], col_widths=[30, 60])

pdf.set_font("Helvetica", "B", 10)
pdf.set_text_color(30, 30, 120)
pdf.cell(0, 7, "Q4. Swords with attack > 190", new_x="LMARGIN", new_y="NEXT")
pdf.answer_block("SELECT * FROM swords WHERE attack > 190;")
pdf.result_label()
pdf.result_table(
    ["id", "name", "attack", "owner_id"],
    [["1", "Oathkeeper", "200", "1"], ["2", "Wolf Bane", "214", "2"]],
    col_widths=[20, 50, 30, 30],
)

pdf.set_font("Helvetica", "B", 10)
pdf.set_text_color(30, 30, 120)
pdf.cell(0, 7, "Q5. Users sorted A-Z", new_x="LMARGIN", new_y="NEXT")
pdf.answer_block("SELECT * FROM users ORDER BY name ASC;")
pdf.result_label()
pdf.result_table(
    ["id", "name"],
    [["1", "Jaime"], ["2", "Jon Snow"], ["3", "Theon Greyjoy"]],
    col_widths=[30, 60],
)

pdf.add_page()

pdf.set_font("Helvetica", "B", 10)
pdf.set_text_color(30, 30, 120)
pdf.cell(0, 7, "Q6. Swords sorted by attack DESC", new_x="LMARGIN", new_y="NEXT")
pdf.answer_block("SELECT * FROM swords ORDER BY attack DESC;")
pdf.result_label()
pdf.result_table(
    ["id", "name", "attack", "owner_id"],
    [["2", "Wolf Bane", "214", "2"], ["1", "Oathkeeper", "200", "1"], ["3", "KrakenSlayer", "185", "3"]],
    col_widths=[20, 50, 30, 30],
)

pdf.set_font("Helvetica", "B", 10)
pdf.set_text_color(30, 30, 120)
pdf.cell(0, 7, "Q7. Swords with attack between 185 and 200", new_x="LMARGIN", new_y="NEXT")
pdf.answer_block("SELECT * FROM swords WHERE attack BETWEEN 185 AND 200;")
pdf.result_label()
pdf.result_table(
    ["id", "name", "attack", "owner_id"],
    [["1", "Oathkeeper", "200", "1"], ["3", "KrakenSlayer", "185", "3"]],
    col_widths=[20, 50, 30, 30],
)

pdf.set_font("Helvetica", "B", 10)
pdf.set_text_color(30, 30, 120)
pdf.cell(0, 7, "Q8. Users whose name starts with 'J'", new_x="LMARGIN", new_y="NEXT")
pdf.answer_block("SELECT * FROM users WHERE name LIKE 'J%';")
pdf.result_label()
pdf.result_table(
    ["id", "name"],
    [["1", "Jaime"], ["2", "Jon Snow"]],
    col_widths=[30, 60],
)

pdf.set_font("Helvetica", "B", 10)
pdf.set_text_color(30, 30, 120)
pdf.cell(0, 7, "Q9. First 2 users", new_x="LMARGIN", new_y="NEXT")
pdf.answer_block("SELECT * FROM users LIMIT 2;")
pdf.result_label()
pdf.result_table(
    ["id", "name"],
    [["1", "Jaime"], ["2", "Jon Snow"]],
    col_widths=[30, 60],
)

pdf.set_font("Helvetica", "B", 10)
pdf.set_text_color(30, 30, 120)
pdf.cell(0, 7, "Q10. Jaime or Theon using IN", new_x="LMARGIN", new_y="NEXT")
pdf.answer_block("SELECT * FROM users WHERE name IN ('Jaime', 'Theon Greyjoy');")
pdf.result_label()
pdf.result_table(
    ["id", "name"],
    [["1", "Jaime"], ["3", "Theon Greyjoy"]],
    col_widths=[30, 60],
)

# ── MEDIUM ANSWERS ──
pdf.add_page()
pdf.sub_title("Section B: Medium")

pdf.set_font("Helvetica", "B", 10)
pdf.set_text_color(30, 30, 120)
pdf.cell(0, 7, "Q11. Count total users", new_x="LMARGIN", new_y="NEXT")
pdf.answer_block("SELECT COUNT(*) FROM users;")
pdf.result_label()
pdf.result_table(["count"], [["3"]], col_widths=[30])

pdf.set_font("Helvetica", "B", 10)
pdf.set_text_color(30, 30, 120)
pdf.cell(0, 7, "Q12. Sword with highest attack", new_x="LMARGIN", new_y="NEXT")
pdf.answer_block("SELECT name, attack FROM swords ORDER BY attack DESC LIMIT 1;")
pdf.result_label()
pdf.result_table(["name", "attack"], [["Wolf Bane", "214"]], col_widths=[50, 30])

pdf.set_font("Helvetica", "B", 10)
pdf.set_text_color(30, 30, 120)
pdf.cell(0, 7, "Q13. Average attack", new_x="LMARGIN", new_y="NEXT")
pdf.answer_block("SELECT AVG(attack) FROM swords;")
pdf.result_label()
pdf.result_table(["avg"], [["199.67"]], col_widths=[30])

pdf.set_font("Helvetica", "B", 10)
pdf.set_text_color(30, 30, 120)
pdf.cell(0, 7, "Q14. Sum of all attack values", new_x="LMARGIN", new_y="NEXT")
pdf.answer_block("SELECT SUM(attack) FROM swords;")
pdf.result_label()
pdf.result_table(["sum"], [["599"]], col_widths=[30])

pdf.set_font("Helvetica", "B", 10)
pdf.set_text_color(30, 30, 120)
pdf.cell(0, 7, "Q15. Join users and swords", new_x="LMARGIN", new_y="NEXT")
pdf.answer_block(
    "SELECT users.name, swords.name AS sword\n"
    "FROM users\n"
    "JOIN swords ON users.id = swords.owner_id;"
)
pdf.result_label()
pdf.result_table(
    ["name", "sword"],
    [["Jaime", "Oathkeeper"], ["Jon Snow", "Wolf Bane"], ["Theon Greyjoy", "KrakenSlayer"]],
    col_widths=[50, 50],
)

pdf.set_font("Helvetica", "B", 10)
pdf.set_text_color(30, 30, 120)
pdf.cell(0, 7, "Q16. Join with attack > 200", new_x="LMARGIN", new_y="NEXT")
pdf.answer_block(
    "SELECT users.name, swords.name AS sword, swords.attack\n"
    "FROM users\n"
    "JOIN swords ON users.id = swords.owner_id\n"
    "WHERE swords.attack > 200;"
)
pdf.result_label()
pdf.result_table(
    ["name", "sword", "attack"],
    [["Jon Snow", "Wolf Bane", "214"]],
    col_widths=[45, 50, 30],
)

pdf.add_page()

pdf.set_font("Helvetica", "B", 10)
pdf.set_text_color(30, 30, 120)
pdf.cell(0, 7, "Q17. Join sorted by attack DESC", new_x="LMARGIN", new_y="NEXT")
pdf.answer_block(
    "SELECT users.name, swords.name AS sword, swords.attack\n"
    "FROM users\n"
    "JOIN swords ON users.id = swords.owner_id\n"
    "ORDER BY swords.attack DESC;"
)
pdf.result_label()
pdf.result_table(
    ["name", "sword", "attack"],
    [["Jon Snow", "Wolf Bane", "214"], ["Jaime", "Oathkeeper", "200"], ["Theon Greyjoy", "KrakenSlayer", "185"]],
    col_widths=[45, 50, 30],
)

pdf.set_font("Helvetica", "B", 10)
pdf.set_text_color(30, 30, 120)
pdf.cell(0, 7, "Q18. Insert Arya Stark", new_x="LMARGIN", new_y="NEXT")
pdf.answer_block("INSERT INTO users (name) VALUES ('Arya Stark');")
pdf.body_text("After running, users table will have 4 rows with Arya Stark as id=4.")

pdf.set_font("Helvetica", "B", 10)
pdf.set_text_color(30, 30, 120)
pdf.cell(0, 7, "Q19. Update KrakenSlayer attack", new_x="LMARGIN", new_y="NEXT")
pdf.answer_block("UPDATE swords SET attack = 195 WHERE name = 'KrakenSlayer';")
pdf.result_label()
pdf.body_text("KrakenSlayer's attack is now 195 instead of 185.")

pdf.set_font("Helvetica", "B", 10)
pdf.set_text_color(30, 30, 120)
pdf.cell(0, 7, "Q20. Delete Arya Stark", new_x="LMARGIN", new_y="NEXT")
pdf.answer_block("DELETE FROM users WHERE name = 'Arya Stark';")
pdf.body_text("Arya is removed. Table is back to 3 users.")

# ── HARD ANSWERS ──
pdf.add_page()
pdf.sub_title("Section C: Hard")

pdf.set_font("Helvetica", "B", 10)
pdf.set_text_color(30, 30, 120)
pdf.cell(0, 7, "Q21. User with highest attack sword (subquery)", new_x="LMARGIN", new_y="NEXT")
pdf.answer_block(
    "SELECT * FROM users\n"
    "WHERE id = (\n"
    "  SELECT owner_id FROM swords\n"
    "  ORDER BY attack DESC LIMIT 1\n"
    ");"
)
pdf.result_label()
pdf.result_table(["id", "name"], [["2", "Jon Snow"]], col_widths=[30, 60])

pdf.set_font("Helvetica", "B", 10)
pdf.set_text_color(30, 30, 120)
pdf.cell(0, 7, "Q22. CASE WHEN for sword rarity", new_x="LMARGIN", new_y="NEXT")
pdf.answer_block(
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
    [["Oathkeeper", "200", "Epic"], ["Wolf Bane", "214", "Legendary"], ["KrakenSlayer", "185", "Common"]],
    col_widths=[50, 30, 40],
)

pdf.set_font("Helvetica", "B", 10)
pdf.set_text_color(30, 30, 120)
pdf.cell(0, 7, "Q23. CTE for powerful swords", new_x="LMARGIN", new_y="NEXT")
pdf.answer_block(
    "WITH strong_swords AS (\n"
    "  SELECT owner_id, name AS sword, attack\n"
    "  FROM swords WHERE attack > 190\n"
    ")\n"
    "SELECT u.name, ss.sword, ss.attack\n"
    "FROM users u\n"
    "JOIN strong_swords ss ON u.id = ss.owner_id;"
)
pdf.result_label()
pdf.result_table(
    ["name", "sword", "attack"],
    [["Jaime", "Oathkeeper", "200"], ["Jon Snow", "Wolf Bane", "214"]],
    col_widths=[45, 50, 30],
)

pdf.add_page()

pdf.set_font("Helvetica", "B", 10)
pdf.set_text_color(30, 30, 120)
pdf.cell(0, 7, "Q24. ROW_NUMBER() to rank swords", new_x="LMARGIN", new_y="NEXT")
pdf.answer_block(
    "SELECT name, attack,\n"
    "  ROW_NUMBER() OVER (ORDER BY attack DESC) AS rank\n"
    "FROM swords;"
)
pdf.result_label()
pdf.result_table(
    ["name", "attack", "rank"],
    [["Wolf Bane", "214", "1"], ["Oathkeeper", "200", "2"], ["KrakenSlayer", "185", "3"]],
    col_widths=[50, 30, 30],
)

pdf.set_font("Helvetica", "B", 10)
pdf.set_text_color(30, 30, 120)
pdf.cell(0, 7, "Q25. EXISTS to find sword owners", new_x="LMARGIN", new_y="NEXT")
pdf.answer_block(
    "SELECT * FROM users u\n"
    "WHERE EXISTS (\n"
    "  SELECT 1 FROM swords s\n"
    "  WHERE s.owner_id = u.id\n"
    ");"
)
pdf.result_label()
pdf.result_table(
    ["id", "name"],
    [["1", "Jaime"], ["2", "Jon Snow"], ["3", "Theon Greyjoy"]],
    col_widths=[30, 60],
)

pdf.set_font("Helvetica", "B", 10)
pdf.set_text_color(30, 30, 120)
pdf.cell(0, 7, "Q26. UNION user names and sword names", new_x="LMARGIN", new_y="NEXT")
pdf.answer_block(
    "SELECT name AS all_names FROM users\n"
    "UNION\n"
    "SELECT name FROM swords;"
)
pdf.result_label()
pdf.result_table(
    ["all_names"],
    [["Jaime"], ["Jon Snow"], ["Theon Greyjoy"], ["Oathkeeper"], ["Wolf Bane"], ["KrakenSlayer"]],
    col_widths=[60],
)

pdf.set_font("Helvetica", "B", 10)
pdf.set_text_color(30, 30, 120)
pdf.cell(0, 7, "Q27. Owner of sword with min attack (subquery)", new_x="LMARGIN", new_y="NEXT")
pdf.answer_block(
    "SELECT owner_id FROM swords\n"
    "WHERE attack = (SELECT MIN(attack) FROM swords);"
)
pdf.result_label()
pdf.result_table(["owner_id"], [["3"]], col_widths=[30])
pdf.body_text("owner_id 3 = Theon Greyjoy, who owns KrakenSlayer (attack: 185)")

pdf.add_page()

pdf.set_font("Helvetica", "B", 10)
pdf.set_text_color(30, 30, 120)
pdf.cell(0, 7, "Q28. LEFT JOIN to find users without swords", new_x="LMARGIN", new_y="NEXT")
pdf.answer_block(
    "SELECT u.id, u.name\n"
    "FROM users u\n"
    "LEFT JOIN swords s ON u.id = s.owner_id\n"
    "WHERE s.id IS NULL;"
)
pdf.result_label()
pdf.body_text("(empty result - all 3 users currently have swords. If a user without a sword existed, they would appear here.)")

pdf.set_font("Helvetica", "B", 10)
pdf.set_text_color(30, 30, 120)
pdf.cell(0, 7, "Q29. Attack percentage of total", new_x="LMARGIN", new_y="NEXT")
pdf.answer_block(
    "SELECT u.name, s.attack,\n"
    "  ROUND(s.attack * 100.0 / (SELECT SUM(attack) FROM swords), 1)\n"
    "    AS pct_of_total\n"
    "FROM users u\n"
    "JOIN swords s ON u.id = s.owner_id;"
)
pdf.result_label()
pdf.result_table(
    ["name", "attack", "pct_of_total"],
    [["Jaime", "200", "33.4"], ["Jon Snow", "214", "35.7"], ["Theon Greyjoy", "185", "30.9"]],
    col_widths=[50, 30, 40],
)

pdf.set_font("Helvetica", "B", 10)
pdf.set_text_color(30, 30, 120)
pdf.cell(0, 7, "Q30. Transaction: insert user + sword", new_x="LMARGIN", new_y="NEXT")
pdf.answer_block(
    "BEGIN;\n"
    "  INSERT INTO users (id, name)\n"
    "    VALUES (4, 'Sansa Stark');\n"
    "  INSERT INTO swords (name, attack, owner_id)\n"
    "    VALUES ('Needle', 150, 4);\n"
    "COMMIT;"
)
pdf.result_label()
pdf.body_text("After COMMIT, both tables have 4 rows. Sansa owns Needle (attack: 150).")
pdf.result_table(
    ["id", "name"],
    [["1", "Jaime"], ["2", "Jon Snow"], ["3", "Theon Greyjoy"], ["4", "Sansa Stark"]],
    col_widths=[30, 60],
)
pdf.result_table(
    ["id", "name", "attack", "owner_id"],
    [["1", "Oathkeeper", "200", "1"], ["2", "Wolf Bane", "214", "2"],
     ["3", "KrakenSlayer", "185", "3"], ["4", "Needle", "150", "4"]],
    col_widths=[20, 50, 30, 30],
)

output_path = "SQL_Exercises_For_Test_Automation_Engineers.pdf"
pdf.output(output_path)
print(f"PDF generated: {output_path}")
