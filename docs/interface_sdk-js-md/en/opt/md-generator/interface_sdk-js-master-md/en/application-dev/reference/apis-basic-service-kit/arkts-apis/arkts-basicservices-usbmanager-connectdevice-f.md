# connectDevice

## Modules to Import

```TypeScript
import { usbManager } from '@kit.BasicServicesKit';
```

## connectDevice

```TypeScript
function connectDevice(device: USBDevice): Readonly<USBDevicePipe>
```

Connects to the USB device based on the device information returned by **getDevices()**. If the USB service is abnormal, **undefined** may be returned. Check whether the return value of the API is empty.

1. Call [usbManager.getDevices](arkts-basicservices-usbmanager-getdevices-f.md#getDevices) to obtain the USB device list.2. Call [usbManager.requestRight](arkts-basicservices-usbmanager-requestright-f.md#requestRight) to request the device access permission.

**Since:** 9

<!--Device-usbManager-function connectDevice(device: USBDevice): Readonly<USBDevicePipe>--><!--Device-usbManager-function connectDevice(device: USBDevice): Readonly<USBDevicePipe>-End-->

**System capability:** SystemCapability.USB.USBManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| device | [USBDevice](arkts-basicservices-usb-usbdevice-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Readonly](../../apis-default/arkts-apis/arkts-readonly-t.md)&lt;USBDevicePipe&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [14400012](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-usb.md#14400012-io-error) |
| [14400001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-usb.md#14400001-usb-device-connection-denied) |
| [14400004](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-usb.md#14400004-service-exception) |

## Examples

```TypeScript
function connectDevice() {
  let devicesList: Array<usbManager.USBDevice> = usbManager.getDevices();
  if (!devicesList || devicesList.length == 0) {
    console.info(`device list is empty`);
    return;
  }

  let device: usbManager.USBDevice = devicesList?.[0];
  usbManager.requestRight(device.name);
  let devicepipe: usbManager.USBDevicePipe = usbManager.connectDevice(device);
  console.info(`devicepipe = ${devicepipe}`);
}
```
