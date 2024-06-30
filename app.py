from flask import Flask, render_template, send_file, request
import requests
import os
import re
from PIL import Image
from datetime import datetime

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/")
def index():
    return render_template("home.html")
    
circuit_images = {
    "Bahrain International Circuit": "https://cdn.racingnews365.com/Circuits/Bahrain/_503xAUTO_crop_center-center_none/f1_2024_bhr_outline.png?v=1708703548",
    "Jeddah Corniche Circuit": "https://cdn.racingnews365.com/Circuits/Saudi-Arabia/_503xAUTO_crop_center-center_none/f1_2024_sau_outline.png?v=1708703549",
    "Albert Park Circuit": "https://cdn.racingnews365.com/Circuits/Australia/_503xAUTO_crop_center-center_none/f1_2024_aus_outline.png?v=1708703549",
    "Suzuka International Racing Course": "https://cdn.racingnews365.com/Circuits/Japan/_503xAUTO_crop_center-center_none/f1_2024_jap_outline.png?v=1708703688",
    "Shanghai International Circuit": "https://cdn.racingnews365.com/Circuits/China/_503xAUTO_crop_center-center_none/f1_2024_chn_outline.png?v=1708703688",
    "Miami International Autodrome": "https://cdn.racingnews365.com/Circuits/Miami/_503xAUTO_crop_center-center_none/f1_2024_mia_outline.png?v=1708703688",
    "Autodromo Enzo e Dino Ferrari": "https://cdn.racingnews365.com/Circuits/Imola/_503xAUTO_crop_center-center_none/f1_2024_ero_outline.png?v=1708704457",
    "Circuit de Monaco": "https://cdn.racingnews365.com/Circuits/Monaco/_503xAUTO_crop_center-center_none/f1_2024_mco_outline.png?v=1708704457",
    "Circuit de Barcelona-Catalunya": "https://cdn.racingnews365.com/Circuits/Spain/_503xAUTO_crop_center-center_none/f1_2024_spn_outline.png?v=1708704458",
    "Circuit Gilles-Villeneuve": "https://cdn.racingnews365.com/Circuits/Canada/_503xAUTO_crop_center-center_none/f1_2024_can_outline.png?v=1708704457",
    "Red Bull Ring": "https://cdn.racingnews365.com/Circuits/Austria/_503xAUTO_crop_center-center_none/f1_2024_aut_outline.png?v=1708704458",
    "Silverstone Circuit": "https://cdn.racingnews365.com/Circuits/Great-Britain/_503xAUTO_crop_center-center_none/f1_2024_gbr_outline.png?v=1708704458",
    "Hungaroring": "https://cdn.racingnews365.com/Circuits/Hungary/_503xAUTO_crop_center-center_none/f1_2024_hun_outline.png?v=1708704458",
    "Circuit de Spa-Francorchamps": "https://cdn.racingnews365.com/Circuits/Belgium/_503xAUTO_crop_center-center_none/f1_2024_bel_outline.png?v=1708704458",
    "Circuit Zandvoort": "https://cdn.racingnews365.com/Circuits/The-Netherlands/_503xAUTO_crop_center-center_none/f1_2024_nld_outline.png?v=1708704459",
    "Autodromo Nazionale Monza": "https://cdn.racingnews365.com/Circuits/Italy/_503xAUTO_crop_center-center_none/f1_2024_ita_outline.png?v=1708704459",
    "Marina Bay Street Circuit": "https://cdn.racingnews365.com/Circuits/Singapore/_503xAUTO_crop_center-center_none/f1_2024_sgp_outline.png?v=1708704459",
    "Baku City Circuit": "https://cdn.racingnews365.com/Circuits/Azerbaijan/_503xAUTO_crop_center-center_none/f1_2024_aze_outline.png?v=1708704459",
    "Circuit of The Americas": "https://cdn.racingnews365.com/Circuits/United-States/_503xAUTO_crop_center-center_none/f1_2024_usa_outline.png?v=1708704579",
    "Autódromo Hermanos Rodríguez": "https://cdn.racingnews365.com/Circuits/Mexico/_503xAUTO_crop_center-center_none/f1_2024_mex_outline.png?v=1708704579",
    "Autódromo José Carlos Pace": "https://cdn.racingnews365.com/Circuits/Brazil/_503xAUTO_crop_center-center_none/f1_2024_bra_outline.png?v=1708705480",
    "Las Vegas Strip Circuit": "https://cdn.racingnews365.com/Circuits/Las-Vegas/_503xAUTO_crop_center-center_none/f1_2024_lve_outline.png?v=1708705481",
    "Losail International Circuit": "https://cdn.racingnews365.com/Circuits/Qatar/_503xAUTO_crop_center-center_none/f1_2024_qat_outline.png?v=1708705481",
    "Yas Marina Circuit": "https://cdn.racingnews365.com/Circuits/Abu-Dhabi/_503xAUTO_crop_center-center_none/f1_2024_abu_outline.png?v=1708705548"
}

