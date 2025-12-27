from flask import Flask, render_template, request

app = Flask(__name__, template_folder = 'templates')
General = {
    "CV" : 0,
    "numberC" : 0,
    "RM" :0 ,
    "MagneticD" : 0,
    "Arena" : 0
}
Drive = {
    "DmotorKV" : 0,
    "DSaturation" : 0,
    "DGearboxR" : 0,
    "DExternalR" : 0,
    "DDR" : 0,
    "Dnummotor" : 0,
    "DWheelD" : 0
}
Weapon = {
    "WmotorKV" : 0,
    "WRR" : 0,
    "Wnummotor" : 0,
    "WWeightmotor" : 0,
    "WweaponD" : 0,
    "WTorque" : 0,
    "WSaturation" : 0,
    "WGoalMOI" : 0
}
Arm = {
    "AMotorKV" : 0,
    "AGearboxR" : 0,
    "ABeltR" : 0,
    "ABevelR" : 0,
    "ASaturation" : 0,
    "AMaxSwingA" : 0,
    "ArmLength" : 0,
    "AWeaponW" : 0,
    "ArmWeight" :0,
    "MOI" : 0
}
@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        for key, value in request.form.items():
            if key in General:
                General[key] = value
            if key in Drive:
                Drive[key] = value
            if key in Weapon:
                Weapon[key] = value
            if key in Arm:
                Arm[key] = value
    return render_template('Calculator.html', gpara = General, dpara = Drive, wpara = Weapon, apara = Arm)
if __name__ == "__main__":
    app.run(host = '127.0.0.1', debug=True)