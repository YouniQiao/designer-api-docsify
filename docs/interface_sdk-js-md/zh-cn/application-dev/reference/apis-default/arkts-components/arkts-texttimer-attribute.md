# TextTimerAttribute

除支持通用属性外，还支持以下属性。除支持通用事件外，还支持以下事件。

**继承/实现关系：** TextTimerAttribute extends CommonMethod

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-unnamed-export declare interface TextTimerAttribute--><!--Device-unnamed-export declare interface TextTimerAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
attributeModifier(modifier: AttributeModifier<TextTimerAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-TextTimerAttribute-attributeModifier(modifier: AttributeModifier<TextTimerAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-TextTimerAttribute-attributeModifier(modifier: AttributeModifier<TextTimerAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[TextTimerAttribute](arkts-texttimer-attribute.md)&gt; \| [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../../apis-arkui/arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## contentModifier

```TypeScript
contentModifier(modifier: ContentModifier<TextTimerConfiguration> | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-TextTimerAttribute-contentModifier(modifier: ContentModifier<TextTimerConfiguration> | undefined): this--><!--Device-TextTimerAttribute-contentModifier(modifier: ContentModifier<TextTimerConfiguration> | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | [ContentModifier](../../apis-arkui/arkts-components/arkts-arkui-contentmodifier-i.md)&lt;[TextTimerConfiguration](arkts-texttimer-texttimerconfiguration-i.md)&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## fontColor

```TypeScript
fontColor(value: ResourceColor | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-TextTimerAttribute-fontColor(value: ResourceColor | undefined): this--><!--Device-TextTimerAttribute-fontColor(value: ResourceColor | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](../../apis-arkui/arkts-apis/arkts-arkui-resourcecolor-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## fontFamily

```TypeScript
fontFamily(value: ResourceStr | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-TextTimerAttribute-fontFamily(value: ResourceStr | undefined): this--><!--Device-TextTimerAttribute-fontFamily(value: ResourceStr | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceStr](../../apis-arkui/arkts-apis/arkts-arkui-resourcestr-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## fontSize

```TypeScript
fontSize(value: Length | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-TextTimerAttribute-fontSize(value: Length | undefined): this--><!--Device-TextTimerAttribute-fontSize(value: Length | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Length](../../apis-arkui/arkts-apis/arkts-arkui-length-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## fontStyle

```TypeScript
fontStyle(value: FontStyle | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-TextTimerAttribute-fontStyle(value: FontStyle | undefined): this--><!--Device-TextTimerAttribute-fontStyle(value: FontStyle | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [FontStyle](../../apis-arkui/arkts-apis/arkts-arkui-fontstyle-e.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## fontWeight

```TypeScript
fontWeight(value: int | FontWeight | ResourceStr | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-TextTimerAttribute-fontWeight(value: int | FontWeight | ResourceStr | undefined): this--><!--Device-TextTimerAttribute-fontWeight(value: int | FontWeight | ResourceStr | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | int \| [FontWeight](../../apis-arkui/arkts-apis/arkts-arkui-fontweight-e.md) \| [ResourceStr](../../apis-arkui/arkts-apis/arkts-arkui-resourcestr-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## format

```TypeScript
format(value: string | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-TextTimerAttribute-format(value: string | undefined): this--><!--Device-TextTimerAttribute-format(value: string | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onTimer

```TypeScript
onTimer(event: TimerCallback | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-TextTimerAttribute-onTimer(event: TimerCallback | undefined): this--><!--Device-TextTimerAttribute-onTimer(event: TimerCallback | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [TimerCallback](arkts-timercallback-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## setTextTimerOptions

```TypeScript
setTextTimerOptions(options?: TextTimerOptions): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-TextTimerAttribute-setTextTimerOptions(options?: TextTimerOptions): this--><!--Device-TextTimerAttribute-setTextTimerOptions(options?: TextTimerOptions): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [TextTimerOptions](arkts-texttimer-texttimeroptions-i.md) | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## textShadow

```TypeScript
textShadow(value: ShadowOptions | Array<ShadowOptions> | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-TextTimerAttribute-textShadow(value: ShadowOptions | Array<ShadowOptions> | undefined): this--><!--Device-TextTimerAttribute-textShadow(value: ShadowOptions | Array<ShadowOptions> | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ShadowOptions](../../apis-arkui/arkts-components/arkts-arkui-shadowoptions-i.md) \| Array&lt;[ShadowOptions](../../apis-arkui/arkts-components/arkts-arkui-shadowoptions-i.md)&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## default

```TypeScript
default
```

设置TextTimer组件的选项。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-TextTimerAttribute-default--><!--Device-TextTimerAttribute-default-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

