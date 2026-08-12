# RectShape

用于clipShape和maskShape接口的矩形形状。

继承自[BaseShape](arkts-arkui-arkui-shape-baseshape-c.md#BaseShape)。

**继承/实现关系：** RectShape extends [BaseShape<RectShape>](BaseShape<RectShape>)

**起始版本：** 12

<!--Device-unnamed-export declare class RectShape extends BaseShape<RectShape>--><!--Device-unnamed-export declare class RectShape extends BaseShape<RectShape>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(options?: RectShapeOptions | RoundRectShapeOptions)
```

创建RectShape对象。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

<!--Device-RectShape-constructor(options?: RectShapeOptions | RoundRectShapeOptions)--><!--Device-RectShape-constructor(options?: RectShapeOptions | RoundRectShapeOptions)-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [RectShapeOptions](arkts-arkui-arkui-shape-rectshapeoptions-i.md) \| [RoundRectShapeOptions](arkts-arkui-arkui-shape-roundrectshapeoptions-i.md) | 否 |

## radius

```TypeScript
radius(radius: number | string | Array<number | string>): RectShape
```

设置矩形形状的圆角半径。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

<!--Device-RectShape-radius(radius: number | string | Array<number | string>): RectShape--><!--Device-RectShape-radius(radius: number | string | Array<number | string>): RectShape-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [radius](#radius) | number \| string \| Array & lt;number \ | string & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| [RectShape](arkts-arkui-arkui-shape-rectshape-c.md) |

## radiusHeight

```TypeScript
radiusHeight(rHeight: number | string): RectShape
```

设置矩形形状圆角半径的高度。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

<!--Device-RectShape-radiusHeight(rHeight: number | string): RectShape--><!--Device-RectShape-radiusHeight(rHeight: number | string): RectShape-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| rHeight | number \| string | 是 |

**返回值：**

| 类型 |
| --- |
| [RectShape](arkts-arkui-arkui-shape-rectshape-c.md) |

## radiusWidth

```TypeScript
radiusWidth(rWidth: number | string): RectShape
```

设置矩形形状圆角半径的宽度。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

<!--Device-RectShape-radiusWidth(rWidth: number | string): RectShape--><!--Device-RectShape-radiusWidth(rWidth: number | string): RectShape-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| rWidth | number \| string | 是 |

**返回值：**

| 类型 |
| --- |
| [RectShape](arkts-arkui-arkui-shape-rectshape-c.md) |
