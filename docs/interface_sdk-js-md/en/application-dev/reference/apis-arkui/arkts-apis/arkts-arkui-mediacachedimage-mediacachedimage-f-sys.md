# MediaCachedImage (System API)

## MediaCachedImage

```TypeScript
export declare function MediaCachedImage(
    src: PixelMap | ResourceStr | DrawableDescriptor | ASTCResource, 
    content_?: CustomBuilder
): MediaCachedImageAttribute
```

Defines the MediaCachedImage component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function MediaCachedImage(    src: PixelMap | ResourceStr | DrawableDescriptor | ASTCResource,     content_?: CustomBuilder): MediaCachedImageAttribute--><!--Device-unnamed-export declare function MediaCachedImage(    src: PixelMap | ResourceStr | DrawableDescriptor | ASTCResource,     content_?: CustomBuilder): MediaCachedImageAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| src | [PixelMap](../arkts-components/arkts-arkui-pixelmap-t.md) \| [ResourceStr](arkts-arkui-resourcestr-t.md) \| [DrawableDescriptor](arkts-arkui-arkui-drawabledescriptor-drawabledescriptor-c.md) \| [ASTCResource](arkts-arkui-mediacachedimage-astcresource-i-sys.md) | Yes | mediaCachedImage resource type. |
| content_ | [CustomBuilder](arkts-arkui-custombuilder-t.md) | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [MediaCachedImageAttribute](arkts-arkui-mediacachedimage-mediacachedimageattribute-i.md) | The attribute of the mediaCachedImage. |

