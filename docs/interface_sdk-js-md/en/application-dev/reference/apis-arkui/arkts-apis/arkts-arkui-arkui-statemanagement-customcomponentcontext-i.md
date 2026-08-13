# CustomComponentContext

The **CustomComponentContext** class provides access to component-level services, including the reuse pool. You can obtain an instance through [UIUtils.getCustomComponentContext](arkts-arkui-arkui-statemanagement-uiutils-c.md#getCustomComponentContext).

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

<!--Device-unnamed-export declare interface CustomComponentContext--><!--Device-unnamed-export declare interface CustomComponentContext-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { Binding, ComponentReuse, CustomComponentLifecycleState, ComponentInactive, PersistenceV2, ComponentDisappear, MutableBinding, CustomComponentLifecycleObserver, AppStorageV2, Type, ConnectOptionsCollections, CollectionType, CustomComponentContext, IReusePool, ConnectOptions, UIUtils, ComponentActive, CustomComponentLifecycle, ComponentInit, ComponentAppear, ComponentBuilt, ComponentRecycle, IReusableInfo } from '@kit.ArkUI';
```

## getReusePool

```TypeScript
getReusePool(): IReusePool | undefined
```

Obtains the global reuse pool of the custom component. If the component does not configure the reuse pool through **reusePool** and **poolAccepts**, **undefined** is returned. For details about how to configure the global reuse pool, see [Global Reuse: Centralized Component Recycling and Reuse](../../../ui/state-management/arkts-global-reuse-pool.md).

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-CustomComponentContext-getReusePool(): IReusePool | undefined--><!--Device-CustomComponentContext-getReusePool(): IReusePool | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [IReusePool](arkts-arkui-arkui-statemanagement-ireusepool-i.md) | If a global reuse pool is configured for the current component, the reuse pool information is returned. Otherwise, **undefined** is returned. |