circuit_backgrounds = {
    "Bahrain International Circuit": "https://www.cebarco.com.bh/media/bic_wJNSbDF_vrRMUoI.jpg",
    "Jeddah Corniche Circuit": "https://www.racingcircuits.info/assets/components/gallery/connector.php?action=web/phpthumb&ctx=web&w=544&h=362&zc=1&far=C&q=90&src=%2Fassets%2Fgallery%2F49%2F552.jpg",
    "Albert Park Circuit": "https://www.austadiums.com/stadiums/photos/albert-park-gp-circuit-1.jpg",
    "Suzuka International Racing Course": "https://www.suzukacircuit.jp/eng/assets/img/slide01-pc.jpg",
    "Shanghai International Circuit": "https://www.gtplanet.net/wp-content/uploads/2016/08/shanghai-international-circuit-home-of-the-formula-one-chinese-grand-prix.jpg",
    "Miami International Autodrome": "https://www.everythingf1.com/wp-content/smush-webp/2024/04/Miami-2048x1366.jpg.webp",
    "Autodromo Enzo e Dino Ferrari": "https://motorsportguides.com/wp-content/uploads/2020/04/Autodromo-Internazionale-Enzo-e-Dino-Ferrari-GPDestinations.com-5.jpg",
    "Circuit de Monaco": "https://c4.wallpaperflare.com/wallpaper/344/548/990/sea-the-city-coast-sport-wallpaper-preview.jpg",
    "Circuit de Barcelona-Catalunya": "https://resources.motogp.pulselive.com/photo-resources/2023/03/29/2e4955bc-1c8c-4f9e-b100-57af2b1f605f/urntOqhp.jpg?width=1200&height=630",
    "Circuit Gilles-Villeneuve": "https://upload.wikimedia.org/wikipedia/commons/0/0e/Circuit_Gilles-Villeneuve_Bassin_Olympique.jpg",
    "Red Bull Ring": "https://fia-cez.com/wp-content/uploads/2019/06/20190116_170032.jpg",
    "Silverstone Circuit": "https://media.gettyimages.com/id/1325259761/video/aerial-view-of-silverstone-circuit-tracking-in.jpg?s=640x640&k=20&c=E1eInE5I95dFIGlsOMOwoYbv2TTnQvKQXQ0wQwT5-bI=",
    "Hungaroring": "https://e1.pxfuel.com/desktop-wallpaper/939/1007/desktop-wallpaper-hungarian-grand-prix-hungaroring-hungarian-grand-prix.jpg",
    "Circuit de Spa-Francorchamps": "https://i.pinimg.com/originals/e6/72/44/e6724477de5872a2ba64ad5728ca58c6.jpg",
    "Circuit Zandvoort": "https://c0.wallpaperflare.com/preview/394/972/841/car-transportation-automobile-vehicle.jpg",
    "Autodromo Nazionale Monza": "https://www.shutterstock.com/shutterstock/videos/1015360882/thumb/1.jpg?ip=x480",
    "Marina Bay Street Circuit": "https://www.formula1.com/content/dam/fom-website/manual/Getty/Singapore_2019/Friday/GettyImages-1175912103.jpg",
    "Baku City Circuit": "https://wallpapers.com/images/hd/f1-baku-city-circuit-zdcvz8g2t67ia8yz.jpg",
    "Circuit of The Americas": "https://images.ps-aws.com/c?url=https%3A%2F%2Fd3cm515ijfiu6w.cloudfront.net%2Fwp-content%2Fuploads%2F2022%2F08%2F20184146%2Fcircuit-of-the-americas-view-2021-planetf1.jpg",
    "Autódromo Hermanos Rodríguez": "https://www.shutterstock.com/shutterstock/videos/1104370055/thumb/1.jpg?ip=x480",
    "Autódromo José Carlos Pace": "https://as2.ftcdn.net/v2/jpg/05/13/62/63/1000_F_513626344_SiRbvNlLTqAJQcYJ43Eh8lU2ivZO9B0v.jpg",
    "Las Vegas Strip Circuit": "https://preview.redd.it/xa6uju3qvqma1.jpg?width=1200&format=pjpg&auto=webp&v=enabled&s=9b3eeda93a7e60142fe779f7d9f48025d0755a50",
    "Losail International Circuit": "https://resources.motogp.pulselive.com/photo-resources/2023/08/24/9d8cd339-6b4d-4057-9c6f-60921e67f9e9/F1JpFksXoAAASwg.jpg?width=1440&height=810",
    "Yas Marina Circuit": "https://cdn-9.motorsport.com/images/amp/0rGEEzO2/s6/yas-marina-circuit-new-layout-.jpg"
}


