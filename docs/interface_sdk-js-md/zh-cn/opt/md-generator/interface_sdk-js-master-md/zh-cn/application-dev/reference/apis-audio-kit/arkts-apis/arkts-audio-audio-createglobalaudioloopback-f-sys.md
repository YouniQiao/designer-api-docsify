# createGlobalAudioLoopback（系统接口）

## 导入模块

```TypeScript
```

## createGlobalAudioLoopback

```TypeScript
function createGlobalAudioLoopback(mode: AudioLoopbackMode, isController: boolean): Promise<AudioLoopback | null>
```

创建全局音频环回实例，提供低时延入耳监听功能。 硬件音频环回只能在支持的平台中创建，应用程序可以使用 > **说明：**> [isAudioLoopbackSupported](arkts-audio-audio-audiostreammanager-i.md#isaudioloopbacksupported)先检查。 > 系统中应该只有一个拥有全局环回的主实例，其他 > 是控制器。控制器可以通过向主设备发送命令来管理全局环回。 > 实例，并从中监听状态变化。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-audio-function createGlobalAudioLoopback(mode: AudioLoopbackMode, isController: boolean): Promise<AudioLoopback | null>--><!--Device-audio-function createGlobalAudioLoopback(mode: AudioLoopbackMode, isController: boolean): Promise<AudioLoopback | null>-End-->

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
| [6800101](../errorcode-audio.md#6800101-无效入参) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [6800104](../errorcode-audio.md#6800104-参数选项不支持) |
