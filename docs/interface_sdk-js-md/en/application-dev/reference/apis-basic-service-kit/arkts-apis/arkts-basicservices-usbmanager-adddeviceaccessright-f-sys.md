# addDeviceAccessRight (System API)

## Modules to Import

```TypeScript
import { usbManager } from 'usbManager';
```

## addDeviceAccessRight

```TypeScript
function addDeviceAccessRight(tokenId: string, deviceName: string): boolean
```

Adds the device access permission for the application. System applications are granted the device access permission by default, and calling this API will not revoke the permission. [usbManager.requestRight]{(@link usbManager.requestRight)} triggers a dialog box to request for user authorization, whereas addDeviceAccessRight adds the access permission directly without displaying a dialog box.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Required permissions:** ohos.permission.MANAGE_USB_CONFIG

<!--Device-usbManager-function addDeviceAccessRight(tokenId: string, deviceName: string): boolean--><!--Device-usbManager-function addDeviceAccessRight(tokenId: string, deviceName: string): boolean-End-->

**System capability:** SystemCapability.USB.USBManager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| tokenId | string | Yes | Token ID of the software package. |
| deviceName | string | Yes | Device name. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Permission addition result. The value **true** indicates that the access permission is added successfully; and the value **false** indicates the opposite. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes:  <br>1.Mandatory parameters are left unspecified.  <br>2.Incorrect parameter types. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported.<br>**Applicable version:** 18 and later |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API.<br>**Applicable version:** 18 and later |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission denied. Normal application do not have permission to use system api. |

