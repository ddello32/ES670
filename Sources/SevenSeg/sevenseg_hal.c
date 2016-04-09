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
#include "GPIO/gpio_util.h"
#include "KL25Z/es670_peripheral_board.h"

#define SEV_SEG_SEGMENT_MASK GPIO_HIGH << SEGA_PIN | GPIO_HIGH << SEGB_PIN | GPIO_HIGH << SEGC_PIN | GPIO_HIGH << SEGD_PIN | GPIO_HIGH << SEGE_PIN | GPIO_HIGH << SEGF_PIN | GPIO_HIGH << SEGG_PIN | GPIO_HIGH << SEGDP_PIN
#define SEV_SEG_DISP_MASK GPIO_HIGH << SEG_DISP1_PIN | GPIO_HIGH << SEG_DISP2_PIN | GPIO_HIGH << SEG_DISP3_PIN | GPIO_HIGH << SEG_DISP4_PIN

#define MAX_SEGMENT_NUMBER 8

/*!
* Method name:        sevenseg_init
* Method description: Initialize the seven segment display
*/
void sevenseg_init(void){
	GPIO_UNGATE_PORT(SEV_SEG_PORT_ID);

	// Init the Seven Segment segment control pins as OUTPUT
	GPIO_INIT_PIN(SEV_SEG_PORT_ID, SEGA_PIN, GPIO_OUTPUT);
	GPIO_INIT_PIN(SEV_SEG_PORT_ID, SEGB_PIN, GPIO_OUTPUT);
	GPIO_INIT_PIN(SEV_SEG_PORT_ID, SEGC_PIN, GPIO_OUTPUT);
	GPIO_INIT_PIN(SEV_SEG_PORT_ID, SEGD_PIN, GPIO_OUTPUT);
	GPIO_INIT_PIN(SEV_SEG_PORT_ID, SEGE_PIN, GPIO_OUTPUT);
	GPIO_INIT_PIN(SEV_SEG_PORT_ID, SEGF_PIN, GPIO_OUTPUT);
	GPIO_INIT_PIN(SEV_SEG_PORT_ID, SEGG_PIN, GPIO_OUTPUT);
	GPIO_INIT_PIN(SEV_SEG_PORT_ID, SEGDP_PIN, GPIO_OUTPUT);
	// Init the Seven Segment segment display pins as OUTPUT
	GPIO_INIT_PIN(SEV_SEG_PORT_ID, SEG_DISP1_PIN, GPIO_OUTPUT);
	GPIO_INIT_PIN(SEV_SEG_PORT_ID, SEG_DISP2_PIN, GPIO_OUTPUT);
	GPIO_INIT_PIN(SEV_SEG_PORT_ID, SEG_DISP3_PIN, GPIO_OUTPUT);
	GPIO_INIT_PIN(SEV_SEG_PORT_ID, SEG_DISP4_PIN, GPIO_OUTPUT);
}


/* ******************************************************** */
/* Method name:        sevenseg_setSegs                     */
/* Method description: Sets only the selected segments as   */
/* 					 	   high. Setting the others as low  */
/* Input params:       us_segmentNumber = Number of         */
/*						  elements in the segment array <= 8*/
/*					   set_segments = Array with the        */
/*						 segments that should be set as on  */
/* Output params:      n/a                                  */
/* ******************************************************** */
void sevenseg_setSegs(unsigned short us_segmentNumber, seven_segment_seg_type_e* ea_set_segments){
	if(us_segmentNumber <= MAX_SEGMENT_NUMBER){
		//Clear all segments.
		GPIO_WRITE_MASK(SEV_SEG_PORT_ID, SEV_SEG_SEGMENT_MASK, GPIO_LOW);
		//Set the selected segments to high
		for(unsigned short us_counter = 0; us_counter < us_segmentNumber; us_counter++){
			GPIO_WRITE_PIN(SEV_SEG_PORT_ID, ea_set_segments[us_counter], GPIO_HIGH);
		}
	}
}

/* ************************************************* */
/* Method name:        sevenseg_setSegs              */
/* Method description: Shows the value written in the*/
/*						segment pins to the given    */
/*						display	after clearing the   */
/* 						others						 */
/* Input params:       e_display = the display to    */
/*						initialize.					 */
/* Output params:      n/a                           */
/* ************************************************* */
void sevenseg_setDisp(seven_segment_disp_type_e e_display){
	//Clear all displays
	GPIO_WRITE_MASK(SEV_SEG_PORT_ID, SEV_SEG_DISP_MASK, GPIO_LOW);
	//Activate the selected display
	GPIO_WRITE_PIN(SEV_SEG_PORT_ID, e_display, GPIO_HIGH);
}
