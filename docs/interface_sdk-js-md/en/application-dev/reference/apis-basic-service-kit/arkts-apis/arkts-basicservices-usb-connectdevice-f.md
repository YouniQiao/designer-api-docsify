# connectDevice

## Modules to Import

```TypeScript
import { usb } from 'kits/@kit.BasicServicesKit';
```

## connectDevice

```TypeScript
function connectDevice(device: USBDevice): Readonly<USBDevicePipe>
```

Connects to a USB device.

Before you do this, call [usb.getDevices](arkts-basicservices-usb-getdevices-f.md#getdevices) to obtain the USB device list, and then call  
[usb.requestRight](arkts-basicservices-usb-requestright-f.md#requestright) to request the device access permission.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [@ohos.usbManager:usbManager.connectDevice](arkts-basicservices-usbmanager-connectdevice-f.md#connectdevice)

<!--Device-usb-function connectDevice(device: USBDevice): Readonly<USBDevicePipe>--><!--Device-usb-function connectDevice(device: USBDevice): Readonly<USBDevicePipe>-End-->

**System capability:** SystemCapability.USB.USBManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| device | [USBDevice](arkts-basicservices-usb-usbdevice-i.md) | Yes | USB device information. |

**Return value:**

| Type | Description |
| --- | --- |
| [Readonly](../../apis-default/arkts-apis/arkts-readonly-t.md)&lt;USBDevicePipe&gt; | USB device pipe for data transfer. |

## Examples

```TypeScript
let devicepipe= usb.connectDevice(device);
console.info(`devicepipe = ${devicepipe}`);
```

