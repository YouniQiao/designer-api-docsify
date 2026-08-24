# AudioVolumeManager

音量管理。在使用AudioVolumeManager的接口前，需要使用 [getVolumeManager](arkts-audio-audio-audiomanager-i.md#getvolumemanager)获取AudioVolumeManager实例。

**起始版本：** 23

<!--Device-audio-interface AudioVolumeManager--><!--Device-audio-interface AudioVolumeManager-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Volume

## 导入模块

```TypeScript
import { audio } from '@kit.AudioKit';
```

## confirmVolumeLimitExceeded

```TypeScript
confirmVolumeLimitExceeded(volumeType: AudioVolumeType, result: boolean): void
```

确认调整超出音量保护阈值的音量结果。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AudioVolumeManager-confirmVolumeLimitExceeded(volumeType: AudioVolumeType, result: boolean): void--><!--Device-AudioVolumeManager-confirmVolumeLimitExceeded(volumeType: AudioVolumeType, result: boolean): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | 是 | 音频音量类型， 不同的音量类型有不同的阈值， volumeType 用于识别当前的音量类型阈值。 |
| result | boolean | 是 | 确认音量调整已超过音量保护阈值 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) | Not system App. |
| [6800101](../errorcode-audio.md#6800101-无效入参) | Parameter verification failed. |
| [6800301](../errorcode-audio.md#6800301-系统处理异常) | System error. |

## forceVolumeKeyControlType

```TypeScript
forceVolumeKeyControlType(volumeType: AudioVolumeType, duration: int): void
```

设置音量键调节类型。

**起始版本：** 23

**需要权限：** ohos.permission.MODIFY_AUDIO_SETTINGS

<!--Device-AudioVolumeManager-forceVolumeKeyControlType(volumeType: AudioVolumeType, duration: int): void--><!--Device-AudioVolumeManager-forceVolumeKeyControlType(volumeType: AudioVolumeType, duration: int): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | 是 | 应用程序期望控制的音频音量类型。 |
| duration | int | 是 | 无音量键事件时，控制音量类型的持续时间，单位为秒（s）。<br>当计时器到期时，强制音量类型设置将被取消，最大持续时间不得超过10秒。<br>如果持续时间设置为-1，则取消该设置。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [201](../../errorcode-universal.md#201-权限校验失败) | Permission denied. |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) | Not system App. |
| [6800101](../errorcode-audio.md#6800101-无效入参) | Parameter verification failed. |
| [6800301](../errorcode-audio.md#6800301-系统处理异常) | Crash or blocking occurs in system process. |

**示例**

```TypeScript
import { audio } from '@kit.AudioKit';

let audioManager = audio.getAudioManager();
let audioVolumeManager = audioManager.getVolumeManager();

// 设置音量保持类型为响铃模式。
let volumeType = audio.AudioVolumeType.RINGTONE;
let duration = 10;
audioVolumeManager.forceVolumeKeyControlType(volumeType, duration);

// 取消音量保持类型，恢复默认音量控制。
let volumeTypeDefault = audio.AudioVolumeType.MEDIA;
let durationToCancel = -1;
audioVolumeManager.forceVolumeKeyControlType(volumeTypeDefault, durationToCancel);
```

## getActiveStreamsVolumeInfo

```TypeScript
getActiveStreamsVolumeInfo(): ActiveStreamsVolumeInfoArray
```

获取活动音频流的音量信息。

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AudioVolumeManager-getActiveStreamsVolumeInfo(): ActiveStreamsVolumeInfoArray--><!--Device-AudioVolumeManager-getActiveStreamsVolumeInfo(): ActiveStreamsVolumeInfoArray-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ActiveStreamsVolumeInfoArray](arkts-audio-audio-activestreamsvolumeinfoarray-t-sys.md) | 返回结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) | Not system App. |
| [6800301](../errorcode-audio.md#6800301-系统处理异常) | System error, crash or blocking occurs in system process. |

## getAppVolumePercentageForUid

```TypeScript
getAppVolumePercentageForUid(uid: int): Promise<int>
```

根据应用ID获取指定应用的音量百分比（范围为0到100）。使用Promise异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.MANAGE_AUDIO_CONFIG

<!--Device-AudioVolumeManager-getAppVolumePercentageForUid(uid: int): Promise<int>--><!--Device-AudioVolumeManager-getAppVolumePercentageForUid(uid: int): Promise<int>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uid | int | 是 | 表示应用ID。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;int&gt; | Promise对象，返回应用的音量百分比，范围为[0, 100]。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [201](../../errorcode-universal.md#201-权限校验失败) | Permission denied. |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) | Not system App. |
| [6800101](../errorcode-audio.md#6800101-无效入参) | Parameter verification failed. |

**示例**

```TypeScript
let uid = 20010041; // 应用ID。

audioVolumeManager.getAppVolumePercentageForUid(20010041).then((value) => {
  console.info(`app volume is ${value}.`);
});
```

## getAudioVolumeTypeByStreamUsage

```TypeScript
getAudioVolumeTypeByStreamUsage(streamUsage: StreamUsage): AudioVolumeType
```

按流类型获取卷类型。

**起始版本：** 23

<!--Device-AudioVolumeManager-getAudioVolumeTypeByStreamUsage(streamUsage: StreamUsage): AudioVolumeType--><!--Device-AudioVolumeManager-getAudioVolumeTypeByStreamUsage(streamUsage: StreamUsage): AudioVolumeType-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| streamUsage | [StreamUsage](arkts-audio-audio-streamusage-e.md) | 是 | 音频流类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | 返回音频音量类型。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) | Not system App. |
| [6800101](../errorcode-audio.md#6800101-无效入参) | Parameter verification failed. |

## getMaxSystemVolume

```TypeScript
getMaxSystemVolume(volumeType: AudioVolumeType): int
```

获取音量类型允许的最大音量大小。

**起始版本：** 23

<!--Device-AudioVolumeManager-getMaxSystemVolume(volumeType: AudioVolumeType): int--><!--Device-AudioVolumeManager-getMaxSystemVolume(volumeType: AudioVolumeType): int-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | 是 | 音量类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 最大音量。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) | Not system App. |
| [6800101](../errorcode-audio.md#6800101-无效入参) | Parameter verification failed. |

## getMinSystemVolume

```TypeScript
getMinSystemVolume(volumeType: AudioVolumeType): int
```

获取音量类型允许的最小音量大小。

**起始版本：** 23

<!--Device-AudioVolumeManager-getMinSystemVolume(volumeType: AudioVolumeType): int--><!--Device-AudioVolumeManager-getMinSystemVolume(volumeType: AudioVolumeType): int-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | 是 | 音量类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 最小音量. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) | Not system App. |
| [6800101](../errorcode-audio.md#6800101-无效入参) | Parameter verification failed. |

## getMinSystemVolumePercentage

```TypeScript
getMinSystemVolumePercentage(volumeType: AudioVolumeType): int
```

获取指定流的最小音量百分比。

**起始版本：** 23

<!--Device-AudioVolumeManager-getMinSystemVolumePercentage(volumeType: AudioVolumeType): int--><!--Device-AudioVolumeManager-getMinSystemVolumePercentage(volumeType: AudioVolumeType): int-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | 是 | 音量流类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 音量百分比，取值范围为[0, 100]。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) | Not system App. |
| [6800101](../errorcode-audio.md#6800101-无效入参) | Parameter verification failed. |

**示例**

```TypeScript
try {
  let volume = audioVolumeManager.getMinSystemVolumePercentage(audio.AudioVolumeType.MEDIA);
  console.info(`MEDIA volume percentage obtained success.`);
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to obtain the volume percentage, error: ${error}`);
}
```

## getStreamUsagesByVolumeType

```TypeScript
getStreamUsagesByVolumeType(volumeType: AudioVolumeType): StreamUsageArray
```

按音量类型获取流类型。

**起始版本：** 23

<!--Device-AudioVolumeManager-getStreamUsagesByVolumeType(volumeType: AudioVolumeType): StreamUsageArray--><!--Device-AudioVolumeManager-getStreamUsagesByVolumeType(volumeType: AudioVolumeType): StreamUsageArray-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | 是 | 音量类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [StreamUsageArray](arkts-audio-audio-streamusagearray-t-sys.md) | 返回音频流类型。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) | Not system App. |
| [6800101](../errorcode-audio.md#6800101-无效入参) | Parameter verification failed. |

## getSupportedAudioVolumeTypes

```TypeScript
getSupportedAudioVolumeTypes(): Array<Readonly<AudioVolumeType>>
```

获取系统支持的卷类型。

**起始版本：** 23

<!--Device-AudioVolumeManager-getSupportedAudioVolumeTypes(): Array<Readonly<AudioVolumeType>>--><!--Device-AudioVolumeManager-getSupportedAudioVolumeTypes(): Array<Readonly<AudioVolumeType>>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array&lt;Readonly&lt;[AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md)&gt;&gt; | 返回系统音量类型数组。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) | Not system App. |

## getSystemVolume

```TypeScript
getSystemVolume(volumeType: AudioVolumeType): int
```

取消监听系统音量变化事件。使用callback异步回调。

**起始版本：** 23

<!--Device-AudioVolumeManager-getSystemVolume(volumeType: AudioVolumeType): int--><!--Device-AudioVolumeManager-getSystemVolume(volumeType: AudioVolumeType): int-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | 是 | 音量类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 当前系统音量级别。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) | Not system App. |
| [6800101](../errorcode-audio.md#6800101-无效入参) | Parameter verification failed. |

## getSystemVolumeByUid

```TypeScript
getSystemVolumeByUid(volumeType: AudioVolumeType, callingUid: int): int
```

获取特定uid应用中的流媒体数量。

**起始版本：** 23

<!--Device-AudioVolumeManager-getSystemVolumeByUid(volumeType: AudioVolumeType, callingUid: int): int--><!--Device-AudioVolumeManager-getSystemVolumeByUid(volumeType: AudioVolumeType, callingUid: int): int-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | 是 | 音量类型。 |
| callingUid | int | 是 | 流所有者的UID。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 当前系统音量级别。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) | Not system App. |
| [6800101](../errorcode-audio.md#6800101-无效入参) | Parameter verification failed. |
| [6800301](../errorcode-audio.md#6800301-系统处理异常) | Crash or blocking occurs in system process. |

## getSystemVolumePercentage

```TypeScript
getSystemVolumePercentage(volumeType: AudioVolumeType): int
```

获取指定流的音量百分比。

**起始版本：** 23

<!--Device-AudioVolumeManager-getSystemVolumePercentage(volumeType: AudioVolumeType): int--><!--Device-AudioVolumeManager-getSystemVolumePercentage(volumeType: AudioVolumeType): int-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | 是 | 音量流类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 音量百分比，取值范围为[0, 100]。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) | Not system App. |
| [6800101](../errorcode-audio.md#6800101-无效入参) | Parameter verification failed. |

**示例**

```TypeScript
try {
  let volume = audioVolumeManager.getSystemVolumePercentage(audio.AudioVolumeType.MEDIA);
  console.info(`MEDIA volume percentage obtained success.`);
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to obtain the volume percentage, error: ${error}`);
}
```

## getVolumeGroupInfos

```TypeScript
getVolumeGroupInfos(networkId: string, callback: AsyncCallback<VolumeGroupInfos>): void
```

获取音量组信息列表。使用callback异步回调。

**起始版本：** 23

<!--Device-AudioVolumeManager-getVolumeGroupInfos(networkId: string, callback: AsyncCallback<VolumeGroupInfos>): void--><!--Device-AudioVolumeManager-getVolumeGroupInfos(networkId: string, callback: AsyncCallback<VolumeGroupInfos>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| networkId | string | 是 | 设备的网络id。本地设备audio.LOCAL_NETWORK_ID。 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[VolumeGroupInfos](arkts-audio-audio-volumegroupinfos-t-sys.md)&gt; | 是 | 回调函数。当获取音量组信息列表成功，err为undefined，data为获取到的音量组信息列表；否则为错误对象。 |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioVolumeManager.getVolumeGroupInfos(audio.LOCAL_NETWORK_ID, (err: BusinessError, value: audio.VolumeGroupInfos) => {
  if (err) {
    console.error(`Failed to obtain the volume group infos list. ${err}`);
    return;
  }
  console.info('Callback invoked to indicate that the volume group infos list is obtained.');
});
```

```TypeScript
async function getVolumeGroupInfos(){
  let volumegroupinfos: audio.VolumeGroupInfos = await audio.getAudioManager().getVolumeManager().getVolumeGroupInfos(audio.LOCAL_NETWORK_ID);
  console.info('Promise returned to indicate that the volumeGroup list is obtained.'+JSON.stringify(volumegroupinfos))
}
```

## getVolumeGroupInfos

```TypeScript
getVolumeGroupInfos(networkId: string): Promise<VolumeGroupInfos>
```

获取音量组信息列表。使用Promise异步回调。

**起始版本：** 23

<!--Device-AudioVolumeManager-getVolumeGroupInfos(networkId: string): Promise<VolumeGroupInfos>--><!--Device-AudioVolumeManager-getVolumeGroupInfos(networkId: string): Promise<VolumeGroupInfos>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| networkId | string | 是 | 设备的网络id。本地设备audio.LOCAL_NETWORK_ID。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;[VolumeGroupInfos](arkts-audio-audio-volumegroupinfos-t-sys.md)&gt; | Promise对象，返回音量组信息列表。 |

**示例**

参见 [getVolumeGroupInfos](#getvolumegroupinfos)

## getVolumeGroupInfosSync

```TypeScript
getVolumeGroupInfosSync(networkId: string): VolumeGroupInfos
```

获取音量组信息列表，同步返回结果。

**起始版本：** 23

<!--Device-AudioVolumeManager-getVolumeGroupInfosSync(networkId: string): VolumeGroupInfos--><!--Device-AudioVolumeManager-getVolumeGroupInfosSync(networkId: string): VolumeGroupInfos-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| networkId | string | 是 | 设备的网络id。本地设备audio.LOCAL_NETWORK_ID。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [VolumeGroupInfos](arkts-audio-audio-volumegroupinfos-t-sys.md) | 音量组信息列表。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [6800101](../errorcode-audio.md#6800101-无效入参) | Parameter verification failed. |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let volumegroupinfos: audio.VolumeGroupInfos = audioVolumeManager.getVolumeGroupInfosSync(audio.LOCAL_NETWORK_ID);
  console.info(`Indicate that the volumeGroup list is obtained. ${JSON.stringify(volumegroupinfos)}`);
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to obtain the volumeGroup list ${error}`);
}
```

## getVolumeInUnitOfDb

```TypeScript
getVolumeInUnitOfDb(volumeType: AudioVolumeType, volumeLevel: int, device: DeviceType): double
```

获取系统根据音量类型、音量级别和设备类型计算出的音量分贝值。

**起始版本：** 23

<!--Device-AudioVolumeManager-getVolumeInUnitOfDb(volumeType: AudioVolumeType, volumeLevel: int, device: DeviceType): double--><!--Device-AudioVolumeManager-getVolumeInUnitOfDb(volumeType: AudioVolumeType, volumeLevel: int, device: DeviceType): double-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | 是 | 音量类型。 |
| volumeLevel | int | 是 | 要设置的音量级别。 |
| device | DeviceType | 是 | 输出设备类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| double | 系统音量（以分贝为单位）。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) | Not system App. |
| [6800101](../errorcode-audio.md#6800101-无效入参) | Parameter verification failed. |

## isAppVolumeMutedForUid

```TypeScript
isAppVolumeMutedForUid(uid: int, owned: boolean): Promise<boolean>
```

根据应用ID查询应用音量是否已静音。使用Promise异步回调。

> **说明：**&gt;
> 如果有多个调用者设置了静音状态，那么只有当所有调用者都取消静音状态后，此应用才会真正取消静音。

**起始版本：** 23

**需要权限：** ohos.permission.MANAGE_AUDIO_CONFIG

<!--Device-AudioVolumeManager-isAppVolumeMutedForUid(uid: int, owned: boolean): Promise<boolean>--><!--Device-AudioVolumeManager-isAppVolumeMutedForUid(uid: int, owned: boolean): Promise<boolean>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uid | int | 是 | 表示应用ID。 |
| owned | boolean | 是 | 要查询的静音状态。true查询当前调用者的静音状态，false查询应用的静音状态。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;boolean&gt; | Promise对象。返回true表示应用为静音状态；返回false表示应用为非静音状态。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [201](../../errorcode-universal.md#201-权限校验失败) | Permission denied. |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) | Not system App. |
| [6800101](../errorcode-audio.md#6800101-无效入参) | Parameter verification failed. |

**示例**

```TypeScript
let uid = 20010041; // 应用ID。

audioVolumeManager.isAppVolumeMutedForUid(uid, true).then((value: boolean) => {
  console.info(`app muted state is ${value}.`);
});
```

## isSystemMuted

```TypeScript
isSystemMuted(volumeType: AudioVolumeType): boolean
```

检查音量类型是否被静音。

**起始版本：** 23

<!--Device-AudioVolumeManager-isSystemMuted(volumeType: AudioVolumeType): boolean--><!--Device-AudioVolumeManager-isSystemMuted(volumeType: AudioVolumeType): boolean-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | 是 | 音量类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 音量类型的静音状态。值为 true 表示该音量类型处于静音状态，false 则表示相反。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) | Not system App. |
| [6800101](../errorcode-audio.md#6800101-无效入参) | Parameter verification failed. |

## off('activeVolumeTypeChange')

```TypeScript
off(type: 'activeVolumeTypeChange', callback?: Callback<AudioVolumeType>): void
```

取消监听当前活跃流变化事件。使用callback异步回调。

**起始版本：** 20

<!--Device-AudioVolumeManager-off(type: 'activeVolumeTypeChange', callback?: Callback<AudioVolumeType>): void--><!--Device-AudioVolumeManager-off(type: 'activeVolumeTypeChange', callback?: Callback<AudioVolumeType>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'activeVolumeTypeChange' | 是 | 事件回调类型，支持的事件为'activeVolumeTypeChange'，当取消监听当前活跃流变化事件时，触发该事件。 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md)&gt; | 否 | 回调函数，返回变化后的活跃音频音量类型。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) | Not system App. |
| [6800101](../errorcode-audio.md#6800101-无效入参) | Parameter verification failed. |

**示例**

```TypeScript
// 取消该事件的所有监听。
audioVolumeManager.off('activeVolumeTypeChange');

// 同一监听事件中，on方法和off方法传入callback参数一致，off方法取消对应on方法订阅的监听。
let activeVolumeTypeChangeCallback = (volumeType: audio.AudioVolumeType) => {
  console.info(`VolumeType of stream: ${volumeType} `);
};

audioVolumeManager.on('activeVolumeTypeChange', activeVolumeTypeChangeCallback);

audioVolumeManager.off('activeVolumeTypeChange', activeVolumeTypeChangeCallback);
```

## off('appVolumeChangeForUid')

```TypeScript
off(type: 'appVolumeChangeForUid', callback?: Callback<VolumeEvent>): void
```

取消监听指定应用应用级音量变化事件。使用callback异步回调。

**起始版本：** 19

**需要权限：** ohos.permission.MANAGE_AUDIO_CONFIG

<!--Device-AudioVolumeManager-off(type: 'appVolumeChangeForUid', callback?: Callback<VolumeEvent>): void--><!--Device-AudioVolumeManager-off(type: 'appVolumeChangeForUid', callback?: Callback<VolumeEvent>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'appVolumeChangeForUid' | 是 | 事件回调类型，支持的事件为'appVolumeChangeForUid'，当取消监听指定应用应用级音量变化事件时，触发该事件。 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[VolumeEvent](arkts-audio-audio-volumeevent-i.md)&gt; | 否 | 回调函数，返回变化后的音量信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [201](../../errorcode-universal.md#201-权限校验失败) | Permission denied. |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) | Not system App. |
| [6800101](../errorcode-audio.md#6800101-无效入参) | Parameter verification failed. |

**示例**

```TypeScript
// 取消该事件的所有监听。
audioVolumeManager.off('appVolumeChangeForUid');

// 同一监听事件中，on方法和off方法传入callback参数一致，off方法取消对应on方法订阅的监听。
let appVolumeChangeForUidCallback = (volumeEvent: audio.VolumeEvent) => {
  console.info(`VolumeType of stream: ${volumeEvent.volumeType} `);
  console.info(`Volume level: ${volumeEvent.volume} `);
  console.info(`Whether to updateUI: ${volumeEvent.updateUi} `);
};

audioVolumeManager.on('appVolumeChangeForUid', appVolumeChangeForUidCallback);

audioVolumeManager.off('appVolumeChangeForUid', appVolumeChangeForUidCallback);
```

## off('systemVolumeChange')

```TypeScript
off(type: 'systemVolumeChange', callback?: Callback<VolumeEvent>): void
```

取消监听系统音量变化事件。使用callback异步回调。

**起始版本：** 20

<!--Device-AudioVolumeManager-off(type: 'systemVolumeChange', callback?: Callback<VolumeEvent>): void--><!--Device-AudioVolumeManager-off(type: 'systemVolumeChange', callback?: Callback<VolumeEvent>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'systemVolumeChange' | 是 | 事件回调类型，支持的事件为'systemVolumeChange'，当取消监听系统音量变化事件时，触发该事件。 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[VolumeEvent](arkts-audio-audio-volumeevent-i.md)&gt; | 否 | 回调函数，返回变化后的音量信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) | Not system App. |
| [6800101](../errorcode-audio.md#6800101-无效入参) | Parameter verification failed. |

**示例**

```TypeScript
// 取消该事件的所有监听。
audioVolumeManager.off('systemVolumeChange');

// 同一监听事件中，on方法和off方法传入callback参数一致，off方法取消对应on方法订阅的监听。
let systemVolumeChangeCallback = (volumeEvent: audio.VolumeEvent) => {
  console.info(`Succeeded in using on or off function, VolumeEvent: ${volumeEvent}.`);
};

audioVolumeManager.on('systemVolumeChange', systemVolumeChangeCallback);

audioVolumeManager.off('systemVolumeChange', systemVolumeChangeCallback);
```

## offActiveVolumeTypeChange

```TypeScript
offActiveVolumeTypeChange(callback?: Callback<AudioVolumeType>): void
```

取消监听当前活跃流变化事件。使用callback异步回调。

**起始版本：** 23

<!--Device-AudioVolumeManager-offActiveVolumeTypeChange(callback?: Callback<AudioVolumeType>): void--><!--Device-AudioVolumeManager-offActiveVolumeTypeChange(callback?: Callback<AudioVolumeType>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md)&gt; | 否 | 回调函数，返回变化后的活跃音频音量类型。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) | Not system App. |
| [6800101](../errorcode-audio.md#6800101-无效入参) | Parameter verification failed. |

**示例**

```TypeScript
// 取消该事件的所有监听。
audioVolumeManager.offActiveVolumeTypeChange();

// 同一监听事件中，on方法和off方法传入callback参数一致，off方法取消对应on方法订阅的监听。
let activeVolumeTypeChangeCallback = (volumeType: audio.AudioVolumeType) => {
  console.info(`VolumeType of stream: ${volumeType} `);
};

audioVolumeManager.onActiveVolumeTypeChange(activeVolumeTypeChangeCallback);

audioVolumeManager.offActiveVolumeTypeChange(activeVolumeTypeChangeCallback);
```

## offAppVolumeChangeForUid

```TypeScript
offAppVolumeChangeForUid(callback?: Callback<VolumeEvent>): void
```

取消监听指定应用应用级音量变化事件。使用callback异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.MANAGE_AUDIO_CONFIG

<!--Device-AudioVolumeManager-offAppVolumeChangeForUid(callback?: Callback<VolumeEvent>): void--><!--Device-AudioVolumeManager-offAppVolumeChangeForUid(callback?: Callback<VolumeEvent>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[VolumeEvent](arkts-audio-audio-volumeevent-i.md)&gt; | 否 | 回调函数，返回变化后的音量信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [201](../../errorcode-universal.md#201-权限校验失败) | Permission denied. |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) | Not system App. |
| [6800101](../errorcode-audio.md#6800101-无效入参) | Parameter verification failed. |

**示例**

```TypeScript
// 取消该事件的所有监听。
audioVolumeManager.offAppVolumeChangeForUid();

// 同一监听事件中，on方法和off方法传入callback参数一致，off方法取消对应on方法订阅的监听。
let appVolumeChangeForUidCallback = (volumeEvent: audio.VolumeEvent) => {
  console.info(`VolumeType of stream: ${volumeEvent.volumeType} `);
  console.info(`Volume level: ${volumeEvent.volume} `);
  console.info(`Whether to updateUI: ${volumeEvent.updateUi} `);
};

audioVolumeManager.onAppVolumeChangeForUid(appVolumeChangeForUidCallback);

audioVolumeManager.offAppVolumeChangeForUid(appVolumeChangeForUidCallback);
```

## offSystemVolumeChange

```TypeScript
offSystemVolumeChange(callback?: Callback<VolumeEvent>): void
```

取消监听系统音量变化事件。使用callback异步回调。

**起始版本：** 23

<!--Device-AudioVolumeManager-offSystemVolumeChange(callback?: Callback<VolumeEvent>): void--><!--Device-AudioVolumeManager-offSystemVolumeChange(callback?: Callback<VolumeEvent>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[VolumeEvent](arkts-audio-audio-volumeevent-i.md)&gt; | 否 | 回调函数，返回变化后的音量信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) | Not system App. |
| [6800101](../errorcode-audio.md#6800101-无效入参) | Parameter verification failed. |

**示例**

```TypeScript
// 取消该事件的所有监听。
audioVolumeManager.offSystemVolumeChange();

// 同一监听事件中，on方法和off方法传入callback参数一致，off方法取消对应on方法订阅的监听。
let systemVolumeChangeCallback = (volumeEvent: audio.VolumeEvent) => {
  console.info(`Succeeded in using on or off function, VolumeEvent: ${volumeEvent}.`);
};

audioVolumeManager.onSystemVolumeChange(systemVolumeChangeCallback);

audioVolumeManager.offSystemVolumeChange(systemVolumeChangeCallback);
```

## offSystemVolumeChangeByFilter

```TypeScript
offSystemVolumeChangeByFilter(callback?: Callback<VolumeEvent>): void
```

取消订阅系统音量变化事件。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AudioVolumeManager-offSystemVolumeChangeByFilter(callback?: Callback<VolumeEvent>): void--><!--Device-AudioVolumeManager-offSystemVolumeChangeByFilter(callback?: Callback<VolumeEvent>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[VolumeEvent](arkts-audio-audio-volumeevent-i.md)&gt; | 否 | 订阅中使用的回调函数。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) | Not system app. |
| [6800101](../errorcode-audio.md#6800101-无效入参) | Parameter verification failed. |

## offVolumeLimitExceeded

```TypeScript
offVolumeLimitExceeded(callback?: Callback<VolumeLimitExceededEvent>): void
```

取消订阅当前音量是否超过音量保护阈值的监控。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AudioVolumeManager-offVolumeLimitExceeded(callback?: Callback<VolumeLimitExceededEvent>): void--><!--Device-AudioVolumeManager-offVolumeLimitExceeded(callback?: Callback<VolumeLimitExceededEvent>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[VolumeLimitExceededEvent](arkts-audio-audio-volumelimitexceededevent-i-sys.md)&gt; | 否 | 1. 必填参数缺失；。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) | Not system App. |
| [6800101](../errorcode-audio.md#6800101-无效入参) | Parameter verification failed. |

## offVolumePercentageChange

```TypeScript
offVolumePercentageChange(callback?: Callback<VolumeEvent>): void
```

取消监听系统音量变化事件。使用callback异步回调。

**起始版本：** 23

<!--Device-AudioVolumeManager-offVolumePercentageChange(callback?: Callback<VolumeEvent>): void--><!--Device-AudioVolumeManager-offVolumePercentageChange(callback?: Callback<VolumeEvent>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[VolumeEvent](arkts-audio-audio-volumeevent-i.md)&gt; | 否 | 回调函数，返回变化后的音量信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) | Not system App. |
| [6800101](../errorcode-audio.md#6800101-无效入参) | Parameter verification failed. |

**示例**

```TypeScript
// 取消该事件的所有监听。
audioVolumeManager.offVolumePercentageChange();

// 同一监听事件中，on方法和off方法传入callback参数一致，off方法取消对应on方法订阅的监听。
let volumePercentageChangeCallback = (volumeEvent: audio.VolumeEvent) => {
  console.info(`VolumeType of stream: ${volumeEvent.volumeType} `);
  console.info(`Volume level: ${volumeEvent.volume} `);
  console.info(`Volume percentage: ${volumeEvent.percentage} `);
  console.info(`Whether to updateUI: ${volumeEvent.updateUi} `);
};

audioVolumeManager.onVolumePercentageChange(volumePercentageChangeCallback);

audioVolumeManager.offVolumePercentageChange(volumePercentageChangeCallback);
```

## on('activeVolumeTypeChange')

```TypeScript
on(type: 'activeVolumeTypeChange', callback: Callback<AudioVolumeType>): void
```

监听当前活跃流变化事件（当活跃流发生变化时触发）。使用callback异步回调。

**起始版本：** 20

<!--Device-AudioVolumeManager-on(type: 'activeVolumeTypeChange', callback: Callback<AudioVolumeType>): void--><!--Device-AudioVolumeManager-on(type: 'activeVolumeTypeChange', callback: Callback<AudioVolumeType>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'activeVolumeTypeChange' | 是 | 事件回调类型，支持的事件为'activeVolumeTypeChange'，当活跃流发生变化时，触发该事件。 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md)&gt; | 是 | 回调函数，返回变化后的活跃音频音量类型。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) | Not system App. |
| [6800101](../errorcode-audio.md#6800101-无效入参) | Parameter verification failed. |

**示例**

```TypeScript
audioVolumeManager.on('activeVolumeTypeChange', (volumeType: audio.AudioVolumeType) => {
  console.info(`VolumeType of stream: ${volumeType} `);
});
```

## on('appVolumeChangeForUid')

```TypeScript
on(type: 'appVolumeChangeForUid', uid: int, callback: Callback<VolumeEvent>): void
```

监听指定应用应用级音量变化事件（当应用级音量发生变化时触发）。使用callback异步回调。

**起始版本：** 19

**需要权限：** ohos.permission.MANAGE_AUDIO_CONFIG

<!--Device-AudioVolumeManager-on(type: 'appVolumeChangeForUid', uid: int, callback: Callback<VolumeEvent>): void--><!--Device-AudioVolumeManager-on(type: 'appVolumeChangeForUid', uid: int, callback: Callback<VolumeEvent>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'appVolumeChangeForUid' | 是 | 事件回调类型，支持的事件为'appVolumeChangeForUid'，当应用级音量发生变化时，触发该事件。 |
| uid | int | 是 | 表示应用ID。 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[VolumeEvent](arkts-audio-audio-volumeevent-i.md)&gt; | 是 | 回调函数，返回变化后的音量信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [201](../../errorcode-universal.md#201-权限校验失败) | Permission denied. |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) | Not system App. |
| [6800101](../errorcode-audio.md#6800101-无效入参) | Parameter verification failed. |

**示例**

```TypeScript
let uid: number = 20010041; // 应用ID。

audioVolumeManager.on('appVolumeChangeForUid', uid, (volumeEvent: audio.VolumeEvent) => {
  console.info(`VolumeType of stream: ${volumeEvent.volumeType} `);
  console.info(`Volume level: ${volumeEvent.volume} `);
  console.info(`Whether to updateUI: ${volumeEvent.updateUi} `);
});
```

## on('systemVolumeChange')

```TypeScript
on(type: 'systemVolumeChange', callback: Callback<VolumeEvent>): void
```

监听系统音量变化事件（当系统音量发生变化时触发）。使用callback异步回调。

**起始版本：** 20

<!--Device-AudioVolumeManager-on(type: 'systemVolumeChange', callback: Callback<VolumeEvent>): void--><!--Device-AudioVolumeManager-on(type: 'systemVolumeChange', callback: Callback<VolumeEvent>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'systemVolumeChange' | 是 | 事件回调类型，支持的事件为'systemVolumeChange'，当系统音量发生变化时，触发该事件。 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[VolumeEvent](arkts-audio-audio-volumeevent-i.md)&gt; | 是 | 回调函数，返回变化后的音量信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) | Not system App. |
| [6800101](../errorcode-audio.md#6800101-无效入参) | Parameter verification failed. |

**示例**

```TypeScript
audioVolumeManager.on('systemVolumeChange', (volumeEvent: audio.VolumeEvent) => {
  console.info(`Succeeded in using on function, VolumeEvent: ${volumeEvent}.`);
});
```

## onActiveVolumeTypeChange

```TypeScript
onActiveVolumeTypeChange(callback: Callback<AudioVolumeType>): void
```

监听当前活跃流变化事件（当活跃流发生变化时触发）。使用callback异步回调。

**起始版本：** 23

<!--Device-AudioVolumeManager-onActiveVolumeTypeChange(callback: Callback<AudioVolumeType>): void--><!--Device-AudioVolumeManager-onActiveVolumeTypeChange(callback: Callback<AudioVolumeType>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md)&gt; | 是 | 回调函数，返回变化后的活跃音频音量类型。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) | Not system App. |
| [6800101](../errorcode-audio.md#6800101-无效入参) | Parameter verification failed. |

**示例**

```TypeScript
audioVolumeManager.onActiveVolumeTypeChange((volumeType: audio.AudioVolumeType) => {
  console.info(`VolumeType of stream: ${volumeType} `);
});
```

## onAppVolumeChangeForUid

```TypeScript
onAppVolumeChangeForUid(uid: int, callback: Callback<VolumeEvent>): void
```

L监听指定应用应用级音量变化事件（当应用级音量发生变化时触发）。使用callback异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.MANAGE_AUDIO_CONFIG

<!--Device-AudioVolumeManager-onAppVolumeChangeForUid(uid: int, callback: Callback<VolumeEvent>): void--><!--Device-AudioVolumeManager-onAppVolumeChangeForUid(uid: int, callback: Callback<VolumeEvent>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uid | int | 是 | The app's uid. <br>取值限定为整数。 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[VolumeEvent](arkts-audio-audio-volumeevent-i.md)&gt; | 是 | 回调函数，返回变化后的音量信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [201](../../errorcode-universal.md#201-权限校验失败) | Permission denied. |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) | Not system App. |
| [6800101](../errorcode-audio.md#6800101-无效入参) | Parameter verification failed. |

**示例**

```TypeScript
let uid: int = 20010041; // 应用ID。

audioVolumeManager.onAppVolumeChangeForUid(uid, (volumeEvent: audio.VolumeEvent) => {
  console.info(`VolumeType of stream: ${volumeEvent.volumeType} `);
  console.info(`Volume level: ${volumeEvent.volume} `);
  console.info(`Whether to updateUI: ${volumeEvent.updateUi} `);
});
```

## onSystemVolumeChange

```TypeScript
onSystemVolumeChange(callback: Callback<VolumeEvent>): void
```

监听系统音量变化事件（当系统音量发生变化时触发）。使用callback异步回调。

**起始版本：** 23

<!--Device-AudioVolumeManager-onSystemVolumeChange(callback: Callback<VolumeEvent>): void--><!--Device-AudioVolumeManager-onSystemVolumeChange(callback: Callback<VolumeEvent>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[VolumeEvent](arkts-audio-audio-volumeevent-i.md)&gt; | 是 | 回调函数，返回变化后的音量信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) | Not system App. |
| [6800101](../errorcode-audio.md#6800101-无效入参) | Parameter verification failed. |

**示例**

```TypeScript
audioVolumeManager.onSystemVolumeChange((volumeEvent: audio.VolumeEvent) => {
  console.info(`Succeeded in using on function, VolumeEvent: ${volumeEvent}.`);
});
```

## onSystemVolumeChangeByFilter

```TypeScript
onSystemVolumeChangeByFilter(filter: SystemVolumeFilter, callback: Callback<VolumeEvent>): void
```

订阅系统音量变化事件。 当目标过滤器的系统音量发生变化时，已注册的客户端将收到回调通知。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AudioVolumeManager-onSystemVolumeChangeByFilter(filter: SystemVolumeFilter, callback: Callback<VolumeEvent>): void--><!--Device-AudioVolumeManager-onSystemVolumeChangeByFilter(filter: SystemVolumeFilter, callback: Callback<VolumeEvent>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| filter | [SystemVolumeFilter](arkts-audio-audio-systemvolumefilter-i-sys.md) | 是 | 用于系统音量变化的过滤器。 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[VolumeEvent](arkts-audio-audio-volumeevent-i.md)&gt; | 是 | 订阅中使用的回调函数。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) | Not a system app. |
| [6800101](../errorcode-audio.md#6800101-无效入参) | Parameter verification failed. |

## onVolumeLimitExceeded

```TypeScript
onVolumeLimitExceeded(callback: Callback<VolumeLimitExceededEvent>): void
```

监听当前音量超过音量保护阈值的事件。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AudioVolumeManager-onVolumeLimitExceeded(callback: Callback<VolumeLimitExceededEvent>): void--><!--Device-AudioVolumeManager-onVolumeLimitExceeded(callback: Callback<VolumeLimitExceededEvent>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[VolumeLimitExceededEvent](arkts-audio-audio-volumelimitexceededevent-i-sys.md)&gt; | 是 | 回调函数，用于获取音量限制事件。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) | Not system App. |
| [6800101](../errorcode-audio.md#6800101-无效入参) | Parameter verification failed. |

## onVolumePercentageChange

```TypeScript
onVolumePercentageChange(callback: Callback<VolumeEvent>): void
```

监听系统音量百分比变化事件。使用callback异步回调。

**起始版本：** 23

<!--Device-AudioVolumeManager-onVolumePercentageChange(callback: Callback<VolumeEvent>): void--><!--Device-AudioVolumeManager-onVolumePercentageChange(callback: Callback<VolumeEvent>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[VolumeEvent](arkts-audio-audio-volumeevent-i.md)&gt; | 是 | 回调函数，返回变化后的音量信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) | Not system App. |
| [6800101](../errorcode-audio.md#6800101-无效入参) | Parameter verification failed. |

**示例**

```TypeScript
audioVolumeManager.onVolumePercentageChange((volumeEvent: audio.VolumeEvent) => {
  console.info(`VolumeType of stream: ${volumeEvent.volumeType} `);
  console.info(`Volume level: ${volumeEvent.volume} `);
  console.info(`Volume percentage: ${volumeEvent.percentage} `);
  console.info(`Whether to updateUI: ${volumeEvent.updateUi} `);
});
```

## setAppVolumeMutedForUid

```TypeScript
setAppVolumeMutedForUid(uid: int, muted: boolean): Promise<void>
```

根据应用ID设置应用静音状态。使用Promise异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.MANAGE_AUDIO_CONFIG

<!--Device-AudioVolumeManager-setAppVolumeMutedForUid(uid: int, muted: boolean): Promise<void>--><!--Device-AudioVolumeManager-setAppVolumeMutedForUid(uid: int, muted: boolean): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uid | int | 是 | 表示应用ID。 |
| muted | boolean | 是 | 设置应用的静音状态。true设置为静音，false解除静音。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [201](../../errorcode-universal.md#201-权限校验失败) | Permission denied. |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) | Not system App. |
| [6800101](../errorcode-audio.md#6800101-无效入参) | Parameter verification failed. |
| [6800301](../errorcode-audio.md#6800301-系统处理异常) | Crash or blocking occurs in system process. |

**示例**

```TypeScript
let uid = 20010041; // 应用ID。

audioVolumeManager.setAppVolumeMutedForUid(uid, true).then(() => {
  console.info(`set app mute state success.`);
});
```

## setAppVolumePercentageForUid

```TypeScript
setAppVolumePercentageForUid(uid: int, volume: int): Promise<void>
```

根据应用ID设置指定应用的音量百分比（范围为[0, 100]）。使用Promise异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.MANAGE_AUDIO_CONFIG

<!--Device-AudioVolumeManager-setAppVolumePercentageForUid(uid: int, volume: int): Promise<void>--><!--Device-AudioVolumeManager-setAppVolumePercentageForUid(uid: int, volume: int): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uid | int | 是 | 表示应用ID。 |
| volume | int | 是 | 要设置的音量百分比，范围为[0, 100]。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [201](../../errorcode-universal.md#201-权限校验失败) | Permission denied. |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) | Not system App. |
| [6800101](../errorcode-audio.md#6800101-无效入参) | Parameter verification failed. |
| [6800301](../errorcode-audio.md#6800301-系统处理异常) | Crash or blocking occurs in system process. |

**示例**

```TypeScript
let uid = 20010041; // 应用ID。
let volume = 20;    // 要设置的音量值。

audioVolumeManager.setAppVolumePercentageForUid(uid, volume).then(() => {
  console.info(`set app volume success.`);
});
```

## setSystemVolumeByUid

```TypeScript
setSystemVolumeByUid(volumeType: AudioVolumeType, volume: int, callingUid: int): Promise<void>
```

为特定用户ID的应用设置音量。此方法使用Promise来返回结果。

**起始版本：** 23

**需要权限：** ohos.permission.ACCESS_NOTIFICATION_POLICY

<!--Device-AudioVolumeManager-setSystemVolumeByUid(volumeType: AudioVolumeType, volume: int, callingUid: int): Promise<void>--><!--Device-AudioVolumeManager-setSystemVolumeByUid(volumeType: AudioVolumeType, volume: int, callingUid: int): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | 是 | 音量类型。 |
| volume | int | 是 | 要设置的音量。可通过调用getMinVolume和getMaxVolume获取取值范围。 |
| callingUid | int | 是 | 流所有者的UID。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | 承诺用于返回结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [201](../../errorcode-universal.md#201-权限校验失败) | Permission denied. |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) | Not system App. |
| [6800101](../errorcode-audio.md#6800101-无效入参) | Parameter verification failed. |
| [6800301](../errorcode-audio.md#6800301-系统处理异常) | Crash or blocking occurs in system process. |

## setSystemVolumePercentage

```TypeScript
setSystemVolumePercentage(volumeType: AudioVolumeType, percentage: int): Promise<void>
```

设置指定流的音量百分比。使用Promise异步回调。

> **说明：**&gt;
> - 设置指定流的音量百分比时需要使用整数，范围从最小系统音量百分比到100。&gt;
> - 音量百分比与音量等级相对应，每个等级对应特定的百分比。&gt;
> - 当音量等级发生变化时，音量百分比会相应调整，并映射在音量等级的范围内。&gt;
> - 0等级音量映射为0%，最大音量映射为100%。中间音量等级均匀分布在1至99之间。&gt;
> - 当音量百分比变化时，音量等级会相应调整。

**起始版本：** 23

**需要权限：** ohos.permission.MANAGE_AUDIO_CONFIG

<!--Device-AudioVolumeManager-setSystemVolumePercentage(volumeType: AudioVolumeType, percentage: int): Promise<void>--><!--Device-AudioVolumeManager-setSystemVolumePercentage(volumeType: AudioVolumeType, percentage: int): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volumeType | [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md) | 是 | 音量流类型。 |
| percentage | int | 是 | 音量百分比，可设置范围的最小值是通过 [getMinSystemVolumePercentage](#getminsystemvolumepercentage)接口获取到的音量百分比， 最大值是100。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [201](../../errorcode-universal.md#201-权限校验失败) | Permission denied. |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) | Not system App. |
| [6800101](../errorcode-audio.md#6800101-无效入参) | Parameter verification failed, including volumeType or percentage param being out of range. |
| [6800301](../errorcode-audio.md#6800301-系统处理异常) | Crash or blocking occurs in system process. |

**示例**

```TypeScript
audioVolumeManager.setSystemVolumePercentage(audio.AudioVolumeType.MEDIA, 10).then(() => {
  console.info('Promise returned to indicate a successful volume setting.');
});
```

