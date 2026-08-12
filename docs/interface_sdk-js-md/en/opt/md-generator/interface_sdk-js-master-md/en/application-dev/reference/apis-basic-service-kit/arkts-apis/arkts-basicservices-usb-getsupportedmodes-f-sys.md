# getSupportedModes (System API)

## Modules to Import

```TypeScript
import { usb } from '@kit.BasicServicesKit';
```

## getSupportedModes

```TypeScript
function getSupportedModes(portId: number): PortModeType
```

Obtains the mask combination for the supported mode list of a given USB port.

**Since:** 9

**Deprecated since:** 9

**Substitutes:** [getSupportedModes](arkts-basicservices-usbmanager-getsupportedmodes-f-sys.md#getSupportedModes)

<!--Device-usb-function getSupportedModes(portId: number): PortModeType--><!--Device-usb-function getSupportedModes(portId: number): PortModeType-End-->

**System capability:** SystemCapability.USB.USBManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [portId](arkts-basicservices-serialmanager-serialport-i.md) | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [PortModeType](arkts-basicservices-usb-portmodetype-e-sys.md) |

## Examples

```TypeScript
let ret = usb.getSupportedModes(0);
```
