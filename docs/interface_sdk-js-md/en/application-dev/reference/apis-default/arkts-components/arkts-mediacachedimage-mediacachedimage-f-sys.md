# MediaCachedImage (System API)

## MediaCachedImage

```TypeScript
@ComponentBuilder
export declare function MediaCachedImage(
    src: PixelMap | ResourceStr | DrawableDescriptor | ASTCResource, 
    content_?: CustomBuilder
): MediaCachedImageAttribute
```

Defines the MediaCachedImage component.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@ComponentBuilderexport declare function MediaCachedImage(    src: PixelMap | ResourceStr | DrawableDescriptor | ASTCResource,     content_?: CustomBuilder): MediaCachedImageAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function MediaCachedImage(    src: PixelMap | ResourceStr | DrawableDescriptor | ASTCResource,     content_?: CustomBuilder): MediaCachedImageAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| src | [PixelMap](../../apis-arkui/arkts-components/arkts-arkui-pixelmap-t.md) \| [ResourceStr](../../apis-arkui/arkts-apis/arkts-arkui-resourcestr-t.md) \| [DrawableDescriptor](../../apis-arkui/arkts-apis/arkts-arkui-arkuidrawabledescriptor-drawabledescriptor-c.md) \| [ASTCResource](arkts-mediacachedimage-astcresource-i-sys.md) | Yes | mediaCachedImage resource type. |
| content_ | [CustomBuilder](../arkts-apis/arkts-custombuilder-t.md) | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [MediaCachedImageAttribute](arkts-mediacachedimage-attribute.md) | The attribute of the mediaCachedImage. |

