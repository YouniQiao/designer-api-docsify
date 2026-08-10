# createVideoRecorder (System API)

## Modules to Import

```TypeScript
import { media } from 'kits/@kit.MediaKit';
```

## createVideoRecorder

```TypeScript
function createVideoRecorder(callback: AsyncCallback<VideoRecorder>): void
```

该接口自API version 9起停止维护，建议使用AVRecorder。创建视频录制实例。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-media-function createVideoRecorder(callback: AsyncCallback<VideoRecorder>): void--><!--Device-media-function createVideoRecorder(callback: AsyncCallback<VideoRecorder>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.VideoRecorder

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;VideoRecorder&gt; | Yes | 回调函数，返回VideoRecorder实例，失败时返回null。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 5400101 | No memory. Return by callback. |
| 202 | Not System App.<br>**Applicable version:** 12 and later |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let videoRecorder: media.VideoRecorder;
media.createVideoRecorder((error: BusinessError, video: media.VideoRecorder) => {
  if (video != null) {
    videoRecorder = video;
    console.info('video createVideoRecorder success');
  } else {
    console.error(`video createVideoRecorder fail, error message:${error.message}`);
  }
});
```


## createVideoRecorder

```TypeScript
function createVideoRecorder(callback: AsyncCallback<VideoRecorder | undefined>): void
```

该接口自API version 9起停止维护，建议使用AVRecorder。创建视频录制实例。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-media-function createVideoRecorder(callback: AsyncCallback<VideoRecorder | undefined>): void--><!--Device-media-function createVideoRecorder(callback: AsyncCallback<VideoRecorder | undefined>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.VideoRecorder

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;VideoRecorder \| undefined&gt; | Yes | 回调函数，返回VideoRecorder实例，失败时返回null。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 5400101 | No memory. Return by callback. |
| 202 | Not System App. |


## createVideoRecorder

```TypeScript
function createVideoRecorder(): Promise<VideoRecorder>
```

该接口自API version 9起停止维护，建议使用AVRecorder。创建视频录制实例。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-media-function createVideoRecorder(): Promise<VideoRecorder>--><!--Device-media-function createVideoRecorder(): Promise<VideoRecorder>-End-->

**System capability:** SystemCapability.Multimedia.Media.VideoRecorder

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;VideoRecorder&gt; | Promise对象，返回VideoRecorder实例，失败时返回null。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 5400101 | No memory. Return by promise. |
| 202 | Not System App.<br>**Applicable version:** 12 and later |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let videoRecorder: media.VideoRecorder;
media.createVideoRecorder().then((video: media.VideoRecorder) => {
  if (video != null) {
    videoRecorder = video;
    console.info('video createVideoRecorder success');
  } else {
    console.error('video createVideoRecorder fail');
  }
}).catch((error: BusinessError) => {
  console.error(`video catchCallback, error message:${error.message}`);
});
```


## createVideoRecorder

```TypeScript
function createVideoRecorder(): Promise<VideoRecorder | undefined>
```

该接口自API version 9起停止维护，建议使用AVRecorder。创建视频录制实例。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-media-function createVideoRecorder(): Promise<VideoRecorder | undefined>--><!--Device-media-function createVideoRecorder(): Promise<VideoRecorder | undefined>-End-->

**System capability:** SystemCapability.Multimedia.Media.VideoRecorder

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;VideoRecorder \| undefined&gt; | Promise对象，返回VideoRecorder实例，失败时返回null。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 5400101 | No memory. Return by promise. |
| 202 | Not System App. |

