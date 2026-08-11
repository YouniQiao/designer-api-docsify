# PolygonAttribute

多边形绘制组件属性。

**继承/实现关系：** PolygonAttribute extends [CommonShapeMethod](arkts-arkui-arkui-shape-commonshapemethod-c.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-unnamed-export declare interface PolygonAttribute extends CommonShapeMethod--><!--Device-unnamed-export declare interface PolygonAttribute extends CommonShapeMethod-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<PolygonAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

调用attributeModifier。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PolygonAttribute-default attributeModifier(modifier: AttributeModifier<PolygonAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-PolygonAttribute-default attributeModifier(modifier: AttributeModifier<PolygonAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;PolygonAttribute&gt; \| AttributeModifier&lt;CommonMethod&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## points

```TypeScript
default points(value: Array<ShapePoint> | undefined): this
```

设置多边形的顶点坐标列表，支持[attributeModifier](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法。异常值按照默认值处理。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PolygonAttribute-default points(value: Array<ShapePoint> | undefined): this--><!--Device-PolygonAttribute-default points(value: Array<ShapePoint> | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Array&lt;ShapePoint&gt; \| undefined | 是 | 多边形的顶点坐标列表。使用时传入一个二维数组，每个子数组表示一个顶点的[x, y]坐标。 &lt;br/&gt;默认值：[]（空数组）&lt;br/&gt;默认单位：vp &lt;br/&gt;异常值undefined和null按照默认值处理。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## setPolygonOptions

```TypeScript
default setPolygonOptions(options?: PolygonOptions): this
```

设置Polygon构造参数。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PolygonAttribute-default setPolygonOptions(options?: PolygonOptions): this--><!--Device-PolygonAttribute-default setPolygonOptions(options?: PolygonOptions): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [PolygonOptions](arkts-arkui-polygon-polygonoptions-i.md) | 否 | Polygon绘制区域。&lt;br/&gt;异常值undefined和null按照无效值处理，本次设置不生效。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | 返回PolygonAttribute实例。 |

