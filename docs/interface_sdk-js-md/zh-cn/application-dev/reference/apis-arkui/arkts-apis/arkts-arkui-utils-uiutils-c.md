# UIUtils

UIUtils是状态管理提供的工具，用于处理可观察数据。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## addMonitor

```TypeScript
static addMonitor(valueCallback: MonitorValueCallback | MonitorValueCallback[], 
    monitorCallback: MonitorCallback, options?: MonitorOptions): IMonitorDecoratedVariable
```

动态地为状态变量注册监听。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| valueCallback | [MonitorValueCallback](arkts-arkui-monitorvaluecallback-t.md) \| [MonitorValueCallback](arkts-arkui-monitorvaluecallback-t.md)[] | 是 |
| monitorCallback | [MonitorCallback](arkts-arkui-monitorcallback-t.md) | 是 |
| options | [MonitorOptions](arkts-arkui-utils-monitoroptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [IMonitorDecoratedVariable](arkts-arkui-decorator-imonitordecoratedvariable-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [130000](../errorcode-stateManagement.md#130000-addmonitorclearmonitor非法目标对象) |

## addMonitor

```TypeScript
static addMonitor(valueInfo: MonitorValueInfo | MonitorValueInfo[], 
    monitorCallback: MonitorCallback, options?: MonitorBaseOptions): IMonitorDecoratedVariable
```

动态地为状态变量注册监听。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| valueInfo | [MonitorValueInfo](arkts-arkui-utils-monitorvalueinfo-i.md) \| [MonitorValueInfo](arkts-arkui-utils-monitorvalueinfo-i.md)[] | 是 |
| monitorCallback | [MonitorCallback](arkts-arkui-monitorcallback-t.md) | 是 |
| options | [MonitorBaseOptions](arkts-arkui-utils-monitorbaseoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [IMonitorDecoratedVariable](arkts-arkui-decorator-imonitordecoratedvariable-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [130000](../errorcode-stateManagement.md#130000-addmonitorclearmonitor非法目标对象) |

## canBeObserved

```TypeScript
static canBeObserved<T extends object>(source: T): ObservedResult
```

判断数据对象是否为可观察对象，并返回观察结果。详见 canBeObserved接口：判断对象是否为可被观察对象。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| source | T | 是 |

**返回值：**

| 类型 |
| --- |
| [ObservedResult](arkts-arkui-utils-observedresult-i.md) |

## clearMonitor

```TypeScript
static clearMonitor(monitor: IMonitorDecoratedVariable): void
```

动态地为状态变量解绑监听。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| monitor | [IMonitorDecoratedVariable](arkts-arkui-decorator-imonitordecoratedvariable-i.md) | 是 |

## getCustomComponentContext

```TypeScript
static getCustomComponentContext<T extends IVariableOwner>(customComponent: T): CustomComponentContext
```

获取自定义组件的上下文信息。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| customComponent | T | 是 |

**返回值：**

| 类型 |
| --- |
| [CustomComponentContext](arkts-arkui-utils-customcomponentcontext-i.md) |

## getLifecycle

```TypeScript
static getLifecycle<T extends IVariableOwner>(customComponent: T): CustomComponentLifecycle
```

getLifecycle用于获取[自定义组件的生命周期](arkts-arkui-decorator-componentinit-i.md)实例。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| customComponent | T | 是 |

**返回值：**

| 类型 |
| --- |
| [CustomComponentLifecycle](arkts-arkui-customcomponent-customcomponentlifecycle-i.md) |

## getTarget

```TypeScript
static getTarget<T extends object>(source: T): T
```

获取状态管理框架包装前的原始对象。支持built-in类型（Array、Map、Set、Date）以及interface字面量。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| source | T | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## makeBinding

```TypeScript
static makeBinding<T>(getter: GetterCallback<T>): Binding<T>
```

创建只读的单向数据绑定实例，用于在@Builder函数中为参数类型为Binding的参数提供实参。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| getter | [GetterCallback](arkts-arkui-gettercallback-t.md)&lt;T&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| [Binding](arkts-arkui-utils-binding-c.md)&lt;T&gt; |

## makeBinding

```TypeScript
static makeBinding<T>(getter: GetterCallback<T>, setter: SetterCallback<T>): MutableBinding<T>
```

创建双向数据绑定实例，用于构建@Builder函数中类型为MutableBinding的参数。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| getter | [GetterCallback](arkts-arkui-gettercallback-t.md)&lt;T&gt; | 是 |
| [setter](../../apis-ability-kit/arkts-apis/arkts-ability-appmanager-keepalivebundleinfo-i-sys.md) | [SetterCallback](arkts-arkui-settercallback-t.md)&lt;T&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| [MutableBinding](arkts-arkui-utils-mutablebinding-c.md)&lt;T&gt; |

## makeObserved

```TypeScript
static makeObserved<T extends object | null | undefined>(source: T): T
```

将不可观察数据转化为可观察数据。支持built-in类型（Array、Map、Set、Date）以及interface字面量。

> **说明：**

> 默认情况下，返回对象支持深度观察，可观察嵌套属性变化。

> 如果传入了undefined或null，则直接返回传入值。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| source | T | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## makeObserved

```TypeScript
static makeObserved<T extends object | null | undefined>(source: T, allowDeep: boolean): T
```

将不可观察数据转化为可观察数据，并通过`allowDeep`控制观察深度。支持built-in类型（Array、Map、Set、Date）以及interface字面量。

> **说明：**

> 如果传入了undefined或null，则直接返回传入值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| source | T | 是 |
| allowDeep | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| T |
