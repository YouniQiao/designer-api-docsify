# KeyboardInfo

Describes the information about the soft keyboard window.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-window-interface KeyboardInfo--><!--Device-window-interface KeyboardInfo-End-->

**System capability:** SystemCapability.Window.SessionManager

## animated

```TypeScript
animated?: boolean
```

Whether there is a show/hide animation. **true** if there is a show/hide animation, **false** otherwise.

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

Position and size of the soft keyboard before the animation starts.

**Type:** Rect

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-KeyboardInfo-beginRect: Rect--><!--Device-KeyboardInfo-beginRect: Rect-End-->

**System capability:** SystemCapability.Window.SessionManager

## config

```TypeScript
config?: WindowAnimationConfig
```

Animation configuration.

**Type:** WindowAnimationConfig

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-KeyboardInfo-config?: WindowAnimationConfig--><!--Device-KeyboardInfo-config?: WindowAnimationConfig-End-->

**System capability:** SystemCapability.Window.SessionManager

## endRect

```TypeScript
endRect: Rect
```

Position and size of the soft keyboard after the animation ends.

**Type:** Rect

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-KeyboardInfo-endRect: Rect--><!--Device-KeyboardInfo-endRect: Rect-End-->

**System capability:** SystemCapability.Window.SessionManager

