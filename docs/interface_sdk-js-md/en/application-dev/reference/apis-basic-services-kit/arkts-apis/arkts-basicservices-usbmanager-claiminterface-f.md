# claimInterface

## Modules to Import

```TypeScript
import { usbManager } from 'kits/@kit.BasicServicesKit';
```

## claimInterface

```TypeScript
function claimInterface(pipe: USBDevicePipe, iface: USBInterface, force?: boolean): number
```

Claims a USB device interface.

> **NOTE：**&gt;
> In USB programming, **claimInterface** is a common operation, which indicates that an application requests the
> operating system to release a USB interface from the kernel driver and hand over the USB interface to a user
> space program for control.

> 
> All the **claim** communication interfaces used below refer to the claim interface operations.

**Since:** 9

**System capability:** SystemCapability.USB.USBManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [pipe](../../apis-arkts/arkts-apis/arkts-arkts-stream-readable-c.md) | [USBDevicePipe](arkts-basicservices-usbmanager-usbdevicepipe-i.md) | Yes |
| iface | [USBInterface](arkts-basicservices-usb-usbinterface-i.md) | Yes |
| [force](../../apis-arkui/arkts-components/arkts-arkui-historicalpoint-i.md) | boolean | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
