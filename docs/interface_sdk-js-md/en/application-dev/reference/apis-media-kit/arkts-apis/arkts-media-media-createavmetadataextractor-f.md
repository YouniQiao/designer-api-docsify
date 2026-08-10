# createAVMetadataExtractor

## Modules to Import

```TypeScript
import { media } from 'kits/@kit.MediaKit';
```

## createAVMetadataExtractor

```TypeScript
function createAVMetadataExtractor(): Promise<AVMetadataExtractor>
```

创建AVMetadataExtractor实例。使用Promise异步回调。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

<!--Device-media-function createAVMetadataExtractor(): Promise<AVMetadataExtractor>--><!--Device-media-function createAVMetadataExtractor(): Promise<AVMetadataExtractor>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVMetadataExtractor

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;AVMetadataExtractor&gt; | Promise对象。异步返回元数据获取类对象（AVMetadataExtractor）。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 5400101 | No memory. Returned by promise. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let avMetadataExtractor: media.AVMetadataExtractor;
media.createAVMetadataExtractor().then((extractor: media.AVMetadataExtractor) => {
  if (extractor) {
    avMetadataExtractor = extractor;
    console.info('Succeeded in creating AVMetadataExtractor');
  } else {
    console.error(`Failed to create AVMetadataExtractor`);
  }
}).catch((error: BusinessError) => {
  console.error(`Failed to create AVMetadataExtractor, error message:${error.message}`);
});
```


## createAVMetadataExtractor

```TypeScript
function createAVMetadataExtractor(): Promise<AVMetadataExtractor | undefined>
```

Creates an **AVMetadataExtractor** instance. This API uses a promise to return the result.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-media-function createAVMetadataExtractor(): Promise<AVMetadataExtractor | undefined>--><!--Device-media-function createAVMetadataExtractor(): Promise<AVMetadataExtractor | undefined>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVMetadataExtractor

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;AVMetadataExtractor \| undefined&gt; | A Promise instance used to return AVMetadataExtractor instance if the operation is successful; returns null otherwise. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 5400101 | No memory. Returned by promise. |


## createAVMetadataExtractor

```TypeScript
function createAVMetadataExtractor(callback: AsyncCallback<AVMetadataExtractor>): void
```

创建AVMetadataExtractor实例。使用callback异步回调。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

<!--Device-media-function createAVMetadataExtractor(callback: AsyncCallback<AVMetadataExtractor>): void--><!--Device-media-function createAVMetadataExtractor(callback: AsyncCallback<AVMetadataExtractor>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVMetadataExtractor

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;AVMetadataExtractor&gt; | Yes | 回调函数。当创建AVMetadataExtractor实例成功，err为undefined，data为获取到的 AVMetadataExtractor实例，否则为错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 5400101 | No memory. Returned by callback. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let avMetadataExtractor: media.AVMetadataExtractor;
media.createAVMetadataExtractor((error: BusinessError, extractor: media.AVMetadataExtractor) => {
  if (extractor) {
    avMetadataExtractor = extractor;
    console.info('Succeeded in creating AVMetadataExtractor');
  } else {
    console.error(`Failed to create AVMetadataExtractor, error message:${error.message}`);
  }
});
```


## createAVMetadataExtractor

```TypeScript
function createAVMetadataExtractor(callback: AsyncCallback<AVMetadataExtractor | undefined>): void
```

Creates an **AVMetadataExtractor** instance. This API uses an asynchronous callback to return the result.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-media-function createAVMetadataExtractor(callback: AsyncCallback<AVMetadataExtractor | undefined>): void--><!--Device-media-function createAVMetadataExtractor(callback: AsyncCallback<AVMetadataExtractor | undefined>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVMetadataExtractor

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;AVMetadataExtractor \| undefined&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the **AVMetadataExtractor** instance created; otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 5400101 | No memory. Returned by callback. |

