/* ***************************************************************** */
/* File name:        cooler_hal.c                                    */
/* File description: File containing the functions/methods   		 */
/*                   for cooler control	  						     */
/* Author name:      ddello		                                     */
/* Creation date:    13maio2016                                      */
/* Revision date:    13maio2016                                      */
/* ***************************************************************** */

#include "cooler_hal.h"
#include "KL25Z/es670_peripheral_board.h"
#include "GPIO/gpio_hal.h"


/**
 * Initialize the cooler module
 */
void cooler_initCooler(void){
	GPIO_UNGATE_PORT(COOLER_PORT_ID);
	GPIO_INIT_PIN(COOLER_PORT_ID, COOLER_PIN, COOLER_PIN_DIR);
}


/**
 * Set the cooler velocity
 *
 * @param ucVelocity Cooler velocity from 0 (stopped) to 255 (max)
 */
void cooler_setVelocity(unsigned char ucVelocity){
	if(ucVelocity){
		GPIO_WRITE_PIN(COOLER_PORT_ID, COOLER_PIN, GPIO_HIGH);
	}else{
		GPIO_WRITE_PIN(COOLER_PORT_ID, COOLER_PIN, GPIO_LOW);
	}
}
