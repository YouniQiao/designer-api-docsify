# getAbilityInfo

## Modules to Import

```TypeScript
import { bundleManager } from 'kits/@kit.AbilityKit';
```

## getAbilityInfo

```TypeScript
function getAbilityInfo(uri: string, abilityFlags: number): Promise<Array<AbilityInfo>>
```

Obtains the ability information based on the given resource identifier and ability flag. This API uses a promise to return the result.

**Since:** 20

**Required permissions:** ohos.permission.GET_ABILITY_INFO

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |
| abilityFlags | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;AbilityInfo & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [17700003](../errorcode-bundle.md#17700003-ability-name-does-not-exist) |
