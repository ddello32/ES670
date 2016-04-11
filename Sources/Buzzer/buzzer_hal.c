/* ***************************************************************** */
/* File name:        buzzer_hal.c                                    */
/* File description: File dedicated to the hardware abstraction layer*/
/*                   related buzzer from the peripheral board        */
/* Author name:      dloubach                                        */
/* Creation date:    12jan2016                                       */
/* Revision date:    25fev2016                                       */
/* ***************************************************************** */

#include "GPIO/gpio_hal.h"
#include "buzzer_hal.h"
#include "KL25Z/es670_peripheral_board.h"
#include "PIT/pit_hal.h"

/* ************************************************ */
/* Method name:        buzzer_init                  */
/* Method description: Initialize the buzzer device */
/* Input params:       n/a                          */
/* Output params:      n/a                          */
/* ************************************************ */
void buzzer_init(void)
{
	GPIO_UNGATE_PORT(BUZZER_PORT_ID);
	GPIO_INIT_PIN(BUZZER_PORT_ID, BUZZER_PIN, GPIO_OUTPUT);
	pit_enable();
}



/* ************************************************ */
/* Method name:        buzzer_clearBuzz             */
/* Method description: Clear the buzzer             */
/* Input params:       n/a                          */
/* Output params:      n/a                          */
/* ************************************************ */
void buzzer_clearBuzz(void)
{
    GPIO_WRITE_PIN(BUZZER_PORT_ID, BUZZER_PIN, GPIO_LOW);
}



/* ************************************************ */
/* Method name:        buzzer_setBuz                */
/* Method description: Set the buzzer               */
/* Input params:       n/a                          */
/* Output params:       n/a                         */
/* ************************************************ */
void buzzer_setBuzz(void)
{
	GPIO_WRITE_PIN(BUZZER_PORT_ID, BUZZER_PIN, GPIO_HIGH);
}

/**
 * Handler for buzzer interruptions
 */
void _buzzer_interrupt_handler(void){
	buzzer_setBuzz();
	buzzer_clearBuzz();
	pit_mark_interrupt_handled(BUZZER_PIT_TIMER_NUMB);
}

/**
 * Starts the buzzer with the specified period
 *
 * @param period - the period of the buzzer signal, in clock cycles (40MHz)
 */
void buzzer_initPeriodic(unsigned int period){
	//Init timer 1
	pit_start_timer_interrupt(BUZZER_PIT_TIMER_NUMB, period, &_buzzer_interrupt_handler);
}

/**
 * Stops any periodic buzzer signal
 */
void buzzer_stopPeriodic(void){
	pit_stop_timer_interrupt(BUZZER_PIT_TIMER_NUMB);
}
