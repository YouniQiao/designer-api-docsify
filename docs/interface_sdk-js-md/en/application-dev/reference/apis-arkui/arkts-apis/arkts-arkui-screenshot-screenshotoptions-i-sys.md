# ScreenshotOptions (System API)

Describes the screenshot options.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-screenshot-interface ScreenshotOptions--><!--Device-screenshot-interface ScreenshotOptions-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { screenshot } from 'kits/@kit.ArkUI';
```

## displayId

```TypeScript
displayId?: long
```

ID of the [display](arkts-arkui-display-displaystate-e.md) device on which the screen region is to be captured. The value must be an integer.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-ScreenshotOptions-displayId?: long--><!--Device-ScreenshotOptions-displayId?: long-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

## imageSize

```TypeScript
imageSize?: Size
```

Region of the screen to capture. If no value is passed, the region of the logical screen associated with the specified display ID is returned.

**Type:** [Size](arkts-arkui-window-size-i.md)

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-ScreenshotOptions-imageSize?: Size--><!--Device-ScreenshotOptions-imageSize?: Size-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

## isCaptureFullOfScreen

```TypeScript
isCaptureFullOfScreen?: boolean
```

Whether to capture all displays on the current screen. If the screen contains multiple displays, the value  
**true** means that the entire screen is captured, and **false** means that only the region of the logical screen associated with the specified display ID is captured.

**Type:** boolean

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-ScreenshotOptions-isCaptureFullOfScreen?: boolean--><!--Device-ScreenshotOptions-isCaptureFullOfScreen?: boolean-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

## isNotificationNeeded

```TypeScript
isNotificationNeeded?: boolean
```

Whether to send a notification after a snapshot is captured. **true** to send, **false** otherwise. The default value is **true**. Such a notification can be listened for through  
[captureStatusChange](@ohos.display:display.on(type: 'captureStatusChange', callback: Callback&lt;boolean&gt;)).

**Type:** boolean

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-ScreenshotOptions-isNotificationNeeded?: boolean--><!--Device-ScreenshotOptions-isNotificationNeeded?: boolean-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

## rotation

```TypeScript
rotation?: int
```

Angle by which the captured image should be rotated. Currently, the value can be **0** only. The default value is  
**0**.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-ScreenshotOptions-rotation?: int--><!--Device-ScreenshotOptions-rotation?: int-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

## screenRect

```TypeScript
screenRect?: Rect
```

Region of the screen to capture. If no value is passed, the region of the logical screen associated with the specified display ID is returned.

**Type:** [Rect](../../apis-form-kit/arkts-apis/arkts-form-forminfo-rect-i.md)

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-ScreenshotOptions-screenRect?: Rect--><!--Device-ScreenshotOptions-screenRect?: Rect-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

