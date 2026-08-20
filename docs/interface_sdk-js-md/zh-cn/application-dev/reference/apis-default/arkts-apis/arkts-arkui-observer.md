# @ohos.arkui.observer

Register callbacks to observe ArkUI behavior.

@namespace uiObserver

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-declare namespace uiObserver--><!--Device-unnamed-declare namespace uiObserver-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## 汇总

### 函数

| 名称 | 说明 |
| --- | --- |
| [offDensityUpdate](arkts-uiobserver-offdensityupdate-f.md) | Removes a callback function that was previously registered with `on()`. |
| [offDidLayout](arkts-uiobserver-offdidlayout-f.md) | Removes a callback function that was previously registered with `on()`. |
| [offNavDestinationSwitch](arkts-uiobserver-offnavdestinationswitch-f.md) | 取消监听Navigation的页面切换事件。 |
| [offNavDestinationSwitch](arkts-uiobserver-offnavdestinationswitch-f.md) | 取消监听Navigation的页面切换事件。 |
| [offNavDestinationUpdate](arkts-uiobserver-offnavdestinationupdate-f.md) | 取消监听NavDestination组件的状态变化。 |
| [offNavDestinationUpdate](arkts-uiobserver-offnavdestinationupdate-f.md) | 取消监听NavDestination组件的状态变化。 |
| [offRouterPageUpdate](arkts-uiobserver-offrouterpageupdate-f.md) | 取消监听router中page页面的状态变化。 |
| [offScrollEvent](arkts-uiobserver-offscrollevent-f.md) | Removes a callback function that was previously registered with `onScrollEvent()`. |
| [offScrollEvent](arkts-uiobserver-offscrollevent-f.md) | Removes a callback function that was previously registered with `onScrollEvent()`. |
| [offTabContentUpdate](arkts-uiobserver-offtabcontentupdate-f.md) | 取消监听TabContent页面的切换事件。 |
| [offTabContentUpdate](arkts-uiobserver-offtabcontentupdate-f.md) | 取消监听TabContent页面的切换事件。 |
| [offWillDraw](arkts-uiobserver-offwilldraw-f.md) | Removes a callback function that was previously registered with `on()`. |
| [onDensityUpdate](arkts-uiobserver-ondensityupdate-f.md) | Registers a callback function to be called when the screen density is updated. |
| [onDidLayout](arkts-uiobserver-ondidlayout-f.md) | Registers a callback function to be called when the layout is done. |
| [onNavDestinationSwitch](arkts-uiobserver-onnavdestinationswitch-f.md) | 监听Navigation的页面切换事件。 |
| [onNavDestinationSwitch](arkts-uiobserver-onnavdestinationswitch-f.md) | 监听Navigation的页面切换事件。 |
| [onNavDestinationUpdate](arkts-uiobserver-onnavdestinationupdate-f.md) | 监听NavDestination组件的状态变化。 |
| [onNavDestinationUpdate](arkts-uiobserver-onnavdestinationupdate-f.md) | 监听NavDestination组件的状态变化。 |
| [onRouterPageUpdate](arkts-uiobserver-onrouterpageupdate-f.md) | 监听router中page页面的状态变化。 |
| [onScrollEvent](arkts-uiobserver-onscrollevent-f.md) | Registers a callback function to be called when the scroll event starts or stops. |
| [onScrollEvent](arkts-uiobserver-onscrollevent-f.md) | Registers a callback function to be called when the scroll event starts or stops. |
| [onTabContentUpdate](arkts-uiobserver-ontabcontentupdate-f.md) | 监听TabContent页面的切换事件。 |
| [onTabContentUpdate](arkts-uiobserver-ontabcontentupdate-f.md) | 监听TabContent页面的切换事件。 |
| [onWillDraw](arkts-uiobserver-onwilldraw-f.md) | Registers a callback function to be called when the draw command will be drawn. |

### 类

| 名称 | 说明 |
| --- | --- |
| [DensityInfo](arkts-uiobserver-densityinfo-c.md) | Density info. |
| [RouterPageInfo](arkts-uiobserver-routerpageinfo-c.md) | RouterPageInfo包含的信息。 |

### 接口

| 名称 | 说明 |
| --- | --- |
| [NavDestinationInfo](arkts-uiobserver-navdestinationinfo-i.md) | NavDestination组件信息。 |
| [NavDestinationSwitchInfo](arkts-uiobserver-navdestinationswitchinfo-i.md) | Navigation组件页面切换的信息。 |
| [NavDestinationSwitchObserverOptions](arkts-uiobserver-navdestinationswitchobserveroptions-i.md) | Indicates the options of NavDestination switch. |
| [NavigationInfo](arkts-uiobserver-navigationinfo-i.md) | Navigation组件信息。 |
| [ObserverOptions](arkts-uiobserver-observeroptions-i.md) | observer options. |
| [ScrollEventInfo](arkts-uiobserver-scrolleventinfo-i.md) | ScrollEvent info. |
| [TabContentInfo](arkts-uiobserver-tabcontentinfo-i.md) | TabContent页面的切换信息。 |
| [TextChangeEventInfo](arkts-uiobserver-textchangeeventinfo-i.md) | 文本更改事件信息 |
| [WindowSizeLayoutBreakpointInfo](arkts-uiobserver-windowsizelayoutbreakpointinfo-i.md) | 定义窗口大小断点信息。 这个接口定义了当前窗口长宽的断点信息，基于配置好的断点阈值。 |

### 枚举

| 名称 | 说明 |
| --- | --- |
| [NavDestinationState](arkts-uiobserver-navdestinationstate-e.md) | NavDestination组件状态。 |
| [RouterPageState](arkts-uiobserver-routerpagestate-e.md) | routerPage生命周期触发时对应的状态。 |
| [ScrollEventType](arkts-uiobserver-scrolleventtype-e.md) | ScrollEvent type. |
| [TabContentState](arkts-uiobserver-tabcontentstate-e.md) | TabContent组件的状态。 |

