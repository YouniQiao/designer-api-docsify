# RenderOptions

创建BuilderNode时的可选参数。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export interface RenderOptions--><!--Device-unnamed-export interface RenderOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## enableMinimized

```TypeScript
enableMinimized?: boolean
```

控制BuilderNode持有的FrameNode的类型，当此开关设置为true时，BuilderNode持有的FrameNode为轻量化的FrameNode，内存更小，但是不支持FrameNode的部分接口，具体信息请参见  
[isMinimized](../../../reference/apis-arkui/js-apis-arkui-frameNode.md#isminimized)。默认值：false。

**Type:** boolean

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RenderOptions-enableMinimized?: boolean--><!--Device-RenderOptions-enableMinimized?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## selfIdealSize

```TypeScript
selfIdealSize?: Size
```

节点的理想大小。

默认值：{ width: 0, height: 0 }

**Type:** [Size](arkts-arkui-graphics-size-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RenderOptions-selfIdealSize?: Size--><!--Device-RenderOptions-selfIdealSize?: Size-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## surfaceId

```TypeScript
surfaceId?: string
```

纹理接收方的surfaceId。纹理接收方一般为  
[OH_NativeImage](../../../reference/apis-arkgraphics2d/capi-oh-nativeimage-oh-nativeimage.md)。

surfaceId仅当type为NodeRenderType.RENDER_TYPE_TEXTURE时生效。

默认值：""

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RenderOptions-surfaceId?: string--><!--Device-RenderOptions-surfaceId?: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## type

```TypeScript
type?: NodeRenderType
```

节点的渲染类型。

默认值：NodeRenderType.RENDER_TYPE_DISPLAY

**Type:** [NodeRenderType](arkts-arkui-buildernode-noderendertype-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RenderOptions-type?: NodeRenderType--><!--Device-RenderOptions-type?: NodeRenderType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

