#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def set_tickets(tickets):
    tics = {}
    for ticket in tickets:
        tics[ticket.source] = ticket.destination

    return tics


def reconstruct_trip(tickets, length):
    tics = set_tickets(tickets)

    next = tics["NONE"]
    done = False
    route = []
    route.append(next)
    while done is not True:
        if tics[next] == "NONE":
            done = True

        route.append(tics[next])
        next = tics[next]

    return route
