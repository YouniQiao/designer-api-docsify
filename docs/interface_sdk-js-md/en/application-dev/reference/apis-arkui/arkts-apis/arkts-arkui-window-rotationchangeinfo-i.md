# RotationChangeInfo

窗口旋转变化时的窗口信息。

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

<!--Device-window-interface RotationChangeInfo--><!--Device-window-interface RotationChangeInfo-End-->

**System capability:** SystemCapability.Window.SessionManager

## Modules to Import

```TypeScript
import { window } from 'kits/@kit.ArkUI';
```

## displayId

```TypeScript
displayId: long
```

窗口所在屏幕Id。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-RotationChangeInfo-displayId: long--><!--Device-RotationChangeInfo-displayId: long-End-->

**System capability:** SystemCapability.Window.SessionManager

## displayRect

```TypeScript
displayRect: Rect
```

窗口所在屏幕旋转后的矩形区域大小。

**Type:** [Rect](../../apis-form-kit/arkts-apis/arkts-form-forminfo-rect-i.md)

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-RotationChangeInfo-displayRect: Rect--><!--Device-RotationChangeInfo-displayRect: Rect-End-->

**System capability:** SystemCapability.Window.SessionManager

## orientation

```TypeScript
orientation: int
```

窗口显示方向。

- 0表示竖屏。  
- 1表示反向横屏。  
- 2表示反向竖屏。  
- 3表示横屏。

开发者在使用时，需要注意该方向与display对象的属性orientation含义不一致。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-RotationChangeInfo-orientation: int--><!--Device-RotationChangeInfo-orientation: int-End-->

**System capability:** SystemCapability.Window.SessionManager

## type

```TypeScript
type: RotationChangeType
```

窗口旋转事件类型。

**Type:** [RotationChangeType](arkts-arkui-window-rotationchangetype-e.md)

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-RotationChangeInfo-type: RotationChangeType--><!--Device-RotationChangeInfo-type: RotationChangeType-End-->

**System capability:** SystemCapability.Window.SessionManager

