from flask import Flask, render_template, request

app = Flask(__name__, template_folder = 'templates')
General = {
    "CV" : "",
    "numberC" : "",
    "RM" :"" ,
    "MagneticD" : "",
    "Arena" : ""
}
Drive = {
    "DmotorKV" : "",
    "DSaturation" : "",
    "DGearboxR" : "",
    "DExternalR" : "",
    "DDR" : "",
    "D#motor" : "",
    "DWheelD" : ""
}
Weapon = {
    "WmotorKV" : "",
    "WRR" : "",
    "W#motor" : "",
    "WWeightmotor" : "",
    "WweaponD" : "",
    "WTorque" : "",
    "WSaturation" : "",
    "WGoalMOI" : ""
}
Arm = {
    "AMotorKV" : "",
    "AGearboxR" : "",
    "ABeltR" : "",
    "ABevelR" : "",
    "ASaturation" : "",
    "AMaxSwingA" : "",
    "ArmLength" : "",
    "AWeaponW" : "",
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