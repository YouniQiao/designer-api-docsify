# AudioRendererWriteDataCallback

```TypeScript
type AudioRendererWriteDataCallback = (data: ArrayBuffer) => AudioDataCallbackResult
```

Type definition of callback function for audio renderer write data.

**Since:** 23

<!--Device-audio-type AudioRendererWriteDataCallback = (data: ArrayBuffer) => AudioDataCallbackResult--><!--Device-audio-type AudioRendererWriteDataCallback = (data: ArrayBuffer) => AudioDataCallbackResult-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | ArrayBuffer | Yes | audio data array buffer. |

**Return value:**

| Type | Description |
| --- | --- |
| [AudioDataCallbackResult](arkts-audio-audio-audiodatacallbackresult-e.md) | result of callback. If AudioDataCallbackResult.VALID is returned, it indicates the data is valid and will be played. If AudioDataCallbackResult.INVALID is returned, it indicates the data is will not be played. |

