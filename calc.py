from flask import Flask, render_template, request

app = Flask(__name__, template_folder = 'templates')
General = {
    "CV" : "",
    "#C" : "",
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
        user_input = request.form.get('kv_input')
        if user_input:
            Drive["DmotorKV"] = user_input
    return render_template('Calculator.html', gpara = General, dpara = Drive, wpara = Weapon, apara = Arm)
if __name__ == "__main__":
    app.run(host = '127.0.0.1', debug=True)