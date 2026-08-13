# closePipe

## Modules to Import

```TypeScript
import { usb } from '@kit.BasicServicesKit';
```

## closePipe

```TypeScript
function closePipe(pipe: USBDevicePipe): number
```

Closes a USB device pipe. Before you do this, call [usb.getDevices](arkts-basicservices-usb-getdevices-f.md#getDevices) to obtain the USB device list, call [usb.requestRight](arkts-basicservices-usb-requestright-f.md#requestRight) to request the device access permission, and call [usb.connectDevice](arkts-basicservices-usb-connectdevice-f.md#connectDevice) to obtain **devicepipe** as an input parameter.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [closePipe](arkts-basicservices-usbmanager-closepipe-f.md#closePipe)

<!--Device-usb-function closePipe(pipe: USBDevicePipe): number--><!--Device-usb-function closePipe(pipe: USBDevicePipe): number-End-->

**System capability:** SystemCapability.USB.USBManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [pipe](../../apis-arkts/arkts-apis/arkts-arkts-stream-readable-c.md) | [USBDevicePipe](arkts-basicservices-usbmanager-usbdevicepipe-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## Examples

```TypeScript
let ret = usb.closePipe(devicepipe);
console.info(`closePipe = ${ret}`);
```
