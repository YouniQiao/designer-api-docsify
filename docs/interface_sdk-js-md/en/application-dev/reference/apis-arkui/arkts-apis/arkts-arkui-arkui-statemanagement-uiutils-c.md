# UIUtils

UIUtils状态管理相关的工具方法，包括获取代理对象的原始对象、将非观察数据变为可观察数据、动态添加和删除状态变量监听、同步刷新状态变量修改、创建数据绑定等，适用于需要手动管理状态观察、监听和同步刷新的场景。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-export declare class UIUtils--><!--Device-unnamed-export declare class UIUtils-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { Binding, ComponentReuse, CustomComponentLifecycleState, ComponentInactive, PersistenceV2, ComponentDisappear, MutableBinding, CustomComponentLifecycleObserver, AppStorageV2, Type, ConnectOptionsCollections, CollectionType, CustomComponentContext, IReusePool, ConnectOptions, UIUtils, ComponentActive, CustomComponentLifecycle, ComponentInit, ComponentAppear, ComponentBuilt, ComponentRecycle, IReusableInfo } from 'kits/@kit.ArkUI';
```

## addMonitor

```TypeScript
static addMonitor(target: object, path: string | string[], monitorCallback: MonitorCallback, options?: MonitorOptions): void
```

给状态管理V2的状态变量动态添加监听方法，详见  
[addMonitor/clearMonitor](../../../ui/state-management/arkts-new-addMonitor-clearMonitor.md)。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-UIUtils-static addMonitor(target: object, path: string | string[], monitorCallback: MonitorCallback, options?: MonitorOptions): void--><!--Device-UIUtils-static addMonitor(target: object, path: string | string[], monitorCallback: MonitorCallback, options?: MonitorOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| target | object | Yes | 目标对象，仅支持 [@ComponentV2](../../../ui/state-management/arkts-create-custom-components.md#componentv2)和 [@ObservedV2](../../../ui/state-management/arkts-new-observedV2-and-trace.md)实例。 &lt;br&gt;对于不支持的类型，会抛出运行时错误，错误码见表格。 |
| path | string \| string[] | Yes | 添加监听的变量名路径。可指定一个路径或者传入string数组用于一次性指定多个监听的变量路径。 &lt;br&gt;仅支持string和string数组，对于不支持的类型，会抛出运行时错误，错误码见表格。 |
| monitorCallback | [MonitorCallback](arkts-arkui-monitorcallback-t.md) | Yes | 给对应的状态变量注册的监听函数，即path路径对应的状态变量改变时，会回调对应的函数。 &lt;br&gt;对于不支持的类型，会抛出运行时错误，错误码见表格。 |
| options | [MonitorOptions](arkts-arkui-arkui-statemanagement-monitoroptions-i.md) | No | 监听函数的配置项，具体可见[MonitorOptions](arkts-arkui-arkui-statemanagement-monitoroptions-i.md)。默认为异步回调。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 130001 | The path is invalid. |
| 130000 | The target is not a custom component instance or V2 class instance. |
| 130002 | monitorCallback is not a function or an anonymous function. |

## applySync

```TypeScript
static applySync<T>(task: TaskCallback): T
```

同步刷新指定的状态变量，该接口接收一个闭包函数，仅刷新闭包函数内的修改，包括更新[@Computed计算](../../../ui/state-management/arkts-new-computed.md)、  
[@Monitor回调](../../../ui/state-management/arkts-new-monitor.md)以及重新渲染UI节点，详见  
[applySync/flushUpdates/flushUIUpdates接口：同步刷新](../../../ui/state-management/arkts-new-applySync-flushUpdates-flushUIUpdates.md)。

**Since:** 22

**ArkTS mode:** ArkTS-Dyn only, since version 22.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-UIUtils-static applySync<T>(task: TaskCallback): T--><!--Device-UIUtils-static applySync<T>(task: TaskCallback): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| task | [TaskCallback](arkts-arkui-taskcallback-t.md) | Yes | 闭包函数，该闭包中产生的状态变量修改会同步执行。 |

**Return value:**

| Type | Description |
| --- | --- |
| T | 闭包函数执行得到的返回值。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 140001 | The function is not allowed to be called in @Computed |

## Examples

```TypeScript
import { UIUtils } from '@kit.ArkUI';

