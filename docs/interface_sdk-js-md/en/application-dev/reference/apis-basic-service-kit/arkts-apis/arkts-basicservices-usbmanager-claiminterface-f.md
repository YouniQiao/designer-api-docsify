# claimInterface

## Modules to Import

```TypeScript
import { usbManager } from 'kits/@kit.BasicServicesKit';
```

## claimInterface

```TypeScript
function claimInterface(pipe: USBDevicePipe, iface: USBInterface, force?: boolean): int
```

Claims a USB device interface.

> **NOTE：**
> 
> In USB programming, **claimInterface** is a common operation, which indicates that an application requests the
> operating system to release a USB interface from the kernel driver and hand over the USB interface to a user
> space program for control.&lt;br&gt;
> > All the **claim** communication interfaces used below refer to the claim interface operations.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-usbManager-function claimInterface(pipe: USBDevicePipe, iface: USBInterface, force?: boolean): int--><!--Device-usbManager-function claimInterface(pipe: USBDevicePipe, iface: USBInterface, force?: boolean): int-End-->

**System capability:** SystemCapability.USB.USBManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pipe | [USBDevicePipe](arkts-basicservices-usbmanager-usbdevicepipe-i.md) | Yes | USB device pipe, which is used to determine the bus number and device address. You need to call [usbManager.connectDevice](arkts-basicservices-usbmanager-connectdevice-f.md#connectdevice) to obtain its value. |
| iface | [USBInterface](arkts-basicservices-usb-usbinterface-i.md) | Yes | USB interface. You can use [usbManager.getDevices](arkts-basicservices-usbmanager-getdevices-f.md#getdevices) to obtain device information and identify the USB interface based on the ID. |
| force | boolean | No | Whether to forcibly claim a USB interface. The default value is **false**, which means not to forcibly claim a USB interface. You can set the value as required. |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：int | Returns **0** if the **claim** interface is called successfully; returns an error code otherwise. The error codes are as follows: |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes:  &lt;br&gt;1.Mandatory parameters are left unspecified.  &lt;br&gt;2.Incorrect parameter types. |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported.<br>**Applicable version:** 18 and later |

## Examples

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

