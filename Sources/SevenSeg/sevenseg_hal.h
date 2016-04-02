/* ***************************************************************** */
/* File name:        sevenseg_hal.h                                  */
/* File description: Header file containing the functions/methods    */
/*                   interfaces for handling SEVEN SEGMENT DISPLAY   */
/*                    from the peripheral board                      */
/* Author name:      dloubach                                        */
/* Creation date:    12jan2016                                       */
/* Revision date:    25fev2016                                       */
/* ***************************************************************** */

#ifndef SOURCES_SEVEN_SEGMENT_HAL_H_
#define SOURCES_SEVEN_SEGMENT_HAL_H_

/* ************************************************ */
/* Method name:        sevenseg_init                */
/* Method description: Initialize the seven segment display */
/* Input params:       n/a                          */
/* Output params:      n/a                          */
/* ************************************************ */
void sevenseg_init(void);


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
