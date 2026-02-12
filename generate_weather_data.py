import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Define realistic monthly weather patterns for each city
city_weather_patterns = {
    # EXTREME COLD - Himalayan/Hill Stations
    'Leh': {
        'Jan': {'temp_min': -15, 'temp_max': -5, 'humidity': 40, 'rainfall': 10, 'wind': 15, 'conditions': ['Clear', 'Cloudy', 'Snow']},
        'Feb': {'temp_min': -12, 'temp_max': -2, 'humidity': 42, 'rainfall': 12, 'wind': 15, 'conditions': ['Clear', 'Cloudy', 'Snow']},
        'Mar': {'temp_min': -5, 'temp_max': 5, 'humidity': 45, 'rainfall': 15, 'wind': 18, 'conditions': ['Clear', 'Cloudy', 'Snow']},
        'Apr': {'temp_min': 0, 'temp_max': 10, 'humidity': 40, 'rainfall': 10, 'wind': 20, 'conditions': ['Clear', 'Cloudy', 'Partly Cloudy']},
        'May': {'temp_min': 5, 'temp_max': 18, 'humidity': 35, 'rainfall': 8, 'wind': 18, 'conditions': ['Clear', 'Sunny', 'Partly Cloudy']},
        'Jun': {'temp_min': 10, 'temp_max': 25, 'humidity': 30, 'rainfall': 5, 'wind': 15, 'conditions': ['Sunny', 'Clear', 'Partly Cloudy']},
        'Jul': {'temp_min': 12, 'temp_max': 28, 'humidity': 35, 'rainfall': 10, 'wind': 12, 'conditions': ['Sunny', 'Clear', 'Partly Cloudy']},
        'Aug': {'temp_min': 10, 'temp_max': 26, 'humidity': 38, 'rainfall': 12, 'wind': 12, 'conditions': ['Sunny', 'Partly Cloudy', 'Clear']},
        'Sep': {'temp_min': 5, 'temp_max': 20, 'humidity': 40, 'rainfall': 8, 'wind': 10, 'conditions': ['Clear', 'Sunny', 'Partly Cloudy']},
        'Oct': {'temp_min': -2, 'temp_max': 12, 'humidity': 42, 'rainfall': 5, 'wind': 12, 'conditions': ['Clear', 'Partly Cloudy', 'Cloudy']},
        'Nov': {'temp_min': -8, 'temp_max': 3, 'humidity': 45, 'rainfall': 8, 'wind': 15, 'conditions': ['Cloudy', 'Clear', 'Snow']},
        'Dec': {'temp_min': -13, 'temp_max': -3, 'humidity': 48, 'rainfall': 10, 'wind': 15, 'conditions': ['Snow', 'Cloudy', 'Clear']}
    },
    
    'Shimla': {
        'Jan': {'temp_min': 0, 'temp_max': 9, 'humidity': 65, 'rainfall': 60, 'wind': 12, 'conditions': ['Cloudy', 'Snow', 'Foggy']},
        'Feb': {'temp_min': 2, 'temp_max': 11, 'humidity': 60, 'rainfall': 65, 'wind': 12, 'conditions': ['Cloudy', 'Rainy', 'Snow']},
        'Mar': {'temp_min': 6, 'temp_max': 16, 'humidity': 55, 'rainfall': 70, 'wind': 10, 'conditions': ['Cloudy', 'Rainy', 'Partly Cloudy']},
        'Apr': {'temp_min': 10, 'temp_max': 20, 'humidity': 50, 'rainfall': 55, 'wind': 8, 'conditions': ['Partly Cloudy', 'Cloudy', 'Clear']},
        'May': {'temp_min': 14, 'temp_max': 24, 'humidity': 52, 'rainfall': 60, 'wind': 8, 'conditions': ['Partly Cloudy', 'Cloudy', 'Rainy']},
        'Jun': {'temp_min': 16, 'temp_max': 26, 'humidity': 65, 'rainfall': 150, 'wind': 10, 'conditions': ['Rainy', 'Cloudy', 'Heavy Rain']},
        'Jul': {'temp_min': 16, 'temp_max': 24, 'humidity': 75, 'rainfall': 280, 'wind': 12, 'conditions': ['Heavy Rain', 'Rainy', 'Cloudy']},
        'Aug': {'temp_min': 15, 'temp_max': 23, 'humidity': 78, 'rainfall': 300, 'wind': 12, 'conditions': ['Heavy Rain', 'Rainy', 'Cloudy']},
        'Sep': {'temp_min': 13, 'temp_max': 21, 'humidity': 70, 'rainfall': 150, 'wind': 10, 'conditions': ['Rainy', 'Cloudy', 'Partly Cloudy']},
        'Oct': {'temp_min': 9, 'temp_max': 18, 'humidity': 60, 'rainfall': 40, 'wind': 8, 'conditions': ['Partly Cloudy', 'Clear', 'Cloudy']},
        'Nov': {'temp_min': 5, 'temp_max': 14, 'humidity': 62, 'rainfall': 25, 'wind': 10, 'conditions': ['Clear', 'Partly Cloudy', 'Cloudy']},
        'Dec': {'temp_min': 2, 'temp_max': 10, 'humidity': 68, 'rainfall': 35, 'wind': 12, 'conditions': ['Cloudy', 'Snow', 'Foggy']}
    },
    
    'Srinagar': {
        'Jan': {'temp_min': -2, 'temp_max': 7, 'humidity': 75, 'rainfall': 80, 'wind': 8, 'conditions': ['Snow', 'Cloudy', 'Foggy']},
        'Feb': {'temp_min': 0, 'temp_max': 10, 'humidity': 70, 'rainfall': 90, 'wind': 8, 'conditions': ['Snow', 'Rainy', 'Cloudy']},
        'Mar': {'temp_min': 4, 'temp_max': 16, 'humidity': 65, 'rainfall': 110, 'wind': 10, 'conditions': ['Rainy', 'Cloudy', 'Partly Cloudy']},
        'Apr': {'temp_min': 8, 'temp_max': 21, 'humidity': 60, 'rainfall': 95, 'wind': 10, 'conditions': ['Rainy', 'Partly Cloudy', 'Clear']},
        'May': {'temp_min': 12, 'temp_max': 26, 'humidity': 55, 'rainfall': 65, 'wind': 8, 'conditions': ['Partly Cloudy', 'Clear', 'Cloudy']},
        'Jun': {'temp_min': 16, 'temp_max': 30, 'humidity': 55, 'rainfall': 45, 'wind': 8, 'conditions': ['Partly Cloudy', 'Clear', 'Sunny']},
        'Jul': {'temp_min': 19, 'temp_max': 32, 'humidity': 60, 'rainfall': 60, 'wind': 8, 'conditions': ['Partly Cloudy', 'Rainy', 'Clear']},
        'Aug': {'temp_min': 18, 'temp_max': 31, 'humidity': 62, 'rainfall': 65, 'wind': 8, 'conditions': ['Rainy', 'Partly Cloudy', 'Cloudy']},
        'Sep': {'temp_min': 14, 'temp_max': 28, 'humidity': 60, 'rainfall': 40, 'wind': 6, 'conditions': ['Partly Cloudy', 'Clear', 'Cloudy']},
        'Oct': {'temp_min': 8, 'temp_max': 23, 'humidity': 62, 'rainfall': 35, 'wind': 6, 'conditions': ['Clear', 'Partly Cloudy', 'Cloudy']},
        'Nov': {'temp_min': 2, 'temp_max': 16, 'humidity': 68, 'rainfall': 40, 'wind': 6, 'conditions': ['Cloudy', 'Foggy', 'Clear']},
        'Dec': {'temp_min': -1, 'temp_max': 9, 'humidity': 75, 'rainfall': 60, 'wind': 8, 'conditions': ['Snow', 'Cloudy', 'Foggy']}
    },
    
    'Darjeeling': {
        'Jan': {'temp_min': 2, 'temp_max': 10, 'humidity': 70, 'rainfall': 15, 'wind': 8, 'conditions': ['Foggy', 'Cloudy', 'Clear']},
        'Feb': {'temp_min': 3, 'temp_max': 11, 'humidity': 68, 'rainfall': 20, 'wind': 8, 'conditions': ['Foggy', 'Cloudy', 'Partly Cloudy']},
        'Mar': {'temp_min': 7, 'temp_max': 16, 'humidity': 65, 'rainfall': 35, 'wind': 10, 'conditions': ['Cloudy', 'Rainy', 'Foggy']},
        'Apr': {'temp_min': 10, 'temp_max': 19, 'humidity': 70, 'rainfall': 85, 'wind': 10, 'conditions': ['Rainy', 'Cloudy', 'Foggy']},
        'May': {'temp_min': 13, 'temp_max': 19, 'humidity': 78, 'rainfall': 180, 'wind': 12, 'conditions': ['Heavy Rain', 'Rainy', 'Cloudy']},
        'Jun': {'temp_min': 14, 'temp_max': 19, 'humidity': 85, 'rainfall': 550, 'wind': 15, 'conditions': ['Heavy Rain', 'Rainy', 'Cloudy']},
        'Jul': {'temp_min': 15, 'temp_max': 19, 'humidity': 88, 'rainfall': 800, 'wind': 15, 'conditions': ['Heavy Rain', 'Rainy', 'Cloudy']},
        'Aug': {'temp_min': 15, 'temp_max': 19, 'humidity': 88, 'rainfall': 650, 'wind': 15, 'conditions': ['Heavy Rain', 'Rainy', 'Cloudy']},
        'Sep': {'temp_min': 14, 'temp_max': 18, 'humidity': 85, 'rainfall': 400, 'wind': 12, 'conditions': ['Rainy', 'Heavy Rain', 'Cloudy']},
        'Oct': {'temp_min': 11, 'temp_max': 17, 'humidity': 78, 'rainfall': 110, 'wind': 10, 'conditions': ['Rainy', 'Cloudy', 'Partly Cloudy']},
        'Nov': {'temp_min': 7, 'temp_max': 14, 'humidity': 72, 'rainfall': 20, 'wind': 8, 'conditions': ['Cloudy', 'Foggy', 'Clear']},
        'Dec': {'temp_min': 4, 'temp_max': 11, 'humidity': 72, 'rainfall': 10, 'wind': 8, 'conditions': ['Foggy', 'Cloudy', 'Clear']}
    },
    
    # EXTREME HOT - Desert/Semi-Arid
    'Jaisalmer': {
        'Jan': {'temp_min': 7, 'temp_max': 24, 'humidity': 45, 'rainfall': 5, 'wind': 12, 'conditions': ['Clear', 'Sunny', 'Partly Cloudy']},
        'Feb': {'temp_min': 10, 'temp_max': 27, 'humidity': 40, 'rainfall': 3, 'wind': 12, 'conditions': ['Sunny', 'Clear', 'Partly Cloudy']},
        'Mar': {'temp_min': 16, 'temp_max': 33, 'humidity': 35, 'rainfall': 2, 'wind': 15, 'conditions': ['Sunny', 'Hot', 'Clear']},
        'Apr': {'temp_min': 22, 'temp_max': 39, 'humidity': 28, 'rainfall': 1, 'wind': 18, 'conditions': ['Hot', 'Sunny', 'Clear']},
        'May': {'temp_min': 27, 'temp_max': 43, 'humidity': 25, 'rainfall': 5, 'wind': 20, 'conditions': ['Very Hot', 'Hot', 'Sunny']},
        'Jun': {'temp_min': 29, 'temp_max': 42, 'humidity': 35, 'rainfall': 12, 'wind': 25, 'conditions': ['Very Hot', 'Hot', 'Dusty']},
        'Jul': {'temp_min': 28, 'temp_max': 39, 'humidity': 55, 'rainfall': 65, 'wind': 22, 'conditions': ['Hot', 'Rainy', 'Cloudy']},
        'Aug': {'temp_min': 26, 'temp_max': 37, 'humidity': 60, 'rainfall': 85, 'wind': 20, 'conditions': ['Rainy', 'Hot', 'Cloudy']},
        'Sep': {'temp_min': 24, 'temp_max': 37, 'humidity': 50, 'rainfall': 25, 'wind': 18, 'conditions': ['Hot', 'Partly Cloudy', 'Sunny']},
        'Oct': {'temp_min': 19, 'temp_max': 35, 'humidity': 42, 'rainfall': 5, 'wind': 15, 'conditions': ['Sunny', 'Clear', 'Hot']},
        'Nov': {'temp_min': 13, 'temp_max': 30, 'humidity': 45, 'rainfall': 2, 'wind': 12, 'conditions': ['Clear', 'Sunny', 'Partly Cloudy']},
        'Dec': {'temp_min': 9, 'temp_max': 26, 'humidity': 48, 'rainfall': 3, 'wind': 12, 'conditions': ['Clear', 'Sunny', 'Partly Cloudy']}
    },
    
    'Bikaner': {
        'Jan': {'temp_min': 8, 'temp_max': 23, 'humidity': 50, 'rainfall': 8, 'wind': 10, 'conditions': ['Clear', 'Sunny', 'Partly Cloudy']},
        'Feb': {'temp_min': 11, 'temp_max': 26, 'humidity': 45, 'rainfall': 5, 'wind': 12, 'conditions': ['Sunny', 'Clear', 'Partly Cloudy']},
        'Mar': {'temp_min': 17, 'temp_max': 32, 'humidity': 38, 'rainfall': 3, 'wind': 15, 'conditions': ['Sunny', 'Hot', 'Clear']},
        'Apr': {'temp_min': 23, 'temp_max': 39, 'humidity': 30, 'rainfall': 2, 'wind': 18, 'conditions': ['Hot', 'Very Hot', 'Sunny']},
        'May': {'temp_min': 28, 'temp_max': 43, 'humidity': 28, 'rainfall': 8, 'wind': 22, 'conditions': ['Very Hot', 'Hot', 'Sunny']},
        'Jun': {'temp_min': 30, 'temp_max': 42, 'humidity': 38, 'rainfall': 25, 'wind': 25, 'conditions': ['Very Hot', 'Hot', 'Dusty']},
        'Jul': {'temp_min': 28, 'temp_max': 38, 'humidity': 60, 'rainfall': 110, 'wind': 22, 'conditions': ['Rainy', 'Hot', 'Cloudy']},
        'Aug': {'temp_min': 26, 'temp_max': 36, 'humidity': 68, 'rainfall': 130, 'wind': 20, 'conditions': ['Rainy', 'Cloudy', 'Hot']},
        'Sep': {'temp_min': 24, 'temp_max': 36, 'humidity': 55, 'rainfall': 40, 'wind': 15, 'conditions': ['Hot', 'Partly Cloudy', 'Rainy']},
        'Oct': {'temp_min': 20, 'temp_max': 34, 'humidity': 48, 'rainfall': 8, 'wind': 12, 'conditions': ['Sunny', 'Clear', 'Hot']},
        'Nov': {'temp_min': 14, 'temp_max': 29, 'humidity': 50, 'rainfall': 3, 'wind': 10, 'conditions': ['Clear', 'Sunny', 'Partly Cloudy']},
        'Dec': {'temp_min': 10, 'temp_max': 25, 'humidity': 52, 'rainfall': 5, 'wind': 10, 'conditions': ['Clear', 'Sunny', 'Partly Cloudy']}
    },
    
    'Jodhpur': {
        'Jan': {'temp_min': 9, 'temp_max': 24, 'humidity': 48, 'rainfall': 5, 'wind': 10, 'conditions': ['Clear', 'Sunny', 'Partly Cloudy']},
        'Feb': {'temp_min': 12, 'temp_max': 27, 'humidity': 42, 'rainfall': 3, 'wind': 12, 'conditions': ['Sunny', 'Clear', 'Partly Cloudy']},
        'Mar': {'temp_min': 17, 'temp_max': 33, 'humidity': 35, 'rainfall': 2, 'wind': 15, 'conditions': ['Sunny', 'Hot', 'Clear']},
        'Apr': {'temp_min': 23, 'temp_max': 38, 'humidity': 28, 'rainfall': 1, 'wind': 18, 'conditions': ['Hot', 'Very Hot', 'Sunny']},
        'May': {'temp_min': 27, 'temp_max': 41, 'humidity': 28, 'rainfall': 10, 'wind': 20, 'conditions': ['Very Hot', 'Hot', 'Sunny']},
        'Jun': {'temp_min': 29, 'temp_max': 40, 'humidity': 40, 'rainfall': 35, 'wind': 25, 'conditions': ['Very Hot', 'Hot', 'Partly Cloudy']},
        'Jul': {'temp_min': 27, 'temp_max': 36, 'humidity': 62, 'rainfall': 120, 'wind': 22, 'conditions': ['Rainy', 'Hot', 'Cloudy']},
        'Aug': {'temp_min': 25, 'temp_max': 34, 'humidity': 70, 'rainfall': 140, 'wind': 20, 'conditions': ['Rainy', 'Cloudy', 'Hot']},
        'Sep': {'temp_min': 24, 'temp_max': 35, 'humidity': 58, 'rainfall': 50, 'wind': 15, 'conditions': ['Hot', 'Rainy', 'Partly Cloudy']},
        'Oct': {'temp_min': 20, 'temp_max': 34, 'humidity': 45, 'rainfall': 5, 'wind': 12, 'conditions': ['Sunny', 'Clear', 'Hot']},
        'Nov': {'temp_min': 14, 'temp_max': 29, 'humidity': 46, 'rainfall': 2, 'wind': 10, 'conditions': ['Clear', 'Sunny', 'Partly Cloudy']},
        'Dec': {'temp_min': 10, 'temp_max': 25, 'humidity': 48, 'rainfall': 3, 'wind': 10, 'conditions': ['Clear', 'Sunny', 'Partly Cloudy']}
    },
    
    # HOT & HUMID - Coastal/Tropical
    'Chennai': {
        'Jan': {'temp_min': 20, 'temp_max': 29, 'humidity': 72, 'rainfall': 25, 'wind': 15, 'conditions': ['Partly Cloudy', 'Clear', 'Cloudy']},
        'Feb': {'temp_min': 21, 'temp_max': 31, 'humidity': 70, 'rainfall': 10, 'wind': 15, 'conditions': ['Sunny', 'Hot', 'Partly Cloudy']},
        'Mar': {'temp_min': 23, 'temp_max': 33, 'humidity': 68, 'rainfall': 15, 'wind': 18, 'conditions': ['Hot', 'Humid', 'Partly Cloudy']},
        'Apr': {'temp_min': 26, 'temp_max': 36, 'humidity': 65, 'rainfall': 20, 'wind': 18, 'conditions': ['Hot', 'Humid', 'Partly Cloudy']},
        'May': {'temp_min': 28, 'temp_max': 38, 'humidity': 65, 'rainfall': 50, 'wind': 20, 'conditions': ['Very Hot', 'Humid', 'Rainy']},
        'Jun': {'temp_min': 27, 'temp_max': 37, 'humidity': 68, 'rainfall': 55, 'wind': 25, 'conditions': ['Hot', 'Humid', 'Rainy']},
        'Jul': {'temp_min': 26, 'temp_max': 35, 'humidity': 72, 'rainfall': 85, 'wind': 25, 'conditions': ['Rainy', 'Humid', 'Cloudy']},
        'Aug': {'temp_min': 26, 'temp_max': 35, 'humidity': 72, 'rainfall': 120, 'wind': 25, 'conditions': ['Rainy', 'Humid', 'Cloudy']},
        'Sep': {'temp_min': 25, 'temp_max': 34, 'humidity': 72, 'rainfall': 120, 'wind': 20, 'conditions': ['Rainy', 'Humid', 'Cloudy']},
        'Oct': {'temp_min': 24, 'temp_max': 32, 'humidity': 75, 'rainfall': 280, 'wind': 18, 'conditions': ['Heavy Rain', 'Rainy', 'Cloudy']},
        'Nov': {'temp_min': 23, 'temp_max': 30, 'humidity': 78, 'rainfall': 350, 'wind': 15, 'conditions': ['Heavy Rain', 'Rainy', 'Cloudy']},
        'Dec': {'temp_min': 21, 'temp_max': 29, 'humidity': 75, 'rainfall': 140, 'wind': 15, 'conditions': ['Rainy', 'Cloudy', 'Partly Cloudy']}
    },
    
    'Mumbai': {
        'Jan': {'temp_min': 17, 'temp_max': 31, 'humidity': 62, 'rainfall': 1, 'wind': 12, 'conditions': ['Clear', 'Sunny', 'Partly Cloudy']},
        'Feb': {'temp_min': 18, 'temp_max': 32, 'humidity': 60, 'rainfall': 0, 'wind': 12, 'conditions': ['Sunny', 'Clear', 'Hot']},
        'Mar': {'temp_min': 21, 'temp_max': 33, 'humidity': 65, 'rainfall': 0, 'wind': 15, 'conditions': ['Hot', 'Humid', 'Sunny']},
        'Apr': {'temp_min': 24, 'temp_max': 34, 'humidity': 68, 'rainfall': 1, 'wind': 15, 'conditions': ['Hot', 'Humid', 'Partly Cloudy']},
        'May': {'temp_min': 26, 'temp_max': 34, 'humidity': 72, 'rainfall': 20, 'wind': 18, 'conditions': ['Hot', 'Humid', 'Partly Cloudy']},
        'Jun': {'temp_min': 26, 'temp_max': 32, 'humidity': 80, 'rainfall': 585, 'wind': 25, 'conditions': ['Heavy Rain', 'Rainy', 'Cloudy']},
        'Jul': {'temp_min': 25, 'temp_max': 30, 'humidity': 85, 'rainfall': 840, 'wind': 28, 'conditions': ['Heavy Rain', 'Rainy', 'Cloudy']},
        'Aug': {'temp_min': 25, 'temp_max': 30, 'humidity': 85, 'rainfall': 540, 'wind': 25, 'conditions': ['Heavy Rain', 'Rainy', 'Cloudy']},
        'Sep': {'temp_min': 24, 'temp_max': 31, 'humidity': 80, 'rainfall': 265, 'wind': 20, 'conditions': ['Rainy', 'Cloudy', 'Humid']},
        'Oct': {'temp_min': 23, 'temp_max': 33, 'humidity': 72, 'rainfall': 65, 'wind': 15, 'conditions': ['Rainy', 'Partly Cloudy', 'Humid']},
        'Nov': {'temp_min': 21, 'temp_max': 33, 'humidity': 65, 'rainfall': 15, 'wind': 12, 'conditions': ['Partly Cloudy', 'Clear', 'Humid']},
        'Dec': {'temp_min': 18, 'temp_max': 32, 'humidity': 62, 'rainfall': 3, 'wind': 12, 'conditions': ['Clear', 'Sunny', 'Partly Cloudy']}
    },
    
    'Kochi': {
        'Jan': {'temp_min': 23, 'temp_max': 31, 'humidity': 75, 'rainfall': 20, 'wind': 12, 'conditions': ['Partly Cloudy', 'Clear', 'Humid']},
        'Feb': {'temp_min': 24, 'temp_max': 32, 'humidity': 72, 'rainfall': 25, 'wind': 12, 'conditions': ['Partly Cloudy', 'Humid', 'Clear']},
        'Mar': {'temp_min': 25, 'temp_max': 33, 'humidity': 72, 'rainfall': 70, 'wind': 12, 'conditions': ['Humid', 'Rainy', 'Partly Cloudy']},
        'Apr': {'temp_min': 26, 'temp_max': 33, 'humidity': 75, 'rainfall': 125, 'wind': 15, 'conditions': ['Rainy', 'Humid', 'Cloudy']},
        'May': {'temp_min': 26, 'temp_max': 32, 'humidity': 78, 'rainfall': 310, 'wind': 15, 'conditions': ['Heavy Rain', 'Rainy', 'Cloudy']},
        'Jun': {'temp_min': 25, 'temp_max': 30, 'humidity': 85, 'rainfall': 660, 'wind': 20, 'conditions': ['Heavy Rain', 'Rainy', 'Cloudy']},
        'Jul': {'temp_min': 24, 'temp_max': 29, 'humidity': 85, 'rainfall': 575, 'wind': 20, 'conditions': ['Heavy Rain', 'Rainy', 'Cloudy']},
        'Aug': {'temp_min': 24, 'temp_max': 29, 'humidity': 85, 'rainfall': 390, 'wind': 18, 'conditions': ['Heavy Rain', 'Rainy', 'Cloudy']},
        'Sep': {'temp_min': 24, 'temp_max': 30, 'humidity': 80, 'rainfall': 210, 'wind': 15, 'conditions': ['Rainy', 'Humid', 'Cloudy']},
        'Oct': {'temp_min': 24, 'temp_max': 30, 'humidity': 80, 'rainfall': 345, 'wind': 12, 'conditions': ['Heavy Rain', 'Rainy', 'Cloudy']},
        'Nov': {'temp_min': 24, 'temp_max': 31, 'humidity': 78, 'rainfall': 160, 'wind': 12, 'conditions': ['Rainy', 'Humid', 'Cloudy']},
        'Dec': {'temp_min': 23, 'temp_max': 31, 'humidity': 75, 'rainfall': 45, 'wind': 12, 'conditions': ['Partly Cloudy', 'Humid', 'Rainy']}
    },
    
    # MODERATE/VARIED CLIMATE
    'Bangalore': {
        'Jan': {'temp_min': 15, 'temp_max': 27, 'humidity': 60, 'rainfall': 5, 'wind': 10, 'conditions': ['Clear', 'Pleasant', 'Partly Cloudy']},
        'Feb': {'temp_min': 16, 'temp_max': 30, 'humidity': 55, 'rainfall': 10, 'wind': 10, 'conditions': ['Pleasant', 'Clear', 'Partly Cloudy']},
        'Mar': {'temp_min': 19, 'temp_max': 33, 'humidity': 50, 'rainfall': 15, 'wind': 12, 'conditions': ['Warm', 'Pleasant', 'Partly Cloudy']},
        'Apr': {'temp_min': 21, 'temp_max': 34, 'humidity': 52, 'rainfall': 55, 'wind': 12, 'conditions': ['Warm', 'Rainy', 'Partly Cloudy']},
        'May': {'temp_min': 21, 'temp_max': 33, 'humidity': 58, 'rainfall': 115, 'wind': 15, 'conditions': ['Rainy', 'Pleasant', 'Cloudy']},
        'Jun': {'temp_min': 20, 'temp_max': 29, 'humidity': 68, 'rainfall': 90, 'wind': 15, 'conditions': ['Rainy', 'Cloudy', 'Pleasant']},
        'Jul': {'temp_min': 20, 'temp_max': 28, 'humidity': 70, 'rainfall': 105, 'wind': 15, 'conditions': ['Rainy', 'Cloudy', 'Pleasant']},
        'Aug': {'temp_min': 19, 'temp_max': 28, 'humidity': 70, 'rainfall': 140, 'wind': 15, 'conditions': ['Rainy', 'Cloudy', 'Pleasant']},
        'Sep': {'temp_min': 19, 'temp_max': 28, 'humidity': 68, 'rainfall': 175, 'wind': 12, 'conditions': ['Rainy', 'Pleasant', 'Cloudy']},
        'Oct': {'temp_min': 19, 'temp_max': 28, 'humidity': 70, 'rainfall': 180, 'wind': 10, 'conditions': ['Rainy', 'Pleasant', 'Cloudy']},
        'Nov': {'temp_min': 17, 'temp_max': 27, 'humidity': 68, 'rainfall': 60, 'wind': 10, 'conditions': ['Pleasant', 'Rainy', 'Partly Cloudy']},
        'Dec': {'temp_min': 16, 'temp_max': 27, 'humidity': 62, 'rainfall': 15, 'wind': 10, 'conditions': ['Pleasant', 'Clear', 'Partly Cloudy']}
    },
    
    'Delhi': {
        'Jan': {'temp_min': 7, 'temp_max': 21, 'humidity': 65, 'rainfall': 20, 'wind': 8, 'conditions': ['Foggy', 'Clear', 'Cloudy']},
        'Feb': {'temp_min': 10, 'temp_max': 24, 'humidity': 60, 'rainfall': 25, 'wind': 10, 'conditions': ['Clear', 'Partly Cloudy', 'Pleasant']},
        'Mar': {'temp_min': 15, 'temp_max': 30, 'humidity': 52, 'rainfall': 18, 'wind': 12, 'conditions': ['Pleasant', 'Warm', 'Partly Cloudy']},
        'Apr': {'temp_min': 21, 'temp_max': 36, 'humidity': 42, 'rainfall': 10, 'wind': 15, 'conditions': ['Hot', 'Warm', 'Clear']},
        'May': {'temp_min': 26, 'temp_max': 40, 'humidity': 40, 'rainfall': 20, 'wind': 18, 'conditions': ['Very Hot', 'Hot', 'Dusty']},
        'Jun': {'temp_min': 28, 'temp_max': 40, 'humidity': 48, 'rainfall': 65, 'wind': 20, 'conditions': ['Very Hot', 'Hot', 'Dusty']},
        'Jul': {'temp_min': 27, 'temp_max': 35, 'humidity': 70, 'rainfall': 210, 'wind': 18, 'conditions': ['Rainy', 'Humid', 'Cloudy']},
        'Aug': {'temp_min': 26, 'temp_max': 34, 'humidity': 75, 'rainfall': 250, 'wind': 15, 'conditions': ['Rainy', 'Humid', 'Cloudy']},
        'Sep': {'temp_min': 24, 'temp_max': 34, 'humidity': 68, 'rainfall': 125, 'wind': 12, 'conditions': ['Rainy', 'Humid', 'Partly Cloudy']},
        'Oct': {'temp_min': 19, 'temp_max': 33, 'humidity': 58, 'rainfall': 30, 'wind': 10, 'conditions': ['Pleasant', 'Clear', 'Partly Cloudy']},
        'Nov': {'temp_min': 12, 'temp_max': 28, 'humidity': 62, 'rainfall': 5, 'wind': 8, 'conditions': ['Pleasant', 'Clear', 'Partly Cloudy']},
        'Dec': {'temp_min': 8, 'temp_max': 23, 'humidity': 68, 'rainfall': 10, 'wind': 8, 'conditions': ['Foggy', 'Clear', 'Cloudy']}
    },
    
    'Kolkata': {
        'Jan': {'temp_min': 14, 'temp_max': 27, 'humidity': 68, 'rainfall': 10, 'wind': 8, 'conditions': ['Clear', 'Pleasant', 'Partly Cloudy']},
        'Feb': {'temp_min': 17, 'temp_max': 29, 'humidity': 62, 'rainfall': 25, 'wind': 10, 'conditions': ['Pleasant', 'Clear', 'Warm']},
        'Mar': {'temp_min': 21, 'temp_max': 34, 'humidity': 60, 'rainfall': 30, 'wind': 12, 'conditions': ['Warm', 'Hot', 'Partly Cloudy']},
        'Apr': {'temp_min': 25, 'temp_max': 36, 'humidity': 65, 'rainfall': 50, 'wind': 15, 'conditions': ['Hot', 'Humid', 'Rainy']},
        'May': {'temp_min': 26, 'temp_max': 36, 'humidity': 70, 'rainfall': 140, 'wind': 18, 'conditions': ['Hot', 'Humid', 'Rainy']},
        'Jun': {'temp_min': 27, 'temp_max': 35, 'humidity': 78, 'rainfall': 280, 'wind': 18, 'conditions': ['Rainy', 'Humid', 'Cloudy']},
        'Jul': {'temp_min': 27, 'temp_max': 33, 'humidity': 82, 'rainfall': 325, 'wind': 18, 'conditions': ['Heavy Rain', 'Rainy', 'Humid']},
        'Aug': {'temp_min': 27, 'temp_max': 33, 'humidity': 82, 'rainfall': 305, 'wind': 18, 'conditions': ['Heavy Rain', 'Rainy', 'Humid']},
        'Sep': {'temp_min': 26, 'temp_max': 33, 'humidity': 80, 'rainfall': 250, 'wind': 15, 'conditions': ['Rainy', 'Humid', 'Cloudy']},
        'Oct': {'temp_min': 24, 'temp_max': 32, 'humidity': 75, 'rainfall': 115, 'wind': 10, 'conditions': ['Rainy', 'Humid', 'Partly Cloudy']},
        'Nov': {'temp_min': 19, 'temp_max': 30, 'humidity': 68, 'rainfall': 20, 'wind': 8, 'conditions': ['Pleasant', 'Clear', 'Partly Cloudy']},
        'Dec': {'temp_min': 15, 'temp_max': 27, 'humidity': 68, 'rainfall': 5, 'wind': 8, 'conditions': ['Clear', 'Pleasant', 'Partly Cloudy']}
    },
    
    'Hyderabad': {
        'Jan': {'temp_min': 15, 'temp_max': 29, 'humidity': 55, 'rainfall': 5, 'wind': 10, 'conditions': ['Clear', 'Pleasant', 'Partly Cloudy']},
        'Feb': {'temp_min': 17, 'temp_max': 32, 'humidity': 48, 'rainfall': 10, 'wind': 12, 'conditions': ['Pleasant', 'Warm', 'Clear']},
        'Mar': {'temp_min': 21, 'temp_max': 36, 'humidity': 42, 'rainfall': 15, 'wind': 12, 'conditions': ['Warm', 'Hot', 'Partly Cloudy']},
        'Apr': {'temp_min': 24, 'temp_max': 38, 'humidity': 42, 'rainfall': 25, 'wind': 15, 'conditions': ['Hot', 'Warm', 'Partly Cloudy']},
        'May': {'temp_min': 26, 'temp_max': 39, 'humidity': 45, 'rainfall': 45, 'wind': 15, 'conditions': ['Hot', 'Very Hot', 'Partly Cloudy']},
        'Jun': {'temp_min': 24, 'temp_max': 35, 'humidity': 58, 'rainfall': 110, 'wind': 18, 'conditions': ['Rainy', 'Hot', 'Cloudy']},
        'Jul': {'temp_min': 23, 'temp_max': 31, 'humidity': 68, 'rainfall': 165, 'wind': 18, 'conditions': ['Rainy', 'Cloudy', 'Pleasant']},
        'Aug': {'temp_min': 22, 'temp_max': 30, 'humidity': 70, 'rainfall': 150, 'wind': 15, 'conditions': ['Rainy', 'Cloudy', 'Pleasant']},
        'Sep': {'temp_min': 22, 'temp_max': 31, 'humidity': 65, 'rainfall': 150, 'wind': 12, 'conditions': ['Rainy', 'Pleasant', 'Cloudy']},
        'Oct': {'temp_min': 20, 'temp_max': 31, 'humidity': 62, 'rainfall': 90, 'wind': 10, 'conditions': ['Rainy', 'Pleasant', 'Partly Cloudy']},
        'Nov': {'temp_min': 17, 'temp_max': 29, 'humidity': 60, 'rainfall': 30, 'wind': 10, 'conditions': ['Pleasant', 'Clear', 'Partly Cloudy']},
        'Dec': {'temp_min': 15, 'temp_max': 29, 'humidity': 58, 'rainfall': 10, 'wind': 10, 'conditions': ['Clear', 'Pleasant', 'Partly Cloudy']}
    },
    
    'Pune': {
        'Jan': {'temp_min': 12, 'temp_max': 30, 'humidity': 48, 'rainfall': 2, 'wind': 10, 'conditions': ['Clear', 'Pleasant', 'Partly Cloudy']},
        'Feb': {'temp_min': 13, 'temp_max': 32, 'humidity': 42, 'rainfall': 1, 'wind': 10, 'conditions': ['Clear', 'Warm', 'Pleasant']},
        'Mar': {'temp_min': 17, 'temp_max': 35, 'humidity': 38, 'rainfall': 5, 'wind': 12, 'conditions': ['Warm', 'Hot', 'Clear']},
        'Apr': {'temp_min': 20, 'temp_max': 37, 'humidity': 38, 'rainfall': 15, 'wind': 12, 'conditions': ['Hot', 'Warm', 'Partly Cloudy']},
        'May': {'temp_min': 23, 'temp_max': 37, 'humidity': 45, 'rainfall': 45, 'wind': 15, 'conditions': ['Hot', 'Rainy', 'Partly Cloudy']},
        'Jun': {'temp_min': 23, 'temp_max': 32, 'humidity': 68, 'rainfall': 130, 'wind': 18, 'conditions': ['Rainy', 'Cloudy', 'Pleasant']},
        'Jul': {'temp_min': 22, 'temp_max': 29, 'humidity': 78, 'rainfall': 185, 'wind': 18, 'conditions': ['Heavy Rain', 'Rainy', 'Cloudy']},
        'Aug': {'temp_min': 21, 'temp_max': 28, 'humidity': 78, 'rainfall': 140, 'wind': 15, 'conditions': ['Rainy', 'Cloudy', 'Pleasant']},
        'Sep': {'temp_min': 21, 'temp_max': 30, 'humidity': 70, 'rainfall': 150, 'wind': 12, 'conditions': ['Rainy', 'Pleasant', 'Cloudy']},
        'Oct': {'temp_min': 19, 'temp_max': 32, 'humidity': 62, 'rainfall': 70, 'wind': 10, 'conditions': ['Pleasant', 'Rainy', 'Partly Cloudy']},
        'Nov': {'temp_min': 15, 'temp_max': 31, 'humidity': 55, 'rainfall': 20, 'wind': 10, 'conditions': ['Pleasant', 'Clear', 'Partly Cloudy']},
        'Dec': {'temp_min': 13, 'temp_max': 30, 'humidity': 50, 'rainfall': 5, 'wind': 10, 'conditions': ['Clear', 'Pleasant', 'Partly Cloudy']}
    },
    
    'Ahmedabad': {
        'Jan': {'temp_min': 12, 'temp_max': 28, 'humidity': 52, 'rainfall': 2, 'wind': 10, 'conditions': ['Clear', 'Pleasant', 'Partly Cloudy']},
        'Feb': {'temp_min': 14, 'temp_max': 31, 'humidity': 48, 'rainfall': 1, 'wind': 12, 'conditions': ['Clear', 'Warm', 'Pleasant']},
        'Mar': {'temp_min': 19, 'temp_max': 36, 'humidity': 42, 'rainfall': 1, 'wind': 12, 'conditions': ['Warm', 'Hot', 'Clear']},
        'Apr': {'temp_min': 23, 'temp_max': 40, 'humidity': 38, 'rainfall': 1, 'wind': 15, 'conditions': ['Hot', 'Very Hot', 'Clear']},
        'May': {'temp_min': 27, 'temp_max': 42, 'humidity': 42, 'rainfall': 10, 'wind': 18, 'conditions': ['Very Hot', 'Hot', 'Dusty']},
        'Jun': {'temp_min': 28, 'temp_max': 38, 'humidity': 60, 'rainfall': 95, 'wind': 20, 'conditions': ['Hot', 'Rainy', 'Humid']},
        'Jul': {'temp_min': 27, 'temp_max': 33, 'humidity': 75, 'rainfall': 280, 'wind': 20, 'conditions': ['Heavy Rain', 'Rainy', 'Cloudy']},
        'Aug': {'temp_min': 26, 'temp_max': 32, 'humidity': 78, 'rainfall': 210, 'wind': 18, 'conditions': ['Rainy', 'Heavy Rain', 'Cloudy']},
        'Sep': {'temp_min': 25, 'temp_max': 34, 'humidity': 68, 'rainfall': 125, 'wind': 15, 'conditions': ['Rainy', 'Humid', 'Partly Cloudy']},
        'Oct': {'temp_min': 22, 'temp_max': 36, 'humidity': 55, 'rainfall': 10, 'wind': 12, 'conditions': ['Pleasant', 'Warm', 'Clear']},
        'Nov': {'temp_min': 17, 'temp_max': 32, 'humidity': 52, 'rainfall': 3, 'wind': 10, 'conditions': ['Pleasant', 'Clear', 'Partly Cloudy']},
        'Dec': {'temp_min': 13, 'temp_max': 29, 'humidity': 52, 'rainfall': 1, 'wind': 10, 'conditions': ['Clear', 'Pleasant', 'Partly Cloudy']}
    }
}

