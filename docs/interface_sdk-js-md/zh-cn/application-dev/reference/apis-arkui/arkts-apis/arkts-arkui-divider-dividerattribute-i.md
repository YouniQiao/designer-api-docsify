# DividerAttribute

The DividerAttribute.@extends CommonMethod @interface DividerAttribute

**继承/实现关系：** DividerAttribute extends CommonMethod

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<DividerAttribute>
        | AttributeModifier<CommonMethod> | undefined): this
```

设置组件的动态属性。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[DividerAttribute](arkts-arkui-divider-dividerattribute-i.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [DividerAttribute](arkts-arkui-divider-dividerattribute-i.md) |

## color

```TypeScript
default color(value: ResourceColor | undefined): this
```

设置分割线的颜色，支持 attributeModifier 动态设置属性方法。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [DividerAttribute](arkts-arkui-divider-dividerattribute-i.md) |

## lineCap

```TypeScript
default lineCap(value: LineCapStyle | undefined): this
```

设置分割线的端点样式，支持 attributeModifier 动态设置属性方法。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [LineCapStyle](arkts-arkui-linecapstyle-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [DividerAttribute](arkts-arkui-divider-dividerattribute-i.md) |

## setDividerOptions

```TypeScript
default setDividerOptions(): this
```

Set Divider options.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [DividerAttribute](arkts-arkui-divider-dividerattribute-i.md) |

## strokeWidth

```TypeScript
default strokeWidth(value: double | string | undefined): this
```

设置分割线的宽度，支持 attributeModifier 动态设置属性方法。

> **说明：**&gt;
> 分割线的宽度不支持百分比设置。
> 使用水平分割线时，strokeWidth控制高度，优先级低于通用属性
> height；
> 使用垂直分割线时，strokeWidth控制宽度，优先级低于通用属性
> width。
> 超过通用属性设置大小时，按照通用属性进行裁切。
> 如果设备硬件存在1像素取整后分割线不显示问题，建议使用2像素。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | double \| string \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [DividerAttribute](arkts-arkui-divider-dividerattribute-i.md) |

## vertical

```TypeScript
default vertical(value: boolean | undefined): this
```

设置分割线的方向，支持 attributeModifier 动态设置属性方法。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [DividerAttribute](arkts-arkui-divider-dividerattribute-i.md) |
