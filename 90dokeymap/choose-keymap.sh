#!/bin/sh 

chooseKeymap() {
	if [ $dokeymap -eq 1 ]; then
		cat "/lib/keymaps/keymapList"
		read -t 10 -p '<< Load keymap (Enter for default): ' keymap
		case ${keymap} in
				1|azerty) keymap=azerty ;;
				2|be) keymap=be ;;
				3|bepo) keymap=bepo ;;
				4|bg) keymap=bg ;;
				5|br-a) keymap=br-a ;;
				6|br-l) keymap=br-l ;;
				7|by) keymap=by ;;
				8|cf) keymap=cf ;;
				9|colemak) keymap=colemak ;;
				10|croat) keymap=croat ;;
				11|cz) keymap=cz ;;
				12|de) keymap=de ;;
				13|dk) keymap=dk ;;
				14|dvorak) keymap=dvorak ;;
				15|es) keymap=es ;;
				16|et) keymap=et ;;
				17|fi) keymap=fi ;;
				18|fr) keymap=fr ;;
				19|gr) keymap=gr ;;
				20|hu) keymap=hu ;;
				21|il) keymap=il ;;
				22|is) keymap=is ;;
				23|it) keymap=it ;;
				24|jp) keymap=jp ;;
				25|la) keymap=la ;;
				26|lt) keymap=lt ;;
				27|mk) keymap=mk ;;
				28|nl) keymap=nl ;;
				29|no) keymap=no ;;
				30|pl) keymap=pl ;;
				31|pt) keymap=pt ;;
				32|ro) keymap=ro ;;
				33|ru) keymap=ru ;;
				34|se) keymap=se ;;
				35|sf|ch*) keymap=sf ;;
				36|sg) keymap=sg ;;
				37|sk-y) keymap=sk-y ;;
				38|sk-z) keymap=sk-z ;;
				39|slovene) keymap=slovene ;;
				40|trf) keymap=trf ;;
				41|ua) keymap=ua ;;
				42|uk) keymap=uk ;;
				43|us) keymap=us ;;
				44|wangbe) keymap=wangbe ;;
			esac
		if [ -e /lib/keymaps/${keymap}.map ]; then
			info "Loading the keymap..."
			busybox loadkmap < /lib/keymaps/${keymap}.map
			mkdir -p /etc/sysconfig
			echo "XKEYBOARD=${keymap}" > /etc/sysconfig/keyboard
		elif [ -z "${keymap}" ]
		then
			info "Keeping default keymap"
		else
			info "Sorry, but keymap '${keymap}' is invalid!"
			unset keymap
			chooseKeymap
		fi
	fi
}

chooseKeymap
