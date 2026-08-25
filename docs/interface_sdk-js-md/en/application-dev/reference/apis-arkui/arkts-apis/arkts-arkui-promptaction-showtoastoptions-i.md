# ShowToastOptions

**Since:** 9

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { promptAction, LevelMode, ImmersiveMode, LevelOrder } from 'kits/@kit.ArkUI';
```

## alignment

```TypeScript
alignment?: Alignment
```

Alignment mode.Default value: **undefined**. If **alignment** is not set and a navigation bar or soft keyboard is present, the toast is automatically adjusted according to the position of the navigation bar or soft keyboard. For details, see the description of **bottom**.  
**NOTE：**The figure below shows the position of the toast in different alignment modes.The text display of the toast is always left-aligned; other alignment modes are not supported.

**Type:** [Alignment](arkts-arkui-alignment-e.md)

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundBlurStyle

```TypeScript
backgroundBlurStyle?: BlurStyle
```

Background blur style of the toast.Default value: **BlurStyle.COMPONENT_ULTRA_THICK**  
**NOTE：**Setting this parameter to **BlurStyle.NONE** disables the background blur. When **backgroundBlurStyle** is set to a value other than **NONE**, do not set **backgroundColor**. If you do, the color display may not produce the expected visual effect.

**Type:** BlurStyle

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundColor

```TypeScript
backgroundColor?: ResourceColor
```

Background color of the toast.Default value: **Color.Transparent**.  
**NOTE：**The background color will be visually combined with the blur effect when both properties are set. If the resulting effect does not match your design requirements, you can disable the blur effect entirely by explicitly setting the **backgroundBlurStyle** property to **BlurStyle.NONE**.

**Type:** [ResourceColor](arkts-arkui-resourcecolor-t.md)

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## bottom

```TypeScript
bottom?: string | number
```

Distance from the bottom of the toast to the navigation bar. If the soft keyboard is raised and the **bottom** value is too small, the toast will automatically avoid being blocked by the soft keyboard by moving up 80 vp above it.Default value: **80vp**  
**NOTE：**When there is no navigation bar at the bottom, **bottom** sets the distance from the bottom of the toast to the bottom of the window.If the **alignment** property is set, **bottom** will not take effect.

**Type:** string \| number

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## duration

```TypeScript
duration?: number
```

Duration that the toast will remain on the screen.Default value: 1500 ms.Value range: [1500, 10000].If a value less than 1500 ms is set, the default value is used. If the value greater than 10000 ms is set, the upper limit 10000 ms is used.

**Type:** number

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## enableHoverMode

```TypeScript
enableHoverMode?: boolean
```

Whether to respond when the device is in semi-folded mode. The value **true** means to respond when the device is in semi-folded mode.Default value: **false**, meaning not to respond when the device is in semi-folded mode.

**Type:** boolean

**Default:** false

**Since:** 14

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## hoverModeArea

```TypeScript
hoverModeArea?: HoverModeAreaType
```

Display area of the toast in the hover state.Default value: **HoverModeAreaType.BOTTOM_SCREEN**, indicating that the toast is displayed in the lower half screen

**Type:** [HoverModeAreaType](../arkts-components/arkts-arkui-hovermodeareatype-e.md)

**Default:** HoverModeAreaType.BOTTOM_SCREEN

**Since:** 14

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## message

```TypeScript
message: string | Resource
```

Text to display.   
**NOTE：**The default font is **'Harmony Sans'**. Other fonts are not supported.

**Type:** string \| Resource

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## offset

```TypeScript
offset?: Offset
```

Offset in the specified alignment mode.Default value: **{ dx: 0, dy: 0 }**, indicating no offset  
**NOTE：**Only values in units of px are supported. Values in other units must be converted to units of px before being passed in. For example, to set a value in vp, convert it to px first and then pass the converted value.

**Type:** Offset

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## shadow

```TypeScript
shadow?: ShadowOptions | ShadowStyle
```

Shadow of the toast background.Default value: **ShadowStyle.OUTER_DEFAULT_MD**

**Type:** [ShadowOptions](../arkts-components/arkts-arkui-shadowoptions-i.md) \| [ShadowStyle](../arkts-components/arkts-arkui-shadowstyle-e.md)

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## showMode

```TypeScript
showMode?: ToastShowMode
```

Display level mode of the toast.Default value: **ToastShowMode.DEFAULT**, which means to show the toast in the application.

**Type:** [ToastShowMode](arkts-arkui-promptaction-toastshowmode-e.md)

**Default:** ToastShowMode.DEFAULT

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## systemMaterial

```TypeScript
systemMaterial?: SystemUiMaterial
```

Set system-styled materials for toast. Different materials have different effects, which can influence backgroundColor, border, shadow, and other visual attributes of toast.

**Type:** [SystemUiMaterial](../arkts-components/arkts-arkui-systemuimaterial-t.md)

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## textColor

```TypeScript
textColor?: ResourceColor
```

Text color of the toast.Default value: **Color.Black**.

**Type:** [ResourceColor](arkts-arkui-resourcecolor-t.md)

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full
