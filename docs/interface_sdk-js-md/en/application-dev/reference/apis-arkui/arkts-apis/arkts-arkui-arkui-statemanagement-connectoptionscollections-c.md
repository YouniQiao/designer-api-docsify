# ConnectOptionsCollections

[globalConnect](PersistenceV2.globalConnect&lt;T extends CollectionType<S>, S extends object&gt;&lt;S&gt;, S extends object>( type: ConnectOptionsCollections&lt;T, S&gt; | ConnectOptions&lt;T&gt; ))接口参数类型，ConnectOptionsCollections继承自[ConnectOptions\&lt;T\&gt;](arkts-arkui-arkui-statemanagement-connectoptions-c.md)。当开发者需要持久化容器类型数据（如`Array&lt;S&gt;`）时，需要使用`ConnectOptionsCollections`入参。

如下展示`StorageDefaultCreator&lt;T&gt;`和`StorageDefaultCreator&lt;S&gt;`示例：

**Inheritance/Implementation:** ConnectOptionsCollections extends [ConnectOptions<T>](ConnectOptions<T>)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

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

用于持久化容器类型数据，当提供默认`defaultSubCreator`时，则需要同时提供默认构造器`defaultCreator`，不提供默认构造器会导致持久化失败。集合项类型`S`必须与`defaultSubCreator`的返回类型相同。

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-ConnectOptionsCollections-defaultCreator?: StorageDefaultCreator<T>--><!--Device-ConnectOptionsCollections-defaultCreator?: StorageDefaultCreator<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## defaultSubCreator

```TypeScript
defaultSubCreator?: StorageDefaultCreator<S>
```

使用该集合项默认构造函数，用于持久化容器类数据。使用此参数时，必须同时提供`defaultCreator`，否则会导致持久化失败。如果defaultSubCreator返回的是`undefined`或`null`时，会导致持久化失败。 当持久化用户自定义class类集合（如`Array&lt;ClassA&gt;`）时，`defaultCreator`中的泛型类型`T`为`Array&lt;ClassA&gt;`，则`defaultSubCreator`中的泛型类型`S`为`ClassA`。

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-ConnectOptionsCollections-defaultSubCreator?: StorageDefaultCreator<S>--><!--Device-ConnectOptionsCollections-defaultSubCreator?: StorageDefaultCreator<S>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

