# @ohos.deviceStatus.dragInteraction

拖拽功能模块，提供注册和取消拖拽状态监听的能力。

> **说明：**
> 
> - 本模块接口均为系统接口。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-unnamed-declare namespace dragInteraction--><!--Device-unnamed-declare namespace dragInteraction-End-->

**System capability:** SystemCapability.Msdp.DeviceStatus.Drag

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { dragInteraction } from 'kits/@kit.ArkUI';
```

## Summary

<!--Del-->
### Functions（系统接口）

| Name | Description |
| --- | --- |
| [getDataSummary](arkts-arkui-draginteraction-getdatasummary-f-sys.md#getdatasummary) | 获取所有拖拽对象的摘要。 |
| [off](arkts-arkui-draginteraction-off-f-sys.md#off) | 取消监听拖拽状态。 |
| [offDragStateChange](arkts-arkui-draginteraction-offdragstatechange-f-sys.md#offdragstatechange) | Disables listening for dragging state change events. |
| [on](arkts-arkui-draginteraction-on-f-sys.md#on) | 注册监听拖拽状态。 |
| [onDragStateChange](arkts-arkui-draginteraction-ondragstatechange-f-sys.md#ondragstatechange) | Listens for dragging state change events. |
| [setAppDragSwitchState](arkts-arkui-draginteraction-setappdragswitchstate-f-sys.md#setappdragswitchstate) | 控制统一拖拽适配应用开关。 |
| [setDragSwitchState](arkts-arkui-draginteraction-setdragswitchstate-f-sys.md#setdragswitchstate) | 控制统一拖拽功能总开关。 |
<!--DelEnd-->

<!--Del-->
### Interfaces（系统接口）

| Name | Description |
| --- | --- |
| [Summary](arkts-arkui-draginteraction-summary-i-sys.md) | 拖拽对象的数据摘要。 |
<!--DelEnd-->

<!--Del-->
### Enums（系统接口）

| Name | Description |
| --- | --- |
| [DragState](arkts-arkui-draginteraction-dragstate-e-sys.md) | 拖拽状态。 |
<!--DelEnd-->

