/* ***************************************************************** */
/* File name:        pit_hal.c                                       */
/* File description: File containing the functions/methods 		     */
/*                   for handling the Periodic Interruption  		 */
/*                   Timer module                                	 */
/* Author name:      ddello	                                         */
/* Creation date:    10abr2016                                       */
/* Revision date:    10abr2016                                       */
/* ***************************************************************** */
//Careful when handling PIT DOC! Bit endianness is inverted in relation to GPIO doc

#include "fsl_interrupt_manager.h"
#include "pit_hal.h"

#define PIT_IRQ_NUMBER PIT_IRQn

/**
 *Default timer interruption handler. Does nothing.
 */
static void _nop_handler(void){}

static void (*timer0Handler)(void) = &_nop_handler;
static void (*timer1Handler)(void) = &_nop_handler;

/**
 * Pit interruption handler. Checks what timer caused the interruption and call the
 * correct timer interruption handler.
 */
void _PIT_IRQHandler(void){
	if(PIT_TFLG0){
		(*timer0Handler)();
	}
	if(PIT_TFLG1){
		(*timer1Handler)();
	}
}

/**
 * Enables Periodic Interruption Timer module.
 * (With the stop on debug flag set to on)
 */
void pit_enable(void){
	PIT_MCR &= ~PIT_MCR_MDIS(0x1u);
	//Freeze in debug mode
	PIT_MCR |= PIT_MCR_FRZ(0x1u);
	INT_SYS_InstallHandler(PIT_IRQ_NUMBER, &_PIT_IRQHandler);
	INT_SYS_EnableIRQ(PIT_IRQ_NUMBER);
}

/**
 * Start interruptions for given timer, unchained mode.
 *
 * @param timer_number 	The number for the desired timer (0,1)
 * @param timer_period  The number of bus_clock cycles between interrupts
 * @param handler   	Timer interrupt handler routine address pointer
 */
void pit_start_timer_interrupt(unsigned short timer_numb, unsigned int timer_period, void (*interrupt_handler)(void)){
	if(!timer_numb){
		timer0Handler = interrupt_handler;
		PIT_LDVAL0 = PIT_LDVAL_TSV(timer_period);
		PIT_TCTRL0 &= ~PIT_TCTRL_CHN(0x1u);		/*Disable chain mode*/
		PIT_TCTRL0 |= PIT_TCTRL_TIE(0x1u);		/*Enable interrupts for timer 0*/
		PIT_TCTRL0 |= PIT_TCTRL_TEN(0x1u);		/*Enable timer 0*/
	}else{
		timer1Handler = interrupt_handler;
		PIT_LDVAL1 = PIT_LDVAL_TSV(timer_period);
		PIT_TCTRL1 &= ~PIT_TCTRL_CHN(0x1u);		/*Disable chain mode*/
		PIT_TCTRL1 |= PIT_TCTRL_TIE(0x1u);		/*Enable interrupts for timer 1*/
		PIT_TCTRL1 |= PIT_TCTRL_TEN(0x1u);		/*Enable timer 1*/
	}
}

/**
 * Stop interruptions for given timer, unchained mode.
 *
 * @param timer_number 	The number for the desired timer (0,1)
 */
void pit_stop_timer_interrupt(unsigned short timer_numb){
	if(!timer_numb){
		PIT_TCTRL0 &= ~PIT_TCTRL_TIE(0x1u);
		PIT_TCTRL0 &= ~PIT_TCTRL_TEN(0x1u);
	}else{
		PIT_TCTRL1 &= ~PIT_TCTRL_TIE(0x1u);
		PIT_TCTRL1 &= ~PIT_TCTRL_TEN(0x1u);
	}
}

/**
 * Mark interruption as handled for the given timer, this should be called by timer
 * interruption handlers once they are finished.
 *
 * @param timer_number 	The number for the desired timer (0,1)
 */
void pit_mark_interrupt_handled(unsigned short timer_numb){
	if(!timer_numb){
		PIT_TFLG0 |= PIT_TFLG_TIF(0x1u);
	}else{
		PIT_TFLG1 |= PIT_TFLG_TIF(0x1u);
	}
}
