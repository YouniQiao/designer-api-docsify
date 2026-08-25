# createPixelMap

## 导入模块

```TypeScript
import { image } from 'kits/@kit.ImageKit';
```

## createPixelMap

```TypeScript
function createPixelMap(colors: ArrayBuffer, options: InitializationOptions, callback: AsyncCallback<PixelMap>): void
```

Create pixelmap by data buffer.Starting from API 26.0.0, it is recommended to use [createPixelMapFromPixels](arkts-image-image-createpixelmapfrompixels-f.md) instead for better exception handling capabilities.

**起始版本：** 10

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| colors | ArrayBuffer | 是 |
| options | [InitializationOptions](arkts-image-image-initializationoptions-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;PixelMap&gt; | 是 |


## createPixelMap

```TypeScript
function createPixelMap(colors: ArrayBuffer, options: InitializationOptions): Promise<PixelMap>
```

Create pixelmap by data buffer.Starting from API 26.0.0, it is recommended to use [createPixelMapFromPixels](arkts-image-image-createpixelmapfrompixels-f.md) instead for better exception handling capabilities.

**起始版本：** 10

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| colors | ArrayBuffer | 是 |
| options | [InitializationOptions](arkts-image-image-initializationoptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;PixelMap & gt; |
