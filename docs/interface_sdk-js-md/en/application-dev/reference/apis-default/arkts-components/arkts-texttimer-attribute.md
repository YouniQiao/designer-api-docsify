# TextTimerAttribute

Defines the TextTimer component attributes.

**Inheritance/Implementation:** TextTimerAttribute extends CommonMethod

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-unnamed-export declare interface TextTimerAttribute--><!--Device-unnamed-export declare interface TextTimerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
attributeModifier(modifier: AttributeModifier<TextTimerAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-TextTimerAttribute-attributeModifier(modifier: AttributeModifier<TextTimerAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-TextTimerAttribute-attributeModifier(modifier: AttributeModifier<TextTimerAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[TextTimerAttribute](arkts-texttimer-attribute.md)&gt; \| [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../../apis-arkui/arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## contentModifier

```TypeScript
contentModifier(modifier: ContentModifier<TextTimerConfiguration> | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-TextTimerAttribute-contentModifier(modifier: ContentModifier<TextTimerConfiguration> | undefined): this--><!--Device-TextTimerAttribute-contentModifier(modifier: ContentModifier<TextTimerConfiguration> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | [ContentModifier](../../apis-arkui/arkts-components/arkts-arkui-contentmodifier-i.md)&lt;[TextTimerConfiguration](arkts-texttimer-texttimerconfiguration-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## fontColor

```TypeScript
fontColor(value: ResourceColor | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-TextTimerAttribute-fontColor(value: ResourceColor | undefined): this--><!--Device-TextTimerAttribute-fontColor(value: ResourceColor | undefined): this-End-->

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

<!--Device-TextTimerAttribute-fontFamily(value: ResourceStr | undefined): this--><!--Device-TextTimerAttribute-fontFamily(value: ResourceStr | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ResourceStr](../../apis-arkui/arkts-apis/arkts-arkui-resourcestr-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## fontSize

```TypeScript
fontSize(value: Length | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-TextTimerAttribute-fontSize(value: Length | undefined): this--><!--Device-TextTimerAttribute-fontSize(value: Length | undefined): this-End-->

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

<!--Device-TextTimerAttribute-fontStyle(value: FontStyle | undefined): this--><!--Device-TextTimerAttribute-fontStyle(value: FontStyle | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [FontStyle](../../apis-arkui/arkts-apis/arkts-arkui-fontstyle-e.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## fontWeight

```TypeScript
fontWeight(value: int | FontWeight | ResourceStr | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-TextTimerAttribute-fontWeight(value: int | FontWeight | ResourceStr | undefined): this--><!--Device-TextTimerAttribute-fontWeight(value: int | FontWeight | ResourceStr | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | int \| [FontWeight](../../apis-arkui/arkts-apis/arkts-arkui-fontweight-e.md) \| [ResourceStr](../../apis-arkui/arkts-apis/arkts-arkui-resourcestr-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## format

```TypeScript
format(value: string | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-TextTimerAttribute-format(value: string | undefined): this--><!--Device-TextTimerAttribute-format(value: string | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | string \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onTimer

```TypeScript
onTimer(event: TimerCallback | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-TextTimerAttribute-onTimer(event: TimerCallback | undefined): this--><!--Device-TextTimerAttribute-onTimer(event: TimerCallback | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [TimerCallback](arkts-timercallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## setTextTimerOptions

```TypeScript
setTextTimerOptions(options?: TextTimerOptions): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-TextTimerAttribute-setTextTimerOptions(options?: TextTimerOptions): this--><!--Device-TextTimerAttribute-setTextTimerOptions(options?: TextTimerOptions): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [TextTimerOptions](arkts-texttimer-texttimeroptions-i.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
## textShadow

```TypeScript
textShadow(value: ShadowOptions | Array<ShadowOptions> | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-TextTimerAttribute-textShadow(value: ShadowOptions | Array<ShadowOptions> | undefined): this--><!--Device-TextTimerAttribute-textShadow(value: ShadowOptions | Array<ShadowOptions> | undefined): this-End-->

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

Set TextTimer options.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextTimerAttribute-default--><!--Device-TextTimerAttribute-default-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

