# UIUtils

UIUtils is a state management tool class for operating the observed data.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class UIUtils--><!--Device-unnamed-export declare class UIUtils-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## addMonitor

```TypeScript
static addMonitor(valueCallback: MonitorValueCallback | MonitorValueCallback[], 
    monitorCallback: MonitorCallback, options?: MonitorOptions): IMonitorDecoratedVariable
```

Dynamically add monitor for state variable change.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIUtils-static addMonitor(valueCallback: MonitorValueCallback | MonitorValueCallback[],     monitorCallback: MonitorCallback, options?: MonitorOptions): IMonitorDecoratedVariable--><!--Device-UIUtils-static addMonitor(valueCallback: MonitorValueCallback | MonitorValueCallback[],     monitorCallback: MonitorCallback, options?: MonitorOptions): IMonitorDecoratedVariable-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| valueCallback | [MonitorValueCallback](arkts-arkui-monitorvaluecallback-t.md) \| [MonitorValueCallback](arkts-arkui-monitorvaluecallback-t.md)[] | Yes | monitored change for state variable. |
| monitorCallback | [MonitorCallback](arkts-arkui-monitorcallback-t.md) | Yes | the function triggered when state variable changes. |
| options | [MonitorOptions](arkts-arkui-utils-monitoroptions-i.md) | No | the monitor configuration. |

**Return value:**

