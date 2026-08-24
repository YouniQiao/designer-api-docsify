# CounterAttribute

除支持通用属性外，还支持以下属性。除支持通用事件外，还支持以下事件。

**继承/实现关系：** CounterAttribute extends CommonMethod

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-unnamed-export declare interface CounterAttribute--><!--Device-unnamed-export declare interface CounterAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
attributeModifier(modifier: AttributeModifier<CounterAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-CounterAttribute-attributeModifier(modifier: AttributeModifier<CounterAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-CounterAttribute-attributeModifier(modifier: AttributeModifier<CounterAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CounterAttribute](arkts-counter-attribute.md)&gt; \| [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../../apis-arkui/arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## enableDec

```TypeScript
enableDec(value: boolean | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-CounterAttribute-enableDec(value: boolean | undefined): this--><!--Device-CounterAttribute-enableDec(value: boolean | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## enableInc

```TypeScript
enableInc(value: boolean | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-CounterAttribute-enableInc(value: boolean | undefined): this--><!--Device-CounterAttribute-enableInc(value: boolean | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onDec

```TypeScript
onDec(event: VoidCallback | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-CounterAttribute-onDec(event: VoidCallback | undefined): this--><!--Device-CounterAttribute-onDec(event: VoidCallback | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [VoidCallback](../../apis-arkui/arkts-apis/arkts-arkui-voidcallback-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onInc

```TypeScript
onInc(event: VoidCallback | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-CounterAttribute-onInc(event: VoidCallback | undefined): this--><!--Device-CounterAttribute-onInc(event: VoidCallback | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [VoidCallback](../../apis-arkui/arkts-apis/arkts-arkui-voidcallback-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## setCounterOptions

```TypeScript
setCounterOptions(): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-CounterAttribute-setCounterOptions(): this--><!--Device-CounterAttribute-setCounterOptions(): this-End-->

**返回值：**

| 类型 | 说明 |
| --- | --- |
## default

```TypeScript
default
```

设置Counter选项。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CounterAttribute-default--><!--Device-CounterAttribute-default-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

