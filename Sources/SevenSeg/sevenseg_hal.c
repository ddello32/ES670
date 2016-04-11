/* ***************************************************************** */
/* File name:        sevenseg_hal.c                                  */
/* File description: File containing the functions/methods           */
/*                   for handling SEVEN SEGMENT DISPLAY              */
/*                    from the peripheral board                      */
/* Author name:      ddello	                                         */
/* Creation date:    18mar2016                                       */
/* Revision date:    10abr2016          	                         */
/* ***************************************************************** */

#include "GPIO/gpio_hal.h"
#include "sevenseg_hal.h"
#include "math.h"
#include "KL25Z/es670_peripheral_board.h"
#include "PIT/pit_hal.h"

#define SEV_SEG_SEGMENT_MASK GPIO_HIGH << SEGA_PIN | GPIO_HIGH << SEGB_PIN | GPIO_HIGH << SEGC_PIN | GPIO_HIGH << SEGD_PIN | GPIO_HIGH << SEGE_PIN | GPIO_HIGH << SEGF_PIN | GPIO_HIGH << SEGG_PIN | GPIO_HIGH << SEGDP_PIN
#define SEV_SEG_DISP_MASK GPIO_HIGH << SEG_DISP1_PIN | GPIO_HIGH << SEG_DISP2_PIN | GPIO_HIGH << SEG_DISP3_PIN | GPIO_HIGH << SEG_DISP4_PIN

static unsigned short isHex = 0;
static unsigned int printVal = -1;

/**
 * Method name: sevenseg_interrupt_handler
 * Method description:	Interrupt handler for updating in display configuration
 */
void _sevenseg_interrupt_handler(void){
	static seven_segment_disp_type_e displays[] = {DISP_1, DISP_2, DISP_3, DISP_4};
	static seven_segment_seg_type_e seg_array[9];
	static unsigned short cur_disp = 0;
	if(isHex){
		sevenseg_hex2segArray(printVal/pow(16,cur_disp), seg_array);
	}else{
		sevenseg_dec2segArray(printVal/pow(10,cur_disp), seg_array);
	}
	sevenseg_setSegs(seg_array);
	sevenseg_setDisp(displays[cur_disp]);
	cur_disp = (cur_disp+1)%4;
	pit_mark_interrupt_handled(SEV_SEG_PIT_TIMER_NUMB);
}

/**
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

	//Init pit interrupts
	pit_enable();
	//Init timer 0
	pit_start_timer_interrupt(SEV_SEG_PIT_TIMER_NUMB, SEVEN_SEG_PIT_PERIOD, &_sevenseg_interrupt_handler);
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
void sevenseg_setSegs(seven_segment_seg_type_e* ea_set_segments){
	//Clear all segments.
	GPIO_WRITE_MASK(SEV_SEG_PORT_ID, SEV_SEG_SEGMENT_MASK, GPIO_LOW);
	//Set the selected segments to high
	for(unsigned short us_counter = 0; ea_set_segments[us_counter] != SEG_END; us_counter++){
		GPIO_WRITE_PIN(SEV_SEG_PORT_ID, ea_set_segments[us_counter], GPIO_HIGH);
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

/**
 * Method name:        sevenseg_printHex
 * Method description: Shows the passed value in hexadecimal format in the
 * 						seven segment display.
 * Input params:	    unsigned int hex = the value to be printed
 * Output params:      n/a
 */
void sevenseg_printHex(unsigned int hex){
	isHex = 1;
	printVal = hex;
}

/**
 * Method name:        sevenseg_printDec
 * Method description: Shows the passed value in decimal format in the
 * 						seven segment display.
 * Input params:	   unsigned int dec = the value to be printed
 * Output params:      n/a
 */
void sevenseg_printDec(unsigned int dec){
	isHex = 0;
	printVal = dec;
}

/**
 * Method name:        sevenseg_dec2segArray
 * Method description: Converts the less significative decimal digit of the argument into it's seven
 * 					    segment display configuration
 * Input params:	   unsigned short dec = the value to be converted (-1 if none should be displayed)
 * 					   seven_segment_seg_type_e* ret= address for results
 * 					   	(should be a allocated array of minimal 8 elements)
 * Output params:      ret
 */
