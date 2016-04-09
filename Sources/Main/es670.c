#include "fsl_device_registers.h"
#include "KL25Z/es670_peripheral_board.h"
#include "LedSwi/ledswi_hal.h"
#include "Mcg/mcg_hal.h"
#include "Buzzer/buzzer_hal.h"
#include "SevenSeg/sevenseg_hal.h"
#include "Util/util.h"

static int i = 0;

int main(void)
{
	mcg_clockInit();
	buzzer_init();
	ledswi_initLedSwitch(MAX_LED_SWI,0);
	sevenseg_init();

	seven_segment_seg_type_e on_segments[] = {SEG_A, SEG_B, SEG_C, SEG_D};
	seven_segment_disp_type_e displays[] = {DISP_1, DISP_2, DISP_3, DISP_4};
	while(1){
		for(i=0; i<4; i++) {
			sevenseg_setSegs(4, on_segments);
			sevenseg_setDisp(displays[i]);
			util_genDelay1ms();
			util_genDelay1ms();
			util_genDelay1ms();
		}
	}
    /* Never leave main */
    return 0;
}
