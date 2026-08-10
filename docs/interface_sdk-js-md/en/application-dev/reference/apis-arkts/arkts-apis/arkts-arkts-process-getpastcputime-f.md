# getPastCpuTime

## Modules to Import

```TypeScript
import { process } from 'kits/@kit.ArkTS';
```

## getPastCpuTime

```TypeScript
function getPastCpuTime(): number
```

获取进程启动到当前时间的 CPU 时间（以毫秒为单位）。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-process-function getPastCpuTime(): number--><!--Device-process-function getPastCpuTime(): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| number | 返回经过的 CPU 时间。单位：毫秒。 |

## Examples

```TypeScript
let result = process.getPastCpuTime();
```

