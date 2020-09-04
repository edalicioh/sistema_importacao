from dao.Dao import Dao


class AddressDao(Dao):

    def insert(self, params):

        sql = """
            INSERT INTO addresses(
                street,
                number,
                observation,
                post_code,
                district_id ,
                city_id,
                state_id,
            ) VALUES (%s, %s,%s, %s,%s, %s,%s)
        """
        self.db.execute_query(sql, params)

    def get_cidy(self, name):
        sql = "SELECT id, city_name FROM cities WHERE city_name = %s"
        val = (name,)
        execute = self.db.execute_query(sql, val)
        return execute.fetchone()

    def get_district(self, name):
        sql = "SELECT id, district_name FROM districts WHERE district_name = %s"
        val = (name,)
        execute = self.db.execute_query(sql, val)
        return execute.fetchone()

    def get_state(self, name):
        sql = "SELECT id, state_name FROM states WHERE state_name = %s"
        val = (name,)
        execute = self.db.execute_query(sql, val)
        return execute.fetchone()
