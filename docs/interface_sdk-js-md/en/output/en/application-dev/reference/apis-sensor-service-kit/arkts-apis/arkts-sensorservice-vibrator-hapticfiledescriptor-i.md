# HapticFileDescriptor

Describes the FD of a custom vibration configuration file. Ensure that the file is available, and the parameters in it can be obtained from the sandbox path through the \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_ API or from the HAP resource through the [getRawFd]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_ API. The application scenario is as follows: The vibration sequence is stored in a file and vibration needs to be triggered based on the offset and length. For details about the storage format of the vibration sequence, see \_\_\_MD\_LINK\_DESC\_USD\_1\_\_\_.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-vibrator-interface HapticFileDescriptor--><!--Device-vibrator-interface HapticFileDescriptor-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

## fd

```TypeScript
fd: int
```

FD of the custom vibration configuration file.

**Type:** int

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-HapticFileDescriptor-fd: int--><!--Device-HapticFileDescriptor-fd: int-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

## length

```TypeScript
length?: long
```

Resource length, in bytes. The default value is the length from the offset position to the end of the file, and the value cannot exceed the valid range of the file.

**Type:** long

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-HapticFileDescriptor-length?: long--><!--Device-HapticFileDescriptor-length?: long-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

## offset

```TypeScript
offset?: long
```

Offset from the start position of the file, in bytes. The default value is the start position of the file, and the value cannot exceed the valid range of the file.

**Type:** long

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-HapticFileDescriptor-offset?: long--><!--Device-HapticFileDescriptor-offset?: long-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

