/* ***************************************************************** */
/* File name:        buzzer_hal.h                                    */
/* File description: Header file containing the functions/methods    */
/*                   interfaces for handling BUZZER from the         */
/*                   peripheral board                                */
/* Author name:      dloubach                                        */
/* Creation date:    12jan2016                                       */
/* Revision date:    25fev2016                                       */
/* ***************************************************************** */

#ifndef SOURCES_BUZZER_HAL_H_
#define SOURCES_BUZZER_HAL_H_

/* ************************************************ */
/* Method name:        buzzer_init                  */
/* Method description: Initialize the buzzer device */
/* Input params:       n/a                          */
/* Output params:      n/a                          */
/* ************************************************ */
void buzzer_init(void);


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

/**
 * Starts the buzzer with the specified period
 *
 * @param period - the period of the buzzer signal, in clock cycles (40MHz)
 */
void buzzer_initPeriodic(unsigned int period);

/**
 * Stops any periodic buzzer signal
 */
void buzzer_stopPeriodic(void);


#endif /* SOURCES_BUZZER_HAL_H_ */
