# RenderOptions

RenderOptions info.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-unnamed-export interface RenderOptions--><!--Device-unnamed-export interface RenderOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## enableMinimized

```TypeScript
enableMinimized?: boolean
```

Indicates whether minimized mode is enabled. If this option is enabled, the FrameNode obtained through BuilderNode.getFrameNode() is a minimized FrameNode, which provide the smallest set of capabilities. Default value: false.

**Type:** boolean

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RenderOptions-enableMinimized?: boolean--><!--Device-RenderOptions-enableMinimized?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## selfIdealSize

```TypeScript
selfIdealSize?: Size
```

The ideal size of the node.

**Type:** [Size](arkts-graphics-size-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RenderOptions-selfIdealSize?: Size--><!--Device-RenderOptions-selfIdealSize?: Size-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## surfaceId

```TypeScript
surfaceId?: string
```

The surfaceId of a texture consumer.

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RenderOptions-surfaceId?: string--><!--Device-RenderOptions-surfaceId?: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## type

```TypeScript
type?: NodeRenderType
```

Render type of the node.

**Type:** [NodeRenderType](arkts-buildernode-noderendertype-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RenderOptions-type?: NodeRenderType--><!--Device-RenderOptions-type?: NodeRenderType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

