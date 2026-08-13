# usbSubmitTransfer

## Modules to Import

```TypeScript
import { usbManager } from '@kit.BasicServicesKit';
```

## usbSubmitTransfer

```TypeScript
function usbSubmitTransfer(transfer: UsbDataTransferParams): void
```

Requests a USB data transfer. > **NOTE：**> > This API uses an asynchronous callback to return the result. > > Before calling this API, call the > [usbManager.claimInterface](arkts-basicservices-usbmanager-claiminterface-f.md#claimInterface) > API to claim a communication interface.

**Since:** 23

**Deprecated since:** -1

<!--Device-usbManager-function usbSubmitTransfer(transfer: UsbDataTransferParams): void--><!--Device-usbManager-function usbSubmitTransfer(transfer: UsbDataTransferParams): void-End-->

**System capability:** SystemCapability.USB.USBManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| transfer | [UsbDataTransferParams](arkts-basicservices-usbmanager-usbdatatransferparams-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [14400009](../../apis-basic-services-kit/errorcode-usb.md#14400009-insufficient-memory) |
| [14400008](../../apis-basic-services-kit/errorcode-usb.md#14400008-no-device-disconnected) |
| [14400012](../../apis-basic-services-kit/errorcode-usb.md#14400012-io-error) |
| [14400001](../../apis-basic-services-kit/errorcode-usb.md#14400001-usb-device-connection-denied) |
| [14400007](../../apis-basic-services-kit/errorcode-usb.md#14400007-resource-busy) |

## Examples

The following sample code shows the basic process for calling the usbSubmitTransfer API and it needs to be executed in a specific method. In actual calling, you must comply with the device-related protocols to ensure correct data transfer and device compatibility.

```TypeScript
// Call usbManager.getDevices to obtain a data set. Then, obtain a USB device and its access permission.
// Pass the obtained USB device as a parameter to usbManager.connectDevice. Then, call usbManager.connectDevice to connect the USB device.
// Call usbManager.claimInterface to claim a USB interface. After that, call usbManager.bulkTransfer to start bulk transfer.
function usbSubmitTransfer() {
  let devicesList: Array<usbManager.USBDevice> = usbManager.getDevices();
  if (!devicesList || devicesList.length == 0) {
    console.info(`device list is empty`);
    return;
  }
  let device: usbManager.USBDevice = devicesList?.[0];
  usbManager.requestRight(device.name);
  if (!usbManager.hasRight(device.name)) {
    console.info(`request right fail`);
    return;
  }
  let devicepipe: usbManager.USBDevicePipe = usbManager.connectDevice(device);
  // Obtain the endpoint address.
  let endpoint = device.configs?.[0]?.interfaces?.[0]?.endpoints.find((value) => {
    return value.direction === 0 && value.type === 2
  })
  // Obtain the first ID of the device.
  let ret: number = usbManager.claimInterface(devicepipe, device.configs?.[0]?.interfaces?.[0], true);

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
    console.info('USB transfer request submitted.');
  } catch (error) {
    console.error('USB transfer failed:', error);
  }
}
```
