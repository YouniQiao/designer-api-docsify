# usbControlTransfer

## Modules to Import

```TypeScript
import { usbManager } from '@kit.BasicServicesKit';
```

## usbControlTransfer

```TypeScript
function usbControlTransfer(pipe: USBDevicePipe, requestparam: USBDeviceRequestParams, timeout?: number): Promise<number>
```

Performs control transfer. This API uses a promise to return the result.

**Since:** 12

**System capability:** SystemCapability.USB.USBManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pipe | [USBDevicePipe](arkts-basicservices-usbmanager-usbdevicepipe-i.md) | Yes | USB device pipe. You need to call [usbManager.connectDevice](arkts-basicservices-usbmanager-connectdevice-f.md) to obtain its value. |
| requestparam | [USBDeviceRequestParams](arkts-basicservices-usbmanager-usbdevicerequestparams-i.md) | Yes | Control transfer parameters. Set the parameters as required. For details, see the USB protocol. |
| timeout | number | No | Timeout interval.Unit: milliseconds. This parameter is optional. If the control transfer is complete within the specified time, the size of the transferred or received data block is returned; otherwise, a timeout error is returned. The default value is **0**, indicating that the system waits infinitely until the control transfer is complete. Set this parameter as required. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;number&gt; | Promise used to return the result, which is the size of the transferred or received data block if the transfer is successful. If the API call fails, the following error codes are returned: |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes:  1.Mandatory parameters are left unspecified.  2.Incorrect parameter types. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported.<br>**Applicable version:** 18 and later |

**Examples**

```TypeScript
import {BusinessError} from '@kit.BasicServicesKit';
// Control transfer parameters: Set each field based on the USB protocol specifications, device descriptor, or device specifications document.
// bmRequestType: request control type. Common values are as follows: 0x00 (standard request, from the host to the device), 0x20 (class request, from the host to the device), 0x40 (vendor request, from the host to the device), and 0x80 (standard request, from the device to the host).
// bRequest: specific control request command (such as obtaining a descriptor or setting an address)
// wValue: content of the request parameter
// wIndex: index of the request parameter
// wLength: data length
// data: buffer for writing or reading data
let param: usbManager.USBDeviceRequestParams = {
  bmRequestType: 0x80,
  bRequest: 0x06,
  wValue: 0x01 << 8 | 0,
  wIndex: 0,
  wLength: 18,
  data: new Uint8Array(18)
};

async function usbControlTransfer() {
  let devicesList: Array<usbManager.USBDevice> = usbManager.getDevices();
  if (!devicesList || devicesList.length == 0) {
    console.info(`device list is empty`);
    return;
  }

  let rightResult = await usbManager.requestRight(devicesList?.[0]?.name);
  if (!rightResult) {
    console.error(`request right failed`);
    return;
  }
  let devicePipe: usbManager.USBDevicePipe = usbManager.connectDevice(devicesList?.[0]);
  if (devicePipe == undefined) {
    console.error(`connect device failed`);
    return;
  }
  usbManager.usbControlTransfer(devicePipe, param).then((ret: number) => {
    console.info(`usbControlTransfer = ${ret}`);
  }).catch((error: BusinessError) => {
    console.error(`usbControlTransfer failed: ${error.code}, message: ${error.message}`);
  }).finally(() => {
    usbManager.closePipe(devicePipe);
  });
}
```
