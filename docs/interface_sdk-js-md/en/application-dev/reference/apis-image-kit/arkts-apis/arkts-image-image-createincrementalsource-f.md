# CreateIncrementalSource

## Modules to Import

```TypeScript
import { image } from 'kits/@kit.ImageKit';
```

## CreateIncrementalSource

```TypeScript
function CreateIncrementalSource(buf: ArrayBuffer): ImageSource
```

Creates an ImageSource instance in incremental mode based on buffers. Such an instance does not support reading or writing of Exif information.Images occupy a large amount of memory. When you finish using an ImageSource instance, call [release](arkts-image-image-imagesource-i.md#release) to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.The ImageSource instance created in incremental mode supports the following capabilities (applicable to synchronous, callback, and promise modes):  
- Obtaining image information: Call  
[getImageInfo](arkts-image-image-imagesource-i.md#getimageinfo) to obtain image information by index, or call [getImageInfo](arkts-image-image-imagesource-i.md#getimageinfo) to directly obtain image information.  
- Obtaining an image property: Call  
[getImageProperty](arkts-image-image-imagesource-i.md#getimageproperty) to obtain the value of a property with the specified index in an image.  
- Obtaining image properties: Call  
[getImageProperties](arkts-image-image-imagesource-i.md#getimageproperties) to obtain the values of properties with the given names in an image.  
- Updating incremental data: Call  
[updateData](arkts-image-image-imagesource-i.md#updatedata).  
- Creating a PixelMap object: Call  
[createPixelMap](arkts-image-image-imagesource-i.md#createpixelmap) or [createPixelMap](arkts-image-image-imagesource-i.md#createpixelmap) to create a PixelMap object based on decoding options; call [createPixelMap](arkts-image-image-imagesource-i.md#createpixelmap) to create a PixelMap object based on default parameters.  
- Releasing an ImageSource instance: Call  
[release](arkts-image-image-imagesource-i.md#release).

**Since:** 9

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| buf | ArrayBuffer | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ImageSource](arkts-image-sendableimage-imagesource-i.md) |


## CreateIncrementalSource

```TypeScript
function CreateIncrementalSource(buf: ArrayBuffer, options?: SourceOptions): ImageSource
```

Creates an ImageSource instance in incremental mode based on buffers. Such an instance does not support reading or writing of Exif information.The capabilities supported by the ImageSource instance created by this API are the same as those supported by the instance created by [CreateIncrementalSource(buf: ArrayBuffer): ImageSource](#createincrementalsource). Images occupy a large amount of memory. When you finish using an ImageSource instance, call [release](arkts-image-image-imagesource-i.md#release) to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**Since:** 9

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| buf | ArrayBuffer | Yes |
| options | [SourceOptions](arkts-image-image-sourceoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ImageSource](arkts-image-sendableimage-imagesource-i.md) |
