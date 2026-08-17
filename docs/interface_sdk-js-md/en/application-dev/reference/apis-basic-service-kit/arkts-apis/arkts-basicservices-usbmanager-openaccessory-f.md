# openAccessory

## Modules to Import

```TypeScript
import { usbManager } from 'usbManager';
```

## openAccessory

```TypeScript
function openAccessory(accessory: USBAccessory): USBAccessoryHandle
```

Obtains the accessory handle and opens the accessory file descriptor. Then, the host can communicate with the accessory through the **read** and **write** APIs provided by Core File Kit. You need to call [usbManager.getAccessoryList](arkts-basicservices-usbmanager-getaccessorylist-f.md#getaccessorylist) to obtain the accessory list and use [USBAccessory](arkts-basicservices-usbmanager-usbaccessory-i.md#usbaccessory) as a parameter.

**Since:** 23

<!--Device-usbManager-function openAccessory(accessory: USBAccessory): USBAccessoryHandle--><!--Device-usbManager-function openAccessory(accessory: USBAccessory): USBAccessoryHandle-End-->

**System capability:** SystemCapability.USB.USBManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| accessory | [USBAccessory](arkts-basicservices-usbmanager-usbaccessory-i.md) | Yes | USB accessory, which is obtained through [getAccessoryList](arkts-basicservices-usbmanager-getaccessorylist-f.md#getaccessorylist). |

**Return value:**

| Type | Description |
| --- | --- |
| [USBAccessoryHandle](arkts-basicservices-usbmanager-usbaccessoryhandle-i.md) | USB accessory handle. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [14401003](../../apis-basic-services-kit/errorcode-usb.md#14401003-accessory-opened-repeatedly) | Cannot reopen the accessory. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes:  <br>1. Mandatory parameters are left unspecified.  <br>2. Incorrect parameter types. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported.<br>**Applicable version:** 18 and later |
| [14401002](../../apis-basic-services-kit/errorcode-usb.md#14401002-failed-to-open-the-native-accessory-node) | Failed to open the native accessory node. |
| [14401001](../../apis-basic-services-kit/errorcode-usb.md#14401001-target-usb-accessory-unmatched) | The target USBAccessory not matched. |
| [14400001](../../apis-basic-services-kit/errorcode-usb.md#14400001-usb-device-connection-denied) | Access right denied. Call requestRight to get the USBDevicePipe access right first. |
| [14400004](../../apis-basic-services-kit/errorcode-usb.md#14400004-service-exception) | Service exception. Possible causes:  <br>1. No accessory is plugged in. |

**Examples**

```TypeScript
import { hilog } from '@kit.PerformanceAnalysisKit';
import { fileIo as fs } from '@kit.CoreFileKit';
try {
  let accList: usbManager.USBAccessory[] = usbManager.getAccessoryList()
  let flag = usbManager.requestAccessoryRight(accList[0])
  let handle = usbManager.openAccessory(accList[0])
  hilog.info(0, 'testTag ui', `openAccessory success`)
  let arrayBuffer = new ArrayBuffer(4096);
  let readLength = fs.readSync(handle.accessoryFd, arrayBuffer, {offset: 0, length: 4096});
  hilog.info(0, 'testTag ui', 'readSync ret: ' + readLength.toString(10));
} catch (error) {
  hilog.info(0, 'testTag ui', `openAccessory error ${error.code}, message is ${error.message}`)
}
```

