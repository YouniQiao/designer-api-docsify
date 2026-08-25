# SystemSoundManager（系统接口）

管理系统声音。在调用SystemSoundManager的接口前，需要先 通过[getSystemSoundManager](arkts-audio-systemsoundmanager-getsystemsoundmanager-f-sys.md)创建实例。

**起始版本：** 10

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { systemSoundManager } from 'kits/@kit.AudioKit';
```

## addCustomizedTone

```TypeScript
addCustomizedTone(context: BaseContext, toneAttr: ToneAttrs, externalUri: string): Promise<string>
```

通过铃音uri将自定义铃音添加到铃音库。使用Promise异步回调。

**起始版本：** 12

**需要权限：** ohos.permission.WRITE_RINGTONE

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | 是 |
| toneAttr | [ToneAttrs](arkts-audio-systemsoundmanager-toneattrs-i-sys.md) | 是 |
| externalUri | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [5400102](../../apis-media-kit/errorcode-media.md#5400102-当前状态不支持此操作) |
| [5400103](../../apis-media-kit/errorcode-media.md#5400103-出现io错误) |
| [20700004](../errorcode-audio-ringtone-sys.md#20700004-数据大小超过限制) |
| [20700005](../errorcode-audio-ringtone-sys.md#20700005-文件个数超过限制) |
| [20700006](../errorcode-audio-ringtone-sys.md#20700006-rom空间不足) |

## addCustomizedTone

```TypeScript
addCustomizedTone(context: BaseContext, toneAttr: ToneAttrs, fd: number, offset?: number, length?: number)
      : Promise<string>
