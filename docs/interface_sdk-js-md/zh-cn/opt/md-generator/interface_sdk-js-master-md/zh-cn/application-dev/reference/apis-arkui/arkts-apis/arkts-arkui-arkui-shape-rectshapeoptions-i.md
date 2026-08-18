# RectShapeOptions(形状)

RectShape 的构造函数参数。 继承自[ShapeSize](arkts-arkui-arkui-shape-shapesize-i.md#shapesize)。

**继承/实现关系：** RectShapeOptions extends [ShapeSize](arkts-arkui-arkui-shape-shapesize-i.md#shapesize)

**起始版本：** 12

<!--Device-unnamed-interface RectShapeOptions--><!--Device-unnamed-interface RectShapeOptions-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## radius

```TypeScript
radius?: number | string | Array<number | string>
```

矩形形状的圆角半径。 类型为number时取值范围是[0, +∞)，string时是[Length](arkts-arkui-length-t.md#length)。 单位：vp 取值为异常值时按照0vp处理。

**类型：** number \| string \| Array&lt;number \| string&gt;

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

<!--Device-RectShapeOptions-radius?: number | string | Array<number | string>--><!--Device-RectShapeOptions-radius?: number | string | Array<number | string>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full
