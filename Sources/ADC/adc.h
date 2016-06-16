/*
 * File name: adc.h
 *
 *  Created on: 06/06/2016
 *      Author: msoliveira
 */

#include <stdint.h>

/**
 *  Configure ADC module
 */
void adc_initADCModule(void);

/**
 * Init conversion from A to D
 */
void adc_initConvertion(void);

/**
 * Check if conversion is done
 */
short adc_isAdcDone(void);

/**
 * Retrieve converted value
 */
uint16_t adc_getConvertionValue(void);
