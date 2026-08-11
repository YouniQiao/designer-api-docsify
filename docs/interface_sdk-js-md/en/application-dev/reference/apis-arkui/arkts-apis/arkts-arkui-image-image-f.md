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

Defines the Image component.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function Image(    src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent | undefined,    imageAIOptions?: ImageAIOptions,    reloadKey?: string): ImageAttribute--><!--Device-unnamed-export declare function Image(    src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent | undefined,    imageAIOptions?: ImageAIOptions,    reloadKey?: string): ImageAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| src | [PixelMap](../arkts-components/arkts-arkui-pixelmap-t.md) \| ResourceStr \| DrawableDescriptor \| ImageContent \| undefined | Yes | image resource type. |
| imageAIOptions | [ImageAIOptions](arkts-arkui-imageaioptions-i.md) | No | Options for AI analyzer. |
| reloadKey | string | No | Options for image reload. |

**Return value:**

| Type | Description |
| --- | --- |
| [ImageAttribute](../arkts-components/arkts-arkui-image-attribute.md) | The attribute of the Image. |


## Image

```TypeScript
export declare function Image(
    src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent | undefined,
    reloadKey?: string
): ImageAttribute
```

Defines the Image component.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function Image(    src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent | undefined,    reloadKey?: string): ImageAttribute--><!--Device-unnamed-export declare function Image(    src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent | undefined,    reloadKey?: string): ImageAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| src | [PixelMap](../arkts-components/arkts-arkui-pixelmap-t.md) \| ResourceStr \| DrawableDescriptor \| ImageContent \| undefined | Yes | image resource type. |
| reloadKey | string | No | Options for image reload. |

**Return value:**

| Type | Description |
| --- | --- |
| [ImageAttribute](../arkts-components/arkts-arkui-image-attribute.md) | The attribute of the Image. |


## Image

```TypeScript
export declare function Image(style: CustomBuilderT<ImageAttribute>): ImageAttribute
```

Defines the Image component. It requires call setImageOptions at start of the component attribute set-up.ant it requires call applyAttributeFinish at the end of the component attribute set-up.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function Image(style: CustomBuilderT<ImageAttribute>): ImageAttribute--><!--Device-unnamed-export declare function Image(style: CustomBuilderT<ImageAttribute>): ImageAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [CustomBuilderT](../arkts-components/arkts-arkui-custombuildert-t.md)&lt;ImageAttribute&gt; | Yes | the callback to set up component's attribute. |

**Return value:**

| Type | Description |
| --- | --- |
| [ImageAttribute](../arkts-components/arkts-arkui-image-attribute.md) | The attribute of the Image. |

