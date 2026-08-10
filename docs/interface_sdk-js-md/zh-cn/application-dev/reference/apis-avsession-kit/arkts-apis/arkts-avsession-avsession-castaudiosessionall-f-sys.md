# castAudioSessionAll（系统接口）

## 导入模块

```TypeScript
import { avSession } from 'kits/@kit.AVSessionKit';
```

## castAudioSessionAll

```TypeScript
function castAudioSessionAll(audioDevices: Array<audio.AudioDeviceDescriptor>): Promise<void>
```

Cast all the media audio to the remote devices or cast back local device

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**需要权限：** ohos.permission.MANAGE_MEDIA_RESOURCES

<!--Device-avSession-function castAudioSessionAll(audioDevices: Array<audio.AudioDeviceDescriptor>): Promise<void>--><!--Device-avSession-function castAudioSessionAll(audioDevices: Array<audio.AudioDeviceDescriptor>): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Manager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| audioDevices | Array&lt;audio.AudioDeviceDescriptor&gt; | 是 | Specifies the audio devices to cast. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | void promise when executed successfully |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 201 | permission denied |
| 202 | Not System App. |
| 6600104 | The remote session connection failed. |

