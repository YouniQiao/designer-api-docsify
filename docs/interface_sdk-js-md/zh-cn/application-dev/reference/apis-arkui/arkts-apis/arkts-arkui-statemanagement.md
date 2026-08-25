# @ohos.arkui.StateManagement(状态管理)

状态管理模块具备应用数据存储、持久化管理以及UIAbility（包含用户界面的应用组件）数据存储能力，同时覆盖环境状态、工具和UI状态同步等场景，从而帮助开发者简化状态管理逻辑，提升应用的响应能力和数据一致性。
 本文中T和S的含义如下：
| [类型](#类型) |
| ---- |
| T    |
| S    |


## 导入模块

```TypeScript
import { AppStorageV2, PersistenceV2, Type, UIUtils, ConnectOptions, Binding, MutableBinding, CustomComponentLifecycle, CustomComponentLifecycleObserver, CustomComponentLifecycleState, ComponentInit, ComponentAppear, ComponentBuilt, ComponentReuse, ComponentActive, ComponentInactive, ComponentRecycle, ComponentDisappear, CollectionType, ConnectOptionsCollections, CustomComponentContext, IReusePool, IReusableInfo } from '@kit.ArkUI';
```

## 汇总

### 类

| 名称 |
| --- |
| [AppStorageV2(状态管理)](arkts-arkui-arkui-statemanagement-appstoragev2-c.md) |
| [Binding(状态管理)](arkts-arkui-arkui-statemanagement-binding-c.md) |
| [ConnectOptions(状态管理)](arkts-arkui-arkui-statemanagement-connectoptions-c.md) |
| [ConnectOptionsCollections(状态管理)](arkts-arkui-arkui-statemanagement-connectoptionscollections-c.md) |
| [MutableBinding(状态管理)](arkts-arkui-arkui-statemanagement-mutablebinding-c.md) |
| [PersistenceV2(状态管理)](arkts-arkui-arkui-statemanagement-persistencev2-c.md) |
| [UIUtils(状态管理)](arkts-arkui-arkui-statemanagement-uiutils-c.md) |

### 接口

| 名称 |
| --- |
| [CustomComponentContext(状态管理)](arkts-arkui-arkui-statemanagement-customcomponentcontext-i.md) |
| [CustomComponentLifecycle(状态管理)](arkts-arkui-arkui-statemanagement-customcomponentlifecycle-i.md) |
| [CustomComponentLifecycleObserver(状态管理)](arkts-arkui-arkui-statemanagement-customcomponentlifecycleobserver-i.md) |
| [DecoratorInfo(状态管理)](arkts-arkui-arkui-statemanagement-decoratorinfo-i.md) |
| [ElementInfo(状态管理)](arkts-arkui-arkui-statemanagement-elementinfo-i.md) |
| [IReusableInfo(状态管理)](arkts-arkui-arkui-statemanagement-ireusableinfo-i.md) |
| [IReusePool(状态管理)](arkts-arkui-arkui-statemanagement-ireusepool-i.md) |
| [MonitorOptions(状态管理)](arkts-arkui-arkui-statemanagement-monitoroptions-i.md) |
| [ObservedResult(状态管理)](arkts-arkui-arkui-statemanagement-observedresult-i.md) |
| [TypeConstructor(状态管理)](arkts-arkui-arkui-statemanagement-typeconstructor-i.md) |
| [TypeConstructorWithArgs(状态管理)](arkts-arkui-arkui-statemanagement-typeconstructorwithargs-i.md) |

### 枚举

| 名称 |
| --- |
| [CustomComponentLifecycleState(状态管理)](arkts-arkui-arkui-statemanagement-customcomponentlifecyclestate-e.md) |

### 类型

| 名称 |
| --- |
| [CollectionType(状态管理)](arkts-arkui-collectiontype-t.md) |
| [GetterCallback(状态管理)](arkts-arkui-gettercallback-t.md) |
| [MonitorCallback(状态管理)](arkts-arkui-monitorcallback-t.md) |
| [PersistenceErrorCallback(状态管理)](arkts-arkui-persistenceerrorcallback-t.md) |
| [ReusableComponentConstructor(状态管理)](arkts-arkui-reusablecomponentconstructor-t.md) |
| [SetterCallback(状态管理)](arkts-arkui-settercallback-t.md) |
| [StorageDefaultCreator(状态管理)](arkts-arkui-storagedefaultcreator-t.md) |
| [TaskCallback(状态管理)](arkts-arkui-taskcallback-t.md) |
| [TypeDecorator(状态管理)](arkts-arkui-typedecorator-t.md) |
