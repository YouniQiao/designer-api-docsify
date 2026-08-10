# runCmd (System API)

## Modules to Import

```TypeScript
import { process } from 'kits/@kit.ArkTS';
```

## runCmd

```TypeScript
function runCmd(
    command: string,
    options?: ConditionType
  ): ChildProcess
```

返回一个子进程对象，并 spawn 一个新的 ChildProcess 来运行命令。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

<!--Device-process-function runCmd(    command: string,    options?: ConditionType  ): ChildProcess--><!--Device-process-function runCmd(    command: string,    options?: ConditionType  ): ChildProcess-End-->

**System capability:** SystemCapability.Utils.Lang

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| command | string | Yes | 子进程执行的 shell 命令字符串。 |
| options | [ConditionType](arkts-arkts-process-conditiontype-i-sys.md) | No | 是一个对象，包含三个参数。timeout 是子进程的运行时间，killSignal 是子进程达到 timeout 时发送的信号，maxBuffer 是标准输入和输出的最大缓冲区大小。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ChildProcess](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-childprocess-childprocess-c.md) | 返回一个子进程对象。 |

