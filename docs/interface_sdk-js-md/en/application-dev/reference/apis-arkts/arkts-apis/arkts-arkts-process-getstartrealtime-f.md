# getStartRealtime

## Modules to Import

```TypeScript
import { process } from 'kits/@kit.ArkTS';
```

## getStartRealtime

```TypeScript
function getStartRealtime(): number
```

获取系统启动到进程启动的实时时间（以毫秒为单位，不包含系统休眠时间）。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-process-function getStartRealtime(): number--><!--Device-process-function getStartRealtime(): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| number | 返回经过的实时时间。单位：毫秒。 |

## Examples

```TypeScript
let realtime = process.getStartRealtime();
```

