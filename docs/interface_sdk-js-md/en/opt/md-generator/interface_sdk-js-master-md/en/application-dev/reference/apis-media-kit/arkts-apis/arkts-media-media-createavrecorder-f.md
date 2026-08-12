# createAVRecorder

## Modules to Import

```TypeScript
import { media } from '@kit.MediaKit';
```

## createAVRecorder

```TypeScript
function createAVRecorder(callback: AsyncCallback<AVRecorder>): void
```

Creates an AVRecorder instance. This API uses an asynchronous callback to return the result.

> **NOTE：**
> 
> An application can create multiple AVRecorder instances. However, because the device shares a common audio
> channel, only one instance can record audio at a time. Any attempt to create the second instance for audio
> recording fails due to audio channel conflicts.

**Since:** 9

<!--Device-media-function createAVRecorder(callback: AsyncCallback<AVRecorder>): void--><!--Device-media-function createAVRecorder(callback: AsyncCallback<AVRecorder>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AVRecorder](arkts-media-media-avrecorder-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [5400101](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400101-memory-allocation-failed) |

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
function createAVRecorder(): Promise<AVRecorder>
```

Creates an AVRecorder instance. This API uses a promise to return the result.

> **NOTE：**
> 
> An application can create multiple AVRecorder instances. However, because the device shares a common audio
> channel, only one instance can record audio at a time. Any attempt to create the second instance for audio
> recording fails due to audio channel conflicts.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-media-function createAVRecorder(): Promise<AVRecorder>--><!--Device-media-function createAVRecorder(): Promise<AVRecorder>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[AVRecorder](arkts-media-media-avrecorder-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [5400101](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400101-memory-allocation-failed) |

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
