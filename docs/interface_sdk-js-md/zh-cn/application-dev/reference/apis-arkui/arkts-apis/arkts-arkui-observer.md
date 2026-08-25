# @ohos.arkui.observer

UIObserver提供了UI组件行为变化的无感监听能力，支持监听Navigation页面状态变化（NavDestination）、滚动事件、路由页面状态、屏幕像素密度变化、绘制指令下发、布局完成、页面切换等多种UI组件行为。 开发者可以通过该模块实现对UI组件状态的实时感知和追踪，适用于需要监控页面生命周期、处理滚动事件、优化渲染性能等场景，帮助开发者更好地理解和管理UI组件的行为变化。无感监听是指在组件状态变化时， 系统自动触发回调函数通知开发者，无需开发者手动轮询或主动查询组件状态。监听器通过注册回调函数实现，当目标组件状态改变时，系统内部的事件分发机制会调用已注册的回调函数，携带状态变化信息。

> **说明：**

> - 以下API需先使用UIContext中的[getUIObserver](arkts-arkui-arkui-uicontext-uicontext-c.md#getuiobserver)方法获取到UIObserver对象，再通过该对象调用对应方法。

> - UIObserver仅能监听到本进程内的UI组件状态变化信息，
> - 不支持获取<!--Del-->UIExtensionComponent等<!--DelEnd-->跨进程场景的信息。

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
import { uiObserver } from '@kit.ArkUI';
```

## 汇总

### 函数

| 名称 |
| --- |
| [off](arkts-arkui-uiobserver-off-f.md#offnavdestinationupdate) |
| [off](arkts-arkui-uiobserver-off-f.md#offnavdestinationupdate) |
| [off](arkts-arkui-uiobserver-off-f.md#offscrollevent) |
| [off](arkts-arkui-uiobserver-off-f.md#offscrollevent) |
| [off](arkts-arkui-uiobserver-off-f.md#offrouterpageupdate) |
| [off](arkts-arkui-uiobserver-off-f.md#offdensityupdate) |
| [off](arkts-arkui-uiobserver-off-f.md#offwilldraw) |
| [off](arkts-arkui-uiobserver-off-f.md#offdidlayout) |
| [off](arkts-arkui-uiobserver-off-f.md#offtabcontentupdate) |
| [off](arkts-arkui-uiobserver-off-f.md#offtabcontentupdate) |
| [off](arkts-arkui-uiobserver-off-f.md#offnavdestinationswitch) |
| [off](arkts-arkui-uiobserver-off-f.md#offnavdestinationswitch) |
| [offDensityUpdate](arkts-arkui-uiobserver-offdensityupdate-f.md) |
| [offDidLayout](arkts-arkui-uiobserver-offdidlayout-f.md) |
| [offNavDestinationSwitch](arkts-arkui-uiobserver-offnavdestinationswitch-f.md) |
| [offNavDestinationSwitch](arkts-arkui-uiobserver-offnavdestinationswitch-f.md) |
| [offNavDestinationUpdate](arkts-arkui-uiobserver-offnavdestinationupdate-f.md) |
| [offNavDestinationUpdate](arkts-arkui-uiobserver-offnavdestinationupdate-f.md) |
| [offRouterPageUpdate](arkts-arkui-uiobserver-offrouterpageupdate-f.md) |
| [offScrollEvent](arkts-arkui-uiobserver-offscrollevent-f.md) |
| [offScrollEvent](arkts-arkui-uiobserver-offscrollevent-f.md) |
| [offTabContentUpdate](arkts-arkui-uiobserver-offtabcontentupdate-f.md) |
| [offTabContentUpdate](arkts-arkui-uiobserver-offtabcontentupdate-f.md) |
| [offWillDraw](arkts-arkui-uiobserver-offwilldraw-f.md) |
| [on](arkts-arkui-uiobserver-on-f.md#onnavdestinationupdate) |
| [on](arkts-arkui-uiobserver-on-f.md#onnavdestinationupdate) |
| [on](arkts-arkui-uiobserver-on-f.md#onscrollevent) |
| [on](arkts-arkui-uiobserver-on-f.md#onscrollevent) |
| [on](arkts-arkui-uiobserver-on-f.md#onrouterpageupdate) |
| [on](arkts-arkui-uiobserver-on-f.md#ondensityupdate) |
| [on](arkts-arkui-uiobserver-on-f.md#onwilldraw) |
| [on](arkts-arkui-uiobserver-on-f.md#ondidlayout) |
| [on](arkts-arkui-uiobserver-on-f.md#ontabcontentupdate) |
| [on](arkts-arkui-uiobserver-on-f.md#ontabcontentupdate) |
| [on](arkts-arkui-uiobserver-on-f.md#onnavdestinationswitch) |
| [on](arkts-arkui-uiobserver-on-f.md#onnavdestinationswitch) |
| [onDensityUpdate](arkts-arkui-uiobserver-ondensityupdate-f.md) |
| [onDidLayout](arkts-arkui-uiobserver-ondidlayout-f.md) |
| [onNavDestinationSwitch](arkts-arkui-uiobserver-onnavdestinationswitch-f.md) |
| [onNavDestinationSwitch](arkts-arkui-uiobserver-onnavdestinationswitch-f.md) |
| [onNavDestinationUpdate](arkts-arkui-uiobserver-onnavdestinationupdate-f.md) |
| [onNavDestinationUpdate](arkts-arkui-uiobserver-onnavdestinationupdate-f.md) |
| [onRouterPageUpdate](arkts-arkui-uiobserver-onrouterpageupdate-f.md) |
| [onScrollEvent](arkts-arkui-uiobserver-onscrollevent-f.md) |
| [onScrollEvent](arkts-arkui-uiobserver-onscrollevent-f.md) |
| [onTabContentUpdate](arkts-arkui-uiobserver-ontabcontentupdate-f.md) |
| [onTabContentUpdate](arkts-arkui-uiobserver-ontabcontentupdate-f.md) |
| [onWillDraw](arkts-arkui-uiobserver-onwilldraw-f.md) |

### 类

| 名称 |
| --- |
| [DensityInfo](arkts-arkui-uiobserver-densityinfo-c.md) |
| [RouterPageInfo](arkts-arkui-uiobserver-routerpageinfo-c.md) |
| [WindowSizeLayoutBreakpointInfo](arkts-arkui-uiobserver-windowsizelayoutbreakpointinfo-c.md) |

### 接口

| 名称 |
| --- |
| [NavDestinationInfo](arkts-arkui-uiobserver-navdestinationinfo-i.md) |
| [NavDestinationSwitchInfo](arkts-arkui-uiobserver-navdestinationswitchinfo-i.md) |
| [NavDestinationSwitchObserverOptions](arkts-arkui-uiobserver-navdestinationswitchobserveroptions-i.md) |
| [NavigationInfo](arkts-arkui-uiobserver-navigationinfo-i.md) |
| [ObserverOptions](arkts-arkui-uiobserver-observeroptions-i.md) |
| [ScrollEventInfo](arkts-arkui-uiobserver-scrolleventinfo-i.md) |
| [TabContentInfo](arkts-arkui-uiobserver-tabcontentinfo-i.md) |
| [TextChangeEventInfo](arkts-arkui-uiobserver-textchangeeventinfo-i.md) |
| [WindowSizeLayoutBreakpointInfo](arkts-arkui-uiobserver-windowsizelayoutbreakpointinfo-i.md) |

### 枚举

| 名称 |
| --- |
| [NavDestinationState](arkts-arkui-uiobserver-navdestinationstate-e.md) |
| [RouterPageState](arkts-arkui-uiobserver-routerpagestate-e.md) |
| [ScrollEventType](arkts-arkui-uiobserver-scrolleventtype-e.md) |
| [TabContentState](arkts-arkui-uiobserver-tabcontentstate-e.md) |
