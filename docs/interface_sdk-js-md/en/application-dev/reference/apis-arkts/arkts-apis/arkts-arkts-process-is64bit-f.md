# is64Bit

## Modules to Import

```TypeScript
import { process } from 'kits/@kit.ArkTS';
```

## is64Bit

```TypeScript
function is64Bit(): boolean
```

检查运行环境是否为 64 位。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-process-function is64Bit(): boolean--><!--Device-process-function is64Bit(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 返回判断结果。如果运行环境是 64 位则返回 true； 否则返回 false。 |

## Examples

```TypeScript
let result = process.is64Bit();
```

