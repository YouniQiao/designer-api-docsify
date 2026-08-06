# createTonePlayer (System API)

## createTonePlayer

```TypeScript
function createTonePlayer(options: AudioRendererInfo, callback: AsyncCallback<TonePlayer>): void
```

Obtains a \_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ instance. This method uses an asynchronous callback to return the renderer instance.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-audio-function createTonePlayer(options: AudioRendererInfo, callback: AsyncCallback<TonePlayer>): void--><!--Device-audio-function createTonePlayer(options: AudioRendererInfo, callback: AsyncCallback<TonePlayer>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Tone

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Tone playing attribute. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;TonePlayer&gt; | Yes | Callback used to return the tonePlayer instance. |

**Example**

```TypeScript
import { audio } from '@kit.AudioKit';

let audioRendererInfo: audio.AudioRendererInfo = {
  usage : audio.StreamUsage.STREAM_USAGE_DTMF,
  rendererFlags : 0
};
let tonePlayer: audio.TonePlayer;

audio.createTonePlayer(audioRendererInfo, (err, data) => {
  console.info(`callback call createTonePlayer: audioRendererInfo: ${audioRendererInfo}`);
  if (err) {
    console.error(`callback call createTonePlayer return error: ${err.message}`);
  } else {
    console.info(`callback call createTonePlayer return data: ${data}`);
    tonePlayer = data;
  }
});
```


## createTonePlayer

```TypeScript
function createTonePlayer(options: AudioRendererInfo, callback: AsyncCallback<TonePlayer | null>): void
```

Obtains a \_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ instance. This method uses an asynchronous callback to return the renderer instance.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-audio-function createTonePlayer(options: AudioRendererInfo, callback: AsyncCallback<TonePlayer | null>): void--><!--Device-audio-function createTonePlayer(options: AudioRendererInfo, callback: AsyncCallback<TonePlayer | null>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Tone

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Tone playing attribute. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;TonePlayer \| null&gt; | Yes | Callback used to return the tonePlayer instance， null when an error happens. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not system App. |


## createTonePlayer

```TypeScript
function createTonePlayer(options: AudioRendererInfo): Promise<TonePlayer>
```

Obtains a \_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ instance. This method uses a promise to return the renderer instance.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-audio-function createTonePlayer(options: AudioRendererInfo): Promise<TonePlayer>--><!--Device-audio-function createTonePlayer(options: AudioRendererInfo): Promise<TonePlayer>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Tone

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Tone playing attribute. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;TonePlayer&gt; | Promise used to return the tonePlayer instance. |

**Example**

```TypeScript
import { audio } from '@kit.AudioKit';

let tonePlayer: audio.TonePlayer;
async function createTonePlayerBefore(){
  let audioRendererInfo: audio.AudioRendererInfo = {
    usage : audio.StreamUsage.STREAM_USAGE_DTMF,
    rendererFlags : 0
  };
  tonePlayer = await audio.createTonePlayer(audioRendererInfo);
}
```


## createTonePlayer

```TypeScript
function createTonePlayer(options: AudioRendererInfo): Promise<TonePlayer | null>
```

Obtains a \_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ instance. This method uses a promise to return the renderer instance.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-audio-function createTonePlayer(options: AudioRendererInfo): Promise<TonePlayer | null>--><!--Device-audio-function createTonePlayer(options: AudioRendererInfo): Promise<TonePlayer | null>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Tone

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Tone playing attribute. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;TonePlayer \| null&gt; | Promise used to return the tonePlayer instance, or null when an error happens. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not system App. |

