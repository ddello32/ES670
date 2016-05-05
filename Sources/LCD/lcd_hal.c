/* ***************************************************************** */
/* File name:        lcd_hal.c                                       */
/* File description: File dedicated to the hardware abstraction layer*/
/*                   related to the LCD HARDWARE based on the KS006U */
/*                   controller                                      */
/* Author name:      dloubach                                        */
/* Creation date:    16out2015                                       */
/* Revision date:    25fev2016                                       */
/* ***************************************************************** */

#include "lcd_hal.h"
#include "KL25Z/es670_peripheral_board.h"
#include "Util/util.h"
#include "GPIO/gpio_hal.h"

/* line and columns */
#define LINE0        0U
#define COLUMN0        0U

#define L0C0_BASE    0x80 /* line 0, column 0 */
#define L1C0_BASE    0xC0 /* line 1, column 0 */
#define MAX_COLUMN  15U

/* ************************************************ */
/* Method name:        lcd_initLcd                  */
/* Method description: Initialize the LCD function  */
/* Input params:       n/a                          */
/* Output params:       n/a                         */
/* ************************************************ */
void lcd_initLcd(void)
{
    /* pins configured as outputs */

    /* un-gate port clock*/
    GPIO_UNGATE_PORT(LCD_PORT_ID);

    /* set pin as gpio output*/
    GPIO_INIT_PIN(LCD_PORT_ID, LCD_RS_PIN, LCD_RS_DIR);
    GPIO_INIT_PIN(LCD_PORT_ID, LCD_ENABLE_PIN, LCD_ENABLE_DIR);
    GPIO_INIT_PIN(LCD_PORT_ID, LCD_DATA_DB0_PIN, LCD_DATA_DIR);
    GPIO_INIT_PIN(LCD_PORT_ID, LCD_DATA_DB1_PIN, LCD_DATA_DIR);
    GPIO_INIT_PIN(LCD_PORT_ID, LCD_DATA_DB2_PIN, LCD_DATA_DIR);
    GPIO_INIT_PIN(LCD_PORT_ID, LCD_DATA_DB3_PIN, LCD_DATA_DIR);
    GPIO_INIT_PIN(LCD_PORT_ID, LCD_DATA_DB4_PIN, LCD_DATA_DIR);
    GPIO_INIT_PIN(LCD_PORT_ID, LCD_DATA_DB5_PIN, LCD_DATA_DIR);
    GPIO_INIT_PIN(LCD_PORT_ID, LCD_DATA_DB6_PIN, LCD_DATA_DIR);
    GPIO_INIT_PIN(LCD_PORT_ID, LCD_DATA_DB7_PIN, LCD_DATA_DIR);

    // turn-on LCD, with no cursor and no blink
    lcd_sendCommand(CMD_NO_CUR_NO_BLINK);

    // init LCD
    lcd_sendCommand(CMD_INIT_LCD);

    // clear LCD
    lcd_sendCommand(CMD_CLEAR);

    // LCD with no cursor
    lcd_sendCommand(CMD_NO_CURSOR);

    // cursor shift to right
    lcd_sendCommand(CMD_CURSOR2R);

}



