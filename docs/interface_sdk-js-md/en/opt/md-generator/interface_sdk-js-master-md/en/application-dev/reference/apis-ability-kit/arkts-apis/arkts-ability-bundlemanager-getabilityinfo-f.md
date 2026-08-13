# getAbilityInfo

## Modules to Import

```TypeScript
import { bundleManager } from '@kit.AbilityKit';
```

## getAbilityInfo

```TypeScript
function getAbilityInfo(uri: string, abilityFlags: number): Promise<Array<AbilityInfo>>
```

Obtains the ability information based on the given resource identifier and ability flag. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.GET_ABILITY_INFO

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-bundleManager-function getAbilityInfo(uri: string, abilityFlags: int): Promise<Array<AbilityInfo>>--><!--Device-bundleManager-function getAbilityInfo(uri: string, abilityFlags: int): Promise<Array<AbilityInfo>>-End-->

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

## Examples

```TypeScript
import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let abilityFlags = bundleManager.AbilityFlag.GET_ABILITY_INFO_WITH_APPLICATION;
let uri = "https://www.example.com";

try {
  bundleManager.getAbilityInfo(uri, abilityFlags).then((data) => {
    hilog.info(0x0000, 'testTag', 'getAbilityInfo successfully. Data: %{public}s', JSON.stringify(data));
  }).catch((err: BusinessError) => {
    let message = (err as BusinessError).message;
    hilog.error(0x0000, 'testTag', 'getAbilityInfo failed. Cause: %{public}s', message);
  });
} catch (err) {
  let message = (err as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'getAbilityInfo failed. Cause: %{public}s', message);
}
```
