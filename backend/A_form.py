import flet as ft
import joblib
import pandas as pd


class ModelStuff:
    pipeline = joblib.load("assets/model/pipeline.pkl")
    model = joblib.load("assets/model/model.pkl")
    countries: list[str] = [
        "Italy",
        "Portugal",
        "US",
        "Spain",
        "Germany",
        "France",
        "Argentina",
        "Chile",
        "Australia",
        "South Africa",
        "Israel",
        "Hungary",
        "Austria",
        "Greece",
        "Mexico",
        "Canada",
        "New Zealand",
        "Romania",
        "Slovenia",
        "Georgia",
        "Uruguay",
        "England",
        "Bulgaria",
        "Turkey",
    ]
    provinces: list[str] = [
        "Sicily & Sardinia",
        "Douro",
        "Oregon",
        "Northern Spain",
        "Alsace",
        "California",
        "Mosel",
        "Mendoza Province",
        "Southern Italy",
        "Bordeaux",
        "Central Italy",
        "Washington",
        "Champagne",
        "South Australia",
        "Tuscany",
        "New York",
        "Piedmont",
        "Southwest France",
        "Northeastern Italy",
        "Burgundy",
        "Veneto",
        "Catalonia",
        "Loire Valley",
        "Provence",
    ]
    variety: list[str] = [
        "White Blend",
        "Portuguese Red",
        "Riesling",
        "Pinot Noir",
        "Pinot Gris",
        "Cabernet Sauvignon",
        "Malbec",
        "Red Blend",
        "Merlot",
        "Chardonnay",
        "Sangiovese",
        "Cabernet Franc",
        "Champagne Blend",
        "Sauvignon Blanc",
        "Bordeaux-style Red Blend",
        "Rosé",
        "Zinfandel",
        "Syrah",
        "Nebbiolo",
        "Rhône-style Red Blend",
        "Portuguese White",
        "Grüner Veltliner",
        "Sparkling Blend",
        "Tempranillo",
    ]
    winery: list[str] = [
        "Jean-Baptiste Adam",
        "Tasca d'Almerita",
        "Yalumba",
        "Heron Hill",
        "Lamoreaux Landing",
        "Kuentz-Bas",
        "Domaine Zind-Humbrecht",
        "Testarossa",
        "Dutton-Goldfield",
        "La Chablisienne",
        "Viña Bisquertt",
        "Emiliana",
        "J. Lohr",
        "Wagner",
        "D'Arenberg",
        "Willamette Valley Vineyards",
        "Viña Cobos",
        "Salomon-Undhof",
        "Talley",
        "Clos La Chance",
        "Robert Weil",
        "Louis Latour",
        "Lapostolle",
        "Tommasi",
        "San Pedro",
        "Undurraga",
        "Milbrandt",
        "Winzer Krems",
        "Robert Mondavi",
        "Chehalem",
        "Henri de Villamont",
        "Domaine Serene",
        "Dr. Loosen",
        "Sparkman",
        "Babcock",
        "Fenestra",
        "Maximin Grünhäuser",
        "Iron Horse",
        "Terre Rouge",
        "Loring Wine Company",
        "Midnight",
        "Rodney Strong",
        "Foxen",
        "Quinta da Lagoalva de Cima",
        "Reichsgraf von Kesselstatt",
        "Seven Hills",
        "Chateau Ste. Michelle",
        "Casca Wines",
        "Wines & Winemakers",
        "De Loach",
        "Adelsheim",
        "Laetitia",
        "Brian Carter Cellars",
        "Efeste",
        "Georges Duboeuf",
        "Maryhill",
        "J Vineyards & Winery",
        "Aveleda",
        "Santa Ema",
        "Morandé",
        "Kendall-Jackson",
        "Fournier Père et Fils",
        "Trisaetum",
        "Poças",
        "Williams Selyem",
        "Cayuse",
        "Santa Alicia",
        "Concha y Toro",
        "Santa Rita",
        "Trapiche",
        "Pali",
        "Bacalhôa Wines of Portugal",
        "Fess Parker",
        "J. Portugal Ramos",
        "Balletto",
        "Cameron Hughes",
        "Domäne Wachau",
        "Martin Ray",
        "Louis Jadot",
        "Georges Vigouroux",
        "Domaines Barons de Rothschild (Lafite)",
        "Bründlmayer",
        "Santa Carolina",
        "Herdade do Esporão",
        "DFJ Vinhos",
        "Valentin Bianchi",
        "Recanati",
        "Quinta do Casal Branco",
        "François Lurton",
        "Gérard Bertrand",
        "Caliterra",
        "Errazuriz",
        "Rock Wall",
        "L. Tramier & Fils",
        "Kokomo",
        "Columbia Crest",
        "Montes",
        "Canoe Ridge",
        "Domaines Devillard",
        "Novelty Hill",
        "Casa Santos Lima",
        "Marimar Estate",
        "Hirsch",
        "Januik",
        "Gloria Ferrer",
        "Echeverria",
        "Barton & Guestier",
        "V. Sattui",
        "Jean-Luc and Paul Aegerter",
        "MacPhail",
        "Bodegas Valdemar",
        "Lynmar",
        "Companhia das Quintas",
        "Naggiar",
        "Joseph Swan Vineyards",
        "Viu Manent",
        "Morgan",
        "Feudi di San Gregorio",
        "Zaca Mesa",
        "Kunde",
        "Sojourn",
        "Gary Farrell",
        "Concannon",
        "Zuccardi",
        "Henri Bourgeois",
        "Mumm Napa",
        "Chanson Père et Fils",
        "Mark Ryan",
        "Bernardus",
        "Calera",
        "King Estate",
        "K Vintners",
        "Sineann",
        "José Maria da Fonseca",
        "Raymond",
        "Torii Mor",
        "Dão Sul",
        "Siduri",
        "Albert Bichot",
        "Olivier Leflaive",
        "Gorman",
        "Adelaida",
        "Schramsberg",
        "Bouchard Père & Fils",
        "Dr. Pauly Bergweiler",
    ]


