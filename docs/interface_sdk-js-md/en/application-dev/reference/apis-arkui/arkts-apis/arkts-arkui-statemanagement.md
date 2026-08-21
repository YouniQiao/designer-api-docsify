# @ohos.arkui.StateManagement

## Modules to Import

```TypeScript
import { AppStorageV2, PersistenceV2, Type, UIUtils, ConnectOptions, Binding, MutableBinding, CustomComponentLifecycle, CustomComponentLifecycleObserver, CustomComponentLifecycleState, ComponentInit, ComponentAppear, ComponentBuilt, ComponentReuse, ComponentActive, ComponentInactive, ComponentRecycle, ComponentDisappear, CollectionType, ConnectOptionsCollections, CustomComponentContext, IReusePool, IReusableInfo } from '@kit.ArkUI';
```

## Summary

### Classes

| Name | Description |
| --- | --- |
| [AppStorageV2](arkts-arkui-arkuistatemanagement-appstoragev2-c.md) | For details about how to use AppStorageV2, see [AppStorageV2: Storing Application-wide UI State](../../../ui/state-management/arkts-new-appstoragev2.md). |
| [Binding](arkts-arkui-arkuistatemanagement-binding-c.md) | Represents the generic class for read-only data binding, which can bind data of any type. |
| [ConnectOptions](arkts-arkui-arkuistatemanagement-connectoptions-c.md) | Defines the parameter type for **globalConnect**. |
| [ConnectOptionsCollections](arkts-arkui-arkuistatemanagement-connectoptionscollections-c.md) | Defines the parameter type for the globalConnect API. **ConnectOptionsCollections** is inherited from [ConnectOptions\&lt;T\&gt;](arkts-arkui-arkuistatemanagement-connectoptions-c.md). You can use the **ConnectOptionsCollections** input parameter to persist container data (such as **Array\&lt;S&gt;**). |
| [MutableBinding](arkts-arkui-arkuistatemanagement-mutablebinding-c.md) | Represents a generic class for mutable data binding, which allows the read and write operations on the bound value and provides complete **get** and **set** accessors. |
| [PersistenceV2](arkts-arkui-arkuistatemanagement-persistencev2-c.md) | Inherits from [AppStorageV2](arkts-arkui-arkuistatemanagement-appstoragev2-c.md). For details, see [PersistenceV2: Persisting Application State](../../../ui/state-management/arkts-new-persistencev2.md). |
| [UIUtils](arkts-arkui-arkuistatemanagement-uiutils-c.md) | Provides APIs for handling data transformations related to state management. |

### Interfaces

| Name | Description |
| --- | --- |
| [CustomComponentContext](arkts-arkui-arkuistatemanagement-customcomponentcontext-i.md) | The **CustomComponentContext** class provides access to component-level services, including the reuse pool. You can obtain an instance through [UIUtils.getCustomComponentContext](arkts-arkui-arkuistatemanagement-uiutils-c.md#getcustomcomponentcontext). |
| [CustomComponentLifecycle](arkts-arkui-arkuistatemanagement-customcomponentlifecycle-i.md) | *CustomComponentLifecycle** monitors the lifecycle changes of a custom component. |
| [CustomComponentLifecycleObserver](arkts-arkui-arkuistatemanagement-customcomponentlifecycleobserver-i.md) | Observes lifecycle status changes of a custom component, and triggers the lifecycle callback in the listener when detecting lifecycle status changes. |
| [DecoratorInfo](arkts-arkui-arkuistatemanagement-decoratorinfo-i.md) | Defines the decorator and component information associated with the observable object. |
| [ElementInfo](arkts-arkui-arkuistatemanagement-elementinfo-i.md) | Defines information about the components associated with the observable object, including system components and custom components. |
| [IReusableInfo](arkts-arkui-arkuistatemanagement-ireusableinfo-i.md) | The **IReusableInfo** API provides information about the current number and maximum number of reusable components managed by the reuse pool. |
| [IReusePool](arkts-arkui-arkuistatemanagement-ireusepool-i.md) | The **IReusePool** API provides the features related to the global reuse pool of a custom component. |
| [MonitorOptions](arkts-arkui-arkuistatemanagement-monitoroptions-i.md) | Defines the optional parameters for [addMonitor](arkts-arkui-arkuistatemanagement-uiutils-c.md#addmonitor), which are used to configure the callback type and whether to enable the wildcard capability. |
| [ObservedResult](arkts-arkui-arkuistatemanagement-observedresult-i.md) | Provides the result of whether the object can be observed. |
| [TypeConstructor](arkts-arkui-arkuistatemanagement-typeconstructor-i.md) | Represents a class constructor. |
| [TypeConstructorWithArgs](arkts-arkui-arkuistatemanagement-typeconstructorwithargs-i.md) | Represents a class constructor that accepts arbitrary arguments. |

### Enums

| Name | Description |
| --- | --- |
| [CustomComponentLifecycleState](arkts-arkui-arkuistatemanagement-customcomponentlifecyclestate-e.md) | Current lifecycle status of a custom component. |

### Types

| Name | Description |
| --- | --- |
| [CollectionType](arkts-arkui-collectiontype-t.md) | Defines the types of persistent collection data supported by **globalConnect** using the generic type of the input parameter of **globalConnect**. |
| [GetterCallback](arkts-arkui-gettercallback-t.md) | Defines a callback used to obtain a value. |
| [MonitorCallback](arkts-arkui-monitorcallback-t.md) | Listener callback function of the IMonitor type. |
| [PersistenceErrorCallback](arkts-arkui-persistenceerrorcallback-t.md) | Defines a callback used to return the cause of the persistence failure. |
| [ReusableComponentConstructor](arkts-arkui-reusablecomponentconstructor-t.md) | Function for initializing the reusable custom component. |
| [SetterCallback](arkts-arkui-settercallback-t.md) | Defines a callback used to set a value. |
| [StorageDefaultCreator](arkts-arkui-storagedefaultcreator-t.md) | Obtains the default constructor. |
| [TaskCallback](arkts-arkui-taskcallback-t.md) | Defines a synchronous callback. |
| [TypeDecorator](arkts-arkui-typedecorator-t.md) | Defines the attribute decorator, which is used to decorate attributes of the custom class in a nested class. |

