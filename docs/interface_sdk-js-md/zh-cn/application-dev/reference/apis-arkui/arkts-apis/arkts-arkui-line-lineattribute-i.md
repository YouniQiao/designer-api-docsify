# LineAttribute

直线绘制组件属性。@extends CommonShapeMethod @interface LineAttribute

**继承/实现关系：** LineAttribute extends CommonShapeMethod

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<LineAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

调用attributeModifier。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[LineAttribute](arkts-arkui-line-lineattribute-i.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [LineAttribute](arkts-arkui-line-lineattribute-i.md) |

## endPoint

```TypeScript
default endPoint(value: ShapePoint | undefined): this
```

设置直线终点坐标点（相对坐标），支持attributeModifier动态设置属性方法， 异常值按照默认值处理。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ShapePoint](arkts-arkui-shapepoint-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [LineAttribute](arkts-arkui-line-lineattribute-i.md) |

## setLineOptions

```TypeScript
default setLineOptions(options?: LineOptions): this
```

设置Line构造参数。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [LineOptions](arkts-arkui-line-lineoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [LineAttribute](arkts-arkui-line-lineattribute-i.md) |

## startPoint

```TypeScript
default startPoint(value: ShapePoint | undefined): this
```

设置直线起点坐标点（相对坐标），支持attributeModifier动态设置属性方法， 异常值按照默认值处理。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ShapePoint](arkts-arkui-shapepoint-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [LineAttribute](arkts-arkui-line-lineattribute-i.md) |
