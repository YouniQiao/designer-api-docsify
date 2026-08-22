# @ohos.arkui.performanceMonitor

Provides interfaces to monitor a scene for performance measurement.

<p>These interfaces are used to monitor the begin, end, and value changes of finger processes that last for at least 3 ms.

<p>Example: import "@ohos.arkui.performanceMonitor.d.ts" To start scene monitoring that is expected to complete within 5 ms: &lt;pre&gt;{@code performanceMonitor.begin(string, ActionType, string); //scene finished performanceMonitor.end(string); }&lt;/pre&gt;

<p>Each {@code begin} matches one {@code end}, and they must have the same scene id.

@namespace performanceMonitor

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare namespace performanceMonitor--><!--Device-unnamed-declare namespace performanceMonitor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { performanceMonitor } from '@kit.ArkUI';
```

## Summary

<!--Del-->
### Functions(System API)

| Name | Description |
| --- | --- |
| [begin](arkts-arkui-performancemonitor-begin-f-sys.md) | Begin monitoring an application scene. |
| [end](arkts-arkui-performancemonitor-end-f-sys.md) | End monitoring an application scene. |
| [recordInputEventTime](arkts-arkui-performancemonitor-recordinputeventtime-f-sys.md) | recordInputEventTime monitoring an application scene. |
<!--DelEnd-->

<!--Del-->
### Enums(System API)

| Name | Description |
| --- | --- |
| [ActionType](arkts-arkui-performancemonitor-actiontype-e-sys.md) | Enumerates the input event type. |
| [SourceType](arkts-arkui-performancemonitor-sourcetype-e-sys.md) | Enumerates the input source type. |
<!--DelEnd-->

