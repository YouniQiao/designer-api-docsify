# UIUtils

UIUtils是状态管理提供的工具，用于处理可观察数据。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class UIUtils--><!--Device-unnamed-export declare class UIUtils-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## addMonitor

```TypeScript
static addMonitor(valueCallback: MonitorValueCallback | MonitorValueCallback[], 
    monitorCallback: MonitorCallback, options?: MonitorOptions): IMonitorDecoratedVariable
```

动态地为状态变量注册监听。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIUtils-static addMonitor(valueCallback: MonitorValueCallback | MonitorValueCallback[],     monitorCallback: MonitorCallback, options?: MonitorOptions): IMonitorDecoratedVariable--><!--Device-UIUtils-static addMonitor(valueCallback: MonitorValueCallback | MonitorValueCallback[],     monitorCallback: MonitorCallback, options?: MonitorOptions): IMonitorDecoratedVariable-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| valueCallback | [MonitorValueCallback](arkts-arkui-monitorvaluecallback-t.md) \| MonitorValueCallback[] | Yes | 返回被监听状态变量的箭头函数或箭头函数数组。 |
| monitorCallback | [MonitorCallback](arkts-arkui-monitorcallback-t.md) | Yes | 触发监听时调用的回调函数。 |
| options | [MonitorOptions](arkts-arkui-arkui-statemanagement-monitoroptions-i.md) | No | 设置函数的行为，默认行行为详见[MonitorOptions]{ |

**Return value:**

| Type | Description |
| --- | --- |
| [IMonitorDecoratedVariable](arkts-arkui-decorator-imonitordecoratedvariable-i.md) | 指代监听关系的句柄。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 130000 | options.owner is not ComponentV2 struct. |

## addMonitor

```TypeScript
static addMonitor(valueInfo: MonitorValueInfo | MonitorValueInfo[], 
    monitorCallback: MonitorCallback, options?: MonitorBaseOptions): IMonitorDecoratedVariable
```

动态地为状态变量注册监听。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIUtils-static addMonitor(valueInfo: MonitorValueInfo | MonitorValueInfo[],     monitorCallback: MonitorCallback, options?: MonitorBaseOptions): IMonitorDecoratedVariable--><!--Device-UIUtils-static addMonitor(valueInfo: MonitorValueInfo | MonitorValueInfo[],     monitorCallback: MonitorCallback, options?: MonitorBaseOptions): IMonitorDecoratedVariable-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| valueInfo | [MonitorValueInfo](arkts-arkui-utils-monitorvalueinfo-i.md) \| MonitorValueInfo[] | Yes | 监听变量的信息或其数组。 |
| monitorCallback | [MonitorCallback](arkts-arkui-monitorcallback-t.md) | Yes | 触发监听时调用的回调函数。 |
| options | [MonitorBaseOptions](arkts-arkui-utils-monitorbaseoptions-i.md) | No | 设置函数的行为，默认行为详见[MonitorBaseOptions](arkts-arkui-utils-monitorbaseoptions-i.md)。 |

**Return value:**

| Type | Description |
| --- | --- |
| [IMonitorDecoratedVariable](arkts-arkui-decorator-imonitordecoratedvariable-i.md) | 指代监听关系的句柄。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 130000 | options.owner is not ComponentV2 struct. |

## canBeObserved

```TypeScript
static canBeObserved<T extends object>(source: T): ObservedResult
```

判断数据对象是否为可观察对象，并返回观察结果。详见  
[canBeObserved接口：判断对象是否为可被观察对象](../../../ui/state-management-static/arkts-static-new-canBeObserved.md)。

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIUtils-static canBeObserved<T extends object>(source: T): ObservedResult--><!--Device-UIUtils-static canBeObserved<T extends object>(source: T): ObservedResult-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| source | T | Yes | 输入一个数据对象，判断其是否可被观察。 &lt;/br&gt;具体使用规则，详见 [canBeObserved接口：判断对象是否为可被观察对象](../../../ui/state-management-static/arkts-static-new-canBeObserved.md)。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ObservedResult](arkts-arkui-arkui-statemanagement-observedresult-i.md) | 返回对象是否可被观察的结果。 |

## clearMonitor

```TypeScript
static clearMonitor(monitor: IMonitorDecoratedVariable): void
```

动态地为状态变量解绑监听。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIUtils-static clearMonitor(monitor: IMonitorDecoratedVariable): void--><!--Device-UIUtils-static clearMonitor(monitor: IMonitorDecoratedVariable): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| monitor | [IMonitorDecoratedVariable](arkts-arkui-decorator-imonitordecoratedvariable-i.md) | Yes | 指代监听关系的句柄。 |

## getCustomComponentContext

```TypeScript
static getCustomComponentContext<T extends IVariableOwner>(customComponent: T): CustomComponentContext
```

获取自定义组件的上下文信息。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIUtils-static getCustomComponentContext<T extends IVariableOwner>(customComponent: T): CustomComponentContext--><!--Device-UIUtils-static getCustomComponentContext<T extends IVariableOwner>(customComponent: T): CustomComponentContext-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| customComponent | T | Yes | 自定义组件对象。 |

