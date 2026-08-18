# claimInterface

## Modules to Import

```TypeScript
```

## claimInterface

```TypeScript
function claimInterface(pipe: USBDevicePipe, iface: USBInterface, force?: boolean): number
```

Claims a USB interface. Before you do this, call [usb.getDevices](arkts-basicservices-usb-getdevices-f.md#getdevices) to obtain the USB device list and USB interfaces, call [usb.requestRight](arkts-basicservices-usb-requestright-f.md#requestright) to request the device access permission, and call [usb.connectDevice](arkts-basicservices-usb-connectdevice-f.md#connectdevice) to obtain **devicepipe** as an input parameter.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [claimInterface](arkts-basicservices-usbmanager-claiminterface-f.md#claiminterface)

<!--Device-usb-function claimInterface(pipe: USBDevicePipe, iface: USBInterface, force?: boolean): number--><!--Device-usb-function claimInterface(pipe: USBDevicePipe, iface: USBInterface, force?: boolean): number-End-->

**System capability:** SystemCapability.USB.USBManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [pipe](../../apis-arkts/arkts-apis/arkts-arkts-stream-readable-c.md) | [USBDevicePipe](arkts-basicservices-usbmanager-usbdevicepipe-i.md) | Yes |
| iface | [USBInterface](arkts-basicservices-usb-usbinterface-i.md) | Yes |
| force | boolean | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Examples**

```TypeScript
let ret = usb.claimInterface(devicepipe, interfaces);
console.info(`claimInterface = ${ret}`);
```
