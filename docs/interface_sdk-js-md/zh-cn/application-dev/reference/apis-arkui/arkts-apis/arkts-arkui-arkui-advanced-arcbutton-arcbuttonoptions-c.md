# ArcButtonOptions

定义ArcButton的默认样式或自定义样式参数。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**装饰器类型：** @ObservedV2

<!--Device-unnamed-export declare class ArcButtonOptions--><!--Device-unnamed-export declare class ArcButtonOptions-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

## 导入模块

```TypeScript
import { ArcButtonPosition, ArcButton, ArcButtonStatus, ArcButtonStyleMode, ArcButtonOptions, ArcButtonProgressConfig } from 'kits/@kit.ArkUI';
```

## constructor

```TypeScript
constructor(options: CommonArcButtonOptions)
```

弧形按钮的构造函数。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-ArcButtonOptions-constructor(options: CommonArcButtonOptions)--><!--Device-ArcButtonOptions-constructor(options: CommonArcButtonOptions)-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [CommonArcButtonOptions](arkts-arkui-arkui-advanced-arcbutton-commonarcbuttonoptions-i.md) | 是 | 定义ArcButton组件的文本、背景色、阴影等参数。 |

## backgroundBlurStyle

```TypeScript
public backgroundBlurStyle: BlurStyle
```

弧形按钮背景模糊能力。&lt;br/&gt;默认值：BlurStyle.NONE

