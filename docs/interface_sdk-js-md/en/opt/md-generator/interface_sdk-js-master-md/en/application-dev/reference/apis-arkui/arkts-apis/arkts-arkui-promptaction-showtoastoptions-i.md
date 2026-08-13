# ShowToastOptions

**Since:** 9

**Deprecated since:** -1

<!--Device-promptAction-interface ShowToastOptions--><!--Device-promptAction-interface ShowToastOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { LevelMode, ImmersiveMode, LevelOrder } from '@kit.ArkUI';
```

## alignment

```TypeScript
alignment?: Alignment
```

Alignment mode.&lt;br&gt; Default value: **undefined**. If **alignment** is not set and a navigation bar or soft keyboard is present, the toast is automatically adjusted according to the position of the navigation bar or soft keyboard. For details, see the description of **bottom**.&lt;br&gt; **NOTE：**&lt;br&gt; The figure below shows the position of the toast in different alignment modes.&lt;br&gt; &lt;br&gt; The text display of the toast is always left-aligned; other alignment modes are not supported.

**Type:** [Alignment](arkts-arkui-alignment-e.md)

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ShowToastOptions-alignment?: Alignment--><!--Device-ShowToastOptions-alignment?: Alignment-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundBlurStyle

```TypeScript
backgroundBlurStyle?: BlurStyle
```

Background blur style of the toast.&lt;br&gt; Default value: **BlurStyle.COMPONENT_ULTRA_THICK**&lt;br&gt; **NOTE：**&lt;br&gt; Setting this parameter to **BlurStyle.NONE** disables the background blur. When **backgroundBlurStyle** is set to a value other than **NONE**, do not set **backgroundColor**. If you do, the color display may not produce the expected visual effect.

**Type:** BlurStyle

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ShowToastOptions-backgroundBlurStyle?: BlurStyle--><!--Device-ShowToastOptions-backgroundBlurStyle?: BlurStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundColor

```TypeScript
backgroundColor?: ResourceColor
```

Background color of the toast.&lt;br&gt; Default value: **Color.Transparent**.&lt;br&gt; **NOTE：**&lt;br&gt; The background color will be visually combined with the blur effect when both properties are set. If the resulting effect does not match your design requirements, you can disable the blur effect entirely by explicitly setting the **backgroundBlurStyle** property to **BlurStyle.NONE**.

**Type:** [ResourceColor](arkts-arkui-resourcecolor-t.md)

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ShowToastOptions-backgroundColor?: ResourceColor--><!--Device-ShowToastOptions-backgroundColor?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## bottom

```TypeScript
bottom?: string | number
```

Distance from the bottom of the toast to the navigation bar. If the soft keyboard is raised and the **bottom** value is too small, the toast will automatically avoid being blocked by the soft keyboard by moving up 80 vp above it.&lt;br&gt; Default value: **80vp**&lt;br&gt; **NOTE：**&lt;br&gt; When there is no navigation bar at the bottom, **bottom** sets the distance from the bottom of the toast to the bottom of the window.&lt;br&gt;If the **alignment** property is set, **bottom** will not take effect.

**Type:** string \| number

**Since:** 9

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ShowToastOptions-bottom?: string | number--><!--Device-ShowToastOptions-bottom?: string | number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## duration

```TypeScript
duration?: number
```

Duration that the toast will remain on the screen.&lt;br&gt;Default value: 1500 ms.&lt;br&gt; Value range: [1500, 10000].&lt;br&gt; If a value less than 1500 ms is set, the default value is used. If the value greater than 10000 ms is set, the upper limit 10000 ms is used.

**Type:** number

**Since:** 9

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ShowToastOptions-duration?: number--><!--Device-ShowToastOptions-duration?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## enableHoverMode

```TypeScript
enableHoverMode?: boolean
```

Whether to respond when the device is in semi-folded mode. The value **true** means to respond when the device is in semi-folded mode.&lt;br&gt; Default value: **false**, meaning not to respond when the device is in semi-folded mode.

**Type:** boolean

**Default:** false

**Since:** 14

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-ShowToastOptions-enableHoverMode?: boolean--><!--Device-ShowToastOptions-enableHoverMode?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## hoverModeArea

```TypeScript
hoverModeArea?: HoverModeAreaType
```

Display area of the toast in the hover state.&lt;br&gt; Default value: **HoverModeAreaType.BOTTOM_SCREEN**, indicating that the toast is displayed in the lower half screen

**Type:** [HoverModeAreaType](../arkts-components/arkts-arkui-hovermodeareatype-e.md)

**Default:** HoverModeAreaType.BOTTOM_SCREEN

**Since:** 14

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-ShowToastOptions-hoverModeArea?: HoverModeAreaType--><!--Device-ShowToastOptions-hoverModeArea?: HoverModeAreaType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## message

```TypeScript
message: string | Resource
```

Text to display. &lt;br&gt;**NOTE：**&lt;br&gt;The default font is **'Harmony Sans'**. Other fonts are not supported.&lt;br&gt;

**Type:** string \| Resource

**Since:** 9

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ShowToastOptions-message: string | Resource--><!--Device-ShowToastOptions-message: string | Resource-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## offset

```TypeScript
offset?: Offset
```

Offset in the specified alignment mode.&lt;br&gt; Default value: **{ dx: 0, dy: 0 }**, indicating no offset&lt;br&gt; **NOTE：**&lt;br&gt; Only values in units of px are supported. Values in other units must be converted to units of px before being passed in. For example, to set a value in vp, convert it to px first and then pass the converted value.

**Type:** Offset

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ShowToastOptions-offset?: Offset--><!--Device-ShowToastOptions-offset?: Offset-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## shadow

```TypeScript
shadow?: ShadowOptions | ShadowStyle
```

Shadow of the toast background.&lt;br&gt; Default value: **ShadowStyle.OUTER_DEFAULT_MD**

**Type:** [ShadowOptions](../arkts-components/arkts-arkui-shadowoptions-i.md) \| [ShadowStyle](../arkts-components/arkts-arkui-shadowstyle-e.md)

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ShowToastOptions-shadow?: ShadowOptions | ShadowStyle--><!--Device-ShowToastOptions-shadow?: ShadowOptions | ShadowStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## showMode

```TypeScript
showMode?: ToastShowMode
```

Display level mode of the toast.&lt;br&gt; Default value: **ToastShowMode.DEFAULT**, which means to show the toast in the application.

**Type:** [ToastShowMode](arkts-arkui-promptaction-toastshowmode-e.md)

**Default:** ToastShowMode.DEFAULT

**Since:** 11

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ShowToastOptions-showMode?: ToastShowMode--><!--Device-ShowToastOptions-showMode?: ToastShowMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## systemMaterial

```TypeScript
systemMaterial?: SystemUiMaterial
```

Set system-styled materials for toast. Different materials have different effects, which can influence backgroundColor, border, shadow, and other visual attributes of toast.

**Type:** [SystemUiMaterial](../arkts-components/arkts-arkui-systemuimaterial-t-sys.md)

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ShowToastOptions-systemMaterial?: SystemUiMaterial--><!--Device-ShowToastOptions-systemMaterial?: SystemUiMaterial-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## textColor

```TypeScript
textColor?: ResourceColor
```

Text color of the toast.&lt;br&gt;Default value: **Color.Black**.

**Type:** [ResourceColor](arkts-arkui-resourcecolor-t.md)

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ShowToastOptions-textColor?: ResourceColor--><!--Device-ShowToastOptions-textColor?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full
