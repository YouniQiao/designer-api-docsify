# getSystemConfig

## Modules to Import

```TypeScript
import { process } from 'kits/@kit.ArkTS';
```

## getSystemConfig

```TypeScript
function getSystemConfig(name: number): number
```

获取系统配置信息。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [process.ProcessManager.getSystemConfig](arkts-arkts-process-processmanager-c.md#getsystemconfig)

<!--Device-process-function getSystemConfig(name: number): number--><!--Device-process-function getSystemConfig(name: number): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | number | Yes | 指定系统配置参数名。 |

**Return value:**

| Type | Description |
| --- | --- |
| number | 返回系统配置信息。 |

## Examples

```TypeScript
let _SC_ARG_MAX = 0;
let pres = process.getSystemConfig(_SC_ARG_MAX);
```

