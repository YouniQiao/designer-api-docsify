# TonePlayer (System API)

Provides APIs for tone playing.

**Since:** 23

<!--Device-audio-interface TonePlayer--><!--Device-audio-interface TonePlayer-End-->

**System capability:** SystemCapability.Multimedia.Audio.Tone

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { audio } from '@kit.AudioKit';
```

## load

```TypeScript
load(type: ToneType, callback: AsyncCallback<void>): void
```

Loads tone. This method uses an asynchronous callback to return the result.

**Since:** 23

<!--Device-TonePlayer-load(type: ToneType, callback: AsyncCallback<void>): void--><!--Device-TonePlayer-load(type: ToneType, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Tone

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | [ToneType](arkts-audio-audio-tonetype-e-sys.md) | Yes | Tone type to play. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

tonePlayer.load(audio.ToneType.TONE_TYPE_DIAL_5, (err: BusinessError) => {
  if (err) {
    console.error(`callback call load failed error: ${err.message}`);
    return;
  } else {
    console.info('callback call load success');
  }
});
```

```TypeScript
tonePlayer.load(audio.ToneType.TONE_TYPE_DIAL_1).then(() => {
  console.info('promise call load ');
}).catch(() => {
  console.error('promise call load fail');
});
```

## load

```TypeScript
load(type: ToneType): Promise<void>
```

Loads tone. This method uses a promise to return the result.

**Since:** 23

<!--Device-TonePlayer-load(type: ToneType): Promise<void>--><!--Device-TonePlayer-load(type: ToneType): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Tone

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | [ToneType](arkts-audio-audio-tonetype-e-sys.md) | Yes | Tone type to play. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise used to return the result. |

**Examples**

See [load](#load)

## release

```TypeScript
release(callback: AsyncCallback<void>): void
```

Releases the player. This method uses an asynchronous callback to return the result.

**Since:** 23

<!--Device-TonePlayer-release(callback: AsyncCallback<void>): void--><!--Device-TonePlayer-release(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Tone

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

tonePlayer.release((err: BusinessError) => {
  if (err) {
    console.error(`callback call release failed error: ${err.message}`);
    return;
  } else {
    console.info('callback call release success ');
  }
});
```

```TypeScript
tonePlayer.release().then(() => {
  console.info('promise call release');
}).catch(() => {
  console.error('promise call release fail');
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioCapturer.release((err: BusinessError) => {
  if (err) {
    console.error('capturer release failed');
  } else {
    console.info('capturer released.');
  }
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioCapturer.release().then(() => {
  console.info('AudioFrameworkRecLog: ---------RELEASE RECORD---------');
  console.info('AudioFrameworkRecLog: Capturer release : SUCCESS');
  console.info(`AudioFrameworkRecLog: AudioCapturer : STATE : ${audioCapturer.state}`);
}).catch((err: BusinessError) => {
  console.error(`AudioFrameworkRecLog: Capturer stop: ERROR: ${err}`);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.release((err: BusinessError) => {
  if (err) {
    console.error('Renderer release failed');
  } else {
    console.info('Renderer released.');
  }
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.release().then(() => {
  console.info('Renderer released successfully');
}).catch((err: BusinessError) => {
  console.error(`ERROR: ${err}`);
});
```

## release

```TypeScript
release(): Promise<void>
```

Releases the player. This method uses a promise to return the result.

**Since:** 23

<!--Device-TonePlayer-release(): Promise<void>--><!--Device-TonePlayer-release(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Tone

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise used to return the result. |

**Examples**

See [release](#release)

## start

```TypeScript
start(callback: AsyncCallback<void>): void
```

Starts player. This method uses an asynchronous callback to return the result.

**Since:** 23

<!--Device-TonePlayer-start(callback: AsyncCallback<void>): void--><!--Device-TonePlayer-start(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Tone

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

tonePlayer.start((err: BusinessError) => {
  if (err) {
    console.error(`callback call start failed error: ${err.message}`);
    return;
  } else {
    console.info('callback call start success');
  }
});
```

```TypeScript
tonePlayer.start().then(() => {
  console.info('promise call start');
}).catch(() => {
  console.error('promise call start fail');
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioCapturer.start((err: BusinessError) => {
  if (err) {
    console.error('Capturer start failed.');
  } else {
    console.info('Capturer start success.');
  }
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioCapturer.start().then(() => {
  console.info('Succeeded in doing start.');
  if (audioCapturer.state == audio.AudioState.STATE_RUNNING) {
    console.info('AudioFrameworkRecLog: AudioCapturer is in Running State');
  }
}).catch((err: BusinessError) => {
  console.error(`Failed to start. Code: ${err.code}, message: ${err.message}`);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.start((err: BusinessError) => {
  if (err) {
    console.error('Renderer start failed.');
  } else {
    console.info('Renderer start success.');
  }
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.start().then(() => {
  console.info('Renderer started');
}).catch((err: BusinessError) => {
  console.error(`ERROR: ${err}`);
});
```

## start

```TypeScript
start(): Promise<void>
```

Starts player. This method uses a promise to return the result.

**Since:** 23

<!--Device-TonePlayer-start(): Promise<void>--><!--Device-TonePlayer-start(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Tone

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise used to return the result. |

**Examples**

See [start](#start)

## stop

```TypeScript
stop(callback: AsyncCallback<void>): void
```

Stops player. This method uses an asynchronous callback to return the result.

**Since:** 23

<!--Device-TonePlayer-stop(callback: AsyncCallback<void>): void--><!--Device-TonePlayer-stop(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Tone

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

tonePlayer.stop((err: BusinessError) => {
  if (err) {
    console.error(`callback call stop error: ${err.message}`);
    return;
  } else {
    console.error('callback call stop success ');
  }
});
```

```TypeScript
tonePlayer.stop().then(() => {
  console.info('promise call stop finish');
}).catch(() => {
  console.error('promise call stop fail');
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioCapturer.stop((err: BusinessError) => {
  if (err) {
    console.error('Capturer stop failed');
  } else {
    console.info('Capturer stopped.');
  }
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioCapturer.stop().then(() => {
  console.info('Succeeded in doing stop.');
  if (audioCapturer.state == audio.AudioState.STATE_STOPPED){
    console.info('AudioFrameworkRecLog: State is Stopped:');
  }
}).catch((err: BusinessError) => {
  console.error(`Failed to stop. Code: ${err.code}, message: ${err.message}`);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.stop((err: BusinessError) => {
  if (err) {
    console.error('Renderer stop failed');
  } else {
    console.info('Renderer stopped.');
  }
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.stop().then(() => {
  console.info('Renderer stopped successfully');
}).catch((err: BusinessError) => {
  console.error(`ERROR: ${err}`);
});
```

## stop

```TypeScript
stop(): Promise<void>
```

Stops player. This method uses a promise to return the result.

**Since:** 23

<!--Device-TonePlayer-stop(): Promise<void>--><!--Device-TonePlayer-stop(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Tone

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise used to return the result. |

**Examples**

See [stop](#stop)

