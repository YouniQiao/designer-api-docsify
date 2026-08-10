# OnCameraCaptureStateChangeCallback

```TypeScript
type OnCameraCaptureStateChangeCallback = (event: CameraCaptureStateChangeInfo) => void
```

当页面摄像设备状态发生改变时触发此回调。

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

<!--Device-unnamed-type OnCameraCaptureStateChangeCallback = (event: CameraCaptureStateChangeInfo) => void--><!--Device-unnamed-type OnCameraCaptureStateChangeCallback = (event: CameraCaptureStateChangeInfo) => void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [CameraCaptureStateChangeInfo](arkts-arkweb-cameracapturestatechangeinfo-i.md) | Yes | 网页摄像头状态发生改变时，返回原来的状态和改变后的状态。 |

