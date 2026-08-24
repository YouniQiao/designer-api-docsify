# ArcButtonOptions

The class for ArcButtonOptions.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Decorator:** @ObservedV2

<!--Device-unnamed-export declare class ArcButtonOptions--><!--Device-unnamed-export declare class ArcButtonOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## Modules to Import

```TypeScript
```

## constructor

```TypeScript
constructor(options: CommonArcButtonOptions)
```

Constructor of the CommonArcButtonOptions.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-ArcButtonOptions-constructor(options: CommonArcButtonOptions)--><!--Device-ArcButtonOptions-constructor(options: CommonArcButtonOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [CommonArcButtonOptions](arkts-arkui-advanced-arcbutton-commonarcbuttonoptions-i.md) | Yes |  |

## backgroundBlurStyle

```TypeScript
public backgroundBlurStyle: BlurStyle
```

Describe the blurred background style of the arc-shaped button.

**Type:** BlurStyle

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Decorator:** @Trace

<!--Device-ArcButtonOptions-@Trace  public backgroundBlurStyle: BlurStyle--><!--Device-ArcButtonOptions-@Trace  public backgroundBlurStyle: BlurStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## backgroundColor

```TypeScript
public backgroundColor: ColorMetrics
```

Describes the arc button background color.

**Type:** ColorMetrics

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Decorator:** @Trace

<!--Device-ArcButtonOptions-@Trace  public backgroundColor: ColorMetrics--><!--Device-ArcButtonOptions-@Trace  public backgroundColor: ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## fontColor

```TypeScript
public fontColor: ColorMetrics
```

Describes the arc button text color.

**Type:** ColorMetrics

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Decorator:** @Trace

<!--Device-ArcButtonOptions-@Trace  public fontColor: ColorMetrics--><!--Device-ArcButtonOptions-@Trace  public fontColor: ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## fontFamily

```TypeScript
public fontFamily: string | Resource
```

Describes the arc button text family.

**Type:** string \| Resource

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Decorator:** @Trace

<!--Device-ArcButtonOptions-@Trace  public fontFamily: string | Resource--><!--Device-ArcButtonOptions-@Trace  public fontFamily: string | Resource-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## fontMargin

```TypeScript
public fontMargin: LocalizedMargin
```

Describes the arc button text margin.

**Type:** LocalizedMargin

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Decorator:** @Trace

<!--Device-ArcButtonOptions-@Trace  public fontMargin: LocalizedMargin--><!--Device-ArcButtonOptions-@Trace  public fontMargin: LocalizedMargin-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## fontSize

```TypeScript
public fontSize: LengthMetrics
```

Describes the arc button text size.

**Type:** LengthMetrics

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Decorator:** @Trace

<!--Device-ArcButtonOptions-@Trace  public fontSize: LengthMetrics--><!--Device-ArcButtonOptions-@Trace  public fontSize: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## fontStyle

```TypeScript
public fontStyle: FontStyle
```

Describes the arc button text style.

**Type:** FontStyle

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Decorator:** @Trace

<!--Device-ArcButtonOptions-@Trace  public fontStyle: FontStyle--><!--Device-ArcButtonOptions-@Trace  public fontStyle: FontStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## label

```TypeScript
public label: ResourceStr
```

Describes the arc button displays text.

**Type:** ResourceStr

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Decorator:** @Trace

<!--Device-ArcButtonOptions-@Trace  public label: ResourceStr--><!--Device-ArcButtonOptions-@Trace  public label: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## onClick

```TypeScript
public onClick?: Callback<ClickEvent>
```

Describes the arc button click event.

**Type:** [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ClickEvent&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Decorator:** @Trace

<!--Device-ArcButtonOptions-@Trace  public onClick?: Callback<ClickEvent>--><!--Device-ArcButtonOptions-@Trace  public onClick?: Callback<ClickEvent>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## onTouch

```TypeScript
public onTouch?: Callback<TouchEvent>
```

Describes the arc button touch event.

**Type:** [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;TouchEvent&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Decorator:** @Trace

<!--Device-ArcButtonOptions-@Trace  public onTouch?: Callback<TouchEvent>--><!--Device-ArcButtonOptions-@Trace  public onTouch?: Callback<TouchEvent>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## position

```TypeScript
public position: ArcButtonPosition
```

Describes the position of button on screen.

**Type:** [ArcButtonPosition](arkts-arkui-advanced-arcbutton-arcbuttonposition-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Decorator:** @Trace

<!--Device-ArcButtonOptions-@Trace  public position: ArcButtonPosition--><!--Device-ArcButtonOptions-@Trace  public position: ArcButtonPosition-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## pressedFontColor

```TypeScript
public pressedFontColor: ColorMetrics
```

Describes the arc button pressed text color.

**Type:** ColorMetrics

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Decorator:** @Trace

<!--Device-ArcButtonOptions-@Trace  public pressedFontColor: ColorMetrics--><!--Device-ArcButtonOptions-@Trace  public pressedFontColor: ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## progressConfig

```TypeScript
public progressConfig?: ArcButtonProgressConfig
```

Sets the ArcButton progress bar parameters. When not set, the button style is used. When set, the progress style is used.

**Type:** [ArcButtonProgressConfig](arkts-arkui-advanced-arcbutton-arcbuttonprogressconfig-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Decorator:** @Trace

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArcButtonOptions-@Trace  public progressConfig?: ArcButtonProgressConfig--><!--Device-ArcButtonOptions-@Trace  public progressConfig?: ArcButtonProgressConfig-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## shadowColor

```TypeScript
public shadowColor: ColorMetrics
```

Describes the arc button shadow color.

**Type:** ColorMetrics

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Decorator:** @Trace

<!--Device-ArcButtonOptions-@Trace  public shadowColor: ColorMetrics--><!--Device-ArcButtonOptions-@Trace  public shadowColor: ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## shadowEnabled

```TypeScript
public shadowEnabled: boolean
```

Describes the arc button shadow switch.

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Decorator:** @Trace

<!--Device-ArcButtonOptions-@Trace  public shadowEnabled: boolean--><!--Device-ArcButtonOptions-@Trace  public shadowEnabled: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## status

```TypeScript
public status: ArcButtonStatus
```

Describes the arc button status.

**Type:** [ArcButtonStatus](arkts-arkui-advanced-arcbutton-arcbuttonstatus-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Decorator:** @Trace

<!--Device-ArcButtonOptions-@Trace  public status: ArcButtonStatus--><!--Device-ArcButtonOptions-@Trace  public status: ArcButtonStatus-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## styleMode

```TypeScript
public styleMode: ArcButtonStyleMode
```

Describes the arc button style mode.

**Type:** [ArcButtonStyleMode](arkts-arkui-advanced-arcbutton-arcbuttonstylemode-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Decorator:** @Trace

<!--Device-ArcButtonOptions-@Trace  public styleMode: ArcButtonStyleMode--><!--Device-ArcButtonOptions-@Trace  public styleMode: ArcButtonStyleMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

