# ImageFrameNode

Define the Image type of FrameNode.

**Inheritance/Implementation:** ImageFrameNode extends TypedFrameNode<ImageAttribute>

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-typeNode-abstract class ImageFrameNode--><!--Device-typeNode-abstract class ImageFrameNode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## initialize

```TypeScript
abstract initialize(src: image.PixelMap | ResourceStr | DrawableDescriptor): ImageAttribute
```

Initialize Image FrameNode.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ImageFrameNode-abstract initialize(src: image.PixelMap | ResourceStr | DrawableDescriptor): ImageAttribute--><!--Device-ImageFrameNode-abstract initialize(src: image.PixelMap | ResourceStr | DrawableDescriptor): ImageAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| src | image.PixelMap \| ResourceStr \| [DrawableDescriptor](arkts-arkui-drawabledescriptor-drawabledescriptor-c.md) | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| ImageAttribute |  |

## initialize

```TypeScript
abstract initialize(src: image.PixelMap | ResourceStr | DrawableDescriptor | ImageContent): ImageAttribute
```

Initialize Image FrameNode.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ImageFrameNode-abstract initialize(src: image.PixelMap | ResourceStr | DrawableDescriptor | ImageContent): ImageAttribute--><!--Device-ImageFrameNode-abstract initialize(src: image.PixelMap | ResourceStr | DrawableDescriptor | ImageContent): ImageAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| src | image.PixelMap \| ResourceStr \| [DrawableDescriptor](arkts-arkui-drawabledescriptor-drawabledescriptor-c.md) \| ImageContent | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| ImageAttribute |  |

## initialize

```TypeScript
abstract initialize(src: image.PixelMap | ResourceStr | DrawableDescriptor, value: ImageAIOptions): ImageAttribute
```

Initialize Image FrameNode.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ImageFrameNode-abstract initialize(src: image.PixelMap | ResourceStr | DrawableDescriptor, value: ImageAIOptions): ImageAttribute--><!--Device-ImageFrameNode-abstract initialize(src: image.PixelMap | ResourceStr | DrawableDescriptor, value: ImageAIOptions): ImageAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| src | image.PixelMap \| ResourceStr \| [DrawableDescriptor](arkts-arkui-drawabledescriptor-drawabledescriptor-c.md) | Yes |  |
| value | ImageAIOptions | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| ImageAttribute |  |

