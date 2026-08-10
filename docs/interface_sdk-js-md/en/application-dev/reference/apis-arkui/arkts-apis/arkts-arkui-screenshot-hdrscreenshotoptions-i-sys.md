# HdrScreenshotOptions (System API)

设置截取HDR图像的信息。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-screenshot-interface HdrScreenshotOptions--><!--Device-screenshot-interface HdrScreenshotOptions-End-->

**System capability:** SystemCapability.Window.SessionManager

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { screenshot } from 'kits/@kit.ArkUI';
```

## displayId

```TypeScript
displayId?: long
```

表示截取图像的显示设备[Display](arkts-arkui-display-displaystate-e.md)的ID号，该参数应为整数。默认为0。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Default:** The ID of the current display. The value is a positive integer greater than or equal to 0.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-HdrScreenshotOptions-displayId?: long--><!--Device-HdrScreenshotOptions-displayId?: long-End-->

**System capability:** SystemCapability.Window.SessionManager

**System API:** This is a system API.

## displayIntent

```TypeScript
displayIntent?: DisplayIntentType
```

截取图像的显示类型。

**Type:** [DisplayIntentType](arkts-arkui-screenshot-displayintenttype-e-sys.md)

**Default:** DisplayIntentType.CANONICAL

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-HdrScreenshotOptions-displayIntent?: DisplayIntentType--><!--Device-HdrScreenshotOptions-displayIntent?: DisplayIntentType-End-->

**System capability:** SystemCapability.Window.SessionManager

**System API:** This is a system API.

## isCaptureFullOfScreen

```TypeScript
isCaptureFullOfScreen?: boolean
```

表示是否截取当前物理屏上所有DisplayId对应的逻辑屏。对于一个物理屏上有多个DisplayId的场景，true表示截取整个物理屏，false表示只截取DisplayId所在区域的逻辑屏。默认值为false。

**Type:** boolean

**Default:** false

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-HdrScreenshotOptions-isCaptureFullOfScreen?: boolean--><!--Device-HdrScreenshotOptions-isCaptureFullOfScreen?: boolean-End-->

**System capability:** SystemCapability.Window.SessionManager

**System API:** This is a system API.

## isNotificationNeeded

```TypeScript
isNotificationNeeded?: boolean
```

表示截取图像之后是否发送截屏通知，true表示发送截屏通知，false表示不发送截屏通知，默认值为true。截屏通知可以通过  
[captureStatusChange](@ohos.display:display.on(type: 'captureStatusChange', callback: Callback&lt;boolean&gt;))接口监听。

**Type:** boolean

**Default:** true

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-HdrScreenshotOptions-isNotificationNeeded?: boolean--><!--Device-HdrScreenshotOptions-isNotificationNeeded?: boolean-End-->

**System capability:** SystemCapability.Window.SessionManager

**System API:** This is a system API.

