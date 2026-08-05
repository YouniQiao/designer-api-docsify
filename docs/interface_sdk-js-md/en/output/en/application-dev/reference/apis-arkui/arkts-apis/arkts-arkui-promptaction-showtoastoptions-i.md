# ShowToastOptions

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-promptAction-interface ShowToastOptions--><!--Device-promptAction-interface ShowToastOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## alignment

```TypeScript
alignment?: Alignment
```

Alignment mode.\_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_ Default value: **undefined**. If **alignment** is not set and a navigation bar or soft keyboard is present, the toast is automatically adjusted according to the position of the navigation bar or soft keyboard. For details, see the description of **bottom**.\_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_ **NOTE**\_\_\_HTML\_TAG\_DESC\_USD\_3\_\_\_ The figure below shows the position of the toast in different alignment modes.\_\_\_HTML\_TAG\_DESC\_USD\_4\_\_\_ !\_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_\_\_\_HTML\_TAG\_DESC\_USD\_5\_\_\_ The text display of the toast is always left-aligned; other alignment modes are not supported.

**Type:** Alignment

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ShowToastOptions-alignment?: Alignment--><!--Device-ShowToastOptions-alignment?: Alignment-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundBlurStyle

```TypeScript
backgroundBlurStyle?: BlurStyle
```

Background blur style of the toast.\_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_ Default value: **BlurStyle.COMPONENT\_ULTRA\_THICK**\_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_ **NOTE**\_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_ Setting this parameter to **BlurStyle.NONE** disables the background blur. When **backgroundBlurStyle** is set to a value other than **NONE**, do not set **backgroundColor**. If you do, the color display may not produce the expected visual effect.

**Type:** BlurStyle

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ShowToastOptions-backgroundBlurStyle?: BlurStyle--><!--Device-ShowToastOptions-backgroundBlurStyle?: BlurStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundColor

```TypeScript
backgroundColor?: ResourceColor
```

Background color of the toast.\_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_ Default value: **Color.Transparent**.\_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_ **NOTE**\_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_ The background color will be visually combined with the blur effect when both properties are set. If the resulting effect does not match your design requirements, you can disable the blur effect entirely by explicitly setting the **backgroundBlurStyle** property to **BlurStyle.NONE**.

**Type:** ResourceColor

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ShowToastOptions-backgroundColor?: ResourceColor--><!--Device-ShowToastOptions-backgroundColor?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## bottom

```TypeScript
bottom?: string | number
```

Distance from the bottom of the toast to the navigation bar. If the soft keyboard is raised and the **bottom** value is too small, the toast will automatically avoid being blocked by the soft keyboard by moving up 80 vp above it.\_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_ Default value: **80vp**\_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_ **NOTE**\_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_ When there is no navigation bar at the bottom, **bottom** sets the distance from the bottom of the toast to the bottom of the window.\_\_\_HTML\_TAG\_DESC\_USD\_3\_\_\_If the **alignment** property is set, **bottom** will not take effect.

**Type:** string \| number

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ShowToastOptions-bottom?: string | number--><!--Device-ShowToastOptions-bottom?: string | number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## duration

```TypeScript
duration?: number
```

Duration that the toast will remain on the screen.\_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_Default value: 1500 ms.\_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_ Value range: [1500, 10000].\_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_ If a value less than 1500 ms is set, the default value is used. If the value greater than 10000 ms is set, the upper limit 10000 ms is used.

**Type:** number

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ShowToastOptions-duration?: number--><!--Device-ShowToastOptions-duration?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## enableHoverMode

```TypeScript
enableHoverMode?: boolean
```

Whether to respond when the device is in semi-folded mode. The value **true** means to respond when the device is in semi-folded mode.\_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_ Default value: **false**, meaning not to respond when the device is in semi-folded mode.

**Type:** boolean

**Default:** false

**Since:** 14

**ArkTS mode:** ArkTS-Dyn only, since version 14.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-ShowToastOptions-enableHoverMode?: boolean--><!--Device-ShowToastOptions-enableHoverMode?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## hoverModeArea

```TypeScript
hoverModeArea?: HoverModeAreaType
```

Display area of the toast in the hover state.\_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_ Default value: **HoverModeAreaType.BOTTOM\_SCREEN**, indicating that the toast is displayed in the lower half screen

**Type:** HoverModeAreaType

**Default:** HoverModeAreaType.BOTTOM_SCREEN

**Since:** 14

**ArkTS mode:** ArkTS-Dyn only, since version 14.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-ShowToastOptions-hoverModeArea?: HoverModeAreaType--><!--Device-ShowToastOptions-hoverModeArea?: HoverModeAreaType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## message

```TypeScript
message: string | Resource
```

Text to display. \_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_**NOTE** \_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_The default font is **'Harmony Sans'**. Other fonts are not supported.\_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_

**Type:** string \| Resource

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ShowToastOptions-message: string | Resource--><!--Device-ShowToastOptions-message: string | Resource-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## offset

```TypeScript
offset?: Offset
```

Offset in the specified alignment mode.\_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_ Default value: **{ dx: 0, dy: 0 }**, indicating no offset\_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_ **NOTE**\_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_ Only values in units of px are supported. Values in other units must be converted to units of px before being passed in. For example, to set a value in vp, convert it to px first and then pass the converted value.

**Type:** Offset

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ShowToastOptions-offset?: Offset--><!--Device-ShowToastOptions-offset?: Offset-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## shadow

```TypeScript
shadow?: ShadowOptions | ShadowStyle
```

Shadow of the toast background.\_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_ Default value: **ShadowStyle.OUTER\_DEFAULT\_MD**

**Type:** ShadowOptions \| ShadowStyle

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ShowToastOptions-shadow?: ShadowOptions | ShadowStyle--><!--Device-ShowToastOptions-shadow?: ShadowOptions | ShadowStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## showMode

```TypeScript
showMode?: ToastShowMode
```

Display level mode of the toast.\_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_ Default value: **ToastShowMode.DEFAULT**, which means to show the toast in the application.

**Type:** ToastShowMode

**Default:** ToastShowMode.DEFAULT

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ShowToastOptions-showMode?: ToastShowMode--><!--Device-ShowToastOptions-showMode?: ToastShowMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## systemMaterial

```TypeScript
systemMaterial?: SystemUiMaterial
```

Set system-styled materials for toast. Different materials have different effects, which can influence backgroundColor, border, shadow, and other visual attributes of toast.

**Type:** SystemUiMaterial

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ShowToastOptions-systemMaterial?: SystemUiMaterial--><!--Device-ShowToastOptions-systemMaterial?: SystemUiMaterial-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## textColor

```TypeScript
textColor?: ResourceColor
```

Text color of the toast.\_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_Default value: **Color.Black**.

**Type:** ResourceColor

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ShowToastOptions-textColor?: ResourceColor--><!--Device-ShowToastOptions-textColor?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

