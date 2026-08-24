# ArcSliderOptions

配置弧形Slider的信息。

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**装饰器类型：** @ObservedV2

<!--Device-unnamed-export declare class ArcSliderOptions--><!--Device-unnamed-export declare class ArcSliderOptions-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

## 导入模块

```TypeScript
```

## constructor

```TypeScript
constructor(options?: ArcSliderOptionsConstructorOptions)
```

ArcSliderOptions的构造函数。

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-ArcSliderOptions-constructor(options?: ArcSliderOptionsConstructorOptions)--><!--Device-ArcSliderOptions-constructor(options?: ArcSliderOptionsConstructorOptions)-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ArcSliderOptionsConstructorOptions](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-arcslider-arcslideroptionsconstructoroptions-i.md) | 否 | ArcSliderOptions的构造信息。 |

## digitalCrownSensitivity

```TypeScript
digitalCrownSensitivity?: CrownSensitivity
```

设置旋转表冠的灵敏度。默认值：CrownSensitivity.MEDIUM

**类型：** CrownSensitivity

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**装饰器类型：** @Trace

<!--Device-ArcSliderOptions-@Trace  digitalCrownSensitivity?: CrownSensitivity--><!--Device-ArcSliderOptions-@Trace  digitalCrownSensitivity?: CrownSensitivity-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

## layoutOptions

```TypeScript
layoutOptions?: ArcSliderLayoutOptions
```

配置弧形Slider的样式信息。默认值：[ArcSliderStyleOptions](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-arcslider-arcsliderstyleoptions-c.md)的各项子属性均取其默认值。

**类型：** [ArcSliderLayoutOptions](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-arcslider-arcsliderlayoutoptions-c.md)

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**装饰器类型：** @Trace

<!--Device-ArcSliderOptions-@Trace  layoutOptions?: ArcSliderLayoutOptions--><!--Device-ArcSliderOptions-@Trace  layoutOptions?: ArcSliderLayoutOptions-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

## onChange

```TypeScript
onChange?: ArcSliderChangeHandler
```

弧形Slider的进度值发生变化时，告知应用。默认值：不传入的情况，无回调。

**类型：** [ArcSliderChangeHandler](../../apis-arkui/arkts-apis/arkts-arkui-arcsliderchangehandler-t.md)

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**装饰器类型：** @Trace

<!--Device-ArcSliderOptions-@Trace  onChange?: ArcSliderChangeHandler--><!--Device-ArcSliderOptions-@Trace  onChange?: ArcSliderChangeHandler-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

## onEnlarge

```TypeScript
onEnlarge?: ArcSliderEnlargeHandler
```

弧形Slider放大或缩小时，告知应用。默认值：不传入的情况，无回调。

**类型：** [ArcSliderEnlargeHandler](../../apis-arkui/arkts-apis/arkts-arkui-arcsliderenlargehandler-t.md)

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**装饰器类型：** @Trace

<!--Device-ArcSliderOptions-@Trace  onEnlarge?: ArcSliderEnlargeHandler--><!--Device-ArcSliderOptions-@Trace  onEnlarge?: ArcSliderEnlargeHandler-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

## onTouch

```TypeScript
onTouch?: ArcSliderTouchHandler
```

弧形Slider被触摸时，告知应用。默认值：不传入的情况，无回调。

**类型：** [ArcSliderTouchHandler](../../apis-arkui/arkts-apis/arkts-arkui-arcslidertouchhandler-t.md)

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**装饰器类型：** @Trace

<!--Device-ArcSliderOptions-@Trace  onTouch?: ArcSliderTouchHandler--><!--Device-ArcSliderOptions-@Trace  onTouch?: ArcSliderTouchHandler-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

## styleOptions

```TypeScript
styleOptions?: ArcSliderStyleOptions
```

配置弧形Slider的样式信息。默认值：[ArcSliderStyleOptions](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-arcslider-arcsliderstyleoptions-c.md)的各项子属性均取其默认值。

**类型：** [ArcSliderStyleOptions](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-arcslider-arcsliderstyleoptions-c.md)

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**装饰器类型：** @Trace

<!--Device-ArcSliderOptions-@Trace  styleOptions?: ArcSliderStyleOptions--><!--Device-ArcSliderOptions-@Trace  styleOptions?: ArcSliderStyleOptions-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

## valueOptions

```TypeScript
valueOptions?: ArcSliderValueOptions
```

配置弧形Slider的样式信息。默认值：[ArcSliderStyleOptions](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-arcslider-arcsliderstyleoptions-c.md)的各项子属性均取其默认值。

**类型：** [ArcSliderValueOptions](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-arcslider-arcslidervalueoptions-c.md)

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**装饰器类型：** @Trace

<!--Device-ArcSliderOptions-@Trace  valueOptions?: ArcSliderValueOptions--><!--Device-ArcSliderOptions-@Trace  valueOptions?: ArcSliderValueOptions-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

