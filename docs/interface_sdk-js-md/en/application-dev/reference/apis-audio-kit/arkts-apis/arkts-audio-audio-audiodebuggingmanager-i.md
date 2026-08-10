# AudioDebuggingManager

实现音频调试功能。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-audio-interface AudioDebuggingManager--><!--Device-audio-interface AudioDebuggingManager-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

## Modules to Import

```TypeScript
import { audio } from 'kits/@kit.AudioKit';
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

显示当前应用进程的完整运行时快照。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioDebuggingManager-printAppInfo(fd: int): void--><!--Device-AudioDebuggingManager-printAppInfo(fd: int): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fd | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | fd为文件句柄，表示快照信息将要写入的位置。 如果fd小于0，则将快照信息打印到运行日志中，否则快照将写入文件。 取值限定为整数。 |

## printCapturerInfo

ArkTS-Dyn:
```TypeScript
printCapturerInfo(capturer: AudioCapturer, fd: number): void
```

ArkTS-Sta:
```TypeScript
printCapturerInfo(capturer: AudioCapturer, fd: int): void
```

打印目标音频捕获程序实例的完整音频运行时快照。快照将包含流、管道、卷和设备信息。请注意，不同版本的信息详情和格式可能会有所不同，它只能用于手动调试，用户不应依赖实际功能实现或文件的信息内容提取。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioDebuggingManager-printCapturerInfo(capturer: AudioCapturer, fd: int): void--><!--Device-AudioDebuggingManager-printCapturerInfo(capturer: AudioCapturer, fd: int): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| capturer | [AudioCapturer](arkts-audio-audio-audiocapturer-i.md) | Yes | 目标音频捕获程序实例以打印快照。 取值限定为整数。 |
| fd | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | fd是文件描述符，表示快照信息的位置 写入到。如果fd小于0或无可写，则快照信息将打印到 运行日志，否则快照将写入文件。 取值限定为整数。 |

## printLoopbackInfo

ArkTS-Dyn:
```TypeScript
printLoopbackInfo(loopback: AudioLoopback, fd: number): void
```

ArkTS-Sta:
```TypeScript
printLoopbackInfo(loopback: AudioLoopback, fd: int): void
```

打印目标音频环回实例的完整音频运行时快照。快照将包含环回状态、设备和效果信息。请注意，不同版本的信息详情和格式可能会有所不同，它只能用于手动调试，用户不应依赖实际功能实现或文件的信息内容提取。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioDebuggingManager-printLoopbackInfo(loopback: AudioLoopback, fd: int): void--><!--Device-AudioDebuggingManager-printLoopbackInfo(loopback: AudioLoopback, fd: int): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| loopback | [AudioLoopback](arkts-audio-audio-audioloopback-i.md) | Yes | 目标音频环回实例以打印快照。 取值限定为整数。 |
| fd | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | fd是文件描述符，表示快照信息的位置 写入到。如果fd小于0或无可写，则快照信息将打印到 运行日志，否则快照将写入文件。 取值限定为整数。 |

## printRendererInfo

ArkTS-Dyn:
```TypeScript
printRendererInfo(renderer: AudioRenderer, fd: number): void
```

ArkTS-Sta:
```TypeScript
printRendererInfo(renderer: AudioRenderer, fd: int): void
```

打印目标音频渲染器实例的完整音频运行时快照。快照将包含流、管道、卷和设备信息。请注意，不同版本的信息详情和格式可能会有所不同，它只能用于手动调试，用户不应依赖实际功能实现或文件的信息内容提取。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioDebuggingManager-printRendererInfo(renderer: AudioRenderer, fd: int): void--><!--Device-AudioDebuggingManager-printRendererInfo(renderer: AudioRenderer, fd: int): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| renderer | [AudioRenderer](arkts-audio-audio-audiorenderer-i.md) | Yes | 目标音频渲染器实例以打印快照。 取值限定为整数。 |
| fd | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | fd是文件描述符，表示快照信息的位置 写入到。如果fd小于0或无可写，则快照信息将打印到 运行日志，否则快照将写入文件。 取值限定为整数。 |

## printSessionInfo

ArkTS-Dyn:
```TypeScript
printSessionInfo(session: AudioSessionManager, fd: number): void
```

ArkTS-Sta:
```TypeScript
printSessionInfo(session: AudioSessionManager, fd: int): void
```

打印目标音频会话管理器实例的完整音频运行时快照。快照将包含会话状态、场景、策略和设备信息。请注意，不同版本的信息详情和格式可能会有所不同，它只能用于手动调试，用户不应依赖实际功能实现或文件的信息内容提取。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioDebuggingManager-printSessionInfo(session: AudioSessionManager, fd: int): void--><!--Device-AudioDebuggingManager-printSessionInfo(session: AudioSessionManager, fd: int): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| session | [AudioSessionManager](arkts-audio-audio-audiosessionmanager-i.md) | Yes | 目标音频会话管理器实例以打印快照。 取值限定为整数。 |
| fd | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | fd是文件描述符，表示快照信息的位置 写入到。如果fd小于0或无可写，则快照信息将打印到 运行日志，否则快照将写入文件。 取值限定为整数。 |

