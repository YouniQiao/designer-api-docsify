# usbCancelTransfer

## Modules to Import

```TypeScript
import { usbManager } from '@kit.BasicServicesKit';
```

## usbCancelTransfer

```TypeScript
function usbCancelTransfer(transfer: UsbDataTransferParams): void
```

Cancels an asynchronous USB data transfer request. > **NOTE：**> > This API is used to proactively cancel an unfinished USB data transfer request (for example, the one submitted by > **usbSubmitTransfer**). > Before calling this API, call the > [usbManager.claimInterface](arkts-basicservices-usbmanager-claiminterface-f.md#claimInterface) > API to claim a communication interface.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-usbManager-function usbCancelTransfer(transfer: UsbDataTransferParams): void--><!--Device-usbManager-function usbCancelTransfer(transfer: UsbDataTransferParams): void-End-->

**System capability:** SystemCapability.USB.USBManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| transfer | [UsbDataTransferParams](arkts-basicservices-usbmanager-usbdatatransferparams-i.md) | Yes | Only the [USBDevicePipe](arkts-basicservices-usbmanager-usbdevicepipe-i.md#USBDevicePipe) and [USBEndpoint](arkts-basicservices-usbmanager-usbendpoint-i.md#USBEndpoint) parameters should be specified in this API. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [14400011](../../apis-basic-services-kit/errorcode-usb.md#14400011-no-ongoing-transfer-found) | The transfer is not in progress, or is already complete or cancelled. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [14400010](../../apis-basic-services-kit/errorcode-usb.md#14400010-unrecognized-error) | Other USB error. Possible causes:  &lt;br&gt;1.Unrecognized discard error code. |
| [14400008](../../apis-basic-services-kit/errorcode-usb.md#14400008-no-device-disconnected) | No such device (it may have been disconnected). |
| [14400001](../../apis-basic-services-kit/errorcode-usb.md#14400001-usb-device-connection-denied) | Access right denied. Call requestRight to get the USBDevicePipe access right first. |

## Examples

The following sample code shows the basic process for calling the usbCancelTransfer API and it needs to be executed in a specific method. In actual calling, you must comply with the device-related protocols to ensure correct data transfer and device compatibility.

```TypeScript
// Call usbManager.getDevices to obtain a data set. Then, obtain a USB device and its access permission.
// Pass the obtained USB device as a parameter to usbManager.connectDevice. Then, call usbManager.connectDevice to connect the USB device.
// Call usbManager.claimInterface to claim a USB interface. After that, call usbManager.bulkTransfer to start bulk transfer.
function usbCancelTransfer() {
  let devicesList: Array<usbManager.USBDevice> = usbManager.getDevices();
  if (!devicesList || devicesList.length == 0) {
    console.info(`device list is empty`);
    return;
  }
  let device: usbManager.USBDevice = devicesList[0];
  usbManager.requestRight(device.name);
  let devicepipe: usbManager.USBDevicePipe = usbManager.connectDevice(device);
  // Obtain the endpoint address.
  let endpoint = device.configs[0].interfaces[0]?.endpoints.find((value) => {
    return value.direction === 0 && value.type === 2
  })
  // Obtain the first ID of the device.
  let ret: number = usbManager.claimInterface(devicepipe, device.configs[0].interfaces[0], true);
  let transferParams: usbManager.UsbDataTransferParams = {
    devPipe: devicepipe,
    flags: usbManager.UsbTransferFlags.USB_TRANSFER_SHORT_NOT_OK,
    endpoint: 1,
    type: usbManager.UsbEndpointTransferType.TRANSFER_TYPE_BULK,
    timeout: 2000,
    length: 10, 
    callback: () => {},
    userData: new Uint8Array(10),
    buffer: new Uint8Array(10),
    isoPacketCount: 0,
  };
  try {
    transferParams.endpoint=endpoint?.address as number;
    transferParams.callback=(err, callBackData: usbManager.SubmitTransferCallback)=>{
      console.info('callBackData =' +JSON.stringify(callBackData));
    }
    usbManager.usbSubmitTransfer(transferParams);
    usbManager.usbCancelTransfer(transferParams);
    console.info('USB transfer request submitted.');
  } catch (error) {
    console.error('USB transfer failed:', error);
  }
}
```

