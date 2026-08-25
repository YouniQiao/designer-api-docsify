# RenderContext

定义了所有渲染资源的上下文。在同一渲染上下文中创建的多个场景之间，可以共享渲染资源。@interface RenderContext

**起始版本：** 20

**系统能力：** SystemCapability.ArkUi.Graphics3D

## getRenderResourceFactory

```TypeScript
getRenderResourceFactory() : RenderResourceFactory
```

获取渲染资源工厂，提供创建不同渲染资源的功能。

**起始版本：** 20

**系统能力：** SystemCapability.ArkUi.Graphics3D

**返回值：**

| 类型 |
| --- |
| [RenderResourceFactory](arkts-arkgraphics3d-scene-renderresourcefactory-i.md) |

## loadPlugin

```TypeScript
loadPlugin(name: string): Promise<boolean>
```

用于加载指定名称的插件，通过插件名称查找并加载对应的插件资源，使用Promise异步回调。

**起始版本：** 20

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

## registerResourcePath

```TypeScript
registerResourcePath(protocol: string, uri: string): boolean
```

注册shader等资产文件所在的路径目录及其检索名，通过检索名查找并替换shader内部关联文件的路径描述，找到对应的资产路径目录， 实现资产及其关联文件的正确加载。

**起始版本：** 20

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| protocol | string | 是 |
| uri | string | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |
