# CommonArcButtonOptions

ArcButton的默认样式或自定义样式参数。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface CommonArcButtonOptions--><!--Device-unnamed-export declare interface CommonArcButtonOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## Modules to Import

```TypeScript
import { ArcButtonPosition, ArcButton, ArcButtonStatus, ArcButtonStyleMode, ArcButtonOptions, ArcButtonProgressConfig } from 'kits/@kit.ArkUI';
```

## backgroundBlurStyle

```TypeScript
backgroundBlurStyle?: BlurStyle
```

弧形按钮背景模糊能力。

默认值：BlurStyle.NONE

**Type:** [BlurStyle](../arkts-components/arkts-arkui-blurstyle-e.md)

**Default:** BlurStyle.NONE

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-CommonArcButtonOptions-backgroundBlurStyle?: BlurStyle--><!--Device-CommonArcButtonOptions-backgroundBlurStyle?: BlurStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## backgroundColor

```TypeScript
backgroundColor?: ColorMetrics
```

弧形按钮背景颜色。

ArcButtonStyleMode需要设置为CUSTOM。

默认值：Color.Black

**Type:** [ColorMetrics](arkts-arkui-colormetrics-t.md)

**Default:** Color.Black

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-CommonArcButtonOptions-backgroundColor?: ColorMetrics--><!--Device-CommonArcButtonOptions-backgroundColor?: ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## fontColor

```TypeScript
fontColor?: ColorMetrics
```

弧形按钮文本颜色。

ArcButtonStyleMode需要设置为CUSTOM。

默认值：Color.White

**Type:** [ColorMetrics](arkts-arkui-colormetrics-t.md)

**Default:** Color.White

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-CommonArcButtonOptions-fontColor?: ColorMetrics--><!--Device-CommonArcButtonOptions-fontColor?: ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## fontFamily

```TypeScript
fontFamily?: string | Resource
```

弧形按钮字体名。

**Type:** string \| Resource

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-CommonArcButtonOptions-fontFamily?: string | Resource--><!--Device-CommonArcButtonOptions-fontFamily?: string | Resource-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## fontMargin

```TypeScript
fontMargin?: LocalizedMargin
```

弧形按钮文本边距。

默认值：{start:24vp, top: 10vp,end: 24vp, bottom:16vp }

**Type:** [LocalizedMargin](arkts-arkui-localizedmargin-t.md)

**Default:** { start: 24.0_vp, top: 10.0_vp, end: 24.0_vp, bottom: 16.0_vp }

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-CommonArcButtonOptions-fontMargin?: LocalizedMargin--><!--Device-CommonArcButtonOptions-fontMargin?: LocalizedMargin-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## fontSize

```TypeScript
fontSize?: LengthMetrics
```

弧形按钮文本大小。

默认值：19fp

**Type:** [LengthMetrics](arkts-arkui-lengthmetrics-t.md)

**Default:** 19.0_fp

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-CommonArcButtonOptions-fontSize?: LengthMetrics--><!--Device-CommonArcButtonOptions-fontSize?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## fontStyle

```TypeScript
fontStyle?: FontStyle
```

弧形按钮文本样式。

默认值：FontStyle.Normal

**Type:** [FontStyle](arkts-arkui-fontstyle-e.md)

**Default:** FontStyle.Normal

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-CommonArcButtonOptions-fontStyle?: FontStyle--><!--Device-CommonArcButtonOptions-fontStyle?: FontStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## label

```TypeScript
label?: ResourceStr
```

弧形按钮显示文本。

