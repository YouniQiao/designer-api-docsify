# usbSubmitTransfer

## Modules to Import

```TypeScript
import { usbManager } from 'kits/@kit.BasicServicesKit';
```

## usbSubmitTransfer

```TypeScript
function usbSubmitTransfer(transfer: UsbDataTransferParams): void
```

Requests a USB data transfer.

> **NOTE：**&gt;
> This API uses an asynchronous callback to return the result.&gt;
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
| [14400007](../errorcode-usb.md#14400007-resource-busy) |
| [14400008](../errorcode-usb.md#14400008-no-device-disconnected) |
| [14400009](../errorcode-usb.md#14400009-insufficient-memory) |
| [14400012](../errorcode-usb.md#14400012-io-error) |
