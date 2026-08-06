# Image

The **Image** component is usually used to display images in applications. It supports data sources of the following
types: [PixelMap]{@link @ohos.multimedia.image:image.PixelMap}, [ResourceStr]{@link ResourceStr}, and
[DrawableDescriptor]{@link DrawableDescriptor}. Supported image formats include PNG, JPG, JPEG, BMP, SVG, WEBP, GIF,
HEIF, and TIFF. Note that the APNG and SVGA formats are not supported.

> **NOTE**

> - This component supports the TIFF image format since API version 23.
>
> - When keyboard shortcuts are used to copy an **Image** component, the **Image** component must be in a focused
> state. For instructions on how to set focus, see
> [Setting Whether a Component Is Focusable]
> (docroot://ui/arkts-common-events-focus-event.md#setting-whether-a-component-is-focusable).
> By default, the **Image** component is not focusable. To enable it to gain focus, set both the
> [focusable]{@link CommonMethod#focusable} and [focusOnTouch]{@link CommonMethod#focusOnTouch} attributes to
> **true**.
>
> - The **Image** component supports SVG image sources. For details about SVG tags, see [SVG Tags]{@link ./common}.
>
> - For animated images, animation playback is disabled by default and depends on the visibility of the **Image**
> component. When the component is visible, the animation is started through the callback. When the component is
> invisible, the animation is stopped. The visibility status of the **Image** component can be identified through the
>
> [onVisibleAreaChange]
> {@link CommonMethod#onVisibleAreaChange(ratios: Array<number>, event: VisibleAreaChangeCallback)}
> event. If the value of **ratios** is greater than 0, the component is visible.
>
> - For details about how to resolve white block issues during image loading, see
> [Solution to White Image Blocks]
> (https://developer.huawei.com/consumer/en/doc/best-practices/bpta-image-white-lump-solution).
> For details about how to address slow image loading, see
> [Optimizing Preset Image Loading]
> (https://developer.huawei.com/consumer/en/doc/best-practices/bpta-texture-compression-improve-
> performance#section91526132216).
>

Required Permissions

The **ohos.permission.INTERNET** permission is required for using online images. For details about how to apply for a
permission, see [Declaring Permissions](docroot://security/AccessToken/declare-permissions.md).

Child Components

Not supported

## Image

```TypeScript
Image(src: PixelMap | ResourceStr | DrawableDescriptor)
```

Obtains an image from the specified source for subsequent rendering and display.

If the **Image** component fails to obtain the image or the obtained image size is 0, the **Image** component is automatically resized to 0 and does not follow the layout constraints of its parent component.

By default, the **Image** component crops images to keep their center. For example, if the component has the same width and height, it crops any image whose width and height are different, so as to keep its center.

If the **Image** component does not have its width and height set, its size adapts to that of its parent component once the image is successfully loaded.
    **NOTE**  
    
    - Passing a URL directly to an **Image** component may lead to potential performance issues, such as: (1) Large  
    images cannot be downloaded in advance during loading, resulting in a long display time of white blocks; (2)  
    Small images set to load synchronously may block the UI thread in a weak network environment, causing screen  
    freezes; (3) In a rapidly scrolling waterfall flow, images that are about to be displayed cannot be downloaded in  
    advance, resulting in many white blocks during scrolling. Performance issues may manifest differently in  
    different scenarios. To minimize these issues, separate the network download part from the display of the  
    **Image** component, and download in advance or asynchronously. For details about how to resolve white block  
    issues during image loading, see  
    [Solution to White Image Blocks]  
    (https://developer.huawei.com/consumer/en/doc/best-practices/bpta-image-white-lump-solution).  
    For details about how to address slow image loading, see  
    [Optimizing Preset Image Loading]  
    (https://developer.huawei.com/consumer/en/doc/best-practices/bpta-texture-compression-improve-performance).  
    
    
    - When **src** is switched from a valid value (an image resource that can be parsed and loaded correctly) to an  
    invalid value (an image path that cannot be parsed or loaded), the component retains the previously successfully  
    loaded image content without clearing or resetting it.  
    
    - If the input parameter is of the [PixelMap]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ type, the **Image**  
    component can detect data changes only when the **PixelMap** object is updated to point to a new instance. If  
    modifications are made to the content of the **PixelMap** object, such as pixel values, but the reference to the  
    object remains the same, the **Image** component will not recognize these modifications as a data change.  
    
    - If the input parameter of the **Image** component is a Base64 string, the standard format of the Base64 string  
    is **data:image/subtype;base64,Base64EncodedData**. In this format, **subtype** indicates the type declaration,  
    **Base64EncodedData** indicates the Base64-encoded data, and other values are fixed strings. For example, the  
    input parameter of a PNG image is **data:image/png;base64,iVBORw0KGgo...**.  
        
        1. **image/subType** declares the data type. The **Image** component does not enforce that the declared type  
    exactly matches the actual image format decoded from Base64. In some scenarios, the image may still display  
    correctly even if the declared type does not match the actual format. To prevent future behavior changes or  
    unknown issues, it is recommended that the declared type always match the actual image format.  
        
        2. The **Image** component does not support the wildcard syntax: **data:image/*;base64,Base64EncodedData**.  
    The **subType** must explicitly declare the specific image type.  
        
        3. The **Image** component does not support loading SVG images in Base64 string format.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-ImageInterface-(src: PixelMap | ResourceStr | DrawableDescriptor): ImageAttribute--><!--Device-ImageInterface-(src: PixelMap | ResourceStr | DrawableDescriptor): ImageAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| src | \_\_\_MD\_LINK\_USD\_0\_\_\_ \| ResourceStr \| DrawableDescriptor | Yes | Data source of the image. Local and online sources are supported. For details about how to reference an image, see \_\_\_MD\_LINK\_USD\_0\_\_\_.\_\_\_HTML\_TAG\_USD\_8\_\_\_1. **PixelMap**: a pixel map storing graphical information, commonly used for image editing scenarios.\_\_\_HTML\_TAG\_USD\_9\_\_\_2. **ResourceStr**: a string or a Resource object.\_\_\_HTML\_TAG\_USD\_10\_\_\_The string type can be used to load local images and, more frequently, online images. When \_\_\_MD\_LINK\_USD\_1\_\_\_, the **Image** component cannot be called across bundles or modules. If an image needs to be used globally, you are advised to use the Resource format.\_\_\_HTML\_TAG\_USD\_11\_\_\_Since DevEco Studio 6.0.0 Beta2, resources in non-**resource** directories are not packaged by default for new projects or modules. To enable packaging, go to **buildOption** > **resOptions** > **copyCodeResource** to set **enable** to **true** in the module's **build-profile.json5** file. For details, see \_\_\_MD\_LINK\_USD\_2\_\_\_. \_\_\_HTML\_TAG\_USD\_12\_\_\_- Base64 strings are supported.\_\_\_HTML\_TAG\_USD\_13\_\_\_- When providing an HTTPS network image URL, refer to \_\_\_MD\_LINK\_USD\_3\_\_\_ for implementation guidance.\_\_\_HTML\_TAG\_USD\_14\_\_\_- Strings prefixed with the **file://** path are supported (application sandbox URI: **file://\_\_\_HTML\_TAG\_USD\_15\_\_\_/\_\_\_HTML\_TAG\_USD\_16\_\_\_**). For details about how to construct the application sandbox path URI, see [constructor]\_\_\_JSDOC\_LINK\_USD\_5\_\_\_. The sandbox path must be converted to an application sandbox URI using the [fileUri.getUriFromPath(path)]\_\_\_JSDOC\_LINK\_USD\_6\_\_\_ API before being passed in for display. In addition, ensure that the application has the read permission to the files in the specified path.< br>The Resource format allows for access across bundles and modules. It is recommended for accessing local images. For details, see \_\_\_MD\_LINK\_USD\_4\_\_\_.\_\_\_HTML\_TAG\_USD\_17\_\_\_ 3. **DrawableDescriptor**: an object created when the passed resource ID or name belongs to a common image. The [AnimatedDrawableDescriptor]\_\_\_JSDOC\_LINK\_USD\_7\_\_\_ type can be passed to play animations from a **PixelMap** array.\_\_\_HTML\_TAG\_USD\_18\_\_\_**NOTE**\_\_\_HTML\_TAG\_USD\_19\_\_\_- ArkTS widgets support GIF animations, but the animations only play once on display.\_\_\_HTML\_TAG\_USD\_20\_\_\_- ArkTS widgets do not support the strings with the **http://** or **file://** prefix.  |

## Image

```TypeScript
Image(src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent)
```

Obtains an image. The [ImageContent]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ type allows you to specify the image content.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-ImageInterface-(src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent): ImageAttribute--><!--Device-ImageInterface-(src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent): ImageAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| src | \_\_\_MD\_LINK\_USD\_0\_\_\_ \| ResourceStr \| DrawableDescriptor \| ImageContent | Yes | Data source of the image. Local and online sources are supported. For details about how to reference an image, see \_\_\_MD\_LINK\_USD\_0\_\_\_.\_\_\_HTML\_TAG\_USD\_3\_\_\_For details about how to use **PixelMap**, **ResourceStr**, and **DrawableDescriptor**, see the **src** parameter description of \_\_\_MD\_LINK\_USD\_1\_\_\_.\_\_\_HTML\_TAG\_USD\_4\_\_\_ [ImageContent]\_\_\_JSDOC\_LINK\_USD\_2\_\_\_: image content.\_\_\_HTML\_TAG\_USD\_5\_\_\_**NOTE**\_\_\_HTML\_TAG\_USD\_6\_\_\_- ArkTS widgets support GIF animations, but the animations only play once on display.\_\_\_HTML\_TAG\_USD\_7\_\_\_- ArkTS widgets do not support the strings with the **http://** or **file://** prefix.  |

## Image

```TypeScript
Image(src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent, reloadKey?: string)
```

Set src to obtain images

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**Widget capability:** This API can be used in ArkTS widgets since API version 26.0.0.

<!--Device-ImageInterface-(src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent, reloadKey?: string): ImageAttribute--><!--Device-ImageInterface-(src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent, reloadKey?: string): ImageAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| src | \_\_\_MD\_LINK\_USD\_0\_\_\_ \| ResourceStr \| DrawableDescriptor \| ImageContent | Yes |  |
| reloadKey | string | No |  |

## Image

```TypeScript
Image(src: PixelMap | ResourceStr | DrawableDescriptor, imageAIOptions: ImageAIOptions)
```

Obtains an image. The [imageAIOptions]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ parameter allows you to set AI image analysis options.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ImageInterface-(src: PixelMap | ResourceStr | DrawableDescriptor, imageAIOptions: ImageAIOptions): ImageAttribute--><!--Device-ImageInterface-(src: PixelMap | ResourceStr | DrawableDescriptor, imageAIOptions: ImageAIOptions): ImageAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| src | \_\_\_MD\_LINK\_USD\_0\_\_\_ \| ResourceStr \| DrawableDescriptor | Yes | Data source of the image. Local and online sources are supported. For details about how to reference an image, see \_\_\_MD\_LINK\_USD\_0\_\_\_.\_\_\_HTML\_TAG\_USD\_2\_\_\_For details about how to use **PixelMap**, **ResourceStr**, and **DrawableDescriptor**, see the **src** parameter description of \_\_\_MD\_LINK\_USD\_1\_\_\_.\_\_\_HTML\_TAG\_USD\_3\_\_\_**NOTE**\_\_\_HTML\_TAG\_USD\_4\_\_\_- ArkTS widgets support GIF animations, but the animations only play once on display.\_\_\_HTML\_TAG\_USD\_5\_\_\_- ArkTS widgets do not support the strings with the **http://** or **file://** prefix.  |
| imageAIOptions | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | AI image analysis options. You can configure the analysis type or bind an analyzer controller through this parameter.  |

## Image

```TypeScript
Image(src: PixelMap | ResourceStr | DrawableDescriptor,
      imageAIOptions?: ImageAIOptions, reloadKey?: string)
```

Set src and ai options to obtain images

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ImageInterface-(src: PixelMap | ResourceStr | DrawableDescriptor,      imageAIOptions?: ImageAIOptions, reloadKey?: string): ImageAttribute--><!--Device-ImageInterface-(src: PixelMap | ResourceStr | DrawableDescriptor,      imageAIOptions?: ImageAIOptions, reloadKey?: string): ImageAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| src | \_\_\_MD\_LINK\_USD\_0\_\_\_ \| ResourceStr \| DrawableDescriptor | Yes |  |
| imageAIOptions | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No |  |
| reloadKey | string | No |  |

## Summary

