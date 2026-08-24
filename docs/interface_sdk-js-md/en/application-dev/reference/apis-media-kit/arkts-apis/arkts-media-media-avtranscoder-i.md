# AVTranscoder

AVTranscoder is a transcoding management class. It provides APIs to transcode videos. Before calling any API in AVTranscoder, you must use [createAVTranscoder()](arkts-media-media-createavtranscoder-f.md) to create an AVTranscoder instance.For details about the AVTranscoder demo, see [Using AVTranscoder for Transcoding](../../../media/media/using-avtranscoder-for-transcodering.md).

**Since:** 23

<!--Device-media-interface AVTranscoder--><!--Device-media-interface AVTranscoder-End-->

**System capability:** SystemCapability.Multimedia.Media.AVTranscoder

## Modules to Import

```TypeScript
import { media } from '@kit.MediaKit';
```

## addWatermark

```TypeScript
addWatermark(watermark: image.PixelMap, config: WatermarkConfiguration): Promise<int>
```

add a watermark for the AVTranscoder. This API uses a promise to return the result. App can add up to 5 watermarks. This API can be called only before the prepared state.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVTranscoder-addWatermark(watermark: image.PixelMap, config: WatermarkConfiguration): Promise<int>--><!--Device-AVTranscoder-addWatermark(watermark: image.PixelMap, config: WatermarkConfiguration): Promise<int>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVTranscoder

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| watermark | image.PixelMap | Yes | : Watermark image. |
| config | [WatermarkConfiguration](arkts-media-media-watermarkconfiguration-i.md) | Yes | : Configuration of the watermark. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;int&gt; | Promise that returns the watermark id. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) | Operation not allowed. Return by promise. |
| [5400103](../errorcode-media.md#5400103-io-error) | IO error. Return by promise. |
| [5400105](../errorcode-media.md#5400105-play-service-dead) | Service died. Return by promise. |
| [5400108](../errorcode-media.md#5400108-parameter-value-out-of-range) | The parameter check failed, parameter value out of range. |

## cancel

```TypeScript
cancel(): Promise<void>
```

Cancels video transcoding. This API uses a promise to return the result.This API can be called only after the [prepare()](#prepare), [start()](#start), [pause()](#pause), or [resume()](#resume) API is called.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-AVTranscoder-cancel(): Promise<void>--><!--Device-AVTranscoder-cancel(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVTranscoder

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) | Operation not allowed. Return by promise. |
| [5400103](../errorcode-media.md#5400103-io-error) | IO error. Return by promise. |
| [5400105](../errorcode-media.md#5400105-play-service-dead) | Service died. Return by promise. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';

async function test() {
  // Create an AVTranscoder instance.
  let avTranscoder = await media.createAVTranscoder();
  avTranscoder.cancel().then(() => {
    console.info('cancel AVTranscoder success');
  }).catch((err: BusinessError) => {
    console.error('cancel AVTranscoder failed and catch error is ' + err.message);
  });
}
```

## off('complete')

```TypeScript
off(type:'complete', callback?: Callback<void>):void
```

Unsubscribes from the event indicating that transcoding is complete.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-AVTranscoder-off(type:'complete', callback?: Callback<void>):void--><!--Device-AVTranscoder-off(type:'complete', callback?: Callback<void>):void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVTranscoder

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'complete' | Yes | Event type, which is **'complete'** in this case. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | No | Callback that has been registered to listen for transcoding completion events. |

## off('error')

```TypeScript
off(type:'error', callback?: ErrorCallback):void
```

Unsubscribes from AVTranscoder errors. After the unsubscription, your application can no longer receive AVTranscoder errors.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-AVTranscoder-off(type:'error', callback?: ErrorCallback):void--><!--Device-AVTranscoder-off(type:'error', callback?: ErrorCallback):void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVTranscoder

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'error' | Yes | Event type, which is **'error'** in this case.<br>This event is triggered when an error occurs during transcoding. |
| callback | [ErrorCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | No | Callback that has been registered to listen for AVTranscoder errors. |

## off('progressUpdate')

```TypeScript
off(type:'progressUpdate', callback?: Callback<int>):void
```

Unsubscribes from transcoding progress updates.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-AVTranscoder-off(type:'progressUpdate', callback?: Callback<int>):void--><!--Device-AVTranscoder-off(type:'progressUpdate', callback?: Callback<int>):void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVTranscoder

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'progressUpdate' | Yes | Event type, which is **'progressUpdate'** in this case. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;int&gt; | No | Called that has been registered to listen for progress updates. You are advised to use the default value because only the last registered callback is retained in the current callback mechanism. |

## offComplete

```TypeScript
offComplete(callback?: Callback<void>):void
```

Unsubscribes from the event indicating that transcoding is complete. This event can be triggered by both user operations and the system.

**Since:** 23

<!--Device-AVTranscoder-offComplete(callback?: Callback<void>):void--><!--Device-AVTranscoder-offComplete(callback?: Callback<void>):void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVTranscoder

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | No | Callback that has been registered to listen for transcoding completion events. |

## offError

```TypeScript
offError(callback?: ErrorCallback):void
```

Unsubscribes from AVTranscoder errors. After the unsubscription, your application can no longer receive AVTranscoder errors. This event is triggered when an error occurs during transcoding.

**Since:** 23

<!--Device-AVTranscoder-offError(callback?: ErrorCallback):void--><!--Device-AVTranscoder-offError(callback?: ErrorCallback):void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVTranscoder

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [ErrorCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | No | Callback that has been registered to listen for AVTranscoder errors. |

## offProgressUpdate

```TypeScript
offProgressUpdate(callback?: Callback<int>):void
```

Unsubscribes from transcoding progress updates. This event can be triggered by both user operations and the system.

**Since:** 23

<!--Device-AVTranscoder-offProgressUpdate(callback?: Callback<int>):void--><!--Device-AVTranscoder-offProgressUpdate(callback?: Callback<int>):void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVTranscoder

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;int&gt; | No | Called that has been registered to listen for progress updates. You are advised to use the default value because only the last registered callback is retained in the current allback mechanism. |

## on('complete')

```TypeScript
on(type:'complete', callback: Callback<void>):void
```

Subscribes to the event indicating that transcoding is complete. An application can subscribe to only one transcoding progress update event. When the application initiates multiple subscriptions to this event, the last subscription is applied. This API uses an asynchronous callback to return the result.When this event is reported, the current transcoding operation is complete. You need to call [release()](#release) to exit the transcoding.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-AVTranscoder-on(type:'complete', callback: Callback<void>):void--><!--Device-AVTranscoder-on(type:'complete', callback: Callback<void>):void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVTranscoder

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'complete' | Yes | Event type, which is **'complete'** in this case. This event is triggered by the system during transcoding. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes | Callback used to return the event callback method. |

## on('error')

```TypeScript
on(type:'error', callback: ErrorCallback):void
```

Subscribes to AVTranscoder errors. If this event is reported, call [release()](#release) to exit the transcoding. This API uses an asynchronous callback to return the result.An application can subscribe to only one AVTranscoder error event. When the application initiates multiple subscriptions to this event, the last subscription is applied.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-AVTranscoder-on(type:'error', callback: ErrorCallback):void--><!--Device-AVTranscoder-on(type:'error', callback: ErrorCallback):void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVTranscoder

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'error' | Yes | Event type, which is **'error'** in this case.<br>This event is triggered when an error occurs during recording. |
| callback | [ErrorCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | Yes | Callback invoked when the event is triggered. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | The parameter check failed. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [5400101](../errorcode-media.md#5400101-memory-allocation-failed) | No memory. |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) | Operation not allowed. |
| [5400103](../errorcode-media.md#5400103-io-error) | I/O error. |
| [5400104](../errorcode-media.md#5400104-operation-timeout) | Time out. |
| [5400105](../errorcode-media.md#5400105-play-service-dead) | Service died. |
| [5400106](../errorcode-media.md#5400106-format-not-supported) | Unsupported format. |

## on('progressUpdate')

```TypeScript
on(type:'progressUpdate', callback: Callback<int>):void
```

Subscribes to transcoding progress updates. An application can subscribe to only one transcoding progress update event. When the application initiates multiple subscriptions to this event, the last subscription is applied. This API uses an asynchronous callback to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-AVTranscoder-on(type:'progressUpdate', callback: Callback<int>):void--><!--Device-AVTranscoder-on(type:'progressUpdate', callback: Callback<int>):void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVTranscoder

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'progressUpdate' | Yes | Event type, which is **'progressUpdate'** in this case. This event is triggered by the system during transcoding. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;int&gt; | Yes | Callback used to return the progress update event. The **number** parameter in the function indicates the current transcoding progress, in percentage. |

## onComplete

```TypeScript
onComplete(callback: Callback<void>):void
```

Subscribes to the event indicating that transcoding is complete. An application can subscribe to only one transcoding completion event. When the application initiates multiple subscriptions to this event, the last subscription is applied.When this event is reported, the current transcoding operation is complete. You need to call [release()](#release) to exit the transcoding.

**Since:** 23

<!--Device-AVTranscoder-onComplete(callback: Callback<void>):void--><!--Device-AVTranscoder-onComplete(callback: Callback<void>):void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVTranscoder

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes | Callback that has been registered to listen for transcoding completion events. |

## onError

```TypeScript
onError(callback: ErrorCallback):void
```

Subscribes to AVTranscoder errors. If this event is reported, call [release()](#release) to exit the transcoding.An application can subscribe to only one AVTranscoder error event. When the application initiates multiple subscriptions to this event, the last subscription is applied.

**Since:** 23

<!--Device-AVTranscoder-onError(callback: ErrorCallback):void--><!--Device-AVTranscoder-onError(callback: ErrorCallback):void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVTranscoder

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [ErrorCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | Yes | Callback invoked when the event is triggered. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | The parameter check failed. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [5400101](../errorcode-media.md#5400101-memory-allocation-failed) | No memory. |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) | Operation not allowed. |
| [5400103](../errorcode-media.md#5400103-io-error) | I/O error. |
| [5400104](../errorcode-media.md#5400104-operation-timeout) | Time out. |
| [5400105](../errorcode-media.md#5400105-play-service-dead) | Service died. |
| [5400106](../errorcode-media.md#5400106-format-not-supported) | Unsupported format. |

## onProgressUpdate

```TypeScript
onProgressUpdate(callback: Callback<int>):void
```

Subscribes to transcoding progress updates. An application can subscribe to only one transcoding progress update event. When the application initiates multiple subscriptions to this event, the last subscription is applied.

**Since:** 23

<!--Device-AVTranscoder-onProgressUpdate(callback: Callback<int>):void--><!--Device-AVTranscoder-onProgressUpdate(callback: Callback<int>):void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVTranscoder

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;int&gt; | Yes | Callback invoked when the event is triggered. **progress** is a number that indicates the current transcoding progress, in percentage. |

## pause

```TypeScript
pause(): Promise<void>
```

Pauses video transcoding. This API uses a promise to return the result.This API can be called only after the [start()](#start) API is called. You can call [resume()](#resume) to resume transcoding.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-AVTranscoder-pause(): Promise<void>--><!--Device-AVTranscoder-pause(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVTranscoder

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) | Operation not allowed. Return by promise. |
| [5400103](../errorcode-media.md#5400103-io-error) | IO error. Return by promise. |
| [5400105](../errorcode-media.md#5400105-play-service-dead) | Service died. Return by promise. |

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

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// promise.
videoRecorder.pause().then(() => {
  console.info('pause videorecorder success');
}).catch((err: BusinessError) => {
  console.error('pause videorecorder failed and catch error is ' + err.message);
});
```

```TypeScript
audioPlayer.on('pause', () => {    // Set the 'pause' event callback.
  console.info('audio pause called');
});
audioPlayer.pause();
```

```TypeScript
audioRecorder.on('pause', () => {    // Set the 'pause' event callback.
  console.info('audio recorder pause called');
});
audioRecorder.pause();
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function  test(){
  let avPlayer = await media.createAVPlayer();
  // Here is only an example. In real development, you must wait for the stateChange event to successfully trigger and reach the playing state before proceeding.
  avPlayer.pause((err: BusinessError) => {
    if (err) {
      console.error('Failed to pause,error message is :' + err.message);
    } else {
      console.info('Succeeded in pausing');
    }
  });
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function  test(){
  let avPlayer = await media.createAVPlayer();
  // Here is only an example. In real development, you must wait for the stateChange event to successfully trigger and reach the playing state before proceeding.
  avPlayer.pause().then(() => {
    console.info('Succeeded in pausing');
  }, (err: BusinessError) => {
    console.error('Failed to pause,error message is :' + err.message);
  });
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

avRecorder.pause((err: BusinessError) => {
  if (err) {
    console.error(`Failed to pause AVRecorder and error is: Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info('Succeeded in pausing');
  }
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

avRecorder.pause().then(() => {
  console.info('Succeeded in pausing');
}).catch((err: Error) => {
  let error: BusinessError = err as BusinessError;
  console.error(`Failed to pause AVRecorder and error is: Code: ${error.code}, message: ${error.message}`);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';

async function test() {
  // Create an AVTranscoder instance.
  let avTranscoder = await media.createAVTranscoder();
  avTranscoder.pause().then(() => {
    console.info('pause AVTranscoder success');
  }).catch((err: BusinessError) => {
    console.error('pause AVTranscoder failed and catch error is ' + err.message);
  });
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

videoPlayer.pause((err: BusinessError) => {
  if (err) {
    console.error('Failed to pause!');
  } else {
    console.info('Succeeded in pausing!');
  }
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

videoPlayer.pause().then(() => {
  console.info('Succeeded in pausing');
}).catch((error: BusinessError) => {
  console.error(`video catchCallback, error:${error}`);
});
```

## prepare

```TypeScript
prepare(config: AVTranscoderConfig): Promise<void>
```

Sets video transcoding parameters. This API uses a promise to return the result.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-AVTranscoder-prepare(config: AVTranscoderConfig): Promise<void>--><!--Device-AVTranscoder-prepare(config: AVTranscoderConfig): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVTranscoder

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| config | [AVTranscoderConfig](arkts-media-media-avtranscoderconfig-i.md) | Yes | Video transcoding parameters to set.<!--RP1--><!--RP1End--> |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) | Operation not allowed. Return by promise. |
| [5400103](../errorcode-media.md#5400103-io-error) | IO error. Return by promise. |
| [5400105](../errorcode-media.md#5400105-play-service-dead) | Service died. Return by promise. |
| [5400106](../errorcode-media.md#5400106-format-not-supported) | Unsupported format. Returned by promise. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | The parameter check failed. Return by promise.<br>**Applicable version:** 22 and later |

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

```TypeScript
let audioRecorderConfig: media.AudioRecorderConfig = {
  audioEncoder : media.AudioEncoder.AAC_LC,
  audioEncodeBitRate : 64000,
  audioSampleRate : 44100,
  numberOfChannels : 2,
  format : media.AudioOutputFormat.AAC_ADTS,
  uri : 'fd://1',       // The file must be created by the caller and granted with proper permissions.
  location : { latitude : 30, longitude : 130},
};
audioRecorder.on('prepare', () => {    // Set the 'prepare' event callback.
  console.info('prepare called');
});
audioRecorder.prepare(audioRecorderConfig);
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function  test(){
  let avPlayer = await media.createAVPlayer();
  // Here is only an example. In real development, you must wait for the stateChange event to successfully trigger and reach the initialized state before proceeding.
  avPlayer.prepare((err: BusinessError) => {
    if (err) {
      console.error('Failed to prepare,error message is :' + err.message);
    } else {
      console.info('Succeeded in preparing');
    }
  });
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function  test(){
  let avPlayer = await media.createAVPlayer();
  // Here is only an example. In real development, you must wait for the stateChange event to successfully trigger and reach the initialized state before proceeding.
  avPlayer.prepare().then(() => {
    console.info('Succeeded in preparing');
  }, (err: BusinessError) => {
    console.error('Failed to prepare,error message is :' + err.message);
  });
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// Configure the parameters based on those supported by the hardware device.
let avRecorderProfile: media.AVRecorderProfile = {
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
};
let videoMetaData: media.AVMetadata = {
  videoOrientation: '0' // The value can be 0, 90, 180, or 270. If any other value is used, prepare() reports an error.
};
let avRecorderConfig: media.AVRecorderConfig = {
  audioSourceType : media.AudioSourceType.AUDIO_SOURCE_TYPE_MIC,
  videoSourceType : media.VideoSourceType.VIDEO_SOURCE_TYPE_SURFACE_YUV,
  profile : avRecorderProfile,
  url : 'fd://', // Before passing an FD to this parameter, the file must be created by the caller and granted with the read and write permissions. Example value: fd://45.
  metadata: videoMetaData,
  location : { latitude : 30, longitude : 130 }
};

avRecorder.prepare(avRecorderConfig, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to prepare and error is: Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info('Succeeded in preparing');
  }
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// Configure the parameters based on those supported by the hardware device.
let avRecorderProfile: media.AVRecorderProfile = {
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
};
let videoMetaData: media.AVMetadata = {
  videoOrientation: '0' // The value can be 0, 90, 180, or 270. If any other value is used, prepare() reports an error.
};
let avRecorderConfig: media.AVRecorderConfig = {
  audioSourceType : media.AudioSourceType.AUDIO_SOURCE_TYPE_MIC,
  videoSourceType : media.VideoSourceType.VIDEO_SOURCE_TYPE_SURFACE_YUV,
  profile : avRecorderProfile,
  url : 'fd://',  // Before passing an FD to this parameter, the file must be created by the caller and granted with the read and write permissions. Example value: fd://45.
  metadata : videoMetaData,
  location : { latitude : 30, longitude : 130 }
};

avRecorder.prepare(avRecorderConfig).then(() => {
  console.info('Succeeded in preparing');
}).catch((err: Error) => {
  let error: BusinessError = err as BusinessError;
  console.error(`Failed to prepare and error is: Code: ${error.code}, message: ${error.message}`);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';

async function test() {
  // Create an AVTranscoder instance.
  let avTranscoder = await media.createAVTranscoder();
  // Configure the parameters based on those supported by the hardware device.
  let avTranscoderConfig: media.AVTranscoderConfig = {
    audioBitrate : 200000,
    audioCodec : media.CodecMimeType.AUDIO_AAC,
    fileFormat : media.ContainerFormatType.CFT_MPEG_4,
    videoBitrate : 3000000,
    videoCodec : media.CodecMimeType.VIDEO_AVC,
  };

  avTranscoder.prepare(avTranscoderConfig).then(() => {
    console.info('prepare success');
  }).catch((err: BusinessError) => {
    console.error('prepare failed and catch error is ' + err.message);
  });
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

videoPlayer.prepare((err: BusinessError) => {
  if (err) {
    console.error('Failed to prepare!');
  } else {
    console.info('Succeeded in preparing!');
  }
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

videoPlayer.prepare().then(() => {
  console.info('Succeeded in preparing');
}).catch((error: BusinessError) => {
  console.error(`video catchCallback, error:${error}`);
});
```

## release

```TypeScript
release(): Promise<void>
```

Releases video transcoding resources. This API uses a promise to return the result.After the resources are released, you can no longer perform any operation on the AVTranscoder instance.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-AVTranscoder-release(): Promise<void>--><!--Device-AVTranscoder-release(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVTranscoder

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) | Operation not allowed. Return by promise. |
| [5400105](../errorcode-media.md#5400105-play-service-dead) | Service died. Return by promise. |

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

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// promise.
videoRecorder.release().then(() => {
  console.info('release videorecorder success');
}).catch((err: BusinessError) => {
  console.error('release videorecorder failed and catch error is ' + err.message);
});
```

```TypeScript
audioPlayer.release();
audioPlayer = undefined;
```

```TypeScript
audioRecorder.on('release', () => {    // Set the 'release' event callback.
  console.info('audio recorder release called');
});
audioRecorder.release();
audioRecorder = undefined;
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';

let avImageGenerator: media.AVImageGenerator | undefined = undefined;

// Release the resources.
media.createAVImageGenerator((err: BusinessError, generator: media.AVImageGenerator) => {
  if (generator != null) {
    avImageGenerator = generator;
    console.info(`Succeeded in creating AVImageGenerator`);
    avImageGenerator.release((error: BusinessError) => {
      if (error) {
        console.error(`Failed to release, err = ${JSON.stringify(error)}`);
        return;
      }
      console.info(`Succeeded in releasing`);
    });
  } else {
    console.error(`Failed to create AVImageGenerator, error message:${err.message}`);
  }
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';

let avImageGenerator: media.AVImageGenerator | undefined = undefined;

// Release the resources.
media.createAVImageGenerator((err: BusinessError, generator: media.AVImageGenerator) => {
  if (generator != null) {
    avImageGenerator = generator;
    console.info(`Succeeded in creating AVImageGenerator`);
    avImageGenerator.release().then(() => {
      console.info(`Succeeded in releasing.`);
    }).catch((error: BusinessError) => {
      console.error(`Failed to release, error message:${error.message}`);
    });
  } else {
    console.error(`Failed to create AVImageGenerator, error message:${err.message}`);
  }
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';

async function test() {
  // Create an AVMetadataExtractor instance.
  let avMetadataExtractor: media.AVMetadataExtractor = await media.createAVMetadataExtractor();
  avMetadataExtractor.release((error: BusinessError) => {
    if (error) {
      console.error(`Failed to release, err = ${JSON.stringify(error)}`);
      return;
    }
    console.info(`Succeeded in releasing.`);
  });
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';

async function test() {
  // Create an AVMetadataExtractor instance.
  let avMetadataExtractor: media.AVMetadataExtractor = await media.createAVMetadataExtractor();
  avMetadataExtractor.release().then(() => {
    console.info(`Succeeded in releasing.`);
  }).catch((error: BusinessError) => {
    console.error(`Failed to release, error message:${error.message}`);
  });
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function  test(){
  let avPlayer = await media.createAVPlayer();
  // Here is only an example. In real development, you must wait for the stateChange event to successfully trigger and reach a state other than released before proceeding.
  avPlayer.release((err: BusinessError) => {
    if (err) {
      console.error('Failed to release,error message is :' + err.message);
    } else {
      console.info('Succeeded in releasing');
    }
  });
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function  test(){
  let avPlayer = await media.createAVPlayer();
  // Here is only an example. In real development, you must wait for the stateChange event to successfully trigger and reach a state other than released before proceeding.
  avPlayer.release().then(() => {
    console.info('Succeeded in releasing');
  }, (err: BusinessError) => {
    console.error('Failed to release,error message is :' + err.message);
  });
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

avRecorder.release((err: BusinessError) => {
  if (err) {
    console.error(`Failed to release AVRecorder and error is: Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info('Succeeded in releasing AVRecorder');
  }
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

avRecorder.release().then(() => {
  console.info('Succeeded in releasing AVRecorder');
}).catch((err: Error) => {
  let error: BusinessError = err as BusinessError;
  console.error(`Failed to release AVRecorder and error is: Code: ${error.code}, message: ${error.message}`);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// Initialize avScreenCaptureRecorder.
let avScreenCaptureRecorder: media.AVScreenCaptureRecorder | undefined;
media.createAVScreenCaptureRecorder().then((captureRecorder: media.AVScreenCaptureRecorder) => {
  if (captureRecorder != null) {
    avScreenCaptureRecorder = captureRecorder;
    console.info('Succeeded in creating avScreenCaptureRecorder');
  } else {
    console.error('Failed to create avScreenCaptureRecorder');
  }
}).catch((error: BusinessError) => {
  console.error(`createAVScreenCaptureRecorder catchCallback, error message:${error.message}`);
});

// Other processes.

// Call the release method.
if (avScreenCaptureRecorder != undefined) {
  avScreenCaptureRecorder.release().then(() => {
    console.info('Succeeded in releasing avScreenCaptureRecorder');
  }).catch((err: BusinessError) => {
    console.error(`Failed to release avScreenCaptureRecorder. Code: ${err.code}, message: ${err.message}`);
  });
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';

async function test() {
  // Create an AVTranscoder instance.
  let avTranscoder = await media.createAVTranscoder();
  avTranscoder.release().then(() => {
    console.info('release AVTranscoder success');
  }).catch((err: BusinessError) => {
    console.error('release AVTranscoder failed and catch error is ' + err.message);
  });
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

videoPlayer.release((err: BusinessError) => {
  if (err) {
    console.error('Failed to release!');
  } else {
    console.info('Succeeded in releasing!');
  }
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

videoPlayer.release().then(() => {
  console.info('Succeeded in releasing');
}).catch((error: BusinessError) => {
  console.error(`video catchCallback, error:${error}`);
});
```

## resume

```TypeScript
resume(): Promise<void>
```

Resumes video transcoding. This API uses a promise to return the result.This API can be called only after the [pause()](#pause) API is called.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-AVTranscoder-resume(): Promise<void>--><!--Device-AVTranscoder-resume(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVTranscoder

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) | Operation not allowed. Return by promise. |
| [5400103](../errorcode-media.md#5400103-io-error) | IO error. Return by promise. |
| [5400105](../errorcode-media.md#5400105-play-service-dead) | Service died. Return by promise. |

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

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// promise.
videoRecorder.resume().then(() => {
  console.info('resume videorecorder success');
}).catch((err: BusinessError) => {
  console.error('resume videorecorder failed and catch error is ' + err.message);
});
```

```TypeScript
audioRecorder.on('resume', () => {    // Set the 'resume' event callback.
  console.info('audio recorder resume called');
});
audioRecorder.resume();
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

avRecorder.resume((err: BusinessError) => {
  if (err) {
    console.error(`Failed to resume AVRecorder and error is: Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info('Succeeded in resuming AVRecorder');
  }
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

avRecorder.resume().then(() => {
  console.info('Succeeded in resuming AVRecorder');
}).catch((err: Error) => {
  let error: BusinessError = err as BusinessError;
  console.error(`Failed to resume AVRecorder failed and error is: Code: ${error.code}, message: ${error.message}`);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';

async function test() {
  // Create an AVTranscoder instance.
  let avTranscoder = await media.createAVTranscoder();
  avTranscoder.resume().then(() => {
    console.info('resume AVTranscoder success');
  }).catch((err: BusinessError) => {
    console.error('resume AVTranscoder failed and catch error is ' + err.message);
  });
}
```

## start

```TypeScript
start(): Promise<void>
```

Starts video transcoding. This API uses a promise to return the result.This API can be called only after the [prepare()](#prepare) API is called.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-AVTranscoder-start(): Promise<void>--><!--Device-AVTranscoder-start(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVTranscoder

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) | Operation not allowed. Return by promise. |
| [5400103](../errorcode-media.md#5400103-io-error) | IO error. Return by promise. |
| [5400105](../errorcode-media.md#5400105-play-service-dead) | Service died. Return by promise. |

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

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// promise.
videoRecorder.start().then(() => {
  console.info('start videorecorder success');
}).catch((err: BusinessError) => {
  console.error('start videorecorder failed and catch error is ' + err.message);
});
```

```TypeScript
audioRecorder.on('start', () => {    // Set the 'start' event callback.
  console.info('audio recorder start called');
});
audioRecorder.start();
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

avRecorder.start((err: BusinessError) => {
  if (err) {
    console.error(`Failed to start AVRecorder and error is: Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info('Succeeded in starting AVRecorder');
  }
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

avRecorder.start().then(() => {
  console.info('Succeeded in starting AVRecorder');
}).catch((err: Error) => {
  let error: BusinessError = err as BusinessError;
  console.error(`Failed to start AVRecorder and error is: Code: ${error.code}, message: ${error.message}`);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';

async function test() {
  // Create an AVTranscoder instance.
  let avTranscoder = await media.createAVTranscoder();
  avTranscoder.start().then(() => {
    console.info('start AVTranscoder success');
  }).catch((err: BusinessError) => {
    console.error('start AVTranscoder failed and catch error is ' + err.message);
  });
}
```

## fdDst

```TypeScript
fdDst: int
```

Destination media file descriptor, which specifies the data source. After creating an AVTranscoder instance, you must set both **fdSrc** and **fdDst**.  
**NOTE：**
- After the resource handle (FD) is transferred to an AVTranscoder instance, do not use the resource handle to perform other read and write operations, including but not limited to transferring this handle to other AVPlayer, AVMetadataExtractor, AVImageGenerator, or AVTranscoder instance. - Competition occurs when multiple AVTranscoders use the same resource handle to read and write files at the same time, resulting in errors in obtaining data.

**Type:** int

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-AVTranscoder-fdDst: int--><!--Device-AVTranscoder-fdDst: int-End-->

**System capability:** SystemCapability.Multimedia.Media.AVTranscoder

## fdSrc

```TypeScript
fdSrc: AVFileDescriptor
```

Source media file descriptor, which specifies the data source.There is a media file that stores continuous assets, the address offset is 0, and the byte length is 100. Its file descriptor is **AVFileDescriptor { fd = resourceHandle; offset = 0; length = 100; }**.  
**NOTE：**
- After the resource handle (FD) is transferred to an AVTranscoder instance, do not use the resource handle to perform other read and write operations, including but not limited to transferring this handle to other AVPlayer, AVMetadataExtractor, AVImageGenerator, or AVTranscoder instance. - Competition occurs when multiple AVTranscoders use the same resource handle to read and write files at the same time, resulting in errors in obtaining data.

**Type:** [AVFileDescriptor](arkts-media-media-avfiledescriptor-i.md)

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-AVTranscoder-fdSrc: AVFileDescriptor--><!--Device-AVTranscoder-fdSrc: AVFileDescriptor-End-->

**System capability:** SystemCapability.Multimedia.Media.AVTranscoder

