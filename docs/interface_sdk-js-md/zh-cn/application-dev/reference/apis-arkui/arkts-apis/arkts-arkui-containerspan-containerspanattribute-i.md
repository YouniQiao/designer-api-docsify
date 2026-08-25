# ContainerSpanAttribute

仅支持以下属性：

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## applyAttributesFinish

```TypeScript
default applyAttributesFinish(): void
```

通知组件已完成其属性的设置。

**起始版本：** 26.1.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.1.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<ContainerSpanAttribute> | undefined): this
```

设置组件的动态属性。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[ContainerSpanAttribute](arkts-arkui-containerspan-containerspanattribute-i.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [ContainerSpanAttribute](arkts-arkui-containerspan-containerspanattribute-i.md) |

## debugLine

```TypeScript
default debugLine(sourceLine: string, moduleName?: string): this
```

设置组件源码重定向信息。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sourceLine | string | 是 |
| moduleName | string | 否 |

**返回值：**

| 类型 |
| --- |
| this |

## setContainerSpanOptions

```TypeScript
default setContainerSpanOptions(): this
```

设置ContainerSpan选项。

**起始版本：** 26.1.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.1.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [ContainerSpanAttribute](arkts-arkui-containerspan-containerspanattribute-i.md) |

## textBackgroundStyle

```TypeScript
default textBackgroundStyle(style: TextBackgroundStyle | undefined): this
```

设置文本背景样式。子组件在不设置该属性时，将继承此属性值。

> **说明：**&gt;
> 从API version 12开始，该接口支持在
> attributeModifier
> 中调用。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| style | [TextBackgroundStyle](../arkts-components/arkts-arkui-textbackgroundstyle-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [ContainerSpanAttribute](arkts-arkui-containerspan-containerspanattribute-i.md) |