def generate_daily_weather(city, date, month_pattern):
    """Generate realistic daily weather data with variations"""
    
    # Add daily variations to base patterns
    temp_min = month_pattern['temp_min'] + np.random.normal(0, 2)
    temp_max = month_pattern['temp_max'] + np.random.normal(0, 2.5)
    
    # Ensure min < max
    if temp_min >= temp_max:
        temp_min = temp_max - 3
    
    humidity = max(20, min(100, month_pattern['humidity'] + np.random.normal(0, 8)))
    
    # Rainfall variation - some days more, some less
    if month_pattern['rainfall'] < 10:
        # Dry season - mostly no rain, occasional light rain
        rainfall = 0 if random.random() < 0.9 else np.random.exponential(2)
    elif month_pattern['rainfall'] < 50:
        # Light rain season
        rainfall = 0 if random.random() < 0.7 else np.random.exponential(month_pattern['rainfall'] / 10)
    elif month_pattern['rainfall'] < 150:
        # Moderate rain season
        rainfall = np.random.gamma(2, month_pattern['rainfall'] / 20) if random.random() < 0.5 else 0
    else:
        # Heavy rain season
        rainfall = np.random.gamma(2, month_pattern['rainfall'] / 15) if random.random() < 0.6 else 0
    
    wind_speed = max(0, month_pattern['wind'] + np.random.normal(0, 3))
    
    # Weather condition based on rainfall
    if rainfall > 50:
        condition = 'Heavy Rain'
    elif rainfall > 10:
        condition = 'Rainy'
    elif rainfall > 0:
        condition = random.choice(['Light Rain', 'Drizzle'])
    else:
        condition = random.choice(month_pattern['conditions'])
    
    return {
        'Date': date,
        'City': city,
        'Temperature_Min_C': round(temp_min, 1),
        'Temperature_Max_C': round(temp_max, 1),
        'Humidity_Percent': round(humidity, 1),
        'Rainfall_mm': round(rainfall, 1),
        'Wind_Speed_kmh': round(wind_speed, 1),
        'Weather_Condition': condition
    }

