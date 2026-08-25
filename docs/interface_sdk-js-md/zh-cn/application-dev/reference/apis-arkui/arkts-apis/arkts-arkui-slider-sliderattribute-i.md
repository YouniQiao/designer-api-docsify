# SliderAttribute

支持除触摸热区以外的通用属性。

**继承/实现关系：** SliderAttribute extends CommonMethod

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<SliderAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

设置当前组件的属性修改器。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[SliderAttribute](arkts-arkui-slider-sliderattribute-i.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SliderAttribute](arkts-arkui-slider-sliderattribute-i.md) |

## blockBorderColor

```TypeScript
default blockBorderColor(value: ResourceColor | undefined): this
```

设置滑块描边颜色。当滑块形状设置为SliderBlockType.DEFAULT时，blockBorderColor可设置默认圆形滑块描边颜色。当滑块形状设置为SliderBlockType.IMAGE时，滑块无描边，设置blockBorderColor不生效。当滑块形状设置为SliderBlockType.SHAPE时，blockBorderColor可设置自定义形状中线的颜色。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SliderAttribute](arkts-arkui-slider-sliderattribute-i.md) |

## blockBorderWidth

```TypeScript
default blockBorderWidth(value: Length | undefined): this
```

设置滑块描边粗细。当滑块形状设置为SliderBlockType.DEFAULT时，blockBorderWidth可设置默认圆形滑块描边粗细。当滑块形状设置为SliderBlockType.IMAGE时，滑块无描边，设置blockBorderWidth不生效。当滑块形状设置为SliderBlockType.SHAPE时，blockBorderWidth可设置自定义形状中线的粗细。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Length](arkts-arkui-length-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SliderAttribute](arkts-arkui-slider-sliderattribute-i.md) |

## blockColor

```TypeScript
default blockColor(value: ResourceColor | LinearGradient | undefined): this
```

设置滑块的颜色。当滑块形状设置为SliderBlockType.DEFAULT时，blockColor可设置默认圆形滑块颜色。当滑块形状设置为SliderBlockType.IMAGE时，滑块无填充，设置blockColor不生效。当滑块形状设置为SliderBlockType.SHAPE时，blockColor可设置自定义形状的填充颜色。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| [LinearGradient](arkts-arkui-datapanel-lineargradient-c.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SliderAttribute](arkts-arkui-slider-sliderattribute-i.md) |

## blockSize

```TypeScript
default blockSize(value: SizeOptions | undefined): this
```

设置滑块大小。当滑块形状设置为SliderBlockType.DEFAULT时，取宽高的最小值作为圆形半径。当滑块形状设置为SliderBlockType.IMAGE时，用于设置图片的尺寸大小，图片采用ObjectFit.Cover策略进行缩放。当滑块形状设置为SliderBlockType.SHAPE时，用于设置自定义形状的大小，自定义形状也会采用ObjectFit.Cover策略进行缩放。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [SizeOptions](arkts-arkui-sizeoptions-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SliderAttribute](arkts-arkui-slider-sliderattribute-i.md) |

## blockStyle

```TypeScript
default blockStyle(value: SliderBlockStyle | undefined): this
```

设置滑块形状参数。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [SliderBlockStyle](arkts-arkui-slider-sliderblockstyle-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SliderAttribute](arkts-arkui-slider-sliderattribute-i.md) |

## contentModifier

```TypeScript
default contentModifier(modifier: ContentModifier<SliderConfiguration> | undefined): this
```

定制Slider内容区的方法。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [ContentModifier](../arkts-components/arkts-arkui-contentmodifier-i.md)&lt;[SliderConfiguration](arkts-arkui-slider-sliderconfiguration-i.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SliderAttribute](arkts-arkui-slider-sliderattribute-i.md) |

## digitalCrownSensitivity

```TypeScript
default digitalCrownSensitivity(sensitivity: CrownSensitivity | undefined): this
```

设置旋转表冠的灵敏度。

