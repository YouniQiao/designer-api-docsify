# Camera

相机类型，Camera继承自Node。@extends Node @interface Camera

**继承/实现关系：** Camera extends [Node](arkts-arkgraphics3d-scenenodes-node-i.md)

**起始版本：** 12

**系统能力：** SystemCapability.ArkUi.Graphics3D

## getProjectionMatrix

```TypeScript
getProjectionMatrix(): Mat4x4
```

获取相机的投影矩阵。

**起始版本：** 23

**系统能力：** SystemCapability.ArkUi.Graphics3D

**返回值：**

| 类型 |
| --- |
| [Mat4x4](arkts-arkgraphics3d-scenetypes-mat4x4-i.md) |

## getViewMatrix

```TypeScript
getViewMatrix(): Mat4x4
```

获取相机的视图矩阵。

**起始版本：** 23

**系统能力：** SystemCapability.ArkUi.Graphics3D

**返回值：**

| 类型 |
| --- |
| [Mat4x4](arkts-arkgraphics3d-scenetypes-mat4x4-i.md) |

## raycast

```TypeScript
raycast(viewPosition: Vec2, params: RaycastParameters): Promise<RaycastResult[]>
```

从屏幕指定位置发射射线，检测并返回所有命中的3D物体信息。使用Promise异步回调。

**起始版本：** 20

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| viewPosition | [Vec2](arkts-arkgraphics3d-scenetypes-vec2-i.md) | 是 |
| params | [RaycastParameters](arkts-arkgraphics3d-scene-raycastparameters-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[RaycastResult](arkts-arkgraphics3d-scene-raycastresult-i.md)[]&gt; |

## clearColor

```TypeScript
clearColor: Color | null
```

将渲染目标（render target）清空后的特定颜色。

**类型：** [Color](arkts-arkgraphics3d-scenetypes-color-i.md) \| null

**起始版本：** 12

**系统能力：** SystemCapability.ArkUi.Graphics3D

## effects

```TypeScript
readonly effects: Container<Effect>
```

应用于相机输出的后处理特效。

**类型：** [Container](arkts-arkgraphics3d-scenenodes-container-i.md)&lt;[Effect](arkts-arkgraphics3d-sceneresources-effect-i.md)&gt;

**起始版本：** 21

**系统能力：** SystemCapability.ArkUi.Graphics3D

## enabled

```TypeScript
enabled: boolean
```

是否使能相机。true表示使用相机，false表示不使用相机。

**类型：** boolean

**起始版本：** 12

**系统能力：** SystemCapability.ArkUi.Graphics3D

## farPlane

```TypeScript
farPlane: number
```

远平面，单位为世界坐标系下的场景单位（比如cm、m、km等），取值大于nearPlane。

**类型：** number

**起始版本：** 12

**系统能力：** SystemCapability.ArkUi.Graphics3D

## fov

```TypeScript
fov: number
```

视场，单位为弧度（rad），取值范围为(0, π)。

**类型：** number

**起始版本：** 12

**系统能力：** SystemCapability.ArkUi.Graphics3D

## msaa

```TypeScript
msaa?: boolean
```

控制MSAA是否使能。true表示使能MSAA，false表示不使能MSAA。若未设置，默认为false。

**类型：** boolean

**默认值：** false

**起始版本：** 22

**系统能力：** SystemCapability.ArkUi.Graphics3D

## nearPlane

```TypeScript
nearPlane: number
```

近平面，单位为世界坐标系下的场景单位（比如cm、m、km等），取值大于0。

**类型：** number

**起始版本：** 12

**系统能力：** SystemCapability.ArkUi.Graphics3D

## postProcess

```TypeScript
postProcess: PostProcessSettings | null
```

后处理设置。

**类型：** [PostProcessSettings](arkts-arkgraphics3d-scenepostprocesssettings-postprocesssettings-i.md) \| null

**起始版本：** 12

**系统能力：** SystemCapability.ArkUi.Graphics3D

## renderingPipeline

```TypeScript
renderingPipeline?: RenderingPipelineType
```

控制渲染管线。若未设置，默认使用轻量级前向渲染管线。（如果选择了FORWARD_LIGHTWEIGHT管线，某些功能将不可用。）

**类型：** [RenderingPipelineType](arkts-arkgraphics3d-scenetypes-renderingpipelinetype-e.md)

**默认值：** RenderingPipelineType.FORWARD_LIGHTWEIGHT

**起始版本：** 21

**系统能力：** SystemCapability.ArkUi.Graphics3D
