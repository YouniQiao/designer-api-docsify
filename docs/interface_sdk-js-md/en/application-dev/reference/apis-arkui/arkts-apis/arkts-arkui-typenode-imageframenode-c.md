# ImageFrameNode

定义Image类型的FrameNode。

**Inheritance/Implementation:** ImageFrameNode extends [TypedFrameNode<ImageAttribute>](TypedFrameNode<ImageAttribute>)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-typeNode-abstract class ImageFrameNode extends TypedFrameNode<ImageAttribute>--><!--Device-typeNode-abstract class ImageFrameNode extends TypedFrameNode<ImageAttribute>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## initialize

```TypeScript
abstract initialize(src: image.PixelMap | ResourceStr | DrawableDescriptor): ImageAttribute
```

初始化Image类型的FrameNode。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ImageFrameNode-abstract initialize(src: image.PixelMap | ResourceStr | DrawableDescriptor): ImageAttribute--><!--Device-ImageFrameNode-abstract initialize(src: image.PixelMap | ResourceStr | DrawableDescriptor): ImageAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| src | image.PixelMap \| ResourceStr \| DrawableDescriptor | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| [ImageAttribute](../arkts-components/arkts-arkui-image-attribute.md) |  |

## initialize

```TypeScript
abstract initialize(src: image.PixelMap | ResourceStr | DrawableDescriptor | ImageContent): ImageAttribute
```

初始化Image类型的FrameNode。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ImageFrameNode-abstract initialize(src: image.PixelMap | ResourceStr | DrawableDescriptor | ImageContent): ImageAttribute--><!--Device-ImageFrameNode-abstract initialize(src: image.PixelMap | ResourceStr | DrawableDescriptor | ImageContent): ImageAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| src | image.PixelMap \| ResourceStr \| DrawableDescriptor \| ImageContent | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| [ImageAttribute](../arkts-components/arkts-arkui-image-attribute.md) |  |

## initialize

```TypeScript
abstract initialize(src: image.PixelMap | ResourceStr | DrawableDescriptor, value: ImageAIOptions): ImageAttribute
```

初始化Image类型的FrameNode。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ImageFrameNode-abstract initialize(src: image.PixelMap | ResourceStr | DrawableDescriptor, value: ImageAIOptions): ImageAttribute--><!--Device-ImageFrameNode-abstract initialize(src: image.PixelMap | ResourceStr | DrawableDescriptor, value: ImageAIOptions): ImageAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| src | image.PixelMap \| ResourceStr \| DrawableDescriptor | Yes |  |
| value | [ImageAIOptions](arkts-arkui-imageaioptions-i.md) | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| [ImageAttribute](../arkts-components/arkts-arkui-image-attribute.md) |  |

