#include "fsl_device_registers.h"
#include "KL25Z/es670_peripheral_board.h"
#include "LedSwi/ledswi_hal.h"
#include "Mcg/mcg_hal.h"
#include "Buzzer/buzzer_hal.h"
#include "Util/util.h"

static int i = 0;

int main(void)
{
	mcg_clockInit();
	ledswi_initLedSwitch(MAX_LED_SWI,0);

	while(1){
		for(i=1; i<=MAX_LED_SWI; i++) {
			ledswi_setLed(i);
			util_genDelay10ms();
			util_genDelay10ms();
			util_genDelay10ms();
			util_genDelay10ms();
			util_genDelay10ms();
			util_genDelay10ms();
			util_genDelay10ms();
			util_genDelay10ms();
			util_genDelay10ms();
			util_genDelay10ms();
			util_genDelay10ms();
			ledswi_clearLed(i);
		}
	}
    /* Never leave main */
    return 0;
}
