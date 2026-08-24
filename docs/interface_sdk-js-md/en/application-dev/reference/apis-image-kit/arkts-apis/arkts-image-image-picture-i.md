# Picture

An image that contains special information can be decoded into a picture object, which generally contains the main picture, auxiliary picture, and metadata. The main picture contains most information about the image and is mainly used to render the image. The auxiliary picture is used to store data related to but different from the main picture, revealing more comprehensive details. The metadata is generally used to store information about the image file. The picture object class is used to read or write picture objects. Before calling any API in Picture, you must use [image.createPicture](arkts-image-image-createpicture-f.md) to create a Picture object.Images occupy a large amount of memory. When you finish using a Picture instance, call [release](#release) to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**Since:** 23

<!--Device-image-interface Picture--><!--Device-image-interface Picture-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## Modules to Import

```TypeScript
import { image } from '@kit.ImageKit';
```

## getAuxiliaryPicture

```TypeScript
getAuxiliaryPicture(type: AuxiliaryPictureType): AuxiliaryPicture | null
```

Obtains an auxiliary picture by type.

**Since:** 23

<!--Device-Picture-getAuxiliaryPicture(type: AuxiliaryPictureType): AuxiliaryPicture | null--><!--Device-Picture-getAuxiliaryPicture(type: AuxiliaryPictureType): AuxiliaryPicture | null-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | [AuxiliaryPictureType](arkts-image-image-auxiliarypicturetype-e.md) | Yes | Type of the auxiliary picture. |

**Return value:**

| Type | Description |
| --- | --- |
| [AuxiliaryPicture](arkts-image-image-auxiliarypicture-i.md) \| null | AuxiliaryPicture object. If there is no AuxiliaryPicture object, null is returned. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |

**Examples**

```TypeScript
async function GetAuxiliaryPicture(pictureObj : image.Picture) {
  if (pictureObj != null) {
    let type: image.AuxiliaryPictureType = image.AuxiliaryPictureType.GAINMAP;
    let auxPictureObj: image.AuxiliaryPicture | null = pictureObj.getAuxiliaryPicture(type);
  }
}
```

## getGainmapPixelmap

```TypeScript
getGainmapPixelmap(): PixelMap | null
```

Obtains the PixelMap object of the gain map.

**Since:** 23

<!--Device-Picture-getGainmapPixelmap(): PixelMap | null--><!--Device-Picture-getGainmapPixelmap(): PixelMap | null-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Return value:**

| Type | Description |
| --- | --- |
| PixelMap \| null | PixelMap object obtained. If there is no PixelMap object, null is returned. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function GetGainmapPixelmap(pictureObj : image.Picture) {
  let funcName = "getGainmapPixelmap";
  if (pictureObj != null) { // A gain map is contained.
    let gainPixelmap: image.PixelMap | null = pictureObj.getGainmapPixelmap();
    if (gainPixelmap != null) {
      gainPixelmap.getImageInfo().then((imageInfo: image.ImageInfo) => {
        if (imageInfo != null) {
          console.info(`GetGainmapPixelmap information height:${imageInfo.size.height} width:${imageInfo.size.width}`);
        } else {
          console.error('GainPixelmap is null');
        }
      }).catch((error: BusinessError) => {
        console.error(funcName, `Failed error.code: ${error.code} ,error.message: ${error.message}`);
      });
    } else {
      console.info('GainPixelmap is null');
    }
  } else {
    console.error('PictureObj is null');
  }
}
```

## getHdrComposedPixelmap

```TypeScript
getHdrComposedPixelmap(): Promise<PixelMap>
```

Generates a High Dynamic Range (HDR) image and obtains its PixelMap object. This API uses a promise to return the result.

**Since:** 13

<!--Device-Picture-getHdrComposedPixelmap(): Promise<PixelMap>--><!--Device-Picture-getHdrComposedPixelmap(): Promise<PixelMap>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;PixelMap&gt; | Promise used to return the PixelMap object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7600901](../errorcode-image.md#7600901-unknown-error) | Inner unknown error. Please check the logs for detailed information. |
| [7600201](../errorcode-image.md#7600201-unsupported-operation) | Unsupported operation. e.g.,1. The picture does not has a gainmap. 2. MainPixelMap's allocator type is not DMA. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function GetHdrComposedPixelmap(pictureObj : image.Picture) {
  let funcName = "getHdrComposedPixelmap";
  if (pictureObj != null) { // An HDR image is contained.
    let hdrComposedPixelmap: image.PixelMap = await pictureObj.getHdrComposedPixelmap();
    if (hdrComposedPixelmap != null) {
      hdrComposedPixelmap.getImageInfo().then((imageInfo: image.ImageInfo) => {
        if (imageInfo != null) {
          console.info(`GetHdrComposedPixelmap information height:${imageInfo.size.height} width:${imageInfo.size.width}`);
        }
      }).catch((error: BusinessError) => {
        console.error(funcName, `Failed error.code: ${error.code} ,error.message: ${error.message}`);
      });
    }
  } else {
    console.error('PictureObj is null');
  }
}
```

## getHdrComposedPixelmap

```TypeScript
getHdrComposedPixelmap(): Promise<PixelMap | undefined>
```

Obtains the hdr pixel map. This method uses a promise to return the PixelMap object.

**Since:** 23

<!--Device-Picture-getHdrComposedPixelmap(): Promise<PixelMap | undefined>--><!--Device-Picture-getHdrComposedPixelmap(): Promise<PixelMap | undefined>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;PixelMap \| undefined&gt; | A Promise instance used to return the PixelMap object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7600901](../errorcode-image.md#7600901-unknown-error) | Unknown error. |
| [7600201](../errorcode-image.md#7600201-unsupported-operation) | Unsupported operation. |

**Examples**

See [getHdrComposedPixelmap](#gethdrcomposedpixelmap)

## getHdrComposedPixelmapWithOptions

```TypeScript
getHdrComposedPixelmapWithOptions(options?: HdrComposeOptions): Promise<PixelMap | undefined>
```

Composites an HDR image and returns PixelMap of the image. Composition options (such as PixelMapFormat) can be passed. This API uses a promise to return the result.The Picture object that calls this API must contain the main picture, gain map, and metadata.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-Picture-getHdrComposedPixelmapWithOptions(options?: HdrComposeOptions): Promise<PixelMap | undefined>--><!--Device-Picture-getHdrComposedPixelmapWithOptions(options?: HdrComposeOptions): Promise<PixelMap | undefined>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [HdrComposeOptions](arkts-image-image-hdrcomposeoptions-i.md) | No | Options for HDR composition. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;PixelMap \| undefined&gt; | Promise, which returns the PixelMap object or **undefined**. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7600201](../errorcode-image.md#7600201-unsupported-operation) | Unsupported operation. |

**Examples**

```TypeScript
import { image } from '@kit.ImageKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function GetHdrComposedPixelmapWithOptions(picture : image.Picture) {
  if (picture == null) {
    console.error('picture is null');
    return;
  }

  let opt: image.HdrComposeOptions = {
    desiredPixelFormat: image.PixelMapFormat.RGBA_1010102
  };
  let hdrComposedPixelmap: image.PixelMap | undefined = await picture.getHdrComposedPixelmapWithOptions(opt);
  if (hdrComposedPixelmap == null || hdrComposedPixelmap == undefined) {
    console.error(`GetHdrComposedPixelmapWithOptions failed`);
    return;
  }

  hdrComposedPixelmap.getImageInfo().then((imageInfo: image.ImageInfo) => {
    if (imageInfo !== null) {
      console.info(`GetHdrComposedPixelmapWithOptions information height:${imageInfo.size.height} width:${imageInfo.size.width}`);
    }
  }).catch((error: BusinessError) => {
    console.error(`GetHdrComposedPixelmapWithOptions information failed error.code: ${error.code} ,error.message: ${error.message}`);
  });
}
```

## getMainPixelmap

```TypeScript
getMainPixelmap(): PixelMap
```

Obtains the PixelMap object of the main picture. This API returns the result synchronously.

**Since:** 13

<!--Device-Picture-getMainPixelmap(): PixelMap--><!--Device-Picture-getMainPixelmap(): PixelMap-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Return value:**

| Type | Description |
| --- | --- |
| PixelMap | PixelMap object. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function GetMainPixelmap(pictureObj : image.Picture) {
  let funcName = "getMainPixelmap";
  if (pictureObj != null) {
    let mainPixelmap: image.PixelMap = pictureObj.getMainPixelmap();
    if (mainPixelmap != null) {
      mainPixelmap.getImageInfo().then((imageInfo: image.ImageInfo) => {
        if (imageInfo != null) {
          console.info('GetMainPixelmap information height:' + imageInfo.size.height + ' width:' + imageInfo.size.width);
        }
      }).catch((error: BusinessError) => {
        console.error(funcName, `Failed error.code: ${error.code} ,error.message: ${error.message}`);
      });
    }
  } else {
    console.error('PictureObj is null');
  }
}
```

## getMainPixelmap

```TypeScript
getMainPixelmap(): PixelMap | undefined
```

Obtains the pixel map of the main image.

**Since:** 23

<!--Device-Picture-getMainPixelmap(): PixelMap | undefined--><!--Device-Picture-getMainPixelmap(): PixelMap | undefined-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Return value:**

| Type | Description |
| --- | --- |
| PixelMap \| undefined | Returns the pixel map. |

**Examples**

See [getMainPixelmap](#getmainpixelmap)

## getMetadata

```TypeScript
getMetadata(metadataType: MetadataType): Promise<Metadata>
```

Obtains the metadata of this Picture object. This API uses a promise to return the result.

**Since:** 13

<!--Device-Picture-getMetadata(metadataType: MetadataType): Promise<Metadata>--><!--Device-Picture-getMetadata(metadataType: MetadataType): Promise<Metadata>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| metadataType | [MetadataType](arkts-image-image-metadatatype-e.md) | Yes | Metadata type. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Metadata&gt; | Promise used to return the metadata. |

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

Obtains the metadata of main picture.

**Since:** 23

<!--Device-Picture-getMetadata(metadataType: MetadataType): Promise<Metadata | undefined>--><!--Device-Picture-getMetadata(metadataType: MetadataType): Promise<Metadata | undefined>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| metadataType | [MetadataType](arkts-image-image-metadatatype-e.md) | Yes | The type of metadata. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Metadata \| undefined&gt; | Return the metadata of main picture. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7600202](../errorcode-image.md#7600202-unsupported-metadata-readwrite-operation) | Unsupported metadata. Possible causes: Unsupported metadata type. |

**Examples**

See [getMetadata](#getmetadata)

## hdrComposeToMainPixelmap

```TypeScript
hdrComposeToMainPixelmap(): Promise<void>
```

Invokes the VPE algorithm to compose the main pixelmap and gainmap. The composed result will replace the main pixelmap of the current picture object.The Picture object that calls this API must contain the main pixelmap, gain map.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-Picture-hdrComposeToMainPixelmap(): Promise<void>--><!--Device-Picture-hdrComposeToMainPixelmap(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7600201](../errorcode-image.md#7600201-unsupported-operation) | Unsupported operation. e.g.,1. The picture does not have a gainmap. 2. pixelMap's allocator type is not DMA. |

## marshalling

```TypeScript
marshalling(sequence: rpc.MessageSequence): void
```

Marshals this Picture object and writes it to a MessageSequence object.

**Since:** 23

<!--Device-Picture-marshalling(sequence: rpc.MessageSequence): void--><!--Device-Picture-marshalling(sequence: rpc.MessageSequence): void-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sequence | rpc.MessageSequence | Yes | MessageSequence object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| [62980097](../errorcode-image.md#62980097-pixelmap-serialization-failed) | IPC error. Possible cause: 1.IPC communication failed. 2. Image upload exception. 3. Decode process exception. 4. Insufficient memory. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { rpc } from '@kit.IPCKit';

class MySequence implements rpc.Parcelable {
  picture: image.Picture | null = null;
  constructor(conPicture: image.Picture) {
    this.picture = conPicture;
  }
  marshalling(messageSequence: rpc.MessageSequence) {
    if(this.picture != null) {
      this.picture.marshalling(messageSequence);
      console.info('Marshalling success !');
      return true;
    } else {
      console.error('Marshalling failed !');
      return false;
    }
  }
  unmarshalling(messageSequence : rpc.MessageSequence) {
    this.picture = image.createPictureFromParcel(messageSequence);
    this.picture.getMainPixelmap().getImageInfo().then((imageInfo : image.ImageInfo) => {
      console.info(`Unmarshalling to get mainPixelmap information height:${imageInfo.size.height} width:${imageInfo.size.width}`);
    }).catch((error: BusinessError) => {
      console.error(`Unmarshalling failed error.code: ${error.code} ,error.message: ${error.message}`);
    });
    return true;
  }
}

async function Marshalling_UnMarshalling(pictureObj : image.Picture) {
  if (pictureObj != null) {
    let parcelable: MySequence = new MySequence(pictureObj);
    let data: rpc.MessageSequence = rpc.MessageSequence.create();
    // Implement serialization.
    data.writeParcelable(parcelable);
    let ret: MySequence = new MySequence(pictureObj);
    // Implement deserialization.
    data.readParcelable(ret);
  } else {
    console.error('PictureObj is null');
  }
}
```

```TypeScript
import { rpc } from '@kit.IPCKit';

class MySequence implements rpc.Parcelable {
  pixel_map: image.PixelMap;
  constructor(conPixelMap : image.PixelMap) {
    this.pixel_map = conPixelMap;
  }
  marshalling(messageSequence : rpc.MessageSequence) {
    this.pixel_map.marshalling(messageSequence);
    console.info('marshalling');
    return true;
  }
  unmarshalling(messageSequence : rpc.MessageSequence) {
    image.createPixelMap(new ArrayBuffer(96), {size: { height:4, width: 6}}).then((pixelParcel: image.PixelMap) => {
      pixelParcel.unmarshalling(messageSequence).then(async (pixelMap: image.PixelMap) => {
        this.pixel_map = pixelMap;
        pixelMap.getImageInfo().then((imageInfo: image.ImageInfo) => {
          console.info(`unmarshalling information h: ${imageInfo.size.height} w: ${imageInfo.size.width}`);
        })
      })
    });
    return true;
  }
}
async function Marshalling() {
  const color: ArrayBuffer = new ArrayBuffer(96);
  let bufferArr: Uint8Array = new Uint8Array(color);
  for (let i = 0; i < bufferArr.length; i++) {
    bufferArr[i] = 0x80;
  }
  let opts: image.InitializationOptions = {
    editable: true,
    pixelFormat: image.PixelMapFormat.BGRA_8888,
    size: { height: 4, width: 6 },
    alphaType: image.AlphaType.UNPREMUL
  }
  let pixelMap: image.PixelMap | undefined = undefined;
  await image.createPixelMap(color, opts).then((srcPixelMap: image.PixelMap) => {
    pixelMap = srcPixelMap;
  })
  if (pixelMap != undefined) {
    // Implement serialization.
    let parcelable: MySequence = new MySequence(pixelMap);
    let data: rpc.MessageSequence = rpc.MessageSequence.create();
    data.writeParcelable(parcelable);

    // Implement deserialization to obtain data through the RPC.
    let ret: MySequence = new MySequence(pixelMap);
    data.readParcelable(ret);
  }
}
```

## release

```TypeScript
release(): void
```

Releases this Picture object.Images occupy a large amount of memory. When you finish using a Picture instance, call this API to free the memory promptly.Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**Since:** 23

<!--Device-Picture-release(): void--><!--Device-Picture-release(): void-End-->

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

## setAuxiliaryPicture

```TypeScript
setAuxiliaryPicture(type: AuxiliaryPictureType, auxiliaryPicture: AuxiliaryPicture): void
```

Sets an auxiliary picture.

**Since:** 23

<!--Device-Picture-setAuxiliaryPicture(type: AuxiliaryPictureType, auxiliaryPicture: AuxiliaryPicture): void--><!--Device-Picture-setAuxiliaryPicture(type: AuxiliaryPictureType, auxiliaryPicture: AuxiliaryPicture): void-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | [AuxiliaryPictureType](arkts-image-image-auxiliarypicturetype-e.md) | Yes | Type of the auxiliary picture. |
| auxiliaryPicture | [AuxiliaryPicture](arkts-image-image-auxiliarypicture-i.md) | Yes | AuxiliaryPicture object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |

**Examples**

```TypeScript
async function SetAuxiliaryPicture(context: Context) {
  const resourceMgr = context.resourceManager;
  const rawFile = await resourceMgr.getRawFileContent("hdr.jpg"); // An HDR-compatible image is required.
  let ops: image.SourceOptions = {
    sourceDensity: 98,
  }
  let imageSource: image.ImageSource = image.createImageSource(rawFile.buffer as ArrayBuffer, ops);
  let pixelMap: image.PixelMap = await imageSource.createPixelMap();
  let pictureObj: image.Picture = image.createPicture(pixelMap);
  if (pictureObj != null) {
    console.info('Create picture succeeded');
  } else {
    console.error('Create picture failed');
  }

  if (pictureObj != null) {
    let type: image.AuxiliaryPictureType = image.AuxiliaryPictureType.GAINMAP;
    let auxPictureObj: image.AuxiliaryPicture | null = pictureObj.getAuxiliaryPicture(type);
    if (auxPictureObj != null) {
      pictureObj.setAuxiliaryPicture(type, auxPictureObj);
    }
  }
}
```

## setMainPixelmap

```TypeScript
setMainPixelmap(pixelmap: PixelMap): void
```

Sets the PixelMap object of the picture.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-Picture-setMainPixelmap(pixelmap: PixelMap): void--><!--Device-Picture-setMainPixelmap(pixelmap: PixelMap): void-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pixelmap | PixelMap | Yes | PixelMap object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7700204](../errorcode-image.md#7700204-invalid-parameter) | Parameter error. The pixelmap object is null or has been released. |

## setMetadata

```TypeScript
setMetadata(metadataType: MetadataType, metadata: Metadata): Promise<void>
```

Sets the metadata for this Picture object. This API uses a promise to return the result.

**Since:** 23

<!--Device-Picture-setMetadata(metadataType: MetadataType, metadata: Metadata): Promise<void>--><!--Device-Picture-setMetadata(metadataType: MetadataType, metadata: Metadata): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| metadataType | [MetadataType](arkts-image-image-metadatatype-e.md) | Yes | Metadata type. |
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

