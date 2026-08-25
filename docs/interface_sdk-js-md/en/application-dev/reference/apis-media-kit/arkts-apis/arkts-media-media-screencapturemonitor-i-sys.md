# ScreenCaptureMonitor (System API)

A class that provides APIs to query and monitor the system screen recorder status. Before calling any API, you must use getScreenCaptureMonitor() to obtain a ScreenCaptureMonitor instance.

**Since:** 18

**System capability:** SystemCapability.Multimedia.Media.AVScreenCapture

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { media } from 'kits/@kit.MediaKit';
```

## off('systemScreenRecorder')

```TypeScript
off(type: 'systemScreenRecorder', callback?: Callback<ScreenCaptureEvent>): void
```

Unsubscribes from state change events of the system screen recorder.

**Since:** 18

**System capability:** SystemCapability.Multimedia.Media.AVScreenCapture

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'systemScreenRecorder' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ScreenCaptureEvent](arkts-media-media-screencaptureevent-e-sys.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## on('systemScreenRecorder')

```TypeScript
on(type: 'systemScreenRecorder', callback: Callback<ScreenCaptureEvent>): void
```

Subscribes to state change events of the system screen recorder. From the ScreenCaptureEvent event reported, you can determine whether the system screen recorder is working.

**Since:** 18

**System capability:** SystemCapability.Multimedia.Media.AVScreenCapture

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'systemScreenRecorder' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ScreenCaptureEvent](arkts-media-media-screencaptureevent-e-sys.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## isSystemScreenRecorderWorking

```TypeScript
readonly isSystemScreenRecorderWorking: boolean
```

Whether the system screen recorder is working.

**Type:** boolean

**Since:** 18

**System capability:** SystemCapability.Multimedia.Media.AVScreenCapture

**System API:** This is a system API.
