# PiPWindowSize

Describes the size of a PiP window.

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 26.0.0.

<!--Device-PiPWindow-interface PiPWindowSize--><!--Device-PiPWindow-interface PiPWindowSize-End-->

**System capability:** SystemCapability.Window.SessionManager

## Modules to Import

```TypeScript
import { PiPWindow } from '@kit.ArkUI';
```

## height

```TypeScript
height: int
```

Window height, in px. The value must be a positive integer and cannot be greater than the screen height.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 26.0.0.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-PiPWindowSize-height: int--><!--Device-PiPWindowSize-height: int-End-->

**System capability:** SystemCapability.Window.SessionManager

## scale

```TypeScript
scale: double
```

Scale factor of the window, representing the display size relative to the width and height. The value is a floating-point number in the range (0.0, 1.0]. The value **1** means that the window matches the specified width and height.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 26.0.0.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-PiPWindowSize-scale: double--><!--Device-PiPWindowSize-scale: double-End-->

**System capability:** SystemCapability.Window.SessionManager

## width

```TypeScript
width: int
```

Window width, in px. The value must be a positive integer and cannot be greater than the screen width.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 26.0.0.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-PiPWindowSize-width: int--><!--Device-PiPWindowSize-width: int-End-->

**System capability:** SystemCapability.Window.SessionManager

