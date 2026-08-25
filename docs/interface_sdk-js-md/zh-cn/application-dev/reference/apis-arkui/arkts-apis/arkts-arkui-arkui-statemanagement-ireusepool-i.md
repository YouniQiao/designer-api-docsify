# IReusePool

`IReusePool`接口提供自定义组件上的全局复用池的相关功能，包括查询回收组件的当前数量和上限信息、预渲染可复用组件到复用池中等，适用于开发者需要手动管理和优化组件复用效率的场景。

**起始版本：** 26.0.0

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
import { AppStorageV2, PersistenceV2, Type, UIUtils, ConnectOptions, Binding, MutableBinding, CustomComponentLifecycle, CustomComponentLifecycleObserver, CustomComponentLifecycleState, ComponentInit, ComponentAppear, ComponentBuilt, ComponentReuse, ComponentActive, ComponentInactive, ComponentRecycle, ComponentDisappear, CollectionType, ConnectOptionsCollections, CustomComponentContext, IReusePool, IReusableInfo } from 'kits/@kit.ArkUI';
```

## getReusableInfo

```TypeScript
getReusableInfo(constructor: ReusableComponentConstructor,
    reuseId?: string): IReusableInfo[] | IReusableInfo | undefined
```

检索此复用池中给定可复用组件类型的回收实例信息。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| constructor | [ReusableComponentConstructor](arkts-arkui-reusablecomponentconstructor-t.md) | 是 |
| reuseId | string | 否 |

**返回值：**

| 类型 |
| --- |
| [IReusableInfo](arkts-arkui-arkui-statemanagement-ireusableinfo-i.md)[] \| [IReusableInfo](arkts-arkui-arkui-statemanagement-ireusableinfo-i.md) \| undefined |

## preRender

```TypeScript
preRender(builder: WrappedBuilder<[]>, times: number): Promise<void>
```

调用空闲任务以预创建可复用组件并在首次使用前将其放入复用池。

> **说明：**&gt;
> 1. `preRender`仅将池配置为接受的组件放入池中。预渲染池不接受的组件会立即创建并销毁。&gt;
> 2. 预渲染期间不会从池中复用组件；池仅接受新创建的实例。&gt;
> 3. @Builder函数执行完整的深度渲染，包括嵌套的子组件。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| builder | [WrappedBuilder](../arkts-components/arkts-arkui-wrappedbuilder-c.md)&lt;[]&gt; | 是 |
| times | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |
