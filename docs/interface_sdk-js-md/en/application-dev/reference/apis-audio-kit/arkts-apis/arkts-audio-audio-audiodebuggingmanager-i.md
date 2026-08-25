# AudioDebuggingManager

Provides audio debug management capabilities.

**Since:** 26.0.0

**System capability:** SystemCapability.Multimedia.Audio.Core

## Modules to Import

```TypeScript
import { audio } from 'kits/@kit.AudioKit';
```

## printAppInfo

```TypeScript
printAppInfo(fd: number): void
```

Prints full audio runtime snapshot for current app process. The snapshot will contain all audio renderers, capturers, audio session information. Note that the information details and format may vary from different version, it can only be used for manual debugging, user should not rely on the information for actual function realization or file content extraction.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Multimedia.Audio.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| fd | number | Yes |

## printCapturerInfo

```TypeScript
printCapturerInfo(capturer: AudioCapturer, fd: number): void
```

Prints full audio runtime snapshot for target audio capturer instance. The snapshot will contain the stream, pipe, volume and device information. Note that the information details and format may vary from different version, it can only be used for manual debugging, user should not rely on the information for actual function realization or file content extraction.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Multimedia.Audio.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| capturer | [AudioCapturer](arkts-audio-audio-audiocapturer-i.md) | Yes |
| fd | number | Yes |

## printLoopbackInfo

```TypeScript
printLoopbackInfo(loopback: AudioLoopback, fd: number): void
```

Prints full audio runtime snapshot for target audio loopback instance. The snapshot will contain the loopback status, device and effect information. Note that the information details and format may vary from different version, it can only be used for manual debugging, user should not rely on the information for actual function realization or file content extraction.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Multimedia.Audio.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| loopback | [AudioLoopback](arkts-audio-audio-audioloopback-i.md) | Yes |
| fd | number | Yes |

## printRendererInfo

```TypeScript
printRendererInfo(renderer: AudioRenderer, fd: number): void
```

Prints full audio runtime snapshot for target audio renderer instance. The snapshot will contain the stream, pipe, volume and device information. Note that the information details and format may vary from different version, it can only be used for manual debugging, user should not rely on the information for actual function realization or file content extraction.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Multimedia.Audio.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| renderer | [AudioRenderer](arkts-audio-audio-audiorenderer-i.md) | Yes |
| fd | number | Yes |

## printSessionInfo

```TypeScript
printSessionInfo(session: AudioSessionManager, fd: number): void
```

Prints full audio runtime snapshot for target audio session manager instance. The snapshot will contain the session status, scene, strategy and device information. Note that the information details and format may vary from different version, it can only be used for manual debugging, user should not rely on the information for actual function realization or file content extraction.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Multimedia.Audio.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| session | [AudioSessionManager](arkts-audio-audio-audiosessionmanager-i.md) | Yes |
| fd | number | Yes |
