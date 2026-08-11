# SliderAttribute

支持除触摸热区以外的[通用属性](../../apis-ability-kit/arkts-apis/arkts-app-ability-common.md/arkts-app-ability-common.md)。

**继承/实现关系：** SliderAttribute extends [CommonMethod](arkts-arkui-common-commonmethod-i.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-unnamed-export declare interface SliderAttribute extends CommonMethod--><!--Device-unnamed-export declare interface SliderAttribute extends CommonMethod-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<SliderAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

设置当前组件的属性修改器。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SliderAttribute-default attributeModifier(modifier: AttributeModifier<SliderAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-SliderAttribute-default attributeModifier(modifier: AttributeModifier<SliderAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;SliderAttribute&gt; \| AttributeModifier&lt;CommonMethod&gt; \| undefined | 是 | 在Slider组件的 属性修改器。&lt;br/&gt;当modifier的值为undefined时，不使用属性修改器。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## blockBorderColor

```TypeScript
default blockBorderColor(value: ResourceColor | undefined): this
```

设置滑块描边颜色。

当滑块形状设置为SliderBlockType.DEFAULT时，blockBorderColor可设置默认圆形滑块描边颜色。

当滑块形状设置为SliderBlockType.IMAGE时，滑块无描边，设置blockBorderColor不生效。

当滑块形状设置为SliderBlockType.SHAPE时，blockBorderColor可设置自定义形状中线的颜色。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SliderAttribute-default blockBorderColor(value: ResourceColor | undefined): this--><!--Device-SliderAttribute-default blockBorderColor(value: ResourceColor | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | 是 | 滑块描边颜色。取值为undefined时，按默认值处理。&lt;br/&gt;默认值：'#00000000' |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## blockBorderWidth

```TypeScript
default blockBorderWidth(value: Length | undefined): this
```

设置滑块描边粗细。

当滑块形状设置为SliderBlockType.DEFAULT时，blockBorderWidth可设置默认圆形滑块描边粗细。

当滑块形状设置为SliderBlockType.IMAGE时，滑块无描边，设置blockBorderWidth不生效。

当滑块形状设置为SliderBlockType.SHAPE时，blockBorderWidth可设置自定义形状中线的粗细。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SliderAttribute-default blockBorderWidth(value: Length | undefined): this--><!--Device-SliderAttribute-default blockBorderWidth(value: Length | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Length](arkts-arkui-length-t.md) \| undefined | 是 | 滑块描边粗细。取值为undefined时，按0值处理。&lt;br/&gt;**说明：** &lt;br/&gt;设置string类型时，不支持百分比。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## blockColor

```TypeScript
default blockColor(value: ResourceColor | LinearGradient | undefined): this
```

设置滑块的颜色。

当滑块形状设置为SliderBlockType.DEFAULT时，blockColor可设置默认圆形滑块颜色。

当滑块形状设置为SliderBlockType.IMAGE时，滑块无填充，设置blockColor不生效。

当滑块形状设置为SliderBlockType.SHAPE时，blockColor可设置自定义形状的填充颜色。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SliderAttribute-default blockColor(value: ResourceColor | LinearGradient | undefined): this--><!--Device-SliderAttribute-default blockColor(value: ResourceColor | LinearGradient | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| LinearGradient \| undefined | 是 | 滑块的颜色。 取值为undefined时，按默认值处理。&lt;br/&gt;默认值： `\\$r('sys.color.ohos_id_color_foreground_contrary')` |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## blockSize

```TypeScript
default blockSize(value: SizeOptions | undefined): this
```

设置滑块大小。

当滑块形状设置为SliderBlockType.DEFAULT时，取宽高的最小值作为圆形半径。

当滑块形状设置为SliderBlockType.IMAGE时，用于设置图片的尺寸大小，图片采用ObjectFit.Cover策略进行缩放。

当滑块形状设置为SliderBlockType.SHAPE时，用于设置自定义形状的大小，自定义形状也会采用ObjectFit.Cover策略进行缩放。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SliderAttribute-default blockSize(value: SizeOptions | undefined): this--><!--Device-SliderAttribute-default blockSize(value: SizeOptions | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [SizeOptions](arkts-arkui-sizeoptions-i.md) \| undefined | 是 | 滑块大小。取值为undefined时，按默认值处理。&lt;br/&gt;默认值：当参数style的值设置为 [SliderStyle](../arkts-components/arkts-arkui-sliderstyle-e.md/arkts-arkui-sliderstyle-e.md).OutSet时为{width: 18, height: 18}，当参数style的值设置为 [SliderStyle](../arkts-components/arkts-arkui-sliderstyle-e.md/arkts-arkui-sliderstyle-e.md).InSet时为{width: 12, height: 12}，当参数style的值设置为 [SliderStyle](../arkts-components/arkts-arkui-sliderstyle-e.md/arkts-arkui-sliderstyle-e.md).NONE时，此字段不生效。&lt;br/&gt;当设置的blockSize的宽高值不相等时，取较小值的尺寸，当设置的宽高值中有一个或两个都小于等于0的时候，取默认 值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## blockStyle

```TypeScript
default blockStyle(value: SliderBlockStyle | undefined): this
```

设置滑块形状参数。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SliderAttribute-default blockStyle(value: SliderBlockStyle | undefined): this--><!--Device-SliderAttribute-default blockStyle(value: SliderBlockStyle | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [SliderBlockStyle](../arkts-components/arkts-arkui-sliderblockstyle-i.md) \| undefined | 是 | 滑块形状参数。取值为undefined时，按默认值处理。&lt;br/&gt;默认值：SliderBlockType.DEFAULT，滑块形状 为圆形。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## contentModifier

```TypeScript
default contentModifier(modifier: ContentModifier<SliderConfiguration> | undefined): this
```

定制Slider内容区的方法。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SliderAttribute-default contentModifier(modifier: ContentModifier<SliderConfiguration> | undefined): this--><!--Device-SliderAttribute-default contentModifier(modifier: ContentModifier<SliderConfiguration> | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | [ContentModifier](../arkts-components/arkts-arkui-contentmodifier-i.md)&lt;SliderConfiguration&gt; \| undefined | 是 | 在Slider组件上，定制内容区的方法。&lt;br/&gt;ContentModifier：内 容修改器，开发者需要自定义class实现ContentModifier接口。取值为undefined时，则不使用内容修改器。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## digitalCrownSensitivity

```TypeScript
default digitalCrownSensitivity(sensitivity: CrownSensitivity | undefined): this
```

设置旋转表冠的灵敏度。

> **说明：**
> 
> 该接口不支持在[attributeModifier](../arkts-components/arkts-arkui-commonmethod-c.md/arkts-arkui-commonmethod-c.md#attributemodifier)中调用。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SliderAttribute-default digitalCrownSensitivity(sensitivity: CrownSensitivity | undefined): this--><!--Device-SliderAttribute-default digitalCrownSensitivity(sensitivity: CrownSensitivity | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sensitivity | [CrownSensitivity](arkts-arkui-crownsensitivity-e.md) \| undefined | 是 | 旋转表冠的灵敏度。取值为undefined时，按默认值处理。&lt;br /&gt;默认值： CrownSensitivity.MEDIUM |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## enableHapticFeedback

```TypeScript
default enableHapticFeedback(enabled: boolean | undefined): this
```

设置是否开启触控反馈。

开启触控反馈时，需要在工程的[module.json5](../../../quick-start/module-configuration-file.md)中配置requestPermissions字段开启振动权限，配置如下：

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SliderAttribute-default enableHapticFeedback(enabled: boolean | undefined): this--><!--Device-SliderAttribute-default enableHapticFeedback(enabled: boolean | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean \| undefined | 是 | 设置是否开启触控反馈。取值为undefined时，按默认值处理。&lt;br/&gt;true：开启触控反馈；false：不开启触控反馈。&lt;br/&gt;默认值： true |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## minResponsiveDistance

```TypeScript
default minResponsiveDistance(value: double | undefined): this
```

设置滑动响应的最小距离。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SliderAttribute-default minResponsiveDistance(value: double | undefined): this--><!--Device-SliderAttribute-default minResponsiveDistance(value: double | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | double \| undefined | 是 | 设置滑动响应的最小距离，滑动超过此距离后滑块才开始滑动。取值为undefined时，按默认值处理。&lt;br/&gt;默认值：0&lt;br/&gt;**说明：** &lt;br /&gt;单位与[SliderOptions](../arkts-components/arkts-arkui-slideroptions-i.md/arkts-arkui-slideroptions-i.md)中的属性min以及属性max一致。&lt;br/&gt;当value小于0、大于max-min或非法值时，取默认值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## onChange

```TypeScript
default onChange(callback: ((value: double, mode: SliderChangeMode) => void) | undefined): this
```

Slider拖动或点击时触发事件回调。

Begin和End状态当手势点击时都会触发，Moving和Click状态当value值发生变化时触发。

当连贯动作为拖动动作时，不触发Click状态。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SliderAttribute-default onChange(callback: ((value: double, mode: SliderChangeMode) => void) | undefined): this--><!--Device-SliderAttribute-default onChange(callback: ((value: double, mode: SliderChangeMode) => void) | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | ((value: double, mode: SliderChangeMode) =&gt; void) \| undefined | 是 | Slider拖动或点击时触发事件回调。&lt;br/&gt;- **value**：当前滑动进度值，变化范围为对应步长steps数组。若返回值有小数，可使用number.toFixed()方法将数据处理为预期的精度。&lt;br/&gt;- **mode**：事件触发的相关状态值。&lt;br/&gt; ArkTS-Sta：当callback的值为undefined时，不使用回调函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## prefix

```TypeScript
default prefix<T extends Object>(content: ComponentContent<T> | undefined, options?: SliderPrefixOptions | undefined): this
```

设置滑动条的前缀。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SliderAttribute-default prefix<T extends Object>(content: ComponentContent<T> | undefined, options?: SliderPrefixOptions | undefined): this--><!--Device-SliderAttribute-default prefix<T extends Object>(content: ComponentContent<T> | undefined, options?: SliderPrefixOptions | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| content | [ComponentContent](arkts-arkui-componentcontent-c.md)&lt;T&gt; \| undefined | 是 | 自定义组件内容，用于定义滑块前缀的可视化内容，该内容会显示在滑块的起始位置。取值为undefined时，则不使用前缀。 |
| options | [SliderPrefixOptions](../arkts-components/arkts-arkui-sliderprefixoptions-i.md) \| undefined | 否 | 滑块前缀的配置选项，用于设置与无障碍功能相关的属性。取值为undefined时，则不使用前缀。 &lt;br/&gt;默认值： null |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## selectedBorderRadius

```TypeScript
default selectedBorderRadius(value: Dimension | undefined): this
```

设置已滑动部分（高亮）圆角半径。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SliderAttribute-default selectedBorderRadius(value: Dimension | undefined): this--><!--Device-SliderAttribute-default selectedBorderRadius(value: Dimension | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Dimension](arkts-arkui-dimension-t.md) \| undefined | 是 | 已选择部分的圆角半径。取值为undefined时，按默认值处理。&lt;br/&gt;默认值：当style值为SliderStyle.InSet或 SliderStyle.OutSet时，跟随底板圆角；当style值为SliderStyle.NONE时，为0。&lt;br/&gt;**说明：** &lt;br/&gt;不支持Percentage类型。设定值小于0时取默认值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## selectedColor

```TypeScript
default selectedColor(selectedColor: ResourceColor | LinearGradient | undefined): this
```

设置滑轨的已滑动部分颜色。与[selectedColor](arkts-arkui-slider-sliderattribute-i.md#selectedcolor)相比，新增了LinearGradient类型的支持。

从API version 18开始支持利用LinearGradient设置滑轨的已滑动部分的渐变色。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SliderAttribute-default selectedColor(selectedColor: ResourceColor | LinearGradient | undefined): this--><!--Device-SliderAttribute-default selectedColor(selectedColor: ResourceColor | LinearGradient | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| selectedColor | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| LinearGradient \| undefined | 是 | 滑轨的已滑动部分颜色。 取值为undefined时，按默认值处理。&lt;br/&gt; **说明：** &lt;br/&gt;设置渐变色时，若颜色断点颜色值为非法值或者渐变色断点为空时，渐变色不起效果。 &lt;br/&gt;默认值：`\\$r('sys.color.ohos_id_color_emphasize')` |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## showSteps

```TypeScript
default showSteps(value: boolean | undefined): this
```

设置当前是否显示步长刻度值。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SliderAttribute-default showSteps(value: boolean | undefined): this--><!--Device-SliderAttribute-default showSteps(value: boolean | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean \| undefined | 是 | 当前是否显示步长刻度值。取值为undefined时，按默认值处理。&lt;br/&gt;true：显示刻度值；false：不显示刻度值。&lt;br/&gt;默认值： false |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## showSteps

```TypeScript
default showSteps(value: boolean | undefined, options?: SliderShowStepOptions | undefined): this
```

设置当前是否显示步长刻度值。

支持设置每个刻度点的无障碍文本信息，不设置时默认使用当前刻度点的值作为无障碍文本信息。

当显示步长时，设置的刻度点无障碍文本信息生效。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SliderAttribute-default showSteps(value: boolean | undefined, options?: SliderShowStepOptions | undefined): this--><!--Device-SliderAttribute-default showSteps(value: boolean | undefined, options?: SliderShowStepOptions | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean \| undefined | 是 | 当前是否显示步长刻度值。取值为undefined时，按默认值处理。&lt;br/&gt;true：显示刻度值；false：不显示刻度值。&lt;br /&gt;默认值： false |
| options | [SliderShowStepOptions](arkts-arkui-slider-slidershowstepoptions-i.md) \| undefined | 否 | 刻度点无障碍文本的配置选项，用于设置与无障碍功能相关的属性。取值为undefined时，默认使用当前刻度点的值作 为无障碍文本信息。&lt;br/&gt;默认值：null |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## showTips

```TypeScript
default showTips(value: boolean | undefined, content?: ResourceStr | undefined): this
```

设置滑动时是否显示气泡提示。

当direction的值为Axis.Horizontal时，tip显示在滑块上方，如果上方空间不够，则在下方显示。当值为Axis.Vertical时，tip显示在滑块左边，如果左边空间不够，则在右边显示。当不设置周边边距或者周边边距比较小时，tip会被截断。

tip的绘制区域为Slider自身节点的overlay。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SliderAttribute-default showTips(value: boolean | undefined, content?: ResourceStr | undefined): this--><!--Device-SliderAttribute-default showTips(value: boolean | undefined, content?: ResourceStr | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean \| undefined | 是 | 滑动时是否显示气泡提示。取值为undefined时，按默认值处理。&lt;br/&gt;true：显示气泡；false：不显示气泡。&lt;br/&gt;默认值：false |
| content | [ResourceStr](arkts-arkui-resourcestr-t.md) \| undefined | 否 | 气泡提示的文本内容，默认显示当前百分比。取值为undefined时，按默认处理。&lt;br/&gt; |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## slideRange

```TypeScript
default slideRange(value: SlideRange | undefined): this
```

设置有效滑动区间。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SliderAttribute-default slideRange(value: SlideRange | undefined): this--><!--Device-SliderAttribute-default slideRange(value: SlideRange | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [SlideRange](arkts-arkui-slider-sliderange-i.md) \| undefined | 是 | 设置有效滑动区间。取值为undefined时，不限制有效滑动区间。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## sliderInteractionMode

```TypeScript
default sliderInteractionMode(value: SliderInteraction | undefined): this
```

设置用户与滑动条组件交互方式。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SliderAttribute-default sliderInteractionMode(value: SliderInteraction | undefined): this--><!--Device-SliderAttribute-default sliderInteractionMode(value: SliderInteraction | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [SliderInteraction](arkts-arkui-slider-sliderinteraction-e.md) \| undefined | 是 | 用户与滑动条组件交互方式。取值为undefined时，按默认值处理。 &lt;br /&gt; 默认值： SliderInteraction.SLIDE_AND_CLICK。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## stepColor

```TypeScript
default stepColor(value: ResourceColor | undefined): this
```

设置刻度颜色。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SliderAttribute-default stepColor(value: ResourceColor | undefined): this--><!--Device-SliderAttribute-default stepColor(value: ResourceColor | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | 是 | 刻度颜色。取值为undefined时，按默认值处理。&lt;br/&gt;默认值：&lt;br/&gt; `\\$r('sys.color.ohos_id_color_foreground')`混合&lt;br/&gt;`\\$r('sys.color.ohos_id_alpha_normal_bg')`透明度的颜色 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## stepSize

```TypeScript
default stepSize(value: Length | undefined): this
```

设置刻度大小（直径）。当值为0时，刻度点不显示，当值小于0时，取默认值。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SliderAttribute-default stepSize(value: Length | undefined): this--><!--Device-SliderAttribute-default stepSize(value: Length | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Length](arkts-arkui-length-t.md) \| undefined | 是 | 刻度大小（直径）。取值为undefined时，按默认值处理。 &lt;br/&gt;默认值：'4vp'&lt;br/&gt;取值范围： [0, [trackThickness](arkts-arkui-slider-sliderattribute-i.md#trackthickness)) |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## suffix

```TypeScript
default suffix<T extends Object>(content: ComponentContent<T> | undefined, options?: SliderSuffixOptions | undefined): this
```

设置滑动条的后缀。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SliderAttribute-default suffix<T extends Object>(content: ComponentContent<T> | undefined, options?: SliderSuffixOptions | undefined): this--><!--Device-SliderAttribute-default suffix<T extends Object>(content: ComponentContent<T> | undefined, options?: SliderSuffixOptions | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| content | [ComponentContent](arkts-arkui-componentcontent-c.md)&lt;T&gt; \| undefined | 是 | 自定义组件内容，用于定义滑块后缀的可视化内容，该内容会显示在滑块的结束位置。取值为undefined时，则不使用后缀。 |
| options | [SliderSuffixOptions](arkts-arkui-slider-slidersuffixoptions-i.md) \| undefined | 否 | 滑块后缀的配置选项，用于设置与无障碍功能相关的属性。取值为undefined时，则不使用后缀。 &lt;br/&gt;默认值： null |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## trackBorderRadius

```TypeScript
default trackBorderRadius(value: Length | undefined): this
```

设置底板圆角半径。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SliderAttribute-default trackBorderRadius(value: Length | undefined): this--><!--Device-SliderAttribute-default trackBorderRadius(value: Length | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Length](arkts-arkui-length-t.md) \| undefined | 是 | 底板圆角半径。取值为undefined时，按默认值处理。&lt;br/&gt;默认值：&lt;br/&gt;style值为SliderStyle.OutSet时默认值为'2 vp'。&lt;br/&gt;style值为SliderStyle.InSet时默认值为'10vp'。&lt;br/&gt;**说明：** &lt;br/&gt;设定值小于0时取默认值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## trackColor

```TypeScript
default trackColor(value: ResourceColor | LinearGradient | undefined): this
```

设置滑轨的背景颜色。

从API version 12开始支持利用LinearGradient设置滑轨的渐变色。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SliderAttribute-default trackColor(value: ResourceColor | LinearGradient | undefined): this--><!--Device-SliderAttribute-default trackColor(value: ResourceColor | LinearGradient | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| LinearGradient \| undefined | 是 | 滑轨的背景颜色。取值为undefined时，按默认值处理。&lt;br/&gt;默认值： `\\$r('sys.color.ohos_id_color_component_normal')`&lt;br/&gt;**说明：** &lt;br/&gt;1. 设置渐变色时，如果颜色断点颜色值为非法值或渐变色断点为空，渐变色将不起效果。&lt; br/&gt;2. 该接口中的LinearGradient类型不支持在原子化服务中使用。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## trackColorMetrics

```TypeScript
default trackColorMetrics(color: ColorMetricsLinearGradient | undefined): this
```

设置滑轨轨道的线性渐变背景颜色。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SliderAttribute-default trackColorMetrics(color: ColorMetricsLinearGradient | undefined): this--><!--Device-SliderAttribute-default trackColorMetrics(color: ColorMetricsLinearGradient | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| color | [ColorMetricsLinearGradient](arkts-arkui-slider-colormetricslineargradient-c.md) \| undefined | 是 | 滑轨轨道的线性渐变背景颜色。&lt;br/&gt;设置渐变色时，如果color的值为undefined，渐变色设置无效，轨 道背景颜色默认取值为：`\\$r('sys.color.ohos_id_color_component_normal')`。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## trackThickness

```TypeScript
default trackThickness(value: Length | undefined): this
```

设置滑轨的粗细。设置小于等于0的值时，取默认值。

为保证滑块和滑轨的[SliderStyle](../arkts-components/arkts-arkui-sliderstyle-e.md/arkts-arkui-sliderstyle-e.md)样式，[blockSize](arkts-arkui-slider-sliderattribute-i.md#blocksize)跟随trackThickness同比例增减。

当style为[SliderStyle](../arkts-components/arkts-arkui-sliderstyle-e.md/arkts-arkui-sliderstyle-e.md).OutSet时，trackThickness ：[blockSize](arkts-arkui-slider-sliderattribute-i.md#blocksize) = 1 ：4，当style为  
[SliderStyle](../arkts-components/arkts-arkui-sliderstyle-e.md/arkts-arkui-sliderstyle-e.md).InSet时，trackThickness ：[blockSize](arkts-arkui-slider-sliderattribute-i.md#blocksize) = 5 ：3。

trackThickness或[blockSize](arkts-arkui-slider-sliderattribute-i.md#blocksize)的大小超过Slider组件的宽度或高度时，取默认值。

当[SliderStyle](../arkts-components/arkts-arkui-sliderstyle-e.md/arkts-arkui-sliderstyle-e.md)设置为OutSet时，尽管trackThickness的大小没超过Slider组件的宽度或高度，但是[blockSize](arkts-arkui-slider-sliderattribute-i.md#blocksize)超过了，取默认值。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SliderAttribute-default trackThickness(value: Length | undefined): this--><!--Device-SliderAttribute-default trackThickness(value: Length | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Length](arkts-arkui-length-t.md) \| undefined | 是 | 滑轨的粗细。取值为undefined时，按默认值处理。&lt;br/&gt;默认值：当参数style的值设置 [SliderStyle](../arkts-components/arkts-arkui-sliderstyle-e.md/arkts-arkui-sliderstyle-e.md).OutSet 时为 4.0vp，[SliderStyle](../arkts-components/arkts-arkui-sliderstyle-e.md/arkts-arkui-sliderstyle-e.md).InSet时为20.0vp。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

