# setConfiguration

## Modules to Import

```TypeScript
import { usb } from '@kit.BasicServicesKit';
```

## setConfiguration

```TypeScript
function setConfiguration(pipe: USBDevicePipe, config: USBConfig): number
```

Sets the device configuration.

Before you do this, call [usb.getDevices](arkts-basicservices-usb-getdevices-f.md#getDevices) to obtain the USB device list and device configuration, call [usb.requestRight](arkts-basicservices-usb-requestright-f.md#requestRight) to request the device access permission, and call  
[usb.connectDevice](arkts-basicservices-usb-connectdevice-f.md#connectDevice) to obtain **devicepipe** as an input parameter.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [setConfiguration](arkts-basicservices-usbmanager-setconfiguration-f.md#setConfiguration)

<!--Device-usb-function setConfiguration(pipe: USBDevicePipe, config: USBConfig): number--><!--Device-usb-function setConfiguration(pipe: USBDevicePipe, config: USBConfig): number-End-->

**System capability:** SystemCapability.USB.USBManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [pipe](../../apis-arkts/arkts-apis/arkts-arkts-stream-readable-c.md) | [USBDevicePipe](arkts-basicservices-usbmanager-usbdevicepipe-i.md) | Yes |
| config | [USBConfig](arkts-basicservices-usb-usbconfig-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## Examples

```TypeScript
let ret = usb.setConfiguration(devicepipe, config);
console.info(`setConfiguration = ${ret}`);
```
