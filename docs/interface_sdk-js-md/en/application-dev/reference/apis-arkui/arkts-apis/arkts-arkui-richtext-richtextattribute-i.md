# RichTextAttribute

定义RichText属性函数。

**Inheritance/Implementation:** RichTextAttribute extends [CommonMethod](arkts-arkui-common-commonmethod-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface RichTextAttribute extends CommonMethod--><!--Device-unnamed-export declare interface RichTextAttribute extends CommonMethod-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<RichTextAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

设置属性修饰符。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RichTextAttribute-default attributeModifier(modifier: AttributeModifier<RichTextAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-RichTextAttribute-default attributeModifier(modifier: AttributeModifier<RichTextAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[RichTextAttribute](arkts-arkui-richtext-richtextattribute-i.md)&gt; \| AttributeModifier&lt;CommonMethod&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onComplete

```TypeScript
default onComplete(callback: (() => void) | undefined): this
```

当富文本加载结束时触发。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RichTextAttribute-default onComplete(callback: (() => void) | undefined): this--><!--Device-RichTextAttribute-default onComplete(callback: (() => void) | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | (() =&gt; void) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onStart

```TypeScript
default onStart(callback: (() => void) | undefined): this
```

当富文本加载开始时触发。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RichTextAttribute-default onStart(callback: (() => void) | undefined): this--><!--Device-RichTextAttribute-default onStart(callback: (() => void) | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | (() =&gt; void) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

