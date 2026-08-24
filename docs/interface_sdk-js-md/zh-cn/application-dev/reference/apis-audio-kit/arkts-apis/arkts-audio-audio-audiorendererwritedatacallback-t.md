# AudioRendererWriteDataCallback

```TypeScript
type AudioRendererWriteDataCallback = (data: ArrayBuffer) => AudioDataCallbackResult
```

音频渲染器写入数据的回调函数类型定义。

**起始版本：** 23

<!--Device-audio-type AudioRendererWriteDataCallback = (data: ArrayBuffer) => AudioDataCallbackResult--><!--Device-audio-type AudioRendererWriteDataCallback = (data: ArrayBuffer) => AudioDataCallbackResult-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | ArrayBuffer | 是 | 音频数据数组缓冲区。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AudioDataCallbackResult](arkts-audio-audio-audiodatacallbackresult-e.md) | 回调结果。如果返回 AudioDataCallbackResult.VALID， 表示数据有效并将被播放。如果返回 AudioDataCallbackResult.INVALID， 表示数据将不会被播放。 |

