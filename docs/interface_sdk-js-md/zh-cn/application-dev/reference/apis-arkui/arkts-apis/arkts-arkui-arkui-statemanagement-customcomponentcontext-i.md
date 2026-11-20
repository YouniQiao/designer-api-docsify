# CustomComponentContext

```TypeScript
export declare interface CustomComponentContext
```

`CustomComponentContext`类提供对组件级服务的访问，包括复用池。通过[UIUtils.getCustomComponentContext](arkts-arkui-arkui-statemanagement-uiutils-c.md#getcustomcomponentcontext)获取实例。

**起始版本：** 26.0.0

<!--Device-unnamed-export declare interface CustomComponentContext--><!--Device-unnamed-export declare interface CustomComponentContext-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
import { AppStorageV2, PersistenceV2, Type, UIUtils, ConnectOptions, Binding, MutableBinding, CustomComponentLifecycle, CustomComponentLifecycleObserver, CustomComponentLifecycleState, ComponentInit, ComponentAppear, ComponentBuilt, ComponentReuse, ComponentActive, ComponentInactive, ComponentRecycle, ComponentDisappear, CollectionType, ConnectOptionsCollections, CustomComponentContext, IReusePool, IDefaultReusePool, IReusableInfo, StorageDefaultCreator, TypeConstructorWithArgs, PersistenceErrorCallback, TypeConstructor, TypeDecorator, MonitorCallback, MonitorOptions, GetterCallback, SetterCallback, ObservedResult, DecoratorInfo, ElementInfo, RecoverableStorage, RecoverableConnectOptions, RecoverableStorageError, NotifyOnErrorCallback } from '@kit.ArkUI';
```

## enableAsyncLoad

```TypeScript
enableAsyncLoad(options?: CustomComponentAsyncLoadOptions): void
```

将当前自定义组件置为异步加载。组件实际内容由框架在异步任务中加载，不再阻塞页面转场主线程。

当开发者需要在页面转场等对帧率敏感的场景下，避免自定义组件同步加载导致丢帧卡顿时，使用本方法。调用成功后，该自定义组件进入由组件上下文管理的异步加载状态。加载未完成期间，显示已注册的占位组件（已配置且可找到时）或不显示；加载完成后，占位组件自动替换为实际内容，并由框架自动触发渲染更新。

与[IReusePool.preRender()](arkts-arkui-arkui-statemanagement-ireusepool-i.md#prerender)（预渲染可复用组件实例）不同，本方法延后的是组件实例的加载时机；本方法为配置型接口，返回**void**。

> **说明：** 
> 
> 1、本方法仅对当前自定义组件实例生效；未调用本方法的组件保持既有同步加载行为。
> 2、占位模板须先通过
> getPlaceholderRegister()注册，且builder须为全局
> 无参**\@Builder({ isPlaceholder: true })** 函数。
> 3、**timeout**取值（正数、**0**、负数）的语义请参考
> [CustomComponentAsyncLoadOptions.timeout](arkts-arkui-arkui-statemanagement-customcomponentasyncloadoptions-i.md#timeout)。
> 4、本期不处理异步加载失败场景，由超时强制加载机制兜底。

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-CustomComponentContext-enableAsyncLoad(options?: CustomComponentAsyncLoadOptions): void--><!--Device-CustomComponentContext-enableAsyncLoad(options?: CustomComponentAsyncLoadOptions): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [CustomComponentAsyncLoadOptions](arkts-arkui-arkui-statemanagement-customcomponentasyncloadoptions-i.md) | 否 | 异步加载配置。默认值**undefined**表示加载完成前不显示占位组件，并使用缺省超时阈值（**1000** ms）。 |

## getDefaultReusePool

```TypeScript
getDefaultReusePool(): IDefaultReusePool | undefined
```

返回该自定义组件拥有的默认复用池。

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-CustomComponentContext-getDefaultReusePool(): IDefaultReusePool | undefined--><!--Device-CustomComponentContext-getDefaultReusePool(): IDefaultReusePool | undefined-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IDefaultReusePool](arkts-arkui-arkui-statemanagement-idefaultreusepool-i.md) &#124; undefined | 当前组件存在默认复用池时，返回默认复用池，否则返回`undefined`。 |

**示例**

以下示例中，点击Recycle child按钮可将自定义组件回收进默认复用池，点击Clear按钮可释放默认复用池中的组件。

```TypeScript
import { UIUtils } from '@kit.ArkUI';

@ReusableV2
@ComponentV2
struct ReusableChild {
  @Param label: string = '';
  aboutToAppear() {
    console.info(`ReusableChild [${this.label}] aboutToAppear`);
  }
  aboutToDisappear() {
    console.info(`ReusableChild [${this.label}] aboutToDisappear`);
  }
  aboutToRecycle() {
    console.info(`ReusableChild [${this.label}] aboutToRecycle`);
  }
  aboutToReuse() {
    console.info(`ReusableChild [${this.label}] aboutToReuse`);
  }

  build() {
    Text(`ReusableChild: ${this.label}`)
  }
}

@Entry
@ComponentV2
struct Index {
  @Local showChild: boolean = true;

  clearDefaultPool() {
    // 获取当前组件的默认复用池
    const pool = UIUtils.getCustomComponentContext(this).getDefaultReusePool?.();
    if (!pool) {
      console.info('No default reuse pool available.');
      return;
    }
    // 清理默认复用池中的全部组件
    pool.clearCache();
    // 也可以仅清理reuseId为'A'的组件
    // pool.clearCache('A');
  }

  build() {
    Column() {
      if (this.showChild) {
        ReusableChild({ label: 'A' })
          .reuse({ reuseId: () => 'A' })
      }
      Button('Recycle child')
        .onClick(() => {
          // 切换if分支，触发子组件回收
          this.showChild = false;
        })
      Button('Clear')
        .onClick(() => {
          // 主动清理复用池
          this.clearDefaultPool();
        })
    }
  }
}
```

## getReusePool

```TypeScript
getReusePool(): IReusePool | undefined
```

返回该自定义组件拥有的全局复用池。如果组件或其上层组件没有通过`reusePool`和`poolAccepts`配置全局复用池，则返回`undefined`。配置全局复用池方式请参考[全局复用开发指南](../../../ui/state-management/arkts-global-reuse-pool.md)。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务中使用。

<!--Device-CustomComponentContext-getReusePool(): IReusePool | undefined--><!--Device-CustomComponentContext-getReusePool(): IReusePool | undefined-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IReusePool](arkts-arkui-arkui-statemanagement-ireusepool-i.md) &#124; undefined | 当前组件配置全局复用池时，返回复用池信息，否则返回`undefined`。 |

**示例**

```TypeScript
import { UIUtils } from '@kit.ArkUI';

@ReusableV2
@ComponentV2
struct ReusableChild {
  build() {
    Text('ReusableChild')
  }
}

@Entry
@ComponentV2({ reusePool: 'perInstance', poolAccepts: [ReusableChild], freezeWhenInactive: false })
struct PoolOwner {
  checkPool() {
    const pool = UIUtils.getCustomComponentContext(this).getReusePool();
    if (pool) {
      console.info('Global reuse pool configured.');
    } else {
      console.info('No global reuse pool configured.');
    }
  }

  build() {
    Column() {
      ReusableChild()
      Button('Check Pool')
        .onClick(() => {
          this.checkPool();
        })
    }
  }
}
```
