# AudioDebuggingManager

实现音频调试功能。

**起始版本：** 26.0.0

<!--Device-audio-interface AudioDebuggingManager--><!--Device-audio-interface AudioDebuggingManager-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Core

## printAppInfo

```TypeScript
printAppInfo(fd: number): void
```

显示当前应用进程的完整运行时快照。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AudioDebuggingManager-printAppInfo(fd: int): void--><!--Device-AudioDebuggingManager-printAppInfo(fd: int): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fd | number | 是 |

## printCapturerInfo

```TypeScript
printCapturerInfo(capturer: AudioCapturer, fd: number): void
```

打印目标音频捕获程序实例的完整音频运行时快照。快照将包含流、管道、卷和设备信息。请注意，不同版本的信息详情和格式可能会有所不同，它只能用于手动调试，用户不应依赖实际功能实现或文件的信息内容提取。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AudioDebuggingManager-printCapturerInfo(capturer: AudioCapturer, fd: int): void--><!--Device-AudioDebuggingManager-printCapturerInfo(capturer: AudioCapturer, fd: int): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| capturer | [AudioCapturer](arkts-audio-audio-audiocapturer-i.md) | 是 |
| fd | number | 是 |

## printLoopbackInfo

```TypeScript
printLoopbackInfo(loopback: AudioLoopback, fd: number): void
```

打印目标音频环回实例的完整音频运行时快照。快照将包含环回状态、设备和效果信息。请注意，不同版本的信息详情和格式可能会有所不同，它只能用于手动调试，用户不应依赖实际功能实现或文件的信息内容提取。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AudioDebuggingManager-printLoopbackInfo(loopback: AudioLoopback, fd: int): void--><!--Device-AudioDebuggingManager-printLoopbackInfo(loopback: AudioLoopback, fd: int): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| loopback | [AudioLoopback](arkts-audio-audio-audioloopback-i.md) | 是 |
| fd | number | 是 |

## printRendererInfo

```TypeScript
printRendererInfo(renderer: AudioRenderer, fd: number): void
```

打印目标音频渲染器实例的完整音频运行时快照。快照将包含流、管道、卷和设备信息。请注意，不同版本的信息详情和格式可能会有所不同，它只能用于手动调试，用户不应依赖实际功能实现或文件的信息内容提取。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AudioDebuggingManager-printRendererInfo(renderer: AudioRenderer, fd: int): void--><!--Device-AudioDebuggingManager-printRendererInfo(renderer: AudioRenderer, fd: int): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| renderer | [AudioRenderer](arkts-audio-audio-audiorenderer-i.md) | 是 |
| fd | number | 是 |

## printSessionInfo

```TypeScript
printSessionInfo(session: AudioSessionManager, fd: number): void
```

打印目标音频会话管理器实例的完整音频运行时快照。快照将包含会话状态、场景、策略和设备信息。请注意，不同版本的信息详情和格式可能会有所不同，它只能用于手动调试，用户不应依赖实际功能实现或文件的信息内容提取。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AudioDebuggingManager-printSessionInfo(session: AudioSessionManager, fd: int): void--><!--Device-AudioDebuggingManager-printSessionInfo(session: AudioSessionManager, fd: int): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| session | [AudioSessionManager](arkts-audio-audio-audiosessionmanager-i.md) | 是 |
| fd | number | 是 |
