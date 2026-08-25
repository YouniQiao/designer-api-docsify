# AudioDebuggingManager

音频调试管理器，用于音频运行时调试，包括获取快照信息等功能，用于定位音频播放、录音、耳返、会话等场景中的异常问题。 **起始版本：** 26.0.0

> **说明：**&gt;
> 快照信息的内容和格式后续会根据开发者使用情况和反馈建议优化调整，随版本迭代可能发生变化，所以仅供人工调试参考，不建议开发者依据快照信息开发功能逻辑。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**系统能力：** SystemCapability.Multimedia.Audio.Core

## 导入模块

```TypeScript
import { audio } from '@kit.AudioKit';
```

## printAppInfo

ArkTS-Dyn:
```TypeScript
printAppInfo(fd: number): void
```

ArkTS-Sta:
```TypeScript
printAppInfo(fd: int): void
```

打印当前应用进程的完整音频运行时快照。快照包含所有播放流、录音流和音频会话信息。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fd | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |

## printCapturerInfo

ArkTS-Dyn:
```TypeScript
printCapturerInfo(capturer: AudioCapturer, fd: number): void
```

ArkTS-Sta:
```TypeScript
printCapturerInfo(capturer: AudioCapturer, fd: int): void
```

打印指定录音实例的完整音频运行时快照。快照包含流信息、通路信息、音量和设备信息。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| capturer | [AudioCapturer](arkts-audio-audio-audiocapturer-i.md) | 是 |
| fd | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |

## printLoopbackInfo

ArkTS-Dyn:
```TypeScript
printLoopbackInfo(loopback: AudioLoopback, fd: number): void
```

ArkTS-Sta:
```TypeScript
printLoopbackInfo(loopback: AudioLoopback, fd: int): void
```

打印指定耳返实例的完整音频运行时快照。快照包含耳返状态、设备和音效信息。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| loopback | [AudioLoopback](arkts-audio-audio-audioloopback-i.md) | 是 |
| fd | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |

## printRendererInfo

ArkTS-Dyn:
```TypeScript
printRendererInfo(renderer: AudioRenderer, fd: number): void
```

ArkTS-Sta:
```TypeScript
printRendererInfo(renderer: AudioRenderer, fd: int): void
```

打印指定音频播放实例的完整音频运行时快照。快照包含流信息、通路信息、音量和设备信息。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| renderer | [AudioRenderer](arkts-audio-audio-audiorenderer-i.md) | 是 |
| fd | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |

## printSessionInfo

ArkTS-Dyn:
```TypeScript
printSessionInfo(session: AudioSessionManager, fd: number): void
```

ArkTS-Sta:
```TypeScript
printSessionInfo(session: AudioSessionManager, fd: int): void
```

打印指定会话管理器实例的完整音频运行时快照。快照包含会话状态、场景、策略和设备信息。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| session | [AudioSessionManager](arkts-audio-audio-audiosessionmanager-i.md) | 是 |
| fd | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |
