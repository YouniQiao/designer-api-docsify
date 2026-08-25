# DotIndicator

Define DotIndicator, the indicator type is dot.

**继承/实现关系：** DotIndicator extends [Indicator](arkts-arkui-swiper-indicator-c.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## color

```TypeScript
color(value: ResourceColor | undefined): this
```

Swiper组件圆点导航指示器的颜色。

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
| [DotIndicator](arkts-arkui-swiper-dotindicator-c.md) |

## constructor

```TypeScript
constructor()
```

DotIndicator的构造函数。

> **说明：**&gt;
> - 按压导航点时，导航点会放大至1.33倍显示，因此非按压态时导航点的可见范围边界至实际范围边界存在一定距离，该距离会随着itemWidth、itemHeight、selectedItemWidth、
> selectedItemHeight等参数变大而变大。&gt;
> - 若页面数量较多、圆点导航点超出页面时，建议使用maxDisplayCount设置导航点显示个数。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## itemHeight

```TypeScript
itemHeight(value: Length | undefined): this
```

Swiper组件圆点导航指示器的高。

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
| [DotIndicator](arkts-arkui-swiper-dotindicator-c.md) |

## itemWidth

```TypeScript
itemWidth(value: Length | undefined): this
```

Swiper组件圆点导航指示器的宽。

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
| [DotIndicator](arkts-arkui-swiper-dotindicator-c.md) |

## mask

```TypeScript
mask(value: boolean | undefined): this
```

是否显示Swiper组件圆点导航指示器的蒙版样式。

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
| [DotIndicator](arkts-arkui-swiper-dotindicator-c.md) |

## maxDisplayCount

```TypeScript
maxDisplayCount(maxDisplayCount: int | undefined): this
```

圆点导航点指示器样式下，导航点显示个数最大值。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [maxDisplayCount](#maxdisplaycount) | int \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [DotIndicator](arkts-arkui-swiper-dotindicator-c.md) |

## selectedColor

```TypeScript
selectedColor(value: ResourceColor | undefined): this
```

选中Swiper组件圆点导航指示器的颜色。

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
| [DotIndicator](arkts-arkui-swiper-dotindicator-c.md) |

## selectedItemHeight

```TypeScript
selectedItemHeight(value: Length | undefined): this
```

选中Swiper组件圆点导航指示器的高。

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
| [DotIndicator](arkts-arkui-swiper-dotindicator-c.md) |

## selectedItemWidth

```TypeScript
selectedItemWidth(value: Length | undefined): this
```

选中Swiper组件圆点导航指示器的宽。

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
| [DotIndicator](arkts-arkui-swiper-dotindicator-c.md) |

## space

```TypeScript
space(space: LengthMetrics | undefined): this
```

设置Swiper圆点导航点间距。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [space](#space) | [LengthMetrics](arkts-arkui-lengthmetrics-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [DotIndicator](arkts-arkui-swiper-dotindicator-c.md) |
