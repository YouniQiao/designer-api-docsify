# Scene

用于设置场景。Scene采用树状层次结构组织场景节点，根节点（root）作为场景的入口。

**起始版本：** 12

**系统能力：** SystemCapability.ArkUi.Graphics3D

## load

```TypeScript
static load(uri: ResourceStr, param: SceneLoadParams):Promise<Scene>
```

根据指定的资源路径和场景加载参数加载资源，使用Promise异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUi.Graphics3D

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | [ResourceStr](../../apis-arkui/arkts-apis/arkts-arkui-resourcestr-t.md) | 是 |
| param | [SceneLoadParams](arkts-arkgraphics3d-scene-sceneloadparams-i-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[Scene](arkts-arkgraphics3d-scene-c.md)&gt; |
