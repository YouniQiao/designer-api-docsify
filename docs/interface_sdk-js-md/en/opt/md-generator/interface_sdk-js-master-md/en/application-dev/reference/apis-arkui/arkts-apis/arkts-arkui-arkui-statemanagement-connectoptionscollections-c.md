# ConnectOptionsCollections

Defines the parameter type for the  
[globalConnect](PersistenceV2.globalConnect&lt;T extends CollectionType<S>, S extends object&gt;&lt;S&gt;, S extends object>( type: ConnectOptionsCollections&lt;T, S&gt; | ConnectOptions&lt;T&gt; ))API. **ConnectOptionsCollections** is inherited from [ConnectOptions\&lt;T\&gt;](arkts-arkui-arkui-statemanagement-connectoptions-c.md). You can use the  
**ConnectOptionsCollections** input parameter to persist container data (such as **Array\&lt;S&gt;**).

The following shows the examples of **StorageDefaultCreator\&lt;T&gt;** and **StorageDefaultCreator\&lt;S&gt;**:

**Inheritance/Implementation:** ConnectOptionsCollections extends [ConnectOptions<T>](ConnectOptions<T>)

**Since:** 23

<!--Device-unnamed-export class ConnectOptionsCollections<T extends CollectionType<S>, S extends object> extends ConnectOptions<T>--><!--Device-unnamed-export class ConnectOptionsCollections<T extends CollectionType<S>, S extends object> extends ConnectOptions<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { Binding, ComponentReuse, CustomComponentLifecycleState, ComponentInactive, PersistenceV2, ComponentDisappear, MutableBinding, CustomComponentLifecycleObserver, AppStorageV2, Type, ConnectOptionsCollections, CollectionType, CustomComponentContext, IReusePool, ConnectOptions, UIUtils, ComponentActive, CustomComponentLifecycle, ComponentInit, ComponentAppear, ComponentBuilt, ComponentRecycle, IReusableInfo } from 'kits/@kit.ArkUI';
```

## defaultCreator

```TypeScript
defaultCreator?: StorageDefaultCreator<T>
```

Persists container data. **defaultSubCreator** should be provided together with **defaultCreator**; otherwise, the container data cannot be persisted. The collection item type **S** must be the same as the return type of  
**defaultSubCreator**. If **defaultSubCreator** is provided but **defaultCreator** is not, the persistence fails.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-ConnectOptionsCollections-defaultCreator?: StorageDefaultCreator<T>--><!--Device-ConnectOptionsCollections-defaultCreator?: StorageDefaultCreator<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## defaultSubCreator

```TypeScript
defaultSubCreator?: StorageDefaultCreator<S>
```

Persists container data. If the return value of **defaultSubCreator** is **undefined** or **null**, the persistence fails. When a user-defined class collection (such as **Array&lt;ClassA&gt;**) is persisted, the generic type **T** in  
**defaultCreator** is **Array&lt;ClassA&gt;**, and **S** in **defaultSubCreator** is **ClassA**.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-ConnectOptionsCollections-defaultSubCreator?: StorageDefaultCreator<S>--><!--Device-ConnectOptionsCollections-defaultSubCreator?: StorageDefaultCreator<S>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full
