# exitMasterProcessRole

## Modules to Import

```TypeScript
import { application } from 'kits/@kit.AbilityKit';
```

## exitMasterProcessRole

```TypeScript
export function exitMasterProcessRole(): Promise<void>
```

放弃当前进程的[主控进程](../../../application-models/ability-terminology.md#masterprocess主控进程)身份。使用Promise异步回调。该接口仅在2in1、Tablet设备中可正常调用，在其他设备中返回801错误码。

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-application-export function exitMasterProcessRole(): Promise<void>--><!--Device-application-export function exitMasterProcessRole(): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported. |
| 16000118 | Not a master process. |
| 16000119 | Cannot exit because there is an unfinished request. |

## Examples

```TypeScript
import { AbilityConstant, UIAbility, application, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    try {
      application.exitMasterProcessRole()
        .then(() => {
          console.info('exitMasterProcessRole succeed');
        })
        .catch((err: BusinessError) => {
          console.error(`exitMasterProcessRole failed, code is ${err.code}, message is ${err.message}`);
        });
    } catch (error) {
      let code: number = (error as BusinessError).code;
      let message: string = (error as BusinessError).message;
      console.error(`exitMasterProcessRole failed, error.code: ${code}, error.message: ${message}`);
    }
  }
}
```

