# connectDevice

## Modules to Import

```TypeScript
import { usbManager } from '@kit.BasicServicesKit';
import { serialManager } from '@kit.BasicServicesKit';
```

## connectDevice

```TypeScript
function connectDevice(device: USBDevice): Readonly<USBDevicePipe>
```

Connects to the USB device based on the device information returned by **getDevices()**. If the USB service is abnormal, **undefined** may be returned. Check whether the return value of the API is empty.

1. Call [usbManager.getDevices](arkts-basicservices-usbmanager-getdevices-f.md) to obtain the USB device list. 2. Call [usbManager.requestRight](arkts-basicservices-usbmanager-requestright-f.md) to request the device access permission.

**Since:** 23

<!--Device-usbManager-function connectDevice(device: USBDevice): Readonly<USBDevicePipe>--><!--Device-usbManager-function connectDevice(device: USBDevice): Readonly<USBDevicePipe>-End-->

**System capability:** SystemCapability.USB.USBManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| device | USBDevice | Yes | USB device. The **busNum** and **devAddress** parameters obtained by [usbManager.getDevices](arkts-basicservices-usbmanager-getdevices-f.md) are used to determine a USB device. Other parameters are passed transparently. |

**Return value:**

| Type | Description |
| --- | --- |
| [Readonly](../../apis-default/arkts-apis/arkts-readonly-t.md)&lt;USBDevicePipe&gt; | USB device pipe for data transfer. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes:  <br>1.Mandatory parameters are left unspecified.  <br>2.Incorrect parameter types. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported.<br>**Applicable version:** 18 and later |
| [14400001](../errorcode-usb.md#14400001-usb-device-connection-denied) | Access right denied. Call requestRight to get the USBDevicePipe access right first. |
| [14400004](../errorcode-usb.md#14400004-service-exception) |  |
| [14400012](../errorcode-usb.md#14400012-io-error) |  |

**Examples**

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