> **说明：**&gt;
> 该接口不支持在attributeModifier中调用。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sensitivity | [CrownSensitivity](arkts-arkui-crownsensitivity-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SliderAttribute](arkts-arkui-slider-sliderattribute-i.md) |

## enableHapticFeedback

```TypeScript
default enableHapticFeedback(enabled: boolean | undefined): this
```

设置是否开启触控反馈。开启触控反馈时，需要在工程的[module.json5](../../../quick-start/module-configuration-file.md)中配置requestPermissions字段开启振动权限，配置如 下：

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enabled | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SliderAttribute](arkts-arkui-slider-sliderattribute-i.md) |

## minResponsiveDistance

```TypeScript
default minResponsiveDistance(value: double | undefined): this
```

设置滑动响应的最小距离。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | double \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SliderAttribute](arkts-arkui-slider-sliderattribute-i.md) |

## onChange

```TypeScript
default onChange(callback: ((value: double, mode: SliderChangeMode) => void) | undefined): this
```

Slider拖动或点击时触发事件回调。Begin和End状态当手势点击时都会触发，Moving和Click状态当value值发生变化时触发。当连贯动作为拖动动作时，不触发Click状态。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | ((value: double, mode: SliderChangeMode) = & gt; void) \ | undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SliderAttribute](arkts-arkui-slider-sliderattribute-i.md) |

## prefix

```TypeScript
default prefix<T extends Object>(content: ComponentContent<T> | undefined, options?: SliderPrefixOptions | undefined): this
```

设置滑动条的前缀。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| content | [ComponentContent](arkts-arkui-componentcontent-c.md)&lt;T&gt; \| undefined | 是 |
| options | [SliderPrefixOptions](arkts-arkui-slider-sliderprefixoptions-i.md) \| undefined | 否 |

**返回值：**

| 类型 |
| --- |
| [SliderAttribute](arkts-arkui-slider-sliderattribute-i.md) |

## selectedBorderRadius

```TypeScript
default selectedBorderRadius(value: Dimension | undefined): this
```

设置已滑动部分（高亮）圆角半径。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Dimension](arkts-arkui-dimension-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SliderAttribute](arkts-arkui-slider-sliderattribute-i.md) |

## selectedColor

```TypeScript
default selectedColor(selectedColor: ResourceColor | LinearGradient | undefined): this
```

设置滑轨的已滑动部分颜色。与[selectedColor](#selectedcolor)相比，新增了LinearGradient类型的支持。从API version 18开始支持利用LinearGradient设置滑轨的已滑动部分的渐变色。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [selectedColor](#selectedcolor) | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| [LinearGradient](arkts-arkui-datapanel-lineargradient-c.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SliderAttribute](arkts-arkui-slider-sliderattribute-i.md) |

## showSteps

```TypeScript
default showSteps(value: boolean | undefined): this
```

设置当前是否显示步长刻度值。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SliderAttribute](arkts-arkui-slider-sliderattribute-i.md) |

## showSteps

```TypeScript
default showSteps(value: boolean | undefined, options?: SliderShowStepOptions | undefined): this
```

设置当前是否显示步长刻度值。支持设置每个刻度点的无障碍文本信息，不设置时默认使用当前刻度点的值作为无障碍文本信息。当显示步长时，设置的刻度点无障碍文本信息生效。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean \| undefined | 是 |
| options | [SliderShowStepOptions](arkts-arkui-slider-slidershowstepoptions-i.md) \| undefined | 否 |

**返回值：**

| 类型 |
| --- |
## showTips

```TypeScript
default showTips(value: boolean | undefined, content?: ResourceStr | undefined): this
```

设置滑动时是否显示气泡提示。当direction的值为Axis.Horizontal时，tip显示在滑块上方，如果上方空间不够，则在下方显示。当值为Axis.Vertical时，tip显示在滑块左边，如果左边空间不够，则在右边显示。当不设置周边边距或者周 边边距比较小时，tip会被截断。tip的绘制区域为Slider自身节点的overlay。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean \| undefined | 是 |
| content | [ResourceStr](arkts-arkui-resourcestr-t.md) \| undefined | 否 |

