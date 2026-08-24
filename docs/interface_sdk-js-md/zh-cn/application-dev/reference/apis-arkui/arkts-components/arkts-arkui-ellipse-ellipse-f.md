# Ellipse

## Ellipse

```TypeScript
@ComponentBuilder
export declare function Ellipse(
    options?: EllipseOptions
): EllipseAttribute
```

用于绘制椭圆的构造函数。

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**装饰器类型：** @ComponentBuilder

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-@ComponentBuilderexport declare function Ellipse(    options?: EllipseOptions): EllipseAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function Ellipse(    options?: EllipseOptions): EllipseAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [EllipseOptions](arkts-arkui-ellipse-ellipseoptions-i.md) | 否 | 椭圆绘制尺寸。<br/>异常值undefined和null按照无效值处理，本次设置不生效。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [EllipseAttribute](arkts-arkui-ellipse-attribute.md) | 椭圆的属性。 |


## Ellipse

```TypeScript
@Builder
export declare function Ellipse(
    style: CustomBuilderT<EllipseAttribute>
): EllipseAttribute
```

定义Ellipse组件。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**装饰器类型：** @Builder

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-@Builderexport declare function Ellipse(    style: CustomBuilderT<EllipseAttribute>): EllipseAttribute--><!--Device-unnamed-@Builderexport declare function Ellipse(    style: CustomBuilderT<EllipseAttribute>): EllipseAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style | [CustomBuilderT](../../apis-default/arkts-apis/arkts-custombuildert-t.md)&lt;[EllipseAttribute](arkts-arkui-ellipse-attribute.md)&gt; | 是 | 设置组件属性的回调。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [EllipseAttribute](arkts-arkui-ellipse-attribute.md) |  |

