# AudioRendererWriteDataCallback

```TypeScript
type AudioRendererWriteDataCallback = (data: ArrayBuffer) => AudioDataCallbackResult | void
```

Defines the callback function used to write data to the audio renderer. Once the callback function finishes its execution, the audio service queues the data pointed to by **data** for playback. Therefore, do not change the data outside the callback. It is crucial to fill **data** with the exact length of data designated for playback; otherwise, noises may occur during playback.

**Since:** 12

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| data | ArrayBuffer | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [AudioDataCallbackResult](arkts-audio-audio-audiodatacallbackresult-e.md) \| void |