@Entry
@ComponentV2
struct Index {
  @Local columnWidth: number = 50; // Width
  @Local columnHeight: number = 50; // Height
  @Local message: string = 'Hello';

  build() {
    Column() {
      Button('change size')
        .margin(20)
        .onClick(() => {
          // Values are changed additionally before the animation is executed.
          UIUtils.applySync(() => {
            this.columnWidth = 100;
            this.columnHeight = 100;
            this.message = 'Hello World';
          });
          // The size of the column box gradually changes from (100 × 100) to (200 × 200) within 1s, and the text in the box changes to "Hello ArkUI".
          this.getUIContext().animateTo({
            duration: 1000
          }, () => {
            console.info(`animateTo-in, width=${this.columnWidth}, height=${this.columnHeight}`);
            this.columnWidth = 200;
            this.columnHeight = 200;
            this.message = 'Hello ArkUI';
            console.info(`animateTo-out, width=${this.columnWidth}, height=${this.columnHeight}`);
          });
        })
      // Column box.
      Column() {
        Text(`${this.message}`)
      }
      .backgroundColor('#ff17a98d')
      .width(this.columnWidth)
      .height(this.columnHeight)
    }
  }
}
```

## canBeObserved

```TypeScript
static canBeObserved<T extends object>(source: T): ObservedResult
```

判断数据对象是否为可观察对象，并返回观察结果。详见[canBeObserved接口：判断对象是否为可被观察对象](../../../ui/state-management/arkts-new-canBeObserved.md)。

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-UIUtils-static canBeObserved<T extends object>(source: T): ObservedResult--><!--Device-UIUtils-static canBeObserved<T extends object>(source: T): ObservedResult-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| source | T | Yes | 输入一个数据对象，判断其是否可被观察。支持Array、Map、Set和Date类型数据。 &lt;br&gt;具体使用规则，详见[canBeObserved接口：判断对象是否为可被观察对象](../../../ui/state-management/arkts-new-canBeObserved.md)。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ObservedResult](arkts-arkui-arkui-statemanagement-observedresult-i.md) | 返回对象是否可被观察的结果。 |

## Examples

```TypeScript
import { UIUtils } from '@kit.ArkUI';
import { DecoratorInfo, ElementInfo } from '@ohos.arkui.StateManagement';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = 'CanBeObserved';

class Student {
  public name?: string;

  constructor(name?: string) {
    this.name = name ?? '';
  }

  // Provide a method in the object to determine whether the object can be observed.
  test(): void {
    const result = UIUtils.canBeObserved(this);
    // Whether the object can be observed.
    const isObserved = result.isObserved;
    hilog.info(0x00, TAG, `isObserved: ${JSON.stringify(isObserved)}`);
    // Reason for the object's observability.
    const reason = result.reason;
    hilog.info(0x00, TAG, `reason: ${reason}`);
    // Decorator information associated with the observable object.
    const decoratorInfoArr = result.decoratorInfo;
    decoratorInfoArr.forEach((decorator: DecoratorInfo) => {
      // Decorator name.
      const decoratorName = decorator.decoratorName;
      hilog.info(0x00, TAG, `decoratorName: ${decoratorName}`);
      // Name of the attribute decorated by the decorator.
      const stateVariableName = decorator.stateVariableName;
      hilog.info(0x00, TAG, `stateVariableName: ${stateVariableName}`);
      // Name of the component where the decorator is located.
      const owningName = decorator.owningComponentOrClassName;
      hilog.info(0x00, TAG, `owningComponentOrClassName: ${owningName}`);
      // ID of the component where the decorator is located.
      const owningId = decorator.owningComponentId;
      hilog.info(0x00, TAG, `owningComponentId: ${owningId}`);
      // Information about the component associated with the decorator.
      const dependentInfo = decorator.dependentInfo;
      dependentInfo.forEach((elementInfo: ElementInfo) => {
        // Name of the component associated with the decorator.
        const eleName = elementInfo.elementName;
        hilog.info(0x00, TAG, `elementName: ${eleName}`);
        // ID of the component associated with the decorator.
        const eleId = elementInfo.elementId;
        hilog.info(0x00, TAG, `elementId: ${eleId}`);
      });
    });
  }
}

@Entry
@Component
struct Index {
  @State student: Student = new Student('LiMei');

