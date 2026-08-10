# getEnvironmentVar

## Modules to Import

```TypeScript
import { process } from 'kits/@kit.ArkTS';
```

## getEnvironmentVar

```TypeScript
function getEnvironmentVar(name: string): string
```

获取环境变量名对应的值。如果环境变量不存在，返回undefined。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [process.ProcessManager.getEnvironmentVar](arkts-arkts-process-processmanager-c.md#getenvironmentvar)

<!--Device-process-function getEnvironmentVar(name: string): string--><!--Device-process-function getEnvironmentVar(name: string): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | 环境变量名。 |

**Return value:**

| Type | Description |
| --- | --- |
| string | 返回环境变量名对应的值。 |

## Examples

```TypeScript
let pres = process.getEnvironmentVar("PATH");
```

