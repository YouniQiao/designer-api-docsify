# registerVsyncCallback (System API)

## registerVsyncCallback

```TypeScript
function registerVsyncCallback(callback: Callback<string>): void
```

Registers vsync callback for profiler. AnonyMous Object Rectification.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Profiler-function registerVsyncCallback(callback: Callback<string>): void--><!--Device-Profiler-function registerVsyncCallback(callback: Callback<string>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;string&gt; | Yes | the callback info is json string with ui update info. |

