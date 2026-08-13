# AudioCollaborativeManager（系统接口）

Implements audio collaborative management.

**起始版本：** 23

**废弃版本：** -1

<!--Device-audio-interface AudioCollaborativeManager--><!--Device-audio-interface AudioCollaborativeManager-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Core

**系统接口：** 此接口为系统接口。

## isCollaborativePlaybackEnabledForDevice

```TypeScript
isCollaborativePlaybackEnabledForDevice(deviceDescriptor: AudioDeviceDescriptor): boolean
```

检查指定设备的协同播放状态

**起始版本：** 23

**废弃版本：** -1

<!--Device-AudioCollaborativeManager-isCollaborativePlaybackEnabledForDevice(deviceDescriptor: AudioDeviceDescriptor): boolean--><!--Device-AudioCollaborativeManager-isCollaborativePlaybackEnabledForDevice(deviceDescriptor: AudioDeviceDescriptor): boolean-End-->

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
| [6800101](../errorcode-audio.md#6800101-无效入参) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { audio } from '@kit.AudioKit';
import { BusinessError } from '@kit.BasicServicesKit';

let deviceDescriptor: audio.AudioDeviceDescriptor = {
  deviceRole : audio.DeviceRole.OUTPUT_DEVICE,
  deviceType : audio.DeviceType.BLUETOOTH_A2DP,
  id : 1,
  name : "",
  address : "123",
  sampleRates : [44100],
  channelCounts : [2],
  channelMasks : [0],
  networkId : audio.LOCAL_NETWORK_ID,
  interruptGroupId : 1,
  volumeGroupId : 1,
  displayName : ""
}

try {
  let isCollaborativeEnabled: boolean = audioCollaborativeManager.isCollaborativePlaybackEnabledForDevice(deviceDescriptor);
  console.info(`AudioCollaborativeManager isCollaborativeEnabled: ${isCollaborativeEnabled}`);
} catch (err) {
  let error = err as BusinessError;
  console.error(`ERROR: ${error}`);
}
```

## isCollaborativePlaybackSupported

```TypeScript
isCollaborativePlaybackSupported(): boolean
```

Checks whether the collaborative playback is supported by system.

**起始版本：** 23

**废弃版本：** -1

<!--Device-AudioCollaborativeManager-isCollaborativePlaybackSupported(): boolean--><!--Device-AudioCollaborativeManager-isCollaborativePlaybackSupported(): boolean-End-->

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

## 示例

```TypeScript
import { audio } from '@kit.AudioKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let isCollaborativeSupported: boolean = audioCollaborativeManager.isCollaborativePlaybackSupported();
  console.info(`AudioCollaborativeManager isCollaborativeSupported: ${isCollaborativeSupported}`);
} catch (err) {
  let error = err as BusinessError;
  console.error(`ERROR: ${error}`);
}
```

## isCollaborativePlaybackSupportedForDevice

```TypeScript
isCollaborativePlaybackSupportedForDevice(deviceDescriptor: AudioDeviceDescriptor): boolean
```

检查指定设备是否支持协同播放。

**起始版本：** 24

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AudioCollaborativeManager-isCollaborativePlaybackSupportedForDevice(deviceDescriptor: AudioDeviceDescriptor): boolean--><!--Device-AudioCollaborativeManager-isCollaborativePlaybackSupportedForDevice(deviceDescriptor: AudioDeviceDescriptor): boolean-End-->

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

设置使能或者关闭与指定设备协同播放。当前仅A2DP音频设备支持协同播放。如果系统当前正在使用指定的设备发声，调用此接口后，声音将从本地speaker和指定的设备上协同播放出来。

**起始版本：** 23

**废弃版本：** -1

<!--Device-AudioCollaborativeManager-setCollaborativePlaybackEnabledForDevice(deviceDescriptor: AudioDeviceDescriptor, enabled: boolean): Promise<void>--><!--Device-AudioCollaborativeManager-setCollaborativePlaybackEnabledForDevice(deviceDescriptor: AudioDeviceDescriptor, enabled: boolean): Promise<void>-End-->

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
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [6800101](../errorcode-audio.md#6800101-无效入参) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { audio } from '@kit.AudioKit';
import { BusinessError } from '@kit.BasicServicesKit';

let deviceDescriptor: audio.AudioDeviceDescriptor = {
  deviceRole : audio.DeviceRole.OUTPUT_DEVICE,
  deviceType : audio.DeviceType.BLUETOOTH_A2DP,
  id : 1,
  name : "",
  address : "123",
  sampleRates : [44100],
  channelCounts : [2],
  channelMasks : [0],
  networkId : audio.LOCAL_NETWORK_ID,
  interruptGroupId : 1,
  volumeGroupId : 1,
  displayName : ""
};
let enabled: boolean = true;

audioCollaborativeManager.setCollaborativePlaybackEnabledForDevice(deviceDescriptor, enabled).then(() => {
  console.info(`setSpatializationEnabled success`);
}).catch((err: BusinessError) => {
  console.error(`Result ERROR: ${err}`);
});
```
