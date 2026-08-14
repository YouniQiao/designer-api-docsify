# VibrateFromFile

Represents a custom vibration pattern. It is supported only by certain devices. An error code will be returned if a device does not support this vibration mode. You can pass **VibrateFromFile** to [VibrateEffect9+](arkts-sensorservice-vibrator-vibrateeffect-t.md#VibrateEffect) to specify a custom vibration pattern when calling [vibrator.startVibration9+](arkts-sensorservice-vibrator-startvibration-f.md#startVibration) or [vibrator.startVibration9+](arkts-sensorservice-vibrator-startvibration-f.md#startVibration).

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-vibrator-interface VibrateFromFile--><!--Device-vibrator-interface VibrateFromFile-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

## Modules to Import

```TypeScript
import { vibrator } from 'vibrator';
```

## hapticFd

```TypeScript
hapticFd: HapticFileDescriptor
```

File descriptor (FD) of the vibration configuration file.

**Type:** [HapticFileDescriptor](arkts-sensorservice-vibrator-hapticfiledescriptor-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-VibrateFromFile-hapticFd: HapticFileDescriptor--><!--Device-VibrateFromFile-hapticFd: HapticFileDescriptor-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

## type

```TypeScript
type: 'file'
```

The value **file** means vibration according to a vibration configuration file.

**Type:** 'file'

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-VibrateFromFile-type: 'file'--><!--Device-VibrateFromFile-type: 'file'-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

