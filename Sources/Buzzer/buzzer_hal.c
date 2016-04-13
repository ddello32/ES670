/* ***************************************************************** */
/* File name:        buzzer_hal.c                                    */
/* File description: File dedicated to the hardware abstraction layer*/
/*                   related buzzer from the peripheral board        */
/* Author name:      dloubach                                        */
/* Creation date:    12jan2016                                       */
/* Revision date:    13abr2016                                       */
/* ***************************************************************** */

#include "GPIO/gpio_hal.h"
#include "buzzer_hal.h"
#include "KL25Z/es670_peripheral_board.h"
#include "PIT/pit_hal.h"

/**
 * Initialize the buzzer device
 */
void buzzer_init(void)
{
	GPIO_UNGATE_PORT(BUZZER_PORT_ID);
	GPIO_INIT_PIN(BUZZER_PORT_ID, BUZZER_PIN, GPIO_OUTPUT);
	pit_enable();
}



/**
 * Clear the buzzer
 */
void buzzer_clearBuzz(void)
{
    GPIO_WRITE_PIN(BUZZER_PORT_ID, BUZZER_PIN, GPIO_LOW);
}



/**
 * Set the buzzer
 */
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
 * @param uiPeriod The period of the buzzer signal, in clock cycles (40MHz)
 */
void buzzer_initPeriodic(unsigned int uiPeriod){
	//Init timer 1
	pit_start_timer_interrupt(BUZZER_PIT_TIMER_NUMB, uiPeriod, &_buzzer_interrupt_handler);
}

/**
 * Stops any periodic buzzer signal
 */
void buzzer_stopPeriodic(void){
	pit_stop_timer_interrupt(BUZZER_PIT_TIMER_NUMB);
}
