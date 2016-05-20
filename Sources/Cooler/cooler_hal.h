/* ***************************************************************** */
/* File name:        cooler_hal.h                                    */
/* File description: Header file containing the functions/methods    */
/*                   interfaces for cooler control	  			     */
/* Author name:      ddello		                                     */
/* Creation date:    13maio2016                                      */
/* Revision date:    13maio2016                                      */
/* ***************************************************************** */

#ifndef SOURCES_COOLER_HAL_H_
#define SOURCES_COOLER_HAL_H_

#include <stdint.h>

/**
 * Initialize the cooler module
 */
void cooler_initCooler(void);


/**
 * Set the cooler velocity
 *
 * @param uiVelocity Cooler velocity from 0 (stopped) to 0xFFFF (max)
 */
void cooler_setVelocity(uint16_t uiVelocity);

#endif /* SOURCES_COOLER_HAL_H_ */
