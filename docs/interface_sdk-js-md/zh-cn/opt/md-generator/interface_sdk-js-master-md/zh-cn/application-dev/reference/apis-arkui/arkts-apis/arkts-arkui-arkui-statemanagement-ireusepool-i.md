# IReusePool

`IReusePool`接口提供自定义组件上的全局复用池的相关功能，包括查询回收组件的当前数量和上限信息、预渲染可复用组件到复用池中等，适用于开发者需要手动管理和优化组件复用效率的场景。

**起始版本：** 26.0.0

**废弃版本：** -1

<!--Device-unnamed-export declare interface IReusePool--><!--Device-unnamed-export declare interface IReusePool-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## getReusableInfo

```TypeScript
getReusableInfo(constructor: ReusableComponentConstructor,
    reuseId?: string): IReusableInfo[] | IReusableInfo | undefined
```

检索此复用池中给定可复用组件类型的回收实例信息。

**起始版本：** 26.0.0

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-IReusePool-getReusableInfo(constructor: ReusableComponentConstructor,    reuseId?: string): IReusableInfo[] | IReusableInfo | undefined--><!--Device-IReusePool-getReusableInfo(constructor: ReusableComponentConstructor,    reuseId?: string): IReusableInfo[] | IReusableInfo | undefined-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| constructor | [ReusableComponentConstructor](arkts-arkui-reusablecomponentconstructor-t.md) | 是 |
| reuseId | string | 否 |

**返回值：**

| 类型 |
| --- |
| [IReusableInfo](arkts-arkui-arkui-statemanagement-ireusableinfo-i.md)[] |

## 示例

```TypeScript
import { UIUtils, IReusableInfo } from '@kit.ArkUI';

@ReusableV2
@ComponentV2
struct ReusableChild {
  aboutToRecycle() {
    console.info('ReusableChild aboutToRecycle');
  }
  aboutToReuse() {
    console.info('ReusableChild aboutToReuse');
  }

  build() {
    Text('ReusableChild')
  }
}

@Entry
@ComponentV2({ reusePool: 'perInstance', poolAccepts: [ReusableChild], freezeWhenInactive: false })
struct PoolOwner {
  @Local showChild: boolean = true;

  inspectPool() {
    const pool = UIUtils.getCustomComponentContext(this).getReusePool();
    if (!pool) {
      return;
    }

    // 查询池接受的组件类型。
    const info = pool.getReusableInfo(ReusableChild);
    if (info === undefined) {
      console.info('No reuse pool that accepts ReusableChild');
    } else if (Array.isArray(info)) {
      // 使用了多个 reuseId 桶。
      info.forEach((item: IReusableInfo, i: number) => {
        console.info(`[${i}] reuseId=${item.reuseId}, count=${item.count}, maxCount=${item.maxCount}`);
      });
    } else {
      // 单个条目（未使用 reuseId，或查询了特定的 reuseId）。
      console.info(`count=${info.count}, maxCount=${info.maxCount}`);
    }

    // 查询特定的 reuseId — 始终返回单个 IReusableInfo。
    const bucketInfo = pool.getReusableInfo(ReusableChild, 'A') as IReusableInfo;
    console.info(`reuseId 'A': count=${bucketInfo.count}, maxCount=${bucketInfo.maxCount}`);
  }

  build() {
    Column() {
      Button('切换子组件')
        .onClick(() => {
          this.showChild = !this.showChild;
        })
      Button('检查池')
        .onClick(() => this.inspectPool())
      if (this.showChild) {
        ReusableChild()
          .reuse({ reuseId: () => 'A' })
      }
    }
  }
}
```

## preRender

```TypeScript
preRender(builder: WrappedBuilder<[]>, times: number): Promise<void>
```

调用空闲任务以预创建可复用组件并在首次使用前将其放入复用池。 > **说明：** > > 1. `preRender`仅将池配置为接受的组件放入池中。预渲染池不接受的组件会立即创建并销毁。 > > 2. 预渲染期间不会从池中复用组件；池仅接受新创建的实例。 > > 3. @Builder函数执行完整的深度渲染，包括嵌套的子组件。

**起始版本：** 26.0.0

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-IReusePool-preRender(builder: WrappedBuilder<[]>, times: number): Promise<void>--><!--Device-IReusePool-preRender(builder: WrappedBuilder<[]>, times: number): Promise<void>-End-->

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

## 示例

```TypeScript
import { UIUtils, IReusableInfo } from '@kit.ArkUI';

@ReusableV2
@ComponentV2
struct ReusableComponent {
  @Param param: number = 8;

  aboutToAppear() {
    console.info('ReusableComponent aboutToAppear');
  }
  aboutToReuse() {
    console.info('ReusableComponent aboutToReuse');
  }

  build() {
    Column() {
      Text(`ReusableComponent ${this.param}`)
    }
  }
}

@Builder 
function preRenderBuilder() {
  ReusableComponent()
}

@Entry
@ComponentV2({ reusePool: 'shared', poolAccepts: [ReusableComponent], freezeWhenInactive: false })
struct Index {
  @Local onUIFullyLoaded: boolean = false;

  aboutToAppear() {
    // 获取池并调度预渲染。
    const pool = UIUtils.getCustomComponentContext(this).getReusePool();
    // 预加载preRenderBuilder内的复用组件到当前的全局复用池中，执行一次preRenderBuilder。
    pool!.preRender(new WrappedBuilder<[]>(preRenderBuilder), 1)
      .then(() => {
        console.info('ReusableComponent preRender completes');
      });
  }

  checkPool() {
    // 获取全局复用池内组件数量
    const reusePool = UIUtils.getCustomComponentContext(this).getReusePool();
    const reusableInfo: IReusableInfo = reusePool!.getReusableInfo(ReusableComponent) as IReusableInfo;
    console.info(`ReusableComponent reuse pool count=${reusableInfo.count}`);
  }

  build() {
    Column({ space: 5 }) {
      Button('Switch')
        .onClick(() => {
          this.onUIFullyLoaded = !this.onUIFullyLoaded;
        })
        .width(100)
      Button('Check pool')
        .onClick(() => {
          this.checkPool();
        })
        .width(100)
      CompA({ showFullUI: this.onUIFullyLoaded })
    }
    .width('100%')
  }
}

@ComponentV2
struct CompA {
  @Require @Param showFullUI: boolean;

  build() {
    if (this.showFullUI) {
      // 这将从池中复用预渲染的实例。
      ReusableComponent()
    }
  }
}
```
