# createAVRecorder

## Modules to Import

```TypeScript
import { media } from 'kits/@kit.MediaKit';
```

## createAVRecorder

```TypeScript
function createAVRecorder(callback: AsyncCallback<AVRecorder>): void
```

Creates an AVRecorder instance. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> An application can create multiple AVRecorder instances. However, because the device shares a common audio
> channel, only one instance can record audio at a time. Any attempt to create the second instance for audio
> recording fails due to audio channel conflicts.

**Since:** 9

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AVRecorder](arkts-media-media-avrecorder-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [5400101](../errorcode-media.md#5400101-memory-allocation-failed) |


## createAVRecorder

```TypeScript
function createAVRecorder(): Promise<AVRecorder>
```

Creates an AVRecorder instance. This API uses a promise to return the result.

> **NOTE：**&gt;
> An application can create multiple AVRecorder instances. However, because the device shares a common audio
> channel, only one instance can record audio at a time. Any attempt to create the second instance for audio
> recording fails due to audio channel conflicts.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[AVRecorder](arkts-media-media-avrecorder-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [5400101](../errorcode-media.md#5400101-memory-allocation-failed) |
