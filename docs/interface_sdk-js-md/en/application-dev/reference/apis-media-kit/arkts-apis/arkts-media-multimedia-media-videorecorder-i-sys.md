# VideoRecorder (System API)

该接口自API version 9起停止维护，建议使用AVRecorder。视频录制管理类，用于视频录制。在调用VideoRecorder的方法前，必须先通过createVideoRecorder()创建一个VideoRecorder实例。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-unnamed-interface VideoRecorder--><!--Device-unnamed-interface VideoRecorder-End-->

**System capability:** SystemCapability.Multimedia.Media.VideoRecorder

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { media } from 'kits/@kit.MediaKit';
```

## getInputSurface

```TypeScript
getInputSurface(callback: AsyncCallback<string>): void
```

获取录制surface。必须在prepare完成后和start之前调用。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-VideoRecorder-getInputSurface(callback: AsyncCallback<string>): void--><!--Device-VideoRecorder-getInputSurface(callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.VideoRecorder

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes | 回调函数，返回输入surface id字符串。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 5400102 | Operation not allowed. Return by callback. |
| 5400103 | I/O error. Return by callback. |
| 202 | Not System App.<br>**Applicable version:** 12 and later |
| 5400105 | Service died. Return by callback. |

## Examples

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

获取录制surface。必须在prepare完成后和start之前调用。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-VideoRecorder-getInputSurface(callback: AsyncCallback<string | undefined>): void--><!--Device-VideoRecorder-getInputSurface(callback: AsyncCallback<string | undefined>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.VideoRecorder

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string \| undefined&gt; | Yes | 回调函数，返回输入surface id字符串。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 5400102 | Operation not allowed. Return by callback. |
| 5400103 | I/O error. Return by callback. |
| 202 | Not System App. |
| 5400105 | Service died. Return by callback. |

## getInputSurface

```TypeScript
getInputSurface(): Promise<string>
```

获取录制surface。必须在prepare完成后和start之前调用。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-VideoRecorder-getInputSurface(): Promise<string>--><!--Device-VideoRecorder-getInputSurface(): Promise<string>-End-->

**System capability:** SystemCapability.Multimedia.Media.VideoRecorder

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;string&gt; | Promise对象，返回输入surface id字符串。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 5400102 | Operation not allowed. Return by promise. |
| 5400103 | I/O error. Return by promise. |
| 202 | Not System App.<br>**Applicable version:** 12 and later |
| 5400105 | Service died. Return by promise. |

## Examples

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

获取录制surface。必须在prepare完成后和start之前调用。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-VideoRecorder-getInputSurface(): Promise<string | undefined>--><!--Device-VideoRecorder-getInputSurface(): Promise<string | undefined>-End-->

**System capability:** SystemCapability.Multimedia.Media.VideoRecorder

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;string \| undefined&gt; | Promise对象，返回输入surface id字符串。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 5400102 | Operation not allowed. Return by promise. |
| 5400103 | I/O error. Return by promise. |
| 202 | Not System App. |
| 5400105 | Service died. Return by promise. |

## on('error')

```TypeScript
on(type: 'error', callback: ErrorCallback): void
```

监听视频录制错误事件。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-VideoRecorder-on(type: 'error', callback: ErrorCallback): void--><!--Device-VideoRecorder-on(type: 'error', callback: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.Media.VideoRecorder

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'error' | Yes | 视频录制错误事件的类型。 |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | Yes | 回调函数，监听视频录制错误事件。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 5400103 | I/O error. Return by callback. |
| 201 | permission denied.<br>**Applicable version:** 12 and later |
| 202 | Not System App.<br>**Applicable version:** 12 and later |
| 5400105 | Service died. Return by callback. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// This event is reported when an error occurs during the retrieval of videoRecordState.
videoRecorder.on('error', (error: BusinessError) => { // Set the 'error' event callback.
  console.error(`audio error called, error: ${error}`);
})
```

## onError

```TypeScript
onError(callback: ErrorCallback): void
```

