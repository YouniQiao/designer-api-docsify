# ChildProcess

ChildProcess is the base class for you to customize child processes. When starting a child process through [childProcessManager]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_, you must inherit this class and override the entrypoint method.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-unnamed-declare class ChildProcess--><!--Device-unnamed-declare class ChildProcess-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## onStart

```TypeScript
onStart(args?: ChildProcessArgs): void
```

Entrypoint method of the child process. This callback is triggered when the child process is started through [childProcessManager]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ChildProcess-onStart(args?: ChildProcessArgs): void--><!--Device-ChildProcess-onStart(args?: ChildProcessArgs): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| args | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Parameters transferred to the child process. |

**Example**

```TypeScript
import { ChildProcess, ChildProcessArgs } from '@kit.AbilityKit';

export default class DemoProcess extends ChildProcess {

  onStart(args?: ChildProcessArgs) {
    let entryParams = args?.entryParams;
    let fd = args?.fds?.key1;
    // ..
  }
}
```

