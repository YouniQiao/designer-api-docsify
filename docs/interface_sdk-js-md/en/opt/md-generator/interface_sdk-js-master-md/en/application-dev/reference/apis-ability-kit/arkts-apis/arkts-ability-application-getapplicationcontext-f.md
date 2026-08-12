# getApplicationContext

## Modules to Import

```TypeScript
import { application } from '@kit.AbilityKit';
```

## getApplicationContext

```TypeScript
export function getApplicationContext(): ApplicationContext
```

Obtains the application context. This API provides context access independent of the base class **Context**.Repeated calls to this API generate a new ApplicationContext object.

**Since:** 14

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-application-export function getApplicationContext(): ApplicationContext--><!--Device-application-export function getApplicationContext(): ApplicationContext-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ApplicationContext](arkts-ability-applicationcontext-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [16000050](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000050-internal-error) |

## Examples

```TypeScript
import { AbilityConstant, UIAbility, application, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    try {
      let applicationContext = application.getApplicationContext();
    } catch (error) {
      let code: number = (error as BusinessError).code;
      let message: string = (error as BusinessError).message;
      console.error(`getApplicationContext failed, error.code: ${code}, error.message: ${message}`);
    }
  }
}
```
