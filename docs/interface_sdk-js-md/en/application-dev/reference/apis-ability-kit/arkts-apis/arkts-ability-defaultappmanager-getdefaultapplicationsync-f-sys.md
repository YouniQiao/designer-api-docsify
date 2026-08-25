# getDefaultApplicationSync (System API)

## Modules to Import

```TypeScript
import { defaultAppManager } from 'kits/@kit.AbilityKit';
```

## getDefaultApplicationSync

```TypeScript
function getDefaultApplicationSync(type: string, userId?: number): BundleInfo
```

Obtains the default application based on a system-defined application type, a file type that complies with the media type format (either specified by **type** or **subtype**), or a [uniform data type](../../apis-arkdata/arkts-apis/arkts-data-uniformtypedescriptor.md). This API returns the result synchronously.

**Since:** 10

**Required permissions:** ohos.permission.GET_DEFAULT_APPLICATION

**System capability:** SystemCapability.BundleManager.BundleFramework.DefaultApp

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | string | Yes |
| userId | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [BundleInfo](arkts-ability-bundleinfo-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [17700004](../errorcode-bundle.md#17700004-user-id-does-not-exist) |
| [17700023](../errorcode-bundle.md#17700023-default-application-does-not-exist) |
| [17700025](../errorcode-bundle.md#17700025-invalid-type) |
