# notifyDialogResult (System API)

## Modules to Import

```TypeScript
import { access } from 'kits/@kit.ConnectivityKit';
```

## notifyDialogResult

```TypeScript
function notifyDialogResult(notifyDialogResultParams: NotifyDialogResultParams): Promise<void>
```

Notify bluetooth the result of bluetooth dialog.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH and ohos.permission.MANAGE_BLUETOOTH

<!--Device-access-function notifyDialogResult(notifyDialogResultParams: NotifyDialogResultParams): Promise<void>--><!--Device-access-function notifyDialogResult(notifyDialogResultParams: NotifyDialogResultParams): Promise<void>-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| notifyDialogResultParams | [NotifyDialogResultParams](arkts-connectivity-access-notifydialogresultparams-i-sys.md) | Yes | Indicates the params for dialog result. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Returns the promise object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported. |
| 201 | Permission denied. |
| 202 | Non-system applications are not allowed to use system APIs. |
| 2900001 | Service stopped. |
| 2900099 | Operation failed. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
try {
    let notifyDialogResultParams: access.NotifyDialogResultParams = {
        "dialogType": 0,
        "dialogResult": true,
    };
    access.notifyDialogResult(notifyDialogResultParams);
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

