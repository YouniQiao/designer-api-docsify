# IReusePool

The **IReusePool** API provides the features related to the global reuse pool of a custom component.

**Since:** 26.0.0

<!--Device-unnamed-export declare interface IReusePool--><!--Device-unnamed-export declare interface IReusePool-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { AppStorageV2, PersistenceV2, Type, UIUtils, ConnectOptions, Binding, MutableBinding, CustomComponentLifecycle, CustomComponentLifecycleObserver, CustomComponentLifecycleState, ComponentInit, ComponentAppear, ComponentBuilt, ComponentReuse, ComponentActive, ComponentInactive, ComponentRecycle, ComponentDisappear, CollectionType, ConnectOptionsCollections, CustomComponentContext, IReusePool, IReusableInfo } from '@kit.ArkUI';
```

## getReusableInfo

```TypeScript
getReusableInfo(constructor: ReusableComponentConstructor,
    reuseId?: string): IReusableInfo[] | IReusableInfo | undefined
```

Obtains the information about the recycling instance of a given reusable component type in this reuse pool.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-IReusePool-getReusableInfo(constructor: ReusableComponentConstructor,    reuseId?: string): IReusableInfo[] | IReusableInfo | undefined--><!--Device-IReusePool-getReusableInfo(constructor: ReusableComponentConstructor,    reuseId?: string): IReusableInfo[] | IReusableInfo | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| constructor | [ReusableComponentConstructor](arkts-arkui-reusablecomponentconstructor-t.md) | Yes | Name of the reusable custom component to be queried. |
| reuseId | string | No | Reuse ID for filtering. If specified, only the information about the reuse pool with the reuse ID is returned. The default value is **undefined**, indicating that information about all reuse pools is returned. |

**Return value:**

| Type | Description |
| --- | --- |
| [IReusableInfo](arkts-arkui-arkuistatemanagement-ireusableinfo-i.md)[] \| [IReusableInfo](arkts-arkui-arkuistatemanagement-ireusableinfo-i.md) \| undefined | If the reuse pool is not configured to accept the given component type, **undefined** is returned. <br>If **reuseId** is specified, a single **IReusableInfo** is returned (even if **count** is set to **0** and **maxCount** is set to the default value). <br>If **reuseId** is not specified and the reusable component does not use **reuseId**, a single **IReusableInfo** is returned. <br>If **reuseId** is not specified but the reusable component uses **reuseId**, an **Array&lt;IReusableInfo&gt;** is returned, providing a separate entry for each **reuseId** that has a positive value of **count** or a non- default value of **maxCount** as well as an entry of **reuseId: undefined**. |

## preRender

```TypeScript
preRender(builder: WrappedBuilder<[]>, times: number): Promise<void>
```

Pre-creates @Reusable/@ReusableV2 decorated components and places them in this reuse pool.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-IReusePool-preRender(builder: WrappedBuilder<[]>, times: number): Promise<void>--><!--Device-IReusePool-preRender(builder: WrappedBuilder<[]>, times: number): Promise<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| builder | WrappedBuilder&lt;[]&gt; | Yes | WrappedBuilder** that contains the @Builder decorated function to be executed *n* times. Each execution should create one or more @Reusable/@ReusableV2 decorated components. |
| times | number | Yes | Number of times the @Builder decorated function is executed. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise parsed when the idle task is successfully completed. This promise returns no value. |

