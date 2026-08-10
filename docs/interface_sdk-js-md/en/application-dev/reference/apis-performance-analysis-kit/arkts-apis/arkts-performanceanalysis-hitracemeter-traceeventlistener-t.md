# TraceEventListener

```TypeScript
type TraceEventListener = (traceStatus: boolean) => void
```

定义应用trace捕获开关状态切换时的回调函数类型。

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-hiTraceMeter-type TraceEventListener = (traceStatus: boolean) => void--><!--Device-hiTraceMeter-type TraceEventListener = (traceStatus: boolean) => void-End-->

**System capability:** SystemCapability.HiviewDFX.HiTrace

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| traceStatus | boolean | Yes | 当前应用trace捕获开关状态。 true：开启；false：关闭。 |

