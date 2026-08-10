# unregisterTraceListener

## Modules to Import

```TypeScript
import { hiTraceMeter } from 'kits/@kit.PerformanceAnalysisKit';
```

## unregisterTraceListener

```TypeScript
function unregisterTraceListener(index: int): int
```

注销通过registerTraceListener()注册的trace捕获开关通知回调函数。

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-hiTraceMeter-function unregisterTraceListener(index: int): int--><!--Device-hiTraceMeter-function unregisterTraceListener(index: int): int-End-->

**System capability:** SystemCapability.HiviewDFX.HiTrace

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 已注册回调函数索引，取值范围[0, 9]，即 [registerTraceListener()](arkts-performanceanalysis-hitracemeter-registertracelistener-f.md#registertracelistener)调用成功时的返回值。 |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：int | 回调注销状态。 0：注销成功； -1：目标索引的回调函数未注册； -2：无效索引，参数index值不在[0, 9]范围内。 |

## Examples

```TypeScript
// Deregister the callback used to notify whether the application trace capture is enabled. index is the callback index returned by hiTraceMeter.registerTraceListener.
let ret = hiTraceMeter.unregisterTraceListener(index);
if (ret < 0) {
  // Handle exceptions.
}
```

