import calendar


class NationalPark:
    all = []

    def __init__(self, name):
        self.name = name
        type(self).all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not hasattr(self, "name"):
            if not isinstance(value, str) or not 3 <= len(value):
                raise ValueError("Name must be a string")
            else:
                self._name = value
        else:
            raise AttributeError("Cannot change the name once it is set")

    def trips(self):
        return [trip for trip in Trip.all if trip.national_park == self]

    def visitors(self):
        return list(set([trip.visitor for trip in Trip.all if trip.national_park == self]))

    def total_visits(self):
        # returns the number of times park has been visited
        visits = [trip for trip in Trip.all if trip.national_park == self]
        return len(visits)

    def best_visitor(self):
        # Returns the visitor instance that visited the park the most
        visits = [trip.visitor for trip in Trip.all if trip.national_park == self]
        # returns the highest count
        best_visitor = max(visits, key=lambda x: visits.count(x))
        return best_visitor


class Trip:

    all = []

    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        type(self).all.append(self)

    @property
    def visitor(self):
        return self._visitor

    @visitor.setter
    def visitor(self, value):
        if not isinstance(value, Visitor):
            raise ValueError("Visitor must be of type Visitor")
        else:
            self._visitor = value

    @property
    def national_park(self):
        return self._national_park

    @national_park.setter
    def national_park(self, value):
        if not isinstance(value, NationalPark):
            raise ValueError("National Park must be of type NationalPark")
        else:
            self._national_park = value

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        # Is in the format "September 1st" =>  length must be greater or equal to 7 characters
        if not isinstance(value, str) or not len(value) >= 7:
            raise ValueError("Start date must be a string")
        else:
            # Split the value into month and day
            month, day = value.split(' ')
            # Get the month number from the month name
            month_num = list(calendar.month_name).index(month)
            # Convert the day to integer
            day_num = int(day.rstrip('st').rstrip(
                'nd').rstrip('rd').rstrip('th'))
            # Format the date as "September 1st"
            formatted_date = f"{month} {day_num}{'st' if day.endswith('st') else 'nd' if day.endswith('nd') else 'rd' if day.endswith('rd') else 'th'}"
            self._start_date = formatted_date

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        # Is in the format "September 1st" =>  length must be greater or equal to 7 characters
        if not isinstance(value, str) or not len(value) >= 7:
            raise ValueError("End date must be a string")
        else:
            # Split the value into month and day
            month, day = value.split(' ')
            # Get the month number from the month name
            month_num = list(calendar.month_name).index(month)
            # Convert the day to integer
            day_num = int(day.rstrip('st').rstrip(
                'nd').rstrip('rd').rstrip('th'))
            # Format the date as "September 1st"
            formatted_date = f"{month} {day_num}{'st' if day.endswith('st') else 'nd' if day.endswith('nd') else 'rd' if day.endswith('rd') else 'th'}"
            self._end_date = formatted_date


class Visitor:

    all = []

    def __init__(self, name):
        self.name = name
        type(self).all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not 1 <= len(value) <= 15:
            raise ValueError("Name must be a string")
        else:
            self._name = value

    def trips(self):
        return [trip for trip in Trip.all if trip.visitor == self]

    def national_parks(self):
        # Returns a unique list of all parks that visitor has visited
        return list(set([trip.national_park for trip in Trip.all if trip.visitor == self]))

    def total_visits_at_park(self, park):
        # Returns the number of times visitor has visited park
        visits = [trip for trip in Trip.all if trip.visitor ==
                  self and trip.national_park == park]
        return len(visits)


# np = NationalPark("under the sea")
# breakpoint()