**Return value:**

| Type | Description |
| --- | --- |
| [CustomComponentContext](arkts-arkui-utils-customcomponentcontext-i.md) | 传入自定义组件的上下文信息。 |

## getLifecycle

```TypeScript
static getLifecycle<T extends IVariableOwner>(customComponent: T): CustomComponentLifecycle
```

getLifecycle用于获取[自定义组件的生命周期](arkts-arkui-decorator-componentinit-i.md)实例。

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIUtils-static getLifecycle<T extends IVariableOwner>(customComponent: T): CustomComponentLifecycle--><!--Device-UIUtils-static getLifecycle<T extends IVariableOwner>(customComponent: T): CustomComponentLifecycle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| customComponent | T | Yes | 自定义组件实例。 |

**Return value:**

| Type | Description |
| --- | --- |
| [CustomComponentLifecycle](arkts-arkui-customcomponent-customcomponentlifecycle-i.md) | 自定义组件的生命周期实例。 |

## getTarget

```TypeScript
static getTarget<T extends object>(source: T): T
```

获取状态管理框架包装前的原始对象。支持built-in类型（Array、Map、Set、Date）以及interface字面量。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIUtils-static getTarget<T extends object>(source: T): T--><!--Device-UIUtils-static getTarget<T extends object>(source: T): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| source | T | Yes | 状态管理框架包装的对象。 |

**Return value:**

| Type | Description |
| --- | --- |
| T | 状态管理框架包装前的原始对象。 |

## makeBinding

```TypeScript
static makeBinding<T>(getter: GetterCallback<T>): Binding<T>
```

创建只读的单向数据绑定实例，用于在@Builder函数中为参数类型为Binding的参数提供实参。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIUtils-static makeBinding<T>(getter: GetterCallback<T>): Binding<T>--><!--Device-UIUtils-static makeBinding<T>(getter: GetterCallback<T>): Binding<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| getter | [GetterCallback](arkts-arkui-gettercallback-t.md)&lt;T&gt; | Yes | 获取值的回调函数，每次访问值时重新执行以获取最新值。 |

**Return value:**

| Type | Description |
| --- | --- |
| [Binding](arkts-arkui-arkui-statemanagement-binding-c.md)&lt;T&gt; | 包含一个value属性，用于获取当前绑定的值，且只能读取，不能修改。 |

## makeBinding

```TypeScript
static makeBinding<T>(getter: GetterCallback<T>, setter: SetterCallback<T>): MutableBinding<T>
```

创建双向数据绑定实例，用于构建@Builder函数中类型为MutableBinding的参数。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIUtils-static makeBinding<T>(getter: GetterCallback<T>, setter: SetterCallback<T>): MutableBinding<T>--><!--Device-UIUtils-static makeBinding<T>(getter: GetterCallback<T>, setter: SetterCallback<T>): MutableBinding<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| getter | [GetterCallback](arkts-arkui-gettercallback-t.md)&lt;T&gt; | Yes | 获取值的回调函数，每次访问值时重新执行。 |
| setter | [SetterCallback](arkts-arkui-settercallback-t.md)&lt;T&gt; | Yes | 定义如何更新值，当.value被修改时调用。 |

**Return value:**

| Type | Description |
| --- | --- |
| [MutableBinding](arkts-arkui-utils-mutablebinding-c.md)&lt;T&gt; | 包含一个value属性，支持读取和修改数据，设置值时检查类型是否匹配泛型`T`。 |

## makeObserved

```TypeScript
static makeObserved<T extends object | null | undefined>(source: T): T
```

将不可观察数据转化为可观察数据。支持built-in类型（Array、Map、Set、Date）以及interface字面量。

> **说明：**

> 默认情况下，返回对象支持深度观察，可观察嵌套属性变化。

> 如果传入了undefined或null，则直接返回传入值。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIUtils-static makeObserved<T extends object | null | undefined>(source: T): T--><!--Device-UIUtils-static makeObserved<T extends object | null | undefined>(source: T): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| source | T | Yes | 数据源对象。 |

**Return value:**

| Type | Description |
| --- | --- |
| T | 可观察的数据对象。 |

## makeObserved

```TypeScript
static makeObserved<T extends object | null | undefined>(source: T, allowDeep: boolean): T
```

将不可观察数据转化为可观察数据，并通过`allowDeep`控制观察深度。支持built-in类型（Array、Map、Set、Date）以及interface字面量。

> **说明：**

> 如果传入了undefined或null，则直接返回传入值。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIUtils-static makeObserved<T extends object | null | undefined>(source: T, allowDeep: boolean): T--><!--Device-UIUtils-static makeObserved<T extends object | null | undefined>(source: T, allowDeep: boolean): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| source | T | Yes | 数据源对象。 |
| allowDeep | boolean | Yes | 是否深度观察。传入`true`时为深度观察；传入`false`时仅观察第一层属性变化。 |

**Return value:**

| Type | Description |
| --- | --- |
| T | 可观察的数据对象。 |

