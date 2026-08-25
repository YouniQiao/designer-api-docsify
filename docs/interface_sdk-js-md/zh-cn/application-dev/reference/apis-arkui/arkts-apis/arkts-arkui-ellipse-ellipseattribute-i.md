# EllipseAttribute

椭圆绘制组件属性。 @extends CommonShapeMethod @interface EllipseAttribute

**继承/实现关系：** EllipseAttribute extends CommonShapeMethod

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<EllipseAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

调用attributeModifier。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[EllipseAttribute](arkts-arkui-ellipse-ellipseattribute-i.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [EllipseAttribute](arkts-arkui-ellipse-ellipseattribute-i.md) |

## setEllipseOptions

```TypeScript
default setEllipseOptions(options?: EllipseOptions): this
```

设置Ellipse构造参数。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [EllipseOptions](arkts-arkui-ellipse-ellipseoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [EllipseAttribute](arkts-arkui-ellipse-ellipseattribute-i.md) |
