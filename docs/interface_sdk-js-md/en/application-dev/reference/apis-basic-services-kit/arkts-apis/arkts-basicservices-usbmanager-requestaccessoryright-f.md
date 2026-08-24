# requestAccessoryRight

## Modules to Import

```TypeScript
import { usbManager } from '@kit.BasicServicesKit';
```

## requestAccessoryRight

```TypeScript
function requestAccessoryRight(accessory: USBAccessory): Promise<boolean>
```

Requests the permission to access a USB accessory for a specified application. This API uses a promise to return the result. You need to call [usbManager.getAccessoryList](arkts-basicservices-usbmanager-getaccessorylist-f.md) to obtain the accessory list and use [USBAccessory](arkts-basicservices-usbmanager-usbaccessory-i.md) as a parameter.

**Since:** 23

<!--Device-usbManager-function requestAccessoryRight(accessory: USBAccessory): Promise<boolean>--><!--Device-usbManager-function requestAccessoryRight(accessory: USBAccessory): Promise<boolean>-End-->

**System capability:** SystemCapability.USB.USBManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| accessory | [USBAccessory](arkts-basicservices-usbmanager-usbaccessory-i.md) | Yes | USB accessory, which is obtained through [getAccessoryList](arkts-basicservices-usbmanager-getaccessorylist-f.md). |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise used to return the application result. The value **true** indicates that the device access permissions are granted; **false** indicates the opposite. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes:<br>1. Mandatory parameters are left unspecified.<br>2. Incorrect parameter types. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported.<br>**Applicable version:** 18 and later |
| [14401001](../errorcode-usb.md#14401001-target-usb-accessory-unmatched) | The target USBAccessory not matched. |
| [14400004](../errorcode-usb.md#14400004-service-exception) | Service exception. Possible causes:<br>1. No accessory is plugged in. |
| [14400005](../errorcode-usb.md#14400005-database-operation-exception) | Database operation exception. |

**Examples**

```TypeScript
import { hilog } from '@kit.PerformanceAnalysisKit';
try {
  let accList: usbManager.USBAccessory[] = usbManager.getAccessoryList()
  let flag = usbManager.requestAccessoryRight(accList[0])
  hilog.info(0, 'testTag ui', `requestAccessoryRight success, ret:${flag}`)
} catch (error) {
  hilog.info(0, 'testTag ui', `requestAccessoryRight error ${error.code}, message is ${error.message}`)
}
```

