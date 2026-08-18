# AVCastController

AVCastController definition used to implement a remote control when a cast is connected

**Since:** 23

<!--Device-avSession-interface AVCastController--><!--Device-avSession-interface AVCastController-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

## Modules to Import

```TypeScript
```

## getAVPlaybackState

```TypeScript
getAVPlaybackState(callback: AsyncCallback<AVPlaybackState>): void
```

Get the playback status of the current player

**Since:** 23

<!--Device-AVCastController-getAVPlaybackState(callback: AsyncCallback<AVPlaybackState>): void--><!--Device-AVCastController-getAVPlaybackState(callback: AsyncCallback<AVPlaybackState>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AVPlaybackState](arkts-avsession-avsession-avplaybackstate-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) |

## getAVPlaybackState

```TypeScript
getAVPlaybackState(): Promise<AVPlaybackState>
```

Get the playback status of the current player

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVCastController-getAVPlaybackState(): Promise<AVPlaybackState>--><!--Device-AVCastController-getAVPlaybackState(): Promise<AVPlaybackState>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[AVPlaybackState](arkts-avsession-avsession-avplaybackstate-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) |

## getCurrentItem

```TypeScript
getCurrentItem(callback: AsyncCallback<AVQueueItem>): void
```

Get the current playing item

**Since:** 23

<!--Device-AVCastController-getCurrentItem(callback: AsyncCallback<AVQueueItem>): void--><!--Device-AVCastController-getCurrentItem(callback: AsyncCallback<AVQueueItem>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AVQueueItem](arkts-avsession-avsession-avqueueitem-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) |

## getCurrentItem

```TypeScript
getCurrentItem(): Promise<AVQueueItem>
```

Get the current playing item

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVCastController-getCurrentItem(): Promise<AVQueueItem>--><!--Device-AVCastController-getCurrentItem(): Promise<AVQueueItem>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[AVQueueItem](arkts-avsession-avsession-avqueueitem-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) |

## getRecommendedResolutionLevel

```TypeScript
getRecommendedResolutionLevel(decoderType: DecoderType): Promise<ResolutionLevel>
```

Get recommended resolution of remote player based on each decoder.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-AVCastController-getRecommendedResolutionLevel(decoderType: DecoderType): Promise<ResolutionLevel>--><!--Device-AVCastController-getRecommendedResolutionLevel(decoderType: DecoderType): Promise<ResolutionLevel>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| decoderType | [DecoderType](arkts-avsession-avsession-decodertype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[ResolutionLevel](arkts-avsession-avsession-resolutionlevel-e.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) |

## getSupportedDecoders

```TypeScript
getSupportedDecoders(): Promise<Array<DecoderType>>
```

Get supported decoders of remote player.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-AVCastController-getSupportedDecoders(): Promise<Array<DecoderType>>--><!--Device-AVCastController-getSupportedDecoders(): Promise<Array<DecoderType>>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[DecoderType](arkts-avsession-avsession-decodertype-e.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) |

## getSupportedHdrCapabilities

```TypeScript
getSupportedHdrCapabilities(): Promise<Array<hdrCapability.HDRFormat>>
```

Get supported hdr capabilities of remote player.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-AVCastController-getSupportedHdrCapabilities(): Promise<Array<hdrCapability.HDRFormat>>--><!--Device-AVCastController-getSupportedHdrCapabilities(): Promise<Array<hdrCapability.HDRFormat>>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;hdrCapability.HDRFormat & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) |

## getSupportedPlaySpeeds

```TypeScript
getSupportedPlaySpeeds(): Promise<Array<number>>
```

Get supported speed of remote player.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-AVCastController-getSupportedPlaySpeeds(): Promise<Array<double>>--><!--Device-AVCastController-getSupportedPlaySpeeds(): Promise<Array<double>>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;number & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) |

## getValidCommands

```TypeScript
getValidCommands(callback: AsyncCallback<Array<AVCastControlCommandType>>): void
```

Get commands supported by the current cast controller

**Since:** 23

<!--Device-AVCastController-getValidCommands(callback: AsyncCallback<Array<AVCastControlCommandType>>): void--><!--Device-AVCastController-getValidCommands(callback: AsyncCallback<Array<AVCastControlCommandType>>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[AVCastControlCommandType](arkts-avsession-avsession-avcastcontrolcommandtype-t.md)&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) |

## getValidCommands

```TypeScript
getValidCommands(): Promise<Array<AVCastControlCommandType>>
```

Get commands supported by the current cast controller

**Since:** 23

<!--Device-AVCastController-getValidCommands(): Promise<Array<AVCastControlCommandType>>--><!--Device-AVCastController-getValidCommands(): Promise<Array<AVCastControlCommandType>>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[AVCastControlCommandType](arkts-avsession-avsession-avcastcontrolcommandtype-t.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) |

## offCastControlAudioRendererError

```TypeScript
offCastControlAudioRendererError(callback?: ErrorCallback): void
```

Unregister listeners for cast control audio renderer error events.

**Since:** 23

