# CustomComponentAsyncLoadOptions

```TypeScript
export declare interface CustomComponentAsyncLoadOptions
```

描述自定义组件异步加载的配置选项。

**起始版本：** 26.1.0

<!--Device-unnamed-export declare interface CustomComponentAsyncLoadOptions--><!--Device-unnamed-export declare interface CustomComponentAsyncLoadOptions-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
import { AppStorageV2, PersistenceV2, Type, UIUtils, ConnectOptions, Binding, MutableBinding, CustomComponentLifecycle, CustomComponentLifecycleObserver, CustomComponentLifecycleState, ComponentInit, ComponentAppear, ComponentBuilt, ComponentReuse, ComponentActive, ComponentInactive, ComponentRecycle, ComponentDisappear, CollectionType, ConnectOptionsCollections, CustomComponentContext, CustomComponentAsyncLoadOptions, IReusePool, IDefaultReusePool, IReusableInfo, StorageDefaultCreator, TypeConstructorWithArgs, PersistenceErrorCallback, TypeConstructor, TypeDecorator, MonitorCallback, MonitorOptions, GetterCallback, SetterCallback, ObservedResult, DecoratorInfo, ElementInfo, RecoverableStorage, RecoverableConnectOptions, RecoverableStorageError, NotifyOnErrorCallback } from '@kit.ArkUI';
```

## placeholder

```TypeScript
placeholder?: PlaceholderOptions
```

异步加载期间显示的占位组件。取值为PlaceholderOptions对象：**id**指向经getPlaceholderRegister()注册的模板，**size**为**SizeOptions**类型的布局建议。若配置，该尺寸作为占位根节点的理想尺寸参与测量：数字单位为vp，带单位字符串保留其单位，Resource类型视为未设置。**size**未配置，或其中某一维未设置或非法时，占位组件按占位模板自身的设置布局。

未配置**placeholder**，或其**id**为空或未注册时，异步加载完成前不显示占位组件。

**类型：** PlaceholderOptions

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-CustomComponentAsyncLoadOptions-placeholder?: PlaceholderOptions--><!--Device-CustomComponentAsyncLoadOptions-placeholder?: PlaceholderOptions-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## timeout

```TypeScript
timeout?: number
```

异步加载的超时阈值，单位ms，默认值为**1000**。

取值可为任意数值。**NaN**按默认值（**1000**）处理，**正/负无穷大**按负值处理。正小数值向上取整到整毫秒。若组件在**timeout**毫秒内未完成加载，框架会在后续帧中强制加载该组件，且单帧强制加载的组件数量不超过系统定义的上限。取值**0**表示不等待：组件在后续帧中被强制加载。取值为负数（含**正/负无穷大**）表示永不超时：组件持续等待直至异步加载完成。

**类型：** number

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-CustomComponentAsyncLoadOptions-timeout?: number--><!--Device-CustomComponentAsyncLoadOptions-timeout?: number-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full