**Type:** [ResourceStr](arkts-arkui-resourcestr-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-CommonArcButtonOptions-label?: ResourceStr--><!--Device-CommonArcButtonOptions-label?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## onClick

```TypeScript
onClick?: Callback<ClickEvent>
```

弧形按钮点击动作触发该回调。

**Type:** [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ClickEvent](../arkts-components/arkts-arkui-clickevent-i.md)&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-CommonArcButtonOptions-onClick?: Callback<ClickEvent>--><!--Device-CommonArcButtonOptions-onClick?: Callback<ClickEvent>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## onTouch

```TypeScript
onTouch?: Callback<TouchEvent>
```

弧形按钮手指触摸动作触发该回调。

**Type:** [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[TouchEvent](../arkts-components/arkts-arkui-touchevent-i.md)&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-CommonArcButtonOptions-onTouch?: Callback<TouchEvent>--><!--Device-CommonArcButtonOptions-onTouch?: Callback<TouchEvent>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## position

```TypeScript
position?: ArcButtonPosition
```

上下弧形按钮类型属性。

默认值：ArcButtonPosition.BOTTOM_EDGE

**Type:** [ArcButtonPosition](arkts-arkui-arkui-advanced-arcbutton-arcbuttonposition-e.md)

**Default:** ArcButtonPosition.BOTTOM_EDGE

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-CommonArcButtonOptions-position?: ArcButtonPosition--><!--Device-CommonArcButtonOptions-position?: ArcButtonPosition-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## pressedFontColor

```TypeScript
pressedFontColor?: ColorMetrics
```

弧形按钮按下文本颜色。

ArcButtonStyleMode需要设置为CUSTOM。

默认值：Color.White

**Type:** [ColorMetrics](arkts-arkui-colormetrics-t.md)

**Default:** Color.White

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-CommonArcButtonOptions-pressedFontColor?: ColorMetrics--><!--Device-CommonArcButtonOptions-pressedFontColor?: ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## progressConfig

```TypeScript
progressConfig?: ArcButtonProgressConfig
```

ArcButton进度条参数。不设置该属性时ArcButton组件表现为按钮样式（  
[示例1](../../../reference/apis-arkui/arkui-ts/ohos-arkui-advanced-ArcButton copy.md#示例1-设置弧形按钮)），设置后表现为进度条样式（  
[示例2](../../../reference/apis-arkui/arkui-ts/ohos-arkui-advanced-ArcButton copy.md#示例2-设置设备进度条按钮)），进度条样式不受  
[ArcButtonStyleMode](arkts-arkui-arkui-advanced-arcbutton-arcbuttonstylemode-e.md)属性设置影响。 

默认值：[ArcButtonProgressConfig](arkts-arkui-arkui-advanced-arcbutton-arcbuttonprogressconfig-c.md) 的各项子属性均取其默认值。

**Type:** [ArcButtonProgressConfig](arkts-arkui-arkui-advanced-arcbutton-arcbuttonprogressconfig-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonArcButtonOptions-progressConfig?: ArcButtonProgressConfig--><!--Device-CommonArcButtonOptions-progressConfig?: ArcButtonProgressConfig-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## shadowColor

```TypeScript
shadowColor?: ColorMetrics
```

弧形按钮阴影颜色。

默认值：Color.Black

**Type:** [ColorMetrics](arkts-arkui-colormetrics-t.md)

**Default:** Color.Black

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-CommonArcButtonOptions-shadowColor?: ColorMetrics--><!--Device-CommonArcButtonOptions-shadowColor?: ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## shadowEnabled

```TypeScript
shadowEnabled?: boolean
```

弧形按钮阴影开关。

默认值：false

值为true时，显示阴影。值为false时，不显示阴影。

**Type:** boolean

**Default:** false

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-CommonArcButtonOptions-shadowEnabled?: boolean--><!--Device-CommonArcButtonOptions-shadowEnabled?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## status

```TypeScript
status?: ArcButtonStatus
```

弧形按钮状态。

默认值：ArcButtonStatus.NORMAL

**Type:** [ArcButtonStatus](arkts-arkui-arkui-advanced-arcbutton-arcbuttonstatus-e.md)

**Default:** ArcButtonStatus.NORMAL

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-CommonArcButtonOptions-status?: ArcButtonStatus--><!--Device-CommonArcButtonOptions-status?: ArcButtonStatus-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## styleMode

```TypeScript
styleMode?: ArcButtonStyleMode
```

弧形按钮样式模式。该样式不支持与[ArcButtonProgressConfig](arkts-arkui-arkui-advanced-arcbutton-arcbuttonprogressconfig-c.md)样式同时使用。

默认值：ArcButtonStyleMode.EMPHASIZED_LIGHT

**Type:** [ArcButtonStyleMode](arkts-arkui-arkui-advanced-arcbutton-arcbuttonstylemode-e.md)

**Default:** ArcButtonStyleMode.EMPHASIZED_LIGHT

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-CommonArcButtonOptions-styleMode?: ArcButtonStyleMode--><!--Device-CommonArcButtonOptions-styleMode?: ArcButtonStyleMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

