# PatternLockAttribute

除支持通用属性外，还支持以下属性。除支持通用事件外，还支持以下事件。

**继承/实现关系：** PatternLockAttribute extends CommonMethod

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-unnamed-export declare interface PatternLockAttribute--><!--Device-unnamed-export declare interface PatternLockAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## activateCircleStyle

```TypeScript
activateCircleStyle(options: CircleStyleOptions | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-PatternLockAttribute-activateCircleStyle(options: CircleStyleOptions | undefined): this--><!--Device-PatternLockAttribute-activateCircleStyle(options: CircleStyleOptions | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [CircleStyleOptions](arkts-patternlock-circlestyleoptions-i.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## activeColor

```TypeScript
activeColor(value: ResourceColor | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-PatternLockAttribute-activeColor(value: ResourceColor | undefined): this--><!--Device-PatternLockAttribute-activeColor(value: ResourceColor | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](../../apis-arkui/arkts-apis/arkts-arkui-resourcecolor-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## attributeModifier

```TypeScript
attributeModifier(modifier: AttributeModifier<PatternLockAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-PatternLockAttribute-attributeModifier(modifier: AttributeModifier<PatternLockAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-PatternLockAttribute-attributeModifier(modifier: AttributeModifier<PatternLockAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[PatternLockAttribute](arkts-patternlock-attribute.md)&gt; \| [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../../apis-arkui/arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## autoReset

```TypeScript
autoReset(value: boolean | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-PatternLockAttribute-autoReset(value: boolean | undefined): this--><!--Device-PatternLockAttribute-autoReset(value: boolean | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## backgroundColor

```TypeScript
backgroundColor(value: ResourceColor | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-PatternLockAttribute-backgroundColor(value: ResourceColor | undefined): this--><!--Device-PatternLockAttribute-backgroundColor(value: ResourceColor | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](../../apis-arkui/arkts-apis/arkts-arkui-resourcecolor-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## circleRadius

```TypeScript
circleRadius(value: Length | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-PatternLockAttribute-circleRadius(value: Length | undefined): this--><!--Device-PatternLockAttribute-circleRadius(value: Length | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Length](../../apis-arkui/arkts-apis/arkts-arkui-length-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onDotConnect

```TypeScript
onDotConnect(callback: Callback<int> | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-PatternLockAttribute-onDotConnect(callback: Callback<int> | undefined): this--><!--Device-PatternLockAttribute-onDotConnect(callback: Callback<int> | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;int&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onPatternComplete

```TypeScript
onPatternComplete(callback: Callback<Array<int>> | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-PatternLockAttribute-onPatternComplete(callback: Callback<Array<int>> | undefined): this--><!--Device-PatternLockAttribute-onPatternComplete(callback: Callback<Array<int>> | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;Array&lt;int&gt;&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## pathColor

```TypeScript
pathColor(value: ResourceColor | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-PatternLockAttribute-pathColor(value: ResourceColor | undefined): this--><!--Device-PatternLockAttribute-pathColor(value: ResourceColor | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](../../apis-arkui/arkts-apis/arkts-arkui-resourcecolor-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## pathStrokeWidth

```TypeScript
pathStrokeWidth(value: double | string | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-PatternLockAttribute-pathStrokeWidth(value: double | string | undefined): this--><!--Device-PatternLockAttribute-pathStrokeWidth(value: double | string | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | double \| string \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## regularColor

```TypeScript
regularColor(value: ResourceColor | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-PatternLockAttribute-regularColor(value: ResourceColor | undefined): this--><!--Device-PatternLockAttribute-regularColor(value: ResourceColor | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](../../apis-arkui/arkts-apis/arkts-arkui-resourcecolor-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## selectedColor

```TypeScript
selectedColor(value: ResourceColor | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-PatternLockAttribute-selectedColor(value: ResourceColor | undefined): this--><!--Device-PatternLockAttribute-selectedColor(value: ResourceColor | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](../../apis-arkui/arkts-apis/arkts-arkui-resourcecolor-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## setPatternLockOptions

```TypeScript
setPatternLockOptions(controller?: PatternLockController): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-PatternLockAttribute-setPatternLockOptions(controller?: PatternLockController): this--><!--Device-PatternLockAttribute-setPatternLockOptions(controller?: PatternLockController): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| controller | [PatternLockController](arkts-patternlock-patternlockcontroller-c.md) | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## sideLength

```TypeScript
sideLength(value: Length | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-PatternLockAttribute-sideLength(value: Length | undefined): this--><!--Device-PatternLockAttribute-sideLength(value: Length | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Length](../../apis-arkui/arkts-apis/arkts-arkui-length-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## skipUnselectedPoint

```TypeScript
skipUnselectedPoint(skipped: boolean | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-PatternLockAttribute-skipUnselectedPoint(skipped: boolean | undefined): this--><!--Device-PatternLockAttribute-skipUnselectedPoint(skipped: boolean | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| skipped | boolean \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## default

```TypeScript
default
```

设置PatternLock组件选项。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PatternLockAttribute-default--><!--Device-PatternLockAttribute-default-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

