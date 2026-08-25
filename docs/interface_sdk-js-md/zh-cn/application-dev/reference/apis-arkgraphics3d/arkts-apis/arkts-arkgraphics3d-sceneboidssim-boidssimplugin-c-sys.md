# BoidsSimPlugin（系统接口）

群组模拟插件，提供静态方法用于获取群组模拟世界。

**起始版本：** 26.0.0

**系统能力：** SystemCapability.ArkUi.Graphics3D

**系统接口：** 此接口为系统接口。

## getDefaultBoidsSimWorld

```TypeScript
static getDefaultBoidsSimWorld(scene: Scene): BoidsSimWorld | null
```

获取与指定场景关联的群组模拟世界实例。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| scene | [Scene](arkts-arkgraphics3d-scene-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [BoidsSimWorld](arkts-arkgraphics3d-sceneboidssim-boidssimworld-c-sys.md) \| null |