<!--Device-AVCastController-offCastControlAudioRendererError(callback?: ErrorCallback): void--><!--Device-AVCastController-offCastControlAudioRendererError(callback?: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | No |

## offCastControlDecodingError

```TypeScript
offCastControlDecodingError(callback?: ErrorCallback): void
```

Unregister listeners for cast control decoding error events.

**Since:** 23

<!--Device-AVCastController-offCastControlDecodingError(callback?: ErrorCallback): void--><!--Device-AVCastController-offCastControlDecodingError(callback?: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | No |

## offCastControlDrmError

```TypeScript
offCastControlDrmError(callback?: ErrorCallback): void
```

Unregister listeners for cast control drm error events.

**Since:** 23

<!--Device-AVCastController-offCastControlDrmError(callback?: ErrorCallback): void--><!--Device-AVCastController-offCastControlDrmError(callback?: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | No |

## offCastControlGenericError

```TypeScript
offCastControlGenericError(callback?: ErrorCallback): void
```

Unregister listeners for cast control generic error events.

**Since:** 23

<!--Device-AVCastController-offCastControlGenericError(callback?: ErrorCallback): void--><!--Device-AVCastController-offCastControlGenericError(callback?: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | No |

## offCastControlIoError

```TypeScript
offCastControlIoError(callback?: ErrorCallback): void
```

Unregister listeners for cast control input/output error events.

**Since:** 23

<!--Device-AVCastController-offCastControlIoError(callback?: ErrorCallback): void--><!--Device-AVCastController-offCastControlIoError(callback?: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | No |

## offCastControlParsingError

```TypeScript
offCastControlParsingError(callback?: ErrorCallback): void
```

Unregister listeners for cast control parsing error events.

**Since:** 23

<!--Device-AVCastController-offCastControlParsingError(callback?: ErrorCallback): void--><!--Device-AVCastController-offCastControlParsingError(callback?: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | No |

## offCustomDataChange

```TypeScript
offCustomDataChange(callback?: Callback<Record<string, Object>>): void
```

Unregister listener for custom data sent from remote device.

**Since:** 23

<!--Device-AVCastController-offCustomDataChange(callback?: Callback<Record<string, Object>>): void--><!--Device-AVCastController-offCustomDataChange(callback?: Callback<Record<string, Object>>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[Record](../../apis-na/arkts-apis/arkts-na-record-t.md)&lt;string, Object&gt;&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) |

## offEndOfStream

```TypeScript
offEndOfStream(callback?: NoParamCallback): void
```

Unregister endOfStream state callback.

**Since:** 23

<!--Device-AVCastController-offEndOfStream(callback?: NoParamCallback): void--><!--Device-AVCastController-offEndOfStream(callback?: NoParamCallback): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [NoParamCallback](arkts-avsession-avsession-noparamcallback-t.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) |

## offError

```TypeScript
offError(): void
```

Unregister listens for playback error events.

**Since:** 23

<!--Device-AVCastController-offError(): void--><!--Device-AVCastController-offError(): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Error codes:**

| Error Code ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) |
| [5400102](../../apis-media-kit/errorcode-media.md#5400102-unsupported-operation) |
| [5400103](../../apis-media-kit/errorcode-media.md#5400103-io-error) |
| [5400101](../../apis-media-kit/errorcode-media.md#5400101-memory-allocation-failed) |
| [5400106](../../apis-media-kit/errorcode-media.md#5400106-format-not-supported) |
| [5400104](../../apis-media-kit/errorcode-media.md#5400104-operation-timeout) |
| [5400105](../../apis-media-kit/errorcode-media.md#5400105-play-service-dead) |

## offKeyRequest

```TypeScript
offKeyRequest(callback?: KeyRequestCallback): void
```

Unregister listener for drm key request.

**Since:** 23

<!--Device-AVCastController-offKeyRequest(callback?: KeyRequestCallback): void--><!--Device-AVCastController-offKeyRequest(callback?: KeyRequestCallback): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [KeyRequestCallback](arkts-avsession-avsession-keyrequestcallback-t.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) |

## offMediaItemChange

```TypeScript
offMediaItemChange(): void
```

Unregister listener for current media item playback events.

**Since:** 23

<!--Device-AVCastController-offMediaItemChange(): void--><!--Device-AVCastController-offMediaItemChange(): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Error codes:**

| Error Code ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) |

## offPlayNext

```TypeScript
offPlayNext(): void
```

Unregister playback command callback sent by remote side or media center. When canceling the callback, need to update the supported commands list.

**Since:** 23

<!--Device-AVCastController-offPlayNext(): void--><!--Device-AVCastController-offPlayNext(): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Error codes:**

| Error Code ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) |

## offPlayPrevious

```TypeScript
offPlayPrevious(): void
```

Unregister playback command callback sent by remote side or media center. When canceling the callback, need to update the supported commands list.

**Since:** 23

<!--Device-AVCastController-offPlayPrevious(): void--><!--Device-AVCastController-offPlayPrevious(): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Error codes:**

| Error Code ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) |

## offPlaybackStateChange

```TypeScript
offPlaybackStateChange(callback?: Callback<AVPlaybackState>): void
```

Unregister playback state changed callback

**Since:** 23

<!--Device-AVCastController-offPlaybackStateChange(callback?: Callback<AVPlaybackState>): void--><!--Device-AVCastController-offPlaybackStateChange(callback?: Callback<AVPlaybackState>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AVPlaybackState](arkts-avsession-avsession-avplaybackstate-i.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) |

## offRequestPlay

```TypeScript
offRequestPlay(callback?: Callback<AVQueueItem>): void
```

Unregister requested playback command callback sent by remote side or media center.

**Since:** 23

<!--Device-AVCastController-offRequestPlay(callback?: Callback<AVQueueItem>): void--><!--Device-AVCastController-offRequestPlay(callback?: Callback<AVQueueItem>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AVQueueItem](arkts-avsession-avsession-avqueueitem-i.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) |

## offSeekDone

```TypeScript
offSeekDone(): void
```

Unregister listens for playback events.

**Since:** 23

<!--Device-AVCastController-offSeekDone(): void--><!--Device-AVCastController-offSeekDone(): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Error codes:**

| Error Code ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) |

## offValidCommandChange

```TypeScript
offValidCommandChange(callback?: Callback<Array<AVCastControlCommandType>>): void
```

Unregister the valid commands of the casted session changed callback

**Since:** 23

<!--Device-AVCastController-offValidCommandChange(callback?: Callback<Array<AVCastControlCommandType>>): void--><!--Device-AVCastController-offValidCommandChange(callback?: Callback<Array<AVCastControlCommandType>>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;[AVCastControlCommandType](arkts-avsession-avsession-avcastcontrolcommandtype-t.md)&gt;&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) |

## offVideoSizeChange

```TypeScript
offVideoSizeChange(): void
```

Unregister listener for video size change event, used at remote side.

**Since:** 23

<!--Device-AVCastController-offVideoSizeChange(): void--><!--Device-AVCastController-offVideoSizeChange(): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Error codes:**

| Error Code ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) |

## off_castControlAudioRendererError

```TypeScript
off(type: 'castControlAudioRendererError', callback?: ErrorCallback): void
```

Unregister listeners for cast control audio renderer error events.

**Since:** 13

**Atomic service API:** This API can be used in atomic services since API version 13.

<!--Device-AVCastController-off(type: 'castControlAudioRendererError', callback?: ErrorCallback): void--><!--Device-AVCastController-off(type: 'castControlAudioRendererError', callback?: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'castControlAudioRendererError' | Yes |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## off_castControlDecodingError

```TypeScript
off(type: 'castControlDecodingError', callback?: ErrorCallback): void
```

Unregister listeners for cast control decoding error events.

**Since:** 13

**Atomic service API:** This API can be used in atomic services since API version 13.

<!--Device-AVCastController-off(type: 'castControlDecodingError', callback?: ErrorCallback): void--><!--Device-AVCastController-off(type: 'castControlDecodingError', callback?: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'castControlDecodingError' | Yes |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## off_castControlDrmError

```TypeScript
off(type: 'castControlDrmError', callback?: ErrorCallback): void
```

Unregister listeners for cast control drm error events.

**Since:** 13

**Atomic service API:** This API can be used in atomic services since API version 13.

<!--Device-AVCastController-off(type: 'castControlDrmError', callback?: ErrorCallback): void--><!--Device-AVCastController-off(type: 'castControlDrmError', callback?: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'castControlDrmError' | Yes |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## off_castControlGenericError

```TypeScript
off(type: 'castControlGenericError', callback?: ErrorCallback): void
```

Unregister listeners for cast control generic error events.

**Since:** 13

**Atomic service API:** This API can be used in atomic services since API version 13.

<!--Device-AVCastController-off(type: 'castControlGenericError', callback?: ErrorCallback): void--><!--Device-AVCastController-off(type: 'castControlGenericError', callback?: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'castControlGenericError' | Yes |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## off_castControlIoError

```TypeScript
off(type: 'castControlIoError', callback?: ErrorCallback): void
```

Unregister listeners for cast control input/output error events.

**Since:** 13

**Atomic service API:** This API can be used in atomic services since API version 13.

<!--Device-AVCastController-off(type: 'castControlIoError', callback?: ErrorCallback): void--><!--Device-AVCastController-off(type: 'castControlIoError', callback?: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'castControlIoError' | Yes |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## off_castControlParsingError

```TypeScript
off(type: 'castControlParsingError', callback?: ErrorCallback): void
```

Unregister listeners for cast control parsing error events.

**Since:** 13

**Atomic service API:** This API can be used in atomic services since API version 13.

<!--Device-AVCastController-off(type: 'castControlParsingError', callback?: ErrorCallback): void--><!--Device-AVCastController-off(type: 'castControlParsingError', callback?: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'castControlParsingError' | Yes |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## off_customDataChange

```TypeScript
off(type: 'customDataChange', callback?: Callback<Record<string, Object>>): void
```

Unregister listener for custom data sent from remote device.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-AVCastController-off(type: 'customDataChange', callback?: Callback<Record<string, Object>>): void--><!--Device-AVCastController-off(type: 'customDataChange', callback?: Callback<Record<string, Object>>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'customDataChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[Record](../../apis-na/arkts-apis/arkts-na-record-t.md)&lt;string, Object&gt;&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) |

## off_endOfStream

```TypeScript
off(type: 'endOfStream', callback?: Callback<void>): void
```

Unregister endOfStream state callback.

**Since:** 11

<!--Device-AVCastController-off(type: 'endOfStream', callback?: Callback<void>): void--><!--Device-AVCastController-off(type: 'endOfStream', callback?: Callback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'endOfStream' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) |

## off_error

```TypeScript
off(type: 'error'): void
```

Unregister listens for playback error events.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVCastController-off(type: 'error'): void--><!--Device-AVCastController-off(type: 'error'): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'error' | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) |
| [5400102](../../apis-media-kit/errorcode-media.md#5400102-unsupported-operation) |
| [5400103](../../apis-media-kit/errorcode-media.md#5400103-io-error) |
| [5400101](../../apis-media-kit/errorcode-media.md#5400101-memory-allocation-failed) |
| [5400106](../../apis-media-kit/errorcode-media.md#5400106-format-not-supported) |
| [5400104](../../apis-media-kit/errorcode-media.md#5400104-operation-timeout) |
| [5400105](../../apis-media-kit/errorcode-media.md#5400105-play-service-dead) |

## off_keyRequest

```TypeScript
off(type: 'keyRequest', callback?: KeyRequestCallback): void
```

Unregister listener for drm key request.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVCastController-off(type: 'keyRequest', callback?: KeyRequestCallback): void--><!--Device-AVCastController-off(type: 'keyRequest', callback?: KeyRequestCallback): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'keyRequest' | Yes |
| callback | [KeyRequestCallback](arkts-avsession-avsession-keyrequestcallback-t.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) |

## off_mediaItemChange

```TypeScript
off(type: 'mediaItemChange'): void
```

Unregister listener for current media item playback events.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVCastController-off(type: 'mediaItemChange'): void--><!--Device-AVCastController-off(type: 'mediaItemChange'): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'mediaItemChange' | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) |

## off_playNext

```TypeScript
off(type: 'playNext'): void
```

Unregister playback command callback sent by remote side or media center. When canceling the callback, need to update the supported commands list.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVCastController-off(type: 'playNext'): void--><!--Device-AVCastController-off(type: 'playNext'): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'playNext' | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) |

## off_playPrevious

```TypeScript
off(type: 'playPrevious'): void
```

Unregister playback command callback sent by remote side or media center. When canceling the callback, need to update the supported commands list.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVCastController-off(type: 'playPrevious'): void--><!--Device-AVCastController-off(type: 'playPrevious'): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'playPrevious' | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) |

## off_playbackStateChange

```TypeScript
off(type: 'playbackStateChange', callback?: (state: AVPlaybackState) => void): void
```

Unregister playback state changed callback

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVCastController-off(type: 'playbackStateChange', callback?: (state: AVPlaybackState) => void): void--><!--Device-AVCastController-off(type: 'playbackStateChange', callback?: (state: AVPlaybackState) => void): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'playbackStateChange' | Yes |
| callback | (state: AVPlaybackState) = & gt; void | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) |

## off_requestPlay

```TypeScript
off(type: 'requestPlay', callback?: Callback<AVQueueItem>): void
```

Unregister requested playback command callback sent by remote side or media center.

**Since:** 11

<!--Device-AVCastController-off(type: 'requestPlay', callback?: Callback<AVQueueItem>): void--><!--Device-AVCastController-off(type: 'requestPlay', callback?: Callback<AVQueueItem>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'requestPlay' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AVQueueItem](arkts-avsession-avsession-avqueueitem-i.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) |

## off_seekDone

```TypeScript
off(type: 'seekDone'): void
```

Unregister listens for playback events.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVCastController-off(type: 'seekDone'): void--><!--Device-AVCastController-off(type: 'seekDone'): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'seekDone' | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) |

## off_validCommandChange

```TypeScript
off(type: 'validCommandChange', callback?: Callback<Array<AVCastControlCommandType>>)
```

Unregister the valid commands of the casted session changed callback

**Since:** 11

<!--Device-AVCastController-off(type: 'validCommandChange', callback?: Callback<Array<AVCastControlCommandType>>)--><!--Device-AVCastController-off(type: 'validCommandChange', callback?: Callback<Array<AVCastControlCommandType>>)-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'validCommandChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;[AVCastControlCommandType](arkts-avsession-avsession-avcastcontrolcommandtype-t.md)&gt;&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) |

## off_videoSizeChange

```TypeScript
off(type: 'videoSizeChange'): void
```

Unregister listener for video size change event, used at remote side.

**Since:** 12

<!--Device-AVCastController-off(type: 'videoSizeChange'): void--><!--Device-AVCastController-off(type: 'videoSizeChange'): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'videoSizeChange' | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) |

**Examples**

```TypeScript
avCastController.off('videoSizeChange');
```

## onCastControlAudioRendererError

```TypeScript
onCastControlAudioRendererError(callback: ErrorCallback): void
```

Register listeners for cast control audio renderer error error events.

**Since:** 23

<!--Device-AVCastController-onCastControlAudioRendererError(callback: ErrorCallback): void--><!--Device-AVCastController-onCastControlAudioRendererError(callback: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [6615000](../errorcode-avsession.md#6615000-unknown-error-related-to-the-audio-renderer) |
| [6615001](../errorcode-avsession.md#6615001-audio-renderer-initialization-failure) |
| [6615002](../errorcode-avsession.md#6615002-audio-renderer-failure-in-writing-data) |

## onCastControlDecodingError

```TypeScript
onCastControlDecodingError(callback: ErrorCallback): void
```

Register listeners for cast control decoding error events.

**Since:** 23

<!--Device-AVCastController-onCastControlDecodingError(callback: ErrorCallback): void--><!--Device-AVCastController-onCastControlDecodingError(callback: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [6614004](../errorcode-avsession.md#6614004-content-format-is-beyond-the-device-capability) |
| [6614005](../errorcode-avsession.md#6614005-decoding-of-the-content-format-is-not-supported) |
| [6614000](../errorcode-avsession.md#6614000-unknown-decoding-error) |
| [6614001](../errorcode-avsession.md#6614001-decoder-initialization-failure) |
| [6614002](../errorcode-avsession.md#6614002-decoder-query-failure) |
| [6614003](../errorcode-avsession.md#6614003-media-sample-decoding-failure) |

## onCastControlDrmError

```TypeScript
onCastControlDrmError(callback: ErrorCallback): void
```

Register listeners for cast control drm error events.

**Since:** 23

<!--Device-AVCastController-onCastControlDrmError(callback: ErrorCallback): void--><!--Device-AVCastController-onCastControlDrmError(callback: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [6616004](../errorcode-avsession.md#6616004-license-obtaining-failure) |
| [6616100](../errorcode-avsession.md#6616100-error-in-processing-the-key-response) |
| [6616005](../errorcode-avsession.md#6616005-operation-not-allowed-by-the-license-policy) |
| [6616006](../errorcode-avsession.md#6616006-drm-system-error) |
| [6616007](../errorcode-avsession.md#6616007-drm-privileges-revoked) |
| [6616000](../errorcode-avsession.md#6616000-unknown-drm-error) |
| [6616001](../errorcode-avsession.md#6616001-device-does-not-support-the-selected-drm-solution) |
| [6616002](../errorcode-avsession.md#6616002-device-provisioning-failure) |
| [6616003](../errorcode-avsession.md#6616003-drmprotected-content-to-play-is-incompatible) |
| [6616008](../errorcode-avsession.md#6616008-expired-drm-license-loaded) |

## onCastControlGenericError

```TypeScript
onCastControlGenericError(callback: ErrorCallback): void
```

Register listeners for cast control generic error events.

**Since:** 23

<!--Device-AVCastController-onCastControlGenericError(callback: ErrorCallback): void--><!--Device-AVCastController-onCastControlGenericError(callback: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [6611108](../errorcode-avsession.md#6611108-operation-not-allowed) |
| [6611104](../errorcode-avsession.md#6611104-unsupported-playback-speed) |
| [6611105](../errorcode-avsession.md#6611105-device-revocation) |
| [6611106](../errorcode-avsession.md#6611106-invalid-input-parameter) |
| [6611107](../errorcode-avsession.md#6611107-memory-allocation-failure) |
| [6611004](../errorcode-avsession.md#6611004-runtime-check-failure) |
| [6611100](../errorcode-avsession.md#6611100-crossdevice-data-transmission-locked) |
| [6611101](../errorcode-avsession.md#6611101-unsupported-seek-mode) |
| [6611102](../errorcode-avsession.md#6611102-invalid-seek-target) |
| [6611103](../errorcode-avsession.md#6611103-unsupported-playback-mode) |
| [6611000](../errorcode-avsession.md#6611000-unknown-error-in-the-cast-controller) |
| [6611001](../errorcode-avsession.md#6611001-unknown-error-in-the-remote-device) |
| [6611002](../errorcode-avsession.md#6611002-loading-position-exceeds-the-total-video-progress) |
| [6611003](../errorcode-avsession.md#6611003-cast-controller-loading-timeout) |

## onCastControlIoError

```TypeScript
onCastControlIoError(callback: ErrorCallback): void
```

Register listeners for cast control input/output error events.

**Since:** 23

<!--Device-AVCastController-onCastControlIoError(callback: ErrorCallback): void--><!--Device-AVCastController-onCastControlIoError(callback: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [6612004](../errorcode-avsession.md#6612004-unexpected-http-response-status-code-from-the-http-server) |
| [6612100](../errorcode-avsession.md#6612100-no-playable-content) |
| [6612005](../errorcode-avsession.md#6612005-file-does-not-exist) |
| [6612101](../errorcode-avsession.md#6612101-failure-in-reading-media-assets) |
| [6612006](../errorcode-avsession.md#6612006-no-permission-for-io-operations) |
| [6612102](../errorcode-avsession.md#6612102-resource-is-being-used) |
| [6612007](../errorcode-avsession.md#6612007-operation-not-allowed-by-network-security-configuration) |
| [6612103](../errorcode-avsession.md#6612103-content-expired) |
| [6612000](../errorcode-avsession.md#6612000-unknown-io-error) |
| [6612001](../errorcode-avsession.md#6612001-network-connection-failure) |
| [6612002](../errorcode-avsession.md#6612002-network-timeout) |
| [6612003](../errorcode-avsession.md#6612003-invalid-contenttype-http-header) |
| [6612008](../errorcode-avsession.md#6612008-data-to-read-out-of-range) |
| [6612104](../errorcode-avsession.md#6612104-requested-content-cannot-be-used) |
| [6612105](../errorcode-avsession.md#6612105-unable-to-verify-the-allowed-content) |
| [6612106](../errorcode-avsession.md#6612106-frequent-resource-usage) |
| [6612107](../errorcode-avsession.md#6612107-failure-in-sending-resource-packages-to-the-remote-device) |

## onCastControlParsingError

```TypeScript
onCastControlParsingError(callback: ErrorCallback): void
```

Register listeners for cast control parsing error events.

**Since:** 23

<!--Device-AVCastController-onCastControlParsingError(callback: ErrorCallback): void--><!--Device-AVCastController-onCastControlParsingError(callback: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [6613004](../errorcode-avsession.md#6613004-unsupported-feature-in-the-media-manifest) |
| [6613000](../errorcode-avsession.md#6613000-unknown-parsing-error) |
| [6613001](../errorcode-avsession.md#6613001-invalid-type) |
| [6613002](../errorcode-avsession.md#6613002-error-in-parsing-media-manifest) |
| [6613003](../errorcode-avsession.md#6613003-unsupported-media-format) |

## onCustomDataChange

```TypeScript
onCustomDataChange(callback: Callback<Record<string, Object>>): void
```

Register listener for custom data sent from remote device.

**Since:** 23

<!--Device-AVCastController-onCustomDataChange(callback: Callback<Record<string, Object>>): void--><!--Device-AVCastController-onCustomDataChange(callback: Callback<Record<string, Object>>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[Record](../../apis-na/arkts-apis/arkts-na-record-t.md)&lt;string, Object&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) |

## onEndOfStream

```TypeScript
onEndOfStream(callback: NoParamCallback): void
```

Register endOfStream state callback. Application needs update the new media resource when receive these commands by using playItem.

**Since:** 23

<!--Device-AVCastController-onEndOfStream(callback: NoParamCallback): void--><!--Device-AVCastController-onEndOfStream(callback: NoParamCallback): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [NoParamCallback](arkts-avsession-avsession-noparamcallback-t.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) |

## onError

```TypeScript
onError(callback: ErrorCallback): void
```

Register listeners for playback error events.

**Since:** 23

<!--Device-AVCastController-onError(callback: ErrorCallback): void--><!--Device-AVCastController-onError(callback: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) |
| [5400102](../../apis-media-kit/errorcode-media.md#5400102-unsupported-operation) |
| [5400103](../../apis-media-kit/errorcode-media.md#5400103-io-error) |
| [5400101](../../apis-media-kit/errorcode-media.md#5400101-memory-allocation-failed) |
| [5400106](../../apis-media-kit/errorcode-media.md#5400106-format-not-supported) |
| [5400104](../../apis-media-kit/errorcode-media.md#5400104-operation-timeout) |
| [5400105](../../apis-media-kit/errorcode-media.md#5400105-play-service-dead) |

## onKeyRequest

```TypeScript
onKeyRequest(callback: KeyRequestCallback): void
```

Register listener for drm key request.

**Since:** 23

<!--Device-AVCastController-onKeyRequest(callback: KeyRequestCallback): void--><!--Device-AVCastController-onKeyRequest(callback: KeyRequestCallback): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [KeyRequestCallback](arkts-avsession-avsession-keyrequestcallback-t.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) |

## onMediaItemChange

```TypeScript
onMediaItemChange(callback: Callback<AVQueueItem>): void
```

Register listener for current media item playback events.

**Since:** 23

<!--Device-AVCastController-onMediaItemChange(callback: Callback<AVQueueItem>): void--><!--Device-AVCastController-onMediaItemChange(callback: Callback<AVQueueItem>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AVQueueItem](arkts-avsession-avsession-avqueueitem-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) |

## onPlayNext

```TypeScript
onPlayNext(callback: NoParamCallback): void
```

Register playback command callback sent by remote side or media center. Application needs update the new media resource when receive these commands by using playItem.

**Since:** 23

<!--Device-AVCastController-onPlayNext(callback: NoParamCallback): void--><!--Device-AVCastController-onPlayNext(callback: NoParamCallback): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [NoParamCallback](arkts-avsession-avsession-noparamcallback-t.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) |

## onPlayPrevious

```TypeScript
onPlayPrevious(callback: NoParamCallback): void
```

Register playback command callback sent by remote side or media center. Application needs update the new media resource when receive these commands by using playItem.

**Since:** 23

<!--Device-AVCastController-onPlayPrevious(callback: NoParamCallback): void--><!--Device-AVCastController-onPlayPrevious(callback: NoParamCallback): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [NoParamCallback](arkts-avsession-avsession-noparamcallback-t.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) |

## onPlaybackStateChange

```TypeScript
onPlaybackStateChange(filter: Array<string>, callback: Callback<AVPlaybackState>): void
```

Register playback state changed callback

**Since:** 23

<!--Device-AVCastController-onPlaybackStateChange(filter: Array<string>, callback: Callback<AVPlaybackState>): void--><!--Device-AVCastController-onPlaybackStateChange(filter: Array<string>, callback: Callback<AVPlaybackState>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| filter | Array & lt;string & gt; | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AVPlaybackState](arkts-avsession-avsession-avplaybackstate-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) |

## onPlaybackStateChangeAll

```TypeScript
onPlaybackStateChangeAll(callback: Callback<AVPlaybackState>): void
```

Registers a callback to be invoked whenever the playback state changes

**Since:** 23

<!--Device-AVCastController-onPlaybackStateChangeAll(callback: Callback<AVPlaybackState>): void--><!--Device-AVCastController-onPlaybackStateChangeAll(callback: Callback<AVPlaybackState>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AVPlaybackState](arkts-avsession-avsession-avplaybackstate-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) |

## onRequestPlay

```TypeScript
onRequestPlay(callback: Callback<AVQueueItem>): void
```

Register requested playback command callback sent by remote side or media center. The AVQueueItem may include the requested assetId, starting position and other configurations.

**Since:** 23

<!--Device-AVCastController-onRequestPlay(callback: Callback<AVQueueItem>): void--><!--Device-AVCastController-onRequestPlay(callback: Callback<AVQueueItem>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AVQueueItem](arkts-avsession-avsession-avqueueitem-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) |

## onSeekDone

```TypeScript
onSeekDone(callback: Callback<number>): void
```

Register listens for playback events.

**Since:** 23

<!--Device-AVCastController-onSeekDone(callback: Callback<int>): void--><!--Device-AVCastController-onSeekDone(callback: Callback<int>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) |

## onValidCommandChange

```TypeScript
onValidCommandChange(callback: Callback<Array<AVCastControlCommandType>>): void
```

Register the valid commands of the casted session changed callback

**Since:** 23

<!--Device-AVCastController-onValidCommandChange(callback: Callback<Array<AVCastControlCommandType>>): void--><!--Device-AVCastController-onValidCommandChange(callback: Callback<Array<AVCastControlCommandType>>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;[AVCastControlCommandType](arkts-avsession-avsession-avcastcontrolcommandtype-t.md)&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) |

## onVideoSizeChange

```TypeScript
onVideoSizeChange(callback: VideoSizeEvent): void
```

Register listener for video size change event, used at remote side.

**Since:** 23

<!--Device-AVCastController-onVideoSizeChange(callback: VideoSizeEvent): void--><!--Device-AVCastController-onVideoSizeChange(callback: VideoSizeEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [VideoSizeEvent](arkts-avsession-avsession-videosizeevent-t.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) |

## on_castControlAudioRendererError

```TypeScript
on(type: 'castControlAudioRendererError', callback: ErrorCallback): void
```

Register listeners for cast control audio renderer error error events.

**Since:** 13

**Atomic service API:** This API can be used in atomic services since API version 13.

<!--Device-AVCastController-on(type: 'castControlAudioRendererError', callback: ErrorCallback): void--><!--Device-AVCastController-on(type: 'castControlAudioRendererError', callback: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'castControlAudioRendererError' | Yes |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [6615000](../errorcode-avsession.md#6615000-unknown-error-related-to-the-audio-renderer) |
| [6615001](../errorcode-avsession.md#6615001-audio-renderer-initialization-failure) |
| [6615002](../errorcode-avsession.md#6615002-audio-renderer-failure-in-writing-data) |

## on_castControlDecodingError

```TypeScript
on(type: 'castControlDecodingError', callback: ErrorCallback): void
```

Register listeners for cast control decoding error events.

**Since:** 13

**Atomic service API:** This API can be used in atomic services since API version 13.

<!--Device-AVCastController-on(type: 'castControlDecodingError', callback: ErrorCallback): void--><!--Device-AVCastController-on(type: 'castControlDecodingError', callback: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'castControlDecodingError' | Yes |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [6614004](../errorcode-avsession.md#6614004-content-format-is-beyond-the-device-capability) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [6614005](../errorcode-avsession.md#6614005-decoding-of-the-content-format-is-not-supported) |
| [6614000](../errorcode-avsession.md#6614000-unknown-decoding-error) |
| [6614001](../errorcode-avsession.md#6614001-decoder-initialization-failure) |
| [6614002](../errorcode-avsession.md#6614002-decoder-query-failure) |
| [6614003](../errorcode-avsession.md#6614003-media-sample-decoding-failure) |

## on_castControlDrmError

```TypeScript
on(type: 'castControlDrmError', callback: ErrorCallback): void
```

Register listeners for cast control drm error events.

**Since:** 13

**Atomic service API:** This API can be used in atomic services since API version 13.

<!--Device-AVCastController-on(type: 'castControlDrmError', callback: ErrorCallback): void--><!--Device-AVCastController-on(type: 'castControlDrmError', callback: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'castControlDrmError' | Yes |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [6616004](../errorcode-avsession.md#6616004-license-obtaining-failure) |
| [6616100](../errorcode-avsession.md#6616100-error-in-processing-the-key-response) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [6616005](../errorcode-avsession.md#6616005-operation-not-allowed-by-the-license-policy) |
| [6616006](../errorcode-avsession.md#6616006-drm-system-error) |
| [6616007](../errorcode-avsession.md#6616007-drm-privileges-revoked) |
| [6616000](../errorcode-avsession.md#6616000-unknown-drm-error) |
| [6616001](../errorcode-avsession.md#6616001-device-does-not-support-the-selected-drm-solution) |
| [6616002](../errorcode-avsession.md#6616002-device-provisioning-failure) |
| [6616003](../errorcode-avsession.md#6616003-drmprotected-content-to-play-is-incompatible) |
| [6616008](../errorcode-avsession.md#6616008-expired-drm-license-loaded) |

## on_castControlGenericError

```TypeScript
on(type: 'castControlGenericError', callback: ErrorCallback): void
```

Register listeners for cast control generic error events.

**Since:** 13

**Atomic service API:** This API can be used in atomic services since API version 13.

<!--Device-AVCastController-on(type: 'castControlGenericError', callback: ErrorCallback): void--><!--Device-AVCastController-on(type: 'castControlGenericError', callback: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'castControlGenericError' | Yes |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [6611108](../errorcode-avsession.md#6611108-operation-not-allowed) |
| [6611104](../errorcode-avsession.md#6611104-unsupported-playback-speed) |
| [6611105](../errorcode-avsession.md#6611105-device-revocation) |
| [6611106](../errorcode-avsession.md#6611106-invalid-input-parameter) |
| [6611107](../errorcode-avsession.md#6611107-memory-allocation-failure) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [6611004](../errorcode-avsession.md#6611004-runtime-check-failure) |
| [6611100](../errorcode-avsession.md#6611100-crossdevice-data-transmission-locked) |
| [6611101](../errorcode-avsession.md#6611101-unsupported-seek-mode) |
| [6611102](../errorcode-avsession.md#6611102-invalid-seek-target) |
| [6611103](../errorcode-avsession.md#6611103-unsupported-playback-mode) |
| [6611000](../errorcode-avsession.md#6611000-unknown-error-in-the-cast-controller) |
| [6611001](../errorcode-avsession.md#6611001-unknown-error-in-the-remote-device) |
| [6611002](../errorcode-avsession.md#6611002-loading-position-exceeds-the-total-video-progress) |
| [6611003](../errorcode-avsession.md#6611003-cast-controller-loading-timeout) |

## on_castControlIoError

```TypeScript
on(type: 'castControlIoError', callback: ErrorCallback): void
```

Register listeners for cast control input/output error events.

**Since:** 13

**Atomic service API:** This API can be used in atomic services since API version 13.

<!--Device-AVCastController-on(type: 'castControlIoError', callback: ErrorCallback): void--><!--Device-AVCastController-on(type: 'castControlIoError', callback: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'castControlIoError' | Yes |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [6612004](../errorcode-avsession.md#6612004-unexpected-http-response-status-code-from-the-http-server) |
| [6612100](../errorcode-avsession.md#6612100-no-playable-content) |
| [6612005](../errorcode-avsession.md#6612005-file-does-not-exist) |
| [6612101](../errorcode-avsession.md#6612101-failure-in-reading-media-assets) |
| [6612006](../errorcode-avsession.md#6612006-no-permission-for-io-operations) |
| [6612102](../errorcode-avsession.md#6612102-resource-is-being-used) |
| [6612007](../errorcode-avsession.md#6612007-operation-not-allowed-by-network-security-configuration) |
| [6612103](../errorcode-avsession.md#6612103-content-expired) |
| [6612000](../errorcode-avsession.md#6612000-unknown-io-error) |
| [6612001](../errorcode-avsession.md#6612001-network-connection-failure) |
| [6612002](../errorcode-avsession.md#6612002-network-timeout) |
| [6612003](../errorcode-avsession.md#6612003-invalid-contenttype-http-header) |
| [6612008](../errorcode-avsession.md#6612008-data-to-read-out-of-range) |
| [6612104](../errorcode-avsession.md#6612104-requested-content-cannot-be-used) |
| [6612105](../errorcode-avsession.md#6612105-unable-to-verify-the-allowed-content) |
| [6612106](../errorcode-avsession.md#6612106-frequent-resource-usage) |
| [6612107](../errorcode-avsession.md#6612107-failure-in-sending-resource-packages-to-the-remote-device) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## on_castControlParsingError

```TypeScript
on(type: 'castControlParsingError', callback: ErrorCallback): void
```

Register listeners for cast control parsing error events.

**Since:** 13

**Atomic service API:** This API can be used in atomic services since API version 13.

<!--Device-AVCastController-on(type: 'castControlParsingError', callback: ErrorCallback): void--><!--Device-AVCastController-on(type: 'castControlParsingError', callback: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'castControlParsingError' | Yes |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [6613004](../errorcode-avsession.md#6613004-unsupported-feature-in-the-media-manifest) |
| [6613000](../errorcode-avsession.md#6613000-unknown-parsing-error) |
| [6613001](../errorcode-avsession.md#6613001-invalid-type) |
| [6613002](../errorcode-avsession.md#6613002-error-in-parsing-media-manifest) |
| [6613003](../errorcode-avsession.md#6613003-unsupported-media-format) |

## on_customDataChange

```TypeScript
on(type: 'customDataChange', callback: Callback<Record<string, Object>>): void
```

Register listener for custom data sent from remote device.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-AVCastController-on(type: 'customDataChange', callback: Callback<Record<string, Object>>): void--><!--Device-AVCastController-on(type: 'customDataChange', callback: Callback<Record<string, Object>>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'customDataChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[Record](../../apis-na/arkts-apis/arkts-na-record-t.md)&lt;string, Object&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) |

## on_endOfStream

```TypeScript
on(type: 'endOfStream', callback: Callback<void>): void
```

Register endOfStream state callback. Application needs update the new media resource when receive these commands by using playItem.

**Since:** 11

<!--Device-AVCastController-on(type: 'endOfStream', callback: Callback<void>): void--><!--Device-AVCastController-on(type: 'endOfStream', callback: Callback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'endOfStream' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) |

## on_error

```TypeScript
on(type: 'error', callback: ErrorCallback): void
```

Register listeners for playback error events.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVCastController-on(type: 'error', callback: ErrorCallback): void--><!--Device-AVCastController-on(type: 'error', callback: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'error' | Yes |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) |
| [5400102](../../apis-media-kit/errorcode-media.md#5400102-unsupported-operation) |
| [5400103](../../apis-media-kit/errorcode-media.md#5400103-io-error) |
| [5400101](../../apis-media-kit/errorcode-media.md#5400101-memory-allocation-failed) |
| [5400106](../../apis-media-kit/errorcode-media.md#5400106-format-not-supported) |
| [5400104](../../apis-media-kit/errorcode-media.md#5400104-operation-timeout) |
| [5400105](../../apis-media-kit/errorcode-media.md#5400105-play-service-dead) |

## on_keyRequest

```TypeScript
on(type: 'keyRequest', callback: KeyRequestCallback): void
```

Register listener for drm key request.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVCastController-on(type: 'keyRequest', callback: KeyRequestCallback): void--><!--Device-AVCastController-on(type: 'keyRequest', callback: KeyRequestCallback): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'keyRequest' | Yes |
| callback | [KeyRequestCallback](arkts-avsession-avsession-keyrequestcallback-t.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) |

## on_mediaItemChange

```TypeScript
on(type: 'mediaItemChange', callback: Callback<AVQueueItem>): void
```

Register listener for current media item playback events.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVCastController-on(type: 'mediaItemChange', callback: Callback<AVQueueItem>): void--><!--Device-AVCastController-on(type: 'mediaItemChange', callback: Callback<AVQueueItem>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'mediaItemChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AVQueueItem](arkts-avsession-avsession-avqueueitem-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) |

## on_playNext

```TypeScript
on(type: 'playNext', callback: Callback<void>): void
```

Register playback command callback sent by remote side or media center. Application needs update the new media resource when receive these commands by using playItem.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVCastController-on(type: 'playNext', callback: Callback<void>): void--><!--Device-AVCastController-on(type: 'playNext', callback: Callback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'playNext' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) |

## on_playPrevious

```TypeScript
on(type: 'playPrevious', callback: Callback<void>): void
```

Register playback command callback sent by remote side or media center. Application needs update the new media resource when receive these commands by using playItem.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVCastController-on(type: 'playPrevious', callback: Callback<void>): void--><!--Device-AVCastController-on(type: 'playPrevious', callback: Callback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'playPrevious' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) |

## on_playbackStateChange

```TypeScript
on(type: 'playbackStateChange', filter: Array<keyof AVPlaybackState> | 'all', callback: (state: AVPlaybackState) => void): void
```

Register playback state changed callback

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVCastController-on(type: 'playbackStateChange', filter: Array<keyof AVPlaybackState> | 'all', callback: (state: AVPlaybackState) => void): void--><!--Device-AVCastController-on(type: 'playbackStateChange', filter: Array<keyof AVPlaybackState> | 'all', callback: (state: AVPlaybackState) => void): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'playbackStateChange' | Yes |
| filter | Array & lt;keyof AVPlaybackState & gt; \ | 'all' | Yes |
| callback | (state: AVPlaybackState) = & gt; void | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) |

## on_requestPlay

```TypeScript
on(type: 'requestPlay', callback: Callback<AVQueueItem>): void
```

Register requested playback command callback sent by remote side or media center. The AVQueueItem may include the requested assetId, starting position and other configurations.

**Since:** 11

<!--Device-AVCastController-on(type: 'requestPlay', callback: Callback<AVQueueItem>): void--><!--Device-AVCastController-on(type: 'requestPlay', callback: Callback<AVQueueItem>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'requestPlay' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AVQueueItem](arkts-avsession-avsession-avqueueitem-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) |

## on_seekDone

```TypeScript
on(type: 'seekDone', callback: Callback<number>): void
```

Register listens for playback events.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVCastController-on(type: 'seekDone', callback: Callback<int>): void--><!--Device-AVCastController-on(type: 'seekDone', callback: Callback<int>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'seekDone' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) |

## on_validCommandChange

```TypeScript
on(type: 'validCommandChange', callback: Callback<Array<AVCastControlCommandType>>)
```

Register the valid commands of the casted session changed callback

**Since:** 11

<!--Device-AVCastController-on(type: 'validCommandChange', callback: Callback<Array<AVCastControlCommandType>>)--><!--Device-AVCastController-on(type: 'validCommandChange', callback: Callback<Array<AVCastControlCommandType>>)-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'validCommandChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;[AVCastControlCommandType](arkts-avsession-avsession-avcastcontrolcommandtype-t.md)&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) |

## on_videoSizeChange

```TypeScript
on(type: 'videoSizeChange', callback: (width: number, height: number) => void): void
```

Register listener for video size change event, used at remote side.

**Since:** 12

<!--Device-AVCastController-on(type: 'videoSizeChange', callback: (width: int, height: int) => void): void--><!--Device-AVCastController-on(type: 'videoSizeChange', callback: (width: int, height: int) => void): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'videoSizeChange' | Yes |
| callback | (width: number, height: number) = & gt; void | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) |

**Examples**

```TypeScript
avCastController.on('videoSizeChange', (width: number, height: number) => {
  console.info(`width : ${width} `);
  console.info(`height: ${height} `);
});
```

## prepare

```TypeScript
prepare(item: AVQueueItem, callback: AsyncCallback<void>): void
```

Load the current item and mediaUri can be null, this is needed for sink media information displaying

**Since:** 23

<!--Device-AVCastController-prepare(item: AVQueueItem, callback: AsyncCallback<void>): void--><!--Device-AVCastController-prepare(item: AVQueueItem, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| item | [AVQueueItem](arkts-avsession-avsession-avqueueitem-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) |
| [6600109](../errorcode-avsession.md#6600109-remote-session-does-not-exist) |

## prepare

```TypeScript
prepare(item: AVQueueItem): Promise<void>
```

Load the current item and mediaUri can be null, this is needed for sink media information displaying

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVCastController-prepare(item: AVQueueItem): Promise<void>--><!--Device-AVCastController-prepare(item: AVQueueItem): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| item | [AVQueueItem](arkts-avsession-avsession-avqueueitem-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) |
| [6600109](../errorcode-avsession.md#6600109-remote-session-does-not-exist) |

## processMediaKeyResponse

```TypeScript
processMediaKeyResponse(assetId: string, response: Uint8Array): Promise<void>
```

Process the response corresponding to the media key request obtained by the application.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-AVCastController-processMediaKeyResponse(assetId: string, response: Uint8Array): Promise<void>--><!--Device-AVCastController-processMediaKeyResponse(assetId: string, response: Uint8Array): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| assetId | string | Yes |
| response | Uint8Array | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) |

## release

```TypeScript
release(callback: AsyncCallback<void>): void
```

Destroy the controller

**Since:** 23

<!--Device-AVCastController-release(callback: AsyncCallback<void>): void--><!--Device-AVCastController-release(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) |

## release

```TypeScript
release(): Promise<void>
```

Destroy the controller

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVCastController-release(): Promise<void>--><!--Device-AVCastController-release(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) |

## sendControlCommand

```TypeScript
sendControlCommand(command: AVCastControlCommand, callback: AsyncCallback<void>): void
```

Send control commands to remote player

**Since:** 23

<!--Device-AVCastController-sendControlCommand(command: AVCastControlCommand, callback: AsyncCallback<void>): void--><!--Device-AVCastController-sendControlCommand(command: AVCastControlCommand, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| command | [AVCastControlCommand](arkts-avsession-avsession-avcastcontrolcommand-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) |
| [6600109](../errorcode-avsession.md#6600109-remote-session-does-not-exist) |
| [6600105](../errorcode-avsession.md#6600105-invalid-session-command) |

## sendControlCommand

```TypeScript
sendControlCommand(command: AVCastControlCommand): Promise<void>
```

Send control commands to remote player

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVCastController-sendControlCommand(command: AVCastControlCommand): Promise<void>--><!--Device-AVCastController-sendControlCommand(command: AVCastControlCommand): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| command | [AVCastControlCommand](arkts-avsession-avsession-avcastcontrolcommand-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) |
| [6600109](../errorcode-avsession.md#6600109-remote-session-does-not-exist) |
| [6600105](../errorcode-avsession.md#6600105-invalid-session-command) |

## sendCustomData

```TypeScript
sendCustomData(data: Record<string, Object>): Promise<void>
```

Sends custom data to a remote device.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-AVCastController-sendCustomData(data: Record<string, Object>): Promise<void>--><!--Device-AVCastController-sendCustomData(data: Record<string, Object>): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| data | [Record](../../apis-na/arkts-apis/arkts-na-record-t.md)&lt;string, Object&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) |

## start

```TypeScript
start(item: AVQueueItem, callback: AsyncCallback<void>): void
```

Play the current item, should contain mediaUri otherwise the playback will fail.

**Since:** 23

<!--Device-AVCastController-start(item: AVQueueItem, callback: AsyncCallback<void>): void--><!--Device-AVCastController-start(item: AVQueueItem, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| item | [AVQueueItem](arkts-avsession-avsession-avqueueitem-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) |
| [6600109](../errorcode-avsession.md#6600109-remote-session-does-not-exist) |

## start

```TypeScript
start(item: AVQueueItem): Promise<void>
```

Play the current item, should contain mediaUri otherwise the playback will fail.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVCastController-start(item: AVQueueItem): Promise<void>--><!--Device-AVCastController-start(item: AVQueueItem): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| item | [AVQueueItem](arkts-avsession-avsession-avqueueitem-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) |
| [6600109](../errorcode-avsession.md#6600109-remote-session-does-not-exist) |
