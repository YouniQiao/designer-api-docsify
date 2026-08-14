# connectDevice

## Modules to Import

```TypeScript
import { usbManager } from 'usbManager';
```

## connectDevice

```TypeScript
function connectDevice(device: USBDevice): Readonly<USBDevicePipe>
```

Connects to the USB device based on the device information returned by **getDevices()**. If the USB service is abnormal, **undefined** may be returned. Check whether the return value of the API is empty. 1. Call [usbManager.getDevices](arkts-basicservices-usbmanager-getdevices-f.md#getDevices) to obtain the USB device list. 2. Call [usbManager.requestRight](arkts-basicservices-usbmanager-requestright-f.md#requestRight) to request the device access permission.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-usbManager-function connectDevice(device: USBDevice): Readonly<USBDevicePipe>--><!--Device-usbManager-function connectDevice(device: USBDevice): Readonly<USBDevicePipe>-End-->

**System capability:** SystemCapability.USB.USBManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| device | USBDevice | Yes | USB device. The **busNum** and **devAddress** parameters obtained by [usbManager.getDevices](arkts-basicservices-usbmanager-getdevices-f.md#getDevices) are used to determine a USB device. Other parameters are passed transparently. |

**Return value:**

| Type | Description |
| --- | --- |
| [Readonly](../../apis-na/arkts-apis/arkts-na-readonly-t.md)&lt;USBDevicePipe&gt; | USB device pipe for data transfer. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes:  <br>1.Mandatory parameters are left unspecified.  <br>2.Incorrect parameter types. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported.<br>**Applicable version:** 18 and later |
| [14400012](../../apis-basic-services-kit/errorcode-usb.md#14400012-io-error) | Transmission I/O error.<br>**Applicable version:** 23 and later  **ArkTS mode:** This error code applies only to ArkTS-Sta. |
| [14400001](../../apis-basic-services-kit/errorcode-usb.md#14400001-usb-device-connection-denied) | Access right denied. Call requestRight to get the USBDevicePipe access right first. |
| [14400004](../../apis-basic-services-kit/errorcode-usb.md#14400004-service-exception) | Service exception. Possible causes:  <br>1. No accessory is plugged in.<br>**Applicable version:** 23 and later  **ArkTS mode:** This error code applies only to ArkTS-Sta. |

## Examples

```TypeScript
function connectDevice() {
  let devicesList: Array<usbManager.USBDevice> = usbManager.getDevices();
  if (!devicesList || devicesList.length == 0) {
    console.info(`device list is empty`);
    return;
  }

  let device: usbManager.USBDevice = devicesList[0];
  usbManager.requestRight(device.name);
  let devicepipe: usbManager.USBDevicePipe = usbManager.connectDevice(device);
  console.info(`devicepipe = ${devicepipe}`);
}
```

