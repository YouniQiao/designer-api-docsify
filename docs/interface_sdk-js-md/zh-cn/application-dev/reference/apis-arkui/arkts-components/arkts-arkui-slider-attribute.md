# Slider属性/事件

支持除触摸热区以外的通用属性。除支持通用事件外，还支持以下事件：

**继承/实现关系：** SliderAttribute extends CommonMethod<SliderAttribute>

**起始版本：** 7

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## blockBorderColor

```TypeScript
blockBorderColor(value: ResourceColor)
```

设置滑块描边颜色。当滑块形状设置为SliderBlockType.DEFAULT时，blockBorderColor可设置默认圆形滑块描边颜色。当滑块形状设置为SliderBlockType.IMAGE时，滑块无描边，设置blockBorderColor不生效。当滑块形状设置为SliderBlockType.SHAPE时，blockBorderColor可设置自定义形状中线的颜色。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) | 是 |

## blockBorderWidth

```TypeScript
blockBorderWidth(value: Length)
```

设置滑块描边粗细。当滑块形状设置为SliderBlockType.DEFAULT时，blockBorderWidth可设置默认圆形滑块描边粗细。当滑块形状设置为SliderBlockType.IMAGE时，滑块无描边，设置blockBorderWidth不生效。当滑块形状设置为SliderBlockType.SHAPE时，blockBorderWidth可设置自定义形状中线的粗细。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Length](../arkts-apis/arkts-arkui-length-t.md) | 是 |

## blockColor

```TypeScript
blockColor(value: ResourceColor)
```

设置滑块的颜色。当滑块形状设置为SliderBlockType.DEFAULT时，blockColor可设置默认圆形滑块颜色。当滑块形状设置为SliderBlockType.IMAGE时，滑块无填充，设置blockColor不生效。当滑块形状设置为SliderBlockType.SHAPE时，blockColor可设置自定义形状的填充颜色。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) | 是 |

## blockColor

```TypeScript
blockColor(value: ResourceColor | LinearGradient)
```

设置Slider滑块的颜色，支持渐变色。与blockColor相比，新增LinearGradient类型支持。当滑块形状设置为SliderBlockType.DEFAULT时，blockColor可设置默认圆形滑块颜色。当滑块形状设置为SliderBlockType.IMAGE时，滑块无填充，设置blockColor不生效。当滑块形状设置为SliderBlockType.SHAPE时，blockColor可设置自定义形状的填充颜色。

**起始版本：** 21

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本21开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本21开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) \| [LinearGradient](arkts-arkui-lineargradient-c.md) | 是 |

## blockSize

```TypeScript
blockSize(value: SizeOptions)
```

设置滑块大小。当滑块形状设置为SliderBlockType.DEFAULT时，取宽高的最小值作为圆形半径。当滑块形状设置为SliderBlockType.IMAGE时，用于设置图片的尺寸大小，图片采用ObjectFit.Cover策略进行缩放。当滑块形状设置为SliderBlockType.SHAPE时，用于设置自定义形状的大小，自定义形状也会采用ObjectFit.Cover策略进行缩放。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [SizeOptions](../arkts-apis/arkts-arkui-sizeoptions-i.md) | 是 |

## blockStyle

```TypeScript
blockStyle(value: SliderBlockStyle)
```

设置滑块形状参数。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [SliderBlockStyle](arkts-arkui-sliderblockstyle-i.md) | 是 |

## contentModifier

```TypeScript
contentModifier(modifier: ContentModifier<SliderConfiguration>)
```

定制Slider内容区的方法。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [ContentModifier](arkts-arkui-contentmodifier-i.md)&lt;[SliderConfiguration](arkts-arkui-sliderconfiguration-i.md)&gt; | 是 |

## digitalCrownSensitivity

```TypeScript
digitalCrownSensitivity(sensitivity: Optional<CrownSensitivity>)
```

设置旋转表冠灵敏度。

> **说明：**&gt;
> 该接口不支持在attributeModifier中调用。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [sensitivity](../../apis-localization-kit/arkts-apis/arkts-localization-intl-collatoroptions-i.md) | [Optional](arkts-arkui-optional-t.md)&lt;[CrownSensitivity](../arkts-apis/arkts-arkui-crownsensitivity-e.md)&gt; | 是 |

## enableHapticFeedback

```TypeScript
enableHapticFeedback(enabled: boolean)
```

设置是否开启触控反馈。开启触控反馈时，需要在工程的[module.json5](../../../quick-start/module-configuration-file.md)中配置requestPermissions字段开启振动权限，配置如 下：

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enabled | boolean | 是 |

## maxLabel

```TypeScript
maxLabel(value: string)
```

设置最大值标签的文本内容。

> **说明：**&gt;
> 从API version 7开始支持，从API version 9开始废弃，建议使用max替代。max是[SliderOptions](arkts-arkui-slideroptions-i.md)中的属性。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** max

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | string | 是 |

## minLabel

```TypeScript
minLabel(value: string)
```

设置最小值标签的文本内容。

> **说明：**&gt;
> 从API version 7开始支持，从API version 9开始废弃，建议使用min替代。min是[SliderOptions](arkts-arkui-slideroptions-i.md)中的属性。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** min

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | string | 是 |

## minResponsiveDistance

```TypeScript
minResponsiveDistance(value: number)
```

设置滑块开始滑动的最小响应距离。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | number | 是 |

## onChange

```TypeScript
onChange(callback: (value: number, mode: SliderChangeMode) => void)
```

Slider拖动或点击时触发事件回调。Begin和End状态在点击时触发，Moving和Click状态在value值变化时触发。连贯拖动动作不触发Click状态。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | (value: number, mode: SliderChangeMode) = & gt; void | 是 |

