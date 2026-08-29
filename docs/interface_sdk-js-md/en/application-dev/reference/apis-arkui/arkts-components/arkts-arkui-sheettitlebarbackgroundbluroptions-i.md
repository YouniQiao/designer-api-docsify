# SheetTitleBarBackgroundBlurOptions

Custom options for title bar background blur. All sub-properties are optional; unset properties use system default values.

**Since:** 26.1.0

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## blurStyle

```TypeScript
blurStyle?: SheetTitleBarBackgroundBlur
```

Blur style. Set to GRADIENT to enable gradient blur effect. Default value: **SheetTitleBarBackgroundBlur.NONE**.

**Type:** [SheetTitleBarBackgroundBlur](arkts-arkui-sheettitlebarbackgroundblur-e.md)

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## effectiveDistance

```TypeScript
effectiveDistance?: LengthMetrics
```

Sliding distance required for the blur effect to transition from fully hidden to fully visible. Value range: greater than or equal to 0; values less than 0 are treated as 0. Default value: **8vp**.

**Type:** LengthMetrics

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## maskColor

```TypeScript
maskColor?: ResourceColor
```

Base color of the gradient mask. This color serves as the maximum color at the top of the mask. The system applies a built-in transparency curve to gradually fade it from top to bottom. When not set: on mid-to-high-performance devices: #CCF1F3F5 is used in light mode, and #66202224 is used in dark mode. On low-performance devices: #F2F1F3F5 is used in light mode, and #E5202224 is used in dark mode.

**Type:** [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md)

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## maskExtraHeight

```TypeScript
maskExtraHeight?: LengthMetrics
```

Extra height of the gradient mask. Additional mask coverage height beyond the title bar height. Default value: **32vp**.

**Type:** LengthMetrics

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

**System capability:** SystemCapability.ArkUI.ArkUI.Full
