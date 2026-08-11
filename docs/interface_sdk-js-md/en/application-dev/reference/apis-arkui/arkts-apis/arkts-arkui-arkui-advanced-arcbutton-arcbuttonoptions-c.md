# ArcButtonOptions

The class for ArcButtonOptions.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Decorator:** @ObservedV2

<!--Device-unnamed-export declare class ArcButtonOptions--><!--Device-unnamed-export declare class ArcButtonOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## Modules to Import

```TypeScript
import { ArcButtonPosition, ArcButton, ArcButtonStatus, ArcButtonStyleMode, ArcButtonOptions, ArcButtonProgressConfig } from 'kits/@kit.ArkUI';
```

## constructor

```TypeScript
constructor(options: CommonArcButtonOptions)
```

Constructor of the CommonArcButtonOptions.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-ArcButtonOptions-constructor(options: CommonArcButtonOptions)--><!--Device-ArcButtonOptions-constructor(options: CommonArcButtonOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [CommonArcButtonOptions](arkts-arkui-arkui-advanced-arcbutton-commonarcbuttonoptions-i.md) | Yes |  |

## backgroundBlurStyle

```TypeScript
public backgroundBlurStyle: BlurStyle
```

Describe the blurred background style of the arc-shaped button.

**Type:** [BlurStyle](../arkts-components/arkts-arkui-blurstyle-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-ArcButtonOptions-public backgroundBlurStyle: BlurStyle--><!--Device-ArcButtonOptions-public backgroundBlurStyle: BlurStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## backgroundColor

```TypeScript
public backgroundColor: ColorMetrics
```

Describes the arc button background color.

**Type:** [ColorMetrics](arkts-arkui-colormetrics-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-ArcButtonOptions-public backgroundColor: ColorMetrics--><!--Device-ArcButtonOptions-public backgroundColor: ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## fontColor

```TypeScript
public fontColor: ColorMetrics
```

Describes the arc button text color.

**Type:** [ColorMetrics](arkts-arkui-colormetrics-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-ArcButtonOptions-public fontColor: ColorMetrics--><!--Device-ArcButtonOptions-public fontColor: ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## fontFamily

```TypeScript
public fontFamily: string | Resource
```

Describes the arc button text family.

**Type:** string \| Resource

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-ArcButtonOptions-public fontFamily: string | Resource--><!--Device-ArcButtonOptions-public fontFamily: string | Resource-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## fontMargin

```TypeScript
public fontMargin: LocalizedMargin
```

Describes the arc button text margin.

**Type:** [LocalizedMargin](arkts-arkui-localizedmargin-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-ArcButtonOptions-public fontMargin: LocalizedMargin--><!--Device-ArcButtonOptions-public fontMargin: LocalizedMargin-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## fontSize

```TypeScript
public fontSize: LengthMetrics
```

Describes the arc button text size.

**Type:** [LengthMetrics](arkts-arkui-lengthmetrics-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-ArcButtonOptions-public fontSize: LengthMetrics--><!--Device-ArcButtonOptions-public fontSize: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## fontStyle

```TypeScript
public fontStyle: FontStyle
```

Describes the arc button text style.

**Type:** [FontStyle](arkts-arkui-fontstyle-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-ArcButtonOptions-public fontStyle: FontStyle--><!--Device-ArcButtonOptions-public fontStyle: FontStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## label

```TypeScript
public label: ResourceStr
```

Describes the arc button displays text.

**Type:** [ResourceStr](arkts-arkui-resourcestr-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-ArcButtonOptions-public label: ResourceStr--><!--Device-ArcButtonOptions-public label: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## onClick

```TypeScript
public onClick?: Callback<ClickEvent>
```

Describes the arc button click event.

**Type:** [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ClickEvent](../arkts-components/arkts-arkui-clickevent-i.md)&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-ArcButtonOptions-public onClick?: Callback<ClickEvent>--><!--Device-ArcButtonOptions-public onClick?: Callback<ClickEvent>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## onTouch

```TypeScript
public onTouch?: Callback<TouchEvent>
```

Describes the arc button touch event.

**Type:** [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[TouchEvent](../arkts-components/arkts-arkui-touchevent-i.md)&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-ArcButtonOptions-public onTouch?: Callback<TouchEvent>--><!--Device-ArcButtonOptions-public onTouch?: Callback<TouchEvent>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## position

```TypeScript
public position: ArcButtonPosition
```

Describes the position of button on screen.

**Type:** [ArcButtonPosition](arkts-arkui-arkui-advanced-arcbutton-arcbuttonposition-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-ArcButtonOptions-public position: ArcButtonPosition--><!--Device-ArcButtonOptions-public position: ArcButtonPosition-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## pressedFontColor

```TypeScript
public pressedFontColor: ColorMetrics
```

Describes the arc button pressed text color.

**Type:** [ColorMetrics](arkts-arkui-colormetrics-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-ArcButtonOptions-public pressedFontColor: ColorMetrics--><!--Device-ArcButtonOptions-public pressedFontColor: ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## progressConfig

```TypeScript
public progressConfig?: ArcButtonProgressConfig
```

Sets the ArcButton progress bar parameters.When not set, the button style is used.When set, the progress style is used.

**Type:** [ArcButtonProgressConfig](arkts-arkui-arkui-advanced-arcbutton-arcbuttonprogressconfig-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArcButtonOptions-public progressConfig?: ArcButtonProgressConfig--><!--Device-ArcButtonOptions-public progressConfig?: ArcButtonProgressConfig-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## shadowColor

```TypeScript
public shadowColor: ColorMetrics
```

Describes the arc button shadow color.

**Type:** [ColorMetrics](arkts-arkui-colormetrics-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-ArcButtonOptions-public shadowColor: ColorMetrics--><!--Device-ArcButtonOptions-public shadowColor: ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## shadowEnabled

```TypeScript
public shadowEnabled: boolean
```

Describes the arc button shadow switch.

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-ArcButtonOptions-public shadowEnabled: boolean--><!--Device-ArcButtonOptions-public shadowEnabled: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## status

```TypeScript
public status: ArcButtonStatus
```

Describes the arc button status.

**Type:** [ArcButtonStatus](arkts-arkui-arkui-advanced-arcbutton-arcbuttonstatus-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-ArcButtonOptions-public status: ArcButtonStatus--><!--Device-ArcButtonOptions-public status: ArcButtonStatus-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## styleMode

```TypeScript
public styleMode: ArcButtonStyleMode
```

Describes the arc button style mode.

**Type:** [ArcButtonStyleMode](arkts-arkui-arkui-advanced-arcbutton-arcbuttonstylemode-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-ArcButtonOptions-public styleMode: ArcButtonStyleMode--><!--Device-ArcButtonOptions-public styleMode: ArcButtonStyleMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

