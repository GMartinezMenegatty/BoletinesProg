from calendar import month


class Data:
    def __init__(self, day, month, year):
        self.setAno(year)
        self.setMes(month)
        self.setDia(day)

    def setDia(self, day):
        diasmes = {
            1: 31,
            2: 28,
            3: 31,
            4: 30,
            5: 31,
            6: 30,
            7: 31,
            8: 31,
            9: 30,
            10: 31,
            11: 30,
            12: 31
        }

        if day > 0 and day <= diasmes[self.__month]:
                self.__day = day
        else:
                if self.__month == 2 and self.eBisiesto(self.__year):
                    if day==29:
                        self.__day = 29
                else:
                    self.__day = None
                    self.__month = None
                    self.__year = None

    def nombre_mes(self):
        match self.__month:
            case 1:
                return "Enero"
            case 2:
                return "Febrero"
            case 3:
                return "Marzo"
            case 4:
                return "Abril"
            case 5:
                return "Mayo"
            case 6:
                return "Junio"
            case 7:
                return "Julio"
            case 8:
                return "Agosto"
            case 9:
                return "Septiembre"
            case 10:
                return "Octubre"
            case 11:
                return "Noviembre"
            case 12:
                return "Diciembre"
            case _:
                return "Mes no válido"

    def getDia(self):
        return self.__day

    def setMes(self, month):
        if month > 0 and month < 13 and self.__year is not None:
            self.__month = month
        else:
            self.__month = None
            self.__day = None
            self.__year = None


    def getMes(self):
        return self.__month

    def setAno(self, year):
        if year >= 0:
            self.__year = year
        else:
            self.__year = None
            self.__month = None
            self.__day = None

    def getAno(self):
        return self.__year

    def eBisiesto(self, year):
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return True
        else:
            return False

    def __str__(self):
        return f"A data é {self.__day}/{self.__month}/{self.__year}"

    dia = property(getDia, setDia)
    mes = property(getMes, setMes)
    ano = property(getAno, setAno)


class Data2:
        def __init__(self, day,*mesAno):
            match day:
                case int(day):
                    if len(mesAno) == 2:
                        self.setAno(mesAno[1])
                        self.setMes(mesAno[0])
                        self.setDia(day)
                case str (day):
                    self.setDataStr(day)
                case [day, month, year]:
                    self.setAno(year)
                    self.setMes(month)
                    self.setDia(day)
                case {'dia': day, 'mes': month,'año': year}:
                    self.setAno(year)
                    self.setMes(month)
                    self.setDia(day)
                case Data (day, month, year):
                    self.setAno(year)
                    self.setMes(month)
                    self.setDia(day)
                case _:
                    self.setAno(year)
                    self.setMes(month)
                    self.setDia(day)

        def setDia(self, day):
            diasmes = {
                1: 31,
                2: 28,
                3: 31,
                4: 30,
                5: 31,
                6: 30,
                7: 31,
                8: 31,
                9: 30,
                10: 31,
                11: 30,
                12: 31
            }

            if day > 0 and day <= diasmes[self.__month]:
                self.__day = day
            else:
                if self.__month == 2 and self.eBisiesto(self.__year):
                    if day == 29:
                        self.__day = 29
                else:
                    self.__day = None
                    self.__month = None
                    self.__year = None

        def nombre_mes(self):
            match self.__month:
                case 1:
                    return "Enero"
                case 2:
                    return "Febrero"
                case 3:
                    return "Marzo"
                case 4:
                    return "Abril"
                case 5:
                    return "Mayo"
                case 6:
                    return "Junio"
                case 7:
                    return "Julio"
                case 8:
                    return "Agosto"
                case 9:
                    return "Septiembre"
                case 10:
                    return "Octubre"
                case 11:
                    return "Noviembre"
                case 12:
                    return "Diciembre"
                case _:
                    return "Mes no válido"

        def getDia(self):
            return self.__day

        def setMes(self, month):
            if month > 0 and month < 13 and self.__year is not None:
                self.__month = month
            else:
                self.__month = None
                self.__day = None
                self.__year = None

        def getMes(self):
            return self.__month

        def setAno(self, year):
            if year >= 0:
                self.__year = year
            else:
                self.__year = None
                self.__month = None
                self.__day = None

        def getAno(self):
            return self.__year

        def eBisiesto(self, year):
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                return True
            else:
                return False

        def __str__(self):
            return f"A data é {self.__day}/{self.__month}/{self.__year}"

        dia = property(getDia, setDia)
        mes = property(getMes, setMes)
        ano = property(getAno, setAno)