## prefix

```TypeScript
prefix(content: ComponentContent, options?: SliderPrefixOptions)
```

设置滑动条的前缀。

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| content | [ComponentContent](../arkts-apis/arkts-arkui-componentcontent-c.md) | 是 |
| options | [SliderPrefixOptions](arkts-arkui-sliderprefixoptions-i.md) | 否 |

## selectedBorderRadius

```TypeScript
selectedBorderRadius(value: Dimension)
```

设置已滑动部分（高亮）圆角半径。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Dimension](../arkts-apis/arkts-arkui-dimension-t.md) | 是 |

## selectedColor

```TypeScript
selectedColor(value: ResourceColor)
```

设置滑轨的已滑动部分颜色。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) | 是 |

## selectedColor

```TypeScript
selectedColor(selectedColor: ResourceColor | LinearGradient)
```

设置滑轨的已滑动部分颜色。与[selectedColor](#selectedcolor)相比，新增了LinearGradient类型的支持。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本18开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [selectedColor](#selectedcolor) | [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) \| [LinearGradient](arkts-arkui-lineargradient-c.md) | 是 |

## showSteps

```TypeScript
showSteps(value: boolean)
```

设置是否显示步长刻度值。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean | 是 |

## showSteps

```TypeScript
showSteps(value: boolean, options?: SliderShowStepOptions)
```

设置当前是否显示步长刻度值。支持设置每个刻度点的无障碍文本信息，不设置时默认使用当前刻度点的值作为无障碍文本信息。当显示步长时，设置的刻度点无障碍文本信息生效。

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本20开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean | 是 |
| options | [SliderShowStepOptions](arkts-arkui-slidershowstepoptions-i.md) | 否 |

## showTips

```TypeScript
showTips(value: boolean, content?: ResourceStr)
```

设置滑动时是否显示气泡提示。当direction的值为Axis.Horizontal时，气泡提示显示在滑块上方；若上方空间不足以显示完整气泡提示，则在下方显示。当值为Axis.Vertical时，气泡提示显示在滑块左边；若左边空间不足以显示完整气泡提示，则在右边显示。当未设置周边边距或边距小于气泡提示所需空间时，气泡提示会被截断。气泡提示的绘制区域为Slider自身节点的overlay。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean | 是 |
| content | [ResourceStr](../arkts-apis/arkts-arkui-resourcestr-t.md) | 否 |

## slideRange

```TypeScript
slideRange(value: SlideRange)
```

设置有效滑动区间。设置后滑块滑动范围被限制在[from, to]区间内，区间外的点击和手势不会触发滑动；value初始值若超出区间会自动调整到区间边界。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [SlideRange](arkts-arkui-sliderange-i.md) | 是 |

## sliderInteractionMode

```TypeScript
sliderInteractionMode(value: SliderInteraction)
```

设置用户与滑动条组件交互方式。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [SliderInteraction](arkts-arkui-sliderinteraction-e.md) | 是 |

## stepColor

```TypeScript
stepColor(value: ResourceColor)
```

设置刻度颜色。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) | 是 |

## stepSize

```TypeScript
stepSize(value: Length)
```

设置刻度大小（直径）。当值为0时，刻度点不显示，当值小于0时，取默认值。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Length](../arkts-apis/arkts-arkui-length-t.md) | 是 |

## suffix

```TypeScript
suffix(content: ComponentContent, options?: SliderSuffixOptions)
```

设置滑动条的后缀。

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| content | [ComponentContent](../arkts-apis/arkts-arkui-componentcontent-c.md) | 是 |
| options | [SliderSuffixOptions](arkts-arkui-slidersuffixoptions-i.md) | 否 |

## trackBorderRadius

```TypeScript
trackBorderRadius(value: Length)
```

设置底板圆角半径。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Length](../arkts-apis/arkts-arkui-length-t.md) | 是 |

## trackColor

```TypeScript
trackColor(value: ResourceColor | LinearGradient)
```

设置滑轨的背景颜色。从API version 12开始，支持使用LinearGradient类型设置滑轨的渐变色。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) \| [LinearGradient](arkts-arkui-lineargradient-c.md) | 是 |

## trackColorMetrics

```TypeScript
trackColorMetrics(color: ColorMetricsLinearGradient)
```

设置滑轨轨道的线性渐变背景颜色。与trackColorMetrics相比，使用ColorMetricsLinearGradient类型支持指定色域的渐变。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| color | [ColorMetricsLinearGradient](arkts-arkui-colormetricslineargradient-c.md) | 是 |

## trackThickness

```TypeScript
trackThickness(value: Length)
```

设置滑轨的粗细。设置小于等于0的值时，取默认值。为保证滑块和滑轨的[SliderStyle](arkts-arkui-sliderstyle-e.md)样式，[blockSize](#blocksize)跟随trackThickness同比例增减。当style为[SliderStyle](arkts-arkui-sliderstyle-e.md).OutSet时，trackThickness ：[blockSize](#blocksize) = 1 ： 4，当style为[SliderStyle](arkts-arkui-sliderstyle-e.md).InSet时，trackThickness ：[blockSize](#blocksize) = 5 ： 3。trackThickness或[blockSize](#blocksize)的大小超过Slider组件的宽度或高度时，取默认值。当[SliderStyle](arkts-arkui-sliderstyle-e.md)设置为OutSet时，尽管trackThickness的大小没超过Slider组件的宽度或高度，但是 [blockSize](#blocksize)超过了，取默认值。

**起始版本：** 8

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Length](../arkts-apis/arkts-arkui-length-t.md) | 是 |
