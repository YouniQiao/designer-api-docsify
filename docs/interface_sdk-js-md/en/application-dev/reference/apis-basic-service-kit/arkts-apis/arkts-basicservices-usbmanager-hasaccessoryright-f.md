# hasAccessoryRight

## Modules to Import

```TypeScript
import { usbManager } from 'kits/@kit.BasicServicesKit';
```

## hasAccessoryRight

```TypeScript
function hasAccessoryRight(accessory: USBAccessory): boolean
```

Checks whether the application has the permission to access the USB accessory.You need to call [usbManager.getAccessoryList](arkts-basicservices-usbmanager-getaccessorylist-f.md#getaccessorylist) to obtain the accessory list and use [USBAccessory](arkts-basicservices-usbmanager-usbaccessory-i.md) as a parameter.

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-usbManager-function hasAccessoryRight(accessory: USBAccessory): boolean--><!--Device-usbManager-function hasAccessoryRight(accessory: USBAccessory): boolean-End-->

**System capability:** SystemCapability.USB.USBManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| accessory | [USBAccessory](arkts-basicservices-usbmanager-usbaccessory-i.md) | Yes | USB accessory, which is obtained through [getAccessoryList](arkts-basicservices-usbmanager-getaccessorylist-f.md#getaccessorylist). |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | The value **true** indicates that the application has the permission to access the USB accessory; *false** indicates the opposite. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes:  &lt;br&gt;1. Mandatory parameters are left unspecified.  &lt;br&gt;2. Incorrect parameter types. |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported.<br>**Applicable version:** 18 and later |
| [14401001](../../apis-basic-services-kit/errorcode-usb.md#14401001-target-usb-accessory-unmatched) | The target USBAccessory not matched. |
| [14400005](../../apis-basic-services-kit/errorcode-usb.md#14400005-database-operation-exception) | Database operation exception. |
| [14400004](../../apis-basic-services-kit/errorcode-usb.md#14400004-service-exception) | Service exception. Possible causes:  &lt;br&gt;1. No accessory is plugged in. |

## Examples

```TypeScript
import { hilog } from '@kit.PerformanceAnalysisKit';
try {
  let accList: usbManager.USBAccessory[] = usbManager.getAccessoryList()
  let flag = usbManager.hasAccessoryRight(accList[0])
  hilog.info(0, 'testTag ui', `hasAccessoryRight success, ret:${flag}`)
} catch (error) {
  hilog.info(0, 'testTag ui', `hasAccessoryRight error ${error.code}, message is ${error.message}`)
}
```

