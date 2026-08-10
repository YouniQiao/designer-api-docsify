# BrightnessInfo

屏幕亮度信息。此类型中的信息均来自底层屏幕信息数据。

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

<!--Device-display-interface BrightnessInfo--><!--Device-display-interface BrightnessInfo-End-->

**System capability:** SystemCapability.Window.SessionManager

## Modules to Import

```TypeScript
import { display } from 'kits/@kit.ArkUI';
```

## currentHeadroom

```TypeScript
readonly currentHeadroom: double
```

当前亮度动态余量，该参数为大于0的浮点数。默认值为1.0。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-BrightnessInfo-readonly currentHeadroom: double--><!--Device-BrightnessInfo-readonly currentHeadroom: double-End-->

**System capability:** SystemCapability.Window.SessionManager

## maxHeadroom

```TypeScript
readonly maxHeadroom: double
```

当前最大亮度余量，该参数为大于0的浮点数。默认值为1.0。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-BrightnessInfo-readonly maxHeadroom: double--><!--Device-BrightnessInfo-readonly maxHeadroom: double-End-->

**System capability:** SystemCapability.Window.SessionManager

## sdrNits

```TypeScript
readonly sdrNits: double
```

屏幕的亮度，该参数为大于0的浮点数。默认值为500.0。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-BrightnessInfo-readonly sdrNits: double--><!--Device-BrightnessInfo-readonly sdrNits: double-End-->

**System capability:** SystemCapability.Window.SessionManager

