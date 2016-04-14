/* ***************************************************************** */
/* File name:        pit_hal.c                                       */
/* File description: File containing the functions/methods 		     */
/*                   for handling the Periodic Interruption  		 */
/*                   Timer module                                	 */
/* Author name:      ddello	                                         */
/* Creation date:    10abr2016                                       */
/* Revision date:    13abr2016                                       */
/* ***************************************************************** */
//Careful when handling PIT DOC! Bit endianness is inverted in relation to GPIO doc

#include "pit_hal.h"
#include "KL25Z/es670_peripheral_board.h"

#define PIT_IRQ_NUMBER PIT_IRQn

/**
 *Default timer interruption handler. Does nothing.
 */
static void _nop_handler(void){
	PIT_TFLG0 |= PIT_TFLG_TIF(0x1u);
	PIT_TFLG1 |= PIT_TFLG_TIF(0x1u);
}

static void (*fpTimer0Handler)(void) = &_nop_handler;
static void (*fpTimer1Handler)(void) = &_nop_handler;

/**
 * Pit interruption handler. Checks what timer caused the interruption and call the
 * correct timer interruption handler.
 */
void PIT_IRQHandler(void){
	if(PIT_TFLG0){
		(*fpTimer0Handler)();
	}
	if(PIT_TFLG1){
		(*fpTimer1Handler)();
	}
}

/**
 * Enables Periodic Interruption Timer module.
 * (With the stop on debug flag set to on)
 */
void pit_enable(void){
	SIM_SCGC6 |= SIM_SCGC6_PIT_MASK;
	PIT_MCR &= ~PIT_MCR_MDIS(0x1u);
	//Freeze in debug mode
	PIT_MCR |= PIT_MCR_FRZ(0x1u);
	NVIC_ClearPendingIRQ(PIT_IRQ_NUMBER);
    NVIC_EnableIRQ(PIT_IRQ_NUMBER);
}

/**
 * Start interruptions for given timer, unchained mode.
 * Timer interruptions are masked.
 *
 * @param usTimer_numb 	The number for the desired timer (0,1)
 * @param uiTimer_period  The number of bus_clock cycles between interrupts
 * @param fpInterrupt_handler   	Timer interrupt handler routine address pointer
 */
void pit_start_timer_interrupt(unsigned short usTimer_numb, unsigned int uiTimer_period, void (*fpInterrupt_handler)(void)){
	if(!usTimer_numb){
		fpTimer0Handler = fpInterrupt_handler;
		PIT_LDVAL0 = PIT_LDVAL_TSV(uiTimer_period);
		PIT_TCTRL0 &= ~PIT_TCTRL_CHN(0x1u);		/*Disable chain mode*/
		PIT_TCTRL0 |= PIT_TCTRL_TIE(0x1u);		/*Enable interrupts for timer 0*/
		PIT_TCTRL0 |= PIT_TCTRL_TEN(0x1u);		/*Enable timer 0*/
	}else{
		fpTimer1Handler = fpInterrupt_handler;
		PIT_LDVAL1 = PIT_LDVAL_TSV(uiTimer_period);
		PIT_TCTRL1 &= ~PIT_TCTRL_CHN(0x1u);		/*Disable chain mode*/
		PIT_TCTRL1 |= PIT_TCTRL_TIE(0x1u);		/*Enable interrupts for timer 1*/
		PIT_TCTRL1 |= PIT_TCTRL_TEN(0x1u);		/*Enable timer 1*/
	}
}

/**
 * Stop interruptions for given timer, unchained mode.
 *
 * @param usTimer_numb 	The number for the desired timer (0,1)
 */
void pit_stop_timer_interrupt(unsigned short usTimer_numb){
	if(!usTimer_numb){
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
 * @param usTimer_numb 	The number for the desired timer (0,1)
 */
void pit_mark_interrupt_handled(unsigned short usTimer_numb){
	if(!usTimer_numb){
		PIT_TFLG0 |= PIT_TFLG_TIF(0x1u);
	}else{
		PIT_TFLG1 |= PIT_TFLG_TIF(0x1u);
	}
}
