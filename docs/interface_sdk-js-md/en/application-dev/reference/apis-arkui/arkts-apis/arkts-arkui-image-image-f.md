# Image

## Image

```TypeScript
export declare function Image(
    src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent | undefined,
    imageAIOptions?: ImageAIOptions
): ImageAttribute
```

Defines the Image component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function Image(    src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent | undefined,    imageAIOptions?: ImageAIOptions): ImageAttribute--><!--Device-unnamed-export declare function Image(    src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent | undefined,    imageAIOptions?: ImageAIOptions): ImageAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| src | [PixelMap](../arkts-components/arkts-arkui-pixelmap-t.md) \| ResourceStr \| DrawableDescriptor \| ImageContent \| undefined | Yes | image resource type. |
| imageAIOptions | [ImageAIOptions](arkts-arkui-imageaioptions-i.md) | No | Options for AI analyzer. |

**Return value:**

| Type | Description |
| --- | --- |
| [ImageAttribute](../arkts-components/arkts-arkui-image-attribute.md) | The attribute of the Image. |


## Image

```TypeScript
export declare function Image(
    src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent | undefined,
    imageAIOptions?: ImageAIOptions,
    reloadKey?: string
): ImageAttribute
```

定义Image组件。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function Image(    src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent | undefined,    imageAIOptions?: ImageAIOptions,    reloadKey?: string): ImageAttribute--><!--Device-unnamed-export declare function Image(    src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent | undefined,    imageAIOptions?: ImageAIOptions,    reloadKey?: string): ImageAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| src | [PixelMap](../arkts-components/arkts-arkui-pixelmap-t.md) \| ResourceStr \| DrawableDescriptor \| ImageContent \| undefined | Yes | 图片资源类型。 |
| imageAIOptions | [ImageAIOptions](arkts-arkui-imageaioptions-i.md) | No | AI分析器的参数。 |
| reloadKey | string | No | 用于图像重新加载的选项。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ImageAttribute](../arkts-components/arkts-arkui-image-attribute.md) | Image的属性。 |


## Image

```TypeScript
export declare function Image(
    src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent | undefined,
    reloadKey?: string
): ImageAttribute
```

定义Image组件。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function Image(    src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent | undefined,    reloadKey?: string): ImageAttribute--><!--Device-unnamed-export declare function Image(    src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent | undefined,    reloadKey?: string): ImageAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| src | [PixelMap](../arkts-components/arkts-arkui-pixelmap-t.md) \| ResourceStr \| DrawableDescriptor \| ImageContent \| undefined | Yes | 图片资源类型。 |
| reloadKey | string | No | 用于图像重新加载的选项。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ImageAttribute](../arkts-components/arkts-arkui-image-attribute.md) | The attribute of the Image. |


## Image

```TypeScript
export declare function Image(style: CustomBuilderT<ImageAttribute>): ImageAttribute
```

定义Image组件。它需要在组件属性设置开始时调用setImageOptions。它需要在组件属性设置结束时调用applyAttributeFinish。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function Image(style: CustomBuilderT<ImageAttribute>): ImageAttribute--><!--Device-unnamed-export declare function Image(style: CustomBuilderT<ImageAttribute>): ImageAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [CustomBuilderT](../arkts-components/arkts-arkui-custombuildert-t.md)&lt;ImageAttribute&gt; | Yes | 设置组件属性的回调。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ImageAttribute](../arkts-components/arkts-arkui-image-attribute.md) | Image的属性。 |

