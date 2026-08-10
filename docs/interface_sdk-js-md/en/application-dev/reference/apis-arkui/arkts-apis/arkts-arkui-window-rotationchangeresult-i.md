# RotationChangeResult

应用在窗口旋转变化时返回的信息，系统会根据此信息改变当前窗口矩形区域大小。当返回主窗口旋转变化的信息时，系统不改变主窗口的大小。

应用窗口与系统窗口大小存在限制，具体限制与相关规则可见  
[resize](arkts-arkui-window-window-i.md#resize)。

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

<!--Device-window-interface RotationChangeResult--><!--Device-window-interface RotationChangeResult-End-->

**System capability:** SystemCapability.Window.SessionManager

## Modules to Import

```TypeScript
import { window } from 'kits/@kit.ArkUI';
```

## rectType

```TypeScript
rectType: RectType
```

窗口矩形区域坐标系类型。

**Type:** [RectType](arkts-arkui-window-recttype-e.md)

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-RotationChangeResult-rectType: RectType--><!--Device-RotationChangeResult-rectType: RectType-End-->

**System capability:** SystemCapability.Window.SessionManager

## windowRect

```TypeScript
windowRect: Rect
```

相对于屏幕或父窗坐标系的窗口矩形区域信息。

**Type:** [Rect](../../apis-form-kit/arkts-apis/arkts-form-forminfo-rect-i.md)

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-RotationChangeResult-windowRect: Rect--><!--Device-RotationChangeResult-windowRect: Rect-End-->

**System capability:** SystemCapability.Window.SessionManager

