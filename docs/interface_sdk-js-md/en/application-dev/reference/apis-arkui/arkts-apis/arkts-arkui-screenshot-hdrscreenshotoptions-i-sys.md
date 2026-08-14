# HdrScreenshotOptions (System API)

Describes the HDR screenshot options.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-screenshot-interface HdrScreenshotOptions--><!--Device-screenshot-interface HdrScreenshotOptions-End-->

**System capability:** SystemCapability.Window.SessionManager

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { screenshot } from 'screenshot';
```

## displayId

```TypeScript
displayId?: long
```

ID of the [display](arkts-arkui-display-displaystate-e.md#DisplayState) device on which the screen region is to be captured. The value must be an integer. The default value is **0**.

**Type:** long

**Default:** The ID of the current display. The value is a positive integer greater than or equal to 0.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-HdrScreenshotOptions-displayId?: long--><!--Device-HdrScreenshotOptions-displayId?: long-End-->

**System capability:** SystemCapability.Window.SessionManager

**System API:** This is a system API.

## displayIntent

```TypeScript
displayIntent?: DisplayIntentType
```

screenshot display intent type.

**Type:** [DisplayIntentType](arkts-arkui-screenshot-displayintenttype-e-sys.md)

**Default:** DisplayIntentType.CANONICAL

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-HdrScreenshotOptions-displayIntent?: DisplayIntentType--><!--Device-HdrScreenshotOptions-displayIntent?: DisplayIntentType-End-->

**System capability:** SystemCapability.Window.SessionManager

**System API:** This is a system API.

## isCaptureFullOfScreen

```TypeScript
isCaptureFullOfScreen?: boolean
```

Whether to capture all displays on the current screen. If the screen contains multiple displays, the value **true** means that the entire screen is captured, and **false** means that only the region of the logical screen associated with the specified display ID is captured. The default value is **false**.

**Type:** boolean

**Default:** false

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-HdrScreenshotOptions-isCaptureFullOfScreen?: boolean--><!--Device-HdrScreenshotOptions-isCaptureFullOfScreen?: boolean-End-->

**System capability:** SystemCapability.Window.SessionManager

**System API:** This is a system API.

## isNotificationNeeded

```TypeScript
isNotificationNeeded?: boolean
```

Whether to send a notification after a snapshot is captured. **true** to send, **false** otherwise. The default value is **true**. Such a notification can be listened for through captureStatusChange.

**Type:** boolean

**Default:** true

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-HdrScreenshotOptions-isNotificationNeeded?: boolean--><!--Device-HdrScreenshotOptions-isNotificationNeeded?: boolean-End-->

**System capability:** SystemCapability.Window.SessionManager

**System API:** This is a system API.