def generate_weather_dataset(start_year=2021, end_year=2025):
    """Generate complete weather dataset for all cities and dates"""
    
    weather_data = []
    
    # Generate date range
    start_date = datetime(start_year, 1, 1)
    end_date = datetime(end_year, 12, 31)
    current_date = start_date
    
    total_days = (end_date - start_date).days + 1
    print(f"Generating weather data for {len(city_weather_patterns)} cities...")
    print(f"Date range: {start_date.date()} to {end_date.date()} ({total_days} days)")
    
    while current_date <= end_date:
        month_name = current_date.strftime('%b')
        
        for city, patterns in city_weather_patterns.items():
            month_pattern = patterns[month_name]
            daily_data = generate_daily_weather(city, current_date, month_pattern)
            weather_data.append(daily_data)
        
        current_date += timedelta(days=1)
    
    # Create DataFrame
    df = pd.DataFrame(weather_data)
    
    # Sort by date and city
    df = df.sort_values(['Date', 'City']).reset_index(drop=True)
    
    print(f"\nDataset generated successfully!")
    print(f"Total records: {len(df):,}")
    print(f"Cities: {df['City'].nunique()}")
    print(f"Date range: {df['Date'].min()} to {df['Date'].max()}")
    
    return df

# Generate the dataset
print("=" * 70)
print("INDIAN WEATHER DATA GENERATOR (2021-2025)")
print("=" * 70)
print("\nCities included:")
print("-" * 70)

