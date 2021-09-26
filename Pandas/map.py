import pandas as pd

city_country = {
    "Karachi": "Pakistan",
    "Bangalore": "India",
    "Sydney": "Austrailia",
    "HongKong": "Thailand",
    "Jaddah": "Saudi Arabia",
}

to_frame = {
    "Name": ["Mubashir", "Hassan", "Jamshid", "Qaisar", "Zeeshan"],
    "City": ["Karachi", "Bangalore", "Sydney", "HongKong", "Jaddah"],
}

frame = pd.DataFrame(to_frame, index=[1, 2, 3, 4, 5])
frame['Country'] = frame["City"].map(city_country) #Create a new column in frame named Country
print(frame)