# PersistenceV2

Inherits from [AppStorageV2](arkts-arkui-arkui-statemanagement-appstoragev2-c.md). For details, see [PersistenceV2: Persisting Application State](../../../ui/state-management/arkts-new-persistencev2.md).

**Inheritance/Implementation:** PersistenceV2 extends [AppStorageV2](arkts-arkui-arkui-statemanagement-appstoragev2-c.md)

**Since:** 12

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { AppStorageV2, PersistenceV2, Type, UIUtils, ConnectOptions, Binding, MutableBinding, CustomComponentLifecycle, CustomComponentLifecycleObserver, CustomComponentLifecycleState, ComponentInit, ComponentAppear, ComponentBuilt, ComponentReuse, ComponentActive, ComponentInactive, ComponentRecycle, ComponentDisappear, CollectionType, ConnectOptionsCollections, CustomComponentContext, IReusePool, IReusableInfo } from 'kits/@kit.ArkUI';
```

## globalConnect

```TypeScript
static globalConnect<T extends object>(
    type: ConnectOptions<T>
  ): T | undefined
```

Stores key-value pair data on the application disk. If the given key already exists in [PersistenceV2](../../../ui/state-management/arkts-new-persistencev2.md), the corresponding value is returned. Otherwise, a default value is constructed using the default value constructor and returned. If **globalConnect** is used for an [\@ObservedV2](../../../ui/state-management/arkts-new-observedV2-and-trace.md) decorated object, changes to the object's [\@Trace](../../../ui/state-management/arkts-new-observedV2-and-trace.md) properties will trigger automatic refresh of the associated object, while changes to non-@Trace properties will not. If necessary, the [PersistenceV2.save](#save) API can be called to store the data manually.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | [ConnectOptions](arkts-arkui-arkui-statemanagement-connectoptions-c.md)&lt;T&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T \| undefined |

## globalConnect

```TypeScript
static globalConnect<T extends CollectionType<S>, S extends object>(
    type: ConnectOptionsCollections<T, S> | ConnectOptions<T>
  ): T | undefined
```

Stores key-value pair data on the application disk. Supports the persistence of the following collection types: [Array, Map, Set, Date, collections.Array, collections.Map, and collections.Set](../../../ui/state-management/arkts-new-persistencev2.md#types-supported-by-globalconnect). Note that when persisting data of the **Array\&lt;ClassA&gt;** type, you need to call [makeObserved](arkts-arkui-arkui-statemanagement-uiutils-c.md#makeobserved) to make the returned object observed. Multi-level nested sets are not supported. For example, **Array&lt;Array\<ClassA>&gt;** persistence is not supported.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | [ConnectOptionsCollections](arkts-arkui-arkui-statemanagement-connectoptionscollections-c.md)&lt;T, S&gt; \| [ConnectOptions](arkts-arkui-arkui-statemanagement-connectoptions-c.md)&lt;T&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T \| undefined |

## notifyOnError

```TypeScript
static notifyOnError(callback: PersistenceErrorCallback | undefined): void
```

Called when persistence fails.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [PersistenceErrorCallback](arkts-arkui-persistenceerrorcallback-t.md) \| undefined | Yes |

## save

```TypeScript
static save<T>(keyOrType: string | TypeConstructorWithArgs<T>): void
```

Persists the specified key-value pair data once.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| keyOrType | string \| [TypeConstructorWithArgs](arkts-arkui-arkui-statemanagement-typeconstructorwithargs-i.md)&lt;T&gt; | Yes |
