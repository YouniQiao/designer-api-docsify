# PickerBackgroundStyle

Defines the background style configuration for selected picker items.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-unnamed-declare interface PickerBackgroundStyle--><!--Device-unnamed-declare interface PickerBackgroundStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## borderRadius

```TypeScript
borderRadius?: LengthMetrics | BorderRadiuses | LocalizedBorderRadiuses
```

Border radius of the selected item. Default value: **{ value:24, unit:LengthUnit.VP }**, meaning 24 vp for all corners. **NOTE** 1. [LengthMetrics]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_: uniform radius with a customizable unit 2. [BorderRadiuses]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_: per-corner radius values (vp units only) 3. [LocalizedBorderRadiuses]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_: per-corner radius values with individual units

**Type:** LengthMetrics \| BorderRadiuses \| LocalizedBorderRadiuses

**Default:** { value:24, unit:LengthUnit.VP }

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-PickerBackgroundStyle-borderRadius?: LengthMetrics | BorderRadiuses | LocalizedBorderRadiuses--><!--Device-PickerBackgroundStyle-borderRadius?: LengthMetrics | BorderRadiuses | LocalizedBorderRadiuses-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## color

```TypeScript
color?: ResourceColor
```

Background color of the selected item. Default value: 'sys.color.comp\_background\_tertiary'

**Type:** ResourceColor

**Default:** 'sys.color.comp_background_tertiary'

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-PickerBackgroundStyle-color?: ResourceColor--><!--Device-PickerBackgroundStyle-color?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

