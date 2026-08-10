# registerVsyncCallback (System API)

## registerVsyncCallback

```TypeScript
function registerVsyncCallback(callback: (info: string) => void): void
```

为profiler注册vsync回调。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

<!--Device-Profiler-function registerVsyncCallback(callback: (info: string) => void): void--><!--Device-Profiler-function registerVsyncCallback(callback: (info: string) => void): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | (info: string) =&gt; void | Yes | 回调信息为带有ui更新信息的json字符串。 |

