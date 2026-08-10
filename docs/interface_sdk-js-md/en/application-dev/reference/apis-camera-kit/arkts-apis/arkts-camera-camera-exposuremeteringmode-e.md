# ExposureMeteringMode

枚举，曝光测光模式。

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-camera-enum ExposureMeteringMode--><!--Device-camera-enum ExposureMeteringMode-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## MATRIX

```TypeScript
MATRIX = 0
```

矩阵测光模式。对画面广泛区域进行测光，适合拍摄自然风光。

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-ExposureMeteringMode-MATRIX = 0--><!--Device-ExposureMeteringMode-MATRIX = 0-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## CENTER

```TypeScript
CENTER = 1
```

中心测光模式。对整个画面进行测光，但最大比重分配给中央区域，适合拍摄人像。

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-ExposureMeteringMode-CENTER = 1--><!--Device-ExposureMeteringMode-CENTER = 1-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## SPOT

```TypeScript
SPOT = 2
```

点测光模式。对画面测光点周围约2.5%进行测光，专注于特定微小区域的光线，如被摄主体的眼睛。

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-ExposureMeteringMode-SPOT = 2--><!--Device-ExposureMeteringMode-SPOT = 2-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## CENTER_HIGHLIGHT_WEIGHTED

```TypeScript
CENTER_HIGHLIGHT_WEIGHTED = 3
```

Center-weighted and highlight metering mode. This mode focuses on the highlight area near the center of the screen.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExposureMeteringMode-CENTER_HIGHLIGHT_WEIGHTED = 3--><!--Device-ExposureMeteringMode-CENTER_HIGHLIGHT_WEIGHTED = 3-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

