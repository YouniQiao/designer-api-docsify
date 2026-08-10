# uptime

## Modules to Import

```TypeScript
import { process } from 'kits/@kit.ArkTS';
```

## uptime

```TypeScript
function uptime(): number
```

获取当前系统已运行的时间（以秒为单位）。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-process-function uptime(): number--><!--Device-process-function uptime(): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| number | 当前系统已运行的时间。单位：秒。 |

## Examples

```TypeScript
let time = process.uptime();
```

