# AudioCapturer

This interface provides APIs for audio capture.Before calling any API in AudioCapturer, you must use [createAudioCapturer](arkts-audio-audio-createaudiocapturer-f.md) to create an AudioCapturer instance.

> **NOTE：**
> 
> - The initial APIs of this interface are supported since API version 8.

**Since:** 8

**System capability:** SystemCapability.Multimedia.Audio.Capturer

## Modules to Import

```TypeScript
import audio from '@kit.AudioKit';
import audioHaptic from '@kit.AudioKitHaptic';
```

## offReadMicInData

```TypeScript
offReadMicInData(callback?: Callback<AudioCapturerMicInData>): void
```

Unsubscribes from micIn audio data callback.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioCapturerMicInData](arkts-audio-audio-audiocapturermicindata-i-sys.md)&gt; | No | Callback for the buffers to read. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Caller is not a system application. |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. |
| [6800103](../errorcode-audio.md#6800103-unsupported-state) | Operation not permitted at running state. |

**Examples**

```TypeScript
import { audio } from '@kit.AudioKit';
import { BusinessError } from '@kit.BasicServicesKit';

let audioMicInStreamInfo: audio.AudioStreamInfo = {
  samplingRate: audio.AudioSamplingRate.SAMPLE_RATE_48000,
  channels: audio.AudioChannel.CHANNEL_2,
  sampleFormat: audio.AudioSampleFormat.SAMPLE_FORMAT_S16LE,
  encodingType: audio.AudioEncodingType.ENCODING_TYPE_RAW
};

let audioCapturerInfo: audio.AudioCapturerInfo = {
  source: audio.SourceType.SOURCE_TYPE_UNPROCESSED_VOICE_ASSISTANT,
  capturerFlags: 0
};

let audioCapturerMicInConfig: audio.AudioCapturerMicInConfig = {
  micInStreamInfo: audioMicInStreamInfo,
  capturerInfo: audioCapturerInfo
};

let readMicInDataCallback: Callback<audio.AudioCapturerMicInData> =
  (data: audio.AudioCapturerMicInData): void => {
    console.info(`mic-in data length: ${data.micInData.byteLength}`);
  };

async function unregisterReadMicInDataCallback(): Promise<void> {
  try {
    let audioCapturer: audio.AudioCapturer | null =
      await audio.createMicInAudioCapturer(audioCapturerMicInConfig);
    if (audioCapturer === null) {
      console.error('AudioCapturer Created : ERROR : audioCapturer is null');
      return;
    }

    audioCapturer.onReadMicInData(readMicInDataCallback);

    // Unregister the listener for the specified callback.
    audioCapturer.offReadMicInData(readMicInDataCallback);

    // Cancel all subscriptions to the event.
    audioCapturer.offReadMicInData();
  } catch (err) {
    let error = err as BusinessError;
    console.error(`Failed to create AudioCapturer. Code: ${error.code}, message: ${error.message}`);
  }
}
```

## onReadMicInData

```TypeScript
onReadMicInData(callback: Callback<AudioCapturerMicInData>): void
```

Subscribes to micIn audio data callback. This callback has higher priority than 'readData' callback. If this callback and 'readData' callback are both subscribed, only this callback will be triggered. See onReadData for more details. The event is triggered when an audio buffer is available for reading more data.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioCapturerMicInData](arkts-audio-audio-audiocapturermicindata-i-sys.md)&gt; | Yes | Callback for the buffers to read. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Caller is not a system application. |
| [6800103](../errorcode-audio.md#6800103-unsupported-state) | Operation not permitted at running state. |

**Examples**

```TypeScript
import { audio } from '@kit.AudioKit';
import { BusinessError } from '@kit.BasicServicesKit';

let audioEcStreamInfo: audio.AudioStreamInfo = {
  samplingRate: audio.AudioSamplingRate.SAMPLE_RATE_48000,
  channels: audio.AudioChannel.CHANNEL_2,
  sampleFormat: audio.AudioSampleFormat.SAMPLE_FORMAT_S16LE,
  encodingType: audio.AudioEncodingType.ENCODING_TYPE_RAW
};

let audioProcessedStreamInfo: audio.AudioStreamInfo = {
  samplingRate: audio.AudioSamplingRate.SAMPLE_RATE_48000,
  channels: audio.AudioChannel.CHANNEL_2,
  sampleFormat: audio.AudioSampleFormat.SAMPLE_FORMAT_S16LE,
  encodingType: audio.AudioEncodingType.ENCODING_TYPE_RAW
};

let audioMicInStreamInfo: audio.AudioStreamInfo = {
  samplingRate: audio.AudioSamplingRate.SAMPLE_RATE_48000,
  channels: audio.AudioChannel.CHANNEL_2,
  sampleFormat: audio.AudioSampleFormat.SAMPLE_FORMAT_S16LE,
  encodingType: audio.AudioEncodingType.ENCODING_TYPE_RAW
};

let audioCapturerInfo: audio.AudioCapturerInfo = {
  source: audio.SourceType.SOURCE_TYPE_UNPROCESSED_VOICE_ASSISTANT,
  capturerFlags: 0
};

let audioCapturerMicInConfig: audio.AudioCapturerMicInConfig = {
  processedStreamInfo: audioProcessedStreamInfo,
  micInStreamInfo: audioMicInStreamInfo,
  ecStreamInfo: audioEcStreamInfo,
  capturerInfo: audioCapturerInfo
};

// data indicates the processed audio data, and micInData indicates the original Mic-In audio data.
// ecData indicates the echo reference audio data. If ecStreamInfo is not configured, this field may be null.
let readMicInDataCallback: Callback<audio.AudioCapturerMicInData> =
  (data: audio.AudioCapturerMicInData): void => {
    let ecDataLength: number = data.ecData ? data.ecData.byteLength : 0;
    console.info(`processed data length: ${data.data.byteLength}`);
    console.info(`mic-in data length: ${data.micInData.byteLength}`);
    console.info(`echo reference data length: ${ecDataLength}`);
  };

async function registerReadMicInDataCallback(): Promise<void> {
  try {
    // Create a Mic-In collector instance and then register the data read callback.
    let audioCapturer: audio.AudioCapturer | null =
      await audio.createMicInAudioCapturer(audioCapturerMicInConfig);
    if (audioCapturer === null) {
      console.error('AudioCapturer Created : ERROR : audioCapturer is null');
      return;
    }
    // After the registration is successful, readMicInDataCallback is triggered when there is an audio buffer that can be read.
    audioCapturer.onReadMicInData(readMicInDataCallback);
    console.info('Succeeded in registering onReadMicInData callback.');
  } catch (err) {
    let error = err as BusinessError;
    console.error(`Failed to create AudioCapturer. Code: ${error.code}, message: ${error.message}`);
  }
}
```

## setInputDeviceToAccessory

```TypeScript
setInputDeviceToAccessory(): void
```

Sets default input device of this Capturer to DEVICE_TYPE_ACCESSORY. Other capturers' devices will not be affected by this method. This method can only be used before the capture stream starts. Besides, if audio accessory is not connected, this method will report fail. After calling this function, the input device of this capturer will not be affected by other interfaces.

**Since:** 19

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**System API:** This is a system API.

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Caller is not a system application. |
| [6800103](../errorcode-audio.md#6800103-unsupported-state) | Operation not permit at current state. |
