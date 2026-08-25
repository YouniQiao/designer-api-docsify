# createGlobalAudioLoopback（系统接口）

## 导入模块

```TypeScript
import { audio } from 'kits/@kit.AudioKit';
```

## createGlobalAudioLoopback

```TypeScript
function createGlobalAudioLoopback(mode: AudioLoopbackMode, isController: boolean): Promise<AudioLoopback | null>
```

创建一个全局音频返听实例，该实例提供低延迟的入耳监听功能。 硬件音频返听只能在支持的平台中创建，应用程序应首先使用[isAudioLoopbackSupported](arkts-audio-audio-audiostreammanager-i.md#isaudioloopbacksupported) 进行检查。 系统中只能存在一个拥有全局返听功能的主实例，其他实例均为控制器。控制器可以通过向主实例发送命令来管理全局返听，并监听其状态变化。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mode | [AudioLoopbackMode](arkts-audio-audio-audioloopbackmode-e.md) | 是 |
| isController | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[AudioLoopback](arkts-audio-audio-audioloopback-i.md) \| null & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [6800101](../errorcode-audio.md#6800101-无效入参) |
| [6800104](../errorcode-audio.md#6800104-参数选项不支持) |
