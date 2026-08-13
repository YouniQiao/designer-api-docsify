# deactivateUserKey (System API)

## Modules to Import

```TypeScript
import { keyManager } from '@kit.CoreFileKit';
```

## deactivateUserKey

```TypeScript
function deactivateUserKey(userId: number):void
```

When the screen is locked, the specified user key is uninstalled synchronously. **(Currently, this API is available only to lock screen applications.)**

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.STORAGE_MANAGER_CRYPT

<!--Device-keyManager-function deactivateUserKey(userId: long):void--><!--Device-keyManager-function deactivateUserKey(userId: long):void-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Encryption

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| userId | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| 13600009 |
| 13600008 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 13600001 |

## Examples

```TypeScript
import { keyManager } from "@kit.CoreFileKit";
import { BusinessError } from '@kit.BasicServicesKit';
let userId: number = 100;
try {
  keyManager.deactivateUserKey(userId);
  console.info("deactivateUserKey success");
} catch (err) {
  let error: BusinessError = err as BusinessError;
  console.error("deactivateUserKey failed with error:" + JSON.stringify(error));
}
```
