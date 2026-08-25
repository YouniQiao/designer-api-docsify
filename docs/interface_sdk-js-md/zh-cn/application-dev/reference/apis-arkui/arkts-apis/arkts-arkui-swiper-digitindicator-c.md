# DigitIndicator

Define DigitIndicator, the indicator type is digit.

**继承/实现关系：** DigitIndicator extends [Indicator](arkts-arkui-swiper-indicator-c.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

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

## digitFont

```TypeScript
digitFont(value: Font | undefined): this
```

Swiper组件数字导航点的字体样式。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Font](arkts-arkui-font-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [DigitIndicator](arkts-arkui-swiper-digitindicator-c.md) |

## fontColor

```TypeScript
fontColor(value: ResourceColor | undefined): this
```

Swiper组件数字导航点的字体颜色。

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
| [DigitIndicator](arkts-arkui-swiper-digitindicator-c.md) |

## selectedDigitFont

```TypeScript
selectedDigitFont(value: Font | undefined): this
```

选中Swiper组件数字导航点的字体样式。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Font](arkts-arkui-font-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [DigitIndicator](arkts-arkui-swiper-digitindicator-c.md) |

## selectedFontColor

```TypeScript
selectedFontColor(value: ResourceColor | undefined): this
```

选中Swiper组件数字导航点的字体颜色。

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
| [DigitIndicator](arkts-arkui-swiper-digitindicator-c.md) |
