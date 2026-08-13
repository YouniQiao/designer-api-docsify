# ScreenCaptureMonitor (System API)

A class that provides APIs to query and monitor the system screen recorder status. Before calling any API, you must use getScreenCaptureMonitor() to obtain a ScreenCaptureMonitor instance.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-media-interface ScreenCaptureMonitor--><!--Device-media-interface ScreenCaptureMonitor-End-->

**System capability:** SystemCapability.Multimedia.Media.AVScreenCapture

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { media } from '@kit.MediaKit';
```

## offSystemScreenRecorder

```TypeScript
offSystemScreenRecorder(callback?: Callback<ScreenCaptureEvent>): void
```

Unsubscribes from state change events of the system screen recorder. This event is triggered when the state of the system screen recorder changes.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-ScreenCaptureMonitor-offSystemScreenRecorder(callback?: Callback<ScreenCaptureEvent>): void--><!--Device-ScreenCaptureMonitor-offSystemScreenRecorder(callback?: Callback<ScreenCaptureEvent>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVScreenCapture

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ScreenCaptureEvent](arkts-media-media-screencaptureevent-e-sys.md)&gt; | No | Callback invoked when the event is triggered, where ScreenCaptureEvent indicates the new state. If this parameter is not specified, the last subscription event is canceled. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System App. |

## off_systemScreenRecorder

```TypeScript
off(type: 'systemScreenRecorder', callback?: Callback<ScreenCaptureEvent>): void
```

Unsubscribes from state change events of the system screen recorder.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

<!--Device-ScreenCaptureMonitor-off(type: 'systemScreenRecorder', callback?: Callback<ScreenCaptureEvent>): void--><!--Device-ScreenCaptureMonitor-off(type: 'systemScreenRecorder', callback?: Callback<ScreenCaptureEvent>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVScreenCapture

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'systemScreenRecorder' | Yes | Event type, which is **'systemScreenRecorder'** in this case. This event is triggered when the state of the system screen recorder changes. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ScreenCaptureEvent](arkts-media-media-screencaptureevent-e-sys.md)&gt; | No | Callback invoked when the event is triggered, where ScreenCaptureEvent indicates the new state. If this parameter is not specified, the last subscription event is canceled. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System App. |

## Examples

```TypeScript
screenCaptureMonitor.off('systemScreenRecorder');
```

## onSystemScreenRecorder

```TypeScript
onSystemScreenRecorder(callback: Callback<ScreenCaptureEvent>): void
```

Subscribes to state change events of the system screen recorder. From the ScreenCaptureEvent event reported, you can determine whether the system screen recorder is working. This event is triggered when the state of the system screen recorder changes.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-ScreenCaptureMonitor-onSystemScreenRecorder(callback: Callback<ScreenCaptureEvent>): void--><!--Device-ScreenCaptureMonitor-onSystemScreenRecorder(callback: Callback<ScreenCaptureEvent>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVScreenCapture

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ScreenCaptureEvent](arkts-media-media-screencaptureevent-e-sys.md)&gt; | Yes | Callback invoked when the event is triggered, where ScreenCaptureEvent indicates the new state. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System App. |

## on_systemScreenRecorder

```TypeScript
on(type: 'systemScreenRecorder', callback: Callback<ScreenCaptureEvent>): void
```

Subscribes to state change events of the system screen recorder. From the ScreenCaptureEvent event reported, you can determine whether the system screen recorder is working.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

<!--Device-ScreenCaptureMonitor-on(type: 'systemScreenRecorder', callback: Callback<ScreenCaptureEvent>): void--><!--Device-ScreenCaptureMonitor-on(type: 'systemScreenRecorder', callback: Callback<ScreenCaptureEvent>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVScreenCapture

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'systemScreenRecorder' | Yes | Event type, which is **'systemScreenRecorder'** in this case. This event is triggered when the state of the system screen recorder changes. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ScreenCaptureEvent](arkts-media-media-screencaptureevent-e-sys.md)&gt; | Yes | Callback invoked when the event is triggered, where ScreenCaptureEvent indicates the new state. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System App. |

## Examples

```TypeScript
// This event is reported when the state of the system screen recorder changes.
screenCaptureMonitor.on('systemScreenRecorder', (event: media.ScreenCaptureEvent) => { 
  // Set the 'systemScreenRecorder' event callback.
  console.info(`system ScreenRecorder event: ${event}`);
})
```

## isSystemScreenRecorderWorking

```TypeScript
readonly isSystemScreenRecorderWorking: boolean
```

Whether the system screen recorder is working.

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-ScreenCaptureMonitor-readonly isSystemScreenRecorderWorking: boolean--><!--Device-ScreenCaptureMonitor-readonly isSystemScreenRecorderWorking: boolean-End-->

**System capability:** SystemCapability.Multimedia.Media.AVScreenCapture

**System API:** This is a system API.

