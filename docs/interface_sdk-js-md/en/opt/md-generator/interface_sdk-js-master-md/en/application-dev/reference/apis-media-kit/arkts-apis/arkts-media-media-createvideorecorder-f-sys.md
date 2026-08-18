# createVideoRecorder (System API)

## Modules to Import

```TypeScript
```

## createVideoRecorder

```TypeScript
function createVideoRecorder(callback: AsyncCallback<VideoRecorder>): void
```

The maintenance of this interface has been stopped since version api 9. Please use AVRecorder Creates an VideoRecorder instance.

**Since:** 9

<!--Device-media-function createVideoRecorder(callback: AsyncCallback<VideoRecorder>): void--><!--Device-media-function createVideoRecorder(callback: AsyncCallback<VideoRecorder>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.VideoRecorder

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[VideoRecorder](arkts-media-media-videorecorder-i-sys.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [5400101](../errorcode-media.md#5400101-memory-allocation-failed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

**Examples**

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

The maintenance of this interface has been stopped since version api 9. Please use AVRecorder Creates an VideoRecorder instance.

**Since:** 23

<!--Device-media-function createVideoRecorder(callback: AsyncCallback<VideoRecorder | undefined>): void--><!--Device-media-function createVideoRecorder(callback: AsyncCallback<VideoRecorder | undefined>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.VideoRecorder

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[VideoRecorder](arkts-media-media-videorecorder-i-sys.md) \| undefined & gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [5400101](../errorcode-media.md#5400101-memory-allocation-failed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |


## createVideoRecorder

```TypeScript
function createVideoRecorder(): Promise<VideoRecorder>
```

The maintenance of this interface has been stopped since version api 9. Please use AVRecorder Creates an VideoRecorder instance.

**Since:** 9

<!--Device-media-function createVideoRecorder(): Promise<VideoRecorder>--><!--Device-media-function createVideoRecorder(): Promise<VideoRecorder>-End-->

**System capability:** SystemCapability.Multimedia.Media.VideoRecorder

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[VideoRecorder](arkts-media-media-videorecorder-i-sys.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [5400101](../errorcode-media.md#5400101-memory-allocation-failed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

**Examples**

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

The maintenance of this interface has been stopped since version api 9. Please use AVRecorder Creates an VideoRecorder instance.

**Since:** 23

<!--Device-media-function createVideoRecorder(): Promise<VideoRecorder | undefined>--><!--Device-media-function createVideoRecorder(): Promise<VideoRecorder | undefined>-End-->

**System capability:** SystemCapability.Multimedia.Media.VideoRecorder

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[VideoRecorder](arkts-media-media-videorecorder-i-sys.md) \| undefined & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [5400101](../errorcode-media.md#5400101-memory-allocation-failed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