```

通过文件描述符fd将自定义铃音添加到铃音库。使用Promise异步回调。

**起始版本：** 12

**需要权限：** ohos.permission.WRITE_RINGTONE

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | 是 |
| toneAttr | [ToneAttrs](arkts-audio-systemsoundmanager-toneattrs-i-sys.md) | 是 |
| fd | number | 是 |
| offset | number | 否 |
| length | number | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [5400102](../../apis-media-kit/errorcode-media.md#5400102-当前状态不支持此操作) |
| [5400103](../../apis-media-kit/errorcode-media.md#5400103-出现io错误) |
| [20700004](../errorcode-audio-ringtone-sys.md#20700004-数据大小超过限制) |
| [20700005](../errorcode-audio-ringtone-sys.md#20700005-文件个数超过限制) |
| [20700006](../errorcode-audio-ringtone-sys.md#20700006-rom空间不足) |

## close

```TypeScript
close(fd: number): Promise<void>
```

关闭闹铃文件。使用Promise异步回调。

**起始版本：** 12

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fd | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [5400103](../../apis-media-kit/errorcode-media.md#5400103-出现io错误) |

## getAlarmToneAttrList

```TypeScript
getAlarmToneAttrList(context: BaseContext): Promise<ToneAttrsArray>
```

获取全部闹铃属性列表。使用Promise异步回调。

**起始版本：** 12

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ToneAttrsArray](arkts-audio-systemsoundmanager-toneattrsarray-t-sys.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [5400103](../../apis-media-kit/errorcode-media.md#5400103-出现io错误) |

## getAlarmToneUri

```TypeScript
getAlarmToneUri(context: BaseContext): Promise<string>
```

获取系统当前闹铃uri。使用Promise异步回调。

**起始版本：** 12

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [5400103](../../apis-media-kit/errorcode-media.md#5400103-出现io错误) |

## getCurrentRingtoneAttribute

```TypeScript
getCurrentRingtoneAttribute(type: RingtoneType): Promise<ToneAttrs>
```

获取正在使用的铃声属性。使用Promise异步回调。

**起始版本：** 20

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | [RingtoneType](arkts-audio-systemsoundmanager-ringtonetype-e-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ToneAttrs](arkts-audio-systemsoundmanager-toneattrs-i-sys.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [5400103](../../apis-media-kit/errorcode-media.md#5400103-出现io错误) |

## getDefaultAlarmToneAttrs

```TypeScript
getDefaultAlarmToneAttrs(context: BaseContext): Promise<ToneAttrs>
```

获取系统闹铃的属性。使用Promise异步回调。

**起始版本：** 12

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ToneAttrs](arkts-audio-systemsoundmanager-toneattrs-i-sys.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [5400103](../../apis-media-kit/errorcode-media.md#5400103-出现io错误) |

## getDefaultRingtoneAttrs

```TypeScript
getDefaultRingtoneAttrs(context: BaseContext, type: RingtoneType): Promise<ToneAttrs>
```

获取系统铃声的属性。使用Promise异步回调。

**起始版本：** 12

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | 是 |
| type | [RingtoneType](arkts-audio-systemsoundmanager-ringtonetype-e-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ToneAttrs](arkts-audio-systemsoundmanager-toneattrs-i-sys.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [5400103](../../apis-media-kit/errorcode-media.md#5400103-出现io错误) |

## getDefaultSystemToneAttrs

```TypeScript
getDefaultSystemToneAttrs(context: BaseContext, type: SystemToneType): Promise<ToneAttrs>
```

获取系统提示音的属性。使用Promise异步回调。

**起始版本：** 12

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | 是 |
| type | [SystemToneType](arkts-audio-systemsoundmanager-systemtonetype-e-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ToneAttrs](arkts-audio-systemsoundmanager-toneattrs-i-sys.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [5400103](../../apis-media-kit/errorcode-media.md#5400103-出现io错误) |

## getHapticsAttrsSyncedWithTone

```TypeScript
getHapticsAttrsSyncedWithTone(context: BaseContext, toneUri: string): Promise<ToneHapticsAttrs>
```

获取与指定铃音同步的振动属性。使用Promise异步回调。

**起始版本：** 14

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | 是 |
| toneUri | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ToneHapticsAttrs](arkts-audio-systemsoundmanager-tonehapticsattrs-i-sys.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [5400102](../../apis-media-kit/errorcode-media.md#5400102-当前状态不支持此操作) |
| [5400103](../../apis-media-kit/errorcode-media.md#5400103-出现io错误) |
| [20700003](../errorcode-audio-ringtone-sys.md#20700003-操作不支持) |

## getMockHapticRingtonePlayer

```TypeScript
getMockHapticRingtonePlayer(
      context: BaseContext, type: RingtoneType, ringtoneUri: string): Promise<RingtonePlayer | null>
