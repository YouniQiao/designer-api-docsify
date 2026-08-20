# DigitIndicator

Define DigitIndicator, the indicator type is digit.

**Inheritance/Implementation:** DigitIndicator extends [Indicator](arkts-swiper-indicator-c.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare class DigitIndicator--><!--Device-unnamed-export declare class DigitIndicator-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor()
```

Constructor.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DigitIndicator-constructor()--><!--Device-DigitIndicator-constructor()-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## digitFont

```TypeScript
digitFont(value: Font | undefined): this
```

Set the digital indicator font (just support font size and weight).

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DigitIndicator-digitFont(value: Font | undefined): this--><!--Device-DigitIndicator-digitFont(value: Font | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Font](../../apis-arkui/arkts-apis/arkts-arkui-font-i.md) \| undefined | Yes | the indicator font size and weight, default value is { size: 14, weight: FontWeight.Normal }, undefined means setting to default value. |

**Return value:**

| Type | Description |
| --- | --- |
| [DigitIndicator](arkts-swiper-digitindicator-c.md) |  |

## fontColor

```TypeScript
fontColor(value: ResourceColor | undefined): this
```

Set font color of the digital indicator.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DigitIndicator-fontColor(value: ResourceColor | undefined): this--><!--Device-DigitIndicator-fontColor(value: ResourceColor | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ResourceColor](../../apis-arkui/arkts-apis/arkts-arkui-resourcecolor-t.md) \| undefined | Yes | the indicator font color, default value is { #FF182431 }, undefined means setting to default value. |

**Return value:**

| Type | Description |
| --- | --- |
| [DigitIndicator](arkts-swiper-digitindicator-c.md) |  |

## selectedDigitFont

```TypeScript
selectedDigitFont(value: Font | undefined): this
```

Set the digital indicator font (just support font size and weight).

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DigitIndicator-selectedDigitFont(value: Font | undefined): this--><!--Device-DigitIndicator-selectedDigitFont(value: Font | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Font](../../apis-arkui/arkts-apis/arkts-arkui-font-i.md) \| undefined | Yes | the indicator font size and weight when selected, default value is { size: 14, weight: FontWeight.Normal }, undefined means setting to default value. |

**Return value:**

| Type | Description |
| --- | --- |
| [DigitIndicator](arkts-swiper-digitindicator-c.md) |  |

## selectedFontColor

```TypeScript
selectedFontColor(value: ResourceColor | undefined): this
```

Set font color of the digital indicator when selected.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DigitIndicator-selectedFontColor(value: ResourceColor | undefined): this--><!--Device-DigitIndicator-selectedFontColor(value: ResourceColor | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ResourceColor](../../apis-arkui/arkts-apis/arkts-arkui-resourcecolor-t.md) \| undefined | Yes | the indicator font color when selected, default value is { #FF182431 }, undefined means setting to default value. |

**Return value:**

| Type | Description |
| --- | --- |
| [DigitIndicator](arkts-swiper-digitindicator-c.md) |  |

