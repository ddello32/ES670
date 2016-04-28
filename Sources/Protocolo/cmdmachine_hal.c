/* ***************************************************************** */
/* File name:        cmdmachine_hal.c                                */
/* File description: File containing the functions/methods    		 */
/*                   interfaces for protocol command machine		 */
/* Author name:      ddello		                                     */
/* Creation date:    27abr2016                                       */
/* Revision date:    27abr2016                                       */
/* ***************************************************************** */
#include <string.h>
#include <stdio.h>
#include "cmdmachine_hal.h"
#include "LedSwi/ledswi_hal.h"
#include "Buzzer/buzzer_hal.h"
#include "Util/util.h"

#define ERR_STR "ERR\n"
#define ACK_STR "ACK\n"

#define STATE_IDLE 0
#define STATE_LED_CMD 1
#define STATE_BUZZER_CMD 2
#define STATE_SWITCH_CMD 3
#define STATE_ERR 99

static int iState = STATE_IDLE;

//============================================================================
// IDLE STATE MACHINE
//============================================================================
unsigned int handleIdle(char *cpCmdBuffer, unsigned int uiSize, char* cpCmdRes){
	unsigned int uiCounter = 0;
	while(uiCounter < uiSize && iState == STATE_IDLE){
		switch(cpCmdBuffer[uiCounter++]){
			case 'L':
				iState = STATE_LED_CMD;
				break;
			case 'S':
				iState = STATE_SWITCH_CMD;
				break;
			case 'B':
				iState = STATE_BUZZER_CMD;
				break;
			case ' ':
			case '\t':
			case '\r':
			case '\n':
			case '\0':
				break;
			default:
				iState = STATE_ERR;
		}
	}
	return uiCounter;
}

//==========================================================================
// LED CMD STATE MACHINE
//==========================================================================
char parseLedNum(char cLedInput){
	switch(cLedInput){
		case '1':
			return 1;
		case '2':
			return 2;
		case '3':
			return 3;
		case '4':
			return 4;
		default:
			iState = STATE_ERR;
			return -1;
	}
}


unsigned int handleLed(char *cpCmdBuffer, unsigned int uiSize, char* cpCmdRes){
	unsigned int uiCounter = 0;
	char cLedNum = -1;
	void (*fpLedFunction)(char);
	while(uiCounter < uiSize && iState == STATE_LED_CMD){
		switch(cpCmdBuffer[uiCounter++]){
			case 'C':
				cLedNum = parseLedNum(cpCmdBuffer[uiCounter++]);
				fpLedFunction = &ledswi_clearLed;
				break;
			case 'S':
				cLedNum = parseLedNum(cpCmdBuffer[uiCounter++]);
				fpLedFunction = &ledswi_setLed;
				break;
			default:
				iState = STATE_ERR;
		}
	}
	if(cLedNum > 0){
		strcat(cpCmdRes, ACK_STR);
		(*fpLedFunction)(cLedNum);
		iState = STATE_IDLE;
	}
	return uiCounter;
}
//==========================================================================
// SWITCH CMD STATE MACHINE
//==========================================================================
unsigned int handleSwitch(char *cpCmdBuffer, unsigned int uiSize, char* cpCmdRes){
	unsigned int uiCounter = 0;
	char cSwiNum = -1;
	while(uiCounter < uiSize && iState == STATE_SWITCH_CMD){
		switch(cpCmdBuffer[uiCounter++]){
			case '1':
				cSwiNum = 1;
			case '2':
				cSwiNum = 2;
			case '3':
				cSwiNum = 3;
			case '4':
				cSwiNum = 4;
			default:
				cSwiNum = -1;
				iState = STATE_ERR;
		}
		if(cSwiNum > 0){
			strcat(cpCmdRes, ACK_STR);
			if(ledswi_getSwitchStatus(cSwiNum) == SWITCH_ON){
				strcat(cpCmdRes, "O\n");
			}else{
				strcat(cpCmdRes, "C\n");
			}
			iState = STATE_IDLE;
		}
	}
	return uiCounter;
}


