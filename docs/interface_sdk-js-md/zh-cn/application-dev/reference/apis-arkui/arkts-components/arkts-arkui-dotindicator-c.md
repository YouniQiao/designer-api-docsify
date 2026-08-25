# DotIndicator

构造圆点指示器的样式，继承自[Indicator](arkts-arkui-indicator-c.md)。

**继承/实现关系：** DotIndicator extends Indicator<DotIndicator>

**起始版本：** 10

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## color

```TypeScript
color(value: ResourceColor): DotIndicator
```

Swiper组件圆点导航指示器的颜色。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本10开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [DotIndicator](arkts-arkui-dotindicator-c.md) |

## constructor

```TypeScript
constructor()
```

DotIndicator的构造函数。

> **说明：**

> - 按压导航点时，导航点会放大至1.33倍显示，因此非按压态时导航点的可见范围边界至实际范围边界存在一定距离，该距离会随着itemWidth、itemHeight、selectedItemWidth、
> selectedItemHeight等参数变大而变大。&gt;
> - 若页面数量较多、圆点导航点超出页面时，建议使用maxDisplayCount设置导航点显示个数。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本10开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## indicatorIcon

```TypeScript
indicatorIcon(iconList: Array<IndicatorIconInfo>): DotIndicator
```

设置导航点图标。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本26.0.0开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| iconList | Array&lt;[IndicatorIconInfo](arkts-arkui-indicatoriconinfo-i.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| [DotIndicator](arkts-arkui-dotindicator-c.md) |

## itemHeight

```TypeScript
itemHeight(value: Length): DotIndicator
```

Swiper组件圆点导航指示器的高。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本10开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Length](../arkts-apis/arkts-arkui-length-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [DotIndicator](arkts-arkui-dotindicator-c.md) |

## itemWidth

```TypeScript
itemWidth(value: Length): DotIndicator
```

Swiper组件圆点导航指示器的宽。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本10开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Length](../arkts-apis/arkts-arkui-length-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [DotIndicator](arkts-arkui-dotindicator-c.md) |

## mask

```TypeScript
mask(value: boolean): DotIndicator
```

是否显示Swiper组件圆点导航指示器的蒙版样式。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本10开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| [DotIndicator](arkts-arkui-dotindicator-c.md) |

## maxDisplayCount

```TypeScript
maxDisplayCount(maxDisplayCount: number): DotIndicator
```

圆点导航点指示器样式下，导航点显示个数最大值。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [maxDisplayCount](arkts-arkui-dotindicator-c.md) | number | 是 |

**返回值：**

| 类型 |
| --- |
| [DotIndicator](arkts-arkui-dotindicator-c.md) |

## selectedColor

```TypeScript
selectedColor(value: ResourceColor): DotIndicator
```

选中Swiper组件圆点导航指示器的颜色。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本10开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [DotIndicator](arkts-arkui-dotindicator-c.md) |

## selectedItemHeight

```TypeScript
selectedItemHeight(value: Length): DotIndicator
```

选中Swiper组件圆点导航指示器的高。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本10开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Length](../arkts-apis/arkts-arkui-length-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [DotIndicator](arkts-arkui-dotindicator-c.md) |

## selectedItemWidth

```TypeScript
selectedItemWidth(value: Length): DotIndicator
```

选中Swiper组件圆点导航指示器的宽。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本10开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Length](../arkts-apis/arkts-arkui-length-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [DotIndicator](arkts-arkui-dotindicator-c.md) |

## space

```TypeScript
space(space: LengthMetrics): DotIndicator
```

设置Swiper圆点导航点间距。

**起始版本：** 19

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本19开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [space](#space) | [LengthMetrics](../arkts-apis/arkts-arkui-lengthmetrics-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [DotIndicator](arkts-arkui-dotindicator-c.md) |
