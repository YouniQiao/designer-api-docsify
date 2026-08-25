# isApplicationDisableForbidden (System API)

## Modules to Import

```TypeScript
import { bundleManager } from 'kits/@kit.AbilityKit';
```

## isApplicationDisableForbidden

```TypeScript
function isApplicationDisableForbidden(bundleName: string, userId: number, appIndex: number): boolean
```

Synchronously queries whether a specified application or application clone of a specified user is set to forbid being disabled. If you need to check whether an application is forbidden to be disabled under the current user, ohos.permission.GET_BUNDLE_INFO_PRIVILEGED needs to be applied for. If you need to check whether an application is forbidden to be disabled under other users, ohos.permission.GET_BUNDLE_INFO_PRIVILEGED and ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS need to be applied for.

**Since:** 24

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED or (ohos.permission.GET_BUNDLE_INFO_PRIVILEGED and ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS)

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |
| userId | number | Yes |
| appIndex | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [17700001](../errorcode-bundle.md#17700001-bundle-name-does-not-exist) |
| [17700004](../errorcode-bundle.md#17700004-user-id-does-not-exist) |
| [17700061](../errorcode-bundle.md#17700061-appindex-for-a-clone-is-invalid) |
