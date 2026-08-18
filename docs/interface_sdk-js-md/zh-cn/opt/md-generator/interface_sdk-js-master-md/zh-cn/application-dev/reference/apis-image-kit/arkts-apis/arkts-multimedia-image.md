# @ohos.multimedia.image

本模块提供图片的解码、编码、编辑、元数据处理和图片接收等能力。 本模块包含以下基础类： - [ImageSource](arkts-image-image-imagesource-i.md#imagesource)类，提供获取[图片信息](arkts-image-image-imageinfo-i.md#imageinfo)、将图片解码为PixelMap或Picture、读取和修改 [图片属性](arkts-image-image-propertykey-e.md#propertykey)的能力。[支持解码的图片格式](../../../reference/apis-image-kit/arkts-apis-image-ImageSource.md#属性) 包括png、jpeg、bmp、gif、webp、dng、heic&lt;sup&gt;12+&lt;/sup&gt;、wbmp&lt;sup&gt;23+&lt;/sup&gt;、heifs&lt;sup&gt;23+&lt;/sup&gt;、tiff&lt;sup&gt;23+&lt;/sup&gt;。 - [ImagePacker](arkts-image-image-imagepacker-i.md#imagepacker)类，提供将图片编码为压缩后的数据流或文件的能力。编码前需获取图片的ImageSource、PixelMap或Picture作为输入。 [支持编码的图片格式](../../../reference/apis-image-kit/arkts-apis-image-ImagePacker.md#属性)包括jpeg、webp、png、heic&lt;sup&gt;12+&lt;/sup&gt;、 gif&lt;sup&gt;18+&lt;/sup&gt;。 - [PixelMap](arkts-image-image-pixelmap-i.md#pixelmap)类，位图对象，包含像素数据以及[图片信息](arkts-image-image-imageinfo-i.md#imageinfo)。可用于读取或写入像素数据，进行裁剪、缩放、平移、旋转、镜像等操作，并可直接传 给Image组件用于显示。还提供了获取和设置图片色域、HDR元数据的方法。 - [Picture](arkts-image-image-picture-i.md#picture)类，多图对象，由主图、辅助图和元数据组成。其中，主图包含了主要图像信息；辅助图用于存储与主图相关的附加信息；元数据用于存储与图片相关的其他信息。Picture提供获取主图 、合成HDR图、获取辅助图、设置辅助图、获取元数据、设置元数据等方法。 - [AuxiliaryPicture](arkts-image-image-auxiliarypicture-i.md#auxiliarypicture)类，辅助图一般用于辅助主图进行特殊信息的展示，使图像包含更丰富的信息。目前支持的辅助图的类型可参考 [AuxiliaryPictureType](arkts-image-image-auxiliarypicturetype-e.md#auxiliarypicturetype)。 - [Metadata](arkts-image-image-metadata-i.md#metadata)类，以Key-Value的形式存储图像的元数据。目前支持的元数据类型可参考[MetadataType](arkts-image-image-metadatatype-e.md#metadatatype)，包含 Exif元数据、水印裁剪图元数据和HEIF序列图像元数据。Exif元数据的Key可参考[PropertyKey](arkts-image-image-propertykey-e.md#propertykey)；水印裁剪图元数据的Key可参考 [FragmentMapPropertyKey](arkts-image-image-fragmentmappropertykey-e.md#fragmentmappropertykey)；HEIF序列图像元数据的Key可参考 [HeifsPropertyKey](arkts-image-image-heifspropertykey-e.md#heifspropertykey)。 - [ExifMetadata](arkts-image-image-exifmetadata-c.md#exifmetadata)类，以Key-Value的形式存储图像的Exif元数据。Exif元数据的Key可参考 [PropertyKey](arkts-image-image-propertykey-e.md#propertykey)。 - [MakerNoteHuaweiMetadata](arkts-image-image-makernotehuaweimetadata-c.md#makernotehuaweimetadata)类，以Key-Value的形式存储图像Huawei相机定义的照片元数据。Huawei相机定义的照片元数据的 Key可参考[PropertyKey](arkts-image-image-propertykey-e.md#propertykey)。 - [HeifsMetadata](arkts-image-image-heifsmetadata-c.md#heifsmetadata)类，以Key-Value的形式存储图像的HEIF序列图像元数据。HEIF序列图像元数据的Key可参考 [HeifsPropertyKey](arkts-image-image-heifspropertykey-e.md#heifspropertykey)。 - [WebPMetadata](../../../reference/apis-image-kit/arkts-apis-image-WebPMetadata.md)类，以Key-Value的形式存储图像的WebP图像元数据。 WebP图像元数据的Key可参考[WebPPropertyKey](arkts-image-image-webppropertykey-e.md#webppropertykey)。 - [GifMetadata](../../../reference/apis-image-kit/arkts-apis-image-GifMetadata.md)类，以Key-Value的形式存储图像的GIF图像元数据。GIF图像 元数据的Key可参考[GifPropertyKey](arkts-image-image-gifpropertykey-e.md#gifpropertykey)。 - [JfifMetadata](../../../reference/apis-image-kit/arkts-apis-image-JfifMetadata.md)类，以Key-Value的形式存储图像的JFIF图像元数据。 JFIF图像元数据的Key可参考[JfifPropertyKey](arkts-image-image-jfifpropertykey-e.md#jfifpropertykey)。 - [TiffMetadata](../../../reference/apis-image-kit/arkts-apis-image-TiffMetadata.md)类，以Key-Value的形式存储图像的TIFF图像元数据。 TIFF图像元数据的Key可参考[TiffPropertyKey](arkts-image-image-tiffpropertykey-e.md#tiffpropertykey)。 - [PngMetadata](../../../reference/apis-image-kit/arkts-apis-image-PngMetadata.md)类，以Key-Value的形式存储图像的PNG图像元数据。PNG图像 元数据的Key可参考[PngPropertyKey](arkts-image-image-pngpropertykey-e.md#pngpropertykey)。 - [AvisMetadata](../../../reference/apis-image-kit/arkts-apis-image-AvisMetadata.md)类，以Key-Value的形式存储图像的AVIS图像元数据。 AVIS图像元数据的Key可参考[AvisPropertyKey](arkts-image-image-avispropertykey-e.md#avispropertykey)。 - [ImageReceiver](arkts-image-image-imagereceiver-i.md#imagereceiver)类，作为图片的消费者，用于从Surface中接收、读取图片。 - [ImageCreator](arkts-image-image-imagecreator-i.md#imagecreator)类，作为图片的生产者，用于将图片写入到Surface中。 - [Image](arkts-image-image-image-i.md#image)类，供ImageReceiver和ImageCreator使用，用于传输图片对象，其实际内容由生产者决定。如相机预览流提供的Image对象存储了YUV数据、相机拍照提供的 Image对象存储了JPEG文件。

**起始版本：** 23

<!--Device-unnamed-declare namespace image--><!--Device-unnamed-declare namespace image-End-->

**系统能力：** 
- API版本11+：SystemCapability.Multimedia.Image.Core

## 导入模块

```TypeScript
```

## 汇总

### 函数

| 名称 |
| --- |
| [CreateIncrementalSource](arkts-image-image-createincrementalsource-f.md#createincrementalsource) |
| [CreateIncrementalSource](arkts-image-image-createincrementalsource-f.md#createincrementalsource) |
| [createAuxiliaryPicture](arkts-image-image-createauxiliarypicture-f.md#createauxiliarypicture) |
| [createAuxiliaryPictureUsingAllocator](arkts-image-image-createauxiliarypictureusingallocator-f.md#createauxiliarypictureusingallocator) |
| [createEmptyPixelMap](arkts-image-image-createemptypixelmap-f.md#createemptypixelmap) |
| [createImageCreator](arkts-image-image-createimagecreator-f.md#createimagecreator) |
| [createImageCreator](arkts-image-image-createimagecreator-f.md#createimagecreator) |
| [createImagePacker](arkts-image-image-createimagepacker-f.md#createimagepacker) |
| [createImageReceiver](arkts-image-image-createimagereceiver-f.md#createimagereceiver) |
| [createImageReceiver](arkts-image-image-createimagereceiver-f.md#createimagereceiver) |
| [createImageReceiver](arkts-image-image-createimagereceiver-f.md#createimagereceiver) |
| [createImageReceiver](arkts-image-image-createimagereceiver-f.md#createimagereceiver) |
| [createImageSource](arkts-image-image-createimagesource-f.md#createimagesource) |
| [createImageSource](arkts-image-image-createimagesource-f.md#createimagesource) |
| [createImageSource](arkts-image-image-createimagesource-f.md#createimagesource) |
| [createImageSource](arkts-image-image-createimagesource-f.md#createimagesource) |
| [createImageSource](arkts-image-image-createimagesource-f.md#createimagesource) |
| [createImageSource](arkts-image-image-createimagesource-f.md#createimagesource) |
| [createImageSource](arkts-image-image-createimagesource-f.md#createimagesource) |
| [createImageSource](arkts-image-image-createimagesource-f.md#createimagesource) |
| [createImageSource](arkts-image-image-createimagesource-f.md#createimagesource) |
| [createImageSource](arkts-image-image-createimagesource-f.md#createimagesource) |
| [createImageSource](arkts-image-image-createimagesource-f.md#createimagesource) |
| [createImageSource](arkts-image-image-createimagesource-f.md#createimagesource) |
| [createImageSource](arkts-image-image-createimagesource-f.md#createimagesource) |
| [createImageSource](arkts-image-image-createimagesource-f.md#createimagesource) |
| [createIncrementalSource](arkts-image-image-createincrementalsource-f.md#createincrementalsource) |
| [createIncrementalSource](arkts-image-image-createincrementalsource-f.md#createincrementalsource) |
| [createPicture](arkts-image-image-createpicture-f.md#createpicture) |
| [createPictureFromParcel](arkts-image-image-createpicturefromparcel-f.md#createpicturefromparcel) |
| [createPixelMap](arkts-image-image-createpixelmap-f.md#createpixelmap) |
| [createPixelMap](arkts-image-image-createpixelmap-f.md#createpixelmap) |
| [createPixelMapFromParcel](arkts-image-image-createpixelmapfromparcel-f.md#createpixelmapfromparcel) |
| [createPixelMapFromPixels](arkts-image-image-createpixelmapfrompixels-f.md#createpixelmapfrompixels) |
| [createPixelMapFromPixelsSync](arkts-image-image-createpixelmapfrompixelssync-f.md#createpixelmapfrompixelssync) |
| [createPixelMapFromSurface](arkts-image-image-createpixelmapfromsurface-f.md#createpixelmapfromsurface) |
| [createPixelMapFromSurface](arkts-image-image-createpixelmapfromsurface-f.md#createpixelmapfromsurface) |
| [createPixelMapFromSurfaceSync](arkts-image-image-createpixelmapfromsurfacesync-f.md#createpixelmapfromsurfacesync) |
| [createPixelMapFromSurfaceSync](arkts-image-image-createpixelmapfromsurfacesync-f.md#createpixelmapfromsurfacesync) |
| [createPixelMapFromSurfaceWithTransformation](arkts-image-image-createpixelmapfromsurfacewithtransformation-f.md#createpixelmapfromsurfacewithtransformation) |
| [createPixelMapFromSurfaceWithTransformationSync](arkts-image-image-createpixelmapfromsurfacewithtransformationsync-f.md#createpixelmapfromsurfacewithtransformationsync) |
| [createPixelMapSync](arkts-image-image-createpixelmapsync-f.md#createpixelmapsync) |
| [createPixelMapSync](arkts-image-image-createpixelmapsync-f.md#createpixelmapsync) |
| [createPixelMapUsingAllocator](arkts-image-image-createpixelmapusingallocator-f.md#createpixelmapusingallocator) |
| [createPixelMapUsingAllocatorSync](arkts-image-image-createpixelmapusingallocatorsync-f.md#createpixelmapusingallocatorsync) |
| [createPixelMapUsingAllocatorSync](arkts-image-image-createpixelmapusingallocatorsync-f.md#createpixelmapusingallocatorsync) |
| [createPremultipliedPixelMap](arkts-image-image-createpremultipliedpixelmap-f.md#createpremultipliedpixelmap) |
| [createPremultipliedPixelMap](arkts-image-image-createpremultipliedpixelmap-f.md#createpremultipliedpixelmap) |
| [createUnpremultipliedPixelMap](arkts-image-image-createunpremultipliedpixelmap-f.md#createunpremultipliedpixelmap) |
| [createUnpremultipliedPixelMap](arkts-image-image-createunpremultipliedpixelmap-f.md#createunpremultipliedpixelmap) |
| [getImagePackerSupportedFormats](arkts-image-image-getimagepackersupportedformats-f.md#getimagepackersupportedformats) |
| [getImageSourceSupportedFormats](arkts-image-image-getimagesourcesupportedformats-f.md#getimagesourcesupportedformats) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [createPictureByHdrAndSdrPixelMap](arkts-image-image-createpicturebyhdrandsdrpixelmap-f-sys.md#createpicturebyhdrandsdrpixelmap系统接口) |
| [createPictureByHdrAndSdrPixelMap](arkts-image-image-createpicturebyhdrandsdrpixelmap-f-sys.md#createpicturebyhdrandsdrpixelmap系统接口) |
| [decomposeToPicture](arkts-image-image-decomposetopicture-f-sys.md#decomposetopicture系统接口) |
<!--DelEnd-->

### 类

| 名称 |
| --- |
| [AvisMetadata](arkts-image-image-avismetadata-c.md) |
| [DngMetadata](arkts-image-image-dngmetadata-c.md) |
| [ExifMetadata](arkts-image-image-exifmetadata-c.md) |
| [GifMetadata](arkts-image-image-gifmetadata-c.md) |
| [HeifsMetadata](arkts-image-image-heifsmetadata-c.md) |
| [JfifMetadata](arkts-image-image-jfifmetadata-c.md) |
| [MakerNoteHuaweiMetadata](arkts-image-image-makernotehuaweimetadata-c.md) |
| [PngMetadata](arkts-image-image-pngmetadata-c.md) |
| [TiffMetadata](arkts-image-image-tiffmetadata-c.md) |
| [WebPMetadata](arkts-image-image-webpmetadata-c.md) |
| [XMPMetadata](arkts-image-image-xmpmetadata-c.md) |

### 接口

| 名称 |
| --- |
| [AuxiliaryPicture](arkts-image-image-auxiliarypicture-i.md) |
| [AuxiliaryPictureInfo](arkts-image-image-auxiliarypictureinfo-i.md) |
| [BinaryBufferInfo](arkts-image-image-binarybufferinfo-i.md) |
| [Component](arkts-image-image-component-i.md) |
| [DecodingOptions](arkts-image-image-decodingoptions-i.md) |
| [DecodingOptionsForPicture](arkts-image-image-decodingoptionsforpicture-i.md) |
| [DecodingOptionsForThumbnail](arkts-image-image-decodingoptionsforthumbnail-i.md) |
| [GainmapChannel](arkts-image-image-gainmapchannel-i.md) |
| [GetImagePropertyOptions](arkts-image-image-getimagepropertyoptions-i.md) |
| [HdrComposeOptions](arkts-image-image-hdrcomposeoptions-i.md) |
| [HdrGainmapMetadata](arkts-image-image-hdrgainmapmetadata-i.md) |
| [HdrStaticMetadata](arkts-image-image-hdrstaticmetadata-i.md) |
| [Image](arkts-image-image-image-i.md) |
| [ImageBufferData](arkts-image-image-imagebufferdata-i.md) |
| [ImageCreator](arkts-image-image-imagecreator-i.md) |
| [ImageInfo](arkts-image-image-imageinfo-i.md) |
| [ImageMetadata](arkts-image-image-imagemetadata-i.md) |
| [ImagePacker](arkts-image-image-imagepacker-i.md) |
| [ImagePropertyOptions](arkts-image-image-imagepropertyoptions-i.md) |
| [ImageRawData](arkts-image-image-imagerawdata-i.md) |
| [ImageReceiver](arkts-image-image-imagereceiver-i.md) |
| [ImageReceiverOptions](arkts-image-image-imagereceiveroptions-i.md) |
| [ImageSource](arkts-image-image-imagesource-i.md) |
| [InitializationOptions](arkts-image-image-initializationoptions-i.md) |
| [Metadata](arkts-image-image-metadata-i.md) |
| [PackingOption](arkts-image-image-packingoption-i.md) |
| [PackingOptionsForSequence](arkts-image-image-packingoptionsforsequence-i.md) |
| [PackingOptionsForTiff](arkts-image-image-packingoptionsfortiff-i.md) |
| [PackingSizeLimit](arkts-image-image-packingsizelimit-i.md) |
| [Picture](arkts-image-image-picture-i.md) |
| [PixelMap](arkts-image-image-pixelmap-i.md) |
| [PositionArea](arkts-image-image-positionarea-i.md) |
| [Region](arkts-image-image-region-i.md) |
| [Size](arkts-image-image-size-i.md) |
| [SourceOptions](arkts-image-image-sourceoptions-i.md) |
| [XMPEnumerateOptions](arkts-image-image-xmpenumerateoptions-i.md) |
| [XMPNamespace](arkts-image-image-xmpnamespace-i.md) |
| [XMPTag](arkts-image-image-xmptag-i.md) |

<!--Del-->
### 接口（系统接口）

| 名称 |
| --- |
| [DecodingOptions](arkts-image-image-decodingoptions-i-sys.md) |
| [GainmapParams](arkts-image-image-gainmapparams-i-sys.md) |
| [HdrDecomposeOptions](arkts-image-image-hdrdecomposeoptions-i-sys.md) |
| [ImageSource](arkts-image-image-imagesource-i-sys.md) |
<!--DelEnd-->

### 枚举

| 名称 |
| --- |
| [AllocatorType](arkts-image-image-allocatortype-e.md) |
| [AlphaType](arkts-image-image-alphatype-e.md) |
| [AntiAliasingLevel](arkts-image-image-antialiasinglevel-e.md) |
| [AuxiliaryPictureType](arkts-image-image-auxiliarypicturetype-e.md) |
| [AvisPropertyKey](arkts-image-image-avispropertykey-e.md) |
| [ComponentType](arkts-image-image-componenttype-e.md) |
| [CropAndScaleStrategy](arkts-image-image-cropandscalestrategy-e.md) |
| [DecodingDynamicRange](arkts-image-image-decodingdynamicrange-e.md) |
| [DngPropertyKey](arkts-image-image-dngpropertykey-e.md) |
| [FocusMode](arkts-image-image-focusmode-e.md) |
| [FragmentMapPropertyKey](arkts-image-image-fragmentmappropertykey-e.md) |
| [GifPropertyKey](arkts-image-image-gifpropertykey-e.md) |
| [HdrMetadataKey](arkts-image-image-hdrmetadatakey-e.md) |
| [HdrMetadataType](arkts-image-image-hdrmetadatatype-e.md) |
| [HeifsPropertyKey](arkts-image-image-heifspropertykey-e.md) |
| [ImageFormat](arkts-image-image-imageformat-e.md) |
| [JfifPropertyKey](arkts-image-image-jfifpropertykey-e.md) |
| [MetadataType](arkts-image-image-metadatatype-e.md) |
| [Orientation](arkts-image-image-orientation-e.md) |
| [PackingDynamicRange](arkts-image-image-packingdynamicrange-e.md) |
| [PixelMapFormat](arkts-image-image-pixelmapformat-e.md) |
| [PngPropertyKey](arkts-image-image-pngpropertykey-e.md) |
| [PropertyKey](arkts-image-image-propertykey-e.md) |
| [ScaleMode](arkts-image-image-scalemode-e.md) |
| [TiffPropertyKey](arkts-image-image-tiffpropertykey-e.md) |
| [WebPPropertyKey](arkts-image-image-webppropertykey-e.md) |
| [XMPTagType](arkts-image-image-xmptagtype-e.md) |
| [XmageColorMode](arkts-image-image-xmagecolormode-e.md) |

<!--Del-->
### 枚举（系统接口）

| 名称 |
| --- |
| [PropertyKey](arkts-image-image-propertykey-e-sys.md) |
| [ResolutionQuality](arkts-image-image-resolutionquality-e-sys.md) |
<!--DelEnd-->

### 类型

| 名称 |
| --- |
| [HdrMetadataValue](arkts-image-image-hdrmetadatavalue-t.md) |

### 常量

| 名称 |
| --- |
| [CAPTURE_MODE_FRONT_LENS_NIGHT_VIEW](arkts-image-image-con.md#capturemodefrontlensnightview) |
| [CAPTURE_MODE_LIGHT_GRAFFITI](arkts-image-image-con.md#capturemodelightgraffiti) |
| [CAPTURE_MODE_MOVING_PHOTO](arkts-image-image-con.md#capturemodemovingphoto) |
| [CAPTURE_MODE_PANORAMA](arkts-image-image-con.md#capturemodepanorama) |
| [CAPTURE_MODE_PORTRAIT](arkts-image-image-con.md#capturemodeportrait) |
| [CAPTURE_MODE_PROFESSIONAL](arkts-image-image-con.md#capturemodeprofessional) |
| [CAPTURE_MODE_REAR_LENS_NIGHT_VIEW](arkts-image-image-con.md#capturemoderearlensnightview) |
| [CAPTURE_MODE_SILKY_WATER](arkts-image-image-con.md#capturemodesilkywater) |
| [CAPTURE_MODE_SNAP_SHOT](arkts-image-image-con.md#capturemodesnapshot) |
| [CAPTURE_MODE_STAR_TRACK](arkts-image-image-con.md#capturemodestartrack) |
| [CAPTURE_MODE_SUPER_MACRO](arkts-image-image-con.md#capturemodesupermacro) |
| [CAPTURE_MODE_TAIL_LIGHT](arkts-image-image-con.md#capturemodetaillight) |
| [CAPTURE_MODE_WIDEAPERTURE](arkts-image-image-con.md#capturemodewideaperture) |
| [DUBLIN_CORE](arkts-image-image-con.md#dublincore) |
| [EXIF](arkts-image-image-con.md#exif) |
| [TIFF](arkts-image-image-con.md#tiff) |
| [XMAGE_WATERMARK_MODE_AT_THE_BOTTOM](arkts-image-image-con.md#xmagewatermarkmodeatthebottom) |
| [XMAGE_WATERMARK_MODE_BORDER](arkts-image-image-con.md#xmagewatermarkmodeborder) |
| [XMP_BASIC](arkts-image-image-con.md#xmpbasic) |
| [XMP_RIGHTS](arkts-image-image-con.md#xmprights) |
