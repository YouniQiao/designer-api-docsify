# isEmbeddedOpenAllowed (System API)

## Modules to Import

```TypeScript
import { abilityManager } from '@kit.AbilityKit';
```

## isEmbeddedOpenAllowed

```TypeScript
function isEmbeddedOpenAllowed(context: Context, appId: string): Promise<boolean>
```

Checks whether the [EmbeddableUIAbility](arkts-ability-app-ability-embeddableuiability-embeddableuiability-c.md#EmbeddableUIAbility) can be started in embedded mode. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-abilityManager-function isEmbeddedOpenAllowed(context: Context, appId: string): Promise<boolean>--><!--Device-abilityManager-function isEmbeddedOpenAllowed(context: Context, appId: string): Promise<boolean>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](arkts-ability-context-c.md) | Yes |
| appId | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [16000050](../errorcode-ability.md#16000050-internal-error) |

## Examples

```TypeScript
import { abilityManager, UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onForeground() {
    let appId: string = '6918661953712445909';
    try {
      abilityManager.isEmbeddedOpenAllowed(this.context, appId).then((data) => {
        console.info(`isEmbeddedOpenAllowed data: ${JSON.stringify(data)}`);
      }).catch((err: BusinessError) => {
        console.error(`isEmbeddedOpenAllowed failed, code is ${err.code}, message is ${err.message}`);
      });
    } catch (err) {
      // Process input parameter errors.
      console.error(`param is invalid, code is ${err.code}, message is ${err.message}`);
    }
  }
}
```
