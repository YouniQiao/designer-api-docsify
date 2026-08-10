# demoteCurrentFromCandidateMasterProcess

## Modules to Import

```TypeScript
import { application } from 'kits/@kit.AbilityKit';
```

## demoteCurrentFromCandidateMasterProcess

```TypeScript
export function demoteCurrentFromCandidateMasterProcess(): Promise<void>
```

撤销当前进程的备选主控进程资格。使用Promise异步回调。该接口在PC/2in1、Tablet中可正常调用，在其他设备类型中返回801错误码。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-application-export function demoteCurrentFromCandidateMasterProcess(): Promise<void>--><!--Device-application-export function demoteCurrentFromCandidateMasterProcess(): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 16000116 | The current process is already a master process and does not support cancellation. |
| 801 | Capability not supported. |
| 16000117 | The current process is not a candidate master process and does not support cancellation. |

## Examples

```TypeScript
import { AbilityConstant, UIAbility, application, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    try {
      application.demoteCurrentFromCandidateMasterProcess()
        .then(() => {
          console.info('demote succeed');
        })
        .catch((err: BusinessError) => {
          console.error(`demote failed, code is ${err.code}, message is ${err.message}`);
        });
    } catch (error) {
      let code: number = (error as BusinessError).code;
      let message: string = (error as BusinessError).message;
      console.error(`demoteCurrentFromCandidateMasterProcess failed, error.code: ${code}, error.message: ${message}`);
    }
  }
}
```

