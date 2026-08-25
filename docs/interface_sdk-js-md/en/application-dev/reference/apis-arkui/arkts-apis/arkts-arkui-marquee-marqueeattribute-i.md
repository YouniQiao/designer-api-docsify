# MarqueeAttribute

Declares marquee properties.

**Inheritance/Implementation:** MarqueeAttribute extends CommonMethod

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## allowScale

```TypeScript
default allowScale(value: boolean | undefined): this
```

Set marquee allow scale.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>This parameter is effective only when fontSize is in fp units. </p>

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | boolean \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [MarqueeAttribute](arkts-arkui-marquee-marqueeattribute-i.md) |

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<MarqueeAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

Sets the attribute modifier.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[MarqueeAttribute](arkts-arkui-marquee-marqueeattribute-i.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [MarqueeAttribute](arkts-arkui-marquee-marqueeattribute-i.md) |

## fontColor

```TypeScript
default fontColor(value: ResourceColor | undefined): this
```

Set marquee font Color.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [MarqueeAttribute](arkts-arkui-marquee-marqueeattribute-i.md) |

## fontFamily

```TypeScript
default fontFamily(value: string | Resource | undefined): this
```

Set marquee font family.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>Default font: 'HarmonyOS Sans'<br>The 'HarmonyOS Sans' font and registered custom fonts are supported for applications. <br>Only the 'HarmonyOS Sans' font is supported for widgets. </p>

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | string \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [MarqueeAttribute](arkts-arkui-marquee-marqueeattribute-i.md) |

## fontSize

```TypeScript
default fontSize(value: Length | undefined): this
```

Set marquee font size.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>If fontSize is of the number type, the unit fp is used. The default font size is 16 fp. <br>This parameter cannot be set in percentage. </p>

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [Length](arkts-arkui-length-t.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [MarqueeAttribute](arkts-arkui-marquee-marqueeattribute-i.md) |

## fontWeight

```TypeScript
default fontWeight(value: int | FontWeight | ResourceStr | undefined): this
```

Set marquee font weight.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>If the value is too large, the text may be clipped depending on the font. <br>For the number type, the value range is [100, 900], at an interval of 100. <br>The default value is 400. <br>A larger value indicates a heavier font weight. <br>For the string type, only strings that represent a number, for example, "400", and the following enumerated values of FontWeight are supported: "bold", "bolder", "lighter", "regular", and "medium". </p>

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | int \| [FontWeight](arkts-arkui-fontweight-e.md) \| [ResourceStr](arkts-arkui-resourcestr-t.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [MarqueeAttribute](arkts-arkui-marquee-marqueeattribute-i.md) |

## marqueeUpdateStrategy

```TypeScript
default marqueeUpdateStrategy(value: MarqueeUpdateStrategy | undefined): this
```

Marquee scrolling strategy after text update.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>This attribute takes effect when the marquee is in the playing state and the text content width exceeds the width of the marquee component. </p>

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [MarqueeUpdateStrategy](arkts-arkui-marqueeupdatestrategy-e.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [MarqueeAttribute](arkts-arkui-marquee-marqueeattribute-i.md) |

## onBounce

```TypeScript
default onBounce(event: (() => void) | undefined): this
```

Called when scrolling to the bottom.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>This event will be triggered for multiple times if the loop attribute is not set to 1. </p>

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | (() = & gt; void) \ | undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [MarqueeAttribute](arkts-arkui-marquee-marqueeattribute-i.md) |

## onFinish

```TypeScript
default onFinish(event: (() => void) | undefined): this
```

Called when scrolling is complete.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | (() = & gt; void) \ | undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [MarqueeAttribute](arkts-arkui-marquee-marqueeattribute-i.md) |

## onStart

```TypeScript
default onStart(event: (() => void) | undefined): this
```

Called when scrolling starts.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | (() = & gt; void) \ | undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [MarqueeAttribute](arkts-arkui-marquee-marqueeattribute-i.md) |

## onStop

```TypeScript
default onStop(event: VoidCallback | undefined): this
```

Called when scrolling is stopped.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>If event is set to undefined, the current event will be unbound. </p>

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | [VoidCallback](arkts-arkui-voidcallback-t.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [MarqueeAttribute](arkts-arkui-marquee-marqueeattribute-i.md) |

## setMarqueeOptions

```TypeScript
default setMarqueeOptions(options: MarqueeOptions): this
```

Set Marquee options.

**Since:** 26.1.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [MarqueeOptions](arkts-arkui-marquee-marqueeoptions-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [MarqueeAttribute](arkts-arkui-marquee-marqueeattribute-i.md) |
