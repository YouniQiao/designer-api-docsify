# resetUsbDevice

## Modules to Import

```TypeScript
import { usbManager } from 'kits/@kit.BasicServicesKit';
```

## resetUsbDevice

```TypeScript
function resetUsbDevice(pipe: USBDevicePipe): boolean
```

Resets a USB peripheral.

> **NOTE：**&gt;
> Previous configurations and APIs will be reset. Ensure that the related services have been completed before
> calling this API.

**Since:** 20

**System capability:** SystemCapability.USB.USBManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [pipe](../../apis-arkts/arkts-apis/arkts-arkts-stream-readable-c.md) | [USBDevicePipe](arkts-basicservices-usbmanager-usbdevicepipe-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [14400001](../errorcode-usb.md#14400001-usb-device-connection-denied) |
| [14400008](../errorcode-usb.md#14400008-no-device-disconnected) |
| [14400010](../errorcode-usb.md#14400010-unrecognized-error) |
| [14400013](../errorcode-usb.md#14400013-parameter-validity-check-failed) |
| [14400004](../errorcode-usb.md#14400004-service-exception) |