  build() {
    Column({ space: 20 }) {
      Classroom({ student: this.student })
      Home({ student: this.student })
      Button('test')
        .onClick(() => {
          // You can use this API on any page to determine whether the current object can be observed.
          this.student.test();
        })
    }
    .height('100%')
    .width('100%')
    .justifyContent(FlexAlign.Center)
    .alignItems(HorizontalAlign.Center)
  }
}

@Component
export struct Classroom {
  @State student: Student = new Student();

  build() {
    Column() {
      Text('Classroom ' + this.student.name)
      School({ student: this.student })
    }
  }
}

@Component
export struct Home {
  @State student: Student = new Student();

  build() {
    Column() {
      Text('Home ' + this.student.name)
    }
  }
}

@Component
export struct School {
  @State student: Student = new Student();

  build() {
    Column() {
      Text('School ' + this.student.name)
    }
  }
}
```

## clearMonitor

```TypeScript
static clearMonitor(target: object, path: string | string[], monitorCallback?: MonitorCallback) : void
```

删除通过[addMonitor](arkts-arkui-arkui-statemanagement-uiutils-c.md#addmonitor)给状态管理V2的状态变量添加的监听方法，详见  
[addMonitor/clearMonitor](../../../ui/state-management/arkts-new-addMonitor-clearMonitor.md)。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-UIUtils-static clearMonitor(target: object, path: string | string[], monitorCallback?: MonitorCallback) : void--><!--Device-UIUtils-static clearMonitor(target: object, path: string | string[], monitorCallback?: MonitorCallback) : void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| target | object | Yes | 目标对象，仅支持 [@ComponentV2](../../../ui/state-management/arkts-create-custom-components.md#componentv2)和 [@ObservedV2](../../../ui/state-management/arkts-new-observedV2-and-trace.md)实例。 &lt;br&gt;对于不支持的类型，会抛出运行时错误，错误码见表格。 |
| path | string \| string[] | Yes | 删除监听的变量名路径。可指定一个路径或者传入string数组用于一次性指定删除多个状态变量的监听函数。 &lt;br&gt;仅支持string和数组，对于不支持的类型，会抛出运行时错误，错误码见表格。 |
| monitorCallback | [MonitorCallback](arkts-arkui-monitorcallback-t.md) | No | 指定被删除的监听函数。 &lt;br&gt;当开发者不传此参数时，将删除path对应变量注册的所有监听函数。 &lt;br&gt;对于不支持的类型，会抛出运行时错误，错误码见表格。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 130001 | The path is invalid. |
| 130000 | The target is not a custom component instance or V2 class instance. |
| 130002 | monitorCallback is not a function or an anonymous function. |

## enableV2Compatibility

```TypeScript
static enableV2Compatibility<T extends object>(source: T): T
```

使V1的状态变量能够在\@ComponentV2中观察，主要应用于状态管理V1、V2混用场景。详见  
[状态管理V1和V2混用指导（API version 19及之后）](../../../ui/state-management/arkts-v1-v2-mixusage.md)。

**Since:** 19

**ArkTS mode:** ArkTS-Dyn only, since version 19.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-UIUtils-static enableV2Compatibility<T extends object>(source: T): T--><!--Device-UIUtils-static enableV2Compatibility<T extends object>(source: T): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| source | T | Yes | 数据源，仅支持V1状态数据，如被@Observed装饰的对象或被makeV1Observed方法转换的对象。传入非V1状态数据时返回数据源本身。 |

**Return value:**

| Type | Description |
| --- | --- |
| T | 如果数据源是V1的状态数据，则返回能够在 |

## Examples

```TypeScript
import { UIUtils } from '@kit.ArkUI';

@Observed
class ObservedClass {
  name: string = 'Tom';
}

@Entry
@Component
struct CompV1 {
  @State observedClass: ObservedClass = new ObservedClass();

  build() {
    Column() {
      Text(`@State observedClass: ${this.observedClass.name}`)
        .onClick(() => {
          this.observedClass.name = 'State'; // This will trigger a UI update.
        })
      // Enable the V2 observation capability for the V1 state variable.
      CompV2({ observedClass: UIUtils.enableV2Compatibility(this.observedClass) })
    }
  }
}

@ComponentV2
struct CompV2 {
  @Param observedClass: ObservedClass = new ObservedClass();

