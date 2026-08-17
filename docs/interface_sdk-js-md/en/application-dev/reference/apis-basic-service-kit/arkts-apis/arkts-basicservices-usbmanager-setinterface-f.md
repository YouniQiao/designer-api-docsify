# setInterface

## Modules to Import

```TypeScript
import { usbManager } from 'usbManager';
```

## setInterface

```TypeScript
function setInterface(pipe: USBDevicePipe, iface: USBInterface): int
```

Sets a USB interface. > **NOTE：**> > A USB interface may have multiple selection modes and supports dynamic switching. It is used to reset the > endpoint to match the transmission type during data transmission. > > Before calling this API, call the > [usbManager.claimInterface](arkts-basicservices-usbmanager-claiminterface-f.md#claiminterface) > API to claim a communication interface.

**Since:** 23

<!--Device-usbManager-function setInterface(pipe: USBDevicePipe, iface: USBInterface): int--><!--Device-usbManager-function setInterface(pipe: USBDevicePipe, iface: USBInterface): int-End-->

**System capability:** SystemCapability.USB.USBManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pipe | USBDevicePipe | Yes | USB device pipe, which is used to determine the bus number and device address. You need to call [usbManager.connectDevice](arkts-basicservices-usbmanager-connectdevice-f.md#connectdevice) to obtain its value. |
| iface | USBInterface | Yes | USB interface. You can use [usbManager.getDevices](arkts-basicservices-usbmanager-getdevices-f.md#getdevices) to obtain device information and identify the USB interface based on its **id** and **alternateSetting**. |

**Return value:**

| Type | Description |
| --- | --- |
| int | Returns **0** if the USB interface is successfully set; returns an error code otherwise. The error codes are as follows: |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes:  <br>1.Mandatory parameters are left unspecified.  <br>2.Incorrect parameter types. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported.<br>**Applicable version:** 18 and later |

**Examples**

```TypeScript
function setInterface() {
  let devicesList: Array<usbManager.USBDevice> = usbManager.getDevices();
  if (!devicesList || devicesList.length == 0) {
    console.info(`device list is empty`);
    return;
  }

  let device: usbManager.USBDevice = devicesList[0];
  usbManager.requestRight(device.name);
  let devicepipe: usbManager.USBDevicePipe = usbManager.connectDevice(device);
  let interfaces: usbManager.USBInterface = device.configs[0].interfaces[0];
  let ret: number = usbManager.claimInterface(devicepipe, interfaces);
  ret = usbManager.setInterface(devicepipe, interfaces);
  console.info(`setInterface = ${ret}`);
}
```