class InputForm(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__(expand=True)
        self.page = page
        self.slider_a_value: int = 0
        self.slider_b_value: float = 0
        self.user_values: list = None

        self.drop_a: ft.Dropdown = ft.Dropdown(
            label="Country",
            hint_text="Select the country",
            options=[ft.dropdown.Option(i) for i in ModelStuff.countries],
            autofocus=True,
        )

        self.drop_b: ft.Dropdown = ft.Dropdown(
            label="Province",
            hint_text="Select the province",
            options=[ft.dropdown.Option(i) for i in ModelStuff.provinces],
            autofocus=True,
        )
        self.drop_c: ft.Dropdown = ft.Dropdown(
            label="Variety",
            hint_text="Select the variety",
            options=[ft.dropdown.Option(i) for i in ModelStuff.variety],
            autofocus=True,
        )
        self.drop_d: ft.Dropdown = ft.Dropdown(
            label="Winery",
            hint_text="Select the winery",
            options=[ft.dropdown.Option(i) for i in ModelStuff.winery],
        )

        self.slider_a: ft.Container = ft.Container(
            content=ft.Column(
                [
                    ft.Text("Select wine's age:"),
                    ft.Slider(
                        min=0,
                        max=150,
                        divisions=150,
                        label="{value}",
                        on_change=self.slider_a_changed,
                    ),
                ]
            )
        )
        self.slider_b: ft.Container = ft.Container(
            content=ft.Column(
                [
                    ft.Text("Select wine's points:"),
                    ft.Slider(
                        min=0,
                        max=100,
                        divisions=100,
                        label="{value}%",
                        on_change=self.slider_b_changed,
                    ),
                ]
            )
        )

        self.button: ft.Container = ft.Container(
            content=ft.Column(
                [ft.ElevatedButton(text="Submit", on_click=self.button_clicked)],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            alignment=ft.alignment.center,
        )

        self.predict_button: ft.Container = ft.ElevatedButton(
            text="Predict", on_click=self.predicted_button
        )

        self.txt_predict: ft.Text = ft.Text()

        self.predicted_box: ft.Container = ft.Container(
            content=ft.Row(
                [self.predict_button, self.txt_predict],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            alignment=ft.alignment.center,
        )

        self.content: ft.Column = ft.Column(
            [
                self.drop_a,
                self.drop_b,
                self.drop_c,
                self.drop_d,
                self.slider_a,
                self.slider_b,
                self.button,
                ft.Divider(),
                self.predicted_box,
            ]
        )

    def build(self):
        return self.content

    def button_clicked(self, e):
        self.user_values = [
            self.drop_a.value,
            self.drop_b.value,
            self.drop_c.value,
            self.drop_d.value,
            self.slider_a_value,
            self.slider_b_value,
        ]

        self.page.snack_bar = ft.SnackBar(
            ft.Text("Submitted.", color="black"), bgcolor="green", duration=3000
        )
        self.page.snack_bar.open = True
        self.page.update()

    def model_function(self, country, province, variety, winery, age, points):
        dic: dict = {
            "Pais": country,
            "Provincia": province,
            "Variedad": variety,
            "Bodega": winery,
            "Antiguedad": age,
            "Puntos": points,
        }

        feature_names = [
            "Pais",
            "Provincia",
            "Variedad",
            "Bodega",
            "Antiguedad",
            "Puntos",
        ]
        df = pd.DataFrame(dic, index=[0], columns=feature_names)
        new_data_transformed = ModelStuff.pipeline.transform(df)
        rdo_df = pd.DataFrame(new_data_transformed, columns=feature_names)
        rdo = ModelStuff.model.predict(rdo_df)
        return rdo[0]

    def predicted_button(self, e):
        try:
            prediction = self.model_function(
                self.user_values[0],
                self.user_values[1],
                self.user_values[2],
                self.user_values[3],
                self.user_values[4],
                self.user_values[5],
            )

            self.txt_predict.value = f"Predicted price is: ${prediction}"
        except:
            self.page.snack_bar = ft.SnackBar(
                ft.Text("Check the inputs!! All of them must be completed.", color="black"),
                bgcolor="red",
                duration=1000,
            )
            self.page.snack_bar.open = True

        self.page.update()

    def slider_a_changed(self, e):
        self.slider_a_value = e.control.value

    def slider_b_changed(self, e):
        self.slider_b_value = e.control.value
