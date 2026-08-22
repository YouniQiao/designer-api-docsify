# ImageAnimatorAttribute

Defines the ImageAnimator component attributes.

@extends CommonMethod @interface ImageAnimatorAttribute

**Inheritance/Implementation:** ImageAnimatorAttribute extends CommonMethod

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-unnamed-export declare interface ImageAnimatorAttribute--><!--Device-unnamed-export declare interface ImageAnimatorAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
attributeModifier(modifier: AttributeModifier<ImageAnimatorAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-ImageAnimatorAttribute-attributeModifier(modifier: AttributeModifier<ImageAnimatorAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-ImageAnimatorAttribute-attributeModifier(modifier: AttributeModifier<ImageAnimatorAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[ImageAnimatorAttribute](arkts-imageanimator-attribute.md)&gt; \| [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../../apis-arkui/arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## duration

```TypeScript
duration(value: int | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-ImageAnimatorAttribute-duration(value: int | undefined): this--><!--Device-ImageAnimatorAttribute-duration(value: int | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | int \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## fillMode

```TypeScript
fillMode(value: FillMode | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-ImageAnimatorAttribute-fillMode(value: FillMode | undefined): this--><!--Device-ImageAnimatorAttribute-fillMode(value: FillMode | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [FillMode](../../apis-arkui/arkts-apis/arkts-arkui-fillmode-e.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## fixedSize

```TypeScript
fixedSize(value: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-ImageAnimatorAttribute-fixedSize(value: boolean | undefined): this--><!--Device-ImageAnimatorAttribute-fixedSize(value: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## images

```TypeScript
images(value: Array<ImageFrameInfo> | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-ImageAnimatorAttribute-images(value: Array<ImageFrameInfo> | undefined): this--><!--Device-ImageAnimatorAttribute-images(value: Array<ImageFrameInfo> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | Array&lt;[ImageFrameInfo](arkts-imageanimator-imageframeinfo-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## iterations

```TypeScript
iterations(value: int | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-ImageAnimatorAttribute-iterations(value: int | undefined): this--><!--Device-ImageAnimatorAttribute-iterations(value: int | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | int \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## monitorInvisibleArea

```TypeScript
monitorInvisibleArea(monitorInvisibleArea: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-ImageAnimatorAttribute-monitorInvisibleArea(monitorInvisibleArea: boolean | undefined): this--><!--Device-ImageAnimatorAttribute-monitorInvisibleArea(monitorInvisibleArea: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| monitorInvisibleArea | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onCancel

```TypeScript
onCancel(event: (() => void) | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-ImageAnimatorAttribute-onCancel(event: (() => void) | undefined): this--><!--Device-ImageAnimatorAttribute-onCancel(event: (() => void) | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | (() =&gt; void) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onFinish

```TypeScript
onFinish(event: (() => void) | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-ImageAnimatorAttribute-onFinish(event: (() => void) | undefined): this--><!--Device-ImageAnimatorAttribute-onFinish(event: (() => void) | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | (() =&gt; void) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onPause

```TypeScript
onPause(event: (() => void) | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-ImageAnimatorAttribute-onPause(event: (() => void) | undefined): this--><!--Device-ImageAnimatorAttribute-onPause(event: (() => void) | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | (() =&gt; void) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onRepeat

```TypeScript
onRepeat(event: (() => void) | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-ImageAnimatorAttribute-onRepeat(event: (() => void) | undefined): this--><!--Device-ImageAnimatorAttribute-onRepeat(event: (() => void) | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | (() =&gt; void) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onStart

```TypeScript
onStart(event: (() => void) | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-ImageAnimatorAttribute-onStart(event: (() => void) | undefined): this--><!--Device-ImageAnimatorAttribute-onStart(event: (() => void) | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | (() =&gt; void) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## reverse

```TypeScript
reverse(value: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-ImageAnimatorAttribute-reverse(value: boolean | undefined): this--><!--Device-ImageAnimatorAttribute-reverse(value: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## setImageAnimatorOptions

```TypeScript
setImageAnimatorOptions(): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-ImageAnimatorAttribute-setImageAnimatorOptions(): this--><!--Device-ImageAnimatorAttribute-setImageAnimatorOptions(): this-End-->

**Return value:**

| Type | Description |
| --- | --- |
## state

```TypeScript
state(value: AnimationStatus | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-ImageAnimatorAttribute-state(value: AnimationStatus | undefined): this--><!--Device-ImageAnimatorAttribute-state(value: AnimationStatus | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [AnimationStatus](../../apis-arkui/arkts-apis/arkts-arkui-animationstatus-e.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## default

```TypeScript
default
```

Set the attribute modifier

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ImageAnimatorAttribute-default--><!--Device-ImageAnimatorAttribute-default-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