//==========================================================================
// BUZZER CMD STATE MACHINE
//==========================================================================
unsigned int getBuzzMs(char *cpCmdBuffer, unsigned int uiSize){
	unsigned int uiMs = -1;
	if(uiSize >= 3){
		if(!sscanf(cpCmdBuffer, "%3u", &uiMs)){
			uiMs = -1;
		}
	}
	return uiMs;
}

int handleBuzzer(char *cpCmdBuffer, unsigned int uiSize, char* cpCmdRes){
	unsigned int uiCounter = 0;
	unsigned int buzzMs = -1;
	if(uiCounter < uiSize){
		buzzMs = getBuzzMs(cpCmdBuffer, uiSize);
	}
	if(buzzMs >= 0){
		strcat(cpCmdRes, ACK_STR);
		buzzer_initPeriodic(0xB18Eu);		//440Hz (Base 20MHz)
		for(int i = 0; i < buzzMs; i++){
			util_genDelay1ms();
		}
		buzzer_stopPeriodic();
		iState = STATE_IDLE;
		while(uiCounter < 3 && cpCmdBuffer[uiCounter] >= '0' && cpCmdBuffer[uiCounter] <= '9'){
			uiCounter++;
		}
	}else{
		iState = STATE_ERR;
	}
	return uiCounter;
}

//============================================================================
// ERROR STATE MACHINE
//============================================================================
int handleError(char *cpCmdBuffer, unsigned int uiSize, char* cpCmdRes){
	int uiCounter = 0;
	while(uiCounter < uiSize && iState == STATE_ERR){
		switch(cpCmdBuffer[uiCounter++]){
			case ' ':
			case '\t':
			case '\r':
			case '\n':
			case '\0':
				iState = STATE_IDLE;
				break;
			default:
				break;
		}
	}
	strcat(cpCmdRes, ERR_STR);
	return uiCounter;
}


/**
 * Interpret all commands in the given command buffer.
 * Will trigger the command execution an format an output string for printing
 * Ignores blanks (\r,\n, ,\t,\0) between commands.
 *
 * For each valid command, the string ACK will be concatenated to the response string
 * followed by a line-break and the command response (if any).
 *
 * If invalid command syntax is found ERR will be concatenated to the response string
 * and all the characters before the next blank (\r,\n, ,\t,\0) will be ignored.
 *
 * @param cpCmdBuffer Pointer to command buffer
 * @param uiSize Size of the command buffer
 * @param cpCmdRes Pointer for response string.
 *
 * @after cpCmdRes with the response string for this cmdBuffer,
 * 				this will contain a ACK for each valid commmand in the cmdBuffer
 * 				followed by a line break and the command output (if any).
 * 				If an invalid command syntax is found the output string will contain
 * 				an ERR\n for that command and all characters before the next blank
 * 				(\r,\n, ,\t,\0) will be ignored.
 */
void cmdmachine_interpretCmdBuffer(char *cpCmdBuffer, unsigned int uiSize, char* cpCmdRes){
	iState = STATE_IDLE;
	*cpCmdRes = '\0';	//Start response as an empty string.
	unsigned int uiCounter = 0;
	while(uiCounter < uiSize){
		switch(iState){
			case STATE_IDLE:
				uiCounter += handleIdle(&cpCmdBuffer[uiCounter], uiSize - uiCounter, cpCmdRes);
				break;
			case STATE_LED_CMD:
				uiCounter += handleLed(&cpCmdBuffer[uiCounter], uiSize - uiCounter, cpCmdRes);
				break;
			case STATE_SWITCH_CMD:
				uiCounter += handleSwitch(&cpCmdBuffer[uiCounter], uiSize - uiCounter, cpCmdRes);
				break;
			case STATE_ERR:
				uiCounter += handleError(&cpCmdBuffer[uiCounter], uiSize - uiCounter, cpCmdRes);
				break;
		}
	}
}
