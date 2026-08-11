# releaseInterface

## Modules to Import

```TypeScript
import { usbManager } from 'kits/@kit.BasicServicesKit';
```

## releaseInterface

```TypeScript
function releaseInterface(pipe: USBDevicePipe, iface: USBInterface): int
```

Releases the claimed communication interface.

> **NOTE：**
> 
> Before calling this API, call the
> [usbManager.claimInterface](arkts-basicservices-usbmanager-claiminterface-f.md#claiminterface)
> API to claim a communication interface.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-usbManager-function releaseInterface(pipe: USBDevicePipe, iface: USBInterface): int--><!--Device-usbManager-function releaseInterface(pipe: USBDevicePipe, iface: USBInterface): int-End-->

**System capability:** SystemCapability.USB.USBManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pipe | [USBDevicePipe](arkts-basicservices-usbmanager-usbdevicepipe-i.md) | Yes | USB device pipe, which is used to determine the bus number and device address. You need to call [usbManager.connectDevice](arkts-basicservices-usbmanager-connectdevice-f.md#connectdevice) to obtain its value. |
| iface | [USBInterface](arkts-basicservices-usb-usbinterface-i.md) | Yes | USB interface. You can use [usbManager.getDevices](arkts-basicservices-usbmanager-getdevices-f.md#getdevices) to obtain device information and identify the USB interface based on the ID. |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：int | Returns **0** if the USB interface is successfully released; returns an error code otherwise. The error codes are as follows: |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes:  &lt;br&gt;1.Mandatory parameters are left unspecified.  &lt;br&gt;2.Incorrect parameter types. |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported.<br>**Applicable version:** 18 and later |

## Examples

```TypeScript
function releaseInterface() {
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
  ret = usbManager.releaseInterface(devicepipe, interfaces);
  console.info(`releaseInterface = ${ret}`);
}
```

