# isAppUid

## Modules to Import

```TypeScript
import { process } from 'kits/@kit.ArkTS';
```

## isAppUid

```TypeScript
function isAppUid(v: number): boolean
```

判断 uid 是否属于应用程序。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [process.ProcessManager.isAppUid](arkts-arkts-process-processmanager-c.md#isappuid)

<!--Device-process-function isAppUid(v: number): boolean--><!--Device-process-function isAppUid(v: number): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| v | number | Yes | 应用程序的 uid。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 返回判断结果。如果是应用程序的 uid 则返回 true； 否则返回 false。 |

## Examples

```TypeScript
let result = process.isAppUid(688);
```

