#!/usr/bin/python

#######################

#  http://t.me/DWIComunity#

#######################

import random

import sys

import time

def ban1(b):

    for a in b + '\n':

        sys.stdout.write(a)

        sys.stdout.flush()

        time.sleep(random.random() * 0.2)

ban1('Loading...\n$ Welcome to mini script')

def ban2(d):

    for c in d + '\n':

        sys.stdout.write(c)

        sys.stdout.flush()

        time.sleep(random.random() * 0.01)

ban2('$                      /"\ \n$                     |\./| \n$                     |   |\n$                     |   |\n$                     |>~<|\n$                     |   |\n$                  /"\|   |/"\..\n$              /~\|   |   |   | \ \n$             |   =[@]=   |   |  \ \n$             |   |   |   |   |   \ \n$             | ~   ~   ~   ~ |`   ) \n$             |                   / \n$              \                 / \n$               \               / \n$                \    _____    / \n$                 |--//''`\--| \n$                 | (( +==)) | \n$                 |--\_|_//--|')

def ban3(f):

    for e in f + '\n':

        sys.stdout.write(e)

        sys.stdout.flush()

        time.sleep(random.random() * 0.02)

ban3('$  _____         _  \n$ |   __|_ _ ___| |_    _ _ ___ _ _ \n$ |   __| | |  _| "_|  | | | . | | | \n$ |__|  |___|___|_,_|  |_  |___|___| \n$                      |___|')

 

print "created by Zxce3"

title = raw_input("Judul title: ")

message = raw_input("Pesan lu: ")

name = raw_input("nama lu: ")

#Open the index

fo = open("script.html","w")

script1 = """<html lang="en"><head>

<meta charset="UTF-8">

<title>"""

script2 = title

