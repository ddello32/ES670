################################################################################
# Automatically-generated file. Do not edit!
################################################################################

-include ../makefile.init

RM := rm -rf

# All of the sources participating in the build are defined here
-include sources.mk
-include Sources/Util/subdir.mk
-include Sources/TempSensor/subdir.mk
-include Sources/Tacometro/subdir.mk
-include Sources/SevenSeg/subdir.mk
-include Sources/Serial/subdir.mk
-include Sources/Protocolo/subdir.mk
-include Sources/PIT/subdir.mk
-include Sources/Mcg/subdir.mk
-include Sources/Main/subdir.mk
-include Sources/LedSwi/subdir.mk
-include Sources/LCD/subdir.mk
-include Sources/Heater/subdir.mk
-include Sources/Cooler/subdir.mk
-include Sources/Buzzer/subdir.mk
-include Sources/ADC/subdir.mk
-include Sources/subdir.mk
-include Project_Settings/Startup_Code/subdir.mk
-include subdir.mk
-include objects.mk

ifneq ($(MAKECMDGOALS),clean)
ifneq ($(strip $(C++_DEPS)),)
-include $(C++_DEPS)
endif
ifneq ($(strip $(C_DEPS)),)
-include $(C_DEPS)
endif
ifneq ($(strip $(ASM_DEPS)),)
-include $(ASM_DEPS)
endif
ifneq ($(strip $(CC_DEPS)),)
-include $(CC_DEPS)
endif
ifneq ($(strip $(CPP_DEPS)),)
-include $(CPP_DEPS)
endif
ifneq ($(strip $(CXX_DEPS)),)
-include $(CXX_DEPS)
endif
ifneq ($(strip $(C_UPPER_DEPS)),)
-include $(C_UPPER_DEPS)
endif
ifneq ($(strip $(S_UPPER_DEPS)),)
-include $(S_UPPER_DEPS)
endif
endif

-include ../makefile.defs

# Add inputs and outputs from these tool invocations to the build variables 

# All Target
all: emb.elf secondary-outputs

# Tool invocations
emb.elf: $(OBJS) $(USER_OBJS)
	@echo 'Building target: $@'
	@echo 'Invoking: Cross ARM C++ Linker'
	arm-none-eabi-g++ -mcpu=cortex-m0plus -mthumb -O0 -fmessage-length=0 -fsigned-char -ffunction-sections -fdata-sections  -g3 -T "MKL25Z128xxx4_flash.ld" -Xlinker --gc-sections -L"/home/dello/Workspace/es670/workspace.kds/emb/Project_Settings/Linker_Files" -Wl,-Map,"emb.map" -specs=nosys.specs -specs=nano.specs -Xlinker -z -Xlinker muldefs -o "emb.elf" $(OBJS) $(USER_OBJS) $(LIBS)
	@echo 'Finished building target: $@'
	@echo ' '

# Other Targets
clean:
	-$(RM) $(C++_DEPS)$(OBJS)$(C_DEPS)$(ASM_DEPS)$(CC_DEPS)$(CPP_DEPS)$(CXX_DEPS)$(C_UPPER_DEPS)$(S_UPPER_DEPS) emb.elf
	-@echo ' '

secondary-outputs:

.PHONY: all clean dependents
.SECONDARY:

-include ../makefile.targets
