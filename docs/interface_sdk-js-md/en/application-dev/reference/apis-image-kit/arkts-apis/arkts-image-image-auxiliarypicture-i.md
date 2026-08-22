# AuxiliaryPicture

The **AuxiliaryPicture** class is used to read or write auxiliary picture data of an image and obtain auxiliary picture information of an image. The supported types of auxiliary pictures can be found in [AuxiliaryPictureType](arkts-image-image-auxiliarypicturetype-e.md).

Before calling any API in AuxiliaryPicture, you must create an AuxiliaryPicture instance using [image.createAuxiliaryPicture](arkts-image-image-createauxiliarypicture-f.md) or [getAuxiliaryPicture](arkts-image-image-picture-i.md#getauxiliarypicture) in Picture.

Images occupy a large amount of memory. When you finish using an AuxiliaryPicture instance, call [release](#release) to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**Since:** 23

<!--Device-image-interface AuxiliaryPicture--><!--Device-image-interface AuxiliaryPicture-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## Modules to Import

```TypeScript
import { image } from '@kit.ImageKit';
```

## getAuxiliaryPictureInfo

```TypeScript
getAuxiliaryPictureInfo(): AuxiliaryPictureInfo
```

Obtains the auxiliary picture information.

**Since:** 13

<!--Device-AuxiliaryPicture-getAuxiliaryPictureInfo(): AuxiliaryPictureInfo--><!--Device-AuxiliaryPicture-getAuxiliaryPictureInfo(): AuxiliaryPictureInfo-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Return value:**

| Type | Description |
| --- | --- |
| [AuxiliaryPictureInfo](arkts-image-image-auxiliarypictureinfo-i.md) | Auxiliary picture information. |

## getAuxiliaryPictureInfo

```TypeScript
getAuxiliaryPictureInfo(): AuxiliaryPictureInfo | undefined
```

Obtains the information about this auxiliary picture.

**Since:** 23

<!--Device-AuxiliaryPicture-getAuxiliaryPictureInfo(): AuxiliaryPictureInfo | undefined--><!--Device-AuxiliaryPicture-getAuxiliaryPictureInfo(): AuxiliaryPictureInfo | undefined-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Return value:**

| Type | Description |
| --- | --- |
| [AuxiliaryPictureInfo](arkts-image-image-auxiliarypictureinfo-i.md) \| undefined | Returns the auxiliary picture information. If the operation fails, an error message is returned. |

## getMetadata

```TypeScript
getMetadata(metadataType: MetadataType): Promise<Metadata>
```

Obtains the metadata of this auxiliary picture. This API uses a promise to return the result.

**Since:** 13

<!--Device-AuxiliaryPicture-getMetadata(metadataType: MetadataType): Promise<Metadata>--><!--Device-AuxiliaryPicture-getMetadata(metadataType: MetadataType): Promise<Metadata>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| metadataType | [MetadataType](arkts-image-image-metadatatype-e.md) | Yes | Metadata type, which is used to obtain metadata of the corresponding type. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Metadata&gt; | Promise that returns the metadata. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| [7600202](../errorcode-image.md#7600202-unsupported-metadata-readwrite-operation) | Unsupported metadata. Possible causes: 1. Unsupported metadata type. 2. The metadata type does not match the auxiliary picture type. |

**Examples**

```TypeScript
async function GetAuxPictureObjMetadata(auxPictureObj: image.AuxiliaryPicture) {
  if (auxPictureObj != null) {
    let metadataType: image.MetadataType = image.MetadataType.EXIF_METADATA;
    let auxPictureObjMetaData: image.Metadata | null = await auxPictureObj.getMetadata(metadataType);
    if (auxPictureObjMetaData != null) {
      console.info('Get AuxPictureObj Metadata success' );
    } else {
      console.error('Get AuxPictureObj Metadata failed');
    }
  } else {
    console.error('Get AuxPictureObj is null.');
  }
}
```

```TypeScript
async function GetMetadata(img : image.Image) {
  try {
    let staticMetadata = img.getMetadata(image.HdrMetadataKey.HDR_STATIC_METADATA);
    console.info(`getMetadata:${staticMetadata}`);
  } catch (err) {
    console.error('getMetadata failed' + err);
  }
}
```

```TypeScript
async function GetPictureObjMetadataProperties(pictureObj : image.Picture) {
  if (pictureObj != null) {
    let metadataType: image.MetadataType = image.MetadataType.EXIF_METADATA;
    let pictureObjMetaData: image.Metadata = await pictureObj.getMetadata(metadataType);
    if (pictureObjMetaData != null) {
      console.info('get picture metadata success');
    } else {
      console.error('get picture metadata is failed');
    }
  } else {
    console.error(" pictureObj is null");
  }
}
```

```TypeScript
async function GetMetadata(context: Context) {
  // Replace app.media.startIcon with a local HDR image.
  let img = context.resourceManager.getMediaContentSync($r('app.media.startIcon').id);
  let imageSource = image.createImageSource(img.buffer.slice(0));
  let decodingOptions: image.DecodingOptions = {
    desiredDynamicRange: image.DecodingDynamicRange.AUTO
  };
  let pixelmap = imageSource.createPixelMapSync(decodingOptions);
  if (pixelmap != undefined) {
    console.info('Succeeded in creating pixelMap object.');
    try {
      let staticMetadata = pixelmap.getMetadata(image.HdrMetadataKey.HDR_STATIC_METADATA);
      console.info(`getMetadata:${staticMetadata}`);
    } catch (e) {
      console.error('pixelmap create failed' + e);
    }
  } else {
    console.error('Failed to create pixelMap.');
  }
}
```

## getMetadata

```TypeScript
getMetadata(metadataType: MetadataType): Promise<Metadata | undefined>
```

Obtains the metadata of auxiliary picture.

**Since:** 23

<!--Device-AuxiliaryPicture-getMetadata(metadataType: MetadataType): Promise<Metadata | undefined>--><!--Device-AuxiliaryPicture-getMetadata(metadataType: MetadataType): Promise<Metadata | undefined>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| metadataType | [MetadataType](arkts-image-image-metadatatype-e.md) | Yes | The type of metadata. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Metadata \| undefined&gt; | Return the metadata of auxiliary picture. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7600202](../errorcode-image.md#7600202-unsupported-metadata-readwrite-operation) | Unsupported metadata. Possible causes: 1. Unsupported metadata type. 2. The metadata type does not match the auxiliary picture type. |

**Examples**

See [getMetadata](#getmetadata)

## getType

```TypeScript
getType(): AuxiliaryPictureType
```

Obtains the type of this auxiliary picture.

**Since:** 13

<!--Device-AuxiliaryPicture-getType(): AuxiliaryPictureType--><!--Device-AuxiliaryPicture-getType(): AuxiliaryPictureType-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Return value:**

| Type | Description |
| --- | --- |
| [AuxiliaryPictureType](arkts-image-image-auxiliarypicturetype-e.md) | Type of the auxiliary picture. |

**Examples**

```TypeScript
async function GetAuxiliaryPictureType(auxPictureObj : image.AuxiliaryPicture) {
  if (auxPictureObj != null) {
    let type: image.AuxiliaryPictureType = auxPictureObj.getType();
    console.info('Success get auxiliary picture type ' +  JSON.stringify(type));
  } else {
    console.error('Failed get auxiliary picture type ');
  }
}
```

## getType

```TypeScript
getType(): AuxiliaryPictureType | undefined
```

Obtains the type of auxiliary picture.

**Since:** 23

<!--Device-AuxiliaryPicture-getType(): AuxiliaryPictureType | undefined--><!--Device-AuxiliaryPicture-getType(): AuxiliaryPictureType | undefined-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Return value:**

| Type | Description |
| --- | --- |
| [AuxiliaryPictureType](arkts-image-image-auxiliarypicturetype-e.md) \| undefined | Returns the type of auxiliary picture. |

**Examples**

See [getType](#gettype)

## readPixelsToBuffer

```TypeScript
readPixelsToBuffer(): Promise<ArrayBuffer>
```

Reads pixels of this auxiliary picture and writes the data to an ArrayBuffer. This API uses a promise to return the result.

**Since:** 13

<!--Device-AuxiliaryPicture-readPixelsToBuffer(): Promise<ArrayBuffer>--><!--Device-AuxiliaryPicture-readPixelsToBuffer(): Promise<ArrayBuffer>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;ArrayBuffer&gt; | Promise used to return the pixels of the auxiliary picture. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function ReadPixelsToBuffer(context: Context) {
  const resourceMgr = context.resourceManager;
  const rawFile = await resourceMgr.getRawFileContent("hdr.jpg"); // An HDR-compatible image is required.
  let ops: image.SourceOptions = {
    sourceDensity: 98,
  }
  let imageSource: image.ImageSource = image.createImageSource(rawFile.buffer as ArrayBuffer, ops);
  let commodityPixelMap: image.PixelMap = await imageSource.createPixelMap();
  let pictureObj: image.Picture = image.createPicture(commodityPixelMap);
  let auxPictureObj: image.AuxiliaryPicture | null = pictureObj.getAuxiliaryPicture(image.AuxiliaryPictureType.GAINMAP);
  if(auxPictureObj != null) {
    await auxPictureObj.readPixelsToBuffer().then((pixelsBuffer: ArrayBuffer) => {
      console.info('Read pixels to buffer success.' );
    }).catch((error: BusinessError) => {
      console.error(`Read pixels to buffer failed error.code: ${error.code}, error.message: ${error.message}`);
    });
  } else {
    console.error('AuxPictureObj is null.');
  }
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function ReadPixelsToBuffer(pixelMap : image.PixelMap) {
  const readBuffer: ArrayBuffer = new ArrayBuffer(96); // 96 is the size of the pixel buffer to create. The value is calculated as follows: height * width *4.
  if (pixelMap != undefined) {
    pixelMap.readPixelsToBuffer(readBuffer).then(() => {
      console.info('Succeeded in reading image pixel data.'); // Called if the condition is met.
    }).catch((error: BusinessError) => {
      console.error(`Failed to read image pixel data. code is ${error.code}, message is ${error.message}`); // Called if no condition is met.
    })
  }
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function ReadPixelsToBuffer(pixelMap : image.PixelMap) {
  const readBuffer: ArrayBuffer = new ArrayBuffer(96); // 96 is the size of the pixel buffer to create. The value is calculated as follows: height * width *4.
  if (pixelMap != undefined) {
    pixelMap.readPixelsToBuffer(readBuffer, (error: BusinessError, res: void) => {
      if(error) {
        console.error(`Failed to read image pixel data. code is ${error.code}, message is ${error.message}`); // Called if no condition is met.
        return;
      } else {
        console.info('Succeeded in reading image pixel data.'); // Called if the condition is met.
      }
    })
  }
}
```

## readPixelsToBuffer

```TypeScript
readPixelsToBuffer(): Promise<ArrayBuffer | undefined>
```

Reads image pixel map data and writes the data to an ArrayBuffer. This method uses a promise to return the result.

**Since:** 23

<!--Device-AuxiliaryPicture-readPixelsToBuffer(): Promise<ArrayBuffer | undefined>--><!--Device-AuxiliaryPicture-readPixelsToBuffer(): Promise<ArrayBuffer | undefined>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;ArrayBuffer \| undefined&gt; | A Promise instance used to return the pixel map data. |

**Examples**

See [readPixelsToBuffer](#readpixelstobuffer)

## release

```TypeScript
release():void
```

Releases this AuxiliaryPicture object. No value is returned.

Images occupy a large amount of memory. When you finish using an AuxiliaryPicture instance, call this API to free the memory promptly.

Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**Since:** 23

<!--Device-AuxiliaryPicture-release():void--><!--Device-AuxiliaryPicture-release():void-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Examples**

```TypeScript
async function Release(auxPictureObj: image.AuxiliaryPicture) {
  let funcName = "Release";
  if (auxPictureObj != null) {
    auxPictureObj.release();
    if (auxPictureObj.getType() == null) {
      console.info(funcName, 'Success !');
    } else {
      console.error(funcName, 'Failed !');
    }
  } else {
    console.error('PictureObj is null');
  }
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function Release(img : image.Image) {
  img.release((err: BusinessError) => {
    if (err) {
      console.error(`Failed to release the image instance.code ${err.code},message is ${err.message}`);
    } else {
      console.info('Succeeded in releasing the image instance.');
    }
  })
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function Release(img : image.Image) {
  img.release().then(() => {
    console.info('Succeeded in releasing the image instance.');
  }).catch((error: BusinessError) => {
    console.error(`Failed to release the image instance.code ${error.code},message is ${error.message}`);
  })
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function Release(creator : image.ImageCreator) {
  creator.release((err: BusinessError) => {
    if (err) {
      console.error(`Failed to release the creator.code ${err.code},message is ${err.message}`);
    } else {
      console.info('Succeeded in releasing creator.');
    }
  });
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function Release(creator : image.ImageCreator) {
  creator.release().then(() => {
    console.info('Succeeded in releasing creator.');
  }).catch((error: BusinessError) => {
    console.error(`Failed to release the creator.code ${error.code},message is ${error.message}`);
  })
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function Release() {
  const imagePackerObj: image.ImagePacker = image.createImagePacker();
  imagePackerObj.release((err: BusinessError)=>{
    if (err) {
      console.error(`Failed to release image packaging.code ${err.code},message is ${err.message}`);
    } else {
      console.info('Succeeded in releasing image packaging.');
    }
  })
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function Release() {
  const imagePackerObj: image.ImagePacker = image.createImagePacker();
  imagePackerObj.release().then(() => {
    console.info('Succeeded in releasing image packaging.');
  }).catch((error: BusinessError) => {
    console.error(`Failed to release image packaging.code ${error.code},message is ${error.message}`);
  })
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function Release(receiver : image.ImageReceiver) {
  receiver.release((err: BusinessError) => {
    if (err) {
      console.error(`Failed to release the receiver.code ${err.code},message is ${err.message}`);
    } else {
      console.info('Succeeded in releasing the receiver.');
    }
  })
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function Release(receiver : image.ImageReceiver) {
  receiver.release().then(() => {
    console.info('Succeeded in releasing the receiver.');
  }).catch((error: BusinessError) => {
    console.error(`Failed to release the receiver.code ${error.code},message is ${error.message}`);
  })
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function Release(imageSourceObj : image.ImageSource) {
  imageSourceObj.release((err: BusinessError) => {
    if (err) {
      console.error(`Failed to release the image source instance.code ${err.code},message is ${err.message}`);
    } else {
      console.info('Succeeded in releasing the image source instance.');
    }
  })
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function Release(imageSourceObj : image.ImageSource) {
  imageSourceObj.release().then(() => {
    console.info('Succeeded in releasing the image source instance.');
  }).catch((error: BusinessError) => {
    console.error(`Failed to release the image source instance.code ${error.code},message is ${error.message}`);
  })
}
```

```TypeScript
async function Release(pictureObj : image.Picture) {
  let funcName = "Release";
  if (pictureObj != null) {
    pictureObj.release();
    if (pictureObj.getMainPixelmap() == null) {
      console.info(funcName, 'Success !');
    } else {
      console.error(funcName, 'Failed !');
    }
  } else {
    console.error('PictureObj is null');
  }
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function Release(pixelMap:image.PixelMap) {
  if (pixelMap != undefined) {
    await pixelMap.release().then(() => {
      console.info('Succeeded in releasing pixelmap object.');
    }).catch((error: BusinessError) => {
      console.error(`Failed to release pixelmap object. code is ${error.code}, message is ${error.message}`);
    })
  }
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function Release(pixelMap:image.PixelMap) {
  if (pixelMap != undefined) {
    pixelMap.release((err: BusinessError) => {
      if (err) {
        console.error(`Failed to release pixelmap object. code is ${err.code}, message is ${err.message}`);
        return;
      } else {
        console.info('Succeeded in releasing pixelmap object.');
      }
    })
  }
}
```

## setAuxiliaryPictureInfo

```TypeScript
setAuxiliaryPictureInfo(info: AuxiliaryPictureInfo): void
```

Sets the auxiliary picture information.

**Since:** 23

<!--Device-AuxiliaryPicture-setAuxiliaryPictureInfo(info: AuxiliaryPictureInfo): void--><!--Device-AuxiliaryPicture-setAuxiliaryPictureInfo(info: AuxiliaryPictureInfo): void-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| info | [AuxiliaryPictureInfo](arkts-image-image-auxiliarypictureinfo-i.md) | Yes | Auxiliary picture information. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |

## setMetadata

```TypeScript
setMetadata(metadataType: MetadataType, metadata: Metadata): Promise<void>
```

Sets the metadata for this auxiliary picture. This API uses a promise to return the result.

**Since:** 23

<!--Device-AuxiliaryPicture-setMetadata(metadataType: MetadataType, metadata: Metadata): Promise<void>--><!--Device-AuxiliaryPicture-setMetadata(metadataType: MetadataType, metadata: Metadata): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| metadataType | [MetadataType](arkts-image-image-metadatatype-e.md) | Yes | Metadata type, which is used to set the corresponding metadata. |
| metadata | Metadata | Yes | Metadata object. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| [7600202](../errorcode-image.md#7600202-unsupported-metadata-readwrite-operation) | Unsupported metadata. Possible causes: 1. Unsupported metadata type. 2. The metadata type does not match the auxiliary picture type. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function SetAuxPictureObjMetadata(exifContext: Context, auxPictureObj: image.AuxiliaryPicture) {
  const exifResourceMgr = exifContext.resourceManager;
  const exifRawFile = await exifResourceMgr.getRawFileContent("exif.jpg"); // An image containing Exif metadata is required.
  let exifOps: image.SourceOptions = {
    sourceDensity: 98,
  }
  let exifImageSource: image.ImageSource = image.createImageSource(exifRawFile.buffer as ArrayBuffer, exifOps);
  let exifCommodityPixelMap: image.PixelMap = await exifImageSource.createPixelMap();
  let exifPictureObj: image.Picture = image.createPicture(exifCommodityPixelMap);
  if (exifPictureObj != null) {
    console.info('Create picture succeeded');
  } else {
    console.error('Create picture failed');
  }

  if (auxPictureObj != null) {
    let metadataType: image.MetadataType = image.MetadataType.EXIF_METADATA;
    let exifMetaData: image.Metadata = await exifPictureObj.getMetadata(metadataType);
    auxPictureObj.setMetadata(metadataType, exifMetaData).then(() => {
      console.info('Set metadata success');
    }).catch((error: BusinessError) => {
      console.error(`Set metadata failed.error.code: ${error.code}, error.message: ${error.message}`);
    });
  } else {
    console.error('AuxPictureObjMetaData is null');
  }
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function SetPictureObjMetadata(exifContext: Context) {
  const exifResourceMgr = exifContext.resourceManager;
  const exifRawFile = await exifResourceMgr.getRawFileContent("exif.jpg"); // An image containing Exif metadata is required.
  let exifOps: image.SourceOptions = {
    sourceDensity: 98,
  }
  let exifImageSource: image.ImageSource = image.createImageSource(exifRawFile.buffer as ArrayBuffer, exifOps);
  let exifCommodityPixelMap: image.PixelMap = await exifImageSource.createPixelMap();
  let exifPictureObj: image.Picture = image.createPicture(exifCommodityPixelMap);
  if (exifPictureObj != null) {
    console.info('Create picture succeeded');
  } else {
    console.error('Create picture failed');
  }

  if (exifPictureObj != null) {
    let metadataType: image.MetadataType = image.MetadataType.EXIF_METADATA;
    let exifMetaData: image.Metadata = await exifPictureObj.getMetadata(metadataType);
    exifPictureObj.setMetadata(metadataType, exifMetaData).then(() => {
      console.info('Set metadata success');
    }).catch((error: BusinessError) => {
      console.error('Failed to set metadata. error.code: ' +JSON.stringify(error.code) + ' ,error.message:' + JSON.stringify(error.message));
    });
  } else {
    console.error('exifPictureOb is null');
  }
}
```

For details about how to create a PixelMap with DMA_ALLOC memory, see [Default Memory Allocation Mode](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/image-allocator-type#default-memory-allocation-method).

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import {image} from '@kit.ImageKit';

function SetMetadata(pixelMap: image.PixelMap) { // The input parameter pixelMap must be of the DMA_ALLOC memory type. For details about how to create a PixelMap with DMA_ALLOC memory, see the preceding link.
  let staticMetadata: image.HdrStaticMetadata = {
    displayPrimariesX: [1.1, 1.1, 1.1],
    displayPrimariesY: [1.2, 1.2, 1.2],
    whitePointX: 1.1,
    whitePointY: 1.2,
    maxLuminance: 2.1,
    minLuminance: 1.0,
    maxContentLightLevel: 2.1,
    maxFrameAverageLightLevel: 2.1,
  };
  pixelMap.setMetadata(image.HdrMetadataKey.HDR_STATIC_METADATA, staticMetadata).then(() => {
    console.info('Succeeded in setting pixelMap metadata.');
  }).catch((error: BusinessError) => {
    console.error("Failed to set the metadata.code ", error);
  })
}
```

## writePixelsFromBuffer

```TypeScript
writePixelsFromBuffer(data: ArrayBuffer): Promise<void>
```

Reads pixels from an ArrayBuffer and writes the data to this AuxiliaryPicture object. This API uses a promise to return the result.

**Since:** 23

<!--Device-AuxiliaryPicture-writePixelsFromBuffer(data: ArrayBuffer): Promise<void>--><!--Device-AuxiliaryPicture-writePixelsFromBuffer(data: ArrayBuffer): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | ArrayBuffer | Yes | Pixels of the auxiliary picture. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error.Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |

**Examples**

```TypeScript
async function WritePixelsFromBuffer(context: Context) {
  const resourceMgr = context.resourceManager;
  const rawFile = await resourceMgr.getRawFileContent("hdr.jpg"); // An HDR-compatible image is required.
  let ops: image.SourceOptions = {
    sourceDensity: 98,
  }
  let imageSource: image.ImageSource = image.createImageSource(rawFile.buffer as ArrayBuffer, ops);
  let commodityPixelMap: image.PixelMap = await imageSource.createPixelMap();
  let pictureObj: image.Picture = image.createPicture(commodityPixelMap);
  let auxPictureObj: image.AuxiliaryPicture | null = pictureObj.getAuxiliaryPicture(image.AuxiliaryPictureType.GAINMAP);
  if(auxPictureObj != null) {
    let auxBuffer: ArrayBuffer = await auxPictureObj.readPixelsToBuffer();
    await auxPictureObj.writePixelsFromBuffer(auxBuffer);
    console.info('Write pixels from buffer success.');
  } else {
    console.error('AuxPictureObj is null.');
  }
}
```

