#include "fsl_device_registers.h"
#include "Mcg/mcg_hal.h"
#include "Buzzer/buzzer_hal.h"
#include "Util/util.h"

static int i = 0;

int main(void)
{
	mcg_clockInit();
	buzzer_init();

    while(1) {
    	buzzer_setBuzz();
    	util_genDelay1ms();
    	buzzer_clearBuzz();
    	util_genDelay1ms();
    	util_genDelay1ms();
    	util_genDelay1ms();
    	util_genDelay1ms();
    	util_genDelay1ms();
    	util_genDelay1ms();
    	util_genDelay1ms();
    	util_genDelay1ms();
    }
    /* Never leave main */
    return 0;
}
