# OnMicrophoneCaptureStateChangeCallback

```TypeScript
export type OnMicrophoneCaptureStateChangeCallback = (event: MicrophoneCaptureStateChangeInfo) => void
```

The callback when microphone capturing state of current page has been changed.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export type OnMicrophoneCaptureStateChangeCallback = (event: MicrophoneCaptureStateChangeInfo) => void--><!--Device-unnamed-export type OnMicrophoneCaptureStateChangeCallback = (event: MicrophoneCaptureStateChangeInfo) => void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [MicrophoneCaptureStateChangeInfo](../arkts-components/arkts-arkweb-microphonecapturestatechangeinfo-i.md) | Yes | the microphone capturing state event. |

