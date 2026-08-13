# deleteDisposedStatusSync (System API)

## Modules to Import

```TypeScript
import { appControl } from '@kit.AbilityKit';
```

## deleteDisposedStatusSync

```TypeScript
function deleteDisposedStatusSync(appId: string, appIndex?: number): void
```

Deletes the disposed status for an application or an application clone. This API returns the result synchronously. If the operation is successful, **null** is returned. If the operation fails, an error message is returned.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.MANAGE_DISPOSED_APP_STATUS

<!--Device-appControl-function deleteDisposedStatusSync(appId: string, appIndex?: int): void--><!--Device-appControl-function deleteDisposedStatusSync(appId: string, appIndex?: int): void-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.AppControl

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| appId | string | Yes |
| appIndex | number | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [17700061](../errorcode-bundle.md#17700061-appindex-for-a-clone-is-invalid) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [17700005](../errorcode-bundle.md#17700005-appid-is-an-empty-string) |
