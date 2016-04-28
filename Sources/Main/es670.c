#include "KL25Z/es670_peripheral_board.h"
#include "LedSwi/ledswi_hal.h"
#include "Mcg/mcg_hal.h"
#include "Buzzer/buzzer_hal.h"
#include "SevenSeg/sevenseg_hal.h"
#include "PIT/pit_hal.h"
#include "Util/util.h"
#include "Util/debugUart.h"
#include "Serial/serial_hal.h"
#include "Protocolo/cmdmachine_hal.h"
#include <string.h>

int main(void)
{
	mcg_clockInit();
	ledswi_initLedSwitch(1,3);
	sevenseg_init();
	buzzer_init();
	serial_setConfig();

	char rcvBuffer[100];
	char sndBuffer[100];
	int iCmdSize = 0;
	while(1){
		iCmdSize = serial_recieveBuffer(rcvBuffer, 100);
		if(iCmdSize > 0){
			cmdmachine_interpretCmdBuffer(rcvBuffer, iCmdSize, sndBuffer);
			serial_sendBuffer(sndBuffer, strlen(sndBuffer));
		}
	}
    /* Never leave main */
    return 0;
}