seven_segment_seg_type_e* sevenseg_dec2segArray(unsigned short dec, seven_segment_seg_type_e* ret){
	if(dec < 0){
		ret[0] = SEG_END;
		return ret;
	}
	ret[0] = SEG_A;
	ret[1] = SEG_B;
	ret[2] = SEG_C;
	ret[3] = SEG_D;
	ret[4] = SEG_E;
	ret[5] = SEG_F;
	ret[6] = SEG_G;
	ret[7] = SEG_END;
	switch(dec%10){
	case 0:
		//{SEG_A,SEG_B,SEG_C,SEG_D,SEG_G,SEG_E,SEG_F,SEG_END};
		ret[7] = SEG_END;
		break;
	case 1:
		//{SEG_B,SEG_C,SEG_END};
		ret[0] = SEG_B;
		ret[1] = SEG_C;
		ret[2] = SEG_END;
		break;
	case 2:
		//{SEG_A,SEG_B,SEG_G,SEG_D,SEG_E,SEG_END};
		ret[2] = SEG_G;
		ret[5] = SEG_END;
		break;
	case 3:
		//{SEG_A,SEG_B,SEG_C,SEG_D,SEG_G,SEG_END}
		ret[4] = SEG_G;
		ret[5] = SEG_END;
		break;
	case 4:
		//{SEG_G, SEG_B,SEG_C,SEG_F, SEG_END}
		ret[0] = SEG_G;
		ret[3] = SEG_F;
		ret[4] = SEG_END;
		break;
	case 5:
		//{SEG_A,SEG_G,SEG_C,SEG_D,SEG_F,SEG_END}
		ret[1] = SEG_G;
		ret[4] = SEG_F;
		ret[5] = SEG_END;
		break;
	case 6:
		//{SEG_A,SEG_G,SEG_C,SEG_D,SEG_E,SEG_F,SEG_END}
		ret[1] = SEG_G;
		ret[6] = SEG_END;
		break;
	case 7:
		//{SEG_A,SEG_B,SEG_C,SEG_END}
		ret[3] = SEG_END;
		break;
	case 8:
		//{SEG_A,SEG_B,SEG_C,SEG_D,SEG_E,SEG_F,SEG_G,SEG_END}
		break;
	case 9:
		//SEG_A,SEG_B,SEG_C,SEG_F,SEG_G,SEG_END}
		ret[3] = SEG_F;
		ret[4] = SEG_G;
		ret[5] = SEG_END;
		break;
	}
	return ret;
}

/**
 * Method name:        sevenseg_hex2segArray
 * Method description: Converts the less significative hexadecimal digit of the argument into it's seven
 * 					    segment display configuration
 * Input params:	   unsigned short hex = the value to be converted (-1 if none should be displayed)
 * 					   seven_segment_seg_type_e* ret= address for results
 * 					   	(should be a allocated array of minimal 8 elements)
 * Output params:      ret
 */
seven_segment_seg_type_e* sevenseg_hex2segArray(unsigned short hex, seven_segment_seg_type_e* ret){
	if(hex < 0){
		ret[0] = SEG_END;
		return ret;
	}
	ret[0] = SEG_A;
	ret[1] = SEG_B;
	ret[2] = SEG_C;
	ret[3] = SEG_D;
	ret[4] = SEG_E;
	ret[5] = SEG_F;
	ret[6] = SEG_G;
	ret[7] = SEG_END;
	switch(hex%16){
		case 0:
		case 1:
		case 2:
		case 3:
		case 4:
		case 5:
		case 6:
		case 7:
		case 8:
		case 9:
			return sevenseg_dec2segArray(hex%16, ret);
			break;
		case 10: //A
			//{SEG_A,SEG_B,SEG_C,SEG_G,SEG_E,SEG_F,SEG_END}
			ret[3] = SEG_G;
			ret[6] = SEG_END;
			break;
		case 11: //B (b)
			//{SEG_G,SEG_F,SEG_C,SEG_D,SEG_E,SEG_END}
			ret[0] = SEG_G;
			ret[1] = SEG_F;
			ret[5] = SEG_END;
			break;
		case 12: //C
			//{SEG_A,SEG_E,SEG_F,SEG_D,SEG_END}
			ret[1] = SEG_E;
			ret[2] = SEG_F;
			ret[4] = SEG_END;
			break;
		case 13: //D (d)
			//{SEG_G,SEG_B,SEG_C,SEG_D,SEG_E,SEG_END}
			ret[0] = SEG_G;
			ret[5] = SEG_END;
			break;
		case 14: //E
			//{SEG_A,SEG_G,SEG_F,SEG_D,SEG_E,SEG_END}
			ret[1] = SEG_G;
			ret[2] = SEG_F;
			ret[5] = SEG_END;
			break;
		case 15: //F
			//{SEG_A,SEG_E,SEG_F,SEG_G,SEG_END}
			ret[1] = SEG_E;
			ret[2] = SEG_F;
			ret[3] = SEG_G;
			ret[4] = SEG_END;
			break;
	}
	return ret;
}
