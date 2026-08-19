# ShowToastOptions

Show toast options.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-promptAction-export interface ShowToastOptions--><!--Device-promptAction-export interface ShowToastOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## alignment

```TypeScript
alignment?: Alignment
```

Defines the toast alignment of the screen.

**Type:** Alignment

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ShowToastOptions-alignment?: Alignment--><!--Device-ShowToastOptions-alignment?: Alignment-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundBlurStyle

```TypeScript
backgroundBlurStyle?: BlurStyle
```

Background blur Style of toast.

**Type:** BlurStyle

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ShowToastOptions-backgroundBlurStyle?: BlurStyle--><!--Device-ShowToastOptions-backgroundBlurStyle?: BlurStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundColor

```TypeScript
backgroundColor?: ResourceColor
```

Background color of toast.

**Type:** ResourceColor

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ShowToastOptions-backgroundColor?: ResourceColor--><!--Device-ShowToastOptions-backgroundColor?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## bottom

```TypeScript
bottom?: string | double
```

The distance between toast dialog box and the bottom of screen.

**Type:** string \| double

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ShowToastOptions-bottom?: string | double--><!--Device-ShowToastOptions-bottom?: string | double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## duration

```TypeScript
duration?: int
```

Duration of toast dialog box. The default value is 1500. The recommended value ranges from 1500ms to 10000ms. NOTE: A value less than 1500 is automatically changed to 1500. The maximum value is 10000ms.

**Type:** int

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ShowToastOptions-duration?: int--><!--Device-ShowToastOptions-duration?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## enableHoverMode

```TypeScript
enableHoverMode?: boolean
```

Define whether to respond to the hover mode.

**Type:** boolean

**Default:** false

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ShowToastOptions-enableHoverMode?: boolean--><!--Device-ShowToastOptions-enableHoverMode?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## hoverModeArea

```TypeScript
hoverModeArea?: HoverModeAreaType
```

Defines the toast's display area in hover mode.

**Type:** HoverModeAreaType

**Default:** HoverModeAreaType.BOTTOM_SCREEN

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ShowToastOptions-hoverModeArea?: HoverModeAreaType--><!--Device-ShowToastOptions-hoverModeArea?: HoverModeAreaType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## message

```TypeScript
message: string | Resource
```

Text to display.

**Type:** string \| Resource

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ShowToastOptions-message: string | Resource--><!--Device-ShowToastOptions-message: string | Resource-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## offset

```TypeScript
offset?: Offset
```

Defines the toast offset.

**Type:** Offset

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ShowToastOptions-offset?: Offset--><!--Device-ShowToastOptions-offset?: Offset-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## shadow

```TypeScript
shadow?: ShadowOptions | ShadowStyle
```

Shadow of toast.

**Type:** ShadowOptions \| ShadowStyle

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ShowToastOptions-shadow?: ShadowOptions | ShadowStyle--><!--Device-ShowToastOptions-shadow?: ShadowOptions | ShadowStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## showMode

```TypeScript
showMode?: ToastShowMode
```

Determine the show mode of the toast.

**Type:** [ToastShowMode](arkts-na-promptaction-toastshowmode-e.md)

**Default:** ToastShowMode.DEFAULT

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ShowToastOptions-showMode?: ToastShowMode--><!--Device-ShowToastOptions-showMode?: ToastShowMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## systemMaterial

```TypeScript
systemMaterial?: SystemUiMaterial
```

Set system-styled materials for toast. Different materials have different effects, which can influence backgroundColor, border, shadow, and other visual attributes of toast.

**Type:** SystemUiMaterial

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ShowToastOptions-systemMaterial?: SystemUiMaterial--><!--Device-ShowToastOptions-systemMaterial?: SystemUiMaterial-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## textColor

```TypeScript
textColor?: ResourceColor
```

Text color of toast.

**Type:** ResourceColor

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ShowToastOptions-textColor?: ResourceColor--><!--Device-ShowToastOptions-textColor?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

