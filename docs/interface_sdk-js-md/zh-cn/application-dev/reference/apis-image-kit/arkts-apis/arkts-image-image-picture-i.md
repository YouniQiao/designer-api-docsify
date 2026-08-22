# Picture

Picture类，一些包含特殊信息的图片可以解码为Picture（也可以称为多图对象）。多图对象一般包含主图、辅助图和元数据。其中主图包含图像的大部分信息，主要用于显示图像内容；辅助图用于存储与主图相关但不同的数据，展示图像更丰富 的信息；元数据一般用来存储关于图像文件的信息。多图对象类用于读取或写入多图对象。在调用Picture的方法前，需要先通过[image.createPicture](arkts-image-image-createpicture-f.md)创建一个 Picture实例。

由于图片占用内存较大，所以当Picture实例使用完成后，应主动调用[release](#release)方法及时释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

> **说明：**
> 
> - 本Interface首批接口从API version 13开始支持。

**起始版本：** 23

<!--Device-image-interface Picture--><!--Device-image-interface Picture-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

## 导入模块

```TypeScript
import { image } from '@kit.ImageKit';
```

## getAuxiliaryPicture

```TypeScript
getAuxiliaryPicture(type: AuxiliaryPictureType): AuxiliaryPicture | null
```

根据类型获取辅助图。

**起始版本：** 23

<!--Device-Picture-getAuxiliaryPicture(type: AuxiliaryPictureType): AuxiliaryPicture | null--><!--Device-Picture-getAuxiliaryPicture(type: AuxiliaryPictureType): AuxiliaryPicture | null-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [AuxiliaryPictureType](arkts-image-image-auxiliarypicturetype-e.md) | 是 | 辅助图类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AuxiliaryPicture](arkts-image-image-auxiliarypicture-i.md) \| null | 返回AuxiliaryPicture对象，如果没有则返回null。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |

**示例**

ArkTS-Dyn示例：

```TypeScript
async function GetAuxiliaryPicture(pictureObj : image.Picture) {
  if (pictureObj != null) {
    let type: image.AuxiliaryPictureType = image.AuxiliaryPictureType.GAINMAP;
    let auxPictureObj: image.AuxiliaryPicture | null = pictureObj.getAuxiliaryPicture(type);
  }
}
```

ArkTS-Sta示例：

```TypeScript
function GetAuxiliaryPictureFunc(picture: image.Picture): void {
  let type: image.AuxiliaryPictureType = image.AuxiliaryPictureType.GAINMAP;
  try {
    let auxPixelMap: image.AuxiliaryPicture | null = picture.getAuxiliaryPicture(type);
    if (auxPixelMap == null) {
      console.error(0x00000, 'GetAuxiliaryPictureFunc', 'getAuxiliaryPicture is null!');
    } else {
      console.info(0x00000, 'GetAuxiliaryPictureFunc', 'getAuxiliaryPicture success!');
    }
  } catch (err) {
    console.error(0x00000, 'GetAuxiliaryPictureFunc', 'GetAuxiliaryPictureFunc failed: ' + err);
  }
}
```

## getGainmapPixelmap

```TypeScript
getGainmapPixelmap(): PixelMap | null
```

获取增益图的pixelmap。

**起始版本：** 23

<!--Device-Picture-getGainmapPixelmap(): PixelMap | null--><!--Device-Picture-getGainmapPixelmap(): PixelMap | null-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| PixelMap \| null | 返回Pixelmap对象，如果没有则返回null。 |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function GetGainmapPixelmap(pictureObj : image.Picture) {
  let funcName = "getGainmapPixelmap";
  if (pictureObj != null) { // 图片包含增益图。
    let gainPixelmap: image.PixelMap | null = pictureObj.getGainmapPixelmap();
    if (gainPixelmap != null) {
      gainPixelmap.getImageInfo().then((imageInfo: image.ImageInfo) => {
        if (imageInfo != null) {
          console.info(`Succeeded in getting gainmap PixelMap information. Height: ${imageInfo.size.height}, width: ${imageInfo.size.width}.`);
        } else {
          console.error('Gainmap PixelMap is null.');
        }
      }).catch((error: BusinessError) => {
        console.error(funcName, `Failed to get gainmap PixelMap information. Code: ${error.code}, message: ${error.message}.`);
      });
    } else {
      console.info('Gainmap PixelMap is null.');
    }
  } else {
    console.error('Picture object is null.');
  }
}
```

ArkTS-Sta示例：

```TypeScript
function GetGainmapPixelmapFunc(picture: image.Picture): void {
  try {
    let pixelMap: image.PixelMap | null = picture.getGainmapPixelmap();
    if (pixelMap == null) {
      console.error(0x00000, 'GetGainmapPixelmapFunc', 'getGainmapPixelmap is null!');
    } else {
      console.info(0x00000, 'GetGainmapPixelmapFunc', 'getGainmapPixelmap success!');
    }
  } catch (err) {
    console.error(0x00000, 'GetGainmapPixelmapFunc', 'GetGainmapPixelmapFunc failed: ' + err);
  }
}
```

## getHdrComposedPixelmap

```TypeScript
getHdrComposedPixelmap(): Promise<PixelMap>
```

合成HDR图并获取HDR图的pixelmap。使用Promise异步回调。

**起始版本：** 13

<!--Device-Picture-getHdrComposedPixelmap(): Promise<PixelMap>--><!--Device-Picture-getHdrComposedPixelmap(): Promise<PixelMap>-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;PixelMap&gt; | Promise对象，返回PixelMap。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [7600901](../errorcode-image.md#7600901-未知错误) | Inner unknown error. Please check the logs for detailed information. |
| [7600201](../errorcode-image.md#7600201-不支持的操作) | Unsupported operation. e.g.,1. The picture does not has a gainmap. 2. MainPixelMap's allocator type is not DMA. |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function GetHdrComposedPixelmap(pictureObj : image.Picture) {
  let funcName = "getHdrComposedPixelmap";
  if (pictureObj != null) { // 图片包含Hdr图。
    let hdrComposedPixelmap: image.PixelMap = await pictureObj.getHdrComposedPixelmap();
    if (hdrComposedPixelmap != null) {
      hdrComposedPixelmap.getImageInfo().then((imageInfo: image.ImageInfo) => {
        if (imageInfo != null) {
          console.info(`Succeeded in getting HDR composed PixelMap information. Height: ${imageInfo.size.height}, width: ${imageInfo.size.width}.`);
        }
      }).catch((error: BusinessError) => {
        console.error(funcName, `Failed to get HDR composed PixelMap information. Code: ${error.code}, message: ${error.message}.`);
      });
    }
  } else {
    console.error('Picture object is null.');
  }
}
```

