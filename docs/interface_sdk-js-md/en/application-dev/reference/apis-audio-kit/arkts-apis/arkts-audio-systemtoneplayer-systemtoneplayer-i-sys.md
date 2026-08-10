# SystemTonePlayer (System API)

系统提示音播放器提供了短信提示音、通知提示音的播放、配置、获取信息等功能。在调用SystemTonePlayer的接口前，需要先通过  
[getSystemTonePlayer](arkts-audio-systemsoundmanager-systemsoundmanager-i.md#getsystemtoneplayer)创建实例。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-unnamed-export declare interface SystemTonePlayer--><!--Device-unnamed-export declare interface SystemTonePlayer-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**System API:** This is a system API.

## getAudioVolumeScale

ArkTS-Dyn:
```TypeScript
getAudioVolumeScale(): number
```

ArkTS-Sta:
```TypeScript
getAudioVolumeScale(): double
```

获取当前音频音量大小，同步返回当前音量。

**Since:** 13

**ArkTS mode:** ArkTS-Dyn since version 13; ArkTS-Sta since version 23.

<!--Device-SystemTonePlayer-getAudioVolumeScale(): double--><!--Device-SystemTonePlayer-getAudioVolumeScale(): double-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：double | 当前音频音量，音量范围为[0, 1]。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 202 | Caller is not a system application. |

## getHapticsFeature

```TypeScript
getHapticsFeature(): systemSoundManager.ToneHapticsFeature
```

获取播放铃音时的振动风格，同步返回振动风格枚举值。

**Since:** 13

**ArkTS mode:** ArkTS-Dyn since version 13; ArkTS-Sta since version 23.

<!--Device-SystemTonePlayer-getHapticsFeature(): systemSoundManager.ToneHapticsFeature--><!--Device-SystemTonePlayer-getHapticsFeature(): systemSoundManager.ToneHapticsFeature-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| systemSoundManager.ToneHapticsFeature | 振动风格。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 20700003 | Unsupported operation. |
| 202 | Caller is not a system application. |

## getSupportedHapticsFeatures

```TypeScript
getSupportedHapticsFeatures(): Promise<Array<systemSoundManager.ToneHapticsFeature>>
```

获取当前支持的振动风格。使用Promise异步回调。

**Since:** 13

**ArkTS mode:** ArkTS-Dyn since version 13; ArkTS-Sta since version 23.

<!--Device-SystemTonePlayer-getSupportedHapticsFeatures(): Promise<Array<systemSoundManager.ToneHapticsFeature>>--><!--Device-SystemTonePlayer-getSupportedHapticsFeatures(): Promise<Array<systemSoundManager.ToneHapticsFeature>>-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;systemSoundManager.ToneHapticsFeature&gt;&gt; | Promise对象，返回当前支持的振动风格。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 20700003 | Unsupported operation. |
| 202 | Caller is not a system application. |

## getTitle

```TypeScript
getTitle(): Promise<string>
```

获取提示音标题。使用Promise异步回调。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-SystemTonePlayer-getTitle(): Promise<string>--><!--Device-SystemTonePlayer-getTitle(): Promise<string>-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;string&gt; | Promise对象，返回获取的系统提示音标题。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 5400103 | I/O error. |
| 202 | Caller is not a system application. |

## off('playFinished')

```TypeScript
off(type: 'playFinished', callback?: Callback<int>): void
```

取消监听铃音播放完成事件。使用callback异步回调。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

<!--Device-SystemTonePlayer-off(type: 'playFinished', callback?: Callback<int>): void--><!--Device-SystemTonePlayer-off(type: 'playFinished', callback?: Callback<int>): void-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'playFinished' | Yes | 事件回调类型，支持的事件为'playFinished'，当取消监听铃音播放完成事件时，触发该事件。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;int&gt; | No | 回调函数，返回结束事件的音频流的streamId。不填入此参数时，会取消该事件的所有监听。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 20700002 | Parameter check error. |
| 202 | Not system App. |

## off('error')

```TypeScript
off(type: 'error', callback?: ErrorCallback): void
```

取消监听铃音播放过程中的错误事件。使用callback异步回调。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

<!--Device-SystemTonePlayer-off(type: 'error', callback?: ErrorCallback): void--><!--Device-SystemTonePlayer-off(type: 'error', callback?: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'error' | Yes | 事件回调类型，支持的事件为'error'，当取消监听铃音播放过程中的错误事件时，触发该事件。 |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | No | 回调函数，返回错误码和错误信息。不填入此参数时，会取消该事件的所有监听。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 20700002 | Parameter check error. |
| 202 | Not system App. |

## offError

```TypeScript
offError(callback?: ErrorCallback): void
```

取消监听铃音播放过程中的错误事件。使用callback异步回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-SystemTonePlayer-offError(callback?: ErrorCallback): void--><!--Device-SystemTonePlayer-offError(callback?: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | No | Error callback while receiving the error event. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 20700002 | Parameter check error. |
| 202 | Not system App. |

## offPlayFinished

```TypeScript
offPlayFinished(callback?: Callback<int>): void
```

取消监听铃音播放完成事件。使用callback异步回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-SystemTonePlayer-offPlayFinished(callback?: Callback<int>): void--><!--Device-SystemTonePlayer-offPlayFinished(callback?: Callback<int>): void-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;int&gt; | No | Callback used to obtain the finished event. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 20700002 | Parameter check error. |
| 202 | Not system App. |

## on('playFinished')

```TypeScript
on(type: 'playFinished', streamId: int, callback: Callback<int>): void
```

监听铃音播放完成事件（当铃音播放完成时触发）。使用callback异步回调。

监听对象为传入的streamId对应音频流。当streamId传入0时，监听本播放器对应的所有音频流。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

<!--Device-SystemTonePlayer-on(type: 'playFinished', streamId: int, callback: Callback<int>): void--><!--Device-SystemTonePlayer-on(type: 'playFinished', streamId: int, callback: Callback<int>): void-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'playFinished' | Yes | 事件回调类型，支持的事件为'playFinished'，当铃音播放完成时，触发该事件。 |
| streamId | int | Yes | 监听对象为指定streamId对应的音频流，streamId通过[start](arkts-audio-systemtoneplayer-systemtoneplayer-i-sys.md#start)获取。 当streamId传入0时，可监听当前播放器对应的所有音频流。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;int&gt; | Yes | 'playFinished'的回调方法。返回播放完成的音频流的streamId。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 20700002 | Parameter check error. |
| 202 | Not system App. |

## on('error')

```TypeScript
on(type: 'error', callback: ErrorCallback): void
```

监听铃音播放过程中的错误事件（当铃音播放过程中发生错误时触发）。使用callback异步回调。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

<!--Device-SystemTonePlayer-on(type: 'error', callback: ErrorCallback): void--><!--Device-SystemTonePlayer-on(type: 'error', callback: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'error' | Yes | 事件回调类型，支持的事件为'error'，当铃音播放过程中发生错误时，触发该事件。 |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | Yes | 回调函数，返回错误码和错误信息。错误码请参考AVPlayer的 [on('error')](@ohos.multimedia.media:media.AVPlayer.on(type: 'error', callback: ErrorCallback))。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 20700002 | Parameter check error. |
| 202 | Not system App. |

## onError

```TypeScript
onError(callback: ErrorCallback): void
```

监听铃音播放过程中的错误事件（当铃音播放过程中发生错误时触发）。使用callback异步回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-SystemTonePlayer-onError(callback: ErrorCallback): void--><!--Device-SystemTonePlayer-onError(callback: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | Yes | Error callback while receiving the error event. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 20700002 | Parameter check error. |
| 202 | Not system App. |

## onPlayFinished

```TypeScript
onPlayFinished(streamId: int, callback: Callback<int>): void
```

监听铃音播放完成事件（当铃音播放完成时触发）。使用callback异步回调。

监听对象为传入的streamId对应音频流。当streamId传入0时，监听本播放器对应的所有音频流。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-SystemTonePlayer-onPlayFinished(streamId: int, callback: Callback<int>): void--><!--Device-SystemTonePlayer-onPlayFinished(streamId: int, callback: Callback<int>): void-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| streamId | int | Yes | Stream id, received from start(). |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;int&gt; | Yes | Callback used to obtain the finished event. The callback info is the stream id that is finished. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 20700002 | Parameter check error. |
| 202 | Not system App. |

## prepare

```TypeScript
prepare(): Promise<void>
```

准备播放提示音。使用Promise异步回调。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-SystemTonePlayer-prepare(): Promise<void>--><!--Device-SystemTonePlayer-prepare(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 5400102 | Operation not allowed. |
| 5400103 | I/O error. |
| 202 | Caller is not a system application. |

## release

```TypeScript
release(): Promise<void>
```

释放提示音播放器。使用Promise异步回调。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-SystemTonePlayer-release(): Promise<void>--><!--Device-SystemTonePlayer-release(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 202 | Caller is not a system application. |

## setAudioVolumeScale

ArkTS-Dyn:
```TypeScript
setAudioVolumeScale(scale: number): void
```

ArkTS-Sta:
```TypeScript
setAudioVolumeScale(scale: double): void
```

设置音频音量大小，无返回结果。

**Since:** 13

**ArkTS mode:** ArkTS-Dyn since version 13; ArkTS-Sta since version 23.

<!--Device-SystemTonePlayer-setAudioVolumeScale(scale: double): void--><!--Device-SystemTonePlayer-setAudioVolumeScale(scale: double): void-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| scale | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | 音频音量大小，必须在[0, 1]之间取值。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 5400102 | Operation not allowed. |
| 20700002 | Parameter check error. For example, value is outside [0,1]. |
| 202 | Caller is not a system application. |

## setHapticsFeature

```TypeScript
setHapticsFeature(hapticsFeature: systemSoundManager.ToneHapticsFeature): void
```

设置播放铃音时的振动风格。

调用本接口前，应该先调用[getSupportedHapticsFeatures](arkts-audio-systemtoneplayer-systemtoneplayer-i-sys.md#getsupportedhapticsfeatures)查询支持的振动风格，如果设置不支持的振动风格，则设置失败。

**Since:** 13

**ArkTS mode:** ArkTS-Dyn since version 13; ArkTS-Sta since version 23.

<!--Device-SystemTonePlayer-setHapticsFeature(hapticsFeature: systemSoundManager.ToneHapticsFeature): void--><!--Device-SystemTonePlayer-setHapticsFeature(hapticsFeature: systemSoundManager.ToneHapticsFeature): void-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| hapticsFeature | systemSoundManager.ToneHapticsFeature | Yes | 振动风格。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 5400102 | Operation not allowed. |
| 20700003 | Unsupported operation. |
| 202 | Caller is not a system application. |

## start

ArkTS-Dyn:
```TypeScript
start(toneOptions?: SystemToneOptions): Promise<number>
```

ArkTS-Sta:
```TypeScript
start(toneOptions?: SystemToneOptions): Promise<int>
```

开始播放提示音。使用Promise异步回调。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.VIBRATE

<!--Device-SystemTonePlayer-start(toneOptions?: SystemToneOptions): Promise<int>--><!--Device-SystemTonePlayer-start(toneOptions?: SystemToneOptions): Promise<int>-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| toneOptions | [SystemToneOptions](arkts-audio-systemsoundmanager-systemtoneoptions-t.md) | No | 系统提示音选项。 |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: Promise&lt;number&gt;  <br>ArkTS-Sta：Promise&lt;int&gt; | Promise对象，返回streamID。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 5400102 | Operation not allowed. |
| 201 | Permission denied. |
| 202 | Caller is not a system application. |

## stop

ArkTS-Dyn:
```TypeScript
stop(id: number): Promise<void>
```

ArkTS-Sta:
```TypeScript
stop(id: int): Promise<void>
```

停止播放提示音。使用Promise异步回调。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-SystemTonePlayer-stop(id: int): Promise<void>--><!--Device-SystemTonePlayer-stop(id: int): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| id | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Promise对象，返回streamID。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise回调返回停止播放成功或失败。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 5400102 | Operation not allowed. |
| 202 | Caller is not a system application. |