script3 = """</title></head>

<style>

			body{				background-color:rgb(FF, FF, FFF);

			}

		</style>

<style>

* {

	border: 0;

	box-sizing: border-box;

	margin: 0;

	padding: 0;

}

body {

	background: #f1f1f1;

	font-size: calc(16px + (20 - 16)*(100vw - 320px)/(1024 - 320));

}

.troll {

	font-size: 0.625em;

	margin: auto;

	overflow: hidden;

	position: relative;

	width: 22em;

	height: 39em;

}

.troll div {

	animation-duration: 0.75s;

	animation-timing-function: linear;

	animation-iteration-count: infinite;

	position: absolute;

}

/* Head */

.troll__head {

	animation-name: head;

	top: 2.5em;

	left: 8em;

	width: 14em;

	height: 11.5em;

}

.troll__head div {

	background: #171717;

	border-radius: 0.5em;

	transform-origin: 0.5em 0.5em;

	width: 1em;

	z-index: -1;

}

.troll__face {

	width: 100%;

	height: auto;

}

/* Arms */

.troll__head > div {

	top: calc(100% - 3.25em);

	left: calc(50% - 0.5em);

}

.troll__head > div div {

	top: calc(100% - 1em);

}

.troll__right-arm {

	animation-name: rightArm;

	height: 11em;

	transform: rotate(85deg);

}

.troll__left-arm {

	animation-name: leftArm;

	height: 10em;

	transform: rotate(-12deg);

}

.troll__right-lower-arm {

	animation-name: rightLowerArm;

	height: 4em;

	transform: rotate(-145deg);

}

.troll__left-lower-arm {

	animation-name: leftLowerArm;

	height: 7em;

	transform: rotate(143deg);

}

div.troll__right-hand, div.troll__left-hand {

	border-radius: 0.75em;

	left: -0.25em;

	transform-origin: 0.75em 0.5em;

	height: 1.5em;

	width: 1.5em;

}

.troll__right-hand {

	animation-name: rightHand;

	transform: rotate(-30deg);

}

.troll__left-hand {

	animation-name: leftHand;

	transform: rotate(90deg);

}

/* Body */

.troll__upper-body {

	animation-name: upperBody;

	height: 7em;

	transform: rotate(-5deg);

}

.troll__lower-body {

	animation-name: lowerBody;

	height: 8em;

	transform: rotate(18deg);

}

/* Legs */

.troll__right-thigh {

	animation-name: rightThigh;

	height: 9.25em;

	transform: rotate(100deg);

}

.troll__left-thigh {

	animation-name: leftThigh;

	height: 6.25em;

	transform: rotate(-25deg);

}

.troll__right-lower-leg {

	animation-name: rightLowerLeg;

	height: 4.5em;

	transform: rotate(-120deg);

}

.troll__left-lower-leg {

	animation-name: leftLowerLeg;

	height: 6.75em;

	transform: rotate(24deg);

}

.troll__right-foot, .troll__left-foot {

	height: 3em;

}

.troll__right-foot {

	animation-name: rightFoot;

	transform: rotate(95deg);

}

.troll__left-foot {

	animation-name: leftFoot;

	transform: rotate(-90deg);

}

/* Animations */

@keyframes head {

	from, to { transform: translate(0,0) rotate(0) }

	10% { transform: translate(-0.25em,0.25em) rotate(0) }

	20% { transform: translate(-1.25em,1.5em) rotate(-4deg) }

	30% { transform: translate(-2.75em,3em) rotate(-8deg) }

	40% { transform: translate(-5.25em,1.5em) rotate(-16deg) }

	50% { transform: translate(-6.25em,-0.5em) rotate(-24deg) }

	60% { transform: translate(-6.25em,-0.75em) rotate(-20deg) }

	70% { transform: translate(-4.25em,1.25em) rotate(-18deg) }

	80% { transform: translate(-2.25em,4.25em) rotate(0) }

	90% { transform: translate(-0.75em,3.75em) rotate(0) }

}

@keyframes rightArm {

	from, to { height: 11em; transform: rotate(85deg) }

	10% { height: 10.5em; transform: rotate(80deg) }

	20% { height: 9.5em; transform: rotate(70deg) }

	30% { height: 8em; transform: rotate(60deg) }

	40% { height: 7em; transform: rotate(45deg) }

	50% { height: 8.75em; transform: rotate(36deg) }

	60% { height: 9.25em; transform: rotate(27deg) }

	70% { height: 8.25em; transform: rotate(35deg) }

	80% { height: 6.5em; transform: rotate(40deg) }

	90% { height: 7.5em; transform: rotate(56deg) }

}

@keyframes leftArm {

	from, to { height: 10em; transform: rotate(-12deg) }

	10% { height: 9em; transform: rotate(-20deg) }

	20% { height: 9em; transform: rotate(-27deg) }

	30% { height: 8.5em; transform: rotate(-35deg) }

	40% { height: 10em; transform: rotate(-87deg) }

	50% { height: 9.75em; transform: rotate(-70deg) }

	60% { height: 9.25em; transform: rotate(-80deg) }

	70% { height: 8.25em; transform: rotate(-80deg) }

	80% { height: 8.75em; transform: rotate(-65deg) }

	90% { height: 9em; transform: rotate(-43deg) }

}

@keyframes rightLowerArm {

	from, to { height: 4em; transform: rotate(-145deg) }

	10% { height: 3.5em; transform: rotate(-150deg) }

	20% { height: 4em; transform: rotate(-130deg) }

	30% { height: 4em; transform: rotate(-95deg) }

	40% { height: 6em; transform: rotate(-148deg) }

	50% { height: 5.75em; transform: rotate(-145deg) }

	60% { height: 5.5em; transform: rotate(-150deg) }

	70% { height: 4em; transform: rotate(-150deg) }

	80% { height: 3.25em; transform: rotate(-100deg) }

	90% { height: 4.5em; transform: rotate(-105deg) }

}

@keyframes leftLowerArm {

	from, to { height: 7em; transform: rotate(143deg) }

	10% { height: 7em; transform: rotate(140deg) }

	20% { height: 5em; transform: rotate(110deg) }

	30% { height: 3em; transform: rotate(95deg) }

	40% { height: 4em; transform: rotate(147deg) }

	50% { height: 3.25em; transform: rotate(130deg) }

	60% { height: 4.5em; transform: rotate(120deg) }

	70% { height: 4.5em; transform: rotate(120deg) }

	80% { height: 4.25em; transform: rotate(143deg) }

	90% { height: 4.25em; transform: rotate(125deg) }

}

@keyframes rightHand {

	from, to { transform: rotate(-30deg) }

	10% { transform: rotate(-30deg) }

	20% { transform: rotate(-100deg) }

	30% { transform: rotate(-45deg) }

	40% { transform: rotate(-65deg) }

	50% { transform: rotate(-75deg) }

	60% { transform: rotate(-60deg) }

	70% { transform: rotate(-30deg) }

	80% { transform: rotate(-60deg) }

	90% { transform: rotate(-30deg) }

}

@keyframes leftHand {

	from, to { transform: rotate(90deg) }

	10% { transform: rotate(90deg) }

	20% { transform: rotate(90deg) }

	30% { transform: rotate(30deg) }

	40% { transform: rotate(90deg) }

	50% { transform: rotate(0deg) }

	60% { transform: rotate(90deg) }

	70% { transform: rotate(45deg) }

	80% { transform: rotate(-90deg) }

	90% { transform: rotate(60deg) }

}

@keyframes upperBody {

	from, to { transform: rotate(-5deg) }

	10% { transform: rotate(5deg) }

	20% { transform: rotate(12deg) }

	30% { transform: rotate(15deg) }

	40% { transform: rotate(24deg) }

	50% { transform: rotate(30deg) }

	60% { transform: rotate(16deg) }

	70% { transform: rotate(11deg) }

	80% { transform: rotate(-10deg) }

	90% { transform: rotate(-8deg) }

}

@keyframes lowerBody {

	from, to { height: 8em; transform: rotate(18deg) }

	10% { height: 8.5em; transform: rotate(-2deg) }

	20% { height: 8em; transform: rotate(-10deg) }

	30% { height: 6.75em; transform: rotate(-18deg) }

	40% { height: 7em; transform: rotate(-24deg) }

	50% { height: 8.75em; transform: rotate(-20deg) }

	60% { height: 10.25em; transform: rotate(-5deg) }

	70% { height: 8em; transform: rotate(6deg) }

	80% { height: 5.75em; transform: rotate(18deg) }

	90% { height: 5.75em; transform: rotate(25deg) }

}

@keyframes rightThigh {

	from, to { height: 9.25em; transform: rotate(100deg) }

	10% { height: 8.75em; transform: rotate(110deg) }

	20% { height: 9.25em; transform: rotate(50deg) }

	30% { height: 9.75em; transform: rotate(53deg) }

	40% { height: 8.75em; transform: rotate(53deg) }

	50% { height: 9.25em; transform: rotate(45deg) }

	60% { height: 8.5em; transform: rotate(46deg) }

	70% { height: 8.25em; transform: rotate(38deg) }

	80% { height: 8.5em; transform: rotate(38deg) }

	90% { height: 7.75em; transform: rotate(65deg) }

}

@keyframes leftThigh {

	from, to { height: 6.25em; transform: rotate(-25deg) }

	10% { height: 7em; transform: rotate(-23deg) }

	20% { height: 8.75em; transform: rotate(-29deg) }

	30% { height: 10.5em; transform: rotate(-78deg) }

	40% { height: 10em; transform: rotate(-88deg) }

	50% { height: 10em; transform: rotate(-87deg) }

	60% { height: 9em; transform: rotate(-95deg) }

	70% { height: 8em; transform: rotate(-64deg) }

	80% { height: 5.5em; transform: rotate(-45deg) }

	90% { height: 5.75em; transform: rotate(-42deg) }

}

@keyframes rightLowerLeg {

	from, to { height: 4.5em; transform: rotate(-120deg) }

	10% { height: 5em; transform: rotate(-115deg) }

	20% { height: 7em; transform: rotate(-90deg) }

	30% { height: 5.25em; transform: rotate(-85deg) }

	40% { height: 5em; transform: rotate(-80deg) }

	50% { height: 5.25em; transform: rotate(-70deg) }

	60% { height: 5.5em; transform: rotate(-70deg) }

	70% { height: 6em; transform: rotate(-50deg) }

	80% { height: 5.5em; transform: rotate(-70deg) }

	90% { height: 6.5em; transform: rotate(-95deg) }

}

@keyframes leftLowerLeg {

	from, to { height: 6.75em; transform: rotate(24deg) }

	10% { height: 6em; transform: rotate(45deg) }

	20% { height: 4.75em; transform: rotate(85deg) }

	30% { height: 6.75em; transform: rotate(135deg) }

	40% { height: 6.25em; transform: rotate(132deg) }

	50% { height: 6.25em; transform: rotate(125deg) }

	60% { height: 5.75em; transform: rotate(110deg) }

	70% { height: 5.75em; transform: rotate(88deg) }

	80% { height: 6.75em; transform: rotate(45deg) }

	90% { height: 6em; transform: rotate(35deg) }

}

@keyframes rightFoot {

	from, to { transform: rotate(95deg) }

	10% { transform: rotate(150deg) }

	20% { transform: rotate(130deg) }

	30% { transform: rotate(95deg) }

	40% { transform: rotate(100deg) }

	50% { transform: rotate(110deg) }

	60% { transform: rotate(103deg) }

	70% { transform: rotate(70deg) }

	80% { transform: rotate(65deg) }

	90% { transform: rotate(80deg) }

}

@keyframes leftFoot {

	from, to { transform: rotate(-90deg) }

	10% { transform: rotate(-105deg) }

	20% { transform: rotate(-90deg) }

	30% { transform: rotate(-70deg) }

	40% { transform: rotate(-85deg) }

	50% { transform: rotate(-85deg) }

	60% { transform: rotate(-70deg) }

	70% { transform: rotate(-90deg) }

	80% { transform: rotate(-70deg) }

	90% { transform: rotate(-60deg) }

}

/* Dark Mode */

@media screen and (prefers-color-scheme: dark) {

	body {

		background: #171717;

	}

	.troll__head div {

		background: #f1f1f1;

	}

}

</style>

<script>

  window.console = window.console || function(t) {};

</script>

<script>

  if (document.location.search.match(/type=embed/gi)) {

    window.parent.postMessage("resize", "*");

  }

</script>

</head>

<body translate="no">

<div class="troll">

<div class="troll__head">

<img class="troll__face" src="https://i.ibb.co/XjW89FS/rsz-pngguru-com.png" srcset="https://i.ibb.co/XjW89FS/rsz-pngguru-com.png 1x, https://i.ibb.co/tXXns3H/rsz-pnggurucom-1.png 2x" alt="Trollface" width="140" height="115">

<div class="troll__right-arm">

<div class="troll__right-lower-arm">

<div class="troll__right-hand"></div>

</div>

</div>

<div class="troll__left-arm">

<div class="troll__left-lower-arm">

<div class="troll__left-hand"></div>

</div>

</div>

<div class="troll__upper-body">

<div class="troll__lower-body">

<div class="troll__right-thigh">

<div class="troll__right-lower-leg">

<div class="troll__right-foot"></div>

</div>

</div>

<div class="troll__left-thigh">

<div class="troll__left-lower-leg">

<div class="troll__left-foot"></div>

</div>

</div>

</div>

</div>

</div>

</div>

<div>

<marquee scrollamount="15" ><h1>"""

script4 = message

script5 = """</h1></marquee><br>

<h1 align="center" font-size="20">"""

script6 = name

"""</h1></div>"""

fo.write(script1)

fo.write(script2)

fo.write(script3)

fo.write(script4)

fo.write(script5)

fo.write(script6)

print "Script Berhasil Di buat!"

print "Kontak : +6281315126056"

fo.close()
