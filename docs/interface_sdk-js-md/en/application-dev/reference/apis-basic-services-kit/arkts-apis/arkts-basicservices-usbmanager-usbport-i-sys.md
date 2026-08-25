# USBPort (System API)

Represents a USB port.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**System capability:** SystemCapability.USB.USBManager

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { usbManager } from '@kit.BasicServicesKit';
```

## id

```TypeScript
id: int
```

Unique identifier of a USB port.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**System capability:** SystemCapability.USB.USBManager

**System API:** This is a system API.

## status

```TypeScript
status: USBPortStatus
```

USB port role.

**Type:** USBPortStatus

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**System capability:** SystemCapability.USB.USBManager

**System API:** This is a system API.

## supportedModes

```TypeScript
supportedModes: PortModeType
```

Numeric mask combination for the supported mode list.

**Type:** PortModeType

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**System capability:** SystemCapability.USB.USBManager

**System API:** This is a system API.
