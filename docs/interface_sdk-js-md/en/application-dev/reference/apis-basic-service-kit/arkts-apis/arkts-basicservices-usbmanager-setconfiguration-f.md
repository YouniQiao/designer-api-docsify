# setConfiguration

## Modules to Import

```TypeScript
import { usbManager } from 'usbManager';
```

## setConfiguration

```TypeScript
function setConfiguration(pipe: USBDevicePipe, config: USBConfiguration): int
```

Sets the device configuration.

**Since:** 23

<!--Device-usbManager-function setConfiguration(pipe: USBDevicePipe, config: USBConfiguration): int--><!--Device-usbManager-function setConfiguration(pipe: USBDevicePipe, config: USBConfiguration): int-End-->

**System capability:** SystemCapability.USB.USBManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pipe | USBDevicePipe | Yes | USB device pipe, which is used to determine the bus number and device address. You need to call [usbManager.connectDevice](arkts-basicservices-usbmanager-connectdevice-f.md#connectdevice) to obtain its value. |
| config | [USBConfiguration](arkts-basicservices-usbmanager-usbconfiguration-i.md) | Yes | USB configuration. You can use [usbManager.getDevices](arkts-basicservices-usbmanager-getdevices-f.md#getdevices) to obtain device information and identify the USB configuration based on the ID. |

**Return value:**

| Type | Description |
| --- | --- |
| int | Returns **0** if the USB configuration is successfully set; returns an error code otherwise. The error codes are as follows: |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes:  <br>1.Mandatory parameters are left unspecified.  <br>2.Incorrect parameter types. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported.<br>**Applicable version:** 18 and later |

**Examples**

```TypeScript
function setConfiguration() {
  let devicesList: Array<usbManager.USBDevice> = usbManager.getDevices();
  if (!devicesList || devicesList.length == 0) {
    console.info(`device list is empty`);
    return;
  }

  let device: usbManager.USBDevice = devicesList[0];
  usbManager.requestRight(device.name);
  let devicepipe: usbManager.USBDevicePipe = usbManager.connectDevice(device);
  let config: usbManager.USBConfiguration = device.configs[0];
  let ret: number= usbManager.setConfiguration(devicepipe, config);
  console.info(`setConfiguration = ${ret}`);
}
```

