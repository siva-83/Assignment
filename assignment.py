started_city="Kiev"
visited_cities=["Amsterdam","Kiev","Zurich","Prague","Berlin","Barcelona"]
tickets=["Paris=Skopje", "Zurich-Amsterdam", "Prague-Zurich", "Barcelona-Berlin","Kiev-Prague", "Skopje-Paris",
"Amsterdam-Barcelona", "Berlin-Kiev", "Berlin-Barcelona"]

routes = []

visited_count = 0

while visited_count!=len(visited_cities):
    for ticket in tickets:
        temp = ticket.split("-")
        if temp[0] == started_city:
            routes.append(started_city)
            started_city = temp[1]
            visited_count+=1
            tickets.remove(ticket)
            break
print(routes)