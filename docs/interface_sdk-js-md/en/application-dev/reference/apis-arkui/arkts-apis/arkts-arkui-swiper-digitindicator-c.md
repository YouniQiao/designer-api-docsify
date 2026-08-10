# DigitIndicator

Define DigitIndicator, the indicator type is digit.

**Inheritance/Implementation:** DigitIndicator extends [Indicator](../arkts-components/arkts-arkui-indicator-c.md/arkts-arkui-indicator-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class DigitIndicator extends Indicator--><!--Device-unnamed-export declare class DigitIndicator extends Indicator-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor()
```

DotIndicator的构造函数。

> **说明：**
> 
> - 按压导航点时，导航点会放大至1.33倍显示，因此非按压态时导航点的可见范围边界至实际范围边界存在一定距离，该距离会随着itemWidth、itemHeight、selectedItemWidth、
> selectedItemHeight等参数变大而变大。
> 
> - 若页面数量较多、圆点导航点超出页面时，建议使用maxDisplayCount设置导航点显示个数。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DigitIndicator-constructor()--><!--Device-DigitIndicator-constructor()-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## digitFont

```TypeScript
digitFont(value: Font | undefined): this
```

Swiper组件数字导航点的字体样式。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DigitIndicator-digitFont(value: Font | undefined): this--><!--Device-DigitIndicator-digitFont(value: Font | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Font](arkts-arkui-font-i.md) \| undefined | Yes | 设置Swiper组件数字导航点的字体样式。&lt;br/&gt;只支持Font中size和weight参数，family和style设置不生效。&lt;br/&gt;默认值：{ size:?14,?weight:?FontWeight.Normal?}&lt;br/&gt;取值为undefined时，按默认值处理。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## fontColor

```TypeScript
fontColor(value: ResourceColor | undefined): this
```

Swiper组件数字导航点的字体颜色。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DigitIndicator-fontColor(value: ResourceColor | undefined): this--><!--Device-DigitIndicator-fontColor(value: ResourceColor | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | Yes | 设置Swiper组件数字导航点的字体颜色。&lt;br/&gt;默认值：'#ff182431'，黑色。&lt;br/&gt;取值为undefined时，按默认值处理 。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## selectedDigitFont

```TypeScript
selectedDigitFont(value: Font | undefined): this
```

选中Swiper组件数字导航点的字体样式。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DigitIndicator-selectedDigitFont(value: Font | undefined): this--><!--Device-DigitIndicator-selectedDigitFont(value: Font | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Font](arkts-arkui-font-i.md) \| undefined | Yes | 设置选中Swiper组件数字导航点的字体样式。&lt;br/&gt;默认值：{?size:?14,?weight:?FontWeight.Normal?}&lt;br/&gt;取值为 undefined时，按默认值处理。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## selectedFontColor

```TypeScript
selectedFontColor(value: ResourceColor | undefined): this
```

选中Swiper组件数字导航点的字体颜色。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DigitIndicator-selectedFontColor(value: ResourceColor | undefined): this--><!--Device-DigitIndicator-selectedFontColor(value: ResourceColor | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | Yes | 设置选中Swiper组件数字导航点的字体颜色。&lt;br/&gt;默认值：'#ff182431'，黑色。&lt;br/&gt;取值为undefined时，按默认值 处理。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

