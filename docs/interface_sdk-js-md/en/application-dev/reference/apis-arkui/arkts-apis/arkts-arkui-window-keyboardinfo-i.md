# KeyboardInfo

Describes the information about the soft keyboard window.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-window-interface KeyboardInfo--><!--Device-window-interface KeyboardInfo-End-->

**System capability:** SystemCapability.Window.SessionManager

## Modules to Import

```TypeScript
import { window } from 'window';
```

## animated

```TypeScript
animated?: boolean
```

Whether there is a show/hide animation. **true** if there is a show/hide animation, **false** otherwise.

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-KeyboardInfo-animated?: boolean--><!--Device-KeyboardInfo-animated?: boolean-End-->

**System capability:** SystemCapability.Window.SessionManager

## beginRect

```TypeScript
beginRect: Rect
```

Position and size of the soft keyboard before the animation starts.

**Type:** Rect

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-KeyboardInfo-beginRect: Rect--><!--Device-KeyboardInfo-beginRect: Rect-End-->

**System capability:** SystemCapability.Window.SessionManager

## config

```TypeScript
config?: WindowAnimationConfig
```

Animation configuration.

**Type:** [WindowAnimationConfig](arkts-arkui-window-windowanimationconfig-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-KeyboardInfo-config?: WindowAnimationConfig--><!--Device-KeyboardInfo-config?: WindowAnimationConfig-End-->

**System capability:** SystemCapability.Window.SessionManager

## endRect

```TypeScript
endRect: Rect
```

Position and size of the soft keyboard after the animation ends.

**Type:** Rect

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-KeyboardInfo-endRect: Rect--><!--Device-KeyboardInfo-endRect: Rect-End-->

**System capability:** SystemCapability.Window.SessionManager

