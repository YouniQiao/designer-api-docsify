# PickerBackgroundStyle

Defines the background style configuration for selected picker items.

**Since:** 20

**ArkTS mode:** Supports only ArkTS-Dyn, since version 20.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## borderRadius

```TypeScript
borderRadius?: LengthMetrics | BorderRadiuses | LocalizedBorderRadiuses
```

Border radius of the selected item.Default value: **{ value:24, unit:LengthUnit.VP }**, meaning 24 vp for all corners.  
**NOTE：**
1. [LengthMetrics](../arkts-apis/arkts-arkui-graphics-lengthmetrics-c.md): uniform radius with a customizable unit
2. BorderRadiuses: per-corner radius values (vp units only)
3. LocalizedBorderRadiuses: per-corner radius values with individual units

**Type:** LengthMetrics \| BorderRadiuses \| LocalizedBorderRadiuses

**Default:** { value:24, unit:LengthUnit.VP }

**Since:** 20

**ArkTS mode:** Supports only ArkTS-Dyn, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## color

```TypeScript
color?: ResourceColor
```

Background color of the selected item.Default value: 'sys.color.comp_background_tertiary'

**Type:** ResourceColor

**Default:** 'sys.color.comp_background_tertiary'

**Since:** 20

**ArkTS mode:** Supports only ArkTS-Dyn, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.ArkUI.ArkUI.Full
