/* ***************************************************************** */
/* File name:        pit_hal.h                                       */
/* File description: Header file containing the functions/methods    */
/*                  interfaces for handling the Periodic Interruption*/
/*                  timer module                                	 */
/* Author name:      ddello	                                         */
/* Creation date:    10abr2016                                       */
/* Revision date:    10abr2016                                       */
/* ***************************************************************** */

#ifndef SOURCES_PIT_PIT_HAL_H_
#define SOURCES_PIT_PIT_HAL_H_

/**
 * Enables Periodic Interruption Timer module.
 * (With the stop on debug flag set to on)
 */
void pit_enable(void);

/**
 * Start interruptions for given timer, unchained mode.
 *
 * @param timer_number 	The number for the desired timer (0,1)
 * @param timer_period  The number of bus_clock cycles between interrupts
 * @param handler   	Timer interrupt handler routine address pointer
 */
void pit_start_timer_interrupt(unsigned short timer_numb, unsigned int timer_period, void (*interrupt_handler)(void));

/**
 * Stop interruptions for given timer, unchained mode.
 *
 * @param timer_number 	The number for the desired timer (0,1)
 */
void pit_stop_timer_interrupt(unsigned short timer_numb);

/**
 * Mark interruption as handled for the given timer, this should be called by timer
 * interruption handlers once they are finished.
 *
 * @param timer_number 	The number for the desired timer (0,1)
 */
void pit_mark_interrupt_handled(unsigned short timer_numb);
#endif /* SOURCES_PIT_PIT_HAL_H_ */
