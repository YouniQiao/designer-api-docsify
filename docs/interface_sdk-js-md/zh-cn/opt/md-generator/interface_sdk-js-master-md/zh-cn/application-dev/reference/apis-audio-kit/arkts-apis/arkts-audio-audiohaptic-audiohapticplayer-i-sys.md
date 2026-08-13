# AudioHapticPlayer

音振播放器，提供音振协同播放功能。在调用AudioHapticPlayer的接口前，需要先通过 [createPlayer](arkts-audio-audiohaptic-audiohapticmanager-i.md#createPlayer)创建 实例。

**起始版本：** 23

**废弃版本：** -1

<!--Device-audioHaptic-interface AudioHapticPlayer--><!--Device-audioHaptic-interface AudioHapticPlayer-End-->

**系统能力：** SystemCapability.Multimedia.AudioHaptic.Core

## enableHapticsInSilentMode

```TypeScript
enableHapticsInSilentMode(enable: boolean): void
```

Enable haptics when the ringer mode is silent mode. 这个方法只能在播放器start前，或stop后release前调用

**起始版本：** 23

**废弃版本：** -1

<!--Device-AudioHapticPlayer-enableHapticsInSilentMode(enable: boolean): void--><!--Device-AudioHapticPlayer-enableHapticsInSilentMode(enable: boolean): void-End-->

**系统能力：** SystemCapability.Multimedia.AudioHaptic.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enable | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [5400102](../../apis-media-kit/errorcode-media.md#5400102-当前状态不支持此操作) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## isHapticsIntensityAdjustmentSupported

```TypeScript
isHapticsIntensityAdjustmentSupported(): boolean
```

Check whether the device supports haptics intensity adjustment.

**起始版本：** 23

**废弃版本：** -1

<!--Device-AudioHapticPlayer-isHapticsIntensityAdjustmentSupported(): boolean--><!--Device-AudioHapticPlayer-isHapticsIntensityAdjustmentSupported(): boolean-End-->

**系统能力：** SystemCapability.Multimedia.AudioHaptic.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## isHapticsRampSupported

```TypeScript
isHapticsRampSupported(): boolean
```

Check whether the device supports haptics intensity ramp effect.

**起始版本：** 23

**废弃版本：** -1

<!--Device-AudioHapticPlayer-isHapticsRampSupported(): boolean--><!--Device-AudioHapticPlayer-isHapticsRampSupported(): boolean-End-->

**系统能力：** SystemCapability.Multimedia.AudioHaptic.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## setHapticsIntensity

```TypeScript
setHapticsIntensity(intensity: number): Promise<void>
```

Set haptics intensity for this player. This method uses a promise to return the result. 这个方法只能在播放器释放前调用，并且每次播放过程只能设置一次。

**起始版本：** 23

**废弃版本：** -1

<!--Device-AudioHapticPlayer-setHapticsIntensity(intensity: double): Promise<void>--><!--Device-AudioHapticPlayer-setHapticsIntensity(intensity: double): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.AudioHaptic.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| intensity | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [5400102](../../apis-media-kit/errorcode-media.md#5400102-当前状态不支持此操作) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [5400108](../../apis-media-kit/errorcode-media.md#5400108-参数超过取值范围) |

## setHapticsRamp

```TypeScript
setHapticsRamp(duration: number, startIntensity: number, endIntensity: number): Promise<void>
```

Set haptics intensity ramp effect for this player. This method uses a promise to return the result. 这个方法只能在播放器start前，或stop后release前调用

**起始版本：** 23

**废弃版本：** -1

<!--Device-AudioHapticPlayer-setHapticsRamp(duration: int, startIntensity: double, endIntensity: double): Promise<void>--><!--Device-AudioHapticPlayer-setHapticsRamp(duration: int, startIntensity: double, endIntensity: double): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.AudioHaptic.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| duration | number | 是 |
| startIntensity | number | 是 |
| endIntensity | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [5400102](../../apis-media-kit/errorcode-media.md#5400102-当前状态不支持此操作) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [5400108](../../apis-media-kit/errorcode-media.md#5400108-参数超过取值范围) |
