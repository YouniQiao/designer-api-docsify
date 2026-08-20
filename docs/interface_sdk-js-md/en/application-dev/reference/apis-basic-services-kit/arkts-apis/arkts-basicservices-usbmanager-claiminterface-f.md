# claimInterface

## Modules to Import

```TypeScript
import { usbManager } from '@kit.BasicServicesKit';
import { serialManager } from '@kit.BasicServicesKit';
```

## claimInterface

```TypeScript
function claimInterface(pipe: USBDevicePipe, iface: USBInterface, force?: boolean): int
```

Claims a USB device interface.

> **NOTE：**
> 
> In USB programming, **claimInterface** is a common operation, which indicates that an application requests the &gt; operating system to release a USB interface from the kernel driver and hand over the USB interface to a user &gt; space program for control.<br>
> 
> All the **claim** communication interfaces used below refer to the claim interface operations.

**Since:** 23

<!--Device-usbManager-function claimInterface(pipe: USBDevicePipe, iface: USBInterface, force?: boolean): int--><!--Device-usbManager-function claimInterface(pipe: USBDevicePipe, iface: USBInterface, force?: boolean): int-End-->

**System capability:** SystemCapability.USB.USBManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pipe | USBDevicePipe | Yes | USB device pipe, which is used to determine the bus number and device address. You need to call [usbManager.connectDevice](arkts-basicservices-usbmanager-connectdevice-f.md) to obtain its value. |
| iface | USBInterface | Yes | USB interface. You can use [usbManager.getDevices](arkts-basicservices-usbmanager-getdevices-f.md) to obtain device information and identify the USB interface based on the ID. |
| force | boolean | No | Whether to forcibly claim a USB interface. The default value is **false**, which means not to forcibly claim a USB interface. You can set the value as required. |

**Return value:**

| Type | Description |
| --- | --- |
| int | Returns **0** if the **claim** interface is called successfully; returns an error code otherwise. The error codes are as follows: |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes:  <br>1.Mandatory parameters are left unspecified.  <br>2.Incorrect parameter types. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported.<br>**Applicable version:** 18 and later |

**Examples**

```TypeScript
function claimInterface() {
  let devicesList: Array<usbManager.USBDevice> = usbManager.getDevices();
  if (!devicesList || devicesList.length == 0) {
    console.info(`device list is empty`);
    return;
  }

  let device: usbManager.USBDevice = devicesList[0];
  usbManager.requestRight(device.name);
  let devicepipe: usbManager.USBDevicePipe = usbManager.connectDevice(device);
  let interfaces: usbManager.USBInterface = device.configs[0].interfaces[0];
  let ret: number= usbManager.claimInterface(devicepipe, interfaces);
  console.info(`claimInterface = ${ret}`);
}
```