ArkTS-Sta示例：

```TypeScript
function GetHdrComposedPixelmapFunc(picture: image.Picture): void {
  try {
    let pixelMap = picture.getHdrComposedPixelmap();
    console.info(0x00000, 'GetHdrComposedPixelmapFunc', 'getHdrComposedPixelmap success!');
  } catch (err) {
    console.error(0x00000, 'GetHdrComposedPixelmapFunc', 'GetHdrComposedPixelmapFunc failed: ' + err);
  }
}
```

## getHdrComposedPixelmap

```TypeScript
getHdrComposedPixelmap(): Promise<PixelMap | undefined>
```

Obtains the hdr pixel map. This method uses a promise to return the PixelMap object.

**起始版本：** 23

<!--Device-Picture-getHdrComposedPixelmap(): Promise<PixelMap | undefined>--><!--Device-Picture-getHdrComposedPixelmap(): Promise<PixelMap | undefined>-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;PixelMap \| undefined&gt; | A Promise instance used to return the PixelMap object. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [7600901](../errorcode-image.md#7600901-未知错误) | Unknown error. |
| [7600201](../errorcode-image.md#7600201-不支持的操作) | Unsupported operation. |

**示例**

参见 [getHdrComposedPixelmap](#gethdrcomposedpixelmap)

## getHdrComposedPixelmapWithOptions

```TypeScript
getHdrComposedPixelmapWithOptions(options?: HdrComposeOptions): Promise<PixelMap | undefined>
```

合成HDR图像并返回HDR图像的PixelMap，支持传入合成参数（如PixelMapFormat等）。使用Promise异步回调。

调用该接口的Picture对象中必须包含主图、增益图和元数据。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Picture-getHdrComposedPixelmapWithOptions(options?: HdrComposeOptions): Promise<PixelMap | undefined>--><!--Device-Picture-getHdrComposedPixelmapWithOptions(options?: HdrComposeOptions): Promise<PixelMap | undefined>-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [HdrComposeOptions](arkts-image-image-hdrcomposeoptions-i.md) | 否 | 合成HDR的选项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;PixelMap \| undefined&gt; | Promise对象，返回PixelMap或undefined。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [7600201](../errorcode-image.md#7600201-不支持的操作) | Unsupported operation. |

**示例**

ArkTS-Dyn示例：

```TypeScript
// EntryAbility.ets
import { BusinessError } from '@kit.BasicServicesKit';

async function GetHdrComposedPixelmapWithOptions(picture : image.Picture) {
  if (picture == null) {
    console.error('Picture is null.');
    return;
  }

  let opt: image.HdrComposeOptions = {
    desiredPixelFormat: image.PixelMapFormat.RGBA_1010102
  };
  let hdrComposedPixelmap: image.PixelMap | undefined = await picture.getHdrComposedPixelmapWithOptions(opt);
  if (hdrComposedPixelmap == null || hdrComposedPixelmap == undefined) {
    console.error(`Failed to get an HDR composed PixelMap with options.`);
    return;
  }

  hdrComposedPixelmap.getImageInfo().then((imageInfo: image.ImageInfo) => {
    if (imageInfo !== null) {
      console.info(`Succeeded in getting HDR composed PixelMap information with options. Height: ${imageInfo.size.height}, width: ${imageInfo.size.width}.`);
    }
  }).catch((error: BusinessError) => {
    console.error(`Failed to get HDR composed PixelMap information with options. Code: ${error.code}, message: ${error.message}.`);
  });
}
```

ArkTS-Sta示例：

```TypeScript
// EntryAbility.ets
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
  try {
    let imageInfo = await hdrComposedPixelmap.getImageInfo();
    if (imageInfo && imageInfo.size) {
      console.info(`GetHdrComposedPixelmapWithOptions information height:${imageInfo.size.height} width:${imageInfo.size.width}`);
    }
  } catch (err) {
    console.error(`GetHdrComposedPixelmapWithOptions information failed error.code: ${err.code} ,error.message: ${err.message}`);
  }
}
```

## getMainPixelmap

```TypeScript
getMainPixelmap(): PixelMap
```

获取主图的pixelmap。

**起始版本：** 13

<!--Device-Picture-getMainPixelmap(): PixelMap--><!--Device-Picture-getMainPixelmap(): PixelMap-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| PixelMap | 同步返回PixelMap对象。 |

## getMainPixelmap

```TypeScript
getMainPixelmap(): PixelMap | undefined
```

Obtains the pixel map of the main image.

**起始版本：** 23

<!--Device-Picture-getMainPixelmap(): PixelMap | undefined--><!--Device-Picture-getMainPixelmap(): PixelMap | undefined-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| PixelMap \| undefined | Returns the pixel map. |

## getMetadata

```TypeScript
getMetadata(metadataType: MetadataType): Promise<Metadata>
```

获取主图的元数据。使用Promise异步回调。

**起始版本：** 13

<!--Device-Picture-getMetadata(metadataType: MetadataType): Promise<Metadata>--><!--Device-Picture-getMetadata(metadataType: MetadataType): Promise<Metadata>-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| metadataType | [MetadataType](arkts-image-image-metadatatype-e.md) | 是 | 元数据类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;Metadata&gt; | Promise对象。返回元数据。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| [7600202](../errorcode-image.md#7600202-不支持的元数据读写) | Unsupported metadata. Possible causes: 1. Unsupported metadata type. 2. The metadata type does not match the auxiliary picture type. |

**示例**

ArkTS-Dyn示例：

```TypeScript
async function GetAuxPictureObjMetadata(auxPictureObj: image.AuxiliaryPicture) {
  if (auxPictureObj != null) {
    let metadataType: image.MetadataType = image.MetadataType.EXIF_METADATA;
    let auxPictureObjMetaData: image.Metadata | null = await auxPictureObj.getMetadata(metadataType);
    if (auxPictureObjMetaData != null) {
      console.info('Succeeded in getting AuxPictureObj Metadata.' );
    } else {
      console.error('Failed to get AuxPictureObj Metadata.');
    }
  } else {
    console.error('Get AuxPictureObj is null.');
  }
}
```

ArkTS-Sta示例：

```TypeScript
function GetMetadataFunc(auxPicture: image.AuxiliaryPicture): void {
  try {
    let metadataType: image.MetadataType = image.MetadataType.EXIF_METADATA;
    let metadata = auxPicture.getMetadata(metadataType);
    if (metadata != null) {
      console.info(0x00000, 'GetMetadataFunc', 'getMetadata success!');
    }
  } catch (err) {
    console.error(0x00000, 'GetMetadataFunc', 'GetMetadataFunc failed: ' + err);
  }
}
```

ArkTS-Dyn示例：

```TypeScript
async function GetMetadata(img : image.Image) {
  try {
    let staticMetadata = img.getMetadata(image.HdrMetadataKey.HDR_STATIC_METADATA);
    console.info(`getMetadata:${staticMetadata}`);
  } catch (err) {
    console.error('Failed to getMetadata.' + err);
  }
}
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function GetMetadata(img : image.Image) {
  try {
    let staticMetadata = img.getMetadata(image.HdrMetadataKey.HDR_STATIC_METADATA);
    if (staticMetadata) {
      console.info(`GetMetadata:${staticMetadata}`);
    }
  } catch (err) {
    console.error('GetMetadata failed' + err);
  }
}
```

ArkTS-Dyn示例：

```TypeScript
async function GetPictureObjMetadataProperties(pictureObj : image.Picture) {
  if (pictureObj != null) {
    let metadataType: image.MetadataType = image.MetadataType.EXIF_METADATA;
    let pictureObjMetaData: image.Metadata = await pictureObj.getMetadata(metadataType);
    if (pictureObjMetaData != null) {
      console.info('Succeeded in getting picture metadata.');
    } else {
      console.error('Failed to get picture metadata.');
    }
  } else {
    console.error(" pictureObj is null");
  }
}
```

ArkTS-Sta示例：

```TypeScript
function GetMetadataFunc(picture: image.Picture): void {
  try {
    let metadataType: image.MetadataType = image.MetadataType.EXIF_METADATA;
    let metaData = await picture.getMetadata(metadataType);
    console.info(0x00000, 'SetMetadataFunc', 'getMetadata success!');
  } catch (err) {
    console.error(0x00000, 'SetMetadataFunc', 'SetMetadataFunc failed: ' + err);
  }
}
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function getMetadata(context: Context) {
  // 此处'app.media.startIcon'需要替换为本地HDR图片。
  let img = context.resourceManager.getMediaContentSync($r('app.media.startIcon').id);
  let imageSource = image.createImageSource(img.buffer.slice(0));
  let decodingOptions: image.DecodingOptions = {
    desiredDynamicRange: image.DecodingDynamicRange.AUTO
  };
  let pixelMap = imageSource.createPixelMapSync(decodingOptions);
  if (pixelMap != undefined) {
    console.info('Succeeded in creating the PixelMap object.');
    try {
      let staticMetadata = pixelMap.getMetadata(image.HdrMetadataKey.HDR_STATIC_METADATA);
      console.info('Succeeded in getting the metadata.');
    } catch (e) {
      const err = e as BusinessError;
      console.error(`Failed to get the metadata. Code: ${err.code}, message: ${err.message}`);
    }
  } else {
    console.error('Failed to create the PixelMap.');
  }
}
```

ArkTS-Sta示例：

```TypeScript
function getMetadata(context: Context) {
  // 此处'app.media.startIcon'需要替换为本地HDR图片。
  let img = context.resourceManager.getMediaContentSync($r('app.media.startIcon').id);
  let imageSource = image.createImageSource(img.buffer.slice(0));
  let decodingOptions: image.DecodingOptions = {
    desiredDynamicRange: image.DecodingDynamicRange.AUTO
  };
  let pixelMap = imageSource.createPixelMapSync(decodingOptions);
  if (pixelMap != undefined) {
    console.info('Succeeded in creating the PixelMap object.');
    try {
      let staticMetadata = pixelMap.getMetadata(image.HdrMetadataKey.HDR_STATIC_METADATA);
      console.info('Succeeded in getting the metadata.');
    } catch (err) {
      console.error(`Failed to get the metadata. Code: ${err.code}, message: ${err.message}`);
    }
  } else {
    console.error('Failed to create the PixelMap.');
  }
}
```

## getMetadata

```TypeScript
getMetadata(metadataType: MetadataType): Promise<Metadata | undefined>
```

Obtains the metadata of main picture.

**起始版本：** 23

<!--Device-Picture-getMetadata(metadataType: MetadataType): Promise<Metadata | undefined>--><!--Device-Picture-getMetadata(metadataType: MetadataType): Promise<Metadata | undefined>-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| metadataType | [MetadataType](arkts-image-image-metadatatype-e.md) | 是 | The type of metadata. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;Metadata \| undefined&gt; | Return the metadata of main picture. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [7600202](../errorcode-image.md#7600202-不支持的元数据读写) | Unsupported metadata. Possible causes: Unsupported metadata type. |

**示例**

参见 [getMetadata](#getmetadata)

## hdrComposeToMainPixelmap

```TypeScript
hdrComposeToMainPixelmap(): Promise<void>
```

将Picture对象的主图和增益图合成为HDR图，合成后原Picture的主图被替换为HDR图，原Picture的增益图被删除。使用Promise异步回调。

调用该接口的Picture对象中必须包含主图、增益图。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Picture-hdrComposeToMainPixelmap(): Promise<void>--><!--Device-Picture-hdrComposeToMainPixelmap(): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [7600201](../errorcode-image.md#7600201-不支持的操作) | Unsupported operation. e.g.,1. The picture does not have a gainmap. 2. pixelMap's allocator type is not DMA. |

**示例**

```TypeScript
// EntryAbility.ets
import { image } from '@kit.ImageKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function HdrComposeToMainPixelmap(picture : image.Picture) {
  if (picture == null) {
    console.error('picture is null');
    return;
  }
  try {
    await picture.hdrComposeToMainPixelmap();
  } catch(error) {
    console.error(`Failed to do HdrComposeToMainPixelmap. error.code: ${error.code} ,error.message: ${error.message}`);
  }
}
```

## marshalling

```TypeScript
marshalling(sequence: rpc.MessageSequence): void
```

将picture序列化后写入MessageSequence。

**起始版本：** 23

<!--Device-Picture-marshalling(sequence: rpc.MessageSequence): void--><!--Device-Picture-marshalling(sequence: rpc.MessageSequence): void-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sequence | rpc.MessageSequence | 是 | 新创建的MessageSequence。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| [62980097](../errorcode-image.md#62980097-pixelmap序列化传输失败) | IPC error. Possible cause: 1.IPC communication failed. 2. Image upload exception. 3. Decode process exception. 4. Insufficient memory. |

**示例**

ArkTS-Dyn示例：

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
      console.info('Succeeded in marshalling a picture.');
      return true;
    } else {
      console.error('Failed to marshall a picture.');
      return false;
    }
  }
  unmarshalling(messageSequence : rpc.MessageSequence) {
    this.picture = image.createPictureFromParcel(messageSequence);
    this.picture.getMainPixelmap().getImageInfo().then((imageInfo : image.ImageInfo) => {
      console.info(`Succeeded in unmarshalling a picture and getting main PixelMap information. Height: ${imageInfo.size.height}, width: ${imageInfo.size.width}.`);
    }).catch((error: BusinessError) => {
      console.error(`Failed to unmarshall a picture. Code: ${error.code}, message: ${error.message}.`);
    });
    return true;
  }
}

async function Marshalling_UnMarshalling(pictureObj : image.Picture) {
  if (pictureObj != null) {
    let parcelable: MySequence = new MySequence(pictureObj);
    let data: rpc.MessageSequence = rpc.MessageSequence.create();
    // 序列化。
    data.writeParcelable(parcelable);
    let ret: MySequence = new MySequence(pictureObj);
    // 反序列化。
    data.readParcelable(ret);
  } else {
    console.error('Picture object is null.');
  }
}
```

ArkTS-Sta示例：

```TypeScript
import { common } from '@kit.AbilityKit';
import { resourceManager } from '@kit.LocalizationKit';
import { rpc } from '@kit.IPCKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext。
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
if (context != undefined) {
  MarshallingUnMarshallingFunc(context);
}

class MySequence implements rpc.Parcelable {
  picture_: image.Picture;

  constructor(conPicture: image.Picture) {
    this.picture_ = conPicture;
  }

  marshalling(messageSequence: rpc.MessageSequence): boolean {
    this.picture_.marshalling(messageSequence);
    console.info(0x00000, 'MySequence', 'marshalling success!');
    return true;
  }

  unmarshalling(messageSequence: rpc.MessageSequence): boolean {
    let picture: image.Picture = image.createPictureFromParcel(messageSequence)
    this.picture_ = picture;
    console.info(0x00000, 'MySequence', 'unmarshalling success!');
    return true;
  }
}

function MarshallingUnMarshallingFunc(context: common.UIAbilityContext): void {
  const resourceMgr = context.resourceManager;
  const rawFile = await resourceMgr.getRawFileContent("test_image.jpg");
  let opts: image.SourceOptions = { sourceDensity: 98 };
  try {
    let imageSource: image.ImageSource = image.createImageSource(rawFile.buffer as ArrayBuffer, opts);
    let pixelMap: image.PixelMap = await imageSource.createPixelMap();
    let picture: image.Picture = image.createPicture(pixelMap);
    if (picture != null || picture != undefined) {
      let parcelable: MySequence = new MySequence(picture);
      let data: rpc.MessageSequence = rpc.MessageSequence.create();
      // 序列化。
      data.writeParcelable(parcelable);

      let ret: MySequence = new MySequence(picture);
      // 反序列化。
      data.readParcelable(ret);
    } else {
      console.error(0x00000, 'MarshallingUnMarshallingFunc', 'picture is null!');
    }
  } catch (err) {
    console.error(0x00000, 'MarshallingUnMarshallingFunc', 'MarshallingUnMarshallingFunc failed: ' + err);
  }
}
```

```TypeScript
// EntryAbility.ets
import { rpc } from '@kit.IPCKit';

class MySequence implements rpc.Parcelable {
  pixelMap: image.PixelMap;
  constructor(pixelMap: image.PixelMap) {
    this.pixelMap = pixelMap;
  }
  marshalling(messageSequence: rpc.MessageSequence) {
    this.pixelMap.marshalling(messageSequence);
    console.info('Marshalled the PixelMap.');
    return true;
  }
  unmarshalling(messageSequence: rpc.MessageSequence) {
    image.createPixelMap(new ArrayBuffer(96), {size: { height: 4, width: 6 }}).then((pixelParcel: image.PixelMap) => {
      pixelParcel.unmarshalling(messageSequence).then(async (pixelMap: image.PixelMap) => {
        this.pixelMap = pixelMap;
        pixelMap.getImageInfo().then((imageInfo: image.ImageInfo) => {
          console.info(`Unmarshalled information: height = ${imageInfo.size.height}, width = ${imageInfo.size.width}.`);
        });
      });
    });
    return true;
  }
}

async function marshal() {
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
  };
  let pixelMap: image.PixelMap | undefined = await image.createPixelMap(color, opts);
  if (pixelMap != undefined) {
    // 序列化。
    let parcelable: MySequence = new MySequence(pixelMap);
    let data: rpc.MessageSequence = rpc.MessageSequence.create();
    data.writeParcelable(parcelable);

    // 反序列化rpc获取到data。
    let seq: MySequence = new MySequence(pixelMap);
    data.readParcelable(seq);
  }
}
```

## release

```TypeScript
release(): void
```

释放picture对象。

由于图片占用内存较大，所以当Picture对象使用完成后，应主动调用该方法及时释放内存。

释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

**起始版本：** 23

<!--Device-Picture-release(): void--><!--Device-Picture-release(): void-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
import { common } from '@kit.AbilityKit';
// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext。
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
if (context != undefined) {
  let auxPicture: image.AuxiliaryPicture | null = GetAuxiliaryPicture(context)
  if (auxPicture != null) {
    auxPicture.release();
  } else {
    console.error(0x00000, 'GetAuxiliaryPicture', 'auxPicture is null!');
  }
}
```

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@ohos.base';

function ReleaseFunc(img: image.Image): void {
  try {
    img.release((err: BusinessError | null) => {
      if (err) {
        console.error(0x00000, 'ReleaseFunc', 'release failed: ' + err);
      } else {
        console.info(0x00000, 'ReleaseFunc', 'release success!');
      }
    })
  } catch (err) {
    console.error(0x00000, 'ReleaseFunc', 'ReleaseFunc failed: ' + err);
  }
}
```

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
function ReleaseFunc(img: image.Image): void {
  try {
    await img.release()
  } catch (err) {
    console.error(0x00000, 'ReleaseFunc', 'ReleaseFunc failed: ' + err);
  }
}
```

ArkTS-Dyn示例：

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
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function ReleaseFunc(creator: image.ImageCreator): void {
  try {
    creator.release((err: BusinessError | null) => {
      if (err) {
        console.error(0x00000, 'ReleaseFunc', 'release failed: ' + err);
      } else {
        console.info(0x00000, 'ReleaseFunc', 'release success!');
      }
    })
  } catch (err) {
    console.error(0x00000, 'ReleaseFunc', 'ReleaseFunc failed: ' + err);
  }
}
```

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
function ReleaseFunc(creator: image.ImageCreator): void {
  try {
    await creator.release();
  } catch (err) {
    console.error(0x00000, 'ReleaseFunc', 'ReleaseFunc failed: ' + err);
  }
}
```

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function ReleaseFunc(): void {
  try {
    let imagePacker: image.ImagePacker = image.createImagePacker();
    imagePacker.release((err: BusinessError | null) => {
      if (err) {
        console.error(0x00000, 'ReleaseFunc', 'release failed: ' + err);
      } else {
        console.info(0x00000, 'ReleaseFunc', 'release success!');
      }
    });
  } catch (err) {
    console.error(0x00000, 'ReleaseFunc', 'ReleaseFunc failed: ' + err);
  }
}
```

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
async function ReleaseFunc(): Promise<void> {
  try {
    let imagePacker: image.ImagePacker = image.createImagePacker();
    await imagePacker.release();
    console.info(0x00000, 'ReleaseFunc', 'release success!');
  } catch (err) {
    console.error(0x00000, 'ReleaseFunc', 'ReleaseFunc failed: ' + err);
  }
}
```

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function ReleaseFunc(): void {
  let size: image.Size = { height: 8192, width: 8 };
  try {
    let receiver = image.createImageReceiver(size, image.ImageFormat.JPEG, 8);
    receiver.release((err: BusinessError | null) => {
      if (err) {
        console.error(0x00000, 'ReleaseFunc', 'release failed: ' + err);
      } else {
        console.info(0x00000, 'ReleaseFunc', 'ReleaseFunc success!');
      }
    });
  } catch (err) {
    console.error(0x00000, 'ReleaseFunc', 'ReleaseFunc failed: ' + err);
  }
}
```

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
function ReleaseFunc(): void {
  let size: image.Size = { height: 8192, width: 8 };
  try {
    let receiver = image.createImageReceiver(size, image.ImageFormat.JPEG, 8);
    await receiver.release();
    console.info(0x00000, 'ReleaseFunc', 'release success!');
  } catch (err) {
    console.error(0x00000, 'ReleaseFunc', 'ReleaseFunc failed: ' + err);
  }
}
```

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function ReleaseFunc(imageSource: image.ImageSource): void {
  try {
    imageSource.release((err: BusinessError | null) => {
      if (err) {
        console.error(0x00000, 'ReleaseFunc', 'release failed: ' + err);
      } else {
        console.info(0x00000, 'ReleaseFunc', 'release success!');
      }
    });
  } catch (err) {
    console.error(0x00000, 'ReleaseFunc', 'ReleaseFunc failed: ' + err);
  }
}
```

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
async function ReleaseFunc(imageSource: image.ImageSource): Promise<void> {
  try {
    await imageSource.release();
    console.info(0x00000, 'ReleaseFunc', 'release success!');
  } catch (err) {
    console.error(0x00000, 'ReleaseFunc', 'ReleaseFunc failed: ' + err);
  }
}
```

ArkTS-Dyn示例：

```TypeScript
async function Release(pictureObj : image.Picture) {
  let funcName = "Release";
  if (pictureObj != null) {
    pictureObj.release();
    if (pictureObj.getMainPixelmap() == null) {
      console.info(funcName, 'Succeeded in releasing a picture.');
    } else {
      console.error(funcName, 'Failed to release a picture.');
    }
  } else {
    console.error('Picture object is null.');
  }
}
```

ArkTS-Sta示例：

```TypeScript
function ReleaseFunc(picture: image.Picture): void {
  try {
    picture.release();
    console.info(0x00000, 'ReleaseFunc', 'release success!');
  } catch (err) {
    console.error(0x00000, 'ReleaseFunc', 'ReleaseFunc failed: ' + err);
  }
}
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function release(pixelMap: image.PixelMap) {
  pixelMap.release().then(() => {
    console.info('Succeeded in releasing the PixelMap object.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to release the PixelMap object. Code: ${err.code}, message: ${err.message}`);
  });
}
```

ArkTS-Sta示例：

```TypeScript
function release(pixelMap: image.PixelMap) {
  pixelMap.release().then(() => {
    console.info('Succeeded in releasing the PixelMap object.');
  }).catch((err: Error) => {
    console.error(`Failed to release the PixelMap object. Code: ${err.code}, message: ${err.message}`);
  });
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function release(pixelMap: image.PixelMap) {
  pixelMap.release((err: BusinessError) => {
    if (err) {
      console.error(`Failed to release the PixelMap object. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info('Succeeded in releasing the PixelMap object.');
  });
}
```

## setAuxiliaryPicture

```TypeScript
setAuxiliaryPicture(type: AuxiliaryPictureType, auxiliaryPicture: AuxiliaryPicture): void
```

设置辅助图。

**起始版本：** 23

<!--Device-Picture-setAuxiliaryPicture(type: AuxiliaryPictureType, auxiliaryPicture: AuxiliaryPicture): void--><!--Device-Picture-setAuxiliaryPicture(type: AuxiliaryPictureType, auxiliaryPicture: AuxiliaryPicture): void-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [AuxiliaryPictureType](arkts-image-image-auxiliarypicturetype-e.md) | 是 | 辅助图类型。 |
| auxiliaryPicture | [AuxiliaryPicture](arkts-image-image-auxiliarypicture-i.md) | 是 | 辅助图对象。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |

**示例**

ArkTS-Dyn示例：

```TypeScript
async function SetAuxiliaryPicture(context: Context) {
  const resourceMgr = context.resourceManager;
  const rawFile = await resourceMgr.getRawFileContent("hdr.jpg");// 需要支持hdr的图片。
  let ops: image.SourceOptions = {
    sourceDensity: 98,
  }
  let imageSource: image.ImageSource = image.createImageSource(rawFile.buffer as ArrayBuffer, ops);
  let pixelMap: image.PixelMap = await imageSource.createPixelMap();
  let pictureObj: image.Picture = image.createPicture(pixelMap);
  if (pictureObj != null) {
    console.info('Succeeded in creating picture.');
  } else {
    console.error('Failed to create picture.');
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

ArkTS-Sta示例：

```TypeScript
function SetAuxiliaryPictureFunc(picture: image.Picture, auxPixelMap: image.AuxiliaryPicture): void {
  let type: image.AuxiliaryPictureType = image.AuxiliaryPictureType.GAINMAP;
  try {
    picture.setAuxiliaryPicture(type, auxPixelMap);
    console.info(0x00000, 'SetAuxiliaryPictureFunc', 'setAuxiliaryPicture success!');
  } catch (err) {
    console.error(0x00000, 'SetAuxiliaryPictureFunc', 'SetAuxiliaryPictureFunc failed: ' + err);
  }
}
```

## setMainPixelmap

```TypeScript
setMainPixelmap(pixelmap: PixelMap): void
```

设置图片的PixelMap对象。

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Picture-setMainPixelmap(pixelmap: PixelMap): void--><!--Device-Picture-setMainPixelmap(pixelmap: PixelMap): void-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pixelmap | PixelMap | 是 | PixelMap对象。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [7700204](../errorcode-image.md#7700204-无效参数) | 参数错误。 |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function setMainPixelmap(picture : image.Picture, pixelmap : image.PixelMap) {
  if (picture == null || pixelmap == null) {
    console.error('picture or pixelmap is null');
    return;
  }
  try {
    picture.setMainPixelmap(pixelmap);
  } catch(error) {
    console.error(`Failed to do setMainPixelmap. error.code: ${error.code} ,error.message: ${error.message}`);
  }
}
```

## setMetadata

```TypeScript
setMetadata(metadataType: MetadataType, metadata: Metadata): Promise<void>
```

设置主图的元数据。使用Promise异步回调。

**起始版本：** 23

<!--Device-Picture-setMetadata(metadataType: MetadataType, metadata: Metadata): Promise<void>--><!--Device-Picture-setMetadata(metadataType: MetadataType, metadata: Metadata): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| metadataType | [MetadataType](arkts-image-image-metadatatype-e.md) | 是 | 元数据类型。 |
| metadata | Metadata | 是 | 元数据对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| [7600202](../errorcode-image.md#7600202-不支持的元数据读写) | Unsupported metadata. Possible causes: 1. Unsupported metadata type. 2. The metadata type does not match the auxiliary picture type. |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function SetAuxPictureObjMetadata(exifContext: Context, auxPictureObj: image.AuxiliaryPicture) {
  const exifResourceMgr = exifContext.resourceManager;
  const exifRawFile = await exifResourceMgr.getRawFileContent("exif.jpg");// 图片包含exif metadata。
  let exifOps: image.SourceOptions = {
    sourceDensity: 98,
  }
  let exifImageSource: image.ImageSource = image.createImageSource(exifRawFile.buffer as ArrayBuffer, exifOps);
  let exifCommodityPixelMap: image.PixelMap = await exifImageSource.createPixelMap();
  let exifPictureObj: image.Picture = image.createPicture(exifCommodityPixelMap);
  if (exifPictureObj != null) {
    console.info('Succeeded in creating picture.');
  } else {
    console.error('Failed to create picture.');
  }

  if (auxPictureObj != null) {
    let metadataType: image.MetadataType = image.MetadataType.EXIF_METADATA;
    let exifMetaData: image.Metadata = await exifPictureObj.getMetadata(metadataType);
    auxPictureObj.setMetadata(metadataType, exifMetaData).then(() => {
      console.info('Succeeded in setting metadata.');
    }).catch((error: BusinessError) => {
      console.error(`Failed to set metadata. error.code: ${error.code}, error.message: ${error.message}`);
    });
  } else {
    console.error('AuxPictureObjMetaData is null');
  }
}
```

ArkTS-Sta示例：

```TypeScript
import { common } from '@kit.AbilityKit';

function SetMetadataFunc(auxPicture: image.AuxiliaryPicture, context: common.UIAbilityContext): void {
  const resourceMgr = context.resourceManager;
  const rawFile = await resourceMgr.getRawFileContent("hdr_exif_image.jpg");
  let opts: image.SourceOptions = { sourceDensity: 98 };
  try {
    let imageSource: image.ImageSource = image.createImageSource(rawFile.buffer as ArrayBuffer, opts);
    let pixelMap: image.PixelMap = await imageSource.createPixelMap(); // 解码图片获取PixelMap。
    let picture: image.Picture = image.createPicture(pixelMap); // 创建Picture对象以获取元数据。
    let metadataType: image.MetadataType = image.MetadataType.EXIF_METADATA;
    let metadata: image.Metadata | null = await picture.getMetadata(metadataType); // 从Picture获取EXIF元数据。
    if (metadata != null) {
       auxPicture.setMetadata(metadataType, metadata); // 将元数据设置到辅助图对象。
       console.info(0x00000, 'SetMetadataFunc', 'setMetadata success!');
    }
  } catch (err) {
    console.error(0x00000, 'SetMetadataFunc', 'SetMetadataFunc failed: ' + err);
  }
}
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function SetPictureObjMetadata(exifContext: Context) {
  const exifResourceMgr = exifContext.resourceManager;
  const exifRawFile = await exifResourceMgr.getRawFileContent("exif.jpg");// 含有exif metadata的图片。
  let exifOps: image.SourceOptions = {
    sourceDensity: 98,
  }
  let exifImageSource: image.ImageSource = image.createImageSource(exifRawFile.buffer as ArrayBuffer, exifOps);
  let exifCommodityPixelMap: image.PixelMap = await exifImageSource.createPixelMap();
  let exifPictureObj: image.Picture = image.createPicture(exifCommodityPixelMap);
  if (exifPictureObj != null) {
    console.info('Succeeded in creating picture.');
  } else {
    console.error('Failed to create picture.');
  }

  if (exifPictureObj != null) {
    let metadataType: image.MetadataType = image.MetadataType.EXIF_METADATA;
    let exifMetaData: image.Metadata = await exifPictureObj.getMetadata(metadataType);
    exifPictureObj.setMetadata(metadataType, exifMetaData).then(() => {
      console.info('Succeeded in setting metadata.');
    }).catch((error: BusinessError) => {
      console.error(`Failed to set metadata. error.code: ${error.code} ,error.message: ${error.message}`);
    });
  } else {
    console.error('exifPictureObj is null');
  }
}
```

ArkTS-Sta示例：

```TypeScript
function SetMetadataFunc(picture: image.Picture): void {
  try {
    let metadataType: image.MetadataType = image.MetadataType.EXIF_METADATA;
    let metaData: image.Metadata = await picture.getMetadata(metadataType);
    await picture.setMetadata(metadataType, metaData);
    console.info(0x00000, 'SetMetadataFunc', 'setMetadata success!');
  } catch (err) {
    console.error(0x00000, 'SetMetadataFunc', 'SetMetadataFunc failed: ' + err);
  }
}
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function setMetadata(pixelMap: image.PixelMap) { // 入参pixelMap内存类型需为DMA_ALLOC内存类型，其创建方法请参考上方说明。
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
    console.info('Succeeded in setting the metadata.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to set the metadata. Code: ${err.code}, message: ${err.message}`);
  });
}
```

ArkTS-Sta示例：

```TypeScript
function setMetadata(pixelMap: image.PixelMap) { // 入参pixelMap内存类型需为DMA_ALLOC内存类型，其创建方法请参考上方说明。
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
    console.info('Succeeded in setting the metadata.');
  }).catch((err: Error) => {
    console.error(`Failed to set the metadata. Code: ${err.code}, message: ${err.message}`);
  });
}
```

