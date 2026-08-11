# MediaCachedImageInterface (System API)

```TypeScript
export type MediaCachedImageInterface = (src: PixelMap | ResourceStr | DrawableDescriptor | ASTCResource)
    => MediaCachedImageAttribute
```

Defines the MediaCachedImageInterface type.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type MediaCachedImageInterface = (src: PixelMap | ResourceStr | DrawableDescriptor | ASTCResource)    => MediaCachedImageAttribute--><!--Device-unnamed-export type MediaCachedImageInterface = (src: PixelMap | ResourceStr | DrawableDescriptor | ASTCResource)    => MediaCachedImageAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| src | [PixelMap](../arkts-components/arkts-arkui-pixelmap-t.md) \| ResourceStr \| DrawableDescriptor \| ASTCResource | Yes | mediaCachedImage resource type. |

**Return value:**

| Type | Description |
| --- | --- |
| [MediaCachedImageAttribute](arkts-arkui-mediacachedimage-mediacachedimageattribute-i.md) | The attribute of the mediaCachedImage. |

