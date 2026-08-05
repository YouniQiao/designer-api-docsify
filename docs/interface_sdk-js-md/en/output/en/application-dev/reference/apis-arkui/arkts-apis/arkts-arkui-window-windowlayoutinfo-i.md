# WindowLayoutInfo

Describes the information about the window layout.

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

<!--Device-window-interface WindowLayoutInfo--><!--Device-window-interface WindowLayoutInfo-End-->

**System capability:** SystemCapability.Window.SessionManager

## windowAlpha

```TypeScript
windowAlpha?: double
```

The window's alpha fade level. This number is in the range 0.0 to 1.0, where 0.0 is fully transparent and 1.0 is fully opaque.

**Type:** double

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-WindowLayoutInfo-windowAlpha?: double--><!--Device-WindowLayoutInfo-windowAlpha?: double-End-->

**System capability:** SystemCapability.Window.SessionManager

## windowRect

```TypeScript
windowRect: Rect
```

Window rectangle, that is, the position and size of the window on the display.

**Type:** Rect

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-WindowLayoutInfo-windowRect: Rect--><!--Device-WindowLayoutInfo-windowRect: Rect-End-->

**System capability:** SystemCapability.Window.SessionManager