**返回值：**

| 类型 |
| --- |
| [SliderAttribute](arkts-arkui-slider-sliderattribute-i.md) |

## slideRange

```TypeScript
default slideRange(value: SlideRange | undefined): this
```

设置有效滑动区间。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [SlideRange](arkts-arkui-slider-sliderange-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SliderAttribute](arkts-arkui-slider-sliderattribute-i.md) |

## sliderInteractionMode

```TypeScript
default sliderInteractionMode(value: SliderInteraction | undefined): this
```

设置用户与滑动条组件交互方式。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [SliderInteraction](arkts-arkui-slider-sliderinteraction-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SliderAttribute](arkts-arkui-slider-sliderattribute-i.md) |

## stepColor

```TypeScript
default stepColor(value: ResourceColor | undefined): this
```

设置刻度颜色。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SliderAttribute](arkts-arkui-slider-sliderattribute-i.md) |

## stepSize

```TypeScript
default stepSize(value: Length | undefined): this
```

设置刻度大小（直径）。当值为0时，刻度点不显示，当值小于0时，取默认值。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Length](arkts-arkui-length-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SliderAttribute](arkts-arkui-slider-sliderattribute-i.md) |

## suffix

```TypeScript
default suffix<T extends Object>(content: ComponentContent<T> | undefined, options?: SliderSuffixOptions | undefined): this
```

设置滑动条的后缀。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| content | [ComponentContent](arkts-arkui-componentcontent-c.md)&lt;T&gt; \| undefined | 是 |
| options | [SliderSuffixOptions](arkts-arkui-slider-slidersuffixoptions-i.md) \| undefined | 否 |

**返回值：**

| 类型 |
| --- |
| [SliderAttribute](arkts-arkui-slider-sliderattribute-i.md) |

## trackBorderRadius

```TypeScript
default trackBorderRadius(value: Length | undefined): this
```

设置底板圆角半径。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Length](arkts-arkui-length-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SliderAttribute](arkts-arkui-slider-sliderattribute-i.md) |

## trackColor

```TypeScript
default trackColor(value: ResourceColor | LinearGradient | undefined): this
```

设置滑轨的背景颜色。从API version 12开始支持利用LinearGradient设置滑轨的渐变色。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| [LinearGradient](arkts-arkui-datapanel-lineargradient-c.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SliderAttribute](arkts-arkui-slider-sliderattribute-i.md) |

## trackColorMetrics

```TypeScript
default trackColorMetrics(color: ColorMetricsLinearGradient | undefined): this
```

设置滑轨轨道的线性渐变背景颜色。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| color | [ColorMetricsLinearGradient](arkts-arkui-slider-colormetricslineargradient-c.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SliderAttribute](arkts-arkui-slider-sliderattribute-i.md) |

## trackThickness

```TypeScript
default trackThickness(value: Length | undefined): this
```

设置滑轨的粗细。设置小于等于0的值时，取默认值。为保证滑块和滑轨的[SliderStyle](arkts-arkui-slider-sliderstyle-e.md)样式，[blockSize](#blocksize)跟随trackThickness同比例增减。当style为[SliderStyle](arkts-arkui-slider-sliderstyle-e.md).OutSet时，trackThickness ：[blockSize](#blocksize) = 1 ：4，当style为 [SliderStyle](arkts-arkui-slider-sliderstyle-e.md).InSet时，trackThickness ：[blockSize](#blocksize) = 5 ：3。trackThickness或[blockSize](#blocksize)的大小超过Slider组件的宽度或高度时，取默认值。当[SliderStyle](arkts-arkui-slider-sliderstyle-e.md)设置为OutSet时，尽管trackThickness的大小没超过Slider组件的宽度或高度，但是[blockSize](#blocksize)超过 了，取默认值。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Length](arkts-arkui-length-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SliderAttribute](arkts-arkui-slider-sliderattribute-i.md) |
