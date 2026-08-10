# ChildProcess

开发者自定义子进程的基类。通过[childProcessManager](arkts-app-ability-childprocessmanager.md)启动子进程时，需要继承此类并重写入口方法。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-unnamed-declare class ChildProcess--><!--Device-unnamed-declare class ChildProcess-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## Modules to Import

```TypeScript
import { ChildProcess } from 'kits/@kit.AbilityKit';
```

## onStart

```TypeScript
onStart(args?: ChildProcessArgs): void
```

子进程的入口方法，通过[childProcessManager](arkts-app-ability-childprocessmanager.md)启动子进程后调用。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ChildProcess-onStart(args?: ChildProcessArgs): void--><!--Device-ChildProcess-onStart(args?: ChildProcessArgs): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| args | [ChildProcessArgs](arkts-ability-app-ability-childprocessargs-childprocessargs-i.md) | No | 传递到子进程的参数。 |

## Examples

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

