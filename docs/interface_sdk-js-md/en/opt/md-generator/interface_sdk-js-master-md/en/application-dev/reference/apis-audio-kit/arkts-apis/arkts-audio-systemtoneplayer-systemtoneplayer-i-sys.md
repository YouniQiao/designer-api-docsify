# SystemTonePlayer (System API)

The module provides APIs for playing and configuring SMS tones and notification tones and obtaining related information. Before calling any API in SystemTonePlayer, you must use   
[getSystemTonePlayer](arkts-audio-systemsoundmanager-systemsoundmanager-i.md#getsystemtoneplayer)to create a SystemTonePlayer instance.

**Since:** 11

<!--Device-unnamed-export declare interface SystemTonePlayer--><!--Device-unnamed-export declare interface SystemTonePlayer-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**System API:** This is a system API.

## getAudioVolumeScale

```TypeScript
getAudioVolumeScale(): number
```

Obtains the scale of the audio volume. This API returns the result synchronously.

**Since:** 13

<!--Device-SystemTonePlayer-getAudioVolumeScale(): double--><!--Device-SystemTonePlayer-getAudioVolumeScale(): double-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## getHapticsFeature

```TypeScript
getHapticsFeature(): systemSoundManager.ToneHapticsFeature
```

Obtains the haptics style of the ringtone. This API returns the result synchronously.

**Since:** 13

<!--Device-SystemTonePlayer-getHapticsFeature(): systemSoundManager.ToneHapticsFeature--><!--Device-SystemTonePlayer-getHapticsFeature(): systemSoundManager.ToneHapticsFeature-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| systemSoundManager.ToneHapticsFeature |

**Error codes:**

| Error Code ID |
| --- |
| [20700003](../errorcode-audio-ringtone-sys.md#20700003-operation-not-supported) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## getSupportedHapticsFeatures

```TypeScript
getSupportedHapticsFeatures(): Promise<Array<systemSoundManager.ToneHapticsFeature>>
```

Obtains the supported haptics styles. This API uses a promise to return the result.

**Since:** 13

<!--Device-SystemTonePlayer-getSupportedHapticsFeatures(): Promise<Array<systemSoundManager.ToneHapticsFeature>>--><!--Device-SystemTonePlayer-getSupportedHapticsFeatures(): Promise<Array<systemSoundManager.ToneHapticsFeature>>-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;systemSoundManager.ToneHapticsFeature&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [20700003](../errorcode-audio-ringtone-sys.md#20700003-operation-not-supported) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## getTitle

```TypeScript
getTitle(): Promise<string>
```

Obtains the title of a system tone. This API uses a promise to return the result.

**Since:** 11

<!--Device-SystemTonePlayer-getTitle(): Promise<string>--><!--Device-SystemTonePlayer-getTitle(): Promise<string>-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;string&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [5400103](../../apis-media-kit/errorcode-media.md#5400103-io-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## off('playFinished')

```TypeScript
off(type: 'playFinished', callback?: Callback<number>): void
```

Unsubscribes from the event indicating that the ringtone playback is finished. This API uses an asynchronous callback to return the result.

**Since:** 18

<!--Device-SystemTonePlayer-off(type: 'playFinished', callback?: Callback<int>): void--><!--Device-SystemTonePlayer-off(type: 'playFinished', callback?: Callback<int>): void-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'playFinished' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [20700002](../errorcode-audio-ringtone-sys.md#20700002-parameter-check-failed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## off('error')

```TypeScript
off(type: 'error', callback?: ErrorCallback): void
```

Unsubscribes from error events that occur during ringtone playback. This API uses an asynchronous callback to return the result.

**Since:** 18

<!--Device-SystemTonePlayer-off(type: 'error', callback?: ErrorCallback): void--><!--Device-SystemTonePlayer-off(type: 'error', callback?: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'error' | Yes |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [20700002](../errorcode-audio-ringtone-sys.md#20700002-parameter-check-failed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## on('playFinished')

```TypeScript
on(type: 'playFinished', streamId: number, callback: Callback<number>): void
```

Subscribes to the event indicating that the ringtone playback is finished. This API uses an asynchronous callback to return the result.

The object to listen for is an audio stream specified by **streamId**. If **streamId** is set to **0**, this API subscribes to the playback complete event of all audio streams of the player.

**Since:** 18

<!--Device-SystemTonePlayer-on(type: 'playFinished', streamId: int, callback: Callback<int>): void--><!--Device-SystemTonePlayer-on(type: 'playFinished', streamId: int, callback: Callback<int>): void-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'playFinished' | Yes |
| streamId | number | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [20700002](../errorcode-audio-ringtone-sys.md#20700002-parameter-check-failed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## on('error')

```TypeScript
on(type: 'error', callback: ErrorCallback): void
```

Subscribes to error events that occur during ringtone playback. This API uses an asynchronous callback to return the result.

**Since:** 18

<!--Device-SystemTonePlayer-on(type: 'error', callback: ErrorCallback): void--><!--Device-SystemTonePlayer-on(type: 'error', callback: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'error' | Yes |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [20700002](../errorcode-audio-ringtone-sys.md#20700002-parameter-check-failed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## prepare

```TypeScript
prepare(): Promise<void>
```

Prepares to play a system tone. This API uses a promise to return the result.

**Since:** 11

<!--Device-SystemTonePlayer-prepare(): Promise<void>--><!--Device-SystemTonePlayer-prepare(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../../apis-media-kit/errorcode-media.md#5400102-unsupported-operation) |
| [5400103](../../apis-media-kit/errorcode-media.md#5400103-io-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## release

```TypeScript
release(): Promise<void>
```

Releases the system tone player. This API uses a promise to return the result.

**Since:** 11

<!--Device-SystemTonePlayer-release(): Promise<void>--><!--Device-SystemTonePlayer-release(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## setAudioVolumeScale

```TypeScript
setAudioVolumeScale(scale: number): void
```

Sets the scale of the audio volume. No result is returned.

**Since:** 13

<!--Device-SystemTonePlayer-setAudioVolumeScale(scale: double): void--><!--Device-SystemTonePlayer-setAudioVolumeScale(scale: double): void-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| scale | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [5400102](../../apis-media-kit/errorcode-media.md#5400102-unsupported-operation) |
| [20700002](../errorcode-audio-ringtone-sys.md#20700002-parameter-check-failed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## setHapticsFeature

```TypeScript
setHapticsFeature(hapticsFeature: systemSoundManager.ToneHapticsFeature): void
```

Sets a haptics style of the ringtone.

Before calling this API, call [getSupportedHapticsFeatures](arkts-audio-systemtoneplayer-systemtoneplayer-i-sys.md#getsupportedhapticsfeatures) to obtain the supported haptics styles. The setting fails if the haptics style to set is not supported.

**Since:** 13

<!--Device-SystemTonePlayer-setHapticsFeature(hapticsFeature: systemSoundManager.ToneHapticsFeature): void--><!--Device-SystemTonePlayer-setHapticsFeature(hapticsFeature: systemSoundManager.ToneHapticsFeature): void-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| hapticsFeature | systemSoundManager.ToneHapticsFeature | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [5400102](../../apis-media-kit/errorcode-media.md#5400102-unsupported-operation) |
| [20700003](../errorcode-audio-ringtone-sys.md#20700003-operation-not-supported) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## start

```TypeScript
start(toneOptions?: SystemToneOptions): Promise<number>
```

Start playing the system tone. By default, the audio and haptic will not be muted. Using tone options to mute audio or haptics. If haptics is needed, caller should have the permission of ohos.permission.VIBRATE.

**Since:** 11

**Required permissions:** ohos.permission.VIBRATE

<!--Device-SystemTonePlayer-start(toneOptions?: SystemToneOptions): Promise<int>--><!--Device-SystemTonePlayer-start(toneOptions?: SystemToneOptions): Promise<int>-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| toneOptions | [SystemToneOptions](arkts-audio-systemsoundmanager-systemtoneoptions-t.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;number&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [5400102](../../apis-media-kit/errorcode-media.md#5400102-unsupported-operation) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## stop

```TypeScript
stop(id: number): Promise<void>
```

Stops playing a system tone. This API uses a promise to return the result.

**Since:** 11

<!--Device-SystemTonePlayer-stop(id: int): Promise<void>--><!--Device-SystemTonePlayer-stop(id: int): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| id | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [5400102](../../apis-media-kit/errorcode-media.md#5400102-unsupported-operation) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
