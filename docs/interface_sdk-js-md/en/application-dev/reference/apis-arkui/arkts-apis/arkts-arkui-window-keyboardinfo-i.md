# KeyboardInfo

软键盘窗口信息。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-window-interface KeyboardInfo--><!--Device-window-interface KeyboardInfo-End-->

**System capability:** SystemCapability.Window.SessionManager

## Modules to Import

```TypeScript
import { window } from 'kits/@kit.ArkUI';
```

## animated

```TypeScript
animated?: boolean
```

当前是否有显示/隐藏动画，true表示有动画，false表示没有。

**Type:** boolean

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-KeyboardInfo-animated?: boolean--><!--Device-KeyboardInfo-animated?: boolean-End-->

**System capability:** SystemCapability.Window.SessionManager

## beginRect

```TypeScript
beginRect: Rect
```

动画开始前软键盘的位置和大小。

**Type:** [Rect](../../apis-form-kit/arkts-apis/arkts-form-forminfo-rect-i.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-KeyboardInfo-beginRect: Rect--><!--Device-KeyboardInfo-beginRect: Rect-End-->

**System capability:** SystemCapability.Window.SessionManager

## config

```TypeScript
config?: WindowAnimationConfig
```

动画配置信息。

**Type:** [WindowAnimationConfig](arkts-arkui-window-windowanimationconfig-i.md)

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-KeyboardInfo-config?: WindowAnimationConfig--><!--Device-KeyboardInfo-config?: WindowAnimationConfig-End-->

**System capability:** SystemCapability.Window.SessionManager

## endRect

```TypeScript
endRect: Rect
```

动画结束后软键盘的位置和大小。

**Type:** [Rect](../../apis-form-kit/arkts-apis/arkts-form-forminfo-rect-i.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-KeyboardInfo-endRect: Rect--><!--Device-KeyboardInfo-endRect: Rect-End-->

**System capability:** SystemCapability.Window.SessionManager