```

获取模拟触觉铃声播放器，根据指定的铃声类型和铃音文件URI，播放该铃音文件对应的振动文件及其模拟触觉声音文件。使用Promise异步回调。

> **说明：**&gt;
> - 调用该接口前，请确保传入的ringtoneUri在系统中存在，否则会出现异常和错误。例如无法播放匹配的触觉声音文件。&gt;
> - 通过该接口获取实例后，在服务终止时需主动调用RingtonePlayer的
> [release](arkts-audio-ringtoneplayer-ringtoneplayer-i-sys.md#release)方法释放播放器资源。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | 是 |
| type | [RingtoneType](arkts-audio-systemsoundmanager-ringtonetype-e-sys.md) | 是 |
| [ringtoneUri](../../apis-notification-kit/arkts-apis/arkts-notification-notificationmanager-ringtoneinfo-i-sys.md) | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;RingtonePlayer \ | null & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [20700002](../errorcode-audio-ringtone-sys.md#20700002-参数检查失败) |
| [5400103](../../apis-media-kit/errorcode-media.md#5400103-出现io错误) |

## getMockHapticRingtonePlayer

```TypeScript
getMockHapticRingtonePlayer(context: BaseContext, hapticUri: string): Promise<RingtonePlayer | null>
```

获取模拟触觉铃声播放器，根据指定的触觉文件URI播放振动文件及其对应的模拟触觉声音文件。使用Promise异步回调。

> **说明：**&gt;
> - 调用该接口前，请确保传入的hapticUri在系统中存在，否则会出现异常和错误。例如无法播放匹配的触觉声音文件。&gt;
> - 通过该接口获取实例后，在服务终止时需主动调用RingtonePlayer的
> [release](arkts-audio-ringtoneplayer-ringtoneplayer-i-sys.md#release)方法释放播放器资源。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | 是 |
| hapticUri | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;RingtonePlayer \ | null & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [20700002](../errorcode-audio-ringtone-sys.md#20700002-参数检查失败) |
| [5400103](../../apis-media-kit/errorcode-media.md#5400103-出现io错误) |

## getRingtoneAttrList

```TypeScript
getRingtoneAttrList(context: BaseContext, type: RingtoneType): Promise<ToneAttrsArray>
```

获取系统铃声的属性列表。使用Promise异步回调。

**起始版本：** 12

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | 是 |
| type | [RingtoneType](arkts-audio-systemsoundmanager-ringtonetype-e-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ToneAttrsArray](arkts-audio-systemsoundmanager-toneattrsarray-t-sys.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [5400103](../../apis-media-kit/errorcode-media.md#5400103-出现io错误) |

## getRingtonePlayer

```TypeScript
getRingtonePlayer(context: BaseContext, type: RingtoneType): Promise<RingtonePlayer>
```

获取系统铃声播放器。使用Promise异步回调。

**起始版本：** 11

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | 是 |
| type | [RingtoneType](arkts-audio-systemsoundmanager-ringtonetype-e-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;RingtonePlayer & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## getRingtoneUri

```TypeScript
getRingtoneUri(context: BaseContext, type: RingtoneType): Promise<string>
```

获取系统铃声uri。使用Promise异步回调。

**起始版本：** 11

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | 是 |
| type | [RingtoneType](arkts-audio-systemsoundmanager-ringtonetype-e-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [5400103](../../apis-media-kit/errorcode-media.md#5400103-出现io错误) |

## getSystemRingtonePlayer

```TypeScript
getSystemRingtonePlayer(context: Context, type: RingtoneType, callback: AsyncCallback<RingtonePlayer>): void
```

获取系统铃声播放器。使用callback异步回调。

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [getRingtonePlayer](#getringtoneplayer)

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | 是 |
| type | [RingtoneType](arkts-audio-systemsoundmanager-ringtonetype-e-sys.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;RingtonePlayer&gt; | 是 |

## getSystemRingtonePlayer

```TypeScript
getSystemRingtonePlayer(context: Context, type: RingtoneType): Promise<RingtonePlayer>
```

获取系统铃声播放器。使用Promise异步回调。

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [getRingtonePlayer](#getringtoneplayer)

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | 是 |
| type | [RingtoneType](arkts-audio-systemsoundmanager-ringtonetype-e-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;RingtonePlayer & gt; |

## getSystemRingtoneUri

```TypeScript
getSystemRingtoneUri(context: Context, type: RingtoneType, callback: AsyncCallback<string>): void
```

获取系统铃声uri。使用callback异步回调。

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [getRingtoneUri](#getringtoneuri)

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | 是 |
| type | [RingtoneType](arkts-audio-systemsoundmanager-ringtonetype-e-sys.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

## getSystemRingtoneUri

```TypeScript
getSystemRingtoneUri(context: Context, type: RingtoneType): Promise<string>
```

获取系统铃声uri。使用Promise异步回调。

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [getRingtoneUri](#getringtoneuri)

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | 是 |
| type | [RingtoneType](arkts-audio-systemsoundmanager-ringtonetype-e-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

## getSystemToneAttrList

```TypeScript
getSystemToneAttrList(context: BaseContext, type: SystemToneType): Promise<ToneAttrsArray>
```

获取系统提示音的属性列表。使用Promise异步回调。

**起始版本：** 12

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | 是 |
| type | [SystemToneType](arkts-audio-systemsoundmanager-systemtonetype-e-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ToneAttrsArray](arkts-audio-systemsoundmanager-toneattrsarray-t-sys.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [5400103](../../apis-media-kit/errorcode-media.md#5400103-出现io错误) |

## getSystemTonePlayer

```TypeScript
getSystemTonePlayer(context: BaseContext, type: SystemToneType): Promise<SystemTonePlayer>
```

获取系统提示音播放器。使用Promise异步回调。

**起始版本：** 11

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | 是 |
| type | [SystemToneType](arkts-audio-systemsoundmanager-systemtonetype-e-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;SystemTonePlayer & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## getSystemToneUri

```TypeScript
getSystemToneUri(context: BaseContext, type: SystemToneType): Promise<string>
```

获取系统提示音uri。使用Promise异步回调。

**起始版本：** 11

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | 是 |
| type | [SystemToneType](arkts-audio-systemsoundmanager-systemtonetype-e-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [5400103](../../apis-media-kit/errorcode-media.md#5400103-出现io错误) |

## getToneHapticsList

```TypeScript
getToneHapticsList(context: BaseContext, isSynced: boolean): Promise<ToneHapticsAttrsArray>
```

获取同步或者非同步的系统铃音的振动属性列表。使用Promise异步回调。

**起始版本：** 14

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | 是 |
| isSynced | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ToneHapticsAttrsArray](arkts-audio-systemsoundmanager-tonehapticsattrsarray-t-sys.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [5400103](../../apis-media-kit/errorcode-media.md#5400103-出现io错误) |
| [20700003](../errorcode-audio-ringtone-sys.md#20700003-操作不支持) |

## getToneHapticsSettings

```TypeScript
getToneHapticsSettings(context: BaseContext, type: ToneHapticsType): Promise<ToneHapticsSettings>
```

获取系统铃音的振动设置。使用Promise异步回调。

**起始版本：** 14

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | 是 |
| type | [ToneHapticsType](arkts-audio-systemsoundmanager-tonehapticstype-e-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ToneHapticsSettings](arkts-audio-systemsoundmanager-tonehapticssettings-i-sys.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [5400103](../../apis-media-kit/errorcode-media.md#5400103-出现io错误) |
| [20700003](../errorcode-audio-ringtone-sys.md#20700003-操作不支持) |

## openAlarmTone

```TypeScript
openAlarmTone(context: BaseContext, uri: string): Promise<number>
```

打开闹铃文件。使用Promise异步回调。

**起始版本：** 12

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | 是 |
| uri | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [5400103](../../apis-media-kit/errorcode-media.md#5400103-出现io错误) |
| 20700001 |

## openToneHaptics

```TypeScript
openToneHaptics(context: BaseContext, hapticsUri: string): Promise<number>
```

打开系统铃音的振动。使用Promise异步回调。

**起始版本：** 14

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | 是 |
| [hapticsUri](arkts-audio-systemsoundmanager-tonehapticssettings-i-sys.md) | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [5400102](../../apis-media-kit/errorcode-media.md#5400102-当前状态不支持此操作) |
| [5400103](../../apis-media-kit/errorcode-media.md#5400103-出现io错误) |
| [20700003](../errorcode-audio-ringtone-sys.md#20700003-操作不支持) |

## openToneList

```TypeScript
openToneList(uriList: Array<string>): Promise<Array<[string, number, SystemSoundError]>>
```

获取系统铃声的属性列表。使用Promise异步回调。

**起始版本：** 20

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [uriList](../../apis-device-certificate-kit/arkts-apis/arkts-devicecertificate-certificatemanager-cmresult-i.md) | Array & lt;string & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;[string, number, SystemSoundError] & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [20700007](../errorcode-audio-ringtone-sys.md#20700007-参数无效) |

## removeCustomizedTone

```TypeScript
removeCustomizedTone(context: BaseContext, uri:string): Promise<void>
```

从铃音库中删除自定义铃音。使用Promise异步回调。

**起始版本：** 12

**需要权限：** ohos.permission.WRITE_RINGTONE

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | 是 |
| uri | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [5400102](../../apis-media-kit/errorcode-media.md#5400102-当前状态不支持此操作) |
| [5400103](../../apis-media-kit/errorcode-media.md#5400103-出现io错误) |

## removeCustomizedToneList

```TypeScript
removeCustomizedToneList(uriList: Array<string>): Promise<Array<[string, SystemSoundError]>>
```

批量删除自定义铃音列表。使用Promise异步回调。

**起始版本：** 20

**需要权限：** ohos.permission.WRITE_RINGTONE

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [uriList](../../apis-device-certificate-kit/arkts-apis/arkts-devicecertificate-certificatemanager-cmresult-i.md) | Array & lt;string & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;[string, SystemSoundError] & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [20700007](../errorcode-audio-ringtone-sys.md#20700007-参数无效) |

## setAlarmToneUri

```TypeScript
setAlarmToneUri(context: BaseContext, uri: string): Promise<void>
```

设置系统闹铃uri。使用Promise异步回调。

**起始版本：** 12

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | 是 |
| uri | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [5400103](../../apis-media-kit/errorcode-media.md#5400103-出现io错误) |
| 20700001 |

## setRingtoneUri

```TypeScript
setRingtoneUri(context: BaseContext, uri: string, type: RingtoneType): Promise<void>
```

设置系统铃声uri。使用Promise异步回调。

**起始版本：** 11

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | 是 |
| uri | string | 是 |
| type | [RingtoneType](arkts-audio-systemsoundmanager-ringtonetype-e-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [5400103](../../apis-media-kit/errorcode-media.md#5400103-出现io错误) |

## setSystemRingtoneUri

```TypeScript
setSystemRingtoneUri(context: Context, uri: string, type: RingtoneType, callback: AsyncCallback<void>): void
```

设置系统铃声uri。使用callback异步回调。

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [setRingtoneUri](#setringtoneuri)

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | 是 |
| uri | string | 是 |
| type | [RingtoneType](arkts-audio-systemsoundmanager-ringtonetype-e-sys.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## setSystemRingtoneUri

```TypeScript
setSystemRingtoneUri(context: Context, uri: string, type: RingtoneType): Promise<void>
```

设置系统铃声uri。使用Promise异步回调。

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [setRingtoneUri](#setringtoneuri)

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | 是 |
| uri | string | 是 |
| type | [RingtoneType](arkts-audio-systemsoundmanager-ringtonetype-e-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## setSystemToneUri

```TypeScript
setSystemToneUri(context: BaseContext, uri: string, type: SystemToneType): Promise<void>
```

设置系统提示音uri。使用Promise异步回调。

**起始版本：** 11

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | 是 |
| uri | string | 是 |
| type | [SystemToneType](arkts-audio-systemsoundmanager-systemtonetype-e-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [5400103](../../apis-media-kit/errorcode-media.md#5400103-出现io错误) |

## setToneHapticsSettings

```TypeScript
setToneHapticsSettings(context: BaseContext, type: ToneHapticsType, settings: ToneHapticsSettings): Promise<void>
```

设置系统铃音的振动。使用Promise异步回调。

**起始版本：** 14

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | 是 |
| type | [ToneHapticsType](arkts-audio-systemsoundmanager-tonehapticstype-e-sys.md) | 是 |
| settings | [ToneHapticsSettings](arkts-audio-systemsoundmanager-tonehapticssettings-i-sys.md) | 是 |

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
| [5400103](../../apis-media-kit/errorcode-media.md#5400103-出现io错误) |
| [20700003](../errorcode-audio-ringtone-sys.md#20700003-操作不支持) |
