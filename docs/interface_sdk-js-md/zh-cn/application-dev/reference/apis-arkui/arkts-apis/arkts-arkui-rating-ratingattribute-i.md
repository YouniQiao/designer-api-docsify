# RatingAttribute

**继承/实现关系：** RatingAttribute extends CommonMethod

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<RatingAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

设置Rating的属性修改器。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[RatingAttribute](arkts-arkui-rating-ratingattribute-i.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [RatingAttribute](arkts-arkui-rating-ratingattribute-i.md) |

## contentModifier

```TypeScript
default contentModifier(modifier: ContentModifier<RatingConfiguration> | undefined): this
```

定制Rating内容区的方法。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [ContentModifier](../arkts-components/arkts-arkui-contentmodifier-i.md)&lt;[RatingConfiguration](arkts-arkui-rating-ratingconfiguration-i.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [RatingAttribute](arkts-arkui-rating-ratingattribute-i.md) |

## onChange

```TypeScript
default onChange(callback: OnRatingChangeCallback | undefined): this
```

当评分条的评星变化时会触发该回调。与[onChange](#onchange)相比，callback参数新增了对undefined类型的支持。使用callback异步回调。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [OnRatingChangeCallback](arkts-arkui-onratingchangecallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [RatingAttribute](arkts-arkui-rating-ratingattribute-i.md) |

## stars

```TypeScript
default stars(value: int | undefined): this
```

设置评分总数。设置为小于等于0的值时，按默认值显示。与stars相比，value参数新增了对undefined类型的支持。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | int \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [RatingAttribute](arkts-arkui-rating-ratingattribute-i.md) |

## starStyle

```TypeScript
default starStyle(options: StarStyleOptions | undefined): this
```

设置评分的样式。该属性所支持的图片类型能力参考Image组件。支持加载本地图片和网络图片，暂不支持[PixelMap](../../apis-image-kit/arkts-apis/arkts-image-image-pixelmap-i.md)类型。默认图片加载方式为异步，暂不支持同步加载。与[starStyle](#starstyle)相比，options参数新增了对undefined类型的支持。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [StarStyleOptions](arkts-arkui-rating-starstyleoptions-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [RatingAttribute](arkts-arkui-rating-ratingattribute-i.md) |

## stepSize

```TypeScript
default stepSize(value: double | undefined): this
```

设置操作评级的步长。设置为小于0.1的值时，按默认值显示。与stepSize相比，value参数新增了对undefined类型的支持。

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
| [RatingAttribute](arkts-arkui-rating-ratingattribute-i.md) |
