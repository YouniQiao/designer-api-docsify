# FrameMetrics

帧率指标。

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

<!--Device-window-interface FrameMetrics--><!--Device-window-interface FrameMetrics-End-->

**System capability:** SystemCapability.Window.SessionManager

## Modules to Import

```TypeScript
import { window } from 'kits/@kit.ArkUI';
```

## firstDrawFrame

```TypeScript
firstDrawFrame: boolean
```

是否是首帧。true表示首帧，false表示非首帧。

**Type:** boolean

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

<!--Device-FrameMetrics-firstDrawFrame: boolean--><!--Device-FrameMetrics-firstDrawFrame: boolean-End-->

**System capability:** SystemCapability.Window.SessionManager

## inputHandlingDuration

```TypeScript
inputHandlingDuration: long
```

一帧中的手势处理耗时（单位：纳秒）。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

<!--Device-FrameMetrics-inputHandlingDuration: long--><!--Device-FrameMetrics-inputHandlingDuration: long-End-->

**System capability:** SystemCapability.Window.SessionManager

## layoutMeasureDuration

```TypeScript
layoutMeasureDuration: long
```

一帧中的布局测量耗时（单位：纳秒）。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

<!--Device-FrameMetrics-layoutMeasureDuration: long--><!--Device-FrameMetrics-layoutMeasureDuration: long-End-->

**System capability:** SystemCapability.Window.SessionManager

## vsyncTimestamp

```TypeScript
vsyncTimestamp: long
```

当前帧的开始时间戳（单位：纳秒）。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

<!--Device-FrameMetrics-vsyncTimestamp: long--><!--Device-FrameMetrics-vsyncTimestamp: long-End-->

**System capability:** SystemCapability.Window.SessionManager

