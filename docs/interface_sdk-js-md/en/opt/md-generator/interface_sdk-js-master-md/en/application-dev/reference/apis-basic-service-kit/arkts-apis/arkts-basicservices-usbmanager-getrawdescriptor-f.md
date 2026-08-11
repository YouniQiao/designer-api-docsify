# getRawDescriptor

## Modules to Import

```TypeScript
import { usbManager } from 'kits/@kit.BasicServicesKit';
```

## getRawDescriptor

```TypeScript
function getRawDescriptor(pipe: USBDevicePipe): Uint8Array
```

Obtains a raw USB descriptor. If the USB service is abnormal, **undefined** may be returned. Check whether the return value of the API is empty.

**Since:** 9

<!--Device-usbManager-function getRawDescriptor(pipe: USBDevicePipe): Uint8Array--><!--Device-usbManager-function getRawDescriptor(pipe: USBDevicePipe): Uint8Array-End-->

**System capability:** SystemCapability.USB.USBManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| pipe | [USBDevicePipe](arkts-basicservices-usbmanager-usbdevicepipe-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Uint8Array |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [14400001](../../apis-basic-services-kit/errorcode-usb.md#14400001-usb-device-connection-denied) |
| [14400004](../../apis-basic-services-kit/errorcode-usb.md#14400004-service-exception) |

## Examples

```TypeScript
function getRawDescriptor() {
  let devicesList: Array<usbManager.USBDevice> = usbManager.getDevices();
  if (!devicesList || devicesList.length == 0) {
    console.info(`device list is empty`);
    return;
  }

  usbManager.requestRight(devicesList?.[0]?.name);
  let devicepipe: usbManager.USBDevicePipe = usbManager.connectDevice(devicesList?.[0]);
  let ret: Uint8Array = usbManager.getRawDescriptor(devicepipe);
}
```
