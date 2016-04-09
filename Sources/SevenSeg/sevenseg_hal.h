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

#include "KL25Z/es670_peripheral_board.h"

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
/* Input params:       us_segmentNumber = Number of         */
/*						  elements in the segment array <= 8*/
/*					   set_segments = Array with the        */
/*						 segments that should be set as on  */
/* Output params:      n/a                                  */
/* ******************************************************** */
void sevenseg_setSegs(unsigned short us_segmentNumber, seven_segment_seg_type_e* ea_set_segments);

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



#endif /* SOURCES_SEVEN_SEGMENT_HAL_H_ */
