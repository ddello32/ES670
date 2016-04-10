/* ***************************************************************** */
/* File name:        sevenseg_hal.h                                  */
/* File description: Header file containing the functions/methods    */
/*                   interfaces for handling SEVEN SEGMENT DISPLAY   */
/*                    from the peripheral board                      */
/* Author name:      ddello	                                         */
/* Creation date:    18mar2016                                       */
/* Revision date:    10abr2016          	                         */
/* ***************************************************************** */

#ifndef SOURCES_SEVEN_SEGMENT_HAL_H_
#define SOURCES_SEVEN_SEGMENT_HAL_H_

#include "KL25Z/es670_peripheral_board.h"

#define MAX_SEGMENT_NUMBER 8
#define MAX_DISP_NUMBER 4


typedef enum
{
    SEG_A =	 SEGA_PIN,
    SEG_B =	 SEGB_PIN,
    SEG_C =	 SEGC_PIN,
    SEG_D =	 SEGD_PIN,
    SEG_E =	 SEGE_PIN,
    SEG_F =	 SEGF_PIN,
    SEG_G =	 SEGG_PIN,
    SEG_DP = SEGDP_PIN,
	SEG_END = -1
} seven_segment_seg_type_e;

typedef enum
{
    DISP_1 =	 SEG_DISP1_PIN,
	DISP_2 =	 SEG_DISP2_PIN,
	DISP_3 =	 SEG_DISP3_PIN,
	DISP_4 =	 SEG_DISP4_PIN,
} seven_segment_disp_type_e;

/*!
/* Method name:        sevenseg_init
/* Method description: Initialize the seven segment display
/* Input params:       n/a
/* Output params:      n/a
*/
void sevenseg_init(void);

/* ******************************************************** */
/* Method name:        sevenseg_setSegs                     */
/* Method description: Sets only the selected segments as   */
/* 					 	   high. Setting the others as low  */
/* Input params:                                            */
/*					   set_segments = Array with the        */
/*						 segments that should be set as on  */
/*						 followed by SEG_END.               */
/* Output params:      n/a                                  */
/* ******************************************************** */
void sevenseg_setSegs(seven_segment_seg_type_e* ea_set_segments);

/* ************************************************ */
/* Method name:        sevenseg_setSegs             */
/* Method description: Shows the value writen in the*/
/*						segment pins to the given   */
/*						display	after clearing the  */
/* 						others						*/
/* Input params:       e_display = the display to   */
/*						initialize.					*/
/* Output params:      n/a                          */
/* ************************************************ */
void sevenseg_setDisp(seven_segment_disp_type_e e_display);


/**
 * Method name:        sevenseg_printHex
 * Method description: Shows the passed value in hexadecimal format in the
 * 						seven segment display.
 * Input params:	    unsigned int hex = the value to be printed
 * Output params:      n/a
 */
void sevenseg_printHex(unsigned int hex);

/**
 * Method name:        sevenseg_printDec
 * Method description: Shows the passed value in decimal format in the
 * 						seven segment display.
 * Input params:	   unsigned int dec = the value to be printed
 * Output params:      n/a
 */
void sevenseg_printDec(unsigned int dec);

/**
 * Method name:        sevenseg_dec2segArray
 * Method description: Converts the less significative decimal digit of the argument into it's seven
 * 					    segment display configuration
 * Input params:	   unsigned short dec = the value to be converted
 * 					   seven_segment_seg_type_e* ret= address for results
 * 					   	(should be a allocated array of minimal 8 elements)
 * Output params:      ret
 */
seven_segment_seg_type_e* sevenseg_dec2segArray(unsigned short dec, seven_segment_seg_type_e* ret);

/**
 * Method name:        sevenseg_hex2segArray
 * Method description: Converts the less significative hexadecimal digit of the argument into it's seven
 * 					    segment display configuration
 * Input params:	   unsigned short hex = the value to be converted
 * 					   seven_segment_seg_type_e* ret= address for results
 * 					   	(should be a allocated array of minimal 8 elements)
 * Output params:      ret
 */
seven_segment_seg_type_e* sevenseg_hex2segArray(unsigned short hex, seven_segment_seg_type_e* ret);

#endif /* SOURCES_SEVEN_SEGMENT_HAL_H_ */
