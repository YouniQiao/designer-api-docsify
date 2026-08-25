# MediaCachedImageInterface（系统接口）

```TypeScript
export type MediaCachedImageInterface = (src: PixelMap | ResourceStr | DrawableDescriptor | ASTCResource)
    => MediaCachedImageAttribute
```

定义 MediaCachedImageInterface 类型。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| src | [PixelMap](../arkts-components/arkts-arkui-pixelmap-t.md) \| [ResourceStr](arkts-arkui-resourcestr-t.md) \| [DrawableDescriptor](arkts-arkui-arkui-drawabledescriptor-drawabledescriptor-c.md) \| [ASTCResource](arkts-arkui-mediacachedimage-astcresource-i-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [MediaCachedImageAttribute](arkts-arkui-mediacachedimage-mediacachedimageattribute-i.md) |
