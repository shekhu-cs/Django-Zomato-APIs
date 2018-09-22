from rest_framework.views import APIView
from rest_framework.response import Response
import json, urllib, urllib.request
import json
import csv
import io


class DailyMenu(APIView):

    def get(self, request):
        url = ('https://developers.zomato.com/api/v2.1/'
               'dailymenu?res_id=16506484&apikey=68aab2421c44cffdf8ca33eaef07dfe3')
        # to get daily menu items of single restaurants

        # grabbing the JSON result
        response = urllib.request.urlopen(url)
        json_raw = response.read()
        json_data = json.loads(json_raw)
        daily_menu = json_data["daily_menus"]

        f = io.open('daily_menu.csv', 'w', encoding="utf-8")     # resolve character encoding issue
        csv_writer = csv.writer(f)
        count = 0

        for dm in daily_menu:
            if count == 0:
                header = dm.keys()
                csv_writer.writerow(header)
                count += 1
                csv_writer.writerow(dm.values())

        f.close()
        return Response(json_data)


class Restaurants(APIView):

    def get(self, request):
        url = ('https://developers.zomato.com/api/v2.1/'
               'search?apikey=68aab2421c44cffdf8ca33eaef07dfe3'
               '&q=restaurant&lat=50.075539&lon=14.437800&radius=100&sort=rating&order=asc')
        # to get all restaurants details

        # grabbing the JSON result
        response = urllib.request.urlopen(url)
        json_raw = response.read()
        json_data = json.loads(json_raw)
        restaurants = json_data["restaurants"]

        f = io.open('restaurants.csv', 'w', encoding="utf-8")     # resolve character encoding issue
        csv_writer = csv.writer(f)
        count = 0

        for res in restaurants:
            if count == 0:
                header = res.keys()
                csv_writer.writerow(header)
                count += 1
                csv_writer.writerow(res.values())
        f.close()
        return Response(json_data)