# BlanklessFrameInterpolationInfo

Defines the frame interpolation information. Device behavior differences: Only the mobile phone is supported. For other devices, 801 is returned.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-webview-interface BlanklessFrameInterpolationInfo--><!--Device-webview-interface BlanklessFrameInterpolationInfo-End-->

**System capability:** SystemCapability.Web.Webview.Core

## key

```TypeScript
key: string
```

Key value that uniquely identifies the page. Device behavior differences: Only the mobile phone is supported. For other devices, 801 is returned.

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-BlanklessFrameInterpolationInfo-key: string--><!--Device-BlanklessFrameInterpolationInfo-key: string-End-->

**System capability:** SystemCapability.Web.Webview.Core

## reason

```TypeScript
reason: string
```

Reason for the frame interpolation failure. Device behavior differences: Only the mobile phone is supported. For other devices, 801 is returned.

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-BlanklessFrameInterpolationInfo-reason: string--><!--Device-BlanklessFrameInterpolationInfo-reason: string-End-->

**System capability:** SystemCapability.Web.Webview.Core

## state

```TypeScript
state: BlanklessFrameInterpolationState
```

Current frame interpolation state. Device behavior differences: Only the mobile phone is supported. For other devices, 801 is returned.

**Type:** [BlanklessFrameInterpolationState](../../apis-arkweb/arkts-apis/arkts-arkweb-webview-blanklessframeinterpolationstate-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-BlanklessFrameInterpolationInfo-state: BlanklessFrameInterpolationState--><!--Device-BlanklessFrameInterpolationInfo-state: BlanklessFrameInterpolationState-End-->

**System capability:** SystemCapability.Web.Webview.Core

## timestamp

```TypeScript
timestamp: int
```

Time when a frame is interpolated or removed. Device behavior differences: Only the mobile phone is supported. For other devices, 801 is returned. The value must be an integer. <br>Unit: ms.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-BlanklessFrameInterpolationInfo-timestamp: int--><!--Device-BlanklessFrameInterpolationInfo-timestamp: int-End-->

**System capability:** SystemCapability.Web.Webview.Core

