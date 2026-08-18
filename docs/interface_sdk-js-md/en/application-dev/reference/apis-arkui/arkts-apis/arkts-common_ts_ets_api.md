# common_ts_ets_api(System API)

/*
 Copyright (c) 2022-2023 Huawei Device Co., Ltd.
 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at
 http://www.apache.org/licenses/LICENSE-2.0
 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
 /


## Modules to Import

```TypeScript
```

## Summary

### Classes

| Name | Description |
| --- | --- |
| [AppStorage](arkts-arkui-appstorage-c.md) | For details about how to use AppStorage, see [AppStorage: Storing Application-wide UI State](../../../ui/state-management/arkts-appstorage.md). |
| [Environment](arkts-arkui-environment-c.md) | For details about how to use environment parameters, see [Environment: Device Environment Query](../../../ui/state-management/arkts-environment.md). |
| [LocalStorage](arkts-arkui-localstorage-c.md) | For details about how to use LocalStorage on the UI, see [LocalStorage: UI State Storage](../../../ui/state-management/arkts-localstorage.md). |
| [PersistentStorage](arkts-arkui-persistentstorage-c.md) | For details about how to use PersistentStorage on the UI, see [PersistentStorage: Persisting Application State](../../../ui/state-management/arkts-persiststorage.md). > **NOTE：**> Since API version 12, PersistentStorage supports **null** and **undefined**. |
| [SubscribedAbstractProperty](arkts-arkui-subscribedabstractproperty-c.md) | Represents a synchronized property from [AppStorage](../../../ui/state-management/arkts-appstorage.md) or [LocalStorage](../../../ui/state-management/arkts-localstorage.md). |

<!--Del-->
### Classes（系统接口）

| Name | Description |
| --- | --- |
| [Environment](arkts-arkui-environment-c-sys.md) | For details about how to use environment parameters, see [Environment: Device Environment Query](../../../ui/state-management/arkts-environment.md). |
| [PersistentStorage](arkts-arkui-persistentstorage-c-sys.md) | For details about how to use PersistentStorage on the UI, see [PersistentStorage: Persisting Application State](../../../ui/state-management/arkts-persiststorage.md). > **NOTE：**> Since API version 12, PersistentStorage supports **null** and **undefined**. |
| [SubscribaleAbstract](arkts-arkui-subscribaleabstract-c-sys.md) | Defines the Subscribale base class. |
| [SubscribedAbstractProperty](arkts-arkui-subscribedabstractproperty-c-sys.md) | Represents a synchronized property from [AppStorage](../../../ui/state-management/arkts-appstorage.md) or [LocalStorage](../../../ui/state-management/arkts-localstorage.md). |
| [SyncedPropertyOneWay](arkts-arkui-syncedpropertyoneway-c-sys.md) | Inherits from SubscribedAbstractProperty&lt;T&gt;. Represents a property with one-way synchronization. |
| [SyncedPropertyTwoWay](arkts-arkui-syncedpropertytwoway-c-sys.md) | Inherits from SubscribedAbstractProperty&lt;T&gt;. Represents a property with two-way synchronization. |
<!--DelEnd-->

### Interfaces

| Name | Description |
| --- | --- |
| [AbstractProperty](arkts-arkui-abstractproperty-i.md) | Provides a reference to properties stored in [AppStorage](../../../ui/state-management/arkts-appstorage.md) or [LocalStorage](../../../ui/state-management/arkts-localstorage.md). |
| [EnvPropsOptions](arkts-arkui-envpropsoptions-i.md) | Defines a key-value pair object used to specify environment variable names and their default values, passed as a parameter to [envProps](arkts-arkui-environment-c.md#envprops). |
| [PersistPropsOptions](arkts-arkui-persistpropsoptions-i.md) | Defines a key-value pair object used to specify persistent properties and their default values, passed as a parameter to [persistProps](arkts-arkui-persistentstorage-c.md#persistprops). |

<!--Del-->
### Interfaces（系统接口）

| Name | Description |
| --- | --- |
| [IPropertySubscriber](arkts-arkui-ipropertysubscriber-i-sys.md) | Provides an interface for attribute subscribers. |
| [ISinglePropertyChangeSubscriber](arkts-arkui-isinglepropertychangesubscriber-i-sys.md) | Inherits from IPropertySubscriber. Represents a subscriber that subscribes to changes in a property value. |
<!--DelEnd-->

