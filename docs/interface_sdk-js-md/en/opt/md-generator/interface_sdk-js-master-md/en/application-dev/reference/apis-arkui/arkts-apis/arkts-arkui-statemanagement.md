# @ohos.arkui.StateManagement(State Management)

The state management module provides data storage, persistent data management, UIAbility data storage, and
 environment state and tools required by applications.
 T and S in this topic represent the types as described below.
| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| ---- |
| T    |
| S    |


## Modules to Import

```TypeScript
import { Binding, ComponentReuse, CustomComponentLifecycleState, ComponentInactive, PersistenceV2, ComponentDisappear, MutableBinding, CustomComponentLifecycleObserver, AppStorageV2, Type, ConnectOptionsCollections, CollectionType, CustomComponentContext, IReusePool, ConnectOptions, UIUtils, ComponentActive, CustomComponentLifecycle, ComponentInit, ComponentAppear, ComponentBuilt, ComponentRecycle, IReusableInfo } from 'kits/@kit.ArkUI';
```

## Summary

### Classes

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AppStorageV2](arkts-arkui-arkui-statemanagement-appstoragev2-c.md) |
| [Binding](arkts-arkui-arkui-statemanagement-binding-c.md) |
| [ConnectOptions](arkts-arkui-arkui-statemanagement-connectoptions-c.md) |
| [ConnectOptionsCollections](arkts-arkui-arkui-statemanagement-connectoptionscollections-c.md) | Defines the parameter type for the  [globalConnect](PersistenceV2.globalConnect&lt;T extends CollectionType<S>, S extends object&gt;&lt;S&gt;, S extends object>( type: ConnectOptionsCollections&lt;T, S&gt; \|
| [MutableBinding](arkts-arkui-arkui-statemanagement-mutablebinding-c.md) |
| [PersistenceV2](arkts-arkui-arkui-statemanagement-persistencev2-c.md) |
| [UIUtils](arkts-arkui-arkui-statemanagement-uiutils-c.md) |

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [CustomComponentContext](arkts-arkui-arkui-statemanagement-customcomponentcontext-i.md) |
| [CustomComponentLifecycle](arkts-arkui-arkui-statemanagement-customcomponentlifecycle-i.md) |
| [CustomComponentLifecycleObserver](arkts-arkui-arkui-statemanagement-customcomponentlifecycleobserver-i.md) |
| [DecoratorInfo](arkts-arkui-arkui-statemanagement-decoratorinfo-i.md) |
| [ElementInfo](arkts-arkui-arkui-statemanagement-elementinfo-i.md) |
| [IReusableInfo](arkts-arkui-arkui-statemanagement-ireusableinfo-i.md) |
| [IReusePool](arkts-arkui-arkui-statemanagement-ireusepool-i.md) |
| [MonitorOptions](arkts-arkui-arkui-statemanagement-monitoroptions-i.md) |
| [ObservedResult](arkts-arkui-arkui-statemanagement-observedresult-i.md) |
| [TypeConstructor](arkts-arkui-arkui-statemanagement-typeconstructor-i.md) |
| [TypeConstructorWithArgs](arkts-arkui-arkui-statemanagement-typeconstructorwithargs-i.md) |

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [CustomComponentLifecycleState](arkts-arkui-arkui-statemanagement-customcomponentlifecyclestate-e.md) |

### Types

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [CollectionType](arkts-arkui-collectiontype-t.md) |
| [GetterCallback](arkts-arkui-gettercallback-t.md) |
| [MonitorCallback](arkts-arkui-monitorcallback-t.md) |
| [PersistenceErrorCallback](arkts-arkui-persistenceerrorcallback-t.md) |
| [ReusableComponentConstructor](arkts-arkui-reusablecomponentconstructor-t.md) |
| [SetterCallback](arkts-arkui-settercallback-t.md) |
| [StorageDefaultCreator](arkts-arkui-storagedefaultcreator-t.md) |
| [TaskCallback](arkts-arkui-taskcallback-t.md) |
| [TypeDecorator](arkts-arkui-typedecorator-t.md) |
