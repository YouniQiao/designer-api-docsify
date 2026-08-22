# createPixelMapUsingAllocator

## 导入模块

```TypeScript
import { image } from '@kit.ImageKit';
```

## createPixelMapUsingAllocator

```TypeScript
function createPixelMapUsingAllocator(colors: ArrayBuffer, param: InitializationOptions,
    allocatorType?: AllocatorType): Promise<PixelMap>
```

Create pixelmap by data buffer based on opts, the memory type used by the PixelMap can be specified by allocatorType. By default, the system selects the memory type based on the image type, image size, platform capability, etc. When processing the PixelMap returned by this interface, please always consider the impact of stride.

**起始版本：** 23

<!--Device-image-function createPixelMapUsingAllocator(colors: ArrayBuffer, param: InitializationOptions,    allocatorType?: AllocatorType): Promise<PixelMap>--><!--Device-image-function createPixelMapUsingAllocator(colors: ArrayBuffer, param: InitializationOptions,    allocatorType?: AllocatorType): Promise<PixelMap>-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| colors | ArrayBuffer | 是 | The image color buffer. |
| param | [InitializationOptions](arkts-image-image-initializationoptions-i.md) | 是 | Initialization options for pixelmap. |
| allocatorType | [AllocatorType](arkts-image-image-allocatortype-e.md) | 否 | Indicate which memory type will be used by the returned PixelMap. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;PixelMap&gt; | A Promise instance used to return the PixelMap object. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [7600201](../errorcode-image.md#7600201-不支持的操作) | Unsupported operation. |
| [7600301](../errorcode-image.md#7600301-申请内存失败) | Memory alloc failed. |
| [7600302](../errorcode-image.md#7600302-内存拷贝失败) | Memory copy failed. |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function createPixelMapUsingAllocator() {
  const color: ArrayBuffer = new ArrayBuffer(96); // 96为需要创建的像素缓冲区大小，取值为：width * height * 4。
  let opts: image.InitializationOptions = {
    size: { height: 4, width: 6 },
    srcPixelFormat: image.PixelMapFormat.RGBA_8888, // 缓冲区中的源像素数据的像素格式。
    pixelFormat: image.PixelMapFormat.BGRA_8888, // 新创建的PixelMap的像素格式。
    editable: true
  };
  image.createPixelMapUsingAllocator(color, opts, image.AllocatorType.DMA).then((pixelMap: image.PixelMap) => {
    console.info('Succeeded in creating the PixelMap.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to create the PixelMap. Code: ${err.code}, message: ${err.message}`);
  });
}
```

ArkTS-Sta示例：

```TypeScript
function createPixelMapUsingAllocator() {
  const color: ArrayBuffer = new ArrayBuffer(96); // 96为需要创建的像素缓冲区大小，取值为：width * height * 4。
  let opts: image.InitializationOptions = {
    size: { height: 4, width: 6 },
    srcPixelFormat: image.PixelMapFormat.RGBA_8888, // 缓冲区中的源像素数据的像素格式。
    pixelFormat: image.PixelMapFormat.BGRA_8888, // 新创建的PixelMap的像素格式。
    editable: true
  };
  image.createPixelMapUsingAllocator(color, opts, image.AllocatorType.DMA).then((pixelMap: image.PixelMap) => {
    console.info('Succeeded in creating the PixelMap.');
  }).catch((err: Error) => {
    console.error(`Failed to create the PixelMap. Code: ${err.code}, message: ${err.message}`);
  });
}
```

ArkTS-Dyn示例：

```TypeScript
async function CreatePixelMapUsingAllocator(context : Context) {
  // 此处'test.jpg'仅作示例，请开发者自行替换，否则imageSource创建失败会导致后续无法正常执行。
  let filePath: string = context.filesDir + "/test.jpg";
  let imageSource = image.createImageSource(filePath);
  let decodingOptions: image.DecodingOptions = {
    editable: true,
    desiredSize: { width: 3072, height: 4096 },
    rotate: 10,
    desiredPixelFormat: image.PixelMapFormat.RGBA_8888,
    desiredRegion: { size: { width: 3072, height: 4096 }, x: 0, y: 0 },
    // 若解码接口同时传入了desiredSize参数与desiredRegion参数，需进一步传入cropAndScaleStrategy参数指定缩放与裁剪的先后顺序，推荐设置CROP_FIRST。
    cropAndScaleStrategy: image.CropAndScaleStrategy.CROP_FIRST,
    index: 0
  };
  let pixelmap = imageSource.createPixelMapUsingAllocator(decodingOptions, image.AllocatorType.AUTO);
  if (pixelmap != undefined) {
    console.info('Succeeded in creating pixelMap object.');
  } else {
    console.error('Failed to create pixelMap.');
  }
}
```

ArkTS-Sta示例：

```TypeScript
async function CreatePixelMapUsingAllocatorFunc(imageSource: image.ImageSource): Promise<void> {
   let decodeOpts: image.DecodingOptions = {
    sampleSize: 1,
    editable: true,
    desiredSize: { width: 198, height: 202 },
    rotate: 0,
    desiredPixelFormat: image.PixelMapFormat.RGBA_8888,
    index: 0,
  };
  try {
    let pixelMap = await imageSource.createPixelMapUsingAllocator(decodeOpts, image.AllocatorType.AUTO);
    console.info(0x00000, 'CreatePixelMapUsingAllocatorFunc', 'createPixelMapUsingAllocator success!');
  } catch (err) {
    console.error(0x00000, 'CreatePixelMapUsingAllocatorFunc', 'CreatePixelMapUsingAllocatorFunc failed: ' + err);
  }
}
```

