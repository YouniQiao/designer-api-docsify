# @ohos.multimedia.image

The module provides capabilities for image decoding, encoding, editing, metadata processing, and image receiving.This module contains the following classes:

- [ImageSource](arkts-image-image-imagesource-i.md#ImageSource): provides the capabilities of obtaining   
[image information](arkts-image-image-imageinfo-i.md#ImageInfo), decoding images to PixelMaps or Pictures, and reading and modifying [image properties](arkts-image-image-propertykey-e.md#PropertyKey).   
[Supported image formats for decoding](@ohos.multimedia.image: image.ImageSource#supportedFormats)include png, jpeg, bmp, gif, webp, dng, and heic&lt;sup&gt;12+&lt;/sup&gt;.  
- [ImagePacker](arkts-image-image-imagepacker-i.md#ImagePacker): provides the capability of encoding images into  
compressed data streams or files. Encoding requires the ImageSource, PixelMap, or Picture of an image as the input.   
[Supported image formats for encoding](@ohos.multimedia.image: image.ImagePacker#supportedFormats)include jpeg, webp, png, heic&lt;sup&gt;12+&lt;/sup&gt;, and gif&lt;sup&gt;18+&lt;/sup&gt;.  
- [PixelMap](arkts-image-image-pixelmap-i.md#PixelMap): contains pixel data and   
[image information](arkts-image-image-imageinfo-i.md#ImageInfo). It can be used for reading/writing pixel data and performing operations such as cropping, scaling, translating, rotating, and mirroring. It can also be directly passed to the [Image component](arkts-image-image-image-i.md#Image) for display. Additionally, it provides APIs for obtaining and setting the color gamut and HDR metadata of images.  
- [Picture](arkts-image-image-picture-i.md#Picture): a multi-picture object composed of a main picture,  
auxiliary pictures, and metadata. The main picture contains the primary image information; auxiliary pictures store additional information related to the main picture; metadata stores other information related to the image.Picture provides methods for obtaining the main picture, compositing HDR images, obtaining and setting auxiliary pictures, and obtaining and setting metadata.  
- [AuxiliaryPicture](arkts-image-image-auxiliarypicture-i.md#AuxiliaryPicture): used to display special information  
alongside the main picture, enriching the overall content of the image. The supported types of auxiliary pictures can be found in [AuxiliaryPictureType](arkts-image-image-auxiliarypicturetype-e.md#AuxiliaryPictureType).  
- [Metadata](arkts-image-image-metadata-i.md#Metadata): used to store image metadata. The supported metadata types  
can be found in [MetadataType](arkts-image-image-metadatatype-e.md#MetadataType). It includes Exif metadata and watermark cropping metadata, both stored in Key-Value pairs. The keys for Exif metadata can be found in  
[PropertyKey](arkts-image-image-propertykey-e.md#PropertyKey), and the keys for watermark cropping metadata can be found in [FragmentPropertyKey](arkts-image-image-fragmentmappropertykey-e.md#FragmentMapPropertyKey).  
- [ImageReceiver](arkts-image-image-imagereceiver-i.md#ImageReceiver): acts as a consumer of images, used for receiving  
and reading images from a surface.  
- [ImageCreator](arkts-image-image-imagecreator-i.md#ImageCreator): acts as a producer of images, used for writing  
images into a surface.  
- [Image](arkts-image-image-image-i.md#Image): used by ImageReceiver and ImageCreator for transferring image  
objects, with the actual content determined by the producer. For example, the Image object provided by a camera preview stream contains YUV data, whereas the Image object provided by a camera photo contains a JPEG file.

**Since:** 6

<!--Device-unnamed-declare namespace image--><!--Device-unnamed-declare namespace image-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## Modules to Import

```TypeScript
import { image } from '@kit.ImageKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [CreateIncrementalSource](arkts-image-image-createincrementalsource-f.md#createincrementalsource) |
| [CreateIncrementalSource](arkts-image-image-createincrementalsource-f.md#createincrementalsource-1) |
| [createAuxiliaryPicture](arkts-image-image-createauxiliarypicture-f.md#createauxiliarypicture) |
| [createAuxiliaryPictureUsingAllocator](arkts-image-image-createauxiliarypictureusingallocator-f.md#createauxiliarypictureusingallocator) |
| [createEmptyPixelMap](arkts-image-image-createemptypixelmap-f.md#createemptypixelmap) |
| [createImageCreator](arkts-image-image-createimagecreator-f.md#createimagecreator) |
| [createImageCreator](arkts-image-image-createimagecreator-f.md#createimagecreator-1) |
| [createImagePacker](arkts-image-image-createimagepacker-f.md#createimagepacker) |
| [createImageReceiver](arkts-image-image-createimagereceiver-f.md#createimagereceiver) |
| [createImageReceiver](arkts-image-image-createimagereceiver-f.md#createimagereceiver-1) |
| [createImageReceiver](arkts-image-image-createimagereceiver-f.md#createimagereceiver-2) |
| [createImageSource](arkts-image-image-createimagesource-f.md#createimagesource) |
| [createImageSource](arkts-image-image-createimagesource-f.md#createimagesource-1) |
| [createImageSource](arkts-image-image-createimagesource-f.md#createimagesource-2) |
| [createImageSource](arkts-image-image-createimagesource-f.md#createimagesource-3) |
| [createImageSource](arkts-image-image-createimagesource-f.md#createimagesource-4) |
| [createImageSource](arkts-image-image-createimagesource-f.md#createimagesource-5) |
| [createImageSource](arkts-image-image-createimagesource-f.md#createimagesource-6) |
| [createPicture](arkts-image-image-createpicture-f.md#createpicture) |
| [createPictureFromParcel](arkts-image-image-createpicturefromparcel-f.md#createpicturefromparcel) |
| [createPixelMap](arkts-image-image-createpixelmap-f.md#createpixelmap) |
| [createPixelMap](arkts-image-image-createpixelmap-f.md#createpixelmap-1) |
| [createPixelMapFromParcel](arkts-image-image-createpixelmapfromparcel-f.md#createpixelmapfromparcel) |
| [createPixelMapFromPixels](arkts-image-image-createpixelmapfrompixels-f.md#createpixelmapfrompixels) |
| [createPixelMapFromPixelsSync](arkts-image-image-createpixelmapfrompixelssync-f.md#createpixelmapfrompixelssync) |
| [createPixelMapFromSurface](arkts-image-image-createpixelmapfromsurface-f.md#createpixelmapfromsurface) |
| [createPixelMapFromSurface](arkts-image-image-createpixelmapfromsurface-f.md#createpixelmapfromsurface-1) |
| [createPixelMapFromSurfaceSync](arkts-image-image-createpixelmapfromsurfacesync-f.md#createpixelmapfromsurfacesync) |
| [createPixelMapFromSurfaceSync](arkts-image-image-createpixelmapfromsurfacesync-f.md#createpixelmapfromsurfacesync-1) |
| [createPixelMapFromSurfaceWithTransformation](arkts-image-image-createpixelmapfromsurfacewithtransformation-f.md#createpixelmapfromsurfacewithtransformation) |
| [createPixelMapFromSurfaceWithTransformationSync](arkts-image-image-createpixelmapfromsurfacewithtransformationsync-f.md#createpixelmapfromsurfacewithtransformationsync) |
| [createPixelMapSync](arkts-image-image-createpixelmapsync-f.md#createpixelmapsync) |
| [createPixelMapSync](arkts-image-image-createpixelmapsync-f.md#createpixelmapsync-1) |
| [createPixelMapUsingAllocator](arkts-image-image-createpixelmapusingallocator-f.md#createpixelmapusingallocator) |
| [createPixelMapUsingAllocatorSync](arkts-image-image-createpixelmapusingallocatorsync-f.md#createpixelmapusingallocatorsync) |
| [createPixelMapUsingAllocatorSync](arkts-image-image-createpixelmapusingallocatorsync-f.md#createpixelmapusingallocatorsync-1) |
| [createPremultipliedPixelMap](arkts-image-image-createpremultipliedpixelmap-f.md#createpremultipliedpixelmap) |
| [createPremultipliedPixelMap](arkts-image-image-createpremultipliedpixelmap-f.md#createpremultipliedpixelmap-1) |
| [createUnpremultipliedPixelMap](arkts-image-image-createunpremultipliedpixelmap-f.md#createunpremultipliedpixelmap) |
| [createUnpremultipliedPixelMap](arkts-image-image-createunpremultipliedpixelmap-f.md#createunpremultipliedpixelmap-1) |
| [getImagePackerSupportedFormats](arkts-image-image-getimagepackersupportedformats-f.md#getimagepackersupportedformats) |
| [getImageSourceSupportedFormats](arkts-image-image-getimagesourcesupportedformats-f.md#getimagesourcesupportedformats) |

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [createPictureByHdrAndSdrPixelMap](arkts-image-image-createpicturebyhdrandsdrpixelmap-f-sys.md#createpicturebyhdrandsdrpixelmap) |
| [createPictureByHdrAndSdrPixelMap](arkts-image-image-createpicturebyhdrandsdrpixelmap-f-sys.md#createpicturebyhdrandsdrpixelmap-1) |
| [decomposeToPicture](arkts-image-image-decomposetopicture-f-sys.md#decomposetopicture) |
<!--DelEnd-->

### Classes

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
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

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
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
### Interfaces（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [DecodingOptions](arkts-image-image-decodingoptions-i-sys.md) |
| [GainmapParams](arkts-image-image-gainmapparams-i-sys.md) |
| [HdrDecomposeOptions](arkts-image-image-hdrdecomposeoptions-i-sys.md) |
| [ImageSource](arkts-image-image-imagesource-i-sys.md) |
<!--DelEnd-->

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
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
### Enums（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [PropertyKey](arkts-image-image-propertykey-e-sys.md) |
| [ResolutionQuality](arkts-image-image-resolutionquality-e-sys.md) |
<!--DelEnd-->

### Types

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [HdrMetadataValue](arkts-image-image-hdrmetadatavalue-t.md) |

### Constants

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [CAPTURE_MODE_FRONT_LENS_NIGHT_VIEW](arkts-image-image-con.md#capture_mode_front_lens_night_view) |
| [CAPTURE_MODE_LIGHT_GRAFFITI](arkts-image-image-con.md#capture_mode_light_graffiti) |
| [CAPTURE_MODE_MOVING_PHOTO](arkts-image-image-con.md#capture_mode_moving_photo) |
| [CAPTURE_MODE_PANORAMA](arkts-image-image-con.md#capture_mode_panorama) |
| [CAPTURE_MODE_PORTRAIT](arkts-image-image-con.md#capture_mode_portrait) |
| [CAPTURE_MODE_PROFESSIONAL](arkts-image-image-con.md#capture_mode_professional) |
| [CAPTURE_MODE_REAR_LENS_NIGHT_VIEW](arkts-image-image-con.md#capture_mode_rear_lens_night_view) |
| [CAPTURE_MODE_SILKY_WATER](arkts-image-image-con.md#capture_mode_silky_water) |
| [CAPTURE_MODE_SNAP_SHOT](arkts-image-image-con.md#capture_mode_snap_shot) |
| [CAPTURE_MODE_STAR_TRACK](arkts-image-image-con.md#capture_mode_star_track) |
| [CAPTURE_MODE_SUPER_MACRO](arkts-image-image-con.md#capture_mode_super_macro) |
| [CAPTURE_MODE_TAIL_LIGHT](arkts-image-image-con.md#capture_mode_tail_light) |
| [CAPTURE_MODE_WIDEAPERTURE](arkts-image-image-con.md#capture_mode_wideaperture) |
| [DUBLIN_CORE](arkts-image-image-con.md#dublin_core) |
| [EXIF](arkts-image-image-con.md#exif) |
| [TIFF](arkts-image-image-con.md#tiff) |
| [XMAGE_WATERMARK_MODE_AT_THE_BOTTOM](arkts-image-image-con.md#xmage_watermark_mode_at_the_bottom) |
| [XMAGE_WATERMARK_MODE_BORDER](arkts-image-image-con.md#xmage_watermark_mode_border) |
| [XMP_BASIC](arkts-image-image-con.md#xmp_basic) |
| [XMP_RIGHTS](arkts-image-image-con.md#xmp_rights) |
