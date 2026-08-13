# preloadUIExtensionAbility (System API)

## Modules to Import

```TypeScript
import { abilityManager } from '@kit.AbilityKit';
```

## preloadUIExtensionAbility

```TypeScript
function preloadUIExtensionAbility(want: Want): Promise<number>
```

Preloads a [UIExtensionAbility](arkts-ability-app-ability-uiextensionability-uiextensionability-c.md#UIExtensionAbility) instance and returns the instance ID. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.PRELOAD_UI_EXTENSION_ABILITY

**Model restriction:** This API can be used only in the stage model.

<!--Device-abilityManager-function preloadUIExtensionAbility(want: Want): Promise<int>--><!--Device-abilityManager-function preloadUIExtensionAbility(want: Want): Promise<int>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [16000004](../errorcode-ability.md#16000004-visibility-verification-failure) |
| [16000001](../errorcode-ability.md#16000001-ability-name-does-not-exist) |
| [16000002](../errorcode-ability.md#16000002-incorrect-ability-type) |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { abilityManager, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  const preloadWant: Want = {
    bundleName: 'com.example.application',
    abilityName: 'EntryBackupAbility',
    moduleName: 'entry',
    parameters: {
      'ability.want.params.uiExtensionType': 'sys/commonUI'
    }
  };

  abilityManager.preloadUIExtensionAbility(preloadWant)
    .then((preloadId: number) => {
      console.info(`preloadUIExtensionAbility success, preloadId: ${preloadId}`);
    })
    .catch((err: BusinessError) => {
      console.error(`preloadUIExtensionAbility fail, err: ${JSON.stringify(err)}`);
    });
} catch (err) {
  let code = (err as BusinessError).code;
  let message = (err as BusinessError).message;
  console.error(`preloadUIExtensionAbility failed, code is ${code}, message is ${message}`);
}
```
