#include "KL25Z/es670_peripheral_board.h"
#include "LedSwi/ledswi_hal.h"
#include "Mcg/mcg_hal.h"
#include "Buzzer/buzzer_hal.h"
#include "SevenSeg/sevenseg_hal.h"
#include "PIT/pit_hal.h"
#include "Util/util.h"
#include "Util/debugUart.h"
#include "fsl_debug_console.h"

int main(void)
{
	mcg_clockInit();
	ledswi_initLedSwitch(1,3);
	sevenseg_init();
	buzzer_init();
	debugUart_init();

	unsigned int uiReceiveBuff;
	sevenseg_printHex(0xABCDu);
	buzzer_initPeriodic(0xB18Eu);		//440Hz (Base 20MHz)
	ledswi_setLed(4);
	while(1){
		if(UART0_BRD_S1_RDRF(UART0)){
			uiReceiveBuff = GETCHAR();
			PUTCHAR(uiReceiveBuff);
		}

		if(ledswi_getSwitchStatus(3) == SWITCH_OFF || ledswi_getSwitchStatus(2) == SWITCH_OFF || ledswi_getSwitchStatus(1) == SWITCH_OFF){
			ledswi_setLed(0x4);
		}else{
			ledswi_clearLed(0x4);
		}
	}
    /* Never leave main */
    return 0;
}
