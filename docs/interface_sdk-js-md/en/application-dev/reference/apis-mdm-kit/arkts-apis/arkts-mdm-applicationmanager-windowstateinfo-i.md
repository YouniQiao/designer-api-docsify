# WindowStateInfo

应用窗口状态信息。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

<!--Device-applicationManager-interface WindowStateInfo--><!--Device-applicationManager-interface WindowStateInfo-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## Modules to Import

```TypeScript
import { applicationManager } from 'kits/@kit.MDMKit';
```

## isOnDock

```TypeScript
isOnDock: boolean
```

表示应用窗口是否在底部Dock栏上显示。PC/2in1设备和Tablet设备的PC模式的应用在底部Dock栏上返回true，其他设备返回false。

**Type:** boolean

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WindowStateInfo-isOnDock: boolean--><!--Device-WindowStateInfo-isOnDock: boolean-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## name

```TypeScript
name: string
```

应用窗口名称。

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WindowStateInfo-name: string--><!--Device-WindowStateInfo-name: string-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## state

```TypeScript
state: WindowState
```

应用窗口状态。

**Type:** [WindowState](arkts-mdm-applicationmanager-windowstate-e.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WindowStateInfo-state: WindowState--><!--Device-WindowStateInfo-state: WindowState-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## windowId

```TypeScript
windowId: number
```

应用窗口ID。

**Type:** number

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WindowStateInfo-windowId: number--><!--Device-WindowStateInfo-windowId: number-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

