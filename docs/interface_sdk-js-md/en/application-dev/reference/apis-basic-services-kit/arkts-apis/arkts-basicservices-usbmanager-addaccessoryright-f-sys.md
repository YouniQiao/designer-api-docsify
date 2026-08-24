# addAccessoryRight (System API)

## Modules to Import

```TypeScript
import { usbManager } from '@kit.BasicServicesKit';
```

## addAccessoryRight

```TypeScript
function addAccessoryRight(tokenId: int, accessory: USBAccessory): void
```

Adds the permission to applications for accessing USB accessories. [usbManager.requestAccessoryRight]{(@link usbManager.requestAccessoryRight)} triggers a dialog box to request user authorization. **addAccessoryRight** does not trigger a dialog box but directly adds the device access permission for the application.

**Since:** 23

**Required permissions:** ohos.permission.MANAGE_USB_CONFIG

<!--Device-usbManager-function addAccessoryRight(tokenId: int, accessory: USBAccessory): void--><!--Device-usbManager-function addAccessoryRight(tokenId: int, accessory: USBAccessory): void-End-->

**System capability:** SystemCapability.USB.USBManager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| tokenId | int | Yes | Token ID of the application. |
| accessory | [USBAccessory](arkts-basicservices-usbmanager-usbaccessory-i.md) | Yes | USB accessory. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | The permission check failed. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission denied. Normal application do not have permission to use system api. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes:<br>1. Mandatory parameters are left unspecified.<br>2. Incorrect parameter types. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported.<br>**Applicable version:** 18 and later |
| [14400004](../errorcode-usb.md#14400004-service-exception) | Service exception. Possible causes:<br>1. No accessory is plugged in. |
| [14400005](../errorcode-usb.md#14400005-database-operation-exception) | Database operation exception. |

**Examples**

```TypeScript
import { hilog } from '@kit.PerformanceAnalysisKit';
import { bundleManager } from '@kit.AbilityKit';

try {
  let accList: usbManager.USBAccessory[] = usbManager.getAccessoryList()
  let flags = bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_APPLICATION |
  bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_EXTENSION_ABILITY
  let bundleInfo = await bundleManager.getBundleInfoForSelf(flags)
  let tokenId: number = bundleInfo.appInfo.accessTokenId
  usbManager.addAccessoryRight(tokenId, accList[0])
  hilog.info(0, 'testTag ui', `addAccessoryRight success`)
} catch (error) {
  hilog.info(0, 'testTag ui', `addAccessoryRight error ${error.code}, message is ${error.message}`)
}
```

