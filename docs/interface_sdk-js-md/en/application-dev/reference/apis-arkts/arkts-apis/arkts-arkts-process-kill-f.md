# kill

## Modules to Import

```TypeScript
import { process } from 'kits/@kit.ArkTS';
```

## kill

```TypeScript
function kill(signal: number, pid: number): boolean
```

发送信号到指定进程，结束该进程。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [process.ProcessManager.kill](arkts-arkts-process-processmanager-c.md#kill)

<!--Device-process-function kill(signal: number, pid: number): boolean--><!--Device-process-function kill(signal: number, pid: number): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| signal | number | Yes | 发送的信号。 |
| pid | number | Yes | 进程的 id。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 信号发送成功返回 true，失败返回 false。 |

## Examples

```TypeScript
let pres = process.pid;
let result = process.kill(28, pres);
```

