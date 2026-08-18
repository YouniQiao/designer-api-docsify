# ConnectOptionsCollections

Defines the parameter type for the globalConnect API. **ConnectOptionsCollections** is inherited from [ConnectOptions\&lt;T\&gt;](arkts-arkui-arkui-statemanagement-connectoptions-c.md#connectoptions). You can use the **ConnectOptionsCollections** input parameter to persist container data (such as **Array\&lt;S&gt;**). The following shows the examples of **StorageDefaultCreator\&lt;T&gt;** and **StorageDefaultCreator\&lt;S&gt;**:

**Inheritance/Implementation:** ConnectOptionsCollections extends ConnectOptions<T>

**Since:** 23

<!--Device-unnamed-export class ConnectOptionsCollections--><!--Device-unnamed-export class ConnectOptionsCollections-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { AppStorageV2, PersistenceV2, Type, UIUtils, ConnectOptions, Binding, MutableBinding, CustomComponentLifecycle, CustomComponentLifecycleObserver, CustomComponentLifecycleState, ComponentInit, ComponentAppear, ComponentBuilt, ComponentReuse, ComponentActive, ComponentInactive, ComponentRecycle, ComponentDisappear, CollectionType, ConnectOptionsCollections, CustomComponentContext, IReusePool, IReusableInfo } from '@kit.ArkUI';
```

## defaultCreator

```TypeScript
defaultCreator?: StorageDefaultCreator<T>
```

Persists container data. **defaultSubCreator** should be provided together with **defaultCreator**; otherwise, the container data cannot be persisted. The collection item type **S** must be the same as the return type of **defaultSubCreator**. If **defaultSubCreator** is provided but **defaultCreator** is not, the persistence fails.

**Type:** [StorageDefaultCreator](arkts-arkui-storagedefaultcreator-t.md)&lt;T&gt;

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-ConnectOptionsCollections-defaultCreator?: StorageDefaultCreator<T>--><!--Device-ConnectOptionsCollections-defaultCreator?: StorageDefaultCreator<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## defaultSubCreator

```TypeScript
defaultSubCreator?: StorageDefaultCreator<S>
```

Persists container data. If the return value of **defaultSubCreator** is **undefined** or **null**, the persistence fails. When a user-defined class collection (such as **Array&lt;ClassA&gt;**) is persisted, the generic type **T** in **defaultCreator** is **Array&lt;ClassA&gt;**, and **S** in **defaultSubCreator** is **ClassA**.

**Type:** [StorageDefaultCreator](arkts-arkui-storagedefaultcreator-t.md)&lt;S&gt;

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-ConnectOptionsCollections-defaultSubCreator?: StorageDefaultCreator<S>--><!--Device-ConnectOptionsCollections-defaultSubCreator?: StorageDefaultCreator<S>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

