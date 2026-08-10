# createGlobalAudioLoopback (System API)

## Modules to Import

```TypeScript
import { audio } from 'kits/@kit.AudioKit';
```

## createGlobalAudioLoopback

```TypeScript
function createGlobalAudioLoopback(mode: AudioLoopbackMode, isController: boolean): Promise<AudioLoopback | null>
```

创建全局音频环回实例，提供低时延入耳监听功能。硬件音频环回只能在支持的平台中创建，应用程序可以使用  
> **说明：**
> {@link AudioStreamManager#isAudioLoopbackSupported}先检查。
> 系统中应该只有一个拥有全局环回的主实例，其他
> 是控制器。控制器可以通过向主设备发送命令来管理全局环回。
> 实例，并从中监听状态变化。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-audio-function createGlobalAudioLoopback(mode: AudioLoopbackMode, isController: boolean): Promise<AudioLoopback | null>--><!--Device-audio-function createGlobalAudioLoopback(mode: AudioLoopbackMode, isController: boolean): Promise<AudioLoopback | null>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mode | [AudioLoopbackMode](arkts-audio-audio-audioloopbackmode-e.md) | Yes | 要创建的音频环回模式 |
| isController | boolean | Yes | 创建拥有音频环回或仅拥有控制器的对象 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;AudioLoopback \| null&gt; | Promise用于返回音频环回实例。 或者发生错误时为null。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6800101 | Parameter verification failed. |
| 202 | Caller is not a system application. |
| 6800104 | Loopback mode is unsupported. |

