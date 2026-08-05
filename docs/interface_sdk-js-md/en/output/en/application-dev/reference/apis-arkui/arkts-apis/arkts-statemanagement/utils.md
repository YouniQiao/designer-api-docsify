# stateManagement/utils

## Summary

### Classes

| Name | Description |
| --- | --- |
| [Binding](utils-binding-c.md) | Represents a read-only data binding. Use with @Builder argument list for primitive types. Use makeBinding to pass values when calling the function. |
| [MutableBinding](utils-mutablebinding-c.md) | Represents a mutable data binding allowing both read and write operations. Use with @Builder argument list for primitive types. Use makeBinding to pass values when calling the function. |
| [ObservedArray](utils-observedarray-c.md) | Observable Array base class. |
| [ObservedDate](utils-observeddate-c.md) | Observable Date base class. |
| [ObservedMap](utils-observedmap-c.md) | Observable Map base class. |
| [ObservedSet](utils-observedset-c.md) | Observable Set base class. |
| [UIUtils](utils-uiutils-c.md) | UIUtils is a state management tool class for operating the observed data. |

### Interfaces

| Name | Description |
| --- | --- |
| [CustomComponentContext](utils-customcomponentcontext-i.md) | CustomComponentContext is a state management tool for operating the observed data. |
| [DecoratorInfo](utils-decoratorinfo-i.md) | The UI component information associated with the object data. |
| [ElementInfo](utils-elementinfo-i.md) | The custom component and UI component information. For the V2 @Monitor or @Computed scenario, The id and decorated function name by @Monitor or @Computed will be returned. |
| [IReusableInfo](utils-ireusableinfo-i.md) | IReusableInfo is a reuse pool information interface for custom component. |
| [IReusePool](utils-ireusepool-i.md) | IReusePool is a reuse pool interface for custom component. |
| [MonitorBaseOptions](utils-monitorbaseoptions-i.md) | Define MonitorBaseOptions. |
| [MonitorOptions](utils-monitoroptions-i.md) | Define Monitor options. |
| [MonitorValueInfo](utils-monitorvalueinfo-i.md) | Define MonitorValueInfo. |
| [ObservedResult](utils-observedresult-i.md) | The return result that defines whether the object data is observable. |

### Types

| Name | Description |
| --- | --- |
| [ActiveAndInactiveCallbackType](arkts-arkui-activeandinactivecallbacktype-t.md) | Defines active and inactive function callback. |
| [GetterCallback](arkts-arkui-gettercallback-t.md) | Getter callback type. It is used to get value. |
| [ObservedArrayInitializer](arkts-arkui-observedarrayinitializer-t.md) | Array initializer Type. |
| [SetterCallback](arkts-arkui-settercallback-t.md) | Setter callback type. It is used to assign a new value. |

