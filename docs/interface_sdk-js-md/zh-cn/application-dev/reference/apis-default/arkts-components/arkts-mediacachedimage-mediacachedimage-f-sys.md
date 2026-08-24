# MediaCachedImage（系统接口）

## MediaCachedImage

```TypeScript
@ComponentBuilder
export declare function MediaCachedImage(
    src: PixelMap | ResourceStr | DrawableDescriptor | ASTCResource, 
    content_?: CustomBuilder
): MediaCachedImageAttribute
```

定义 MediaCachedImage 组件。

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**装饰器类型：** @ComponentBuilder

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-@ComponentBuilderexport declare function MediaCachedImage(    src: PixelMap | ResourceStr | DrawableDescriptor | ASTCResource,     content_?: CustomBuilder): MediaCachedImageAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function MediaCachedImage(    src: PixelMap | ResourceStr | DrawableDescriptor | ASTCResource,     content_?: CustomBuilder): MediaCachedImageAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | [PixelMap](../../apis-arkui/arkts-components/arkts-arkui-pixelmap-t.md) \| [ResourceStr](../../apis-arkui/arkts-apis/arkts-arkui-resourcestr-t.md) \| [DrawableDescriptor](../../apis-arkui/arkts-apis/arkts-arkui-arkui-drawabledescriptor-drawabledescriptor-c.md) \| [ASTCResource](arkts-mediacachedimage-astcresource-i-sys.md) | 是 | mediaCachedImage 资源类型。 |
| content_ | [CustomBuilder](../arkts-apis/arkts-custombuilder-t.md) | 否 | container |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [MediaCachedImageAttribute](arkts-mediacachedimage-attribute.md) | mediaCachedImage 的属性。 |