监听视频录制错误事件。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-VideoRecorder-onError(callback: ErrorCallback): void--><!--Device-VideoRecorder-onError(callback: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.Media.VideoRecorder

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | Yes | 回调函数，监听视频录制错误事件。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 5400103 | I/O error. Return by callback. |
| 201 | permission denied. |
| 202 | Not System App. |
| 5400105 | Service died. Return by callback. |

## pause

```TypeScript
pause(callback: AsyncCallback<void>): void
```

暂停视频录制。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-VideoRecorder-pause(callback: AsyncCallback<void>): void--><!--Device-VideoRecorder-pause(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.VideoRecorder

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数，暂停录制完成时返回。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 5400102 | Operation not allowed. Return by callback. |
| 5400103 | I/O error. Return by callback. |
| 202 | Not System App.<br>**Applicable version:** 12 and later |
| 5400105 | Service died. Return by callback. |

## Examples

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

暂停视频录制。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-VideoRecorder-pause(): Promise<void>--><!--Device-VideoRecorder-pause(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.VideoRecorder

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，暂停录制完成时返回。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 5400102 | Operation not allowed. Return by promise. |
| 5400103 | I/O error. Return by promise. |
| 202 | Not System App.<br>**Applicable version:** 12 and later |
| 5400105 | Service died. Return by promise. |

## Examples

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

视频录制准备。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.MICROPHONE

<!--Device-VideoRecorder-prepare(config: VideoRecorderConfig, callback: AsyncCallback<void>): void--><!--Device-VideoRecorder-prepare(config: VideoRecorderConfig, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.VideoRecorder

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| config | [VideoRecorderConfig](arkts-media-multimedia-media-videorecorderconfig-i-sys.md) | Yes | 录制参数。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数，准备录制完成时返回。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. &lt;br&gt;2. Incorrect parameter types. 3.Parameter verification failed. |
| 5400102 | Operation not allowed. Return by callback. |
| 201 | Permission denied. Return by callback. |
| 202 | Not System App.<br>**Applicable version:** 12 and later |
| 5400105 | Service died. Return by callback. |

## Examples

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

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.MICROPHONE

<!--Device-VideoRecorder-prepare(config: VideoRecorderConfig): Promise<void>--><!--Device-VideoRecorder-prepare(config: VideoRecorderConfig): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.VideoRecorder

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| config | [VideoRecorderConfig](arkts-media-multimedia-media-videorecorderconfig-i-sys.md) | Yes | 录制参数。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，准备录制完成时返回。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. &lt;br&gt;2. Incorrect parameter types. 3.Parameter verification failed. |
| 5400102 | Operation not allowed. Return by promise. |
| 201 | Permission denied. Return by promise. |
| 202 | Not System App.<br>**Applicable version:** 12 and later |
| 5400105 | Service died. Return by promise. |

## Examples

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

释放视频录制资源。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-VideoRecorder-release(callback: AsyncCallback<void>): void--><!--Device-VideoRecorder-release(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.VideoRecorder

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数，释放资源完成时返回。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 202 | Not System App.<br>**Applicable version:** 12 and later |
| 5400105 | Service died. Return by callback. |

## Examples

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

释放视频录制资源。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-VideoRecorder-release(): Promise<void>--><!--Device-VideoRecorder-release(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.VideoRecorder

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，释放资源完成时返回。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 202 | Not System App.<br>**Applicable version:** 12 and later |
| 5400105 | Service died. Return by callback. |

## Examples

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

重置视频录制。在重置之前，必须先调用stop()停止录制。重置后，必须调用prepare()设置录制配置以进行下一次录制。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-VideoRecorder-reset(callback: AsyncCallback<void>): void--><!--Device-VideoRecorder-reset(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.VideoRecorder

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数，重置完成时返回。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 5400103 | I/O error. Return by callback. |
| 202 | Not System App.<br>**Applicable version:** 12 and later |
| 5400105 | Service died. Return by callback. |

## Examples

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

重置视频录制。在重置之前，必须先调用stop()停止录制。重置后，必须调用prepare()设置录制配置以进行下一次录制。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-VideoRecorder-reset(): Promise<void>--><!--Device-VideoRecorder-reset(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.VideoRecorder

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，重置完成时返回。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 5400103 | I/O error. Return by promise. |
| 202 | Not System App.<br>**Applicable version:** 12 and later |
| 5400105 | Service died. Return by promise. |

## Examples

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

恢复视频录制。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-VideoRecorder-resume(callback: AsyncCallback<void>): void--><!--Device-VideoRecorder-resume(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.VideoRecorder

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数，恢复录制完成时返回。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 5400102 | Operation not allowed. Return by callback. |
| 5400103 | I/O error. Return by callback. |
| 202 | Not System App.<br>**Applicable version:** 12 and later |
| 5400105 | Service died. Return by callback. |

## Examples

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

恢复视频录制。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-VideoRecorder-resume(): Promise<void>--><!--Device-VideoRecorder-resume(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.VideoRecorder

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，恢复录制完成时返回。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 5400102 | Operation not allowed. Return by promise. |
| 5400103 | I/O error. Return by promise. |
| 202 | Not System App.<br>**Applicable version:** 12 and later |
| 5400105 | Service died. Return by promise. |

## Examples

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

开始视频录制。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-VideoRecorder-start(callback: AsyncCallback<void>): void--><!--Device-VideoRecorder-start(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.VideoRecorder

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数，开始录制完成时返回。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 5400102 | Operation not allowed. Return by callback. |
| 5400103 | I/O error. Return by callback. |
| 202 | Not System App.<br>**Applicable version:** 12 and later |
| 5400105 | Service died. Return by callback. |

## Examples

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

开始视频录制。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-VideoRecorder-start(): Promise<void>--><!--Device-VideoRecorder-start(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.VideoRecorder

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，开始录制完成时返回。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 5400102 | Operation not allowed. Return by promise. |
| 5400103 | I/O error. Return by promise. |
| 202 | Not System App.<br>**Applicable version:** 12 and later |
| 5400105 | Service died. Return by promise. |

## Examples

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

停止视频录制。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-VideoRecorder-stop(callback: AsyncCallback<void>): void--><!--Device-VideoRecorder-stop(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.VideoRecorder

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数，停止录制完成时返回。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 5400102 | Operation not allowed. Return by callback. |
| 5400103 | I/O error. Return by callback. |
| 202 | Not System App.<br>**Applicable version:** 12 and later |
| 5400105 | Service died. Return by callback. |

## Examples

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

停止视频录制。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-VideoRecorder-stop(): Promise<void>--><!--Device-VideoRecorder-stop(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.VideoRecorder

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，停止录制完成时返回。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 5400102 | Operation not allowed. Return by promise. |
| 5400103 | I/O error. Return by promise. |
| 202 | Not System App.<br>**Applicable version:** 12 and later |
| 5400105 | Service died. Return by promise. |

## Examples

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

视频录制状态。

**Type:** [VideoRecordState](arkts-media-videorecordstate-t-sys.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-VideoRecorder-readonly state: VideoRecordState--><!--Device-VideoRecorder-readonly state: VideoRecordState-End-->

**System capability:** SystemCapability.Multimedia.Media.VideoRecorder

**System API:** This is a system API.

