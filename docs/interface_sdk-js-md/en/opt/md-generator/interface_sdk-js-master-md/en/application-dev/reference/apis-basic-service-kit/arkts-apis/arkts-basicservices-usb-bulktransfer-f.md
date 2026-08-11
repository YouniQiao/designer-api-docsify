# bulkTransfer

## Modules to Import

```TypeScript
import { usb } from 'kits/@kit.BasicServicesKit';
```

## bulkTransfer

```TypeScript
function bulkTransfer(
    pipe: USBDevicePipe,
    endpoint: USBEndpoint,
    buffer: Uint8Array,
    timeout?: number
  ): Promise<number>
```

Performs bulk transfer.

Before you do this, call [usb.getDevices](arkts-basicservices-usb-getdevices-f.md#getdevices) to obtain the USB device list and endpoints, call  
[usb.requestRight](arkts-basicservices-usb-requestright-f.md#requestright) to request the device access permission, call  
[usb.connectDevice](arkts-basicservices-usb-connectdevice-f.md#connectdevice) to obtain **devicepipe** as an input parameter, and call  
[usb.claimInterface](arkts-basicservices-usb-claiminterface-f.md#claiminterface) to claim the USB interface.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [@ohos.usbManager:usbManager.bulkTransfer](arkts-basicservices-usbmanager-bulktransfer-f.md#bulktransfer)

<!--Device-usb-function bulkTransfer(    pipe: USBDevicePipe,    endpoint: USBEndpoint,    buffer: Uint8Array,    timeout?: number  ): Promise<number>--><!--Device-usb-function bulkTransfer(    pipe: USBDevicePipe,    endpoint: USBEndpoint,    buffer: Uint8Array,    timeout?: number  ): Promise<number>-End-->

**System capability:** SystemCapability.USB.USBManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| pipe | [USBDevicePipe](arkts-basicservices-usbmanager-usbdevicepipe-i.md) | Yes |
| endpoint | [USBEndpoint](arkts-basicservices-usbmanager-usbendpoint-i.md) | Yes |
| buffer | Uint8Array | Yes |
| timeout | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;number&gt; |

## Examples

```TypeScript
// Call usb.getDevices to obtain a data set. Then, obtain a USB device and its access permission.
// Pass the obtained USB device as a parameter to usb.connectDevice. Then, call usb.connectDevice to connect the USB device.
// Call usb.claimInterface to claim the USB interface. After that, call usb.bulkTransfer to start bulk transfer.
usb.bulkTransfer(devicepipe, endpoint, buffer).then((ret) => {
 console.info(`bulkTransfer = ${ret}`);
});
```
