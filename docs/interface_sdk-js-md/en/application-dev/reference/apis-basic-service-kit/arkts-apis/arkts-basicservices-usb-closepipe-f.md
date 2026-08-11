# closePipe

## Modules to Import

```TypeScript
import { usb } from 'kits/@kit.BasicServicesKit';
```

## closePipe

```TypeScript
function closePipe(pipe: USBDevicePipe): number
```

Closes a USB device pipe.

Before you do this, call [usb.getDevices](arkts-basicservices-usb-getdevices-f.md#getdevices) to obtain the USB device list, call  
[usb.requestRight](arkts-basicservices-usb-requestright-f.md#requestright) to request the device access permission, and call  
[usb.connectDevice](arkts-basicservices-usb-connectdevice-f.md#connectdevice) to obtain **devicepipe** as an input parameter.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [@ohos.usbManager:usbManager.closePipe](arkts-basicservices-usbmanager-closepipe-f.md#closepipe)

<!--Device-usb-function closePipe(pipe: USBDevicePipe): number--><!--Device-usb-function closePipe(pipe: USBDevicePipe): number-End-->

**System capability:** SystemCapability.USB.USBManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pipe | [USBDevicePipe](arkts-basicservices-usbmanager-usbdevicepipe-i.md) | Yes | USB device pipe. |

**Return value:**

| Type | Description |
| --- | --- |
| number | Returns **0** if the USB device pipe is closed successfully; returns an error code otherwise. |

## Examples

```TypeScript
let ret = usb.closePipe(devicepipe);
console.info(`closePipe = ${ret}`);
```

