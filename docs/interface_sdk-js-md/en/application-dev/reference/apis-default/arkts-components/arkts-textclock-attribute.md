# TextClockAttribute

Defines the TextClock component attributes.

**Inheritance/Implementation:** TextClockAttribute extends CommonMethod

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-unnamed-export declare interface TextClockAttribute--><!--Device-unnamed-export declare interface TextClockAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
attributeModifier(modifier: AttributeModifier<TextClockAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-TextClockAttribute-attributeModifier(modifier: AttributeModifier<TextClockAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-TextClockAttribute-attributeModifier(modifier: AttributeModifier<TextClockAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[TextClockAttribute](arkts-textclock-attribute.md)&gt; \| [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../../apis-arkui/arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## contentModifier

```TypeScript
contentModifier(modifier: ContentModifier<TextClockConfiguration> | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-TextClockAttribute-contentModifier(modifier: ContentModifier<TextClockConfiguration> | undefined): this--><!--Device-TextClockAttribute-contentModifier(modifier: ContentModifier<TextClockConfiguration> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | [ContentModifier](../../apis-arkui/arkts-components/arkts-arkui-contentmodifier-i.md)&lt;[TextClockConfiguration](arkts-textclock-textclockconfiguration-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## dateTimeOptions

```TypeScript
dateTimeOptions(dateTimeOptions: DateTimeOptions | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-TextClockAttribute-dateTimeOptions(dateTimeOptions: DateTimeOptions | undefined): this--><!--Device-TextClockAttribute-dateTimeOptions(dateTimeOptions: DateTimeOptions | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dateTimeOptions | DateTimeOptions \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## fontColor

```TypeScript
fontColor(value: ResourceColor | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-TextClockAttribute-fontColor(value: ResourceColor | undefined): this--><!--Device-TextClockAttribute-fontColor(value: ResourceColor | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ResourceColor](../../apis-arkui/arkts-apis/arkts-arkui-resourcecolor-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## fontFamily

```TypeScript
fontFamily(value: ResourceStr | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-TextClockAttribute-fontFamily(value: ResourceStr | undefined): this--><!--Device-TextClockAttribute-fontFamily(value: ResourceStr | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ResourceStr](../../apis-arkui/arkts-apis/arkts-arkui-resourcestr-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## fontFeature

```TypeScript
fontFeature(value: string | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-TextClockAttribute-fontFeature(value: string | undefined): this--><!--Device-TextClockAttribute-fontFeature(value: string | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | string \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## fontSize

```TypeScript
fontSize(value: Length | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-TextClockAttribute-fontSize(value: Length | undefined): this--><!--Device-TextClockAttribute-fontSize(value: Length | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Length](../../apis-arkui/arkts-apis/arkts-arkui-length-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## fontStyle

```TypeScript
fontStyle(value: FontStyle | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-TextClockAttribute-fontStyle(value: FontStyle | undefined): this--><!--Device-TextClockAttribute-fontStyle(value: FontStyle | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [FontStyle](../../apis-arkui/arkts-apis/arkts-arkui-fontstyle-e.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## fontWeight

```TypeScript
fontWeight(value: int | FontWeight | string | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-TextClockAttribute-fontWeight(value: int | FontWeight | string | undefined): this--><!--Device-TextClockAttribute-fontWeight(value: int | FontWeight | string | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | int \| [FontWeight](../../apis-arkui/arkts-apis/arkts-arkui-fontweight-e.md) \| string \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## format

```TypeScript
format(value: ResourceStr | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-TextClockAttribute-format(value: ResourceStr | undefined): this--><!--Device-TextClockAttribute-format(value: ResourceStr | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ResourceStr](../../apis-arkui/arkts-apis/arkts-arkui-resourcestr-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onDateChange

```TypeScript
onDateChange(event: Callback<long> | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-TextClockAttribute-onDateChange(event: Callback<long> | undefined): this--><!--Device-TextClockAttribute-onDateChange(event: Callback<long> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;long&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## setTextClockOptions

```TypeScript
setTextClockOptions(options?: TextClockOptions): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-TextClockAttribute-setTextClockOptions(options?: TextClockOptions): this--><!--Device-TextClockAttribute-setTextClockOptions(options?: TextClockOptions): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [TextClockOptions](arkts-textclock-textclockoptions-i.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
## textShadow

```TypeScript
textShadow(value: ShadowOptions | Array<ShadowOptions> | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-TextClockAttribute-textShadow(value: ShadowOptions | Array<ShadowOptions> | undefined): this--><!--Device-TextClockAttribute-textShadow(value: ShadowOptions | Array<ShadowOptions> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ShadowOptions](../../apis-arkui/arkts-components/arkts-arkui-shadowoptions-i.md) \| Array&lt;[ShadowOptions](../../apis-arkui/arkts-components/arkts-arkui-shadowoptions-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## default

```TypeScript
default
```

Set TextClock options.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextClockAttribute-default--><!--Device-TextClockAttribute-default-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

