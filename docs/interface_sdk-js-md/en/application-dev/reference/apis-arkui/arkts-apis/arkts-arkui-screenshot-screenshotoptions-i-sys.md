# ScreenshotOptions (System API)

设置截取图像的信息。

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

表示截取图像的显示设备[Display](arkts-arkui-display-displaystate-e.md)的ID号，该参数应为整数。

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

表示截取图像的区域，不传值默认返回displayId所在逻辑屏的区域。

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

表示是否截取当前Screen上的所有display。对于一个Screen上有多个display的场景，为true表示截取整个Screen，false则只截取displayId所在逻辑屏的区域，默认值为false。

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

表示截取图像之后是否发送截屏通知，true表示发送截屏通知，false表示不发送截屏通知，默认值为true。截屏通知可以通过  
[captureStatusChange](@ohos.display:display.on(type: 'captureStatusChange', callback: Callback&lt;boolean&gt;))接口监听。

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

表示截取图像后要旋转的角度，当前仅支持输入值为0，默认值为0。

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

表示截取图像的区域，不传值默认返回displayId所在逻辑屏的区域。

**Type:** [Rect](../../apis-form-kit/arkts-apis/arkts-form-forminfo-rect-i.md)

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-ScreenshotOptions-screenRect?: Rect--><!--Device-ScreenshotOptions-screenRect?: Rect-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

