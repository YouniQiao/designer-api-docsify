# DecodingOptions

Describes the image decoding options.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-image-interface DecodingOptions--><!--Device-image-interface DecodingOptions-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

## cropAndScaleStrategy

```TypeScript
cropAndScaleStrategy?: CropAndScaleStrategy
```

If **desiredRegion** and **desiredSize** are both specified, the order of cropping and scaling is determined.

Only **SCALE\_FIRST** and **CROP\_FIRST** are supported.

**Type:** CropAndScaleStrategy

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-DecodingOptions-cropAndScaleStrategy?: CropAndScaleStrategy--><!--Device-DecodingOptions-cropAndScaleStrategy?: CropAndScaleStrategy-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

## desiredColorSpace

```TypeScript
desiredColorSpace?: colorSpaceManager.ColorSpaceManager
```

Target color space. The default value is **UNKNOWN**.

**Type:** colorSpaceManager.ColorSpaceManager

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-DecodingOptions-desiredColorSpace?: colorSpaceManager.ColorSpaceManager--><!--Device-DecodingOptions-desiredColorSpace?: colorSpaceManager.ColorSpaceManager-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

## desiredDynamicRange

```TypeScript
desiredDynamicRange?: DecodingDynamicRange
```

Desired dynamic range. The default value is **SDR**.

This property cannot be set for an image source created using  
[CreateIncrementalSource]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_. By default, the image source is decoded as SDR content.

If the platform does not support HDR, the setting is invalid and the content is decoded as SDR content by default.

**Type:** DecodingDynamicRange

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-DecodingOptions-desiredDynamicRange?: DecodingDynamicRange--><!--Device-DecodingOptions-desiredDynamicRange?: DecodingDynamicRange-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

## desiredPixelFormat

```TypeScript
desiredPixelFormat?: PixelMapFormat
```

Pixel format for decoding. The default value is **RGBA\_8888**. Only RGBA\_8888, BGRA\_8888, and RGB\_565 are supported. RGB\_565 is not supported for images with alpha channels, such as PNG, GIF, ICO, and WEBP.

**Type:** PixelMapFormat

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-DecodingOptions-desiredPixelFormat?: PixelMapFormat--><!--Device-DecodingOptions-desiredPixelFormat?: PixelMapFormat-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

## desiredRegion

```TypeScript
desiredRegion?: Region
```

Rectangle specified by **Region** in the decoded image. When the original image is large and only a specific part of the image is required, you can set this parameter to improve performance. The default value is the original image size.

Note: If both **desiredSize** and **desiredRegion** are passed to the decoding API, you must also include  
**cropAndScaleStrategy** to determine whether to crop or scale first. **CROP\_FIRST** is recommended.

**Type:** Region

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-DecodingOptions-desiredRegion?: Region--><!--Device-DecodingOptions-desiredRegion?: Region-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

## desiredSize

```TypeScript
desiredSize?: Size
```

Expected output size. The value must be a positive integer and defaults to the original image size. If the output size is different from the original size, the output is stretched or scaled to the specified size.

Note: If both **desiredSize** and **desiredRegion** are passed to the decoding API, you must also include  
**cropAndScaleStrategy** to determine whether to crop or scale first. **CROP\_FIRST** is recommended.

**Type:** Size

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-DecodingOptions-desiredSize?: Size--><!--Device-DecodingOptions-desiredSize?: Size-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

## editable

```TypeScript
editable?: boolean
```

Whether the image is editable. **true** if editable, **false** otherwise. The default value is **false**. If this option is set to **false**, the image cannot be edited again, and operations such as writing pixels will fail.

**Type:** boolean

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-DecodingOptions-editable?: boolean--><!--Device-DecodingOptions-editable?: boolean-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

## fitDensity

```TypeScript
fitDensity?: int
```

Pixel density, in ppi. The default value is **0**.

**Type:** int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-DecodingOptions-fitDensity?: int--><!--Device-DecodingOptions-fitDensity?: int-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

## index

```TypeScript
index?: int
```

Index of the image to decode. The default value is **0**, indicating the first image. If this parameter is set to N, the (N+1)th image is used. For single-frame images, the value is always **0**. For multi-frame images such as animations, the value ranges from 0 to (Number of frames – 1).

**Type:** int

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-DecodingOptions-index?: int--><!--Device-DecodingOptions-index?: int-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

## rotate

```TypeScript
rotate?: int
```

Rotation angle. The default value is **0**.

**Type:** int

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-DecodingOptions-rotate?: int--><!--Device-DecodingOptions-rotate?: int-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

## sampleSize

```TypeScript
sampleSize?: int
```

Sampling size of the thumbnail. The default value is **1**. Currently, the value can only be **1**.

**Type:** int

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-DecodingOptions-sampleSize?: int--><!--Device-DecodingOptions-sampleSize?: int-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

