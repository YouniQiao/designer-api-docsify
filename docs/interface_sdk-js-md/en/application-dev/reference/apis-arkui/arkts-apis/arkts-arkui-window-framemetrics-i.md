# FrameMetrics

Enumerates the metrics for frame performance.

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Window.SessionManager

## Modules to Import

```TypeScript
import { window } from '@kit.ArkUI';
```

## firstDrawFrame

```TypeScript
firstDrawFrame: boolean
```

Whether the frame is the first frame. **true** for first frame, **false** otherwise.

**Type:** boolean

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Window.SessionManager

## inputHandlingDuration

```TypeScript
inputHandlingDuration: long
```

Duration of gesture handling in a frame, in nanoseconds.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Window.SessionManager

## layoutMeasureDuration

```TypeScript
layoutMeasureDuration: long
```

Duration of layout measurement in a frame, in nanoseconds.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Window.SessionManager

## vsyncTimestamp

```TypeScript
vsyncTimestamp: long
```

Timestamp marking the start of the current frame, in nanoseconds.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Window.SessionManager
