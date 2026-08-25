# GridRowAttribute

The GridRowAttribute.@extends CommonMethod @interface GridRowAttribute

**继承/实现关系：** GridRowAttribute extends CommonMethod

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## alignItems

```TypeScript
default alignItems(value: ItemAlign | undefined): this
```

设置GridRow中的GridCol垂直主轴方向对齐方式。 GridCol本身也可通过alignSelf设置自身对齐方式。 当上述两种对齐方式都设置时，以GridCol自身设置为准。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ItemAlign](arkts-arkui-itemalign-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [GridRowAttribute](arkts-arkui-gridrow-gridrowattribute-i.md) |

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<GridRowAttribute> | AttributeModifier<CommonMethod>
        | undefined): this
```

设置组件的动态属性。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[GridRowAttribute](arkts-arkui-gridrow-gridrowattribute-i.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [GridRowAttribute](arkts-arkui-gridrow-gridrowattribute-i.md) |

## onBreakpointChange

```TypeScript
default onBreakpointChange(callback: ((breakpoints: string) => void) | undefined): this
```

断点发生变化时触发回调。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | ((breakpoints: string) = & gt; void) \ | undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [GridRowAttribute](arkts-arkui-gridrow-gridrowattribute-i.md) |

## setGridRowOptions

```TypeScript
default setGridRowOptions(options?: GridRowOptions): this
```

Set GridRow options.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [GridRowOptions](arkts-arkui-gridrow-gridrowoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [GridRowAttribute](arkts-arkui-gridrow-gridrowattribute-i.md) |
