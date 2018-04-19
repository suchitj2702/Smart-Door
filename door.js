// initiating the various pins used in the Raspi
var motorPin1 = 17
var motorPin2 = 22
var greenled = 23
var redled = 24

// the unique token created by the blink app to connect to Raspi
var blynkToken = '1b2544c78fda4079bbf7454f674c5f69';

function opendoor(arg) {
  motor1.digitalWrite(1);
}

function closedoor(arg) {
  motor2.digitalWrite(1);
}

var locked = true

var Gpio = require('pigpio').Gpio,

// initiating the GPIO ports on the Raspi
motor1 = new Gpio(motorPin1, {mode: Gpio.OUTPUT});
motor2 = new Gpio(motorPin2, {mode: Gpio.OUTPUT});
green = new Gpio(greenled, {mode: Gpio.OUTPUT});
red = new Gpio(redled, {mode: Gpio.OUTPUT});

green.digitalWrite(0);
red.digitalWrite(0);
motor1.digitalWrite(0);
motor2.digitalWrite(0);

//Setup blynk
var Blynk = require('blynk-library');
var blynk = new Blynk.Blynk(blynkToken);
var v0 = new blynk.VirtualPin(0);

// rotating the motor in clockwise or anti-clockwise direction based upon input from Blynk app
v0.on('write', function(param) {
console.log('V0:', param);
  	if (param[0] === '0') { //unlocked
  		green.digitalWrite(1);
  		red.digitalWrite(0);
  		setTimeout(opendoor,2000)
  		motor1.digitalWrite(0);
  	} else if (param[0] === '1') { //locked
  		red.digitalWrite(1);
  		green.digitalWrite(0);
  		setTimeout(closedoor,2000)
  		motor2.digitalWrite(0);
  	} else {
  		blynk.notify("Door lock button was pressed with unknown parameter");
  	}
});

blynk.on('connect', function() { console.log("Blynk ready."); });
blynk.on('disconnect', function() { console.log("DISCONNECT"); });
