# RichTextAttribute

定义RichText属性函数。

**继承/实现关系：** RichTextAttribute extends [CommonMethod](CommonMethod)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-unnamed-export declare interface RichTextAttribute extends CommonMethod--><!--Device-unnamed-export declare interface RichTextAttribute extends CommonMethod-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<RichTextAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

设置属性修饰符。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RichTextAttribute-default attributeModifier(modifier: AttributeModifier<RichTextAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-RichTextAttribute-default attributeModifier(modifier: AttributeModifier<RichTextAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[RichTextAttribute](arkts-arkui-richtext-richtextattribute-i.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## onComplete

```TypeScript
default onComplete(callback: (() => void) | undefined): this
```

当富文本加载结束时触发。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RichTextAttribute-default onComplete(callback: (() => void) | undefined): this--><!--Device-RichTextAttribute-default onComplete(callback: (() => void) | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | (() =&gt; void) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## onStart

```TypeScript
default onStart(callback: (() => void) | undefined): this
```

当富文本加载开始时触发。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RichTextAttribute-default onStart(callback: (() => void) | undefined): this--><!--Device-RichTextAttribute-default onStart(callback: (() => void) | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | (() =&gt; void) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

