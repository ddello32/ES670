/* ***************************************************************** */
/* File name:        es670_peripheral_board.h                        */
/* File description: Header file containing the peripherals mapping  */
/*                     of the peripheral board for the ES670 hardware*/
/* Author name:      dloubach                                        */
/* Creation date:    16out2015                                       */
/* Revision date:    25fev2016                                       */
/* ***************************************************************** */

#ifndef SOURCES_ES670_PERIPHERAL_BOARD_H_
#define SOURCES_ES670_PERIPHERAL_BOARD_H_

/* system includes */
#include <MKL25Z4.h>
#include "MKL25Z4_extension.h"

/*                 General uC definitions                 */

/* Clock gate control */
#define  CGC_CLOCK_DISABLED         0x00U
#define  CGC_CLOCK_ENABLED          0x01U

/* GPIO DIRECTION    */
#define GPIO_OUTPUT 				0x01U

/*	Workaround for PORT_ID macro expansion to stop at port level*/
typedef int A;
typedef int B;
typedef int C;
typedef int D;
typedef int E;

/*                 END OF General uC definitions         */


/*                 BUZZER Definitions                    */
#define BUZZER_PORT_BASE_PNT        PORTD                                   /* peripheral port base pointer */
#define BUZZER_GPIO_BASE_PNT        PTD                                     /* peripheral gpio base pointer */
#define BUZZER_PORT_ID				D                                       /* peripheral port identifier*/

#define BUZZER_PIT_TIMER_NUMB		1

#define BUZZER_PIN                  0                                      /* buzzer pin */
#define BUZZER_DIR                  kGpioDigitalOutput
#define BUZZER_ALT                  0x01u
/*                 END OF BUZZER definitions             */


/*                 LED and SWITCH Definitions                    */
#define LS_PORT_BASE_PNT            PORTA                                   /* peripheral port base pointer */
#define LS_PORT_ID                  A                                      /* peripheral port identifier*/
#define LS_GPIO_BASE_PNT            PTA                                     /* peripheral gpio base pointer */

/* THIS PIN CONFLICTS WITH PTA1 USED AS UART0_RX IN THE OPENSDA SERIAL DEBUG PORT */
#define LS1_PIN                     1                                      /* led/switch #1 pin */
#define LS1_DIR_OUTPUT              (GPIO_OUTPUT << LS1_PIN)
#define LS1_DIR_INPUT               (GPIO_OUTPUT << LS1_PIN)
#define LS1_ALT                     0x01u                                   /* GPIO alternative */

/* THIS PIN CONFLICTS WITH PTA2 USED AS UART0_TX IN THE OPENSDA SERIAL DEBUG PORT */
#define LS2_PIN                     2                                      /* led/switch #2 pin */
#define LS2_DIR_OUTPUT              (GPIO_OUTPUT << LS2_PIN)
#define LS2_DIR_INPUT               (GPIO_OUTPUT << LS2_PIN)
#define LS2_ALT                     LS1_ALT

#define LS3_PIN                     4                                      /* led/switch #3 pin */
#define LS3_DIR_OUTPUT              (GPIO_OUTPUT << LS3_PIN)
#define LS3_DIR_INPUT               (GPIO_OUTPUT << LS3_PIN)
#define LS3_ALT                     LS1_ALT

#define LS4_PIN                     5                                      /* led/switch #4 pin */
#define LS4_DIR_OUTPUT              (GPIO_OUTPUT << LS4_PIN)
#define LS4_DIR_INPUT               (GPIO_OUTPUT << LS4_PIN)
#define LS4_ALT                     LS1_ALT

/*                 END OF LED and SWITCH definitions             */

/*                 SEVEN SEGMENT DISPLAY Definitions                    */
#define SEV_SEG_PORT_BASE_PNT      PORTC                                   /* peripheral port base pointer */
#define SEV_SEG_PORT_ID            C                                       /* peripheral port identifier*/
#define SEV_SEG_GPIO_BASE_PNT      PTC                                     /* peripheral gpio base pointer */

#define SEV_SEG_PIT_TIMER_NUMB		 0										/* timer number for seven seg PIT */

#define SEGA_PIN                     0                                      /* Segment A*/
#define SEGA_DIR_OUTPUT              (GPIO_OUTPUT << SEGA_PIN)
#define SEGA_ALT                     0x01u                                   /* GPIO alternative */

#define SEGB_PIN                     1
#define SEGB_DIR_OUTPUT              (GPIO_OUTPUT << SEGB_PIN)
#define SEGB_ALT                     SEGA_ALT

#define SEGC_PIN                     2
#define SEGC_DIR_OUTPUT              (GPIO_OUTPUT << SEGC_PIN)
#define SEGC_ALT                     SEGA_ALT

#define SEGD_PIN                     3
#define SEGD_DIR_OUTPUT              (GPIO_OUTPUT << SEGD_PIN)
#define SEGD_ALT                     SEGA_ALT

#define SEGE_PIN                     4
#define SEGE_DIR_OUTPUT              (GPIO_OUTPUT << SEGE_PIN)
#define SEGE_ALT                     SEGA_ALT

#define SEGF_PIN                     5
#define SEGF_DIR_OUTPUT              (GPIO_OUTPUT << SEGF_PIN)
#define SEGF_ALT                     SEGA_ALT

#define SEGG_PIN                     6
#define SEGG_DIR_OUTPUT              (GPIO_OUTPUT << SEGG_PIN)
#define SEGG_ALT                     SEGA_ALT

#define SEGDP_PIN                     7
#define SEGDP_DIR_OUTPUT              (GPIO_OUTPUT << SEGDP_PIN)
#define SEGDP_ALT                     SEGA_ALT

#define SEG_DISP1_PIN                 13
#define SEG_DISP1_DIR_OUTPUT          (GPIO_OUTPUT << SEG_DISP1_PIN)
#define SEG_DISP1_ALT                 SEGA_ALT

#define SEG_DISP2_PIN                 12
#define SEG_DISP2_DIR_OUTPUT          (GPIO_OUTPUT << SEG_DISP2_PIN)
#define SEG_DISP2_ALT                 SEGA_ALT

#define SEG_DISP3_PIN                 11
#define SEG_DISP3_DIR_OUTPUT          (GPIO_OUTPUT << SEG_DISP3_PIN)
#define SEG_DISP3_ALT                 SEGA_ALT

#define SEG_DISP4_PIN                 10
#define SEG_DISP4_DIR_OUTPUT          (GPIO_OUTPUT << SEG_DISP4_PIN)
#define SEG_DISP4_ALT                 SEGA_ALT

/*                 END of SEVEN SEGMENT DISPLAY Definitions                    */


#endif /* SOURCES_ES670_PERIPHERAL_BOARD_H_ */
