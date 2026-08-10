# isIsolatedProcess

## Modules to Import

```TypeScript
import { process } from 'kits/@kit.ArkTS';
```

## isIsolatedProcess

```TypeScript
function isIsolatedProcess(): boolean
```

检查进程是否已被隔离。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-process-function isIsolatedProcess(): boolean--><!--Device-process-function isIsolatedProcess(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 返回判断结果。如果进程被隔离则返回 true；否则， 返回 false。 |

## Examples

```TypeScript
let result = process.isIsolatedProcess();
```