  build() {
    // After the V2 observation capability is enabled for the V1 state variable, the first-level changes can be observed in V2.
    Text(`@Param observedClass: ${this.observedClass.name}`)
      .onClick(() => {
        this.observedClass.name = 'Param'; // This will trigger a UI update.
      })
  }
}
```

## flushUIUpdates

```TypeScript
static flushUIUpdates(): void
```

立即处理在调用该函数之前所有的状态变量修改，同步[标脏](../../../ui/state-management/arkts-state-management-introduce.md#触发更新)对应的UI节点，但不会同步执行

**Since:** 22

**ArkTS mode:** ArkTS-Dyn only, since version 22.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-UIUtils-static flushUIUpdates(): void--><!--Device-UIUtils-static flushUIUpdates(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 140002 | The function is not allowed to be called in @Monitor |
| 140001 | The function is not allowed to be called in @Computed |

## Examples

```TypeScript
import { UIUtils } from '@kit.ArkUI';

@Entry
@ComponentV2
struct Index {
  @Local columnWidth: number = 50; // Width
  @Local columnHeight: number = 50; // Height
  @Local message: string = 'Hello';

  build() {
    Column() {
      Button('change size')
        .margin(20)
        .onClick(() => {
          // Values are changed additionally before the animation is executed.
          this.columnWidth = 100;
          this.columnHeight = 100;
          this.message = 'Hello World';
          // Immediately process the preceding state variable modifications and synchronize the dirty UI nodes.
          UIUtils.flushUIUpdates();
          // The size of the column box gradually changes from (100 × 100) to (200 × 200) within 1s, and the text in the box changes to "Hello ArkUI".
          this.getUIContext().animateTo({
            duration: 1000
          }, () => {
            console.info(`animateTo-in, width=${this.columnWidth}, height=${this.columnHeight}`);
            this.columnWidth = 200;
            this.columnHeight = 200;
            this.message = 'Hello ArkUI';
            console.info(`animateTo-out, width=${this.columnWidth}, height=${this.columnHeight}`);
          });
        })
      // Column box.
      Column() {
        Text(`${this.message}`)
      }
      .backgroundColor('#ff17a98d')
      .width(this.columnWidth)
      .height(this.columnHeight)
    }
  }
}
```

## flushUpdates

```TypeScript
static flushUpdates(): void
```

同步刷新在调用该函数之前所有的状态变量修改，包括更新@Computed计算、@Monitor回调以及重新渲染UI节点，详见  
[applySync/flushUpdates/flushUIUpdates接口：同步刷新](../../../ui/state-management/arkts-new-applySync-flushUpdates-flushUIUpdates.md)。

**Since:** 22

**ArkTS mode:** ArkTS-Dyn only, since version 22.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-UIUtils-static flushUpdates(): void--><!--Device-UIUtils-static flushUpdates(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 140002 | The function is not allowed to be called in @Monitor |
| 140001 | The function is not allowed to be called in @Computed |

## Examples

```TypeScript
import { UIUtils } from '@kit.ArkUI';

@Entry
@ComponentV2
struct Index {
  @Local columnWidth: number = 50; // Width
  @Local columnHeight: number = 50; // Height
  @Local message: string = 'Hello';

