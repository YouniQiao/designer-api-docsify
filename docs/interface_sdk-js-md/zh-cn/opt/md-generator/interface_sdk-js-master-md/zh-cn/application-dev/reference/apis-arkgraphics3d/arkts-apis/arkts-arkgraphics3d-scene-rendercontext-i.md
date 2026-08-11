# RenderContext

渲染上下文，定义所有渲染资源的上下文。同一渲染上下文中的资源可在该上下文内创建的场景间共享。

**起始版本：** 20

<!--Device-unnamed-export interface RenderContext--><!--Device-unnamed-export interface RenderContext-End-->

**系统能力：** SystemCapability.ArkUi.Graphics3D

## getRenderResourceFactory

```TypeScript
getRenderResourceFactory() : RenderResourceFactory
```

获取资源工厂.

**起始版本：** 20

<!--Device-RenderContext-getRenderResourceFactory() : RenderResourceFactory--><!--Device-RenderContext-getRenderResourceFactory() : RenderResourceFactory-End-->

**系统能力：** SystemCapability.ArkUi.Graphics3D

**返回值：**

| 类型 |
| --- |
| [RenderResourceFactory](arkts-arkgraphics3d-scene-renderresourcefactory-i.md) |

## loadPlugin

```TypeScript
loadPlugin(name: string): Promise<boolean>
```

加载外部插件

**起始版本：** 20

<!--Device-RenderContext-loadPlugin(name: string): Promise<boolean>--><!--Device-RenderContext-loadPlugin(name: string): Promise<boolean>-End-->

**系统能力：** SystemCapability.ArkUi.Graphics3D

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;boolean&gt; |

## registerResourcePath

```TypeScript
registerResourcePath(protocol: string, uri: string): boolean
```

注册shader等资产文件所在的路径目录及其检索名，通过检索名查找并替换shader内部关联文件的路径描述，找到对应的资产路径目录，实现资产及其关联文件的正确加载。

**起始版本：** 20

<!--Device-RenderContext-registerResourcePath(protocol: string, uri: string): boolean--><!--Device-RenderContext-registerResourcePath(protocol: string, uri: string): boolean-End-->

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
