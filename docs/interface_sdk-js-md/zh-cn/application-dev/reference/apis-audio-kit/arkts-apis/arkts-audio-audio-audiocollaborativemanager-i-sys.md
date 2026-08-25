# AudioCollaborativeManager（系统接口）

移动全景声管理器。 在使用AudioCollaborativeManager的接口前，需要先使用[getCollaborativeManager](arkts-audio-audio-audiomanager-i-sys.md#getcollaborativemanager)获取 AudioCollaborativeManager实例。

**起始版本：** 20

**系统能力：** SystemCapability.Multimedia.Audio.Core

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { audio } from 'kits/@kit.AudioKit';
```

## isCollaborativePlaybackEnabledForDevice

```TypeScript
isCollaborativePlaybackEnabledForDevice(deviceDescriptor: AudioDeviceDescriptor): boolean
```

查询指定设备移动全景声状态，同步返回结果。

**起始版本：** 20

**系统能力：** SystemCapability.Multimedia.Audio.Device

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| deviceDescriptor | [AudioDeviceDescriptor](arkts-audio-audio-audiodevicedescriptor-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [6800101](../errorcode-audio.md#6800101-无效入参) |

## isCollaborativePlaybackSupported

```TypeScript
isCollaborativePlaybackSupported(): boolean
```

查询系统移动全景声支持能力，同步返回结果。

**起始版本：** 20

**系统能力：** SystemCapability.Multimedia.Audio.Device

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## isCollaborativePlaybackSupportedForDevice

```TypeScript
isCollaborativePlaybackSupportedForDevice(deviceDescriptor: AudioDeviceDescriptor): boolean
```

检查指定设备是否支持协同播放。

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| deviceDescriptor | [AudioDeviceDescriptor](arkts-audio-audio-audiodevicedescriptor-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## setCollaborativePlaybackEnabledForDevice

```TypeScript
setCollaborativePlaybackEnabledForDevice(deviceDescriptor: AudioDeviceDescriptor, enabled: boolean): Promise<void>
```

根据输入指令，开启或关闭指定设备移动全景声。使用Promise异步回调。 当前只有蓝牙A2DP（Advanced Audio Distribution Profile）设备支持移动全景声。当开启移动全景声后，指定蓝牙A2DP设备和本地扬声器将同时播放音频。

**起始版本：** 20

**系统能力：** SystemCapability.Multimedia.Audio.Device

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| deviceDescriptor | [AudioDeviceDescriptor](arkts-audio-audio-audiodevicedescriptor-i.md) | 是 |
| enabled | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [6800101](../errorcode-audio.md#6800101-无效入参) |
