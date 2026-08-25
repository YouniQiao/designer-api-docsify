# VideoRecorder (System API)

The maintenance of this interface has been stopped since version api 9. Please use AVRecorder. Manages and record video. Before calling an VideoRecorder method, you must use createVideoRecorder() to create an VideoRecorder instance.

**Since:** 9

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

get input surface.it must be called between prepare completed and start.

**Since:** 9

**System capability:** SystemCapability.Multimedia.Media.VideoRecorder

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) |
| [5400103](../errorcode-media.md#5400103-io-error) |
| [5400105](../errorcode-media.md#5400105-play-service-dead) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## getInputSurface

```TypeScript
getInputSurface(): Promise<string>
```

get input surface. it must be called between prepare completed and start.

**Since:** 9

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
| [5400105](../errorcode-media.md#5400105-play-service-dead) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## on('error')

```TypeScript
on(type: 'error', callback: ErrorCallback): void
```

Listens for video recording error events.

**Since:** 9

**System capability:** SystemCapability.Multimedia.Media.VideoRecorder

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'error' | Yes |
| callback | [ErrorCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [5400103](../errorcode-media.md#5400103-io-error) |
| [5400105](../errorcode-media.md#5400105-play-service-dead) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## pause

```TypeScript
pause(callback: AsyncCallback<void>): void
```

Pauses video recording.

**Since:** 9

**System capability:** SystemCapability.Multimedia.Media.VideoRecorder

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) |
| [5400103](../errorcode-media.md#5400103-io-error) |
| [5400105](../errorcode-media.md#5400105-play-service-dead) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## pause

```TypeScript
pause(): Promise<void>
```

Pauses video recording.

**Since:** 9

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
| [5400105](../errorcode-media.md#5400105-play-service-dead) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## prepare

```TypeScript
prepare(config: VideoRecorderConfig, callback: AsyncCallback<void>): void
```

Prepares for recording.

**Since:** 9

**Required permissions:** ohos.permission.MICROPHONE

**System capability:** SystemCapability.Multimedia.Media.VideoRecorder

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| config | [VideoRecorderConfig](arkts-media-media-videorecorderconfig-i-sys.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) |
| [5400105](../errorcode-media.md#5400105-play-service-dead) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## prepare

```TypeScript
prepare(config: VideoRecorderConfig): Promise<void>
```

Prepares for recording.

**Since:** 9

**Required permissions:** ohos.permission.MICROPHONE

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
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) |
| [5400105](../errorcode-media.md#5400105-play-service-dead) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## release

```TypeScript
release(callback: AsyncCallback<void>): void
```

Releases resources used for video recording.

**Since:** 9

**System capability:** SystemCapability.Multimedia.Media.VideoRecorder

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [5400105](../errorcode-media.md#5400105-play-service-dead) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## release

```TypeScript
release(): Promise<void>
```

Releases resources used for video recording.

**Since:** 9

**System capability:** SystemCapability.Multimedia.Media.VideoRecorder

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [5400105](../errorcode-media.md#5400105-play-service-dead) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## reset

```TypeScript
reset(callback: AsyncCallback<void>): void
```

Resets video recording. Before resetting video recording, you must call stop() to stop recording. After video recording is reset, you must call prepare() to set the recording configurations for another recording.

**Since:** 9

**System capability:** SystemCapability.Multimedia.Media.VideoRecorder

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [5400103](../errorcode-media.md#5400103-io-error) |
| [5400105](../errorcode-media.md#5400105-play-service-dead) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## reset

```TypeScript
reset(): Promise<void>
```

Resets video recording. Before resetting video recording, you must call stop() to stop recording. After video recording is reset, you must call prepare() to set the recording configurations for another recording.

**Since:** 9

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
| [5400105](../errorcode-media.md#5400105-play-service-dead) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## resume

```TypeScript
resume(callback: AsyncCallback<void>): void
```

Resumes video recording.

**Since:** 9

**System capability:** SystemCapability.Multimedia.Media.VideoRecorder

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) |
| [5400103](../errorcode-media.md#5400103-io-error) |
| [5400105](../errorcode-media.md#5400105-play-service-dead) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## resume

```TypeScript
resume(): Promise<void>
```

Resumes video recording.

**Since:** 9

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
| [5400105](../errorcode-media.md#5400105-play-service-dead) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## start

```TypeScript
start(callback: AsyncCallback<void>): void
```

Starts video recording.

**Since:** 9

**System capability:** SystemCapability.Multimedia.Media.VideoRecorder

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) |
| [5400103](../errorcode-media.md#5400103-io-error) |
| [5400105](../errorcode-media.md#5400105-play-service-dead) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## start

```TypeScript
start(): Promise<void>
```

Starts video recording.

**Since:** 9

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
| [5400105](../errorcode-media.md#5400105-play-service-dead) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## stop

```TypeScript
stop(callback: AsyncCallback<void>): void
```

Stops video recording.

**Since:** 9

**System capability:** SystemCapability.Multimedia.Media.VideoRecorder

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) |
| [5400103](../errorcode-media.md#5400103-io-error) |
| [5400105](../errorcode-media.md#5400105-play-service-dead) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## stop

```TypeScript
stop(): Promise<void>
```

Stops video recording.

**Since:** 9

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
| [5400105](../errorcode-media.md#5400105-play-service-dead) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## state

```TypeScript
readonly state: VideoRecordState
```

video recorder state.

**Type:** [VideoRecordState](arkts-media-media-videorecordstate-t-sys.md)

**Since:** 9

**System capability:** SystemCapability.Multimedia.Media.VideoRecorder

**System API:** This is a system API.
