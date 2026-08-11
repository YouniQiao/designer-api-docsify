# LineAttribute

直线绘制组件属性。

**继承/实现关系：** LineAttribute extends [CommonShapeMethod](arkts-arkui-arkui-shape-commonshapemethod-c.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-unnamed-export declare interface LineAttribute extends CommonShapeMethod--><!--Device-unnamed-export declare interface LineAttribute extends CommonShapeMethod-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<LineAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

调用attributeModifier。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-LineAttribute-default attributeModifier(modifier: AttributeModifier<LineAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-LineAttribute-default attributeModifier(modifier: AttributeModifier<LineAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;LineAttribute&gt; \| AttributeModifier&lt;CommonMethod&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## endPoint

```TypeScript
default endPoint(value: ShapePoint | undefined): this
```

设置直线终点坐标点（相对坐标），支持[attributeModifier](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法，异常值按照默认值处理。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-LineAttribute-default endPoint(value: ShapePoint | undefined): this--><!--Device-LineAttribute-default endPoint(value: ShapePoint | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ShapePoint](arkts-arkui-shapepoint-t.md) \| undefined | 是 | 直线终点坐标点（相对坐标），单位vp。&lt;br/&gt;默认值：[0,&nbsp;0] &lt;br/&gt;异常值undefined和null按照默认值处理。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## setLineOptions

```TypeScript
default setLineOptions(options?: LineOptions): this
```

设置Line构造参数。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-LineAttribute-default setLineOptions(options?: LineOptions): this--><!--Device-LineAttribute-default setLineOptions(options?: LineOptions): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [LineOptions](../arkts-components/arkts-arkui-lineoptions-i.md) | 否 | Line绘制区域。&lt;br/&gt;异常值undefined和null按照无效值处理，本次设置不生效。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | 返回LineAttribute实例。 |

## startPoint

```TypeScript
default startPoint(value: ShapePoint | undefined): this
```

设置直线起点坐标点（相对坐标），支持[attributeModifier](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法，异常值按照默认值处理。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-LineAttribute-default startPoint(value: ShapePoint | undefined): this--><!--Device-LineAttribute-default startPoint(value: ShapePoint | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ShapePoint](arkts-arkui-shapepoint-t.md) \| undefined | 是 | 直线起点坐标点（相对坐标），单位vp。&lt;br/&gt;默认值：[0,&nbsp;0] &lt;br/&gt;异常值undefined和null按照默认值处理。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

