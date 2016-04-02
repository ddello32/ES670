/* ***************************************************************** */
/* File name:        sevenseg_hal.c                                  */
/* File description: File containing the functions/methods           */
/*                   for handling SEVEN SEGMENT DISPLAY              */
/*                    from the peripheral board                      */
/* Author name:      dloubach                                        */
/* Creation date:    12jan2016                                       */
/* Revision date:    25fev2016                                       */
/* ***************************************************************** */

#include "sevenseg_hal.h"
#include "KL25Z/es670_peripheral_board.h"
#include "GPIO/gpio_util.h"


/* ************************************************ */
/* Method name:        sevenseg_init                */
/* Method description: Initialize the seven segment display */
/* Input params:       n/a                          */
/* Output params:      n/a                          */
/* ************************************************ */
void sevenseg_init(void){
	GPIO_UNGATE_PORT(SEV_SEG_PORT_ID);
	GPIO_INIT_PIN(SEV_SEG_PORT_ID, SEGA_PIN, GPIO_OUTPUT);
	GPIO_INIT_PIN(SEV_SEG_PORT_ID, SEGB_PIN, );
	GPIO_INIT_PIN(SEV_SEG_PORT_ID, SEGC_PIN);
	GPIO_INIT_PIN(SEV_SEG_PORT_ID, SEGD_PIN);
	GPIO_INIT_PIN(SEV_SEG_PORT_ID, SEGE_PIN);
	GPIO_INIT_PIN(SEV_SEG_PORT_ID, SEGF_PIN);
	GPIO_INIT_PIN(SEV_SEG_PORT_ID, SEGG_PIN);
	GPIO_INIT_PIN(SEV_SEG_PORT_ID, SEGGP_PIN);

}


/* ************************************************ */
/* Method name:        buzzer_clearBuzz             */
/* Method description: Clear the buzzer             */
/* Input params:       n/a                          */
/* Output params:      n/a                          */
/* ************************************************ */
void buzzer_clearBuzz(void);


/* ************************************************ */
/* Method name:        buzzer_setBuzz               */
/* Method description: Set the buzzer               */
/* Input params:       n/a                          */
/* Output params:      n/a                          */
/* ************************************************ */
void buzzer_setBuzz(void);



#endif /* SOURCES_SEVEN_SEGMENT_HAL_H_ */
