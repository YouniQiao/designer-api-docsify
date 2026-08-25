# AsrProcessingController（系统接口）

自动语音识别（ASR）处理控制器。

**起始版本：** 12

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { audio } from 'kits/@kit.AudioKit';
```

## getAsrAecMode

```TypeScript
getAsrAecMode(): AsrAecMode
```

获取自动语音识别（ASR）的声学回声消除（AEC）模式，同步返回结果。

**起始版本：** 12

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| [AsrAecMode](arkts-audio-audio-asraecmode-e-sys.md) |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [6800104](../errorcode-audio.md#6800104-参数选项不支持) |

## getAsrNoiseSuppressionMode

```TypeScript
getAsrNoiseSuppressionMode(): AsrNoiseSuppressionMode
```

获取自动语音识别（ASR）的噪音抑制模式，同步返回结果。

**起始版本：** 12

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| [AsrNoiseSuppressionMode](arkts-audio-audio-asrnoisesuppressionmode-e-sys.md) |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [6800104](../errorcode-audio.md#6800104-参数选项不支持) |

## getAsrWhisperDetectionMode

```TypeScript
getAsrWhisperDetectionMode(): AsrWhisperDetectionMode
```

获取自动语音识别（ASR）的耳语检测模式，同步返回结果。

**起始版本：** 12

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| [AsrWhisperDetectionMode](arkts-audio-audio-asrwhisperdetectionmode-e-sys.md) |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [6800104](../errorcode-audio.md#6800104-参数选项不支持) |

## isWhispering

```TypeScript
isWhispering(): boolean
```

查询耳语状态。

**起始版本：** 12

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [6800104](../errorcode-audio.md#6800104-参数选项不支持) |

## setAsrAecMode

```TypeScript
setAsrAecMode(mode: AsrAecMode): boolean
```

设置自动语音识别（ASR）的声学回声消除（AEC）模式，同步返回结果。

**起始版本：** 12

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mode | [AsrAecMode](arkts-audio-audio-asraecmode-e-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6800101](../errorcode-audio.md#6800101-无效入参) |
| [6800104](../errorcode-audio.md#6800104-参数选项不支持) |

## setAsrNoiseSuppressionMode

```TypeScript
setAsrNoiseSuppressionMode(mode: AsrNoiseSuppressionMode): boolean
```

设置自动语音识别（ASR）的噪音抑制模式，同步返回结果。

**起始版本：** 12

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mode | [AsrNoiseSuppressionMode](arkts-audio-audio-asrnoisesuppressionmode-e-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6800101](../errorcode-audio.md#6800101-无效入参) |
| [6800104](../errorcode-audio.md#6800104-参数选项不支持) |

## setAsrVoiceControlMode

```TypeScript
setAsrVoiceControlMode(mode: AsrVoiceControlMode, enable: boolean): boolean
```

设置在系统通话中上报mode及通话录音的上行通路的自动语音识别（ASR）音频通路选择。

**起始版本：** 12

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mode | [AsrVoiceControlMode](arkts-audio-audio-asrvoicecontrolmode-e-sys.md) | 是 |
| enable | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6800101](../errorcode-audio.md#6800101-无效入参) |
| [6800104](../errorcode-audio.md#6800104-参数选项不支持) |

## setAsrVoiceMuteMode

```TypeScript
setAsrVoiceMuteMode(mode: AsrVoiceMuteMode, enable: boolean): boolean
```

在系统通话中，对自动语音识别（ASR）的音频通路进行静音控制。

**起始版本：** 12

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mode | [AsrVoiceMuteMode](arkts-audio-audio-asrvoicemutemode-e-sys.md) | 是 |
| enable | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6800101](../errorcode-audio.md#6800101-无效入参) |
| [6800104](../errorcode-audio.md#6800104-参数选项不支持) |

## setAsrWhisperDetectionMode

```TypeScript
setAsrWhisperDetectionMode(mode: AsrWhisperDetectionMode): boolean
```

设置自动语音识别（ASR）的耳语检测模式。

**起始版本：** 12

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mode | [AsrWhisperDetectionMode](arkts-audio-audio-asrwhisperdetectionmode-e-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6800101](../errorcode-audio.md#6800101-无效入参) |
| [6800104](../errorcode-audio.md#6800104-参数选项不支持) |
