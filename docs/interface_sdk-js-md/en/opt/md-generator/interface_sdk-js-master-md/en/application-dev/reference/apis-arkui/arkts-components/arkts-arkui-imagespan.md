# ImageSpan

As a child of the [Text]{@link ./text} and [ContainerSpan]{@link ./container_span} components, the **ImageSpan**
component is used to display inline images.

## Child Components

Not supported

## ImageSpan

```TypeScript
ImageSpan(value: ResourceStr | PixelMap)
```

Defines the constructor of ImageSpan.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ImageSpanInterface-(value: ResourceStr | PixelMap): ImageSpanAttribute--><!--Device-ImageSpanInterface-(value: ResourceStr | PixelMap): ImageSpanAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [ResourceStr](../arkts-apis/arkts-arkui-resourcestr-t.md) \| [PixelMap](../../apis-image-kit/arkts-apis/arkts-image-image-pixelmap-i.md) | Yes | Image source. Both local and network images are supported.<br>When using an image referenced using a relative path, for example, **ImageSpan("common/test.jpg")**, the **ImageSpan** component cannot be called across bundles or modules. Therefore, you are advised to use **\$r** to reference image resources that need to be used globally.<br>- The supported formats include PNG, JPG, BMP, SVG, GIF, and HEIF.<br>- Base64 strings are supported. The value format is data:image/[png\|jpeg\|bmp\|webp\|

## Summary

- [ImageLoadResult](arkts-arkui-imagespan-imageloadresult-i.md)
- [ImageCompleteCallback](arkts-arkui-imagespan-imagecompletecallback-t.md)
