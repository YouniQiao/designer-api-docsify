# clearPreloadedUIExtensionAbilities (System API)

## Modules to Import

```TypeScript
import { abilityManager } from '@kit.AbilityKit';
```

## clearPreloadedUIExtensionAbilities

```TypeScript
function clearPreloadedUIExtensionAbilities(): Promise<void>
```

Clears all preloaded [UIExtensionAbility](arkts-ability-app-ability-uiextensionability-uiextensionability-c.md#UIExtensionAbility) instances in the current process. This API uses a promise to return the result.

**Since:** 23

**Required permissions:** ohos.permission.PRELOAD_UI_EXTENSION_ABILITY

**Model restriction:** This API can be used only in the stage model.

<!--Device-abilityManager-function clearPreloadedUIExtensionAbilities(): Promise<void>--><!--Device-abilityManager-function clearPreloadedUIExtensionAbilities(): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [16000050](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000050-internal-error) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { abilityManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  abilityManager.clearPreloadedUIExtensionAbilities()
    .then(() => {
      console.info('clearPreloadedUIExtensionAbilities success.');
    })
    .catch((err: BusinessError) => {
      console.error(`clearPreloadedUIExtensionAbilities fail, err: ${JSON.stringify(err)}`);
    });
} catch (err) {
  let code = (err as BusinessError).code;
  let message = (err as BusinessError).message;
  console.error(`clearPreloadedUIExtensionAbilities failed, code is ${code}, message is ${message}`);
}
```
