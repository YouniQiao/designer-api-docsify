# queryAtomicServiceStartupRule (System API)

## Modules to Import

```TypeScript
import { abilityManager } from '@kit.AbilityKit';
```

## queryAtomicServiceStartupRule

```TypeScript
function queryAtomicServiceStartupRule(context: Context, appId: string): Promise<AtomicServiceStartupRule>
```

Obtains the rule for launching an [EmbeddableUIAbility](arkts-ability-app-ability-embeddableuiability-embeddableuiability-c.md#EmbeddableUIAbility) in embedded mode. This API uses a promise to return the result. This API can be properly called only on phones and tablets. On other devices, it returns the error code 801.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-abilityManager-function queryAtomicServiceStartupRule(context: Context, appId: string): Promise<AtomicServiceStartupRule>--><!--Device-abilityManager-function queryAtomicServiceStartupRule(context: Context, appId: string): Promise<AtomicServiceStartupRule>-End-->

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
| Promise&lt;[AtomicServiceStartupRule](arkts-ability-abilitymanager-atomicservicestartuprule-i-sys.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [16000050](../errorcode-ability.md#16000050-internal-error) |

## Examples

```TypeScript
import { abilityManager, UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onForeground() {
    let appId: string = '6918661953712445909';
    try {
      abilityManager.queryAtomicServiceStartupRule(this.context, appId).then((data: abilityManager.AtomicServiceStartupRule) => {
        console.info(`queryAtomicServiceStartupRule data: ${JSON.stringify(data)}`);
      }).catch((err: BusinessError) => {
        console.error(`queryAtomicServiceStartupRule failed, code is ${err.code}, message is ${err.message}`);
      });
    } catch (err) {
      // Process input parameter errors.
      console.error(`param is invalid, code is ${err.code}, message is ${err.message}`);
    }
  }
}
```