/* ************************************************ */
/* Method name:        lcd_write2Lcd                */
/* Method description: Send command or data to LCD  */
/* Input params:       ucBuffer => char to be send  */
/*                     cDataType=>command LCD_RS_CMD*/
/*                     or data LCD_RS_DATA          */
/* Output params:      n/a                          */
/* ************************************************ */
void lcd_write2Lcd(unsigned char ucBuffer,  unsigned char cDataType)
{
    /* writing data or command */
    if(LCD_RS_CMD == cDataType){
        /* will send a command */
        GPIO_WRITE_PIN(LCD_PORT_ID, LCD_RS_PIN, LCD_RS_CMD);
    } else{
        /* will send data */
    	GPIO_WRITE_PIN(LCD_PORT_ID, LCD_RS_PIN, LCD_RS_DATA);
    }

    /* write in the LCD bus */
    GPIO_WRITE_PIN(LCD_PORT_ID, LCD_DATA_DB0_PIN, ((ucBuffer & (1u << 0u)) >> 0u));
    GPIO_WRITE_PIN(LCD_PORT_ID, LCD_DATA_DB1_PIN, ((ucBuffer & (1u << 1u)) >> 1u));
    GPIO_WRITE_PIN(LCD_PORT_ID, LCD_DATA_DB2_PIN, ((ucBuffer & (1u << 2u)) >> 2u));
    GPIO_WRITE_PIN(LCD_PORT_ID, LCD_DATA_DB3_PIN, ((ucBuffer & (1u << 3u)) >> 3u));
    GPIO_WRITE_PIN(LCD_PORT_ID, LCD_DATA_DB4_PIN, ((ucBuffer & (1u << 4u)) >> 4u));
    GPIO_WRITE_PIN(LCD_PORT_ID, LCD_DATA_DB5_PIN, ((ucBuffer & (1u << 5u)) >> 5u));
    GPIO_WRITE_PIN(LCD_PORT_ID, LCD_DATA_DB6_PIN, ((ucBuffer & (1u << 6u)) >> 6u));
    GPIO_WRITE_PIN(LCD_PORT_ID, LCD_DATA_DB7_PIN, ((ucBuffer & (1u << 7u)) >> 7u));

    /* enable, delay, disable LCD */
    /* this generates a pulse in the enable pin */
    GPIO_WRITE_PIN(LCD_PORT_ID, LCD_ENABLE_PIN, LCD_ENABLED);
    util_genDelay1ms();
    GPIO_WRITE_PIN(LCD_PORT_ID, LCD_ENABLE_PIN, LCD_DISABLED);
    util_genDelay1ms();
    util_genDelay1ms();
}



/* ************************************************ */
/* Method name:        lcd_writeData                */
/* Method description: Write data to be displayed   */
/* Input params:       ucData => char to be written */
/* Output params:      n/a                          */
/* ************************************************ */
void lcd_writeData(unsigned char ucData)
{
    /* just a relay to send data */
    lcd_write2Lcd(ucData, LCD_RS_DATA);
}



/* ************************************************ */
/* Method name:        lcd_sendCommand              */
/* Method description: Write command to LCD         */
/* Input params:       ucCmd=>command to be executed*/
/* Output params:      n/a                          */
/* ************************************************ */
void lcd_sendCommand(unsigned char ucCmd)
{
    /* just a relay to send command */
    lcd_write2Lcd(ucCmd, LCD_RS_CMD);
}



/* ************************************************ */
/* Method name:        lcd_setCursor                */
/* Method description: Set cursor line and column   */
/* Input params:       cLine = LINE0..LINE1         */
/*                     cColumn = COLUMN0..MAX_COLUMN*/
/* Output params:       n/a                         */
/* ************************************************ */
void lcd_setCursor(unsigned char cLine, unsigned char cColumn)
{
    char cCommand;

    if(LINE0 == cLine)
        /* line 0 */
        cCommand = L0C0_BASE;
    else
        /* line 1 */
        cCommand = L1C0_BASE;

    /* maximum MAX_COLUMN columns */
    cCommand += (cColumn & MAX_COLUMN);

    // send the command to set the cursor
    lcd_sendCommand(cCommand);
}



/* ************************************************ */
/* Method name:        lcd_writeString              */
/* Method description: Write string to be displayed */
/* Input params:       cBuffer => string to be      */
/*                     written in LCD               */
/* Output params:      n/a                          */
/* ************************************************ */
void lcd_writeString(const char *cBuffer)
{
    while(*cBuffer)
    {
        lcd_writeData(*cBuffer++);
    };
}



/* ************************************************ */
/* Method name:        lcd_dummyText                */
/* Method description: Write a dummy hard coded text*/
/* Input params:       n/a                          */
/* Output params:      n/a                          */
/* ************************************************ */
void lcd_dummyText(void)
{
    // clear LCD
    lcd_sendCommand(CMD_CLEAR);

    // set the cursor line 0, column 1
    lcd_setCursor(0,1);

    // send string
    lcd_writeString("*** ES670 ***");

    // set the cursor line 1, column 0
    lcd_setCursor(1,0);
    lcd_writeString("Prj Sis Embarcad");
}