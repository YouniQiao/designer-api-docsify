# RenderNode

提供自绘制渲染节点RenderNode，支持开发者通过C API进行开发，完成自定义绘制需求。RenderNode还支持渲染节点树管理（添加、删除、查询子节点）、背景色与不透明度等视觉属性设置、变换（缩放、旋转、平移、变换矩阵）、阴影 、边框、遮罩与裁剪、模糊效果等能力，适用于在Stage模型下进行自定义渲染与节点树管理的场景。

> **说明：**&gt;
> - 不建议对BuilderNode中的RenderNode进行修改操作。BuilderNode中持有的FrameNode仅用于将该
> BuilderNode作为子节点挂载到其他FrameNode上，对该FrameNode或对应的RenderNode进行属性设置与子节点操作可能会产生未定义行为，包括但不限于显示异常、事件异常、稳定性问题等。&gt;
> - RenderNode对象不支持使用JSON序列化。

**起始版本：** 11

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## appendChild

```TypeScript
appendChild(node: RenderNode): void
```

在RenderNode最后一个子节点后添加新的子节点。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| node | [RenderNode](arkts-arkui-rendernode-c.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [100025](../errorcode-node.md#100025-传入参数不符合要求) |

## clearChildren

```TypeScript
clearChildren(): void
```

清除当前RenderNode的所有子节点。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor()
```

RenderNode的构造函数。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## dispose

```TypeScript
dispose(): void
```

立即释放当前RenderNode。调用此方法后，RenderNode将解除与后端实体节点的引用关系，再次调用该节点的接口可能会出现crash或返回默认值。可通过 [isDisposed](#isdisposed)接口查询节点是否已释放。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## draw

```TypeScript
draw(context: DrawContext): void
```

绘制方法，需要开发者进行实现。该方法会在RenderNode进行绘制时被调用。该接口的[DrawContext](arkts-arkui-graphics-drawcontext-c.md)中的Canvas是用于记录指令的临时Canvas，并非节点的真实Canvas。使用请参见 [调整自定义绘制Canvas的变换矩阵](../../../ui/arkts-user-defined-arktsNode-renderNode.md#调整自定义绘制canvas的变换矩阵)。

> **说明：**&gt;
> RenderNode初始化时，会调用两次draw方法。第一次调用是在首次创建FrameNode时触发Render流程，第二次调用是在首次设置modifier时触发绘制。后续绘制流程皆由modifier触发。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [DrawContext](arkts-arkui-graphics-drawcontext-c.md) | 是 |

## getChild

```TypeScript
getChild(index: number): RenderNode | null
```

获取当前RenderNode指定位置的子节点。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | number | 是 |

**返回值：**

| 类型 |
| --- |
| [RenderNode](arkts-arkui-rendernode-c.md) \| null |

## getFirstChild

```TypeScript
getFirstChild(): RenderNode | null
```

获取当前RenderNode的第一个子节点。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [RenderNode](arkts-arkui-rendernode-c.md) \| null |

## getNextSibling

```TypeScript
getNextSibling(): RenderNode | null
```

获取当前RenderNode的下一个同级节点。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [RenderNode](arkts-arkui-rendernode-c.md) \| null |

## getPreviousSibling

```TypeScript
getPreviousSibling(): RenderNode | null
```

获取当前RenderNode的上一个同级节点。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [RenderNode](arkts-arkui-rendernode-c.md) \| null |

## insertChildAfter

```TypeScript
insertChildAfter(child: RenderNode, sibling: RenderNode | null): void
```

在RenderNode指定子节点之后添加新的子节点。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [child](../arkts-components/arkts-arkui-nestedscrollinfo-i.md) | [RenderNode](arkts-arkui-rendernode-c.md) | 是 |
| sibling | [RenderNode](arkts-arkui-rendernode-c.md) \| null | 是 |

**错误码：**

| 错误码ID |
| --- |
| [100025](../errorcode-node.md#100025-传入参数不符合要求) |

## invalidate

```TypeScript
invalidate(): void
```

该方法会触发RenderNode的重新渲染，重新渲染时会调用[draw](#draw)方法。若开发者继承了RenderNode并实现了draw方法，调用invalidate()后将重新执行draw方 法中的绘制逻辑。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## isDisposed

```TypeScript
isDisposed(): boolean
```

查询当前RenderNode对象是否已解除与后端实体节点的引用关系。当节点调用dispose接口后，再次调用其他接口可能会出现crash、返回默认值的情况，建议开发者在操作节点前调用此接口检查其有效性，避免潜在风险。

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| boolean |

## removeChild

```TypeScript
removeChild(node: RenderNode): void
```

从RenderNode中删除指定的子节点。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| node | [RenderNode](arkts-arkui-rendernode-c.md) | 是 |

## backgroundBlur

```TypeScript
get backgroundBlur(): BackgroundBlur
```

获取背景模糊效果。

**类型：** [BackgroundBlur](arkts-arkui-graphics-backgroundblur-i.md)

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## backgroundColor

```TypeScript
get backgroundColor(): number
```

获取当前RenderNode的背景颜色。

**类型：** number

**默认值：** 0X00000000 [since 11 - 11]

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## borderColor

```TypeScript
get borderColor(): Edges<number>
```

获取当前RenderNode的边框颜色。

**类型：** [Edges](arkts-arkui-graphics-edges-i.md)&lt;number&gt;

**默认值：** 0XFF000000

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## borderRadius

```TypeScript
get borderRadius(): BorderRadiuses
```

获取当前RenderNode的边框圆角。

**类型：** [BorderRadiuses](arkts-arkui-borderradiuses-t.md)

**默认值：** 0

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## borderStyle

```TypeScript
get borderStyle(): Edges<BorderStyle>
```

获取当前RenderNode的边框样式。

**类型：** [Edges](arkts-arkui-graphics-edges-i.md)&lt;[BorderStyle](arkts-arkui-borderstyle-e.md)&gt;

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## borderWidth

```TypeScript
get borderWidth(): Edges<number>
```

获取当前RenderNode的边框宽度。

**类型：** [Edges](arkts-arkui-graphics-edges-i.md)&lt;number&gt;

**默认值：** 0

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## clipToFrame

```TypeScript
get clipToFrame(): boolean
```

获取当前RenderNode是否需要进行剪裁。

**类型：** boolean

**默认值：** true [since 11 - 11]

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## contentBlur

```TypeScript
get contentBlur(): ContentBlur
```

背景模糊效果。默认值为{radius: 0}。

**类型：** [ContentBlur](arkts-arkui-graphics-contentblur-i.md)

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## foregroundBlur

```TypeScript
get foregroundBlur(): ForegroundBlur
```

获取内容模糊效果。

**类型：** [ForegroundBlur](arkts-arkui-graphics-foregroundblur-i.md)

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## frame

```TypeScript
get frame(): Frame
```

获取当前RenderNode的大小和位置。

**类型：** [Frame](arkts-arkui-graphics-frame-i.md)

**默认值：** Frame { x: 0, y: 0, width: 0, height: 0 } [since 11 - 11]

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## label

```TypeScript
get label(): string
```

获取当前RenderNode的标签。

**类型：** string

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## lengthMetricsUnit

```TypeScript
get lengthMetricsUnit(): LengthMetricsUnit
```

获取RenderNode各个属性使用的单位。

**类型：** [LengthMetricsUnit](arkts-arkui-graphics-lengthmetricsunit-e.md)

**默认值：** LengthMetricsUnit.DEFAULT

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## markNodeGroup

```TypeScript
get markNodeGroup(): boolean
```

获取当前节点是否标记了优先绘制。

**类型：** boolean

**默认值：** false

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## opacity

```TypeScript
get opacity(): number
```

获取当前RenderNode的不透明度。

**类型：** number

**默认值：** 1 [since 11 - 11]

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## pivot

```TypeScript
get pivot(): Pivot
```

获取当前RenderNode的轴心。

**类型：** [Pivot](arkts-arkui-pivot-t.md)

**默认值：** Pivot { x: 0.5, y: 0.5 } [since 11 - 11]

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## position

```TypeScript
get position(): Position
```

获取当前RenderNode的位置。

**类型：** [Position](arkts-arkui-position-t.md)

**默认值：** Position { x: 0, y: 0 } [since 11 - 11]

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## rotation

```TypeScript
get rotation(): Rotation
```

获取当前RenderNode的旋转角度。

**类型：** [Rotation](arkts-arkui-rotation-t.md)

**默认值：** Rotation { x: 0, y: 0, z: 0 } [since 11 - 11]

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## scale

```TypeScript
get scale(): Scale
```

获取当前RenderNode的缩放比例。

**类型：** [Scale](arkts-arkui-scale-t.md)

**默认值：** Scale { x: 1, y: 1 } [since 11 - 11]

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## shadowAlpha

```TypeScript
get shadowAlpha(): number
```

获取当前RenderNode的阴影颜色的Alpha值。

**类型：** number

**默认值：** 0 [since 11 - 11]

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## shadowColor

```TypeScript
get shadowColor(): number
```

获取当前RenderNode的阴影颜色。

**类型：** number

**默认值：** 0X00000000 [since 11 - 11]

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## shadowElevation

```TypeScript
get shadowElevation(): number
```

获取当前RenderNode的阴影的光照高度。

**类型：** number

**默认值：** 0 [since 11 - 11]

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## shadowOffset

```TypeScript
get shadowOffset(): Offset
```

获取当前RenderNode的阴影偏移。

**类型：** [Offset](arkts-arkui-offset-t.md)

**默认值：** Offset { x: 0, y: 0 } [since 11 - 11]

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## shadowRadius

```TypeScript
get shadowRadius(): number
```

获取当前RenderNode的阴影模糊半径。

**类型：** number

**默认值：** 0 [since 11 - 11]

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## shapeClip

```TypeScript
get shapeClip(): ShapeClip
```

获取当前RenderNode的裁剪形状。

**类型：** [ShapeClip](arkts-arkui-graphics-shapeclip-c.md)

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## shapeMask

```TypeScript
get shapeMask(): ShapeMask
```

获取当前RenderNode的遮罩。

**类型：** [ShapeMask](arkts-arkui-graphics-shapemask-c.md)

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## size

```TypeScript
get size(): Size
```

获取当前RenderNode的大小。

**类型：** Size

**默认值：** Size { width: 0, height: 0 } [since 11 - 11]

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## transform

```TypeScript
get transform(): Matrix4
```

获取当前RenderNode的变换矩阵。默认值为：  
```ts
[
 1, 0, 0, 0,
 0, 1, 0, 0,
 0, 0, 1, 0,
 0, 0, 0, 1
]
```

**类型：** [Matrix4](arkts-arkui-matrix4-t.md)

**默认值：** Matrix4 [ 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1 ] [since 11 - 11]

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## translation

```TypeScript
get translation(): Translation
```

获取当前RenderNode的平移量。

**类型：** [Translation](arkts-arkui-translation-t.md)

**默认值：** Translation { x: 0, y: 0 } [since 11 - 11]

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full
