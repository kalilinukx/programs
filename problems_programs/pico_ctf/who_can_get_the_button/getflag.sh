#/!bin/bash
curl -s  -X POST http://2018shell.picoctf.com:65107/button2.php| grep -oE "picoCTF{.*}" --color=none
#picoCTF{button_button_whose_got_the_button_91f6f39a}
