# createAVRecorder

## Modules to Import

```TypeScript
import { media } from 'kits/@kit.MediaKit';
```

## createAVRecorder

```TypeScript
function createAVRecorder(callback: AsyncCallback<AVRecorder>): void
```

创建音视频录制实例。使用callback异步回调。

> **说明：**
> 
> 应用可创建多个音视频录制实例，但由于设备共用音频通路，一个设备仅能有一个实例进行音频录制。创建第二个实例录制音频时，将会因为音频通路冲突导致创建失败。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-media-function createAVRecorder(callback: AsyncCallback<AVRecorder>): void--><!--Device-media-function createAVRecorder(callback: AsyncCallback<AVRecorder>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;AVRecorder&gt; | Yes | 回调函数，返回AVRecorder实例，可用于录制音视频媒体。失败时返回null。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 5400101 | No memory. Return by callback. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
let avRecorder: media.AVRecorder;

media.createAVRecorder((error: BusinessError, recorder: media.AVRecorder) => {
  if (recorder) {
    avRecorder = recorder;
    console.info('Succeeded in creating AVRecorder');
  } else {
    console.error(`Failed to create AVRecorder, error message:${error.message}`);
  }
});
```


## createAVRecorder

```TypeScript
function createAVRecorder(callback: AsyncCallback<AVRecorder | undefined>): void
```

创建音视频录制实例。使用callback异步回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-media-function createAVRecorder(callback: AsyncCallback<AVRecorder | undefined>): void--><!--Device-media-function createAVRecorder(callback: AsyncCallback<AVRecorder | undefined>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;AVRecorder \| undefined&gt; | Yes | 回调函数，返回AVRecorder实例，可用于录制音视频媒体。失败时返回null。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 5400101 | No memory. Return by callback. |


## createAVRecorder

```TypeScript
function createAVRecorder(): Promise<AVRecorder>
```

创建音视频录制实例。使用Promise异步回调。

> **说明：**
> 
> 应用可创建多个音视频录制实例，但由于设备共用音频通路，一个设备仅能有一个实例进行音频录制。创建第二个实例录制音频时，将会因为音频通路冲突导致创建失败。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-media-function createAVRecorder(): Promise<AVRecorder>--><!--Device-media-function createAVRecorder(): Promise<AVRecorder>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;AVRecorder&gt; | Promise对象，返回AVRecorder实例，可用于录制音视频媒体。失败时返回null。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 5400101 | No memory. Return by promise. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
let avRecorder: media.AVRecorder;
media.createAVRecorder().then((recorder: media.AVRecorder) => {
  if (recorder) {
    avRecorder = recorder;
    console.info('Succeeded in creating AVRecorder');
  } else {
    console.error('Failed to create AVRecorder');
  }
}).catch((error: BusinessError) => {
  console.error(`Failed to create AVRecorder, error message:${error.message}`);
});
```


## createAVRecorder

```TypeScript
function createAVRecorder(): Promise<AVRecorder | undefined>
```

创建音视频录制实例。使用Promise异步回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-media-function createAVRecorder(): Promise<AVRecorder | undefined>--><!--Device-media-function createAVRecorder(): Promise<AVRecorder | undefined>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;AVRecorder \| undefined&gt; | Promise对象，返回AVRecorder实例，可用于录制音视频媒体。失败时返回null。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 5400101 | No memory. Return by promise. |

