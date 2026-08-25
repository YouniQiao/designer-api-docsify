# UIUtils

UIUtils状态管理相关的工具方法，包括获取代理对象的原始对象、将非观察数据变为可观察数据、动态添加和删除状态变量监听、同步刷新状态变量修改、创建数据绑定等，适用于需要手动管理状态观察、监听和同步刷新的场景。

**起始版本：** 12

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
import { AppStorageV2, PersistenceV2, Type, UIUtils, ConnectOptions, Binding, MutableBinding, CustomComponentLifecycle, CustomComponentLifecycleObserver, CustomComponentLifecycleState, ComponentInit, ComponentAppear, ComponentBuilt, ComponentReuse, ComponentActive, ComponentInactive, ComponentRecycle, ComponentDisappear, CollectionType, ConnectOptionsCollections, CustomComponentContext, IReusePool, IReusableInfo } from 'kits/@kit.ArkUI';
```

## addMonitor

```TypeScript
static addMonitor(target: object, path: string | string[], monitorCallback: MonitorCallback, options?: MonitorOptions): void
```

给状态管理V2的状态变量动态添加监听方法，详见 [addMonitor/clearMonitor](../../../ui/state-management/arkts-new-addMonitor-clearMonitor.md)。

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| target | object | 是 |
| path | string \| string[] | 是 |
| monitorCallback | [MonitorCallback](arkts-arkui-monitorcallback-t.md) | 是 |
| options | [MonitorOptions](arkts-arkui-arkui-statemanagement-monitoroptions-i.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [130000](../errorcode-stateManagement.md#130000-addmonitorclearmonitor非法目标对象) |
| [130001](../errorcode-stateManagement.md#130001-addmonitorclearmonitor非法路径) |
| [130002](../errorcode-stateManagement.md#130002-addmonitorclearmonitor非法回调方法) |

## applySync

```TypeScript
static applySync<T>(task: TaskCallback): T
```

同步刷新指定的状态变量，该接口接收一个闭包函数，仅刷新闭包函数内的修改，包括更新[@Computed计算](../../../ui/state-management/arkts-new-computed.md)、 [@Monitor回调](../../../ui/state-management/arkts-new-monitor.md)以及重新渲染UI节点，详见 [applySync/flushUpdates/flushUIUpdates接口：同步刷新](../../../ui/state-management/arkts-new-applySync-flushUpdates-flushUIUpdates.md)。

**起始版本：** 22

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| task | [TaskCallback](arkts-arkui-taskcallback-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

**错误码：**

| 错误码ID |
| --- |
| [140001](../errorcode-stateManagement.md#140001-applysyncflushupdatesflushuiupdates非法调用) |

## canBeObserved

```TypeScript
static canBeObserved<T extends object>(source: T): ObservedResult
```

判断数据对象是否为可观察对象，并返回观察结果。详见[canBeObserved接口：判断对象是否为可被观察对象](../../../ui/state-management/arkts-new-canBeObserved.md)。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| source | T | 是 |

**返回值：**

| 类型 |
| --- |
| [ObservedResult](arkts-arkui-arkui-statemanagement-observedresult-i.md) |

## clearMonitor

```TypeScript
static clearMonitor(target: object, path: string | string[], monitorCallback?: MonitorCallback) : void
```

删除通过[addMonitor](#addmonitor)给状态管理V2的状态变量添加的监听方法，详见 [addMonitor/clearMonitor](../../../ui/state-management/arkts-new-addMonitor-clearMonitor.md)。

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| target | object | 是 |
| path | string \| string[] | 是 |
| monitorCallback | [MonitorCallback](arkts-arkui-monitorcallback-t.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [130000](../errorcode-stateManagement.md#130000-addmonitorclearmonitor非法目标对象) |
| [130001](../errorcode-stateManagement.md#130001-addmonitorclearmonitor非法路径) |
| [130002](../errorcode-stateManagement.md#130002-addmonitorclearmonitor非法回调方法) |

## enableV2Compatibility

```TypeScript
static enableV2Compatibility<T extends object>(source: T): T
```

使V1的状态变量能够在\@ComponentV2中观察，主要应用于状态管理V1、V2混用场景。详见 [状态管理V1和V2混用指导（API version 19及之后）](../../../ui/state-management/arkts-v1-v2-mixusage.md)。

**起始版本：** 19

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| source | T | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## flushUIUpdates

```TypeScript
static flushUIUpdates(): void
```

立即处理在调用该函数之前所有的状态变量修改，同步[标脏](../../../ui/state-management/arkts-state-management-introduce.md#触发更新)对应的UI节点，但不会同步执行 @Computed计算和@Monitor回调，详见 [applySync/flushUpdates/flushUIUpdates接口：同步刷新](../../../ui/state-management/arkts-new-applySync-flushUpdates-flushUIUpdates.md)。

**起始版本：** 22

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**错误码：**

| 错误码ID |
| --- |
| [140001](../errorcode-stateManagement.md#140001-applysyncflushupdatesflushuiupdates非法调用) |
| [140002](../errorcode-stateManagement.md#140002-flushupdatesflushuiupdates非法调用) |

## flushUpdates

```TypeScript
static flushUpdates(): void
```

同步刷新在调用该函数之前所有的状态变量修改，包括更新@Computed计算、@Monitor回调以及重新渲染UI节点，详见 [applySync/flushUpdates/flushUIUpdates接口：同步刷新](../../../ui/state-management/arkts-new-applySync-flushUpdates-flushUIUpdates.md)。

**起始版本：** 22

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**错误码：**

| 错误码ID |
| --- |
| [140001](../errorcode-stateManagement.md#140001-applysyncflushupdatesflushuiupdates非法调用) |
| [140002](../errorcode-stateManagement.md#140002-flushupdatesflushuiupdates非法调用) |

## getCustomComponentContext

```TypeScript
static getCustomComponentContext<T extends BaseCustomComponent>(customComponent: T): CustomComponentContext
```

返回给定@Component(V1)或@ComponentV2的[CustomComponentContext](arkts-arkui-arkui-statemanagement-customcomponentcontext-i.md)。使用它来访问组件的复用池。有关复用池的详细信息，请参阅 [全局复用池：集中化的组件回收与复用](../../../ui/state-management/arkts-global-reuse-pool.md)。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| customComponent | T | 是 |

**返回值：**

| 类型 |
| --- |
| [CustomComponentContext](arkts-arkui-arkui-statemanagement-customcomponentcontext-i.md) |

## getLifecycle

```TypeScript
static getLifecycle<T extends BaseCustomComponent>(customComponent: T): CustomComponentLifecycle
```

getLifecycle用于获取自定义组件的生命周期实例。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| customComponent | T | 是 |

**返回值：**

| 类型 |
| --- |
| [CustomComponentLifecycle](arkts-arkui-arkui-statemanagement-customcomponentlifecycle-i.md) |

## getTarget

```TypeScript
static getTarget<T extends object>(source: T): T
```

从状态管理框架包裹的代理对象中获取原始对象。详见[getTarget接口：获取状态管理框架代理前的原始对象](../../../ui/state-management/arkts-new-getTarget.md)。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

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

创建只读的单向数据绑定实例，用于构建[\@Builder](../../../ui/state-management/arkts-builder.md)函数中参数类型为`Binding`的对应实参。

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| getter | [GetterCallback](arkts-arkui-gettercallback-t.md)&lt;T&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| [Binding](arkts-arkui-arkui-statemanagement-binding-c.md)&lt;T&gt; |

## makeBinding

```TypeScript
static makeBinding<T>(getter: GetterCallback<T>, setter: SetterCallback<T>): MutableBinding<T>
```

创建可修改的双向数据绑定实例，用于构建\@Builder函数中参数类型为`MutableBinding`的对应实参。

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| getter | [GetterCallback](arkts-arkui-gettercallback-t.md)&lt;T&gt; | 是 |
| [setter](../../apis-ability-kit/arkts-apis/arkts-ability-appmanager-keepalivebundleinfo-i-sys.md) | [SetterCallback](arkts-arkui-settercallback-t.md)&lt;T&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| [MutableBinding](arkts-arkui-arkui-statemanagement-mutablebinding-c.md)&lt;T&gt; |

## makeObserved

```TypeScript
static makeObserved<T extends object>(source: T): T
```

将普通不可观察数据变为可观察数据。详见[makeObserved接口：将非观察数据变为可观察数据](../../../ui/state-management/arkts-new-makeObserved.md)。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| source | T | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## makeV1Observed

```TypeScript
static makeV1Observed<T extends object>(source: T): T
```

将不可观察的对象包装成状态管理V1可观察的对象，其能力等同于@Observed，可初始化@ObjectLink。该接口可搭配[enableV2Compatibility](#enablev2compatibility)应用于状态管理V1和V2混用场景，详见 [状态管理V1和V2混用指导（API version 19及之后）](../../../ui/state-management/arkts-v1-v2-mixusage.md)。

**起始版本：** 19

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| source | T | 是 |

**返回值：**

| 类型 |
| --- |
| T |
