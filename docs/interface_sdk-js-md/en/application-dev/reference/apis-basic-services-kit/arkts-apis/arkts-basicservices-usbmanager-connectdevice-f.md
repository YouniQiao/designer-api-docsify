# connectDevice

## Modules to Import

```TypeScript
import { usbManager } from 'kits/@kit.BasicServicesKit';
```

## connectDevice

```TypeScript
function connectDevice(device: USBDevice): Readonly<USBDevicePipe>
```

Connects to the USB device based on the device information returned by **getDevices()**. If the USB service is abnormal, **undefined** may be returned. Check whether the return value of the API is empty.
1. Call [usbManager.getDevices](arkts-basicservices-usbmanager-getdevices-f.md) to obtain the USB device list.
2. Call [usbManager.requestRight](arkts-basicservices-usbmanager-requestright-f.md) to request the device access permission.

**Since:** 9

**System capability:** SystemCapability.USB.USBManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| device | [USBDevice](arkts-basicservices-usbmanager-usbdevice-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Readonly & lt;USBDevicePipe & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [14400001](../errorcode-usb.md#14400001-usb-device-connection-denied) |
| [14400004](../errorcode-usb.md#14400004-service-exception) |
| [14400012](../errorcode-usb.md#14400012-io-error) |
