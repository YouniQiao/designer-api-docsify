# RenderOptions

创建BuilderNode时的可选参数。

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## enableMinimized

```TypeScript
enableMinimized?: boolean
```

控制BuilderNode持有的FrameNode的类型，当此开关设置为true时，BuilderNode持有的FrameNode为轻量化的FrameNode，内存更小，但是不支持FrameNode的部分接口，具体信息请参见 [isMinimized](../../../reference/apis-arkui/js-apis-arkui-frameNode.md#isminimized)。 默认值：false。

**类型：** boolean

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## selfIdealSize

```TypeScript
selfIdealSize?: Size
```

节点的理想大小。当将BuilderNode生成的内容嵌入到其它RenderNode中显示时，需要显式指定selfIdealSize，否则Builder内的节点默认父组件布局约束为[0, 0]。默认值：{ width: 0, height: 0 }

**类型：** Size

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## surfaceId

```TypeScript
surfaceId?: string
```

纹理接收方的surfaceId。纹理接收方一般为 OH_NativeImage。surfaceId仅当type为NodeRenderType.RENDER_TYPE_TEXTURE时生效。默认值：""

**类型：** string

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## type

```TypeScript
type?: NodeRenderType
```

节点的渲染类型。当取值为NodeRenderType.RENDER_TYPE_TEXTURE时，仅在BuilderNode持有组件树的根节点为自定义组件时设置生效。默认值：NodeRenderType.RENDER_TYPE_DISPLAY

**类型：** [NodeRenderType](arkts-arkui-buildernode-noderendertype-e.md)

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full
