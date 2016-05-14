#include "KL25Z/es670_peripheral_board.h"
#include "LedSwi/ledswi_hal.h"
#include "Mcg/mcg_hal.h"
#include "Buzzer/buzzer_hal.h"
#include "SevenSeg/sevenseg_hal.h"
#include "PIT/pit_hal.h"
#include "Util/util.h"
#include "Serial/serial_hal.h"
#include "Protocolo/cmdmachine_hal.h"
#include "LCD/lcd_hal.h"
#include "Util/tc_hal.h"
#include "Cooler/cooler_hal.h"
#include <string.h>

/* defines */
#define RCV_BUF_SIZE 100
#define SND_BUF_SIZE 100
#define CYCLIC_EXECUTIVE_PERIOD         100 * 10000 /* 1000000 micro seconds */

/* globals */
volatile unsigned int uiFlagNextPeriod = 0;         /* cyclic executive flag */

/**
 * cyclic executive interrupt service routine
 */
void main_cyclicExecuteIsr(void)
{
    /* set the cyclic executive flag */
    uiFlagNextPeriod = 1;
}


/**
 * Initialize board and periferics
 */
void main_boardInit(){
	mcg_clockInit();
	ledswi_initLedSwitch(1,3);
	serial_initUart();
	lcd_initLcd();
	lcd_dummyText();
	sevenseg_init();
	buzzer_init();
	cooler_initCooler();
}

/**
 * Reads serial comm, interprets received commands and prints output
 */
void main_protocolCheck(){
	static char rcvBuffer[RCV_BUF_SIZE];
	static char sndBuffer[SND_BUF_SIZE];
	int iCmdSize = 0;
	iCmdSize = serial_recieveBuffer(rcvBuffer, RCV_BUF_SIZE);
	if(iCmdSize > 0){
		cmdmachine_interpretCmdBuffer(rcvBuffer, iCmdSize, sndBuffer);
		serial_sendBuffer(sndBuffer, strlen(sndBuffer));
	}
}


int main(void)
{
	main_boardInit();
	cooler_setVelocity(1);

    /* configure cyclic executive interruption */
    tc_installLptmr0(CYCLIC_EXECUTIVE_PERIOD, main_cyclicExecuteIsr);

    /* cooperative cyclic executive main loop */
	while(1){
		main_protocolCheck();

		 /* WAIT FOR CYCLIC EXECUTIVE PERIOD */
		while(!uiFlagNextPeriod);
		uiFlagNextPeriod = 0;

	}
    /* Never leave main */
    return 0;
}
