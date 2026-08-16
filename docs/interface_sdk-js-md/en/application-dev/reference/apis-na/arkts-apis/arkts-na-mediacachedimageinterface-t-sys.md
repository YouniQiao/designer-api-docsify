# MediaCachedImageInterface (System API)

```TypeScript
export type MediaCachedImageInterface = (src: PixelMap | ResourceStr | DrawableDescriptor | ASTCResource)
    => MediaCachedImageAttribute
```

Defines the MediaCachedImageInterface type.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type MediaCachedImageInterface = (src: PixelMap | ResourceStr | DrawableDescriptor | ASTCResource)    => MediaCachedImageAttribute--><!--Device-unnamed-export type MediaCachedImageInterface = (src: PixelMap | ResourceStr | DrawableDescriptor | ASTCResource)    => MediaCachedImageAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| src | [PixelMap](../../apis-arkui/arkts-components/arkts-arkui-pixelmap-t.md) \| [ResourceStr](../../apis-arkui/arkts-apis/arkts-arkui-resourcestr-t.md) \| [DrawableDescriptor](arkts-na-arkui-drawabledescriptor-drawabledescriptor-c.md) \| [ASTCResource](arkts-na-mediacachedimage-astcresource-i-sys.md) | Yes | mediaCachedImage resource type. |

**Return value:**

| Type | Description |
| --- | --- |
| [MediaCachedImageAttribute](arkts-na-mediacachedimage-mediacachedimageattribute-i.md) | The attribute of the mediaCachedImage. |