**类型：** [BlurStyle](../arkts-components/arkts-arkui-blurstyle-e.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-ArcButtonOptions-public backgroundBlurStyle: BlurStyle--><!--Device-ArcButtonOptions-public backgroundBlurStyle: BlurStyle-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

## backgroundColor

```TypeScript
public backgroundColor: ColorMetrics
```

弧形按钮背景颜色。&lt;br/&gt;ArcButtonStyleMode需要设置为CUSTOM。&lt;br/&gt;默认值：Color.Black

**类型：** [ColorMetrics](arkts-arkui-colormetrics-t.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-ArcButtonOptions-public backgroundColor: ColorMetrics--><!--Device-ArcButtonOptions-public backgroundColor: ColorMetrics-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

## fontColor

```TypeScript
public fontColor: ColorMetrics
```

弧形按钮文本颜色。&lt;br/&gt;ArcButtonStyleMode需要设置为CUSTOM。&lt;br/&gt;默认值：Color.White

**类型：** [ColorMetrics](arkts-arkui-colormetrics-t.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-ArcButtonOptions-public fontColor: ColorMetrics--><!--Device-ArcButtonOptions-public fontColor: ColorMetrics-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

## fontFamily

```TypeScript
public fontFamily: string | Resource
```

弧形按钮字体名。

**类型：** string \| Resource

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-ArcButtonOptions-public fontFamily: string | Resource--><!--Device-ArcButtonOptions-public fontFamily: string | Resource-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

## fontMargin

```TypeScript
public fontMargin: LocalizedMargin
```

弧形按钮文本边距。&lt;br/&gt;默认值：{start:24vp, top: 10vp,end: 24vp, bottom:16vp }

**类型：** [LocalizedMargin](arkts-arkui-localizedmargin-t.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-ArcButtonOptions-public fontMargin: LocalizedMargin--><!--Device-ArcButtonOptions-public fontMargin: LocalizedMargin-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

## fontSize

```TypeScript
public fontSize: LengthMetrics
```

弧形按钮文本大小。&lt;br/&gt;默认值：19fp

**类型：** [LengthMetrics](arkts-arkui-lengthmetrics-t.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-ArcButtonOptions-public fontSize: LengthMetrics--><!--Device-ArcButtonOptions-public fontSize: LengthMetrics-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

## fontStyle

```TypeScript
public fontStyle: FontStyle
```

弧形按钮文本样式。&lt;br/&gt;默认值：FontStyle.Normal

**类型：** [FontStyle](arkts-arkui-fontstyle-e.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-ArcButtonOptions-public fontStyle: FontStyle--><!--Device-ArcButtonOptions-public fontStyle: FontStyle-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

## label

```TypeScript
public label: ResourceStr
```

弧形按钮显示文本。

**类型：** [ResourceStr](arkts-arkui-resourcestr-t.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-ArcButtonOptions-public label: ResourceStr--><!--Device-ArcButtonOptions-public label: ResourceStr-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

## onClick

```TypeScript
public onClick?: Callback<ClickEvent>
```

弧形按钮点击动作触发该回调。

**类型：** [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ClickEvent](../arkts-components/arkts-arkui-clickevent-i.md)&gt;

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-ArcButtonOptions-public onClick?: Callback<ClickEvent>--><!--Device-ArcButtonOptions-public onClick?: Callback<ClickEvent>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

## onTouch

```TypeScript
public onTouch?: Callback<TouchEvent>
```

弧形按钮手指触摸动作触发该回调。

**类型：** [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[TouchEvent](../arkts-components/arkts-arkui-touchevent-i.md)&gt;

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-ArcButtonOptions-public onTouch?: Callback<TouchEvent>--><!--Device-ArcButtonOptions-public onTouch?: Callback<TouchEvent>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

## position

```TypeScript
public position: ArcButtonPosition
```

上下弧形按钮类型属性。&lt;br/&gt;默认值：ArcButtonPosition.BOTTOM_EDGE。

**类型：** [ArcButtonPosition](arkts-arkui-arkui-advanced-arcbutton-arcbuttonposition-e.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-ArcButtonOptions-public position: ArcButtonPosition--><!--Device-ArcButtonOptions-public position: ArcButtonPosition-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

## pressedFontColor

```TypeScript
public pressedFontColor: ColorMetrics
```

弧形按钮按下文本颜色。&lt;br/&gt;ArcButtonStyleMode需要设置为CUSTOM。&lt;br/&gt;默认值：Color.White

**类型：** [ColorMetrics](arkts-arkui-colormetrics-t.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-ArcButtonOptions-public pressedFontColor: ColorMetrics--><!--Device-ArcButtonOptions-public pressedFontColor: ColorMetrics-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

## progressConfig

```TypeScript
public progressConfig?: ArcButtonProgressConfig
```

ArcButton进度条参数。不设置该属性时ArcButton组件表现为按钮样式（  
[示例1](../../../reference/apis-arkui/arkui-ts/ohos-arkui-advanced-ArcButton copy.md#示例1-设置弧形按钮)），设置后表现为进度条样式（  
[示例2](../../../reference/apis-arkui/arkui-ts/ohos-arkui-advanced-ArcButton copy.md#示例2-设置设备进度条按钮)），进度条样式不受  
[ArcButtonStyleMode](arkts-arkui-arkui-advanced-arcbutton-arcbuttonstylemode-e.md)属性设置影响。 

默认值：[ArcButtonProgressConfig](arkts-arkui-arkui-advanced-arcbutton-arcbuttonprogressconfig-c.md) 的各项子属性均取其默认值。

**类型：** [ArcButtonProgressConfig](arkts-arkui-arkui-advanced-arcbutton-arcbuttonprogressconfig-c.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArcButtonOptions-public progressConfig?: ArcButtonProgressConfig--><!--Device-ArcButtonOptions-public progressConfig?: ArcButtonProgressConfig-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

## shadowColor

```TypeScript
public shadowColor: ColorMetrics
```

弧形按钮阴影颜色。&lt;br/&gt;默认值：Color.Black

**类型：** [ColorMetrics](arkts-arkui-colormetrics-t.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-ArcButtonOptions-public shadowColor: ColorMetrics--><!--Device-ArcButtonOptions-public shadowColor: ColorMetrics-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

## shadowEnabled

```TypeScript
public shadowEnabled: boolean
```

弧形按钮阴影开关。&lt;br/&gt;默认值：false&lt;br/&gt;值为true时，显示阴影。值为false时，不显示阴影。

**类型：** boolean

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-ArcButtonOptions-public shadowEnabled: boolean--><!--Device-ArcButtonOptions-public shadowEnabled: boolean-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

## status

```TypeScript
public status: ArcButtonStatus
```

弧形按钮状态。&lt;br/&gt;默认值：ArcButtonStatus.NORMAL

**类型：** [ArcButtonStatus](arkts-arkui-arkui-advanced-arcbutton-arcbuttonstatus-e.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-ArcButtonOptions-public status: ArcButtonStatus--><!--Device-ArcButtonOptions-public status: ArcButtonStatus-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

## styleMode

```TypeScript
public styleMode: ArcButtonStyleMode
```

弧形按钮样式模式。该样式不支持与[ArcButtonProgressConfig](#arcbuttonprogressconfig23)样式同时使用。&lt;br&gt;默认值：ArcButtonStyleMode.EMPHASIZED_LIGHT

**类型：** [ArcButtonStyleMode](arkts-arkui-arkui-advanced-arcbutton-arcbuttonstylemode-e.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-ArcButtonOptions-public styleMode: ArcButtonStyleMode--><!--Device-ArcButtonOptions-public styleMode: ArcButtonStyleMode-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

