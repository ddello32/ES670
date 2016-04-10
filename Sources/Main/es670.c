#include "fsl_device_registers.h"
#include "KL25Z/es670_peripheral_board.h"
#include "LedSwi/ledswi_hal.h"
#include "Mcg/mcg_hal.h"
#include "Buzzer/buzzer_hal.h"
#include "SevenSeg/sevenseg_hal.h"
#include "Util/util.h"


int main(void)
{
	mcg_clockInit();
	buzzer_init();
	ledswi_initLedSwitch(3,1);
	sevenseg_init();
	sevenseg_printHex(0xABCDu);
	unsigned short printHex = 1;
	unsigned short ledOn = 1;
	while(1){
		if(ledswi_getSwitchStatus(3) == SWITCH_ON){
			printHex = !printHex;
			ledOn = !ledOn;
			if(printHex){
				sevenseg_printHex(0xABCDu);
			}else{
				sevenseg_printDec(0xABCDu);
			}
			if(ledOn){
				ledswi_setLed(4);
			}else{
				ledswi_clearLed(4);
			}
		}
	}
    /* Never leave main */
    return 0;
}
