# SystemTonePlayer（系统接口）

系统提示音播放器提供了短信提示音、通知提示音的播放、配置、获取信息等功能。在调用SystemTonePlayer的接口前，需要先通过  
[getSystemTonePlayer](arkts-audio-systemsoundmanager-systemsoundmanager-i.md#getsystemtoneplayer)创建实例。

**起始版本：** 11

<!--Device-unnamed-export declare interface SystemTonePlayer--><!--Device-unnamed-export declare interface SystemTonePlayer-End-->

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**系统接口：** 此接口为系统接口。

## getAudioVolumeScale

```TypeScript
getAudioVolumeScale(): number
```

获取当前音频音量大小，同步返回当前音量。

**起始版本：** 13

<!--Device-SystemTonePlayer-getAudioVolumeScale(): double--><!--Device-SystemTonePlayer-getAudioVolumeScale(): double-End-->

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## getHapticsFeature

```TypeScript
getHapticsFeature(): systemSoundManager.ToneHapticsFeature
```

获取播放铃音时的振动风格，同步返回振动风格枚举值。

**起始版本：** 13

<!--Device-SystemTonePlayer-getHapticsFeature(): systemSoundManager.ToneHapticsFeature--><!--Device-SystemTonePlayer-getHapticsFeature(): systemSoundManager.ToneHapticsFeature-End-->

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| systemSoundManager.ToneHapticsFeature |

**错误码：**

| 错误码ID |
| --- |
| [20700003](../errorcode-audio-ringtone-sys.md#20700003-操作不支持) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## getSupportedHapticsFeatures

```TypeScript
getSupportedHapticsFeatures(): Promise<Array<systemSoundManager.ToneHapticsFeature>>
```

获取当前支持的振动风格。使用Promise异步回调。

**起始版本：** 13

<!--Device-SystemTonePlayer-getSupportedHapticsFeatures(): Promise<Array<systemSoundManager.ToneHapticsFeature>>--><!--Device-SystemTonePlayer-getSupportedHapticsFeatures(): Promise<Array<systemSoundManager.ToneHapticsFeature>>-End-->

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;systemSoundManager.ToneHapticsFeature&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [20700003](../errorcode-audio-ringtone-sys.md#20700003-操作不支持) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## getTitle

```TypeScript
getTitle(): Promise<string>
```

获取提示音标题。使用Promise异步回调。

**起始版本：** 11

<!--Device-SystemTonePlayer-getTitle(): Promise<string>--><!--Device-SystemTonePlayer-getTitle(): Promise<string>-End-->

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise&lt;string&gt; |

**错误码：**

| 错误码ID |
| --- |
| [5400103](../../apis-media-kit/errorcode-media.md#5400103-出现io错误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## off('playFinished')

```TypeScript
off(type: 'playFinished', callback?: Callback<number>): void
```

取消监听铃音播放完成事件。使用callback异步回调。

**起始版本：** 18

<!--Device-SystemTonePlayer-off(type: 'playFinished', callback?: Callback<int>): void--><!--Device-SystemTonePlayer-off(type: 'playFinished', callback?: Callback<int>): void-End-->

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'playFinished' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [20700002](../errorcode-audio-ringtone-sys.md#20700002-参数检查失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## off('error')

```TypeScript
off(type: 'error', callback?: ErrorCallback): void
```

取消监听铃音播放过程中的错误事件。使用callback异步回调。

**起始版本：** 18

<!--Device-SystemTonePlayer-off(type: 'error', callback?: ErrorCallback): void--><!--Device-SystemTonePlayer-off(type: 'error', callback?: ErrorCallback): void-End-->

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'error' | 是 |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [20700002](../errorcode-audio-ringtone-sys.md#20700002-参数检查失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## on('playFinished')

```TypeScript
on(type: 'playFinished', streamId: number, callback: Callback<number>): void
```

监听铃音播放完成事件（当铃音播放完成时触发）。使用callback异步回调。

监听对象为传入的streamId对应音频流。当streamId传入0时，监听本播放器对应的所有音频流。

**起始版本：** 18

<!--Device-SystemTonePlayer-on(type: 'playFinished', streamId: int, callback: Callback<int>): void--><!--Device-SystemTonePlayer-on(type: 'playFinished', streamId: int, callback: Callback<int>): void-End-->

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'playFinished' | 是 |
| streamId | number | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [20700002](../errorcode-audio-ringtone-sys.md#20700002-参数检查失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## on('error')

```TypeScript
on(type: 'error', callback: ErrorCallback): void
```

监听铃音播放过程中的错误事件（当铃音播放过程中发生错误时触发）。使用callback异步回调。

**起始版本：** 18

<!--Device-SystemTonePlayer-on(type: 'error', callback: ErrorCallback): void--><!--Device-SystemTonePlayer-on(type: 'error', callback: ErrorCallback): void-End-->

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'error' | 是 |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [20700002](../errorcode-audio-ringtone-sys.md#20700002-参数检查失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## prepare

```TypeScript
prepare(): Promise<void>
```

准备播放提示音。使用Promise异步回调。

**起始版本：** 11

<!--Device-SystemTonePlayer-prepare(): Promise<void>--><!--Device-SystemTonePlayer-prepare(): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [5400102](../../apis-media-kit/errorcode-media.md#5400102-当前状态不支持此操作) |
| [5400103](../../apis-media-kit/errorcode-media.md#5400103-出现io错误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## release

```TypeScript
release(): Promise<void>
```

释放提示音播放器。使用Promise异步回调。

**起始版本：** 11

<!--Device-SystemTonePlayer-release(): Promise<void>--><!--Device-SystemTonePlayer-release(): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## setAudioVolumeScale

```TypeScript
setAudioVolumeScale(scale: number): void
```

设置音频音量大小，无返回结果。

**起始版本：** 13

<!--Device-SystemTonePlayer-setAudioVolumeScale(scale: double): void--><!--Device-SystemTonePlayer-setAudioVolumeScale(scale: double): void-End-->

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| scale | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [5400102](../../apis-media-kit/errorcode-media.md#5400102-当前状态不支持此操作) |
| [20700002](../errorcode-audio-ringtone-sys.md#20700002-参数检查失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## setHapticsFeature

```TypeScript
setHapticsFeature(hapticsFeature: systemSoundManager.ToneHapticsFeature): void
```

设置播放铃音时的振动风格。

调用本接口前，应该先调用[getSupportedHapticsFeatures](arkts-audio-systemtoneplayer-systemtoneplayer-i-sys.md#getsupportedhapticsfeatures)查询支持的振动风格，如果设置不支持的振动风格，则设置失败。

**起始版本：** 13

<!--Device-SystemTonePlayer-setHapticsFeature(hapticsFeature: systemSoundManager.ToneHapticsFeature): void--><!--Device-SystemTonePlayer-setHapticsFeature(hapticsFeature: systemSoundManager.ToneHapticsFeature): void-End-->

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| hapticsFeature | systemSoundManager.ToneHapticsFeature | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [5400102](../../apis-media-kit/errorcode-media.md#5400102-当前状态不支持此操作) |
| [20700003](../errorcode-audio-ringtone-sys.md#20700003-操作不支持) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## start

```TypeScript
start(toneOptions?: SystemToneOptions): Promise<number>
```

开始播放提示音。使用Promise异步回调。

**起始版本：** 11

**需要权限：** ohos.permission.VIBRATE

<!--Device-SystemTonePlayer-start(toneOptions?: SystemToneOptions): Promise<int>--><!--Device-SystemTonePlayer-start(toneOptions?: SystemToneOptions): Promise<int>-End-->

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| toneOptions | [SystemToneOptions](arkts-audio-systemsoundmanager-systemtoneoptions-t.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;number&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [5400102](../../apis-media-kit/errorcode-media.md#5400102-当前状态不支持此操作) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## stop

```TypeScript
stop(id: number): Promise<void>
```

停止播放提示音。使用Promise异步回调。

**起始版本：** 11

<!--Device-SystemTonePlayer-stop(id: int): Promise<void>--><!--Device-SystemTonePlayer-stop(id: int): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| id | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [5400102](../../apis-media-kit/errorcode-media.md#5400102-当前状态不支持此操作) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
