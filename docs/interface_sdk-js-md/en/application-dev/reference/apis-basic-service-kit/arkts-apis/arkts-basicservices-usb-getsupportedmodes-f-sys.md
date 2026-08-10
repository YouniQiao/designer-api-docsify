# getSupportedModes (System API)

## Modules to Import

```TypeScript
import { usb } from 'kits/@kit.BasicServicesKit';
```

## getSupportedModes

```TypeScript
function getSupportedModes(portId: number): PortModeType
```

获取指定的端口支持的模式列表的组合掩码。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 9

**Substitutes:** [@ohos.usbManager:usbManager.getSupportedModes](arkts-basicservices-usbmanager-getsupportedmodes-f-sys.md#getsupportedmodes)

<!--Device-usb-function getSupportedModes(portId: number): PortModeType--><!--Device-usb-function getSupportedModes(portId: number): PortModeType-End-->

**System capability:** SystemCapability.USB.USBManager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| portId | number | Yes | 端口号。 |

**Return value:**

| Type | Description |
| --- | --- |
| [PortModeType](arkts-basicservices-usb-portmodetype-e-sys.md) | 支持的模式列表的组合掩码。 |

## Examples

```TypeScript
let ret = usb.getSupportedModes(0);
```

