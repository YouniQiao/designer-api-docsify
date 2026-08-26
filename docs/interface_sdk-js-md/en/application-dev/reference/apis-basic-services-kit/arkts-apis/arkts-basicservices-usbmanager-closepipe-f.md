# closePipe

## Modules to Import

```TypeScript
import usbManager from '@kit.BasicServicesKit';
import serialManager from '@kit.BasicServicesKit.serial';
```

## closePipe

```TypeScript
function closePipe(pipe: USBDevicePipe): number
```

Closes a USB device pipe.
1. Call [usbManager.getDevices](arkts-basicservices-usbmanager-getdevices-f.md) to obtain the USB device list.
2. Call [usbManager.requestRight](arkts-basicservices-usbmanager-requestright-f.md) to request the device access permission.
3. Call [usbManager.connectDevice](arkts-basicservices-usbmanager-connectdevice-f.md) to obtain **devicepipe** as an input parameter.

**Since:** 9

**System capability:** SystemCapability.USB.USBManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pipe | [USBDevicePipe](arkts-basicservices-usbmanager-usbdevicepipe-i.md) | Yes | USB device pipe, which is used to determine the message control channel. You need to call [usbManager.connectDevice](arkts-basicservices-usbmanager-connectdevice-f.md) to obtain its value. |

**Return value:**

| Type | Description |
| --- | --- |
| number | Returns **0** if the USB device pipe is closed successfully; returns an error code otherwise. The error codes are as follows: |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes:  1.Mandatory parameters are left unspecified.  2.Incorrect parameter types. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported.<br>**Applicable version:** 18 and later |

**Examples**

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
