# clearPreloadedUIExtensionAbility (System API)

## Modules to Import

```TypeScript
import { abilityManager } from '@kit.AbilityKit';
```

## clearPreloadedUIExtensionAbility

```TypeScript
function clearPreloadedUIExtensionAbility(preloadId: number): Promise<void>
```

Clears a [UIExtensionAbility](arkts-ability-app-ability-uiextensionability-uiextensionability-c.md#UIExtensionAbility) instance. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.PRELOAD_UI_EXTENSION_ABILITY

**Model restriction:** This API can be used only in the stage model.

<!--Device-abilityManager-function clearPreloadedUIExtensionAbility(preloadId: int): Promise<void>--><!--Device-abilityManager-function clearPreloadedUIExtensionAbility(preloadId: int): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| preloadId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
| [16000003](../errorcode-ability.md#16000003-id-does-not-exist) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { abilityManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  // ID returned after the preloadUIExtensionAbility API is called to preload a UIExtensionAbility instance.
  let preloadId: number = 1001;
  abilityManager.clearPreloadedUIExtensionAbility(preloadId)
    .then(() => {
      console.info('clearPreloadedUIExtensionAbility success.');
    })
    .catch((err: BusinessError) => {
      console.error(`clearPreloadedUIExtensionAbility fail, err: ${JSON.stringify(err)}`);
    });
} catch (err) {
  let code = (err as BusinessError).code;
  let message = (err as BusinessError).message;
  console.error(`clearPreloadedUIExtensionAbility failed, code is ${code}, message is ${message}`);
}
```
