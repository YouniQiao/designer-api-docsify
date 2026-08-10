# exit

## Modules to Import

```TypeScript
import { process } from 'kits/@kit.ArkTS';
```

## exit

```TypeScript
function exit(code: number): void
```

终止程序。

请谨慎使用此接口。调用此接口后应用将退出。如果输入参数非0，可能会导致数据丢失或出现未定义的运行异常。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [process.ProcessManager.exit](arkts-arkts-process-processmanager-c.md#exit)

<!--Device-process-function exit(code: number): void--><!--Device-process-function exit(code: number): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| code | number | Yes | 进程的退出码。 |

## Examples

```TypeScript
process.exit(0);
```

