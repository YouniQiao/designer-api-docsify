# closePipe

## Modules to Import

```TypeScript
import { usbManager } from 'kits/@kit.BasicServicesKit';
```

## closePipe

```TypeScript
function closePipe(pipe: USBDevicePipe): number
```

Closes a USB device pipe.

1. Call [usbManager.getDevices](arkts-basicservices-usbmanager-getdevices-f.md#getdevices) to obtain the USB device list.2. Call [usbManager.requestRight](arkts-basicservices-usbmanager-requestright-f.md#requestright) to request the device access permission.3. Call [usbManager.connectDevice](arkts-basicservices-usbmanager-connectdevice-f.md#connectdevice) to obtain **devicepipe** as an input parameter.

**Since:** 9

<!--Device-usbManager-function closePipe(pipe: USBDevicePipe): int--><!--Device-usbManager-function closePipe(pipe: USBDevicePipe): int-End-->

**System capability:** SystemCapability.USB.USBManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| pipe | [USBDevicePipe](arkts-basicservices-usbmanager-usbdevicepipe-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |

## Examples

```TypeScript
function closePipe() {
  let devicesList: Array<usbManager.USBDevice> = usbManager.getDevices();
  if (!devicesList || devicesList.length == 0) {
    console.info(`device list is empty`);
    return;
  }

  usbManager.requestRight(devicesList?.[0]?.name);
  let devicepipe: usbManager.USBDevicePipe = usbManager.connectDevice(devicesList?.[0]);
  let ret: number = usbManager.closePipe(devicepipe);
  console.info(`closePipe = ${ret}`);
}
```
