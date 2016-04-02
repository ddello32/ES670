/* ***************************************************************** */
/* File name:        gpio_util.h                                     */
/* File description: This file has a couple of useful macros to      */
/*                   control and init the GPIO pins from the KLM25Z  */
/* Author name:      ddello                                          */
/* Creation date:    01abr2016                                       */
/* Revision date:    01abr2016                                       */
/* ***************************************************************** */

#ifndef SOURCES_GPIO_GPIO_UTIL_H_
#define SOURCES_GPIO_GPIO_UTIL_H_

#include "KL25Z/es670_peripheral_board.h"

#define GPIO_HIGH 1
#define GPIO_LOW  0

/* **************************************************  */
/* Macro name:        GPIO_UNGATE_PORT                 */
/* Macro description: Ungates the clock for a gpio port*/
/* Input params:       PORT_ID = the GPIO port         */
/*                                        id(A,B)      */
/* Output params:       n/a                            */
/* **************************************************  */
#define GPIO_UNGATE_PORT(PORT_ID)\
	__GPIO_UNGATE_PORT(PORT_ID)

#define __GPIO_UNGATE_PORT(PORT_ID)\
	/* un-gate port clock*/\
    SIM_SCGC5 = SIM_SCGC5_PORT ## PORT_ID ##(CGC_CLOCK_ENABLED)

/* ************************************************** */
/* Macro name:        GPIO_INIT_PIN                   */
/* Macro description: inits a pin as GPIO in the      */
/*                     given direction                */
/* Input params:       PORT_ID = the GPIO port        */
/*                                        id(A,B)     */
/*                     PIN_NUM = pin number in port   */
/*                     DIR = pin direction            */
/*                           (GPIO_INPUT, GPIO_OUTPUT)*/
/* Output params:       n/a                           */
/* ************************************************** */
#define GPIO_INIT_PIN(PORT_ID, PIN_NUM, DIR)\
    __GPIO_INIT_PIN(PORT_ID, PIN_NUM, DIR)

#define __GPIO_INIT_PIN(PORT_ID, PIN_NUM, DIR)\
    /* set pin as gpio */\
    PORT ## PORT_ID ## _PCR ## PIN_NUM ## = PORT_PCR_MUX(GPIO_MUX_ALT);\
    /* Set pin direction */\
    if(DIR){\
    	GPIOA_PDDR |= GPIO_PDDR_PDD(0x01 << PIN_NUM);\
    }else{\
    	GPIOA_PDDR &= ~GPIO_PDDR_PDD(0x01 << PIN_NUM);\
    }

/* *************************************************** */
/* Macro name:        GPIO_WRITE_PIN                   */
/* Macro description: Writes a pin with the given value*/
/* Input params:       PORT_ID = the GPIO port         */
/*                                        id(A,B)      */
/*                     PIN_NUM = pin number in port    */
/*                     VAL = pin value                 */
/*                           (GPIO_HIGH, GPIO_LOW)     */
/* Output params:       n/a                            */
/* *************************************************** */
#define GPIO_SET_PIN(PORT_ID, PIN_NUM, VAL)\
    __GPIO_SET_PIN(PORT_ID, PIN_NUM, DIR)

#define __GPIO_SET_PIN(PORT_ID, PIN_NUM, VAL)\
	if(VAL){\
		GPIO ## PORT_ID ## _PSOR = GPIO_P ## VAL ## R_PTSO( (0x01U << PIN_NUM) )\
	}\else{\
		GPIO ## PORT_ID ## _PCOR = GPIO_P ## VAL ## R_PTCO( (0x01U << PIN_NUM) )\
	}

/* *************************************************** */
/* Macro name:        GPIO_READ_PIN                    */
/* Macro description: Reads the status of a GPIO PIN   */
/* Input params:       PORT_ID = the GPIO port         */
/*                                        id(A,B)      */
/*                     PIN_NUM = pin number in port    */
/*                     VAL = pin value                 */
/*                           (GPIO_HIGH, GPIO_LOW)     */
/* Output params:       n/a                            */
/* *************************************************** */
#define GPIO_READ_PIN(PORT_ID, PIN_NUM)\
    __GPIO_READ_PIN(PORT_ID, PIN_NUM)

#define __GPIO_READ_PIN(PORT_ID, PIN_NUM)\
		((GPIO ## PORD_ID ## _PDIR & (0x01u << PIN_NUM)) >> PIN_NUM) )

#endif /* SOURCES_LEDSWI_LEDSWI_HAL_H_ */
