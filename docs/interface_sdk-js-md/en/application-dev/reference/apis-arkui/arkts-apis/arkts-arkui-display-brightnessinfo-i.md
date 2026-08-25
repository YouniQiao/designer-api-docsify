# BrightnessInfo

Describes the screen brightness information. The information comes from the underlying screen data.

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Window.SessionManager

## Modules to Import

```TypeScript
import { display } from '@kit.ArkUI';
```

## brightnessPosition

```TypeScript
readonly brightnessPosition?: double
```

Position of the brightness bar corresponding to the current screen brightness. The value is a floating-point number ranging from 0.0 to 1.0. The default value is 0.0. The value 0.0 indicates the lowest screen brightness, and 1.0 indicates the highest screen brightness. The returned brightness bar position may have an error of 0.01 compared with the actual brightness bar position. Value range: [0.0,1.0]. Default value: 0.0.@readonly

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**System capability:** SystemCapability.Window.SessionManager

## currentHeadroom

```TypeScript
readonly currentHeadroom: double
```

Dynamic brightness headroom. The value is a floating-point number greater than 0. The default value is **1.0**.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Window.SessionManager

## maxHeadroom

```TypeScript
readonly maxHeadroom: double
```

Maximum brightness headroom. The value is a floating-point number greater than 0. The default value is **1.0**.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Window.SessionManager

## sdrNits

```TypeScript
readonly sdrNits: double
```

Screen brightness, in nit. The value is a floating-point number greater than 0. The default value is **500.0**.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Window.SessionManager
