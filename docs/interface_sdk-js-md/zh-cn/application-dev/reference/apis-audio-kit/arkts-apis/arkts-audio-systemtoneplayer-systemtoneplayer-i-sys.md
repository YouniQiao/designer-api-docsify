# SystemTonePlayer（系统接口）

系统提示音播放器提供了短信提示音、通知提示音的播放、配置、获取信息等功能。在调用SystemTonePlayer的接口前，需要先通过 [getSystemTonePlayer](arkts-audio-systemsoundmanager-systemsoundmanager-i-sys.md#getsystemtoneplayer) 创建实例。

**起始版本：** 11

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**系统接口：** 此接口为系统接口。

## getAudioVolumeScale

```TypeScript
getAudioVolumeScale(): number
```

获取当前音频音量大小，同步返回当前音量。

**起始版本：** 13

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

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| systemSoundManager.ToneHapticsFeature |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [20700003](../errorcode-audio-ringtone-sys.md#20700003-操作不支持) |

## getSupportedHapticsFeatures

```TypeScript
getSupportedHapticsFeatures(): Promise<Array<systemSoundManager.ToneHapticsFeature>>
```

获取当前支持的振动风格。使用Promise异步回调。

**起始版本：** 13

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;systemSoundManager.ToneHapticsFeature & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [20700003](../errorcode-audio-ringtone-sys.md#20700003-操作不支持) |

## getTitle

```TypeScript
getTitle(): Promise<string>
```

获取提示音标题。使用Promise异步回调。

**起始版本：** 11

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [5400103](../../apis-media-kit/errorcode-media.md#5400103-出现io错误) |

## off('playFinished')

```TypeScript
off(type: 'playFinished', callback?: Callback<number>): void
```

取消监听铃音播放完成事件。使用callback异步回调。

**起始版本：** 18

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'playFinished' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [20700002](../errorcode-audio-ringtone-sys.md#20700002-参数检查失败) |

## off('error')

```TypeScript
off(type: 'error', callback?: ErrorCallback): void
```

取消监听铃音播放过程中的错误事件。使用callback异步回调。

**起始版本：** 18

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'error' | 是 |
| callback | [ErrorCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [20700002](../errorcode-audio-ringtone-sys.md#20700002-参数检查失败) |

## on('playFinished')

```TypeScript
on(type: 'playFinished', streamId: number, callback: Callback<number>): void
```

监听铃音播放完成事件（当铃音播放完成时触发）。使用callback异步回调。监听对象为传入的streamId对应音频流。当streamId传入0时，监听本播放器对应的所有音频流。

**起始版本：** 18

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'playFinished' | 是 |
| streamId | number | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [20700002](../errorcode-audio-ringtone-sys.md#20700002-参数检查失败) |

## on('error')

```TypeScript
on(type: 'error', callback: ErrorCallback): void
```

监听铃音播放过程中的错误事件（当铃音播放过程中发生错误时触发）。使用callback异步回调。

**起始版本：** 18

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'error' | 是 |
| callback | [ErrorCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [20700002](../errorcode-audio-ringtone-sys.md#20700002-参数检查失败) |

## prepare

```TypeScript
prepare(): Promise<void>
```

准备播放提示音。使用Promise异步回调。

**起始版本：** 11

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [5400102](../../apis-media-kit/errorcode-media.md#5400102-当前状态不支持此操作) |
| [5400103](../../apis-media-kit/errorcode-media.md#5400103-出现io错误) |

## release

```TypeScript
release(): Promise<void>
```

释放提示音播放器。使用Promise异步回调。

**起始版本：** 11

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

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

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| scale | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [5400102](../../apis-media-kit/errorcode-media.md#5400102-当前状态不支持此操作) |
| [20700002](../errorcode-audio-ringtone-sys.md#20700002-参数检查失败) |

## setHapticsFeature

```TypeScript
setHapticsFeature(hapticsFeature: systemSoundManager.ToneHapticsFeature): void
```

设置播放铃音时的振动风格。调用本接口前，应该先调用[getSupportedHapticsFeatures](#getsupportedhapticsfeatures)查询 支持的振动风格，如果设置不支持的振动风格，则设置失败。

**起始版本：** 13

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| hapticsFeature | systemSoundManager.ToneHapticsFeature | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [5400102](../../apis-media-kit/errorcode-media.md#5400102-当前状态不支持此操作) |
| [20700003](../errorcode-audio-ringtone-sys.md#20700003-操作不支持) |

## start

```TypeScript
start(toneOptions?: SystemToneOptions): Promise<number>
```

开始播放提示音。使用Promise异步回调。

**起始版本：** 11

**需要权限：** ohos.permission.VIBRATE

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| toneOptions | [SystemToneOptions](arkts-audio-systemtoneplayer-systemtoneoptions-i-sys.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [5400102](../../apis-media-kit/errorcode-media.md#5400102-当前状态不支持此操作) |

## stop

```TypeScript
stop(id: number): Promise<void>
```

停止播放提示音。使用Promise异步回调。

**起始版本：** 11

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| id | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [5400102](../../apis-media-kit/errorcode-media.md#5400102-当前状态不支持此操作) |