@app.route("/circuits")
def circuits():
    try:
        url = 'https://api-formula-1.p.rapidapi.com/races?season=2024&type=race'
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'x-rapidapi-ua': 'RapidAPI-Playground',
            'x-rapidapi-host': 'api-formula-1.p.rapidapi.com',
            'x-rapidapi-key': os.getenv('rapidapi')
        }
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            circuits = data['response']
            
            for circuit in circuits:
                circuit_name = circuit['circuit']['name']
                circuit_date = circuit['date']
                laps = circuit['laps']['total']
                formated_number = re.findall(r"[-+]?\d*\.\d+|\d+", circuit['distance'])[0]
                distance = float(formated_number)
                circuit_lenght = round(distance / laps, 2)
                circuit_date_obj = datetime.strptime(circuit_date, '%Y-%m-%dT%H:%M:%S%z')
                formatted_date = circuit_date_obj.strftime('%m/%d/%Y')
                circuit['date'] = formatted_date
                circuit['circuit_lenght'] = circuit_lenght
                if circuit_name in circuit_images:
                    circuit['circuit']['image'] = circuit_images[circuit_name]
                    circuit['circuit']['background'] = circuit_backgrounds[circuit_name]
                else:
                    circuit['circuit']['image'] = 'URL_DEFAULT'  

            return render_template("circuits.html", circuits=circuits)

        else:
            return f"Failed to fetch circuits: {response.status_code}", 500

    except Exception as e:
        error_message = f"Ocorreu um erro: {e}"
        print(error_message)
        return error_message, 500
    

teams_images = {
    "Scuderia Ferrari": "https://i.pinimg.com/564x/f3/72/85/f372858d4628fe7bde168cbc1e7be453.jpg",
    "McLaren Racing": "https://media.formula1.com/content/dam/fom-website/teams/2024/mclaren-logo.png",
    "Mercedes-AMG Petronas": "https://media.formula1.com/content/dam/fom-website/teams/2024/mercedes-logo.png",
    "Red Bull Racing": "https://media.formula1.com/content/dam/fom-website/teams/2024/red-bull-racing-logo.png",
    "Williams F1 Team": "https://media.formula1.com/content/dam/fom-website/teams/2024/williams-logo.png",
    "Aston Martin F1 Team": "https://media.formula1.com/content/dam/fom-website/teams/2024/aston-martin-logo.png",
    "Visa Cash App RB Formula One Team": "https://media.formula1.com/content/dam/fom-website/teams/2024/rb-logo.png",
    "Haas F1 Team": "https://media.formula1.com/content/dam/fom-website/teams/2024/haas-logo.png",
    "Alpine F1 Team": "https://media.formula1.com/content/dam/fom-website/teams/2024/alpine-logo.png",
    "Sauber F1 Team": "https://media.formula1.com/content/dam/fom-website/teams/2024/kick-sauber-logo.png"
}

drivers_images = {
    "Oliver Bearman": "https://media.formula1.com/d_driver_fallback_image.png/content/dam/fom-website/drivers/O/OLIBEA01_Oliver_Bearman/olibea01.png"
}

def get_seasons():
    try:
        url = 'https://api-formula-1.p.rapidapi.com/seasons'
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'x-rapidapi-ua': 'RapidAPI-Playground',
            'x-rapidapi-host': 'api-formula-1.p.rapidapi.com',
            'x-rapidapi-key': os.getenv('rapidapi')
        }
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            seasons = data.get('response', [])
            seasons.sort(reverse=True)
            return seasons

        else:
            return f"Failed to fetch circuits: {response.status_code}", 500

    except Exception as e:
        error_message = f"Ocorreu um erro: {e}"
        print(error_message)
        return error_message, 500
    
def get_driver_rankings(season):
    url = f'https://api-formula-1.p.rapidapi.com/rankings/drivers?season={season}'
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x-rapidapi-ua': 'RapidAPI-Playground',
        'x-rapidapi-host': 'api-formula-1.p.rapidapi.com',
        'x-rapidapi-key': os.getenv('rapidapi')
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        drivers = data['response']

        for driver in drivers:
            team_name = driver['team']['name']
            driver_name = driver['driver']['name']
            if team_name in teams_images:
                driver['team']['logo'] = teams_images[team_name]
            if driver_name in drivers_images:
                driver['driver']['image'] = drivers_images[driver_name]

        return drivers
    else:
        return []

@app.route("/drivers", methods=['GET', 'POST'])
def drivers():
    seasons = get_seasons()
    selected_season = request.form.get('season', '2024')  # '2024' é o valor padrão
    drivers = get_driver_rankings(selected_season)
    return render_template("drivers.html", drivers=drivers, seasons=seasons, selected_season=selected_season)

if __name__ == '__main__':
    app.run(debug=True)




