# SymbolSpanAttribute

SymbolSpan组件定义

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
default attributeModifier(modifier: AttributeModifier<SymbolSpanAttribute> | undefined): this
```

设置modifier属性

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[SymbolSpanAttribute](arkts-arkui-symbolspan-symbolspanattribute-i.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SymbolSpanAttribute](arkts-arkui-symbolspan-symbolspanattribute-i.md) |

## debugLine

```TypeScript
default debugLine(sourceLine: string, moduleName?: string): this
```

设置组件的源码跳转信息。

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

## effectStrategy

```TypeScript
default effectStrategy(value: SymbolEffectStrategy | undefined): this
```

Called when the SymbolSpan effect is set.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [SymbolEffectStrategy](../arkts-components/arkts-arkui-symboleffectstrategy-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SymbolSpanAttribute](arkts-arkui-symbolspan-symbolspanattribute-i.md) |

## fontColor

```TypeScript
default fontColor(value: Array<ResourceColor> | undefined): this
```

Called when the SymbolSpan color is set.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | Array&lt;[ResourceColor](arkts-arkui-resourcecolor-t.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SymbolSpanAttribute](arkts-arkui-symbolspan-symbolspanattribute-i.md) |

## fontSize

```TypeScript
default fontSize(value: double | string | Resource | undefined): this
```

Called when the SymbolSpan size is set.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | double \| string \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SymbolSpanAttribute](arkts-arkui-symbolspan-symbolspanattribute-i.md) |

## fontWeight

```TypeScript
default fontWeight(value: int | FontWeight | string | undefined): this
```

设置字体fontWeight属性

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | int \| [FontWeight](arkts-arkui-fontweight-e.md) \| string \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SymbolSpanAttribute](arkts-arkui-symbolspan-symbolspanattribute-i.md) |

## fontWeight

```TypeScript
default fontWeight(value: int | FontWeight | ResourceStr | undefined, fontWeightConfigs?: FontWeightConfigs): this
```

设置SymbolSpan的字体粗细。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | int \| [FontWeight](arkts-arkui-fontweight-e.md) \| [ResourceStr](arkts-arkui-resourcestr-t.md) \| undefined | 是 |
| fontWeightConfigs | [FontWeightConfigs](arkts-arkui-textcommon-fontweightconfigs-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [SymbolSpanAttribute](arkts-arkui-symbolspan-symbolspanattribute-i.md) |

## id

```TypeScript
default id(value: string | undefined): this
```

Id. User can set an id to the component to identify it.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | string \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## key

```TypeScript
default key(value: string | undefined): this
```

Key. User can set an key to the component to identify it.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | string \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## renderingStrategy

```TypeScript
default renderingStrategy(value: SymbolRenderingStrategy | undefined): this
```

Called when the SymbolSpan rendering strategy is set.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [SymbolRenderingStrategy](../arkts-components/arkts-arkui-symbolrenderingstrategy-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SymbolSpanAttribute](arkts-arkui-symbolspan-symbolspanattribute-i.md) |

## setSymbolSpanOptions

```TypeScript
default setSymbolSpanOptions(value: Resource): this
```

设置SymbolSpan组件选项。

**起始版本：** 26.1.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.1.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [SymbolSpanAttribute](arkts-arkui-symbolspan-symbolspanattribute-i.md) |
