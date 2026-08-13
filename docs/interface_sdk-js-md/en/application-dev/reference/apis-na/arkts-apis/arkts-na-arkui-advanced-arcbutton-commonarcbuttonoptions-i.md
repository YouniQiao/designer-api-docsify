# CommonArcButtonOptions

Defines the arc button options.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-export declare interface CommonArcButtonOptions--><!--Device-unnamed-export declare interface CommonArcButtonOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## backgroundBlurStyle

```TypeScript
backgroundBlurStyle?: BlurStyle
```

Describe the blurred background style of the arc-shaped button.

**Type:** BlurStyle

**Default:** BlurStyle.NONE

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-CommonArcButtonOptions-backgroundBlurStyle?: BlurStyle--><!--Device-CommonArcButtonOptions-backgroundBlurStyle?: BlurStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## backgroundColor

```TypeScript
backgroundColor?: ColorMetrics
```

Describes the arc button background color.

**Type:** ColorMetrics

**Default:** Color.Black

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-CommonArcButtonOptions-backgroundColor?: ColorMetrics--><!--Device-CommonArcButtonOptions-backgroundColor?: ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## fontColor

```TypeScript
fontColor?: ColorMetrics
```

Describes the arc button text color.

**Type:** ColorMetrics

**Default:** Color.White

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-CommonArcButtonOptions-fontColor?: ColorMetrics--><!--Device-CommonArcButtonOptions-fontColor?: ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## fontFamily

```TypeScript
fontFamily?: string | Resource
```

Describes the arc button text family.

**Type:** string \| Resource

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-CommonArcButtonOptions-fontFamily?: string | Resource--><!--Device-CommonArcButtonOptions-fontFamily?: string | Resource-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## fontMargin

```TypeScript
fontMargin?: LocalizedMargin
```

Describes the arc button text margin.

**Type:** LocalizedMargin

**Default:** { start: 24.0_vp, top: 10.0_vp, end: 24.0_vp, bottom: 16.0_vp }

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-CommonArcButtonOptions-fontMargin?: LocalizedMargin--><!--Device-CommonArcButtonOptions-fontMargin?: LocalizedMargin-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## fontSize

```TypeScript
fontSize?: LengthMetrics
```

Describes the arc button text size.

**Type:** LengthMetrics

**Default:** 19.0_fp

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-CommonArcButtonOptions-fontSize?: LengthMetrics--><!--Device-CommonArcButtonOptions-fontSize?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## fontStyle

```TypeScript
fontStyle?: FontStyle
```

Describes the arc button text style.

**Type:** FontStyle

**Default:** FontStyle.Normal

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-CommonArcButtonOptions-fontStyle?: FontStyle--><!--Device-CommonArcButtonOptions-fontStyle?: FontStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## label

```TypeScript
label?: ResourceStr
```

Describes the arc button displays text.

**Type:** ResourceStr

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-CommonArcButtonOptions-label?: ResourceStr--><!--Device-CommonArcButtonOptions-label?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## onClick

```TypeScript
onClick?: Callback<ClickEvent>
```

Describes the arc button click event.

**Type:** [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ClickEvent&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-CommonArcButtonOptions-onClick?: Callback<ClickEvent>--><!--Device-CommonArcButtonOptions-onClick?: Callback<ClickEvent>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## onTouch

```TypeScript
onTouch?: Callback<TouchEvent>
```

Describes the arc button touch event.

**Type:** [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;TouchEvent&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-CommonArcButtonOptions-onTouch?: Callback<TouchEvent>--><!--Device-CommonArcButtonOptions-onTouch?: Callback<TouchEvent>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## position

```TypeScript
position?: ArcButtonPosition
```

Describes the arc button position.

**Type:** [ArcButtonPosition](arkts-na-arkui-advanced-arcbutton-arcbuttonposition-e.md)

**Default:** ArcButtonPosition.BOTTOM_EDGE

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-CommonArcButtonOptions-position?: ArcButtonPosition--><!--Device-CommonArcButtonOptions-position?: ArcButtonPosition-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## pressedFontColor

```TypeScript
pressedFontColor?: ColorMetrics
```

Describes the arc button pressed text color.

**Type:** ColorMetrics

**Default:** Color.White

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-CommonArcButtonOptions-pressedFontColor?: ColorMetrics--><!--Device-CommonArcButtonOptions-pressedFontColor?: ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## progressConfig

```TypeScript
progressConfig?: ArcButtonProgressConfig
```

Sets the ArcButton progress bar parameters. When not set, the button style is used. When set, the progress style is used.

**Type:** [ArcButtonProgressConfig](arkts-na-arkui-advanced-arcbutton-arcbuttonprogressconfig-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonArcButtonOptions-progressConfig?: ArcButtonProgressConfig--><!--Device-CommonArcButtonOptions-progressConfig?: ArcButtonProgressConfig-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## shadowColor

```TypeScript
shadowColor?: ColorMetrics
```

Describes the arc button shadow color.

**Type:** ColorMetrics

**Default:** Color.Black

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-CommonArcButtonOptions-shadowColor?: ColorMetrics--><!--Device-CommonArcButtonOptions-shadowColor?: ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## shadowEnabled

```TypeScript
shadowEnabled?: boolean
```

Describes the arc button shadow switch.

**Type:** boolean

**Default:** false

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-CommonArcButtonOptions-shadowEnabled?: boolean--><!--Device-CommonArcButtonOptions-shadowEnabled?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## status

```TypeScript
status?: ArcButtonStatus
```

Describes the arc button status.

**Type:** [ArcButtonStatus](arkts-na-arkui-advanced-arcbutton-arcbuttonstatus-e.md)

**Default:** ArcButtonStatus.NORMAL

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-CommonArcButtonOptions-status?: ArcButtonStatus--><!--Device-CommonArcButtonOptions-status?: ArcButtonStatus-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## styleMode

```TypeScript
styleMode?: ArcButtonStyleMode
```

Describes the arc button style mode.

**Type:** [ArcButtonStyleMode](arkts-na-arkui-advanced-arcbutton-arcbuttonstylemode-e.md)

**Default:** ArcButtonStyleMode.EMPHASIZED_LIGHT

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-CommonArcButtonOptions-styleMode?: ArcButtonStyleMode--><!--Device-CommonArcButtonOptions-styleMode?: ArcButtonStyleMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