  build() {
    Column() {
      Button('change size')
        .margin(20)
        .onClick(() => {
          // Values are changed additionally before the animation is executed.
          this.columnWidth = 100;
          this.columnHeight = 100;
          this.message = 'Hello World';
          UIUtils.flushUpdates();
          // The size of the column box gradually changes from (100 × 100) to (200 × 200) within 1s, and the text in the box changes to "Hello ArkUI".
          this.getUIContext().animateTo({
            duration: 1000
          }, () => {
            console.info(`animateTo-in, width=${this.columnWidth}, height=${this.columnHeight}`);
            this.columnWidth = 200;
            this.columnHeight = 200;
            this.message = 'Hello ArkUI';
            console.info(`animateTo-out, width=${this.columnWidth}, height=${this.columnHeight}`);
          });
        })
      // Column box.
      Column() {
        Text(`${this.message}`)
      }
      .backgroundColor('#ff17a98d')
      .width(this.columnWidth)
      .height(this.columnHeight)
    }
  }
}
```

## getCustomComponentContext

```TypeScript
static getCustomComponentContext<T extends BaseCustomComponent>(customComponent: T): CustomComponentContext
```

返回给定@Component(V1)或@ComponentV2的[CustomComponentContext](arkts-arkui-arkui-statemanagement-customcomponentcontext-i.md)。使用它来访问组件的复用池。有关复用池的详细信息，请参阅  
[全局复用池：集中化的组件回收与复用](../../../ui/state-management/arkts-global-reuse-pool.md)。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-UIUtils-static getCustomComponentContext<T extends BaseCustomComponent>(customComponent: T): CustomComponentContext--><!--Device-UIUtils-static getCustomComponentContext<T extends BaseCustomComponent>(customComponent: T): CustomComponentContext-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| customComponent | T | Yes | 要获取其上下文的@Component或@ComponentV2实例。 |

**Return value:**

| Type | Description |
| --- | --- |
| [CustomComponentContext](arkts-arkui-utils-customcomponentcontext-i.md) | 给定组件实例的上下文对象。 |

## Examples

```TypeScript
import { UIUtils } from '@kit.ArkUI';

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
@ComponentV2({ 
  reusePool: 'shared', // Declare the shared global reuse pool.
  poolAccepts: [ReusableChild], // The global reuse pool accepts the child component type ReusableChild.
  freezeWhenInactive: false // Disable the component freezing feature. This parameter must be provided when reusePools is declared. You can also enable the component freezing feature.
})
struct Index {
  @Local showChild: boolean = true;

  inspectPool() {
    // Obtain CustomComponentContext of this component.
    const context = UIUtils.getCustomComponentContext(this);
    // Access the reuse pool through the context.
    const pool = context.getReusePool();
    if (pool) {
      const info = pool.getReusableInfo(ReusableChild);
      if (info && !Array.isArray(info)) {
        console.info(`ReusableChild in the pool: count=${info.count}, maxCount=${info.maxCount}`);
      }
    }
  }

  build() {
    Column() {
      Button('Switch Child Component')
        .onClick(() => { 
          this.showChild = !this.showChild;
        })
      Button('Check Pool')
        .onClick(() => {
          this.inspectPool();
        })
      if (this.showChild) {
        ReusableChild()
      }
    }
  }
}
```

## getLifecycle

```TypeScript
static getLifecycle<T extends BaseCustomComponent>(customComponent: T): CustomComponentLifecycle
```

getLifecycle用于获取[自定义组件的生命周期](arkts-arkui-statemanagement.md)实例。

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-UIUtils-static getLifecycle<T extends BaseCustomComponent>(customComponent: T): CustomComponentLifecycle--><!--Device-UIUtils-static getLifecycle<T extends BaseCustomComponent>(customComponent: T): CustomComponentLifecycle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| customComponent | T | Yes | 自定义组件实例。 |

**Return value:**

| Type | Description |
| --- | --- |
| [CustomComponentLifecycle](arkts-arkui-customcomponent-customcomponentlifecycle-i.md) | 自定义组件的生命周期实例。 |

## Examples

```TypeScript
import { UIUtils, ComponentAppear } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State lifecycleState: number = -1;

  @ComponentAppear
  myAppear() {
    // Obtain the lifecycle instance of a custom component through UIUtils.getLifecycle, and query the current lifecycle of the custom component through getCurrentState.
    // The expected lifecycle is CustomComponentLifecycleState.APPEARED = 1.
    this.lifecycleState = UIUtils.getLifecycle(this).getCurrentState();
  }

  build() {
    Text(`${this.lifecycleState}`)
  }
}
```

## getTarget

```TypeScript
static getTarget<T extends object>(source: T): T
```

从状态管理框架包裹的代理对象中获取原始对象。详见[getTarget接口：获取状态管理框架代理前的原始对象](../../../ui/state-management/arkts-new-getTarget.md)。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-UIUtils-static getTarget<T extends object>(source: T): T--><!--Device-UIUtils-static getTarget<T extends object>(source: T): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| source | T | Yes | 数据源对象，即被状态管理框架包裹的代理对象，用于获取去除代理后的原始对象。 |

**Return value:**

| Type | Description |
| --- | --- |
| T | 数据源对象去除状态管理框架所加代理后的原始对象。 |

## Examples

```TypeScript
import { UIUtils } from '@kit.ArkUI';

class NonObservedClass {
  name: string = 'Tom';
}

let nonObservedClass: NonObservedClass = new NonObservedClass();

@Entry
@Component
struct Index {
  @State someClass: NonObservedClass = nonObservedClass;

