# OnSeiMessageHandle

```TypeScript
type OnSeiMessageHandle = (messages: Array<SeiMessage>, playbackPosition?: int) => void
```

Describes the handle used to obtain SEI messages. This is used when in subscriptions to SEI message events, and the callback returns detailed SEI information.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-media-type OnSeiMessageHandle = (messages: Array<SeiMessage>, playbackPosition?: int) => void--><!--Device-media-type OnSeiMessageHandle = (messages: Array<SeiMessage>, playbackPosition?: int) => void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| messages | Array&lt;[SeiMessage](arkts-media-media-seimessage-i.md)&gt; | Yes | Array of SEI messages. |
| playbackPosition | int | No | Current playback position, in milliseconds. |

