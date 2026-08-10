# PiPWindowSize

画中画窗口大小。

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 26.0.0.

<!--Device-PiPWindow-interface PiPWindowSize--><!--Device-PiPWindow-interface PiPWindowSize-End-->

**System capability:** SystemCapability.Window.SessionManager

## Modules to Import

```TypeScript
import { PiPWindow } from 'kits/@kit.ArkUI';
```

## height

```TypeScript
height: int
```

窗口高度，单位为px，该参数应为正整数，不大于屏幕高度。

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

窗口缩放比，显示大小相对于width和height的缩放比，该参数为浮点数，取值范围大于0.0，小于等于1.0。等于1表示与width和height一样大。

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

窗口宽度，单位为px，该参数应为正整数，不大于屏幕宽度。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 26.0.0.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-PiPWindowSize-width: int--><!--Device-PiPWindowSize-width: int-End-->

**System capability:** SystemCapability.Window.SessionManager

