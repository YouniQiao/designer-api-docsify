# common_ts_ets_api(System API)

## Modules to Import

```TypeScript
```

## Summary

### Classes

| Name | Description |
| --- | --- |
| [AppStorage(System API)](arkts-arkui-appstorage-c.md) | For details about how to use AppStorage, see [AppStorage: Storing Application-wide UI State](../../../ui/state-management/arkts-appstorage.md). |
| [Environment(System API)](arkts-arkui-environment-c.md) | For details about how to use environment parameters, see [Environment: Device Environment Query](../../../ui/state-management/arkts-environment.md). |
| [LocalStorage(System API)](arkts-arkui-localstorage-c.md) | For details about how to use LocalStorage on the UI, see [LocalStorage: UI State Storage](../../../ui/state-management/arkts-localstorage.md). |
| [PersistentStorage(System API)](arkts-arkui-persistentstorage-c.md) | For details about how to use PersistentStorage on the UI, see [PersistentStorage: Persisting Application State](../../../ui/state-management/arkts-persiststorage.md). > **NOTE：**> Since API version 12, PersistentStorage supports **null** and **undefined**. |
| [SubscribedAbstractProperty(System API)](arkts-arkui-subscribedabstractproperty-c.md) | Represents a synchronized property from [AppStorage](../../../ui/state-management/arkts-appstorage.md) or [LocalStorage](../../../ui/state-management/arkts-localstorage.md). |

<!--Del-->
### Classes(System API)

| Name | Description |
| --- | --- |
| [Environment(System API)](arkts-arkui-environment-c-sys.md) | For details about how to use environment parameters, see [Environment: Device Environment Query](../../../ui/state-management/arkts-environment.md). |
| [PersistentStorage(System API)](arkts-arkui-persistentstorage-c-sys.md) | For details about how to use PersistentStorage on the UI, see [PersistentStorage: Persisting Application State](../../../ui/state-management/arkts-persiststorage.md). > **NOTE：**> Since API version 12, PersistentStorage supports **null** and **undefined**. |
| [SubscribaleAbstract(System API)](arkts-arkui-subscribaleabstract-c-sys.md) | Defines the Subscribale base class. |
| [SubscribedAbstractProperty(System API)](arkts-arkui-subscribedabstractproperty-c-sys.md) | Represents a synchronized property from [AppStorage](../../../ui/state-management/arkts-appstorage.md) or [LocalStorage](../../../ui/state-management/arkts-localstorage.md). |
| [SyncedPropertyOneWay(System API)](arkts-arkui-syncedpropertyoneway-c-sys.md) | Inherits from [SubscribedAbstractProperty&lt;T&gt;](arkts-arkui-subscribedabstractproperty-c.md). Represents a property with one-way synchronization. |
| [SyncedPropertyTwoWay(System API)](arkts-arkui-syncedpropertytwoway-c-sys.md) | Inherits from [SubscribedAbstractProperty&lt;T&gt;](arkts-arkui-subscribedabstractproperty-c.md). Represents a property with two-way synchronization. |
<!--DelEnd-->

### Interfaces

| Name | Description |
| --- | --- |
| [AbstractProperty(System API)](arkts-arkui-abstractproperty-i.md) | Provides a reference to properties stored in [AppStorage](../../../ui/state-management/arkts-appstorage.md) or [LocalStorage](../../../ui/state-management/arkts-localstorage.md). |
| [EnvPropsOptions(System API)](arkts-arkui-envpropsoptions-i.md) | Defines a key-value pair object used to specify environment variable names and their default values, passed as a parameter to [envProps](arkts-arkui-environment-c.md#envprops). |
| [PersistPropsOptions(System API)](arkts-arkui-persistpropsoptions-i.md) | Defines a key-value pair object used to specify persistent properties and their default values, passed as a parameter to [persistProps](arkts-arkui-persistentstorage-c.md#persistprops). |

<!--Del-->
### Interfaces(System API)

| Name | Description |
| --- | --- |
| [IPropertySubscriber(System API)](arkts-arkui-ipropertysubscriber-i-sys.md) | Provides an interface for attribute subscribers. |
| [ISinglePropertyChangeSubscriber(System API)](arkts-arkui-isinglepropertychangesubscriber-i-sys.md) | Inherits from [IPropertySubscriber](arkts-arkui-ipropertysubscriber-i-sys.md). Represents a subscriber that subscribes to changes in a property value. |
<!--DelEnd-->

