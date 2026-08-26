# connectDevice

## Modules to Import

```TypeScript
import usb from '@kit.BasicServicesKit';
import usbManager from '@kit.BasicServicesKitManager';
import serialManager from '@kit.BasicServicesKitManager.serial';
```

## connectDevice

```TypeScript
function connectDevice(device: USBDevice): Readonly<USBDevicePipe>
```

Connects to a USB device.Before you do this, call [usb.getDevices](arkts-basicservices-usb-getdevices-f.md) to obtain the USB device list, and then call [usb.requestRight](arkts-basicservices-usb-requestright-f.md) to request the device access permission.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [connectDevice](arkts-basicservices-usbmanager-connectdevice-f.md)

**System capability:** SystemCapability.USB.USBManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| device | [USBDevice](arkts-basicservices-usbmanager-usbdevice-i.md) | Yes | USB device information. |

**Return value:**

| Type | Description |
| --- | --- |
| Readonly & lt;USBDevicePipe & gt; | USB device pipe for data transfer. |

**Examples**

```TypeScript
let devicepipe= usb.connectDevice(device);
console.info(`devicepipe = ${devicepipe}`);
```
