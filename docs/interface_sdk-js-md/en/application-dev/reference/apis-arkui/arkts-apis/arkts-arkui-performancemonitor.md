# @ohos.arkui.performanceMonitor

Provides interfaces to monitor a scene for performance measurement.

&lt;p&gt;These interfaces are used to monitor the begin, end, and value changes of finger processes that last for at least 3 ms.

&lt;p&gt;Example:import "@ohos.arkui.performanceMonitor.d.ts"To start scene monitoring that is expected to complete within 5 ms:&lt;pre&gt;{@code performanceMonitor.begin(string, ActionType, string);//scene finished performanceMonitor.end(string);}&lt;/pre&gt;

&lt;p&gt;Each {@code begin} matches one {@code end}, and they must have the same scene id.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare namespace performanceMonitor--><!--Device-unnamed-declare namespace performanceMonitor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { performanceMonitor } from 'kits/@kit.ArkUI';
```

## Summary

<!--Del-->
### Functions（系统接口）

| Name | Description |
| --- | --- |
| [begin](arkts-arkui-performancemonitor-begin-f-sys.md#begin) | Begin monitoring an application scene. |
| [end](arkts-arkui-performancemonitor-end-f-sys.md#end) | End monitoring an application scene. |
| [recordInputEventTime](arkts-arkui-performancemonitor-recordinputeventtime-f-sys.md#recordinputeventtime) | recordInputEventTime monitoring an application scene. |
<!--DelEnd-->

<!--Del-->
### Enums（系统接口）

| Name | Description |
| --- | --- |
| [ActionType](arkts-arkui-performancemonitor-actiontype-e-sys.md) | Enumerates the input event type. |
| [SourceType](arkts-arkui-performancemonitor-sourcetype-e-sys.md) | Enumerates the input source type. |
<!--DelEnd-->

