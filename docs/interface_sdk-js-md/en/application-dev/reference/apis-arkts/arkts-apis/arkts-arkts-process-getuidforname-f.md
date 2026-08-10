# getUidForName

## Modules to Import

```TypeScript
import { process } from 'kits/@kit.ArkTS';
```

## getUidForName

```TypeScript
function getUidForName(v: string): number
```

根据指定的用户名，从系统的用户数据库中获取该用户的 uid。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [process.ProcessManager.getUidForName](arkts-arkts-process-processmanager-c.md#getuidforname)

<!--Device-process-function getUidForName(v: string): number--><!--Device-process-function getUidForName(v: string): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| v | string | Yes | 用户名。 |

**Return value:**

| Type | Description |
| --- | --- |
| number | 返回用户 uid。 |

## Examples

```TypeScript
let pres = process.getUidForName("tool");
```

