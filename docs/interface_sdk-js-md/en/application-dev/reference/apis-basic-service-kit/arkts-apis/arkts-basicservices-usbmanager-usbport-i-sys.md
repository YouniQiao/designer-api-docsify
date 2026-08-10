# USBPort (System API)

USB设备端口。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-usbManager-interface USBPort--><!--Device-usbManager-interface USBPort-End-->

**System capability:** SystemCapability.USB.USBManager

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { usbManager } from 'kits/@kit.BasicServicesKit';
```

## id

```TypeScript
id: int
```

USB端口唯一标识。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-USBPort-id: int--><!--Device-USBPort-id: int-End-->

**System capability:** SystemCapability.USB.USBManager

**System API:** This is a system API.

## status

```TypeScript
status: USBPortStatus
```

USB端口角色。

**Type:** [USBPortStatus](arkts-basicservices-usb-usbportstatus-i-sys.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-USBPort-status: USBPortStatus--><!--Device-USBPort-status: USBPortStatus-End-->

**System capability:** SystemCapability.USB.USBManager

**System API:** This is a system API.

## supportedModes

```TypeScript
supportedModes: PortModeType
```

USB端口所支持的模式的数字组合掩码。

**Type:** [PortModeType](arkts-basicservices-usb-portmodetype-e-sys.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-USBPort-supportedModes: PortModeType--><!--Device-USBPort-supportedModes: PortModeType-End-->

**System capability:** SystemCapability.USB.USBManager

**System API:** This is a system API.

