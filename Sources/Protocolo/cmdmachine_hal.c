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
/**
 * Handles parsing while in IDLE state and checks for transitions
 *
 * @param cpCmdBuffer The start of the command string to parse
 * @param uiSize The size of the command string
 * @param cpCmdRes Buffer for concatenating the commmand response
 *
 * @return The number of characters parsed while in the IDLE state
 */
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
/**
 * Parses character ledNumberReference into a led number
 *
 * @param ccLedInput Character between '1' and '4' refering to the desired
 * 						led number
 *
 * @return Led number reference (number between 1 and 4) or -1 in case of invalid
 * 				input
 */
ledswi_pin_type_e parseLedNum(char cLedInput){
	switch(cLedInput){
		case '1':
			return LS_1;
		case '2':
			return LS_2;
		case '3':
			return LS_3;
		case '4':
			return LS_4;
		default:
			iState = STATE_ERR;
			return UNKNOWN;
	}
}

/**
 * Handles parsing while in LED_COMMAND state and checks for transitions
 *
 * @param cpCmdBuffer The start of the command string to parse
 * @param uiSize The size of the command string
 * @param cpCmdRes Buffer for concatenating the command response
 *
 * @return The number of characters parsed while in the LED_COMMAND state
 */
unsigned int handleLed(char *cpCmdBuffer, unsigned int uiSize, char* cpCmdRes){
	unsigned int uiCounter = 0;
	ledswi_pin_type_e eLedNum = UNKNOWN;
	void (*fpLedFunction)(ledswi_pin_type_e);
	while(uiCounter < uiSize && iState == STATE_LED_CMD){
		switch(cpCmdBuffer[uiCounter++]){
			case 'C':
				eLedNum = parseLedNum(cpCmdBuffer[uiCounter++]);
				fpLedFunction = &ledswi_clearLed;
				break;
			case 'S':
				eLedNum = parseLedNum(cpCmdBuffer[uiCounter++]);
				fpLedFunction = &ledswi_setLed;
				break;
			case 'R':
				eLedNum = parseLedNum(cpCmdBuffer[uiCounter++]);
				if(eLedNum != UNKNOWN){
					strcat(cpCmdRes, ACK_STR);
					ledswi_setLed(eLedNum);
					if(ledswi_getLedStatus(eLedNum) == LED_ON){
						strcat(cpCmdRes, "O\n");
					}else{
						strcat(cpCmdRes, "C\n");
					}
					iState = STATE_IDLE;
				}else{
					iState = STATE_ERR;
				}
				return uiCounter;
				break;
			default:
				iState = STATE_ERR;
		}
	}
	if(eLedNum != UNKNOWN){
		strcat(cpCmdRes, ACK_STR);
		ledswi_initLed(eLedNum);
		(*fpLedFunction)(eLedNum);
		iState = STATE_IDLE;
	}else{
		iState = STATE_ERR;
	}
	return uiCounter;
}
//==========================================================================
// SWITCH CMD STATE MACHINE
//==========================================================================
/**
 * Handles parsing while in SWITCH_COMMAND state and checks for transitions
 *
 * @param cpCmdBuffer The start of the command string to parse
 * @param uiSize The size of the command string
 * @param cpCmdRes Buffer for concatenating the command response
 *
 * @return The number of characters parsed while in the SWITCH_COMMAND state
 */
unsigned int handleSwitch(char *cpCmdBuffer, unsigned int uiSize, char* cpCmdRes){
	unsigned int uiCounter = 0;
	ledswi_pin_type_e eSwiNum = UNKNOWN;
	while(uiCounter < uiSize && iState == STATE_SWITCH_CMD){
		switch(cpCmdBuffer[uiCounter++]){
			case '1':
				eSwiNum = LS_1;
				break;
			case '2':
				eSwiNum = LS_2;
				break;
			case '3':
				eSwiNum = LS_3;
				break;
			case '4':
				eSwiNum = LS_4;
				break;
			default:
				eSwiNum = UNKNOWN;
				break;
		}
		if(eSwiNum !=  UNKNOWN){
			strcat(cpCmdRes, ACK_STR);
			ledswi_initSwitch(eSwiNum);
			if(ledswi_getSwitchStatus(eSwiNum) == SWITCH_ON){
				strcat(cpCmdRes, "O\n");
			}else{
				strcat(cpCmdRes, "C\n");
			}
			iState = STATE_IDLE;
		}else{
			iState = STATE_ERR;
		}
	}
	return uiCounter;
}


//==========================================================================
// BUZZER CMD STATE MACHINE
//==========================================================================
/**
 * Parses Buzzer command milliseconds input into integer
 *
 * @param cpCmdBuffer The start of the Buzzer command milliseconds input string
 *
 * @return The parsed number of milliseconds contained in the start of the command
 * 				string or -1 in case of parsing failure
 */
int getBuzzMs(char *cpCmdBuffer){
	int iMs = -1;
	if(!sscanf(cpCmdBuffer, "%3d", &iMs)){
		iMs = -1;
	}
	return iMs;
}

/**
 * Handles parsing while in BUZZER_COMMAND state and checks for transitions
 *
 * @param cpCmdBuffer The start of the command string to parse
 * @param uiSize The size of the command string
 * @param cpCmdRes Buffer for concatenating the command response
 *
 * @return The number of characters parsed while in the BUZZER_COMMAND state
 */
int handleBuzzer(char *cpCmdBuffer, unsigned int uiSize, char* cpCmdRes){
	unsigned int uiCounter = 0;
	int iBuzzMs = -1;
	if(uiCounter < uiSize){
		iBuzzMs = getBuzzMs(cpCmdBuffer);
	}
	if(iBuzzMs >= 0){
		strcat(cpCmdRes, ACK_STR);
		buzzer_initPeriodic(440, iBuzzMs);		//440Hz
		iState = STATE_IDLE;
		//Exactly how many characters where read.
		while(uiCounter < 3 && uiCounter < uiSize && cpCmdBuffer[uiCounter] >= '0' && cpCmdBuffer[uiCounter] <= '9'){
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
/**
 * Handles parsing while in ERR state and checks for transitions
 *
 * @param cpCmdBuffer The start of the command string to parse
 * @param uiSize The size of the command string
 * @param cpCmdRes Buffer for concatenating the command response
 *
 * @return The number of characters parsed while in the ERR state
 */
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
			case STATE_BUZZER_CMD:
				uiCounter += handleBuzzer(&cpCmdBuffer[uiCounter], uiSize - uiCounter, cpCmdRes);
				break;
			case STATE_ERR:
				uiCounter += handleError(&cpCmdBuffer[uiCounter], uiSize - uiCounter, cpCmdRes);
				break;
		}
	}
}
