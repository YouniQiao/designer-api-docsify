# AudioDeviceEnhanceManager

提供增强的音频设备管理能力。

**起始版本：** 26.0.0

<!--Device-audio-interface AudioDeviceEnhanceManager--><!--Device-audio-interface AudioDeviceEnhanceManager-End-->

**系统能力：** SystemCapability.Multimedia.Audio.DeviceEnhance

## getSoundCardInfo

```TypeScript
getSoundCardInfo(): Promise<SoundCardInfo>
```

获取声卡信息。该方法使用promise返回查询结果。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AudioDeviceEnhanceManager-getSoundCardInfo(): Promise<SoundCardInfo>--><!--Device-AudioDeviceEnhanceManager-getSoundCardInfo(): Promise<SoundCardInfo>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.DeviceEnhance

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise&lt;SoundCardInfo&gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { audio } from '@kit.AudioKit';
import { BusinessError } from '@kit.BasicServicesKit';

let audioManager = audio.getAudioManager();
let deviceEnhanceManager = audioManager.getDeviceEnhanceManager();

deviceEnhanceManager.getSoundCardInfo().then((soundCardInfo: audio.SoundCardInfo) => {
  console.info(`Successfully obtained sound card info: ${JSON.stringify(soundCardInfo, null, 2)}`);
})
.catch((err: BusinessError) => {
  console.error(`Failed to get sound card info. Code: ${err.code}, Message: ${err.message}`);
});
```
