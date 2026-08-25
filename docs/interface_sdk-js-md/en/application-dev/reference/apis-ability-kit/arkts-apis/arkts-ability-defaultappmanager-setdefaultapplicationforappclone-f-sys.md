# setDefaultApplicationForAppClone (System API)

## Modules to Import

```TypeScript
import { defaultAppManager } from 'kits/@kit.AbilityKit';
```

## setDefaultApplicationForAppClone

```TypeScript
function setDefaultApplicationForAppClone(type: string, elementName: ElementName, appIndex: number, userId?: number): void
```

Sets an application clone as the default application of the specified type. This API returns the result synchronously.

**Since:** 23

**Required permissions:** ohos.permission.SET_DEFAULT_APPLICATION or (ohos.permission.SET_DEFAULT_APPLICATION and ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS)

**System capability:** SystemCapability.BundleManager.BundleFramework.DefaultApp

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | string | Yes |
| elementName | [ElementName](arkts-ability-elementname-i.md) | Yes |
| appIndex | number | Yes |
| userId | number | No |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [17700004](../errorcode-bundle.md#17700004-user-id-does-not-exist) |
| [17700025](../errorcode-bundle.md#17700025-invalid-type) |
| [17700028](../errorcode-bundle.md#17700028-mismatch-between-ability-and-type) |
| [17700061](../errorcode-bundle.md#17700061-appindex-for-a-clone-is-invalid) |
