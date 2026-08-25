# ScrollBarAttribute

除支持通用属性外，还支持以下属性：

**继承/实现关系：** ScrollBarAttribute extends CommonMethod

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<ScrollBarAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

动态设置ScrollBar组件的属性方法。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[ScrollBarAttribute](arkts-arkui-scrollbar-scrollbarattribute-i.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## enableNestedScroll

```TypeScript
default enableNestedScroll(enabled: boolean | undefined): this
```

设置滚动条是否嵌套滚动。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enabled | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## scrollBarColor

```TypeScript
default scrollBarColor(color: ColorMetrics | undefined): this
```

设置滚动条滑块的颜色，仅滚动条不放置子组件时生效。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| color | [ColorMetrics](arkts-arkui-graphics-colormetrics-c.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## setScrollBarOptions

```TypeScript
default setScrollBarOptions(value: ScrollBarOptions): this
```

设置滚动条选项。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ScrollBarOptions](arkts-arkui-scrollbar-scrollbaroptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [ScrollBarAttribute](arkts-arkui-scrollbar-scrollbarattribute-i.md) |
