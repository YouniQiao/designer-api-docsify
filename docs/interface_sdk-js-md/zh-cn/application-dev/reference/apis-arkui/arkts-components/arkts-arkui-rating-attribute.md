# Rating属性/事件

**继承/实现关系：** RatingAttribute extends CommonMethod<RatingAttribute>

**起始版本：** 7

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## contentModifier

```TypeScript
contentModifier(modifier: ContentModifier<RatingConfiguration>)
```

定制Rating内容区的方法。开发者需自定义class实现ContentModifier接口，并在applyContent方法中返回WrappedBuilder，以此重新定义Rating组件内容区的渲染逻辑。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [ContentModifier](arkts-arkui-contentmodifier-i.md)&lt;[RatingConfiguration](arkts-arkui-ratingconfiguration-i.md)&gt; | 是 |

## contentModifier

```TypeScript
contentModifier(modifier: Optional<ContentModifier<RatingConfiguration>>)
```

定制Rating内容区的方法。与 [contentModifier](#contentmodifier)相比，modifier 参数新增了对undefined类型的支持。当modifier的值为undefined时，不使用内容修改器。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [Optional](arkts-arkui-optional-t.md)&lt;[ContentModifier](arkts-arkui-contentmodifier-i.md)&lt;[RatingConfiguration](arkts-arkui-ratingconfiguration-i.md)&gt;&gt; | 是 |

## onChange

```TypeScript
onChange(callback: (value: number) => void)
```

当评分条的评分变化时触发该回调。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | (value: number) = & gt; void | 是 |

## onChange

```TypeScript
onChange(callback: Optional<OnRatingChangeCallback>)
```

当评分条的评分变化时触发该回调。与onChange相比，callback参数新增了对 undefined类型的支持。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本18开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Optional](arkts-arkui-optional-t.md)&lt;[OnRatingChangeCallback](arkts-arkui-onratingchangecallback-t.md)&gt; | 是 |

## stars

```TypeScript
stars(value: number)
```

设置评分总数。默认值：5。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | number | 是 |

## stars

```TypeScript
stars(starCount: Optional<number>)
```

设置评分总数。与[stars](#stars)相比，starCount参数新增了对undefined类型的支持。当starCount的值为undefined时，默认值：5。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本18开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| starCount | [Optional](arkts-arkui-optional-t.md)&lt;number&gt; | 是 |

## starStyle

```TypeScript
starStyle(options: StarStyleOptions)
```

设置评分的样式。该属性所支持的图片类型能力参考Image组件。支持加载本地图片和网络图片，暂不支持PixelMap类型。默认图片加载方式为异步，暂不支持同步加载。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [StarStyleOptions](arkts-arkui-starstyleoptions-i.md) | 是 |

## starStyle

```TypeScript
starStyle(options: Optional<StarStyleOptions>)
```

设置评分的样式。该属性所支持的图片类型能力参考Image组件。支持加载本地图片和网络图片，暂不支持PixelMap类型。默认图片加载方式为异步，暂不支持同步加载。与[starStyle](#starstyle)相比，options参数新增了对undefined类型的支持。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本18开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [Optional](arkts-arkui-optional-t.md)&lt;[StarStyleOptions](arkts-arkui-starstyleoptions-i.md)&gt; | 是 |

## stepSize

```TypeScript
stepSize(value: number)
```

设置操作评级的步长。设置为小于0.1的值时，按默认值显示。默认值：0.5。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | number | 是 |

## stepSize

```TypeScript
stepSize(size: Optional<number>)
```

设置操作评级的步长。设置为小于0.1的值时，按默认值显示。与[stepSize](#stepsize)相比，size参数新增了对undefined类型的支持。当size的值为undefined时，默认值：0.5。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本18开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| size | [Optional](arkts-arkui-optional-t.md)&lt;number&gt; | 是 |
