# getAutoStartupStatusForSelf

## Modules to Import

```TypeScript
import { autoStartupManager } from '@kit.AbilityKit';
```

## getAutoStartupStatusForSelf

```TypeScript
function getAutoStartupStatusForSelf(): Promise<boolean>
```

Checks whether the current application is enabled for automatic startup at boot time. This API uses a promise to return the result. This API can be properly called only on phones, PC/2-in-1 devices, tablets, and wearables. On other devices, it returns the error code 801.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-autoStartupManager-function getAutoStartupStatusForSelf(): Promise<boolean>--><!--Device-autoStartupManager-function getAutoStartupStatusForSelf(): Promise<boolean>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [16000050](../errorcode-ability.md#16000050-internal-error) |

## Examples

```TypeScript
import { autoStartupManager, UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onForeground() {
    try {
      autoStartupManager.getAutoStartupStatusForSelf().then((isAutoStartup: boolean) => {
        console.info(`getAutoStartupStatusForSelf success, isAutoStartup: ${JSON.stringify(isAutoStartup)}.`);
      }).catch((err: BusinessError) => {
        console.error(`getAutoStartupStatusForSelf failed, err code: ${err.code}, err msg: ${err.message}.`);
      });
    } catch (err) {
      let code = (err as BusinessError).code;
      let msg = (err as BusinessError).message;
      console.error(`getAutoStartupStatusForSelf failed, err code: ${code}, err msg: ${msg}.`);
    }
  }
}
```