| Type | Description |
| --- | --- |
| [IMonitorDecoratedVariable](arkts-arkui-decorator-imonitordecoratedvariable-i.md) | monitor handle. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [130000](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-arkui/errorcode-stateManagement.md#130000-invalid-target-object-for-addmonitorclearmonitor) | options.owner is not ComponentV2 struct. |

## addMonitor

```TypeScript
static addMonitor(valueInfo: MonitorValueInfo | MonitorValueInfo[], 
    monitorCallback: MonitorCallback, options?: MonitorBaseOptions): IMonitorDecoratedVariable
```

Dynamically add monitor for state variable change.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIUtils-static addMonitor(valueInfo: MonitorValueInfo | MonitorValueInfo[],     monitorCallback: MonitorCallback, options?: MonitorBaseOptions): IMonitorDecoratedVariable--><!--Device-UIUtils-static addMonitor(valueInfo: MonitorValueInfo | MonitorValueInfo[],     monitorCallback: MonitorCallback, options?: MonitorBaseOptions): IMonitorDecoratedVariable-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| valueInfo | [MonitorValueInfo](arkts-arkui-utils-monitorvalueinfo-i.md) \| [MonitorValueInfo](arkts-arkui-utils-monitorvalueinfo-i.md)[] | Yes | monitored change for state variable. |
| monitorCallback | [MonitorCallback](arkts-arkui-monitorcallback-t.md) | Yes | the function triggered when state variable changes. |
| options | [MonitorBaseOptions](arkts-arkui-utils-monitorbaseoptions-i.md) | No | the monitor configuration. |

**Return value:**

| Type | Description |
| --- | --- |
| [IMonitorDecoratedVariable](arkts-arkui-decorator-imonitordecoratedvariable-i.md) | monitor handle. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [130000](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-arkui/errorcode-stateManagement.md#130000-invalid-target-object-for-addmonitorclearmonitor) | options.owner is not ComponentV2 struct. |

## canBeObserved

```TypeScript
static canBeObserved<T extends object>(source: T): ObservedResult
```

Determine whether the data object is observable and return the observation result.

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIUtils-static canBeObserved<T extends object>(source: T): ObservedResult--><!--Device-UIUtils-static canBeObserved<T extends object>(source: T): ObservedResult-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| source | T | Yes | input source object data. |

**Return value:**

| Type | Description |
| --- | --- |
| [ObservedResult](arkts-arkui-utils-observedresult-i.md) | return result of whether a class is observable. |

## clearMonitor

```TypeScript
static clearMonitor(monitor: IMonitorDecoratedVariable): void
```

Dynamically clear monitor callback for state variable change.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIUtils-static clearMonitor(monitor: IMonitorDecoratedVariable): void--><!--Device-UIUtils-static clearMonitor(monitor: IMonitorDecoratedVariable): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| monitor | [IMonitorDecoratedVariable](arkts-arkui-decorator-imonitordecoratedvariable-i.md) | Yes | handle |

## getCustomComponentContext

```TypeScript
static getCustomComponentContext<T extends IVariableOwner>(customComponent: T): CustomComponentContext
```

Get the custom component context.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIUtils-static getCustomComponentContext<T extends IVariableOwner>(customComponent: T): CustomComponentContext--><!--Device-UIUtils-static getCustomComponentContext<T extends IVariableOwner>(customComponent: T): CustomComponentContext-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| customComponent | T | Yes | custom component instance |

**Return value:**

| Type | Description |
| --- | --- |
| [CustomComponentContext](arkts-arkui-utils-customcomponentcontext-i.md) | current custom component's context handle. |

## getLifecycle

```TypeScript
static getLifecycle<T extends IVariableOwner>(customComponent: T): CustomComponentLifecycle
```

Get lifecycle instance from custom component.

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIUtils-static getLifecycle<T extends IVariableOwner>(customComponent: T): CustomComponentLifecycle--><!--Device-UIUtils-static getLifecycle<T extends IVariableOwner>(customComponent: T): CustomComponentLifecycle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| customComponent | T | Yes | custom component instance |

**Return value:**

| Type | Description |
| --- | --- |
| [CustomComponentLifecycle](arkts-arkui-customcomponent-customcomponentlifecycle-i.md) | the lifecycle that the custom component belong to . |

## getTarget

```TypeScript
static getTarget<T extends object>(source: T): T
```

Get raw object from the Object wrapped with an ObservedObject.If input parameter is a regular Object without ObservedObject, return Object itself.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIUtils-static getTarget<T extends object>(source: T): T--><!--Device-UIUtils-static getTarget<T extends object>(source: T): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| source | T | Yes | input source Object data. |

**Return value:**

| Type | Description |
| --- | --- |
| T | raw object from the Object wrapped with an ObservedObject. |

## makeBinding

```TypeScript
static makeBinding<T>(getter: GetterCallback<T>): Binding<T>
```

Creates read-only data binding.

Example. UIUtils.makeBinding&lt;number&gt;(()=>this.num);

Supports simple getters for read-only data.Intended for primitive value parameters when calling a @Builder function where arguments are of type Binding.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIUtils-static makeBinding<T>(getter: GetterCallback<T>): Binding<T>--><!--Device-UIUtils-static makeBinding<T>(getter: GetterCallback<T>): Binding<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| getter | [GetterCallback](arkts-arkui-gettercallback-t.md)&lt;T&gt; | Yes | A value or a function that returns the current value of type T. |

**Return value:**

| Type | Description |
| --- | --- |
| [Binding](arkts-arkui-utils-binding-c.md)&lt;T&gt; | read-only data binding value |

## makeBinding

```TypeScript
static makeBinding<T>(getter: GetterCallback<T>, setter: SetterCallback<T>): MutableBinding<T>
```

Creates a mutable data binding.

Two functions to implement function overloading.

Example. UIUtils.makeBinding&lt;number&gt;(()=>this.num, val => this.num = val);

Supports getter-setter pairs for mutable data.Intended for primitive value parameters when calling a @Builder function where arguments are of type MutableBinding.If provided, a MutableBinding is created.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIUtils-static makeBinding<T>(getter: GetterCallback<T>, setter: SetterCallback<T>): MutableBinding<T>--><!--Device-UIUtils-static makeBinding<T>(getter: GetterCallback<T>, setter: SetterCallback<T>): MutableBinding<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| getter | [GetterCallback](arkts-arkui-gettercallback-t.md)&lt;T&gt; | Yes | A value or a function that returns the current value of type T. |
| setter | [SetterCallback](arkts-arkui-settercallback-t.md)&lt;T&gt; | Yes | A function to set a new value of type T. |

**Return value:**

| Type | Description |
| --- | --- |
| [MutableBinding](arkts-arkui-utils-mutablebinding-c.md)&lt;T&gt; | mutable data binding value |

## makeObserved

```TypeScript
static makeObserved<T extends object | null | undefined>(source: T): T
```

Make non-observed data into observed data.Support built-in type and objectLiteral.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIUtils-static makeObserved<T extends object | null | undefined>(source: T): T--><!--Device-UIUtils-static makeObserved<T extends object | null | undefined>(source: T): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| source | T | Yes | input source object data. |

**Return value:**

| Type | Description |
| --- | --- |
| T | proxy object from the source object data. |

## makeObserved

```TypeScript
static makeObserved<T extends object | null | undefined>(source: T, allowDeep: boolean): T
```

Make non-observed data into observed data.Support built-in type and objectLiteral.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIUtils-static makeObserved<T extends object | null | undefined>(source: T, allowDeep: boolean): T--><!--Device-UIUtils-static makeObserved<T extends object | null | undefined>(source: T, allowDeep: boolean): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| source | T | Yes | input source object data. |
| allowDeep | boolean | Yes | enable deep observable. |

**Return value:**

| Type | Description |
| --- | --- |
| T | proxy object from the source object data. |

