/* ***************************************************************** */
/* File name:        ledswi_hal.h                                    */
/* File description: Header file containing the function/methods     */
/*                   prototypes of ledswi.c                          */
/* Author name:      dloubach                                        */
/* Creation date:    09jan2015                                       */
/* Revision date:    13abr2016                                       */
/* ***************************************************************** */

#ifndef SOURCES_LEDSWI_LEDSWI_HAL_H_
#define SOURCES_LEDSWI_LEDSWI_HAL_H_

#define MAX_LED_SWI        04

typedef enum
{
    SWITCH_OFF,
    SWITCH_ON
} switch_status_type_e;

/**
 * As the hardware board was designed with LEDs/Switches sharing
 * 	the same pins, this method configures how many LEDS and switches
 * 	will be available for the application
 * @param cLedNum num of LEDs
 * @param cSwitchNum num of Switches (cLedNum + cSwitchNum <= MAX_LED_SWI)
 */
void ledswi_initLedSwitch(char cLedNum, char cSwitchNum);


/**
 * set the led ON
 * @param cLedNum which LED {1..4}
 */
void ledswi_setLed(char cLedNum);


/**
 * set the led OFF
 * @param cLedNum which LED {1..4}
 */
void ledswi_clearLed(char cLedNum);


/**
 * return the switch status
 * @param cSwitchNum which switch
 * @return If the switch is ON or OFF
 */
switch_status_type_e ledswi_getSwitchStatus(char cSwitchNum);


#endif /* SOURCES_LEDSWI_LEDSWI_HAL_H_ */
