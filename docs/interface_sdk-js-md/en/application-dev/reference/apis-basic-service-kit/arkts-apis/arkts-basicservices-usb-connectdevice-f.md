# connectDevice

## Modules to Import

```TypeScript
import { usb } from '@kit.BasicServicesKit';
```

## connectDevice

```TypeScript
function connectDevice(device: USBDevice): Readonly<USBDevicePipe>
```

Connects to a USB device.

Before you do this, call [usb.getDevices](arkts-basicservices-usb-getdevices-f.md#getDevices) to obtain the USB device list, and then call  
[usb.requestRight](arkts-basicservices-usb-requestright-f.md#requestRight) to request the device access permission.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [connectDevice](arkts-basicservices-usbmanager-connectdevice-f.md#connectDevice)

<!--Device-usb-function connectDevice(device: USBDevice): Readonly<USBDevicePipe>--><!--Device-usb-function connectDevice(device: USBDevice): Readonly<USBDevicePipe>-End-->

**System capability:** SystemCapability.USB.USBManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| device | USBDevice | Yes | USB device information. |

**Return value:**

| Type | Description |
| --- | --- |
| [Readonly](../../apis-default/arkts-apis/arkts-readonly-t.md)&lt;USBDevicePipe&gt; | USB device pipe for data transfer. |

## Examples

```TypeScript
let devicepipe= usb.connectDevice(device);
console.info(`devicepipe = ${devicepipe}`);
```

