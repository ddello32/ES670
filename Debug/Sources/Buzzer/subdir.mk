################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../Sources/Buzzer/buzzer_hal.c 

OBJS += \
./Sources/Buzzer/buzzer_hal.o 

C_DEPS += \
./Sources/Buzzer/buzzer_hal.d 


# Each subdirectory must supply rules for building sources it contributes
Sources/Buzzer/%.o: ../Sources/Buzzer/%.c
	@echo 'Building file: $<'
	@echo 'Invoking: Cross ARM C Compiler'
	arm-none-eabi-gcc -mcpu=cortex-m0plus -mthumb -O0 -fmessage-length=0 -fsigned-char -ffunction-sections -fdata-sections  -g3 -D"CPU_MKL25Z128VLK4" -I"../Sources" -I"../Project_Settings/Startup_Code" -I"../SDK/platform/CMSIS/Include" -I"../SDK/platform/devices" -I"../SDK/platform/devices/MKL25Z4/include" -I/mnt/9A68FEAD68FE8773/ksdk/platform/utilities/inc -I/mnt/9A68FEAD68FE8773/ksdk/platform/hal/inc -I"/mnt/9A68FEAD68FE8773/ksdk/platform/system/inc" -I"/mnt/9A68FEAD68FE8773/ksdk/platform/drivers/inc" -std=c99 -MMD -MP -MF"$(@:%.o=%.d)" -MT"$@" -c -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '


