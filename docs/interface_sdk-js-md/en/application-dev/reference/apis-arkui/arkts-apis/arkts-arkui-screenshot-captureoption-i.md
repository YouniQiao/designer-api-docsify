# CaptureOption

Describes the capture options.

**Since:** 23

<!--Device-screenshot-interface CaptureOption--><!--Device-screenshot-interface CaptureOption-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## Modules to Import

```TypeScript
import { screenshot } from '@kit.ArkUI';
```

## blackWindowIds

```TypeScript
blackWindowIds?: Array<int>
```

List of window IDs that are not displayed during screen capture. By default, this list is empty. Valid window IDs must be positive integers. Currently, this parameter applies only to [floating ball windows](arkts-window-floatingball.md#ohoswindowfloatingball). If a window ID does not correspond to a floating ball window, is not a positive integer, or does not exist, error code 401 is reported. You are advised to call [getFloatingBallWindowInfo()](arkts-arkui-floatingball-floatingballcontroller-i.md#getfloatingballwindowinfo) to obtain the window ID of a floating ball window.

**Type:** Array&lt;int&gt;

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-CaptureOption-blackWindowIds?: Array<int>--><!--Device-CaptureOption-blackWindowIds?: Array<int>-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## displayId

```TypeScript
displayId?: long
```

ID of the [display](arkts-arkui-display-displaystate-e.md#displaystate) to capture. The default value is **0**. The value must be an integer greater than or equal to 0. If a non-integer is passed, error code 401 is reported.

**Type:** long

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-CaptureOption-displayId?: long--><!--Device-CaptureOption-displayId?: long-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

