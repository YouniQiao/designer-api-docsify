# getAllDynamicIconInfo (System API)

## Modules to Import

```TypeScript
import { bundleManager } from 'kits/@kit.AbilityKit';
```

## getAllDynamicIconInfo

```TypeScript
function getAllDynamicIconInfo(userId?: number): Promise<Array<DynamicIconInfo>>
```

Obtains the dynamic icon information of all applications and all application clones of a specified user. This API uses a promise to return the result.To obtain the dynamic icon information of all applications and all application clones of the current user, you must request the ohos.permission.GET_BUNDLE_INFO_PRIVILEGED permission.To obtain the dynamic icon information of all applications and all application clones of other users or all users, you must request the ohos.permission.GET_BUNDLE_INFO_PRIVILEGED and ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS permissions.

**Since:** 20

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED and ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| userId | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;DynamicIconInfo & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [17700004](../errorcode-bundle.md#17700004-user-id-does-not-exist) |
| [17700306](../errorcode-bundle.md#17700306-failed-to-obtain-the-dynamic-icon) |
