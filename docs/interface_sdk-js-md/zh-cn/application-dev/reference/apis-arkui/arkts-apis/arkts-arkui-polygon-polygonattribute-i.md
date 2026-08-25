# PolygonAttribute

多边形绘制组件属性。@extends CommonShapeMethod @interface PolygonAttribute

**继承/实现关系：** PolygonAttribute extends CommonShapeMethod

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<PolygonAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

调用attributeModifier。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[PolygonAttribute](arkts-arkui-polygon-polygonattribute-i.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [PolygonAttribute](arkts-arkui-polygon-polygonattribute-i.md) |

## points

```TypeScript
default points(value: Array<ShapePoint> | undefined): this
```

设置多边形的顶点坐标列表，支持attributeModifier动态设置属性方法。 异常值按照默认值处理。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | Array&lt;[ShapePoint](arkts-arkui-shapepoint-t.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [PolygonAttribute](arkts-arkui-polygon-polygonattribute-i.md) |

## setPolygonOptions

```TypeScript
default setPolygonOptions(options?: PolygonOptions): this
```

设置Polygon构造参数。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [PolygonOptions](arkts-arkui-polygon-polygonoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [PolygonAttribute](arkts-arkui-polygon-polygonattribute-i.md) |
