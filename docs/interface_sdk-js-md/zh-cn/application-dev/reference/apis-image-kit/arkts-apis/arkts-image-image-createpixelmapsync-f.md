# createPixelMapSync

## 导入模块

```TypeScript
import { image } from '@kit.ImageKit';
```

## createPixelMapSync

```TypeScript
function createPixelMapSync(colors: ArrayBuffer, options: InitializationOptions): PixelMap
```

Create pixelmap by data buffer.Starting from API 26.0.0, it is recommended to use [createPixelMapFromPixelsSync](arkts-image-image-createpixelmapfrompixelssync-f.md) instead for better exception handling capabilities.

**起始版本：** 23

<!--Device-image-function createPixelMapSync(colors: ArrayBuffer, options: InitializationOptions): PixelMap--><!--Device-image-function createPixelMapSync(colors: ArrayBuffer, options: InitializationOptions): PixelMap-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| colors | ArrayBuffer | 是 | The image color buffer. |
| options | [InitializationOptions](arkts-image-image-initializationoptions-i.md) | 是 | Initialization options for pixelmap. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| PixelMap | Returns the instance if the operation is successful;Otherwise, return undefined. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function createPixelMapSync() {
  const color: ArrayBuffer = new ArrayBuffer(96); // 96为需要创建的像素缓冲区大小，取值为：width * height * 4。
  let opts: image.InitializationOptions = {
    size: { height: 4, width: 6 },
    srcPixelFormat: image.PixelMapFormat.RGBA_8888, // 缓冲区中的源像素数据的像素格式。
    pixelFormat: image.PixelMapFormat.BGRA_8888, // 新创建的PixelMap的像素格式。
    editable: true
  };
  try {
    let pixelMap: image.PixelMap = image.createPixelMapSync(color, opts);
    if (pixelMap == undefined) {
      console.error(`Failed to create the PixelMap.`);
      return;
    }
    console.info('Succeeded in creating the PixelMap.');
  } catch (e) {
    const err = e as BusinessError;
    console.error(`Failed to create the PixelMap. Code: ${err.code}, message: ${err.message}`);
  }
}
```

ArkTS-Sta示例：

```TypeScript
function createPixelMapSync() {
  const color: ArrayBuffer = new ArrayBuffer(96); // 96为需要创建的像素缓冲区大小，取值为：width * height * 4。
  let opts: image.InitializationOptions = {
    size: { height: 4, width: 6 },
    srcPixelFormat: image.PixelMapFormat.RGBA_8888, // 缓冲区中的源像素数据的像素格式。
    pixelFormat: image.PixelMapFormat.BGRA_8888, // 新创建的PixelMap的像素格式。
    editable: true
  };
  try {
    let pixelMap: image.PixelMap = image.createPixelMapSync(color, opts);
    console.info('Succeeded in creating the PixelMap.');
  } catch (err) {
    console.error(`Failed to create the PixelMap. Code: ${err.code}, message: ${err.message}`);
  }
}
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function createPixelMapSync() {
  let opts: image.InitializationOptions = { editable: true, pixelFormat: image.PixelMapFormat.RGBA_1010102, size: { height: 4, width: 6 } };
  try {
    let pixelMap: image.PixelMap = image.createPixelMapSync(opts);
    if (pixelMap == undefined) {
      console.error(`Failed to create the PixelMap.`);
      return;
    }
    console.info('Succeeded in creating the PixelMap.');
  } catch (e) {
    const err = e as BusinessError;
    console.error(`Failed to create the PixelMap. Code: ${err.code}, message: ${err.message}`);
  }
}
```

ArkTS-Sta示例：

```TypeScript
function createPixelMapSync() {
  let opts: image.InitializationOptions = { editable: true, pixelFormat: image.PixelMapFormat.RGBA_1010102, size: { height: 4, width: 6 } };
  try {
    let pixelMap: image.PixelMap = image.createPixelMapSync(opts);
    console.info('Succeeded in creating the PixelMap.');
  } catch (err) {
    console.error(`Failed to create the PixelMap. Code: ${err.code}, message: ${err.message}`);
  }
}
```

ArkTS-Dyn示例：

```TypeScript
function CreatePixelMapSync(context : Context) {
  // 此处'test.jpg'仅作示例，请开发者自行替换，否则imageSource创建失败会导致后续无法正常执行。
  let filePath: string = context.filesDir + "/test.jpg";
  let imageSource = image.createImageSource(filePath);
  let decodingOptions: image.DecodingOptions = {
    sampleSize: 1,
    editable: true,
    desiredSize: { width: 1, height: 2 },
    rotate: 10,
    desiredPixelFormat: image.PixelMapFormat.RGBA_8888,
    desiredRegion: { size: { width: 1, height: 2 }, x: 0, y: 0 },
    // 若解码接口同时传入了desiredSize参数与desiredRegion参数，需进一步传入cropAndScaleStrategy参数指定缩放与裁剪的先后顺序，推荐设置CROP_FIRST。
    cropAndScaleStrategy: image.CropAndScaleStrategy.CROP_FIRST,
    index: 0
  };
  let pixelmap = imageSource.createPixelMapSync(decodingOptions);
  if (pixelmap != undefined) {
    console.info('Succeeded in creating pixelMap object.');
  } else {
    console.error('Failed to create pixelMap.');
  }
}
```

ArkTS-Sta示例：

```TypeScript
function CreatePixelMapSyncFunc(imageSource: image.ImageSource): void {
  try {
    let pixelMap = imageSource.createPixelMapSync();
    console.info(0x00000, 'CreatePixelMapSyncFunc', 'createPixelMapSync success!');
  } catch (err) {
    console.error(0x00000, 'CreatePixelMapSyncFunc', 'CreatePixelMapSyncFunc failed: ' + err);
  }
}
```


## createPixelMapSync

```TypeScript
function createPixelMapSync(options: InitializationOptions): PixelMap
```

Create an empty pixelmap.Starting from API 26.0.0, it is recommended to use [createEmptyPixelMap](arkts-image-image-createemptypixelmap-f.md) instead for better exception handling capabilities.

**起始版本：** 23

<!--Device-image-function createPixelMapSync(options: InitializationOptions): PixelMap--><!--Device-image-function createPixelMapSync(options: InitializationOptions): PixelMap-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [InitializationOptions](arkts-image-image-initializationoptions-i.md) | 是 | Initialization options for pixelmap. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| PixelMap | Returns the instance if the operation is successful;Otherwise, return undefined. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |

**示例**

参见 [createPixelMapSync](#createpixelmapsync)

