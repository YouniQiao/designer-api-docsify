# CaptureOption

设置截取图像的信息。

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-screenshot-interface CaptureOption--><!--Device-screenshot-interface CaptureOption-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## Modules to Import

```TypeScript
import { screenshot } from 'kits/@kit.ArkUI';
```

## blackWindowIds

```TypeScript
blackWindowIds?: Array<int>
```

表示截取图像时不显示的窗口ID列表，默认为空。窗口ID应为大于0的整数，目前仅[闪控球窗口](arkts-window-floatingball.md)生效，窗口ID为非闪控球窗口、非整数、小于等于0、或者不存在的窗口ID时报参数错误，错误码为401。推荐使用  
[getFloatingBallWindowInfo()](arkts-arkui-floatingball-floatingballcontroller-i.md#getfloatingballwindowinfo)方法获取闪控球窗口ID属性。

**Type:** ArkTS-Dyn: Array&lt;number&gt;  <br>ArkTS-Sta：Array&lt;int&gt;

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 21.

<!--Device-CaptureOption-blackWindowIds?: Array<int>--><!--Device-CaptureOption-blackWindowIds?: Array<int>-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## displayId

```TypeScript
displayId?: long
```

表示截取图像的显示设备[Display](arkts-arkui-display-displaystate-e.md)的ID号，默认为0，该参数应为大于或等于0的整数，非整数会报参数错误。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-CaptureOption-displayId?: long--><!--Device-CaptureOption-displayId?: long-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