# Group cities by climate type
climate_groups = {
    'Extreme Cold': ['Leh', 'Shimla', 'Srinagar', 'Darjeeling'],
    'Extreme Hot': ['Jaisalmer', 'Bikaner', 'Jodhpur'],
    'Hot & Humid': ['Chennai', 'Mumbai', 'Kochi'],
    'Moderate/Varied': ['Bangalore', 'Delhi', 'Kolkata', 'Hyderabad', 'Pune', 'Ahmedabad']
}

for climate_type, cities in climate_groups.items():
    print(f"\n{climate_type}:")
    for city in cities:
        print(f"  • {city}")

print("\n" + "=" * 70)
print("\nGenerating dataset...")
print("-" * 70)

df_weather = generate_weather_dataset(2021, 2025)

# Save to CSV
output_file = 'indian_weather_2021_2025.csv'
df_weather.to_csv(output_file, index=False)
print(f"\n✓ Dataset saved to: {output_file}")

# Display statistics
print("\n" + "=" * 70)
print("DATASET STATISTICS")
print("=" * 70)

print("\nTemperature Range by City:")
print("-" * 70)
temp_stats = df_weather.groupby('City').agg({
    'Temperature_Min_C': ['min', 'mean', 'max'],
    'Temperature_Max_C': ['min', 'mean', 'max']
}).round(1)
print(temp_stats)

print("\n\nTotal Rainfall by City (2021-2025):")
print("-" * 70)
rainfall_stats = df_weather.groupby('City')['Rainfall_mm'].sum().sort_values(ascending=False).round(1)
print(rainfall_stats)

print("\n\nWeather Conditions Distribution:")
print("-" * 70)
condition_counts = df_weather['Weather_Condition'].value_counts()
print(condition_counts)

print("\n\nSample Data (First 20 rows):")
print("-" * 70)
print(df_weather.head(20).to_string(index=False))

print("\n" + "=" * 70)
print("✓ DATASET GENERATION COMPLETE!")
print("=" * 70)
