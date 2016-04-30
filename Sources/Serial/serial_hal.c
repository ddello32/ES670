/* ***************************************************************** */
/* File name:        serial_hal.c                                    */
/* File description: File containing the functions/methods    		 */
/*                   interfaces for serial communication		     */
/* Author name:      ddello		                                     */
/* Creation date:    27abr2016                                       */
/* Revision date:    27abr2016                                       */
/* ***************************************************************** */

#include "serial_hal.h"
#include "Util/debugUart.h"
#include "KL25Z/es670_peripheral_board.h"

/**
 * Initialize the serial device configuration
 */
void serial_setConfig(void){
	debugUart_init();
}


/**
 * Write buffer content to serial port
 *
 * @param cpBuffer Pointer to the start of the buffer
 * @param uiSize Number of characters to write
 */
void serial_sendBuffer(char *cpBuffer, unsigned int uiSize){
	while(uiSize--){
	    while (!UART0_BRD_S1_TDRE(UART0)){
	    	//Wait for room in the transmission buffer
	    }
	    UART0_D = (*cpBuffer++);
	}
}


/**
 * Receive content from serial port to buffer.
 *
 * This function will read until one of {\n, \0} is found
 *
 * @param cpBuffer Pointer to the start of the buffer
 * @param uiSize Maximum number of characters to be read from serial port
 *
 * @return The number of characters actually read if the successful,
 * 				-1 in case of buffer overRun
 */
int serial_recieveBuffer(char *cpBuffer, unsigned int uiSize){
	int ret = 0;
	while(uiSize--){
		while(!UART0_BRD_S1_RDRF(UART0)){
			//Wait for transmission buffer to be filled
		}
		*cpBuffer = UART0_D;
		ret++;
		//In case of a buffer overRun
		if(UART0_BRD_S1_OR(UART0)){
			//Clear OR flag so we can continue to receive
			UART0_BWR_S1_OR(UART0,1U);
			return -1;
		}

		switch(*cpBuffer){
			case '\n':
			case '\r':
				*(++cpBuffer) = '\0';
			case '\0':
				return ret;
			default:
				cpBuffer++;
		}
	}
	*cpBuffer = '\0';
	return ret;
}
