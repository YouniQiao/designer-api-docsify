# RichTextAttribute

定义RichText属性函数。

**继承/实现关系：** RichTextAttribute extends CommonMethod

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<RichTextAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

设置属性修饰符。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[RichTextAttribute](arkts-arkui-richtext-richtextattribute-i.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [RichTextAttribute](arkts-arkui-richtext-richtextattribute-i.md) |

## onComplete

```TypeScript
default onComplete(callback: (() => void) | undefined): this
```

当富文本加载结束时触发。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | (() = & gt; void) \ | undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [RichTextAttribute](arkts-arkui-richtext-richtextattribute-i.md) |

## onStart

```TypeScript
default onStart(callback: (() => void) | undefined): this
```

当富文本加载开始时触发。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | (() = & gt; void) \ | undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [RichTextAttribute](arkts-arkui-richtext-richtextattribute-i.md) |
