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

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@ComponentBuilderexport declare function MediaCachedImage(    src: PixelMap | ResourceStr | DrawableDescriptor | ASTCResource,     content_?: CustomBuilder): MediaCachedImageAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function MediaCachedImage(    src: PixelMap | ResourceStr | DrawableDescriptor | ASTCResource,     content_?: CustomBuilder): MediaCachedImageAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| src | [PixelMap](../../apis-arkui/arkts-components/arkts-arkui-pixelmap-t.md) \| [ResourceStr](../../apis-arkui/arkts-apis/arkts-arkui-resourcestr-t.md) \| [DrawableDescriptor](../../apis-arkui/arkts-apis/arkts-arkui-arkui-drawabledescriptor-drawabledescriptor-c.md) \| [ASTCResource](arkts-na-mediacachedimage-astcresource-i-sys.md) | Yes | mediaCachedImage resource type. |
| content_ | CustomBuilder | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [MediaCachedImageAttribute](arkts-na-mediacachedimage-mediacachedimageattribute-i.md) | The attribute of the mediaCachedImage. |

