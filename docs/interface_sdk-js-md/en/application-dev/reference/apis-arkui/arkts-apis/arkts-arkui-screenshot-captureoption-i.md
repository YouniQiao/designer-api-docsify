# CaptureOption

Describes the capture options.

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-screenshot-interface CaptureOption--><!--Device-screenshot-interface CaptureOption-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## blackWindowIds

```TypeScript
blackWindowIds?: Array<int>
```

List of window IDs that are not displayed during screen capture. By default, this list is empty. Valid window IDs must be positive integers. Currently, this parameter applies only to  
[floating ball windows]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_. If a window ID does not correspond to a floating ball window, is not a positive integer, or does not exist, error code 401 is reported. You are advised to call  
[getFloatingBallWindowInfo()]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_to obtain the window ID of a floating ball window.

**Type:** Array&lt;int&gt;

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 21.

<!--Device-CaptureOption-blackWindowIds?: Array<int>--><!--Device-CaptureOption-blackWindowIds?: Array<int>-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## displayId

```TypeScript
displayId?: long
```

ID of the [display]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ to capture. The default value is **0**. The value must be an integer greater than or equal to 0. If a non-integer is passed, a parameter error is reported.

**Type:** long

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-CaptureOption-displayId?: long--><!--Device-CaptureOption-displayId?: long-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

