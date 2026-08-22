# Image

## Image

```TypeScript
@ComponentBuilder
export declare function Image(
    src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent | undefined,
    imageAIOptions?: ImageAIOptions
): ImageAttribute
```

Defines the Image component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@ComponentBuilderexport declare function Image(    src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent | undefined,    imageAIOptions?: ImageAIOptions): ImageAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function Image(    src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent | undefined,    imageAIOptions?: ImageAIOptions): ImageAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| src | [PixelMap](../../apis-arkui/arkts-components/arkts-arkui-pixelmap-t.md) \| [ResourceStr](../../apis-arkui/arkts-apis/arkts-arkui-resourcestr-t.md) \| [DrawableDescriptor](../../apis-arkui/arkts-apis/arkts-arkui-arkuidrawabledescriptor-drawabledescriptor-c.md) \| [ImageContent](arkts-image-imagecontent-e.md) \| undefined | Yes | image resource type. |
| imageAIOptions | [ImageAIOptions](../../apis-arkui/arkts-apis/arkts-arkui-imagecommon-imageaioptions-i.md) | No | Options for AI analyzer. |

**Return value:**

| Type | Description |
| --- | --- |
| [ImageAttribute](arkts-image-attribute.md) | The attribute of the Image. |


## Image

```TypeScript
@ComponentBuilder
export declare function Image(
    src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent | undefined,
    imageAIOptions?: ImageAIOptions,
    reloadKey?: string
): ImageAttribute
```

Defines the Image component.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@ComponentBuilderexport declare function Image(    src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent | undefined,    imageAIOptions?: ImageAIOptions,    reloadKey?: string): ImageAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function Image(    src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent | undefined,    imageAIOptions?: ImageAIOptions,    reloadKey?: string): ImageAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| src | [PixelMap](../../apis-arkui/arkts-components/arkts-arkui-pixelmap-t.md) \| [ResourceStr](../../apis-arkui/arkts-apis/arkts-arkui-resourcestr-t.md) \| [DrawableDescriptor](../../apis-arkui/arkts-apis/arkts-arkui-arkuidrawabledescriptor-drawabledescriptor-c.md) \| [ImageContent](arkts-image-imagecontent-e.md) \| undefined | Yes | image resource type. |
| imageAIOptions | [ImageAIOptions](../../apis-arkui/arkts-apis/arkts-arkui-imagecommon-imageaioptions-i.md) | No | Options for AI analyzer. |
| reloadKey | string | No | Options for image reload. |

**Return value:**

| Type | Description |
| --- | --- |
| [ImageAttribute](arkts-image-attribute.md) | The attribute of the Image. |


## Image

```TypeScript
@ComponentBuilder
export declare function Image(
    src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent | undefined,
    reloadKey?: string
): ImageAttribute
```

Defines the Image component.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@ComponentBuilderexport declare function Image(    src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent | undefined,    reloadKey?: string): ImageAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function Image(    src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent | undefined,    reloadKey?: string): ImageAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| src | [PixelMap](../../apis-arkui/arkts-components/arkts-arkui-pixelmap-t.md) \| [ResourceStr](../../apis-arkui/arkts-apis/arkts-arkui-resourcestr-t.md) \| [DrawableDescriptor](../../apis-arkui/arkts-apis/arkts-arkui-arkuidrawabledescriptor-drawabledescriptor-c.md) \| [ImageContent](arkts-image-imagecontent-e.md) \| undefined | Yes | image resource type. |
| reloadKey | string | No | Options for image reload. |

**Return value:**

| Type | Description |
| --- | --- |
| [ImageAttribute](arkts-image-attribute.md) | The attribute of the Image. |


## Image

```TypeScript
@Builder
export declare function Image(style: CustomBuilderT<ImageAttribute>): ImageAttribute
```

Defines the Image component. It requires call setImageOptions at start of the component attribute set-up. ant it requires call applyAttributeFinish at the end of the component attribute set-up.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@Builderexport declare function Image(style: CustomBuilderT<ImageAttribute>): ImageAttribute--><!--Device-unnamed-@Builderexport declare function Image(style: CustomBuilderT<ImageAttribute>): ImageAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [CustomBuilderT](../arkts-apis/arkts-custombuildert-t.md)&lt;[ImageAttribute](arkts-image-attribute.md)&gt; | Yes | the callback to set up component's attribute. |

**Return value:**

| Type | Description |
| --- | --- |
| [ImageAttribute](arkts-image-attribute.md) | The attribute of the Image. |

