# ImagePacker

ImagePacker类，用于图片压缩和编码。在调用ImagePacker的方法前，需要先通过[image.createImagePacker](arkts-image-image-createimagepacker-f.md)构建一个ImagePacker实例。编码期间，请避免修改或释放作为输入的ImageSource/PixelMap/Picture对象，以免出现crash或其他未定义行为。由于图片占用内存较大，所以当ImagePacker实例使用完成后，应主动调用[release](#release)方法及时 释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。当前支持的格式有：JPEG、WebP、PNG、HEIC&lt;sup&gt;12+&lt;/sup&gt;、GIF&lt;sup&gt;18+&lt;/sup&gt;、从API版本26.0.0开始支持TIFF格式（不同硬件设备支持情况不同，可通过ImagePacker的 supportedFormats属性查看）。

**起始版本：** 6

**ArkTS模式：** ArkTS-Dyn起始版本为6；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

## 导入模块

```TypeScript
import { image } from '@kit.ImageKit';
```

## packBinaryImageToTiffData

```TypeScript
packBinaryImageToTiffData(bufferInfo: BinaryBufferInfo, options?: PackingOptionsForTiff): Promise<ArrayBuffer>
```

将二值图像数据编码为TIFF数据，以ArrayBuffer的形式返回。使用Promise异步回调。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bufferInfo | [BinaryBufferInfo](arkts-image-image-binarybufferinfo-i.md) | 是 |
| options | [PackingOptionsForTiff](arkts-image-image-packingoptionsfortiff-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;ArrayBuffer & gt; |

**错误码：**

| 错误码ID |
| --- |
| [7800202](../errorcode-image.md#7800202-imagepacker无效参数) |
| [7800301](../errorcode-image.md#7800301-编码失败) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { image } from '@kit.ImageKit';

const DOMAIN = 0X00000;
const TAG: string = 'PackBinaryImageToTiffData';

async function PackBinaryImageToTiffData() {
  const width = 100;
  const height = 100;
  const rowBytes = 13;
  const bufferSize = rowBytes * height;
  const data: ArrayBuffer = new ArrayBuffer(bufferSize);

  let bufferInfo: image.BinaryBufferInfo = {
    size: { width: width, height: height },
    data: data,
    bytesPerRow: rowBytes
  };

  let tiffOptions: image.PackingOptionsForTiff = {
    compression: 4 // CCITT G4压缩
  };

  const imagePackerObj: image.ImagePacker = image.createImagePacker();
  await imagePackerObj.packBinaryImageToTiffData(bufferInfo, tiffOptions)
    .then((data: ArrayBuffer) => {
      hilog.info(DOMAIN, TAG, 'Succeeded in packing binary image to tiff data.');
    }).catch((error: BusinessError) => {
      hilog.error(DOMAIN, TAG, `Failed to pack binary image to tiff data. code ${error.code}, message is ${error.message}`);
    });
}
```

## packBinaryImageToTiffFile

ArkTS-Dyn:
```TypeScript
packBinaryImageToTiffFile(bufferInfo: BinaryBufferInfo, fd: number, options?: PackingOptionsForTiff): Promise<void>
```

ArkTS-Sta:
```TypeScript
packBinaryImageToTiffFile(bufferInfo: BinaryBufferInfo, fd: int, options?: PackingOptionsForTiff): Promise<void>
```

将二值图像数据编码到入参fd对应的TIFF文件。使用Promise异步回调。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bufferInfo | [BinaryBufferInfo](arkts-image-image-binarybufferinfo-i.md) | 是 |
| fd | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |
| options | [PackingOptionsForTiff](arkts-image-image-packingoptionsfortiff-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [7800202](../errorcode-image.md#7800202-imagepacker无效参数) |
| [7800301](../errorcode-image.md#7800301-编码失败) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { image } from '@kit.ImageKit';

const DOMAIN = 0X00000;
const TAG: string = 'PackBinaryImageToTiffFile';

async function PackBinaryImageToTiffFile(context: Context) {
  const width = 100;
  const height = 100;
  const rowBytes = 13;
  const bufferSize = rowBytes * height;
  const data: ArrayBuffer = new ArrayBuffer(bufferSize);

  let bufferInfo: image.BinaryBufferInfo = {
    size: { width: width, height: height },
    data: data,
    bytesPerRow: rowBytes
  };

  const filePath: string = context.filesDir + "/output.tiff";
  let file = fileIo.openSync(filePath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);

  let tiffOptions: image.PackingOptionsForTiff = {
    compression: 4 // CCITT G4压缩
  };

  const imagePackerObj: image.ImagePacker = image.createImagePacker();
  await imagePackerObj.packBinaryImageToTiffFile(bufferInfo, file.fd, tiffOptions)
    .then(() => {
      hilog.info(DOMAIN, TAG, 'Succeeded in packing binary image to tiff file.');
    }).catch((error: BusinessError) => {
      hilog.error(DOMAIN, TAG, `Failed to pack binary image to tiff file. code ${error.code}, message is ${error.message}`);
    });
  fileIo.closeSync(file);
}
```

## packing

```TypeScript
packing(source: ImageSource, option: PackingOption, callback: AsyncCallback<ArrayBuffer>): void
```

图片压缩或重新编码。使用callback异步回调。

> **说明：**&gt;
> [packToData](#packtodata)代替。

**起始版本：** 6

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为6。

**废弃版本：** 13

**替代接口：** [packToData](#packtodata)

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| source | [ImageSource](arkts-image-sendableimage-imagesource-i.md) | 是 |
| option | [PackingOption](arkts-image-image-packingoption-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;ArrayBuffer&gt; | 是 |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function Packing(context: Context) {
  const resourceMgr = context.resourceManager;
  const rawFile = await resourceMgr.getRawFileContent("test.jpg");
  let ops: image.SourceOptions = {
    sourceDensity: 98,
  }
  let imageSource: image.ImageSource = image.createImageSource(rawFile.buffer as ArrayBuffer, ops);
  let commodityPixelMap: image.PixelMap = await imageSource.createPixelMap();
  let pictureObj: image.Picture = image.createPicture(commodityPixelMap);
  const imagePackerObj: image.ImagePacker = image.createImagePacker();
  let funcName = "Packing";
  if (imagePackerObj != null) {
    let opts: image.PackingOption = {
      format: "image/jpeg",
      quality: 98,
      desiredDynamicRange: image.PackingDynamicRange.AUTO,
      needsPackProperties: true};
    await imagePackerObj.packing(pictureObj, opts).then((data: ArrayBuffer) => {
      console.info(funcName, 'Succeeded in packing the image.'+ data);
    }).catch((error: BusinessError) => {
      console.error(funcName, `Failed to pack the image.code ${error.code},message is ${error.message}`);
    });
  }
}
```

ArkTS-Sta示例：

```TypeScript
import { common } from '@kit.AbilityKit';

async function PackingFunc(context: common.UIAbilityContext): Promise<void> {
  const resourceMgr = context.resourceManager;
  const rawFile = await resourceMgr.getRawFileContent("test_image.jpg");
  let opts: image.SourceOptions = { sourceDensity: 98 };
  try {
    let imageSource = image.createImageSource(rawFile.buffer as ArrayBuffer, opts);
    let pixelMap: image.PixelMap = await imageSource.createPixelMap(); // 解码图片为PixelMap对象。
    let picture: image.Picture = image.createPicture(pixelMap); // 使用PixelMap创建Picture对象。
    const imagePacker: image.ImagePacker = image.createImagePacker();
    let packingOpts: image.PackingOption = { format: "image/jpeg", quality: 98, bufferSize: 10 };
    let arrayBuffer: ArrayBuffer = await imagePacker.packing(picture, packingOpts); // 将Picture对象编码为ArrayBuffer。
    console.info(0x00000, 'PackingFunc', 'packing success!');
  } catch (err) {
    console.error(0x00000, 'PackingFunc', 'PackingFunc failed: ' + err);
  }
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function Packing(context : Context) {
  // 此处'test.jpg'仅作示例，请开发者自行替换，否则imageSource会创建失败导致后续无法正常执行。
  let filePath: string = context.filesDir + "/test.jpg";
  const imageSourceObj: image.ImageSource = image.createImageSource(filePath);
  let packOpts: image.PackingOption = { format: "image/jpeg", quality: 98 };
  const imagePackerObj: image.ImagePacker = image.createImagePacker();
  imagePackerObj.packing(imageSourceObj, packOpts, (err: BusinessError, data: ArrayBuffer) => {
    if (err) {
      console.error(`Failed to pack the image.code ${err.code},message is ${err.message}`);
    } else {
      console.info('Succeeded in packing the image.');
    }
  })
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function Packing(context : Context) {
  // 此处'test.jpg'仅作示例，请开发者自行替换，否则imageSource会创建失败导致后续无法正常执行。
  let filePath: string = context.filesDir + "/test.jpg";
  const imageSourceObj: image.ImageSource = image.createImageSource(filePath);
  let packOpts: image.PackingOption = { format: "image/jpeg", quality: 98 }
  const imagePackerObj: image.ImagePacker = image.createImagePacker();
  imagePackerObj.packing(imageSourceObj, packOpts)
    .then((data: ArrayBuffer) => {
      console.info('Succeeded in packing the image.');
    }).catch((error: BusinessError) => {
      console.error(`Failed to pack the image.code ${error.code},message is ${error.message}`);
    })
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function Packing() {
  const color: ArrayBuffer = new ArrayBuffer(96); // 96为需要创建的像素buffer大小，取值为：height * width *4。
  let opts: image.InitializationOptions = { editable: true, pixelFormat: image.PixelMapFormat.RGBA_8888, size: { height: 4, width: 6 } }
  image.createPixelMap(color, opts).then((pixelMap: image.PixelMap) => {
    let packOpts: image.PackingOption = { format: "image/jpeg", quality: 98 }
    const imagePackerObj: image.ImagePacker = image.createImagePacker();
    imagePackerObj.packing(pixelMap, packOpts, (err: BusinessError, data: ArrayBuffer) => {
      if (err) {
        console.error(`Failed to pack the image.code ${err.code},message is ${err.message}`);
      } else {
        console.info('Succeeded in packing the image.');
      }
    })
  }).catch((error: BusinessError) => {
    console.error(`Failed to create the PixelMap.code ${error.code},message is ${error.message}`);
  })
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function Packing() {
  const color: ArrayBuffer = new ArrayBuffer(96); // 96为需要创建的像素buffer大小，取值为：height * width *4。
  let opts: image.InitializationOptions = { editable: true, pixelFormat: image.PixelMapFormat.RGBA_8888, size: { height: 4, width: 6 } }
  image.createPixelMap(color, opts).then((pixelMap: image.PixelMap) => {
    let packOpts: image.PackingOption = { format: "image/jpeg", quality: 98 }
    const imagePackerObj: image.ImagePacker = image.createImagePacker();
    imagePackerObj.packing(pixelMap, packOpts)
      .then((data: ArrayBuffer) => {
        console.info('Succeeded in packing the image.');
      }).catch((error: BusinessError) => {
      console.error(`Failed to pack the image.code ${error.code},message is ${error.message}`);
    })
  }).catch((error: BusinessError) => {
    console.error(`Failed to create PixelMap.code ${error.code},message is ${error.message}`);
  })
}
```

## packing

```TypeScript
packing(source: ImageSource, option: PackingOption): Promise<ArrayBuffer>
```

图片压缩或重新编码。使用Promise异步回调。

> **说明：**&gt;
> [packToData](#packtodata)代替。

**起始版本：** 6

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为6。

**废弃版本：** 13

**替代接口：** [packToData](#packtodata)

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| source | [ImageSource](arkts-image-sendableimage-imagesource-i.md) | 是 |
| option | [PackingOption](arkts-image-image-packingoption-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;ArrayBuffer & gt; |

**示例**

参见 [packing](#packing)

## packing

```TypeScript
packing(source: PixelMap, option: PackingOption, callback: AsyncCallback<ArrayBuffer>): void
```

图片压缩或重新编码。使用callback异步回调。

> **说明：**&gt;
> [packToData](#packtodata)代替。
> 
> **注意：**&gt;
> 接口如果返回"PixelMap mismatch"，表明参数异常，可能是PixelMap对象被提前释放了。需要调用方排查，在该方法调用结束后再释放PixelMap对象。

**起始版本：** 8

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为8。

**废弃版本：** 13

**替代接口：** [packToData](#packtodata)

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| source | [PixelMap](arkts-image-image-pixelmap-i.md) | 是 |
| option | [PackingOption](arkts-image-image-packingoption-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;ArrayBuffer&gt; | 是 |

**示例**

参见 [packing](#packing)

## packing

```TypeScript
packing(source: PixelMap, option: PackingOption): Promise<ArrayBuffer>
```

图片压缩或重新编码。使用Promise异步回调。

> **说明：**&gt;
> [packToData](#packtodata)代替。
> 
> **注意：**&gt;
> 接口如果返回"PixelMap mismatch"，表明参数异常，可能是PixelMap对象被提前释放了。需要调用方排查，在该方法调用结束后再释放PixelMap对象。

**起始版本：** 8

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为8。

**废弃版本：** 13

**替代接口：** [packToData](#packtodata)

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| source | [PixelMap](arkts-image-image-pixelmap-i.md) | 是 |
| option | [PackingOption](arkts-image-image-packingoption-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;ArrayBuffer & gt; |

**示例**

参见 [packing](#packing)

## packing

```TypeScript
packing(picture: Picture, options: PackingOption): Promise<ArrayBuffer>
```

将图像压缩或重新编码。使用Promise异步回调。

**起始版本：** 13

**ArkTS模式：** ArkTS-Dyn起始版本为13；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| picture | [Picture](arkts-image-image-picture-i.md) | 是 |
| options | [PackingOption](arkts-image-image-packingoption-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;ArrayBuffer & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [7800301](../errorcode-image.md#7800301-编码失败) |

**示例**

参见 [packing](#packing)

## packToData

```TypeScript
packToData(source: ImageSource, options: PackingOption): Promise<ArrayBuffer>
```

图片压缩或重新编码。使用Promise异步回调。

**起始版本：** 13

**ArkTS模式：** ArkTS-Dyn起始版本为13；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本13开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| source | [ImageSource](arkts-image-sendableimage-imagesource-i.md) | 是 |
| options | [PackingOption](arkts-image-image-packingoption-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;ArrayBuffer & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [62980096](../errorcode-image.md#62980096-操作失败) |
| [62980101](../errorcode-image.md#62980101-图片输入数据错误) |
| [62980106](../errorcode-image.md#62980106-图片数据太大) |
| [62980113](../errorcode-image.md#62980113-图片未知格式) |
| [62980119](../errorcode-image.md#62980119-图片编码失败) |
| [62980120](../errorcode-image.md#62980120-图片添加像素映射失败) |
| [62980172](../errorcode-image.md#62980172-编码icc失败) |
| [62980252](../errorcode-image.md#62980252-创建surface失败) |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function PackToData(context : Context) {
  // 此处'test.jpg'仅作示例，请开发者自行替换，否则imageSource会创建失败导致后续无法正常执行。
  let filePath: string = context.filesDir + "/test.jpg";
  const imageSourceObj: image.ImageSource = image.createImageSource(filePath);
  let packOpts: image.PackingOption = { format: "image/jpeg", quality: 98 }
  const imagePackerObj: image.ImagePacker = image.createImagePacker();
  imagePackerObj.packToData(imageSourceObj, packOpts)
    .then((data: ArrayBuffer) => {
      console.info('Succeeded in packing the image.');
    }).catch((error: BusinessError) => {
      console.error(`Failed to pack the image.code ${error.code},message is ${error.message}`);
    })
}
```

ArkTS-Sta示例：

```TypeScript
import { common } from '@kit.AbilityKit';

async function ImagePackerFunc(context: common.UIAbilityContext): Promise<void> {
  // 此处'test_image.jpg'仅作示例，请开发者自行替换，否则imageSource会创建失败导致后续无法正常执行。
  let filePath: string = context.filesDir + "test_image.jpg";
  try {
    let imageSource = image.createImageSource(filePath);
    let packOpts: image.PackingOption = { format: "image/jpeg", quality: 98 };
    let imagePacker: image.ImagePacker = image.createImagePacker();
    let arrayBuffer: ArrayBuffer = await imagePacker.packToData(imageSource, packOpts);
    console.info(0x00000, 'ImagePackerFunc', 'packToData success!');
  } catch (err) {
    console.error(0x00000, 'ImagePackerFunc', 'ImagePackerFunc failed: ' + err);
  }
}
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function PackToData() {
  const color: ArrayBuffer = new ArrayBuffer(96); // 96为需要创建的像素buffer大小，取值为：height * width * 4。
  let opts: image.InitializationOptions = { editable: true, pixelFormat: 3, size: { height: 4, width: 6 } }
  image.createPixelMap(color, opts).then((pixelMap: image.PixelMap) => {
    let packOpts: image.PackingOption = { format: "image/jpeg", quality: 98 }
    const imagePackerObj: image.ImagePacker = image.createImagePacker();
    imagePackerObj.packToData(pixelMap, packOpts)
      .then((data: ArrayBuffer) => {
        console.info('Succeeded in packing the image.');
      }).catch((error: BusinessError) => {
      console.error(`Failed to pack the image.code ${error.code},message is ${error.message}`);
    })
  }).catch((error: BusinessError) => {
    console.error(`Failed to create PixelMap.code ${error.code},message is ${error.message}`);
  })
}
```

ArkTS-Sta示例：

```TypeScript
async function ImagePackerFunc(): Promise<void> {
  const color: ArrayBuffer = new ArrayBuffer(96); // 96为需要创建的像素buffer大小，取值为：height * width * 4。
  let opts: image.InitializationOptions = {
    size: { height: 4, width: 6 },
    editable: true,
    pixelFormat: image.PixelMapFormat.RGBA_8888,
  };
  try {
    let pixelMap: image.PixelMap = await image.createPixelMap(color, opts);
    let packOpts: image.PackingOption = { format: "image/jpeg", quality: 98 };
    let imagePacker: image.ImagePacker = image.createImagePacker();
    let arrayBuffer: ArrayBuffer = await imagePacker.packToData(pixelMap, packOpts);
    console.info(0x00000, 'ImagePackerFunc', 'packToData success!');
  } catch (err) {
    console.error(0x00000, 'ImagePackerFunc', 'ImagePackerFunc failed: ' + err);
  }
}
```

## packToData

```TypeScript
packToData(source: PixelMap, options: PackingOption): Promise<ArrayBuffer>
```

图片压缩或重新编码。使用Promise异步回调。

> **注意：**&gt;
> 接口如果返回401错误码，表明参数异常，可能是PixelMap对象被提前释放了。需要调用方排查，在该方法调用结束后再释放PixelMap对象。

**起始版本：** 13

**ArkTS模式：** ArkTS-Dyn起始版本为13；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本13开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| source | [PixelMap](arkts-image-image-pixelmap-i.md) | 是 |
| options | [PackingOption](arkts-image-image-packingoption-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;ArrayBuffer & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [62980096](../errorcode-image.md#62980096-操作失败) |
| [62980101](../errorcode-image.md#62980101-图片输入数据错误) |
| [62980106](../errorcode-image.md#62980106-图片数据太大) |
| [62980113](../errorcode-image.md#62980113-图片未知格式) |
| [62980119](../errorcode-image.md#62980119-图片编码失败) |
| [62980120](../errorcode-image.md#62980120-图片添加像素映射失败) |
| [62980172](../errorcode-image.md#62980172-编码icc失败) |
| [62980252](../errorcode-image.md#62980252-创建surface失败) |

**示例**

参见 [packToData](#packtodata)

## packToDataFromPixelmapSequence

```TypeScript
packToDataFromPixelmapSequence(pixelmapSequence: Array<PixelMap>, options: PackingOptionsForSequence): Promise<ArrayBuffer>
```

将多个PixelMap编码成GIF数据。使用Promise异步回调。

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| pixelmapSequence | Array & lt;PixelMap & gt; | 是 |
| options | [PackingOptionsForSequence](arkts-image-image-packingoptionsforsequence-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;ArrayBuffer & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [7800301](../errorcode-image.md#7800301-编码失败) |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function PackToDataFromPixelmapSequence(context : Context) {
  const resourceMgr = context.resourceManager;
  // 此处'moving_test.gif'仅作示例，请开发者自行替换。否则imageSource会创建失败，导致后续无法正常执行。
  const fileData = await resourceMgr.getRawFileContent('moving_test.gif');
  const color = fileData.buffer as ArrayBuffer;
  let imageSource = image.createImageSource(color);
  let pixelMapList = await imageSource.createPixelMapList();
  let ops: image.PackingOptionsForSequence = {
    frameCount: 3,  // 指定GIF编码中的帧数为3。
    delayTimeList: [10, 10, 10],  // 指定GIF编码中3帧的延迟时间分别为100ms、100ms、100ms。
    disposalTypes: [3, 2, 3], // 指定GIF编码中3帧的帧过渡模式分别为3（恢复到之前的状态）、2（恢复背景色)、3(恢复到之前的状态)。
    loopCount: 0 // 指定GIF编码中循环次数为无限循环。
  };
  let packer = image.createImagePacker();
  packer.packToDataFromPixelmapSequence(pixelMapList, ops)
    .then((data: ArrayBuffer) => {
      console.info('Succeeded in packing.');
    }).catch((error: BusinessError) => {
    console.error('Failed to packing.');
  })
}
```

ArkTS-Sta示例：

```TypeScript
import { common } from '@kit.AbilityKit';

async function PackToDataFromPixelmapSequenceFunc(context: common.UIAbilityContext): Promise<void> {
  const resourceMgr = context.resourceManager;
  // 此处'moving_test.gif'仅作示例，请开发者自行替换。否则imageSource会创建失败，导致后续无法正常执行。
  const fileData = await resourceMgr.getRawFileContent("moving_test.gif");
  const color = fileData.buffer as ArrayBuffer;
  let imageSource = image.createImageSource(color);
let pixelMapList = await imageSource.createPixelMapList(); // 从GIF文件解码出多个PixelMap帧。
    let opts: image.PackingOptionsForSequence = {
      frameCount: 3,  // 指定GIF编码中的帧数为3。
      delayTimeList: [10, 10, 10],  // 指定GIF编码中3帧的延迟时间分别为100ms、100ms、100ms。
      disposalTypes: [3, 2, 3], // 指定GIF编码中3帧的帧过渡模式分别为3（恢复到之前的状态）、2（恢复背景色)、3(恢复到之前的状态)。
      loopCount: 0 // 指定GIF编码中循环次数为无限循环。
    };
    let imagePacker: image.ImagePacker = image.createImagePacker();
    try {
      let array: ArrayBuffer = await imagePacker.packToDataFromPixelmapSequence(pixelMapList, opts); // 将PixelMap序列编码为GIF数据。
    console.info(0x00000, 'PackToDataFromPixelmapSequenceFunc', 'packToDataFromPixelmapSequence success!');
  } catch (err) {
    console.error(0x00000, 'PackToDataFromPixelmapSequenceFunc', 'PackToDataFromPixelmapSequenceFunc failed: ' + err);
  }
}
```

## packToFile

ArkTS-Dyn:
```TypeScript
packToFile(source: ImageSource, fd: number, options: PackingOption, callback: AsyncCallback<void>): void
```

ArkTS-Sta:
```TypeScript
packToFile(source: ImageSource, fd: int, options: PackingOption, callback: AsyncCallback<void>): void
```

指定编码参数，将ImageSource直接编码进文件。使用callback异步回调。

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| source | [ImageSource](arkts-image-sendableimage-imagesource-i.md) | 是 |
| fd | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |
| options | [PackingOption](arkts-image-image-packingoption-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [62980096](../errorcode-image.md#62980096-操作失败) |
| [62980101](../errorcode-image.md#62980101-图片输入数据错误) |
| [62980106](../errorcode-image.md#62980106-图片数据太大) |
| [62980113](../errorcode-image.md#62980113-图片未知格式) |
| [62980115](../errorcode-image.md#62980115-图片无效参数) |
| [62980119](../errorcode-image.md#62980119-图片编码失败) |
| [62980120](../errorcode-image.md#62980120-图片添加像素映射失败) |
| [62980172](../errorcode-image.md#62980172-编码icc失败) |
| [62980252](../errorcode-image.md#62980252-创建surface失败) |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';

async function PackToFile(context : Context) {
  // 此处'test.png'仅作示例，请开发者自行替换，否则imageSource会创建失败导致后续无法正常执行。
  const path: string = context.filesDir + "/test.png";
  const imageSourceObj: image.ImageSource = image.createImageSource(path);
  let packOpts: image.PackingOption = { format: "image/jpeg", quality: 98 };
  const filePath: string = context.filesDir + "/image_source.jpg";
  let file = fileIo.openSync(filePath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
  const imagePackerObj: image.ImagePacker = image.createImagePacker();
  imagePackerObj.packToFile(imageSourceObj, file.fd, packOpts, (err: BusinessError) => {
    if (err) {
      console.error(`Failed to pack the image to file.code ${err.code},message is ${err.message}`);
    } else {
      console.info('Succeeded in packing the image to file.');
    }
  })
}
```

ArkTS-Sta示例：

```TypeScript
import { common } from '@kit.AbilityKit';
import { fileIo } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';

function PackToFileFunc(context: common.UIAbilityContext): void {
  // 此处'test_image.png'仅作示例，请开发者自行替换，否则imageSource会创建失败导致后续无法正常执行。
  const path: string = context.filesDir + "test_image.png";
  const filePath: string = context.filesDir + "test_source.jpg"
  const imageSource = image.createImageSource(path);
  let packOpts: image.PackingOption = { format: "image/jpeg", quality: 98 };

  try {
    let file = fileIo.openSync(filePath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
    const imagePacker: image.ImagePacker = image.createImagePacker();
    imagePacker.packToFile(imageSource, file.fd, packOpts, (err: BusinessError | null) => {
      if (err) {
        console.error(0x00000, 'PackToFileFunc', 'packToFile failed: ' + err);
      } else {
        console.info(0x00000, 'PackToFileFunc', 'packToFile success!');
      }
    })
  } catch (err) {
    console.error(0x00000, 'PackToFileFunc', 'PackToFileFunc failed: ' + err);
  }
}
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';

async function PackToFile(context : Context) {
  // 此处'test.png'仅作示例，请开发者自行替换，否则imageSource会创建失败导致后续无法正常执行。
  const path: string = context.filesDir + "/test.png";
  const imageSourceObj: image.ImageSource = image.createImageSource(path);
  let packOpts: image.PackingOption = { format: "image/jpeg", quality: 98 };
  const filePath: string = context.filesDir + "/image_source.jpg";
  let file = fileIo.openSync(filePath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
  const imagePackerObj: image.ImagePacker = image.createImagePacker();
  imagePackerObj.packToFile(imageSourceObj, file.fd, packOpts).then(() => {
    console.info('Succeeded in packing the image to file.');
  }).catch((error: BusinessError) => { 
    console.error(`Failed to pack the image to file.code ${error.code},message is ${error.message}`);
  })
}
```

ArkTS-Sta示例：

```TypeScript
import { common } from '@kit.AbilityKit';
import { fileIo } from '@kit.CoreFileKit';

async function PackToFileFunc(context: common.UIAbilityContext): Promise<void> {
  // 此处'test_image.png'仅作示例，请开发者自行替换，否则imageSource会创建失败导致后续无法正常执行。
  const path: string = context.filesDir + "test_image.png";
  const filePath: string = context.filesDir + "test_source.jpg"
  const imageSource = image.createImageSource(path);
  let packOpts: image.PackingOption = { format: "image/jpeg", quality: 98 };

  try {
    let file = fileIo.openSync(filePath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
    const imagePacker: image.ImagePacker = image.createImagePacker();
    await imagePacker.packToFile(imageSource, file.fd, packOpts);
    console.info(0x00000, 'PackToFileFunc', 'packToFile success!');
  } catch (err) {
    console.error(0x00000, 'PackToFileFunc', 'PackToFileFunc failed: ' + err);
  }
}
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';

async function PackToFile(context : Context) {
  const color: ArrayBuffer = new ArrayBuffer(96); // 96为需要创建的像素buffer大小，取值为：height * width * 4。
  let opts: image.InitializationOptions = { editable: true, pixelFormat: image.PixelMapFormat.RGBA_8888, size: { height: 4, width: 6 } }
  const path: string = context.filesDir + "/pixel_map.jpg";
  image.createPixelMap(color, opts).then((pixelmap: image.PixelMap) => {
    let packOpts: image.PackingOption = { format: "image/jpeg", quality: 98 }
    let file = fileIo.openSync(path, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
    const imagePackerObj: image.ImagePacker = image.createImagePacker();
    imagePackerObj.packToFile(pixelmap, file.fd, packOpts, (err: BusinessError) => {
      if (err) {
        console.error(`Failed to pack the image to file.code ${err.code},message is ${err.message}`);
      } else {
        console.info('Succeeded in packing the image to file.');
      }
    })
  })
}
```

ArkTS-Sta示例：

```TypeScript
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';

function PackToFileFunc(context: common.UIAbilityContext): void {
  const color: ArrayBuffer = new ArrayBuffer(96); // 96为需要创建的像素buffer大小，取值为：height * width * 4。
  const path: string = context.filesDir + "test_source.jpg"
  let opts: image.InitializationOptions = {
    size: { height: 4, width: 6 },
    editable: true,
    pixelFormat: image.PixelMapFormat.RGBA_8888,
  };
  try {
    let pixelMap: image.PixelMap = await image.createPixelMap(color, opts);
    let file = fileIo.openSync(path, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
    let packOpts: image.PackingOption = { format: "image/jpeg", quality: 98 }
    const imagePacker: image.ImagePacker = image.createImagePacker();
    imagePacker.packToFile(pixelMap, file.fd, packOpts, (err: BusinessError | null) => {
      if (err) {
        console.error(0x00000, 'PackToFileFunc', 'packToFile failed: ' + err);
      } else {
        console.info(0x00000, 'PackToFileFunc', 'packToFile success!');
      }
    })
  } catch (err) {
    console.error(0x00000, 'PackToFileFunc', 'PackToFileFunc failed: ' + err);
  }
}
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';

async function PackToFile(context : Context) {
  const color: ArrayBuffer = new ArrayBuffer(96); // 96为需要创建的像素buffer大小，取值为：height * width * 4。
  let opts: image.InitializationOptions = { editable: true, pixelFormat: image.PixelMapFormat.RGBA_8888, size: { height: 4, width: 6 } }
  const path: string = context.filesDir + "/pixel_map.jpg";
  image.createPixelMap(color, opts).then((pixelmap: image.PixelMap) => {
    let packOpts: image.PackingOption = { format: "image/jpeg", quality: 98 }
    let file = fileIo.openSync(path, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
    const imagePackerObj: image.ImagePacker = image.createImagePacker();
    imagePackerObj.packToFile(pixelmap, file.fd, packOpts)
      .then(() => {
        console.info('Succeeded in packing the image to file.');
      }).catch((error: BusinessError) => {
      console.error(`Failed to pack the image to file.code ${error.code},message is ${error.message}`);
    })
  })
}
```

ArkTS-Sta示例：

```TypeScript
import { common } from '@kit.AbilityKit';
import { fileIo } from '@kit.CoreFileKit';

async function PackToFileFunc(context: common.UIAbilityContext): Promise<void> {
  const color: ArrayBuffer = new ArrayBuffer(96); // 96为需要创建的像素buffer大小，取值为：height * width * 4。
  const path: string = context.filesDir + "test_source.jpg"
  let opts: image.InitializationOptions = {
    size: { height: 4, width: 6 },
    editable: true,
    pixelFormat: image.PixelMapFormat.RGBA_8888,
  };
  try {
    let pixelMap: image.PixelMap = await image.createPixelMap(color, opts);
    let file = fileIo.openSync(path, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
    let packOpts: image.PackingOption = { format: "image/jpeg", quality: 98 }
    const imagePacker: image.ImagePacker = image.createImagePacker();
    await imagePacker.packToFile(pixelMap, file.fd, packOpts);
    console.info(0x00000, 'PackToFileFunc', 'packToFile success!');
  } catch (err) {
    console.error(0x00000, 'PackToFileFunc', 'PackToFileFunc failed: ' + err);
  }
}
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';

async function PackToFile(context: Context) {
  const resourceMgr = context.resourceManager;
  const rawFile = await resourceMgr.getRawFileContent("test.jpg");
  let ops: image.SourceOptions = {
    sourceDensity: 98,
  }
  let imageSource: image.ImageSource = image.createImageSource(rawFile.buffer as ArrayBuffer, ops);
  let commodityPixelMap: image.PixelMap = await imageSource.createPixelMap();
  let pictureObj: image.Picture = image.createPicture(commodityPixelMap);

  let funcName = "PackToFile";
  const imagePackerObj: image.ImagePacker = image.createImagePacker();
  if (imagePackerObj != null) {
    const filePath: string = context.filesDir + "/test.jpg";
    let file = fileIo.openSync(filePath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
    let packOpts: image.PackingOption = {
      format: "image/jpeg",
      quality: 98,
      desiredDynamicRange: image.PackingDynamicRange.AUTO,
      needsPackProperties: true};
    await imagePackerObj.packToFile(pictureObj, file.fd, packOpts).then(() => {
      console.info(funcName, 'Succeeded in packing the image to file.');
    }).catch((error: BusinessError) => {
      console.error(funcName, `Failed to pack the image to file.code ${error.code},message is ${error.message}`);
    });
  }
}
```

ArkTS-Sta示例：

```TypeScript
import { common } from '@kit.AbilityKit';
import { fileIo } from '@kit.CoreFileKit';
import { resourceManager } from '@kit.LocalizationKit';

async function PackToFileFunc(context: common.UIAbilityContext): Promise<void> {
  const resourceMgr = context.resourceManager;
  const filePath: string = context.filesDir + "test_source.jpg";
  let opts: image.SourceOptions = { sourceDensity: 98 };
  try {
    // 此处'test_image.jpg'仅作示例，请开发者自行替换，否则imageSource会创建失败导致后续无法正常执行。
    const rawFile = await resourceMgr.getRawFileContent("test_image.jpg");
    let imageSource = image.createImageSource(rawFile.buffer as ArrayBuffer, opts);
    let pixelMap: image.PixelMap = await imageSource.createPixelMap(); // 解码源图片为PixelMap。
    let picture: image.Picture = image.createPicture(pixelMap); // 创建Picture对象用于编码。
    const imagePacker: image.ImagePacker = image.createImagePacker();
    let file = fileIo.openSync(filePath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
    let packOpts: image.PackingOption = { format: "image/jpeg", quality: 98, bufferSize: 10 };
    await imagePacker.packToFile(picture, file.fd, packOpts); // 将Picture编码后直接写入文件。
    console.info(0x00000, 'PackToFileFunc', 'packToFile success!');
  } catch (err) {
    console.error(0x00000, 'PackToFileFunc', 'PackToFileFunc failed: ' + err);
  }
}
```

## packToFile

ArkTS-Dyn:
```TypeScript
packToFile(source: ImageSource, fd: number, options: PackingOption): Promise<void>
```

ArkTS-Sta:
```TypeScript
packToFile(source: ImageSource, fd: int, options: PackingOption): Promise<void>
```

指定编码参数，将ImageSource直接编码进文件。使用Promise异步回调。

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| source | [ImageSource](arkts-image-sendableimage-imagesource-i.md) | 是 |
| fd | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |
| options | [PackingOption](arkts-image-image-packingoption-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [62980096](../errorcode-image.md#62980096-操作失败) |
| [62980101](../errorcode-image.md#62980101-图片输入数据错误) |
| [62980106](../errorcode-image.md#62980106-图片数据太大) |
| [62980113](../errorcode-image.md#62980113-图片未知格式) |
| [62980115](../errorcode-image.md#62980115-图片无效参数) |
| [62980119](../errorcode-image.md#62980119-图片编码失败) |
| [62980120](../errorcode-image.md#62980120-图片添加像素映射失败) |
| [62980172](../errorcode-image.md#62980172-编码icc失败) |
| [62980252](../errorcode-image.md#62980252-创建surface失败) |

**示例**

参见 [packToFile](#packtofile)

## packToFile

ArkTS-Dyn:
```TypeScript
packToFile(source: PixelMap, fd: number, options: PackingOption, callback: AsyncCallback<void>): void
```

ArkTS-Sta:
```TypeScript
packToFile(source: PixelMap, fd: int, options: PackingOption, callback: AsyncCallback<void>): void
```

指定编码参数，将PixelMap直接编码进文件。使用callback异步回调。

> **注意：**&gt;
> 接口如果返回62980115错误码，表明参数异常，可能是PixelMap对象被提前释放了。需要调用方排查，在该方法调用结束后再释放PixelMap对象。

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| source | [PixelMap](arkts-image-image-pixelmap-i.md) | 是 |
| fd | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |
| options | [PackingOption](arkts-image-image-packingoption-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [62980096](../errorcode-image.md#62980096-操作失败) |
| [62980101](../errorcode-image.md#62980101-图片输入数据错误) |
| [62980106](../errorcode-image.md#62980106-图片数据太大) |
| [62980113](../errorcode-image.md#62980113-图片未知格式) |
| [62980115](../errorcode-image.md#62980115-图片无效参数) |
| [62980119](../errorcode-image.md#62980119-图片编码失败) |
| [62980120](../errorcode-image.md#62980120-图片添加像素映射失败) |
| [62980172](../errorcode-image.md#62980172-编码icc失败) |
| [62980252](../errorcode-image.md#62980252-创建surface失败) |

**示例**

参见 [packToFile](#packtofile)

## packToFile

ArkTS-Dyn:
```TypeScript
packToFile(source: PixelMap, fd: number, options: PackingOption): Promise<void>
```

ArkTS-Sta:
```TypeScript
packToFile(source: PixelMap, fd: int, options: PackingOption): Promise<void>
```

指定编码参数，将PixelMap直接编码进文件。使用Promise异步回调。

> **注意：**&gt;
> 接口如果返回62980115错误码，表明参数异常，可能是PixelMap对象被提前释放了。需要调用方排查，在该方法调用结束后再释放PixelMap对象。

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| source | [PixelMap](arkts-image-image-pixelmap-i.md) | 是 |
| fd | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |
| options | [PackingOption](arkts-image-image-packingoption-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [62980096](../errorcode-image.md#62980096-操作失败) |
| [62980101](../errorcode-image.md#62980101-图片输入数据错误) |
| [62980106](../errorcode-image.md#62980106-图片数据太大) |
| [62980113](../errorcode-image.md#62980113-图片未知格式) |
| [62980115](../errorcode-image.md#62980115-图片无效参数) |
| [62980119](../errorcode-image.md#62980119-图片编码失败) |
| [62980120](../errorcode-image.md#62980120-图片添加像素映射失败) |
| [62980172](../errorcode-image.md#62980172-编码icc失败) |
| [62980252](../errorcode-image.md#62980252-创建surface失败) |

**示例**

参见 [packToFile](#packtofile)

## packToFile

ArkTS-Dyn:
```TypeScript
packToFile(picture: Picture, fd: number, options: PackingOption): Promise<void>
```

ArkTS-Sta:
```TypeScript
packToFile(picture: Picture, fd: int, options: PackingOption): Promise<void>
```

指定编码参数，将Picture直接编码进文件。使用Promise异步回调。

**起始版本：** 13

**ArkTS模式：** ArkTS-Dyn起始版本为13；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| picture | [Picture](arkts-image-image-picture-i.md) | 是 |
| fd | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |
| options | [PackingOption](arkts-image-image-packingoption-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [7800301](../errorcode-image.md#7800301-编码失败) |

**示例**

参见 [packToFile](#packtofile)

## packToFileFromPixelmapSequence

ArkTS-Dyn:
```TypeScript
packToFileFromPixelmapSequence(pixelmapSequence: Array<PixelMap>, fd: number, options: PackingOptionsForSequence): Promise<void>
```

ArkTS-Sta:
```TypeScript
packToFileFromPixelmapSequence(pixelmapSequence: Array<PixelMap>, fd: int, options: PackingOptionsForSequence): Promise<void>
```

指定编码参数，将多个PixelMap编码成GIF文件。使用Promise异步回调。

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| pixelmapSequence | Array & lt;PixelMap & gt; | 是 |
| fd | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |
| options | [PackingOptionsForSequence](arkts-image-image-packingoptionsforsequence-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [7800301](../errorcode-image.md#7800301-编码失败) |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';

async function PackToFile(context : Context) {
  const resourceMgr = context.resourceManager;
  // 此处'moving_test.gif'仅作示例，请开发者自行替换。否则imageSource会创建失败，导致后续无法正常执行。
  const fileData = await resourceMgr.getRawFileContent('moving_test.gif');
  const color = fileData.buffer;
  let imageSource = image.createImageSource(color);
  let pixelMapList = await imageSource.createPixelMapList();
  let path: string = context.cacheDir + '/result.gif';
  let file = fileIo.openSync(path, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
  let ops: image.PackingOptionsForSequence = {
    frameCount: 3,  // 指定GIF编码中的帧数为3。
    delayTimeList: [10, 10, 10],  // 指定GIF编码中3帧的延迟时间分别为100ms、100ms、100ms。
    disposalTypes: [3, 2, 3], // 指定GIF编码中3帧的帧过渡模式分别为3（恢复到之前的状态）、2（恢复背景色)、3(恢复到之前的状态)。
    loopCount: 0 // 指定GIF编码中循环次数为无限循环。
  };
  let packer = image.createImagePacker();
  packer.packToFileFromPixelmapSequence(pixelMapList, file.fd, ops)
    .then(() => {
      console.info('Succeeded in packToFileMultiFrames.');
    }).catch((error: BusinessError) => {
    console.error('Failed to packToFileMultiFrames.');
  })
}
```

ArkTS-Sta示例：

```TypeScript
import { common } from '@kit.AbilityKit';
import { fileIo } from '@kit.CoreFileKit';
import { resourceManager } from '@kit.LocalizationKit';

async function PackToFileFromPixelmapSequenceFunc(context: common.UIAbilityContext): Promise<void> {
  const resourceMgr = context.resourceManager;
  // 此处'moving_test.gif'仅作示例，请开发者自行替换。否则imageSource会创建失败，导致后续无法正常执行。
  const fileData = await resourceMgr.getRawFileContent('moving_test.gif');
  const color = fileData.buffer;
  let imageSource = image.createImageSource(color);
let pixelMapList = await imageSource.createPixelMapList(); // 从源GIF文件解码出PixelMap帧序列。
    let path: string = context.filesDir + "test_source.gif";
    let file = fileIo.openSync(path, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE); // 打开目标文件用于写入编码结果。
    let opts: image.PackingOptionsForSequence = {
      frameCount: 3,  // 指定GIF编码中的帧数为3。
      delayTimeList: [10, 10, 10],  // 指定GIF编码中3帧的延迟时间分别为100ms、100ms、100ms。
      disposalTypes: [3, 2, 3], // 指定GIF编码中3帧的帧过渡模式分别为3（恢复到之前的状态）、2（恢复背景色)、3(恢复到之前的状态)。
      loopCount: 0 // 指定GIF编码中循环次数为无限循环。
    };
    let imagePacker: image.ImagePacker = image.createImagePacker();
    try {
      await imagePacker.packToFileFromPixelmapSequence(pixelMapList, file.fd, opts); // 将PixelMap序列编码并写入文件。
    console.info(0x00000, 'PackToFileFromPixelmapSequenceFunc', 'packToFileFromPixelmapSequence success!');
  } catch (err) {
    console.error(0x00000, 'PackToFileFromPixelmapSequenceFunc', 'PackToFileFromPixelmapSequenceFunc failed: ' + err);
  }
}
```

## release

```TypeScript
release(callback: AsyncCallback<void>): void
```

释放图片编码实例。使用callback异步回调。由于图片占用内存较大，所以当ImagePacker实例使用完成后，应主动调用该方法，及时释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**起始版本：** 6

**ArkTS模式：** ArkTS-Dyn起始版本为6；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

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

## release

```TypeScript
release(): Promise<void>
```

释放图片编码实例。使用Promise异步回调。由于图片占用内存较大，所以当ImagePacker实例使用完成后，应主动调用该方法，及时释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**起始版本：** 6

**ArkTS模式：** ArkTS-Dyn起始版本为6；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**示例**

参见 [release](#release)

## supportedFormats

```TypeScript
readonly supportedFormats: Array<string>
```

图片编码支持的格式，包括：JPEG、WebP、PNG、HEIC&lt;sup&gt;12+&lt;/sup&gt;、GIF&lt;sup&gt;18+&lt;/sup&gt;、从API版本26.0.0开始支持TIFF格式（不同硬件设备支持情况不同）。

**类型：** Array&lt;string&gt;

**起始版本：** 6

**ArkTS模式：** ArkTS-Dyn起始版本为6；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker
