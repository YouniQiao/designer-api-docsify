# ImageSpan

As a child of the [Text]{@link ./text} and [ContainerSpan]{@link ./container_span} components, the **ImageSpan** component is used to display inline images.

## Child Components Not supported

## ImageSpan

```TypeScript
ImageSpan(value: ResourceStr | PixelMap)
```

Defines the constructor of ImageSpan.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ImageSpanInterface-(value: ResourceStr | PixelMap): ImageSpanAttribute--><!--Device-ImageSpanInterface-(value: ResourceStr | PixelMap): ImageSpanAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | \_\_\_MD\_LINK\_USD\_0\_\_\_ \| PixelMap | Yes | Image source. Both local and network images are supported.\_\_\_HTML\_TAG\_USD\_0\_\_\_When using an image referenced using a relative path, for example, **ImageSpan("common/test.jpg")**, the **ImageSpan** component cannot be called across bundles or modules. Therefore, you are advised to use **\$r** to reference image resources that need to be used globally.\_\_\_HTML\_TAG\_USD\_1\_\_\_- The supported formats include PNG, JPG, BMP, SVG, GIF, and HEIF.\_\_\_HTML\_TAG\_USD\_2\_\_\_- Base64 strings are supported. The value format is data:image/[png\|jpeg\|bmp\|webp\|heif];base64, [base64 data], where *[base64 data]* is a Base64 string.\_\_\_HTML\_TAG\_USD\_3\_\_\_- Character string prefixed with file://data/ storage, which is used to read image resources in the file folder in the application installation directory. Ensure that the application has the read permission to the files in the specified path.  |

## Summary