  build() {
    Column() {
      Text(`this.someClass === nonObservedClass: ${this.someClass === nonObservedClass}`) // false
      Text(`UIUtils.getTarget(this.someClass) === nonObservedClass: ${UIUtils.getTarget(this.someClass) ===
        nonObservedClass}`) // true
    }
  }
}
```

## makeBinding

```TypeScript
static makeBinding<T>(getter: GetterCallback<T>): Binding<T>
```

创建只读的单向数据绑定实例，用于构建[\@Builder](../../../ui/state-management/arkts-builder.md)函数中参数类型为`Binding`的对应实参。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-UIUtils-static makeBinding<T>(getter: GetterCallback<T>): Binding<T>--><!--Device-UIUtils-static makeBinding<T>(getter: GetterCallback<T>): Binding<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| getter | [GetterCallback](arkts-arkui-gettercallback-t.md)&lt;T&gt; | Yes | 获取值的回调函数，每次访问值都会重新执行函数，获取最新值。 |

**Return value:**

| Type | Description |
| --- | --- |
| [Binding](arkts-arkui-arkui-statemanagement-binding-c.md)&lt;T&gt; | 仅包含一个`value`属性，用于获取当前绑定的值。只能读取值，不能直接修改。 |

## Examples

```TypeScript
import { Binding, UIUtils } from '@kit.ArkUI';

@Builder
function CustomButton(num1: Binding<number>) {
  Row() {
    Button(`Custom Button: ${num1.value}`)
      .onClick(() => {
        // num1.value += 1; will throw an error because the Binding element does not support modification.
      })
  }
}

@Entry
@ComponentV2
struct CompV2 {
  @Local number1: number = 5;

  build() {
    Column() {
      Text('parent component')

      CustomButton(
        /**
         * Creates a read-only binding instance.
         * @param getter - Function for returning this.number1.
         * @returns Read-only Binding<number> object.
         *
         * Features:
         * 1. The value is recalculated each time .value is accessed.
         * 2. The value cannot be directly modified.
         */
        UIUtils.makeBinding<number>(
          () => this.number1 // GetterCallback
        )
      )
    }
  }
}
```

## makeBinding

```TypeScript
static makeBinding<T>(getter: GetterCallback<T>, setter: SetterCallback<T>): MutableBinding<T>
```

创建可修改的双向数据绑定实例，用于构建\@Builder函数中参数类型为`MutableBinding`的对应实参。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-UIUtils-static makeBinding<T>(getter: GetterCallback<T>, setter: SetterCallback<T>): MutableBinding<T>--><!--Device-UIUtils-static makeBinding<T>(getter: GetterCallback<T>, setter: SetterCallback<T>): MutableBinding<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| getter | [GetterCallback](arkts-arkui-gettercallback-t.md)&lt;T&gt; | Yes | 获取值的回调函数，每次访问值都会重新执行函数，获取最新值。 |
| setter | [SetterCallback](arkts-arkui-settercallback-t.md)&lt;T&gt; | Yes | 定义如何更新值，当`.value`被修改时自动调用此函数。 |

**Return value:**

| Type | Description |
| --- | --- |
| [MutableBinding](arkts-arkui-utils-mutablebinding-c.md)&lt;T&gt; | 包含一个`value`属性，支持通过`.value`读取和修改数据，设置值时会检查类型是否匹配泛型`T`。 |

## Examples

```TypeScript
import { MutableBinding, UIUtils } from '@kit.ArkUI';

@Builder
function CustomButton(num1: MutableBinding<number>) {
  Row() {
    Button(`Custom Button: ${num1.value}`)
      .onClick(() => {
        // MutableBinding type, which can be modified.
        num1.value += 1;
      })
  }
}

@Entry
@ComponentV2
struct CompV2 {
  @Local number1: number = 10;

