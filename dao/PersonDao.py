from dao.Dao import Dao


class PersonDao(Dao):

    def find_all(self):
        sql = "SELECT person_name,gender FROM people where person_name = %s"
        var = ("Edalicio",)
        find = self.db.execute_query(sql, var)

        return find.fetchall()

    def insert(self, params):
        sql = """
            INSERT INTO people ( 
                person_name,
                gender,
                cpf,
                sus_id,
                birth_date,
                age,
                phone,
                work_status,
                patient,
                person_status,
                first_medical_care,
                address_id,
                user_id,
                company_id,
                contaminations_id,
                hospital_id,
                date_death,
                excluded
            ) VALUES (%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s)
        """

        self.db.execute_query(sql, params)
        self.db.conn.commit()
        return self.find_all()
