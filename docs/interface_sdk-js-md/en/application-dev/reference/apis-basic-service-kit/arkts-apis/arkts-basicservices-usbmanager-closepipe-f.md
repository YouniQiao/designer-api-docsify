# closePipe

## Modules to Import

```TypeScript
import { usbManager } from 'usbManager';
```

## closePipe

```TypeScript
function closePipe(pipe: USBDevicePipe): int
```

Closes a USB device pipe. 1. Call [usbManager.getDevices](arkts-basicservices-usbmanager-getdevices-f.md#getDevices) to obtain the USB device list. 2. Call [usbManager.requestRight](arkts-basicservices-usbmanager-requestright-f.md#requestRight) to request the device access permission. 3. Call [usbManager.connectDevice](arkts-basicservices-usbmanager-connectdevice-f.md#connectDevice) to obtain **devicepipe** as an input parameter.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-usbManager-function closePipe(pipe: USBDevicePipe): int--><!--Device-usbManager-function closePipe(pipe: USBDevicePipe): int-End-->

**System capability:** SystemCapability.USB.USBManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pipe | USBDevicePipe | Yes | USB device pipe, which is used to determine the message control channel. You need to call [usbManager.connectDevice](arkts-basicservices-usbmanager-connectdevice-f.md#connectDevice) to obtain its value. |

**Return value:**

| Type | Description |
| --- | --- |
| int | Returns **0** if the USB device pipe is closed successfully; returns an error code otherwise. The error codes are as follows: |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes:  <br>1.Mandatory parameters are left unspecified.  <br>2.Incorrect parameter types. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported.<br>**Applicable version:** 18 and later |

## Examples

```TypeScript
function closePipe() {
  let devicesList: Array<usbManager.USBDevice> = usbManager.getDevices();
  if (!devicesList || devicesList.length == 0) {
    console.info(`device list is empty`);
    return;
  }

  usbManager.requestRight(devicesList[0].name);
  let devicepipe: usbManager.USBDevicePipe = usbManager.connectDevice(devicesList[0]);
  let ret: number = usbManager.closePipe(devicepipe);
  console.info(`closePipe = ${ret}`);
}
```