  build() {
    Column() {
      Text('parent component')

      CustomButton(
        /**
         * Creates a mutable binding.
         * @param getter - Function that returns this.number1
         * @param setter - Callback called when the binding value is modified.
         * @returns A mutable MutableBinding<number> object.
         *
         * Features:
         * 1. Read and write operations are supported.
         * 2. The setter callback is automatically called when .value is modified.
         */
        UIUtils.makeBinding<number>(
          () => this.number1, // GetterCallback
          (val: number) => {
            this.number1 = val;
          }) // SetterCallback
      )
    }
  }
}
```

## makeObserved

```TypeScript
static makeObserved<T extends object>(source: T): T
```

将普通不可观察数据变为可观察数据。详见[makeObserved接口：将非观察数据变为可观察数据](../../../ui/state-management/arkts-new-makeObserved.md)。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-UIUtils-static makeObserved<T extends object>(source: T): T--><!--Device-UIUtils-static makeObserved<T extends object>(source: T): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| source | T | Yes | 数据源对象。支持非@Observed和@ObservedV2装饰的class，JSON.parse返回的Object和@Sendable修饰的class。 &lt;br&gt;支持Array、Map、Set和Date。 &lt;br&gt;支持collections.Array、collections.Set和collections.Map。 &lt;br&gt;具体使用规则，详见[makeObserved接口：将非观察数据变为可观察数据](../../../ui/state-management/arkts-new-makeObserved.md)。 |

**Return value:**

| Type | Description |
| --- | --- |
| T | 对于支持的入参类型，返回可观察的数据。对于不支持的入参类型，返回数据源对象本身。 |

## Examples

```TypeScript
import { UIUtils } from '@kit.ArkUI';

class NonObservedClass {
  name: string = 'Tom';
}

@Entry
@ComponentV2
struct Index {
  // Use makeObserved to make the NonObservedClass instance observable.
  observedClass: NonObservedClass = UIUtils.makeObserved(new NonObservedClass());
  nonObservedClass: NonObservedClass = new NonObservedClass();

  build() {
    Column() {
      Text(`observedClass: ${this.observedClass.name}`)
        .onClick(() => {
          this.observedClass.name = 'Jane'; // This will trigger a UI update.
        })
      Text(`nonObservedClass: ${this.nonObservedClass.name}`)
        .onClick(() => {
          this.nonObservedClass.name = 'Jane'; // This will not trigger a UI update.
        })
    }
  }
}
```

## makeV1Observed

```TypeScript
static makeV1Observed<T extends object>(source: T): T
```

将不可观察的对象包装成状态管理V1可观察的对象，其能力等同于@Observed，可初始化@ObjectLink。

该接口可搭配[enableV2Compatibility](arkts-arkui-arkui-statemanagement-uiutils-c.md#enablev2compatibility)应用于状态管理V1和V2混用场景，详见  
[状态管理V1和V2混用指导（API version 19及之后）](../../../ui/state-management/arkts-v1-v2-mixusage.md)。

**Since:** 19

**ArkTS mode:** ArkTS-Dyn only, since version 19.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-UIUtils-static makeV1Observed<T extends object>(source: T): T--><!--Device-UIUtils-static makeV1Observed<T extends object>(source: T): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| source | T | Yes | 数据源。支持普通class、Array、Map、Set、Date类型。 &lt;br&gt;不支持[@arkts.collections (ArkTS容器集)](../../apis-arkts/arkts-apis/arkts-collections.md/arkts-collections.md)和 [@Sendable](../../../arkts-utils/arkts-sendable.md)修饰的class。 &lt;br&gt;不支持undefined和null。不支持状态管理V2的数据和[makeObserved](arkts-arkui-arkui-statemanagement-uiutils-c.md#makeobserved)的返回值。 |

**Return value:**

| Type | Description |
| --- | --- |
| T | 对于支持的入参类型，返回状态管理V1的观察数据。对于不支持的入参类型，返回数据源对象本身。 |

## Examples

```TypeScript
import { UIUtils } from '@kit.ArkUI';

class Outer {
  outerValue: string = 'outer';
  inner: Inner;

  constructor(inner: Inner) {
    this.inner = inner;
  }
}

class Inner {
  interValue: string = 'inner';
}

@Entry
@Component
struct Index {
  // Use makeV1Observed to wrap the Inner instance as a V1 observable object and pass it to the Outer constructor.
  @State outer: Outer = new Outer(UIUtils.makeV1Observed(new Inner()));

  build() {
    Column() {
      // The return value of makeV1Observed can be used to initialize @ObjectLink.
      Child({ inner: this.outer.inner })
    }
    .height('100%')
    .width('100%')
  }
}

@Component
struct Child {
  @ObjectLink inner: Inner;

  build() {
    Text(`${this.inner.interValue}`)
      .onClick(() => {
        this.inner.interValue += '!';
      })
  }
}
```

