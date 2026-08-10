# MonitorOptions

[addMonitor](arkts-arkui-arkui-statemanagement-uiutils-c.md#addmonitor)的可选参数，用于配置回调类型以及是否使能通配符能力。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-unnamed-export interface MonitorOptions--><!--Device-unnamed-export interface MonitorOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { Binding, ComponentReuse, CustomComponentLifecycleState, ComponentInactive, PersistenceV2, ComponentDisappear, MutableBinding, CustomComponentLifecycleObserver, AppStorageV2, Type, ConnectOptionsCollections, CollectionType, CustomComponentContext, IReusePool, ConnectOptions, UIUtils, ComponentActive, CustomComponentLifecycle, ComponentInit, ComponentAppear, ComponentBuilt, ComponentRecycle, IReusableInfo } from 'kits/@kit.ArkUI';
```

## enableWildcard

```TypeScript
enableWildcard?: boolean
```

配置当前addMonitor是否使能通配符能力。true表示使能，false表示关闭。默认值为false，即关闭。当关闭通配符能力，但路径中含有通配符时，该路径将视为不合法路径。

**Type:** boolean

**Default:** false

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-MonitorOptions-enableWildcard?: boolean--><!--Device-MonitorOptions-enableWildcard?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## isSynchronous

```TypeScript
isSynchronous?: boolean
```

配置当前回调函数是否为同步回调。true为同步回调。默认值为false，即异步回调。

**Type:** boolean

**Default:** false

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-MonitorOptions-isSynchronous?: boolean--><!--Device-MonitorOptions-isSynchronous?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

