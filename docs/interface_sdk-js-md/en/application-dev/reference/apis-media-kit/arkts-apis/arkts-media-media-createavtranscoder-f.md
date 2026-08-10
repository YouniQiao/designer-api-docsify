# createAVTranscoder

## Modules to Import

```TypeScript
import { media } from 'kits/@kit.MediaKit';
```

## createAVTranscoder

```TypeScript
function createAVTranscoder(): Promise<AVTranscoder>
```

创建视频转码实例。使用Promise异步回调。

> **说明：**
> 
> 可创建的视频转码实例不能超过2个。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-media-function createAVTranscoder(): Promise<AVTranscoder>--><!--Device-media-function createAVTranscoder(): Promise<AVTranscoder>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVTranscoder

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;AVTranscoder&gt; | Promise对象。异步返回AVTranscoder实例，失败时返回null。可用于视频转码。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 5400101 | No memory. Return by promise. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let avTranscoder: media.AVTranscoder | undefined = undefined;
media.createAVTranscoder().then((transcoder: media.AVTranscoder) => {
  if (transcoder) {
    avTranscoder = transcoder;
    console.info('Succeeded in creating AVTranscoder');
  } else {
    console.error('Failed to create AVTranscoder');
  }
}).catch((error: BusinessError) => {
  console.error(`Failed to create AVTranscoder, error message:${error.message}`);
});
```


## createAVTranscoder

```TypeScript
function createAVTranscoder(): Promise<AVTranscoder | undefined>
```

Creates an **AVTranscoder** instance. This API uses a promise to return the result.

**NOTE：**

A maximum of 2 **AVTranscoder** instances can be created.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-media-function createAVTranscoder(): Promise<AVTranscoder | undefined>--><!--Device-media-function createAVTranscoder(): Promise<AVTranscoder | undefined>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVTranscoder

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;AVTranscoder \| undefined&gt; | Promise used to return the result. If the operation is successful, an **AVTranscoder** instance is returned; otherwise, **null** is returned. The instance can be used for video transcoding. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 5400101 | No memory. Return by promise. |

