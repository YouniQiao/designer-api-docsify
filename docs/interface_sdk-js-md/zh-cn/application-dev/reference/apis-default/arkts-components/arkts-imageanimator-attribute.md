# ImageAnimatorAttribute

除支持通用属性外，还支持以下属性：

除支持通用事件外，还支持以下事件：

@extends CommonMethod @interface ImageAnimatorAttribute

**继承/实现关系：** ImageAnimatorAttribute extends CommonMethod

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-unnamed-export declare interface ImageAnimatorAttribute--><!--Device-unnamed-export declare interface ImageAnimatorAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
attributeModifier(
    modifier: AttributeModifier<ImageAnimatorAttribute> | AttributeModifier<CommonMethod> | undefined
  ): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-ImageAnimatorAttribute-attributeModifier(    modifier: AttributeModifier<ImageAnimatorAttribute> | AttributeModifier<CommonMethod> | undefined  ): this--><!--Device-ImageAnimatorAttribute-attributeModifier(    modifier: AttributeModifier<ImageAnimatorAttribute> | AttributeModifier<CommonMethod> | undefined  ): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[ImageAnimatorAttribute](arkts-imageanimator-attribute.md)&gt; \| [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../../apis-arkui/arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## duration

```TypeScript
duration(value: int | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-ImageAnimatorAttribute-duration(value: int | undefined): this--><!--Device-ImageAnimatorAttribute-duration(value: int | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | int \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## fillMode

```TypeScript
fillMode(value: FillMode | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-ImageAnimatorAttribute-fillMode(value: FillMode | undefined): this--><!--Device-ImageAnimatorAttribute-fillMode(value: FillMode | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [FillMode](../../apis-arkui/arkts-apis/arkts-arkui-fillmode-e.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## fixedSize

```TypeScript
fixedSize(value: boolean | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-ImageAnimatorAttribute-fixedSize(value: boolean | undefined): this--><!--Device-ImageAnimatorAttribute-fixedSize(value: boolean | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## images

```TypeScript
images(value: Array<ImageFrameInfo> | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-ImageAnimatorAttribute-images(value: Array<ImageFrameInfo> | undefined): this--><!--Device-ImageAnimatorAttribute-images(value: Array<ImageFrameInfo> | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Array&lt;[ImageFrameInfo](arkts-imageanimator-imageframeinfo-i.md)&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## iterations

```TypeScript
iterations(value: int | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-ImageAnimatorAttribute-iterations(value: int | undefined): this--><!--Device-ImageAnimatorAttribute-iterations(value: int | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | int \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## monitorInvisibleArea

```TypeScript
monitorInvisibleArea(monitorInvisibleArea: boolean | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-ImageAnimatorAttribute-monitorInvisibleArea(monitorInvisibleArea: boolean | undefined): this--><!--Device-ImageAnimatorAttribute-monitorInvisibleArea(monitorInvisibleArea: boolean | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| monitorInvisibleArea | boolean \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onCancel

```TypeScript
onCancel(event: (() => void) | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-ImageAnimatorAttribute-onCancel(event: (() => void) | undefined): this--><!--Device-ImageAnimatorAttribute-onCancel(event: (() => void) | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | (() =&gt; void) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onFinish

```TypeScript
onFinish(event: (() => void) | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-ImageAnimatorAttribute-onFinish(event: (() => void) | undefined): this--><!--Device-ImageAnimatorAttribute-onFinish(event: (() => void) | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | (() =&gt; void) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onPause

```TypeScript
onPause(event: (() => void) | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-ImageAnimatorAttribute-onPause(event: (() => void) | undefined): this--><!--Device-ImageAnimatorAttribute-onPause(event: (() => void) | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | (() =&gt; void) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onRepeat

```TypeScript
onRepeat(event: (() => void) | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-ImageAnimatorAttribute-onRepeat(event: (() => void) | undefined): this--><!--Device-ImageAnimatorAttribute-onRepeat(event: (() => void) | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | (() =&gt; void) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onStart

```TypeScript
onStart(event: (() => void) | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-ImageAnimatorAttribute-onStart(event: (() => void) | undefined): this--><!--Device-ImageAnimatorAttribute-onStart(event: (() => void) | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | (() =&gt; void) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## reverse

```TypeScript
reverse(value: boolean | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-ImageAnimatorAttribute-reverse(value: boolean | undefined): this--><!--Device-ImageAnimatorAttribute-reverse(value: boolean | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## setImageAnimatorOptions

```TypeScript
setImageAnimatorOptions(): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-ImageAnimatorAttribute-setImageAnimatorOptions(): this--><!--Device-ImageAnimatorAttribute-setImageAnimatorOptions(): this-End-->

**返回值：**

| 类型 | 说明 |
| --- | --- |
## state

```TypeScript
state(value: AnimationStatus | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-ImageAnimatorAttribute-state(value: AnimationStatus | undefined): this--><!--Device-ImageAnimatorAttribute-state(value: AnimationStatus | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [AnimationStatus](../../apis-arkui/arkts-apis/arkts-arkui-animationstatus-e.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## default

```TypeScript
default
```

Set the attribute modifier

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ImageAnimatorAttribute-default--><!--Device-ImageAnimatorAttribute-default-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

