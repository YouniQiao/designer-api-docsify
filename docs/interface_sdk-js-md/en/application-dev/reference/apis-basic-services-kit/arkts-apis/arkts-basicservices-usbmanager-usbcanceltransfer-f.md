# usbCancelTransfer

## Modules to Import

```TypeScript
import { usbManager } from '@kit.BasicServicesKit';
```

## usbCancelTransfer

```TypeScript
function usbCancelTransfer(transfer: UsbDataTransferParams): void
```

Cancels an asynchronous USB data transfer request.

> **NOTE:** 
> 
> This API is used to proactively cancel an unfinished USB data transfer request (for example, the one submitted by
> **usbSubmitTransfer**).
> Before calling this API, call the
> [usbManager.claimInterface](arkts-basicservices-usbmanager-claiminterface-f.md)
> API to claim a communication interface.

**Since:** 18

**System capability:** SystemCapability.USB.USBManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| transfer | [UsbDataTransferParams](arkts-basicservices-usbmanager-usbdatatransferparams-i.md) | Yes | Only the [USBDevicePipe](arkts-basicservices-usbmanager-usbdevicepipe-i.md) and [USBEndpoint](arkts-basicservices-usbmanager-usbendpoint-i.md) parameters should be specified in this API. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [14400001](../errorcode-usb.md#14400001-usb-device-connection-denied) | Access right denied. Call requestRight to get the USBDevicePipe access right first. |
| [14400008](../errorcode-usb.md#14400008-no-device-disconnected) | No such device (it may have been disconnected). |
| [14400010](../errorcode-usb.md#14400010-unrecognized-error) | Other USB error. Possible causes:<br>1.Unrecognized discard error code. |
| [14400011](../errorcode-usb.md#14400011-no-ongoing-transfer-found) | The transfer is not in progress, or is already complete or cancelled. |

**Examples**

```TypeScript
> NOTE
> 
> The following sample code is only a basic process for calling the usbCancelTransfer API. When calling this API, you must comply with the protocol specifications of the target USB device to ensure proper data transfer and device compatibility. For details about the protocol requirements, see the technical documentation of the device.
```
