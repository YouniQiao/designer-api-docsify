# Image

The **Image** component is usually used to display images in applications. It supports data sources of the following types: [PixelMap](../../apis-image-kit/arkts-apis/arkts-image-image-pixelmap-i.md#pixelmap), [ResourceStr](../arkts-apis/arkts-arkui-resourcestr-t.md#resourcestr), and [DrawableDescriptor](arkts-arkui-drawabledescriptor-t.md#drawabledescriptor). Supported image formats include PNG, JPG, JPEG, BMP, SVG, WEBP, GIF, HEIF, and TIFF. Note that the APNG and SVGA formats are not supported. > **NOTE** > - This component supports the TIFF image format since API version 23. > > - When keyboard shortcuts are used to copy an **Image** component, the **Image** component must be in a focused > state. For instructions on how to set focus, see > [Setting Whether a Component Is Focusable] > (../../../ui/arkts-common-events-focus-event.md#setting-whether-a-component-is-focusable). > By default, the **Image** component is not focusable. To enable it to gain focus, set both the > focusable and [focusOnTouch](arkts-arkui-commonmethod-c.md#focusontouch) attributes to > **true**. > > - The **Image** component supports SVG image sources. For details about SVG tags, see SVG Tags. > > - For animated images, animation playback is disabled by default and depends on the visibility of the **Image** > component. When the component is visible, the animation is started through the callback. When the component is > invisible, the animation is stopped. The visibility status of the **Image** component can be identified through the > > [onVisibleAreaChange] > [onVisibleAreaChange](arkts-arkui-commonmethod-c.md#onvisibleareachange) > event. If the value of **ratios** is greater than 0, the component is visible. > > - For details about how to resolve white block issues during image loading, see > [Solution to White Image Blocks] > (https://developer.huawei.com/consumer/en/doc/best-practices/bpta-image-white-lump-solution). > For details about how to address slow image loading, see > [Optimizing Preset Image Loading] > (https://developer.huawei.com/consumer/en/doc/best-practices/bpta-texture-compression-improve- > performance#section91526132216). > Required Permissions The **ohos.permission.INTERNET** permission is required for using online images. For details about how to apply for a permission, see [Declaring Permissions](../../../security/AccessToken/declare-permissions.md). Child Components Not supported

## Image

```TypeScript
Image(src: PixelMap | ResourceStr | DrawableDescriptor)
```

Obtains an image from the specified source for subsequent rendering and display. If the **Image** component fails to obtain the image or the obtained image size is 0, the **Image** component is automatically resized to 0 and does not follow the layout constraints of its parent component. By default, the **Image** component crops images to keep their center. For example, if the component has the same width and height, it crops any image whose width and height are different, so as to keep its center. If the **Image** component does not have its width and height set, its size adapts to that of its parent component once the image is successfully loaded. > **NOTE：**> > - Passing a URL directly to an **Image** component may lead to potential performance issues, such as: (1) Large > images cannot be downloaded in advance during loading, resulting in a long display time of white blocks; (2) > Small images set to load synchronously may block the UI thread in a weak network environment, causing screen > freezes; (3) In a rapidly scrolling waterfall flow, images that are about to be displayed cannot be downloaded in > advance, resulting in many white blocks during scrolling. Performance issues may manifest differently in > different scenarios. To minimize these issues, separate the network download part from the display of the > **Image** component, and download in advance or asynchronously. For details about how to resolve white block > issues during image loading, see > [Solution to White Image Blocks] > (https://developer.huawei.com/consumer/en/doc/best-practices/bpta-image-white-lump-solution). > For details about how to address slow image loading, see > [Optimizing Preset Image Loading] > (https://developer.huawei.com/consumer/en/doc/best-practices/bpta-texture-compression-improve-performance). > > > - When **src** is switched from a valid value (an image resource that can be parsed and loaded correctly) to an > invalid value (an image path that cannot be parsed or loaded), the component retains the previously successfully > loaded image content without clearing or resetting it. > > - If the input parameter is of the [PixelMap](../../apis-image-kit/arkts-apis/arkts-image-image-pixelmap-i.md#pixelmap) type, the **Image** > component can detect data changes only when the **PixelMap** object is updated to point to a new instance. If > modifications are made to the content of the **PixelMap** object, such as pixel values, but the reference to the > object remains the same, the **Image** component will not recognize these modifications as a data change. > > - If the input parameter of the **Image** component is a Base64 string, the standard format of the Base64 string > is **data:image/subtype;base64,Base64EncodedData**. In this format, **subtype** indicates the type declaration, > **Base64EncodedData** indicates the Base64-encoded data, and other values are fixed strings. For example, the > input parameter of a PNG image is **data:image/png;base64,iVBORw0KGgo...**. > > > > 1. **image/subType** declares the data type. The **Image** component does not enforce that the declared type > exactly matches the actual image format decoded from Base64. In some scenarios, the image may still display > correctly even if the declared type does not match the actual format. To prevent future behavior changes or > unknown issues, it is recommended that the declared type always match the actual image format. > > > > 2. The **Image** component does not support the wildcard syntax: **data:image/*;base64,Base64EncodedData**. > The **subType** must explicitly declare the specific image type. > > > > 3. The **Image** component does not support loading SVG images in Base64 string format.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-ImageInterface-(src: PixelMap | ResourceStr | DrawableDescriptor): ImageAttribute--><!--Device-ImageInterface-(src: PixelMap | ResourceStr | DrawableDescriptor): ImageAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| src | PixelMap \| [ResourceStr](../arkts-apis/arkts-arkui-resourcestr-t.md) \| [DrawableDescriptor](arkts-arkui-drawabledescriptor-t.md) | Yes |

## Image

```TypeScript
Image(src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent)
```

Obtains an image. The [ImageContent](arkts-arkui-imagecontent-e.md#imagecontent) type allows you to specify the image content.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-ImageInterface-(src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent): ImageAttribute--><!--Device-ImageInterface-(src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent): ImageAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| src | PixelMap \| [ResourceStr](../arkts-apis/arkts-arkui-resourcestr-t.md) \| [DrawableDescriptor](arkts-arkui-drawabledescriptor-t.md) \| [ImageContent](arkts-arkui-imagecontent-e.md) | Yes |

## Image

```TypeScript
Image(src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent, reloadKey?: string)
```

Set src to obtain images

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**Widget capability:** This API can be used in ArkTS widgets since API version 26.0.0.

<!--Device-ImageInterface-(src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent, reloadKey?: string): ImageAttribute--><!--Device-ImageInterface-(src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent, reloadKey?: string): ImageAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| src | PixelMap \| [ResourceStr](../arkts-apis/arkts-arkui-resourcestr-t.md) \| [DrawableDescriptor](arkts-arkui-drawabledescriptor-t.md) \| [ImageContent](arkts-arkui-imagecontent-e.md) | Yes |
| reloadKey | string | No |

## Image

```TypeScript
Image(src: PixelMap | ResourceStr | DrawableDescriptor, imageAIOptions: ImageAIOptions)
```

Obtains an image. The [imageAIOptions](../arkts-apis/arkts-arkui-imageaioptions-i.md#imageaioptions) parameter allows you to set AI image analysis options.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ImageInterface-(src: PixelMap | ResourceStr | DrawableDescriptor, imageAIOptions: ImageAIOptions): ImageAttribute--><!--Device-ImageInterface-(src: PixelMap | ResourceStr | DrawableDescriptor, imageAIOptions: ImageAIOptions): ImageAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| src | PixelMap \| [ResourceStr](../arkts-apis/arkts-arkui-resourcestr-t.md) \| [DrawableDescriptor](arkts-arkui-drawabledescriptor-t.md) | Yes |
| imageAIOptions | [ImageAIOptions](../arkts-apis/arkts-arkui-imageaioptions-i.md) | Yes |

## Image

```TypeScript
Image(src: PixelMap | ResourceStr | DrawableDescriptor,
      imageAIOptions?: ImageAIOptions, reloadKey?: string)
```

Set src and ai options to obtain images

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ImageInterface-(src: PixelMap | ResourceStr | DrawableDescriptor,      imageAIOptions?: ImageAIOptions, reloadKey?: string): ImageAttribute--><!--Device-ImageInterface-(src: PixelMap | ResourceStr | DrawableDescriptor,      imageAIOptions?: ImageAIOptions, reloadKey?: string): ImageAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| src | PixelMap \| [ResourceStr](../arkts-apis/arkts-arkui-resourcestr-t.md) \| [DrawableDescriptor](arkts-arkui-drawabledescriptor-t.md) | Yes |
| imageAIOptions | [ImageAIOptions](../arkts-apis/arkts-arkui-imageaioptions-i.md) | No |
| reloadKey | string | No |

## Summary

- [ImageAlt](arkts-arkui-imagealt-i.md)
- [ImageError](arkts-arkui-imageerror-i.md)
- [ImageSourceSize](arkts-arkui-imagesourcesize-i.md)
- [ResizableOptions](arkts-arkui-resizableoptions-i.md)
- [BusinessError](arkts-arkui-businesserror-t.md)
- [DrawableDescriptor](arkts-arkui-drawabledescriptor-t.md)
- [DrawingColorFilter](arkts-arkui-drawingcolorfilter-t.md)
- [DrawingLattice](arkts-arkui-drawinglattice-t.md)
- [ImageErrorCallback](arkts-arkui-imageerrorcallback-t.md)
- [ImageMatrix](arkts-arkui-imagematrix-t.md)
- [RequestDownloadInfo](arkts-arkui-requestdownloadinfo-t.md)
- [ResolutionQuality](arkts-arkui-resolutionquality-t-sys.md)
- [DynamicRangeMode](arkts-arkui-dynamicrangemode-e.md)
- [ImageContent](arkts-arkui-imagecontent-e.md)
- [ImageInterpolation](arkts-arkui-imageinterpolation-e.md)
- [ImageRenderMode](arkts-arkui-imagerendermode-e.md)
- [ImageRotateOrientation](arkts-arkui-imagerotateorientation-e.md)
