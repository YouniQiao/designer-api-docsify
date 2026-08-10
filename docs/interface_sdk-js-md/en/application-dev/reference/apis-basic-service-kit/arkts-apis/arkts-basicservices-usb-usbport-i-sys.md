# USBPort (System API)

USB设备端口。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 9

**Substitutes:** [@ohos.usbManager:usbManager.USBPort](arkts-basicservices-usbmanager-usbport-i-sys.md)

<!--Device-usb-interface USBPort--><!--Device-usb-interface USBPort-End-->

**System capability:** SystemCapability.USB.USBManager

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { usb } from 'kits/@kit.BasicServicesKit';
```

## id

```TypeScript
id: number
```

USB端口唯一标识。

**Type:** number

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 9

**Substitutes:** [@ohos.usbManager:usbManager.USBPort.id](arkts-basicservices-usbmanager-usbport-i-sys.md#id)

<!--Device-USBPort-id: number--><!--Device-USBPort-id: number-End-->

**System capability:** SystemCapability.USB.USBManager

**System API:** This is a system API.

## status

```TypeScript
status: USBPortStatus
```

USB端口角色。

**Type:** [USBPortStatus](arkts-basicservices-usb-usbportstatus-i-sys.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 9

**Substitutes:** [@ohos.usbManager:usbManager.USBPort.status](arkts-basicservices-usbmanager-usbport-i-sys.md#status)

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

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 9

**Substitutes:** [@ohos.usbManager:usbManager.USBPort.supportedModes](arkts-basicservices-usbmanager-usbport-i-sys.md#supportedmodes)

<!--Device-USBPort-supportedModes: PortModeType--><!--Device-USBPort-supportedModes: PortModeType-End-->

**System capability:** SystemCapability.USB.USBManager

**System API:** This is a system API.

