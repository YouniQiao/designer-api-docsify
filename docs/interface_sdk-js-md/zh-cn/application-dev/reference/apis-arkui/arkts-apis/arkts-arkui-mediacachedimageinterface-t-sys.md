# MediaCachedImageInterface（系统接口）

```TypeScript
export type MediaCachedImageInterface = (src: PixelMap | ResourceStr | DrawableDescriptor | ASTCResource)
    => MediaCachedImageAttribute
```

Defines the MediaCachedImageInterface type.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export type MediaCachedImageInterface = (src: PixelMap | ResourceStr | DrawableDescriptor | ASTCResource)    => MediaCachedImageAttribute--><!--Device-unnamed-export type MediaCachedImageInterface = (src: PixelMap | ResourceStr | DrawableDescriptor | ASTCResource)    => MediaCachedImageAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | [PixelMap](../arkts-components/arkts-arkui-pixelmap-t.md) \| ResourceStr \| DrawableDescriptor \| ASTCResource | 是 | mediaCachedImage resource type. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [MediaCachedImageAttribute](arkts-arkui-mediacachedimage-mediacachedimageattribute-i.md) | The attribute of the mediaCachedImage. |

