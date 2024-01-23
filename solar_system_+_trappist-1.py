from math import *
from PIL import Image
from vpython import *
import time

# Planets data: name, radius (proportional to real sizes), distance from the Sun (proportional to reality), angular velocity (proportional to reality)

planets = [
    {"name": "Sun", "radius": 1.7, "distance": 0, "angular_velocity": 0},
    {"name": "Mercury", "radius": 0.05*2, "distance": 2*2, "angular_velocity": 0},
    {"name": "Venus", "radius": 0.1*2, "distance": 4*2, "angular_velocity": 0},
    {"name": "Earth", "radius": 0.1*2, "distance": 6*2, "angular_velocity": 0},
    {"name": "Mars", "radius": 0.07*2, "distance": 8*2, "angular_velocity": 0},
    {"name": "Jupiter", "radius": 0.5*2, "distance": 12*2, "angular_velocity": 0},
    {"name": "Saturn", "radius": 0.4*2, "distance": 18*2, "angular_velocity": 0},
    {"name": "Uranus", "radius": 0.2*2, "distance": 25*2, "angular_velocity": 0},
    {"name": "Neptune", "radius": 0.2*2, "distance": 32*2, "angular_velocity": 0},
]

# Set up the camera
scene = canvas(title='Trappist, solar system model', width=1840, height=930, center=vector(0, 0, 0), background=color.white)

# Create and position planets
planet_objects = []

for planet in planets:
    if planet["name"] == "Sun":
        planet_objects.append(sphere(pos=vec(planet["distance"], 0, 0), radius=planet["radius"], color=color.yellow))
    elif planet['name'] == 'Earth':
        planet_objects.append(sphere(pos=vec(planet["distance"], 0, 0), radius=planet["radius"], texture=textures.earth))
    elif planet['name'] == 'Saturn':
        saturn_planet = sphere(pos=vec(planet["distance"], 0, 0), radius=planet["radius"], color=color.orange)
        saturn_ring = ring(pos=vec(planet["distance"], 0, 0), axis=vec(0, 0, 1), radius=1.25*planet["radius"], thickness=0.05*planet["radius"], color=color.yellow)
        saturn_compound = compound([saturn_planet, saturn_ring])
        planet_objects.append(saturn_compound)
    else:
        planet_objects.append(sphere(pos=vec(planet["distance"], 0, 0), radius=planet["radius"], color=color.black))

trappist_system = [
    {"name": "Center", "radius": 0.3*2, "distance": 0, "angular_velocity": 0},
    {"name": "b", "radius": 1.086*0.12, "distance": 1.111*2, "angular_velocity": 0},
    {"name": "c", "radius": 1.056*0.12, "distance": 1.522*2, "angular_velocity": 0},
    {"name": "d", "radius": 0.772*0.12, "distance": 2.145*2, "angular_velocity": 0},
    {"name": "e", "radius": 0.918*0.12, "distance": 2.818*2, "angular_velocity": 0},
    {"name": "f", "radius": 1.045*0.12, "distance": 3.71*2, "angular_velocity": 0},
    {"name": "g", "radius": 1.127*0.12, "distance": 4.51*2, "angular_velocity": 0},
    {"name": "h", "radius": 0.7150*0.12, "distance": 5.96*2, "angular_velocity": 0},
]

trappist_objects = []

for planet in trappist_system:
    if planet["name"] == "Center":
        trappist_objects.append(sphere(pos=vec(planet["distance"], 0, 24), radius=planet["radius"], color=color.blue))
    else:
        trappist_objects.append(sphere(pos=vec(planet["distance"], 0, 0), radius=planet["radius"], color=color.black))

trail_planets = []

for planet in planets[1:]:
    trail_planets.append(curve(color=color.black, radius=0.02))

trail_trappist = []

for planet in trappist_system[1:]:
    trail_trappist.append(curve(color=color.black, radius=0.02))

time.sleep(5)

# Simulation
while True:
    rate(60)  # frames per second
    for i, planet in enumerate(planets[1:]):  # The Sun doesn't move
        planet["angular_velocity"] += 0.03627454270114749 / sqrt(planet["distance"])
        angle = planet["angular_velocity"]
        x = planet["distance"] * cos(angle)
        y = planet["distance"] * sin(angle)
        planet_objects[i+1].pos = vec(x, y, 0)
        trail_planets[i].append(pos=planet_objects[i + 1].pos)

    for j, planet in enumerate(trappist_system[1:]):
        planet["angular_velocity"] += 0.015415233615516163 / sqrt(planet["distance"])
        angle2 = planet["angular_velocity"]
        x2 = planet["distance"] * cos(angle2)
        y2 = planet["distance"] * sin(angle2)
        trappist_objects[j+1].pos = vec(x2, y2, 24)
        trail_trappist[j].append(pos=trappist_objects[j + 1].pos)
