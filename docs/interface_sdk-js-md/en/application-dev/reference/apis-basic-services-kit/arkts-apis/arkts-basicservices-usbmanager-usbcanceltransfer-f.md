# usbCancelTransfer

## Modules to Import

```TypeScript
import { usbManager } from 'kits/@kit.BasicServicesKit';
```

## usbCancelTransfer

```TypeScript
function usbCancelTransfer(transfer: UsbDataTransferParams): void
```

Cancels an asynchronous USB data transfer request.

> **NOTE：**&gt;
> This API is used to proactively cancel an unfinished USB data transfer request (for example, the one submitted by
> **usbSubmitTransfer**).
> Before calling this API, call the
> [usbManager.claimInterface](arkts-basicservices-usbmanager-claiminterface-f.md)
> API to claim a communication interface.

**Since:** 18

**System capability:** SystemCapability.USB.USBManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [transfer](../../apis-arkts/arkts-apis/arkts-arkts-worker-postmessageoptions-i.md) | [UsbDataTransferParams](arkts-basicservices-usbmanager-usbdatatransferparams-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [14400001](../errorcode-usb.md#14400001-usb-device-connection-denied) |
| [14400008](../errorcode-usb.md#14400008-no-device-disconnected) |
| [14400010](../errorcode-usb.md#14400010-unrecognized-error) |
| [14400011](../errorcode-usb.md#14400011-no-ongoing-transfer-found) |
