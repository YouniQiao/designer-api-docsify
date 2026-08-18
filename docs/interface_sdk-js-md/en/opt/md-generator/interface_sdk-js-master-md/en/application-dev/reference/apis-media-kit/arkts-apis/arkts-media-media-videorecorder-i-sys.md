# VideoRecorder (System API)

The maintenance of this interface has been stopped since version api 9. Please use AVRecorder. Manages and record video. Before calling an VideoRecorder method, you must use createVideoRecorder() to create an VideoRecorder instance.

**Since:** 23

<!--Device-media-interface VideoRecorder--><!--Device-media-interface VideoRecorder-End-->

**System capability:** SystemCapability.Multimedia.Media.VideoRecorder

**System API:** This is a system API.

## Modules to Import

```TypeScript
```

## getInputSurface

```TypeScript
getInputSurface(callback: AsyncCallback<string>): void
```

get input surface.it must be called between prepare completed and start.

**Since:** 9

<!--Device-VideoRecorder-getInputSurface(callback: AsyncCallback<string>): void--><!--Device-VideoRecorder-getInputSurface(callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.VideoRecorder

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) |
| [5400103](../errorcode-media.md#5400103-io-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [5400105](../errorcode-media.md#5400105-play-service-dead) |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// asyncallback.
let surfaceID: string; // Surface ID passed to the external system.
videoRecorder.getInputSurface((err: BusinessError, surfaceId: string) => {
  if (err == null) {
    console.info('getInputSurface success');
    surfaceID = surfaceId;
  } else {
    console.error('getInputSurface failed and error is ' + err.message);
  }
});
```

## getInputSurface

```TypeScript
getInputSurface(callback: AsyncCallback<string | undefined>): void
```

get input surface.it must be called between prepare completed and start.

**Since:** 23

<!--Device-VideoRecorder-getInputSurface(callback: AsyncCallback<string | undefined>): void--><!--Device-VideoRecorder-getInputSurface(callback: AsyncCallback<string | undefined>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.VideoRecorder

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string \| undefined & gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) |
| [5400103](../errorcode-media.md#5400103-io-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [5400105](../errorcode-media.md#5400105-play-service-dead) |

## getInputSurface

```TypeScript
getInputSurface(): Promise<string>
```

get input surface. it must be called between prepare completed and start.

**Since:** 9

<!--Device-VideoRecorder-getInputSurface(): Promise<string>--><!--Device-VideoRecorder-getInputSurface(): Promise<string>-End-->

**System capability:** SystemCapability.Multimedia.Media.VideoRecorder

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) |
| [5400103](../errorcode-media.md#5400103-io-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [5400105](../errorcode-media.md#5400105-play-service-dead) |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// promise.
let surfaceID: string; // Surface ID passed to the external system.
videoRecorder.getInputSurface().then((surfaceId: string) => {
  console.info('getInputSurface success');
  surfaceID = surfaceId;
}).catch((err: BusinessError) => {
  console.error('getInputSurface failed and catch error is ' + err.message);
});
```

## getInputSurface

```TypeScript
getInputSurface(): Promise<string | undefined>
```

get input surface. it must be called between prepare completed and start.

**Since:** 23

<!--Device-VideoRecorder-getInputSurface(): Promise<string | undefined>--><!--Device-VideoRecorder-getInputSurface(): Promise<string | undefined>-End-->

**System capability:** SystemCapability.Multimedia.Media.VideoRecorder

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string \ | undefined & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) |
| [5400103](../errorcode-media.md#5400103-io-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [5400105](../errorcode-media.md#5400105-play-service-dead) |

## onError

```TypeScript
onError(callback: ErrorCallback): void
```

Listens for video recording error events.

**Since:** 23

<!--Device-VideoRecorder-onError(callback: ErrorCallback): void--><!--Device-VideoRecorder-onError(callback: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.Media.VideoRecorder

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [5400103](../errorcode-media.md#5400103-io-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [5400105](../errorcode-media.md#5400105-play-service-dead) |

## on_error

```TypeScript
on(type: 'error', callback: ErrorCallback): void
```

Listens for video recording error events.

**Since:** 9

<!--Device-VideoRecorder-on(type: 'error', callback: ErrorCallback): void--><!--Device-VideoRecorder-on(type: 'error', callback: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.Media.VideoRecorder

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'error' | Yes |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [5400103](../errorcode-media.md#5400103-io-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [5400105](../errorcode-media.md#5400105-play-service-dead) |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// This event is reported when an error occurs during the retrieval of videoRecordState.
videoRecorder.on('error', (error: BusinessError) => { // Set the 'error' event callback.
  console.error(`audio error called, error: ${error}`);
})
```

## pause

```TypeScript
pause(callback: AsyncCallback<void>): void
```

Pauses video recording.

**Since:** 23

<!--Device-VideoRecorder-pause(callback: AsyncCallback<void>): void--><!--Device-VideoRecorder-pause(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.VideoRecorder

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) |
| [5400103](../errorcode-media.md#5400103-io-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [5400105](../errorcode-media.md#5400105-play-service-dead) |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// asyncallback.
videoRecorder.pause((err: BusinessError) => {
  if (err == null) {
    console.info('pause videorecorder success');
  } else {
    console.error('pause videorecorder failed and error is ' + err.message);
  }
});
```

## pause

```TypeScript
pause(): Promise<void>
```

Pauses video recording.

**Since:** 23

<!--Device-VideoRecorder-pause(): Promise<void>--><!--Device-VideoRecorder-pause(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.VideoRecorder

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) |
| [5400103](../errorcode-media.md#5400103-io-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [5400105](../errorcode-media.md#5400105-play-service-dead) |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// promise.
videoRecorder.pause().then(() => {
  console.info('pause videorecorder success');
}).catch((err: BusinessError) => {
  console.error('pause videorecorder failed and catch error is ' + err.message);
});
```

## prepare

```TypeScript
prepare(config: VideoRecorderConfig, callback: AsyncCallback<void>): void
```

Prepares for recording.

**Since:** 23

**Required permissions:** ohos.permission.MICROPHONE

<!--Device-VideoRecorder-prepare(config: VideoRecorderConfig, callback: AsyncCallback<void>): void--><!--Device-VideoRecorder-prepare(config: VideoRecorderConfig, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.VideoRecorder

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| config | [VideoRecorderConfig](arkts-media-media-videorecorderconfig-i-sys.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [5400105](../errorcode-media.md#5400105-play-service-dead) |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// Configure the parameters based on those supported by the hardware device.
let videoProfile: media.VideoRecorderProfile = {
  audioBitrate : 48000,
  audioChannels : 2,
  audioCodec : media.CodecMimeType.AUDIO_AAC,
  audioSampleRate : 48000,
  fileFormat : media.ContainerFormatType.CFT_MPEG_4,
  videoBitrate : 2000000,
  videoCodec : media.CodecMimeType.VIDEO_AVC,
  videoFrameWidth : 640,
  videoFrameHeight : 480,
  videoFrameRate : 30
}

let videoConfig: media.VideoRecorderConfig = {
  audioSourceType : media.AudioSourceType.AUDIO_SOURCE_TYPE_MIC,
  videoSourceType : media.VideoSourceType.VIDEO_SOURCE_TYPE_SURFACE_YUV,
  profile : videoProfile,
  url : 'fd://xx', // The file must be created by the caller and granted with proper permissions.
  rotation : 0,
  location : { latitude : 30, longitude : 130 }
}

// asyncallback.
videoRecorder.prepare(videoConfig, (err: BusinessError) => {
  if (err == null) {
    console.info('prepare success');
  } else {
    console.error('prepare failed and error is ' + err.message);
  }
})
```

## prepare

```TypeScript
prepare(config: VideoRecorderConfig): Promise<void>
```

Prepares for recording.

**Since:** 23

**Required permissions:** ohos.permission.MICROPHONE

<!--Device-VideoRecorder-prepare(config: VideoRecorderConfig): Promise<void>--><!--Device-VideoRecorder-prepare(config: VideoRecorderConfig): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.VideoRecorder

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| config | [VideoRecorderConfig](arkts-media-media-videorecorderconfig-i-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [5400105](../errorcode-media.md#5400105-play-service-dead) |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// Configure the parameters based on those supported by the hardware device.
let videoProfile: media.VideoRecorderProfile = {
  audioBitrate : 48000,
  audioChannels : 2,
  audioCodec : media.CodecMimeType.AUDIO_AAC,
  audioSampleRate : 48000,
  fileFormat : media.ContainerFormatType.CFT_MPEG_4,
  videoBitrate : 2000000,
  videoCodec : media.CodecMimeType.VIDEO_AVC,
  videoFrameWidth : 640,
  videoFrameHeight : 480,
  videoFrameRate : 30
}

let videoConfig: media.VideoRecorderConfig = {
  audioSourceType : media.AudioSourceType.AUDIO_SOURCE_TYPE_MIC,
  videoSourceType : media.VideoSourceType.VIDEO_SOURCE_TYPE_SURFACE_YUV,
  profile : videoProfile,
  url : 'fd://xx', // The file must be created by the caller and granted with proper permissions.
  rotation : 0,
  location : { latitude : 30, longitude : 130 }
}

// promise.
videoRecorder.prepare(videoConfig).then(() => {
  console.info('prepare success');
}).catch((err: BusinessError) => {
  console.error('prepare failed and catch error is ' + err.message);
});
```

## release

```TypeScript
release(callback: AsyncCallback<void>): void
```

Releases resources used for video recording.

**Since:** 23

<!--Device-VideoRecorder-release(callback: AsyncCallback<void>): void--><!--Device-VideoRecorder-release(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.VideoRecorder

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [5400105](../errorcode-media.md#5400105-play-service-dead) |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// asyncallback.
videoRecorder.release((err: BusinessError) => {
  if (err == null) {
    console.info('release videorecorder success');
  } else {
    console.error('release videorecorder failed and error is ' + err.message);
  }
});
```

## release

```TypeScript
release(): Promise<void>
```

Releases resources used for video recording.

**Since:** 23

<!--Device-VideoRecorder-release(): Promise<void>--><!--Device-VideoRecorder-release(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.VideoRecorder

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [5400105](../errorcode-media.md#5400105-play-service-dead) |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// promise.
videoRecorder.release().then(() => {
  console.info('release videorecorder success');
}).catch((err: BusinessError) => {
  console.error('release videorecorder failed and catch error is ' + err.message);
});
```

## reset

```TypeScript
reset(callback: AsyncCallback<void>): void
```

Resets video recording. Before resetting video recording, you must call stop() to stop recording. After video recording is reset, you must call prepare() to set the recording configurations for another recording.

**Since:** 23

<!--Device-VideoRecorder-reset(callback: AsyncCallback<void>): void--><!--Device-VideoRecorder-reset(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.VideoRecorder

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [5400103](../errorcode-media.md#5400103-io-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [5400105](../errorcode-media.md#5400105-play-service-dead) |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// asyncallback.
videoRecorder.reset((err: BusinessError) => {
  if (err == null) {
    console.info('reset videorecorder success');
  } else {
    console.error('reset videorecorder failed and error is ' + err.message);
  }
});
```

## reset

```TypeScript
reset(): Promise<void>
```

Resets video recording. Before resetting video recording, you must call stop() to stop recording. After video recording is reset, you must call prepare() to set the recording configurations for another recording.

**Since:** 23

<!--Device-VideoRecorder-reset(): Promise<void>--><!--Device-VideoRecorder-reset(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.VideoRecorder

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [5400103](../errorcode-media.md#5400103-io-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [5400105](../errorcode-media.md#5400105-play-service-dead) |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// promise.
videoRecorder.reset().then(() => {
  console.info('reset videorecorder success');
}).catch((err: BusinessError) => {
  console.error('reset videorecorder failed and catch error is ' + err.message);
});
```

## resume

```TypeScript
resume(callback: AsyncCallback<void>): void
```

Resumes video recording.

**Since:** 23

<!--Device-VideoRecorder-resume(callback: AsyncCallback<void>): void--><!--Device-VideoRecorder-resume(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.VideoRecorder

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) |
| [5400103](../errorcode-media.md#5400103-io-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [5400105](../errorcode-media.md#5400105-play-service-dead) |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// asyncallback.
videoRecorder.resume((err: BusinessError) => {
  if (err == null) {
    console.info('resume videorecorder success');
  } else {
    console.error('resume videorecorder failed and error is ' + err.message);
  }
});
```

## resume

```TypeScript
resume(): Promise<void>
```

Resumes video recording.

**Since:** 23

<!--Device-VideoRecorder-resume(): Promise<void>--><!--Device-VideoRecorder-resume(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.VideoRecorder

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) |
| [5400103](../errorcode-media.md#5400103-io-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [5400105](../errorcode-media.md#5400105-play-service-dead) |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// promise.
videoRecorder.resume().then(() => {
  console.info('resume videorecorder success');
}).catch((err: BusinessError) => {
  console.error('resume videorecorder failed and catch error is ' + err.message);
});
```

## start

```TypeScript
start(callback: AsyncCallback<void>): void
```

Starts video recording.

**Since:** 23

<!--Device-VideoRecorder-start(callback: AsyncCallback<void>): void--><!--Device-VideoRecorder-start(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.VideoRecorder

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) |
| [5400103](../errorcode-media.md#5400103-io-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [5400105](../errorcode-media.md#5400105-play-service-dead) |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// asyncallback.
videoRecorder.start((err: BusinessError) => {
  if (err == null) {
    console.info('start videorecorder success');
  } else {
    console.error('start videorecorder failed and error is ' + err.message);
  }
});
```

## start

```TypeScript
start(): Promise<void>
```

Starts video recording.

**Since:** 23

<!--Device-VideoRecorder-start(): Promise<void>--><!--Device-VideoRecorder-start(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.VideoRecorder

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) |
| [5400103](../errorcode-media.md#5400103-io-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [5400105](../errorcode-media.md#5400105-play-service-dead) |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// promise.
videoRecorder.start().then(() => {
  console.info('start videorecorder success');
}).catch((err: BusinessError) => {
  console.error('start videorecorder failed and catch error is ' + err.message);
});
```

## stop

```TypeScript
stop(callback: AsyncCallback<void>): void
```

Stops video recording.

**Since:** 23

<!--Device-VideoRecorder-stop(callback: AsyncCallback<void>): void--><!--Device-VideoRecorder-stop(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.VideoRecorder

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) |
| [5400103](../errorcode-media.md#5400103-io-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [5400105](../errorcode-media.md#5400105-play-service-dead) |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// asyncallback.
videoRecorder.stop((err: BusinessError) => {
  if (err == null) {
    console.info('stop videorecorder success');
  } else {
    console.error('stop videorecorder failed and error is ' + err.message);
  }
});
```

## stop

```TypeScript
stop(): Promise<void>
```

Stops video recording.

**Since:** 23

<!--Device-VideoRecorder-stop(): Promise<void>--><!--Device-VideoRecorder-stop(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.VideoRecorder

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) |
| [5400103](../errorcode-media.md#5400103-io-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [5400105](../errorcode-media.md#5400105-play-service-dead) |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// promise.
videoRecorder.stop().then(() => {
  console.info('stop videorecorder success');
}).catch((err: BusinessError) => {
  console.error('stop videorecorder failed and catch error is ' + err.message);
});
```

## state

```TypeScript
readonly state: VideoRecordState
```

video recorder state.

**Type:** [VideoRecordState](arkts-media-media-videorecordstate-t-sys.md)

**Since:** 23

<!--Device-VideoRecorder-readonly state: VideoRecordState--><!--Device-VideoRecorder-readonly state: VideoRecordState-End-->

**System capability:** SystemCapability.Multimedia.Media.VideoRecorder

**System API:** This is a system API.
