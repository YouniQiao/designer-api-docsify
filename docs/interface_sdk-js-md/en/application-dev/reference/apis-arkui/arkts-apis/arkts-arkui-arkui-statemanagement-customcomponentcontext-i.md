# CustomComponentContext

```TypeScript
export declare interface CustomComponentContext
```

The **CustomComponentContext** class provides access to component-level services, including the reuse pool. You can obtain an instance through [UIUtils.getCustomComponentContext](arkts-arkui-arkui-statemanagement-uiutils-c.md#getcustomcomponentcontext).

**Since:** 26.0.0

<!--Device-unnamed-export declare interface CustomComponentContext--><!--Device-unnamed-export declare interface CustomComponentContext-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { AppStorageV2, PersistenceV2, Type, UIUtils, ConnectOptions, Binding, MutableBinding, CustomComponentLifecycle, CustomComponentLifecycleObserver, CustomComponentLifecycleState, ComponentInit, ComponentAppear, ComponentBuilt, ComponentReuse, ComponentActive, ComponentInactive, ComponentRecycle, ComponentDisappear, CollectionType, ConnectOptionsCollections, CustomComponentContext, CustomComponentAsyncLoadOptions, IReusePool, IDefaultReusePool, IReusableInfo, StorageDefaultCreator, TypeConstructorWithArgs, PersistenceErrorCallback, TypeConstructor, TypeDecorator, MonitorCallback, MonitorOptions, GetterCallback, SetterCallback, ObservedResult, DecoratorInfo, ElementInfo, RecoverableStorage, RecoverableConnectOptions, RecoverableStorageError, NotifyOnErrorCallback } from '@kit.ArkUI';
```

## enableAsyncLoad

```TypeScript
enableAsyncLoad(options?: CustomComponentAsyncLoadOptions): void
```

Sets the current custom component to asynchronous loading. The framework loads the actual content of the component in an asynchronous task instead of blocking the main thread during page transition.

Use this method in frame-rate-sensitive scenarios (such as page transitions) where synchronous loading of custom components causes frame drops. After the call succeeds, the component enters the asynchronous loading state managed by the component context. While loading is not complete, the registered placeholder (if configured and found) is displayed, or the component is not displayed. After loading is complete, the placeholder is automatically replaced with the actual content, and the rendering update is triggered automatically.

Different from [IReusePool.preRender()](arkts-arkui-arkui-statemanagement-ireusepool-i.md#prerender), which pre-creates reusable component instances, this method postpones the loading timing of the component instance. It is a configuration method that returns **void**.

> **NOTE:** 
> 
> 1. This method takes effect only for the current custom component instance. Components that do not call this method keep the existing synchronous loading behavior.
> 2. The placeholder template must be registered first through [getPlaceholderRegister()](arkts-arkui-arkui-uicontext-uicontext-c.md#getplaceholderregister), and the builder must be a global, parameterless **\@Builder({ isPlaceholder: true })** function.
> 3. For the semantics of **timeout** values (positive number, **0**, and negative number), see [CustomComponentAsyncLoadOptions.timeout](arkts-arkui-arkui-statemanagement-customcomponentasyncloadoptions-i.md#timeout).
> 4. Failure of asynchronous loading is not handled in this version; the timeout force-load mechanism serves as the fallback.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-CustomComponentContext-enableAsyncLoad(options?: CustomComponentAsyncLoadOptions): void--><!--Device-CustomComponentContext-enableAsyncLoad(options?: CustomComponentAsyncLoadOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [CustomComponentAsyncLoadOptions](arkts-arkui-arkui-statemanagement-customcomponentasyncloadoptions-i.md) | No | Configuration of asynchronous loading. The default value **undefined** indicates that no placeholder is displayed before loading completes and the default timeout (**1000** ms) is used. |

## getDefaultReusePool

```TypeScript
getDefaultReusePool(): IDefaultReusePool | undefined
```

Obtains the default reuse pool of the custom component.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-CustomComponentContext-getDefaultReusePool(): IDefaultReusePool | undefined--><!--Device-CustomComponentContext-getDefaultReusePool(): IDefaultReusePool | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [IDefaultReusePool](arkts-arkui-arkui-statemanagement-idefaultreusepool-i.md) &#124; undefined | If a default reuse pool is available for the current component, the default reuse pool is returned. Otherwise, **undefined** is returned. |

## getReusePool

```TypeScript
getReusePool(): IReusePool | undefined
```

Obtains the global reuse pool of the custom component. If the component or its upper-level component does not configure the global reuse pool using **reusePool** and **poolAccepts**, **undefined** is returned. For details about how to configure the global reuse pool, see [Global Reuse: Centralized Component Recycling and Reuse](../../../ui/state-management/arkts-global-reuse-pool.md).

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-CustomComponentContext-getReusePool(): IReusePool | undefined--><!--Device-CustomComponentContext-getReusePool(): IReusePool | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [IReusePool](arkts-arkui-arkui-statemanagement-ireusepool-i.md) &#124; undefined | If a global reuse pool is configured for the current component, the reuse pool information is returned. Otherwise, **undefined** is returned. |

**Examples**

```TypeScript
import { UIUtils } from '@kit.ArkUI';

@ReusableV2
@ComponentV2
struct ReusableChild {
  build() {
    Text('ReusableChild')
  }
}

@Entry
@ComponentV2({ reusePool: 'perInstance', poolAccepts: [ReusableChild], freezeWhenInactive: false })
struct PoolOwner {
  checkPool() {
    const pool = UIUtils.getCustomComponentContext(this).getReusePool();
    if (pool) {
      console.info('Global reuse pool configured.');
    } else {
      console.info('No global reuse pool configured.');
    }
  }

  build() {
    Column() {
      ReusableChild()
      Button('Check Pool')
        .onClick(() => {
          this.checkPool();
        })
    }
  }
}
```
