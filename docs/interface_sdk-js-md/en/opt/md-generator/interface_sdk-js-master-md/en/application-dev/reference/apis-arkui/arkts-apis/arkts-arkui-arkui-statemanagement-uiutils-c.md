# UIUtils

Provides APIs for handling data transformations related to state management.

**Since:** 12

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

Dynamically adds a listener to the state variable of state management V2. For details, see  
[addMonitor and clearMonitor APIs: Dynamically Adding and Removing Listeners](../../../ui/state-management/arkts-new-addMonitor-clearMonitor.md).

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-UIUtils-static addMonitor(target: object, path: string | string[], monitorCallback: MonitorCallback, options?: MonitorOptions): void--><!--Device-UIUtils-static addMonitor(target: object, path: string | string[], monitorCallback: MonitorCallback, options?: MonitorOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| target | object | Yes |
| path | string \| string[] | Yes |
| monitorCallback | [MonitorCallback](arkts-arkui-monitorcallback-t.md) | Yes |
| options | [MonitorOptions](arkts-arkui-arkui-statemanagement-monitoroptions-i.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [130001](../errorcode-stateManagement.md#130001-invalid-path-for-addmonitorclearmonitor) |
| [130000](../errorcode-stateManagement.md#130000-invalid-target-object-for-addmonitorclearmonitor) |
| [130002](../errorcode-stateManagement.md#130002-invalid-callback-for-addmonitorclearmonitor) |

## applySync

```TypeScript
static applySync<T>(task: TaskCallback): T
```

Synchronously updates a specified state variable. This API receives a closure function and updates only the internal modifications, including the updates of [@Computed](../../../ui/state-management/arkts-new-computed.md)and [@Monitor](../../../ui/state-management/arkts-new-monitor.md) decorators, and re-rendering of the UI nodes.For details, see  
[applySync/flushUpdates/flushUIUpdates APIs: Synchronous Update](../../../ui/state-management/arkts-new-applySync-flushUpdates-flushUIUpdates.md).

**Since:** 22

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-UIUtils-static applySync<T>(task: TaskCallback): T--><!--Device-UIUtils-static applySync<T>(task: TaskCallback): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| task | [TaskCallback](arkts-arkui-taskcallback-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

**Error codes:**

| Error Code ID |
| --- |
| [140001](../errorcode-stateManagement.md#140001-invalid-invocation-of-applysync-flushupdates-or-flushuiupdates) |

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

Determines whether a data object can be observed and returns the observation result. For details, see  
[canBeObserved API: Determining Whether an Object Can Be Observed](../../../ui/state-management/arkts-new-canBeObserved.md).

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-UIUtils-static canBeObserved<T extends object>(source: T): ObservedResult--><!--Device-UIUtils-static canBeObserved<T extends object>(source: T): ObservedResult-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| source | T | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ObservedResult](arkts-arkui-arkui-statemanagement-observedresult-i.md) |

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

Deletes the listener added to the state variable of the state management V2 by calling the  
[addMonitor](arkts-arkui-arkui-statemanagement-uiutils-c.md#addmonitor) API. For details, see  
[addMonitor and clearMonitor APIs: Dynamically Adding and Removing Listeners](../../../ui/state-management/arkts-new-addMonitor-clearMonitor.md).

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-UIUtils-static clearMonitor(target: object, path: string | string[], monitorCallback?: MonitorCallback) : void--><!--Device-UIUtils-static clearMonitor(target: object, path: string | string[], monitorCallback?: MonitorCallback) : void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| target | object | Yes |
| path | string \| string[] | Yes |
| monitorCallback | [MonitorCallback](arkts-arkui-monitorcallback-t.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [130001](../errorcode-stateManagement.md#130001-invalid-path-for-addmonitorclearmonitor) |
| [130000](../errorcode-stateManagement.md#130000-invalid-target-object-for-addmonitorclearmonitor) |
| [130002](../errorcode-stateManagement.md#130002-invalid-callback-for-addmonitorclearmonitor) |

## enableV2Compatibility

```TypeScript
static enableV2Compatibility<T extends object>(source: T): T
```

Enables V1 state variables to be observable in @ComponentV2. This API is primarily used in scenarios where V1 and V2 state management are mixed. For details, see  
[Mixed Use of State Management V1 and V2 (API Version 19 and Later)](../../../ui/state-management/arkts-v1-v2-mixusage.md).

**Since:** 19

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-UIUtils-static enableV2Compatibility<T extends object>(source: T): T--><!--Device-UIUtils-static enableV2Compatibility<T extends object>(source: T): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| source | T | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

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

Processes all state variable modifications before this API call and synchronizes the  
[dirty](../../../ui/state-management/arkts-state-management-introduce.md#triggering-updates) UI nodes. However, it does not synchronize the execution of @Computed and @Monitor decorators. For details, see  
[applySync/flushUpdates/flushUIUpdates APIs: Synchronous Update](../../../ui/state-management/arkts-new-applySync-flushUpdates-flushUIUpdates.md).

**Since:** 22

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-UIUtils-static flushUIUpdates(): void--><!--Device-UIUtils-static flushUIUpdates(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Error codes:**

| Error Code ID |
| --- |
| [140002](../errorcode-stateManagement.md#140002-invalid-invocation-of-flushupdates-or-flushuiupdates) |
| [140001](../errorcode-stateManagement.md#140001-invalid-invocation-of-applysync-flushupdates-or-flushuiupdates) |

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

Synchronously updates all state variable modifications before this API call, including the updates of @Computed and @Monitor decorators, and re-rendering of the UI nodes. For details, see  
[applySync/flushUpdates/flushUIUpdates APIs: Synchronous Update](../../../ui/state-management/arkts-new-applySync-flushUpdates-flushUIUpdates.md).

**Since:** 22

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-UIUtils-static flushUpdates(): void--><!--Device-UIUtils-static flushUpdates(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Error codes:**

| Error Code ID |
| --- |
| [140002](../errorcode-stateManagement.md#140002-invalid-invocation-of-flushupdates-or-flushuiupdates) |
| [140001](../errorcode-stateManagement.md#140001-invalid-invocation-of-applysync-flushupdates-or-flushuiupdates) |

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

Obtains [CustomComponentContext](arkts-arkui-arkui-statemanagement-customcomponentcontext-i.md) of the given @Component(V1) or @ComponentV2.  
**CustomComponentContext** can be used to access the reuse pool of the component. For details about the reuse pool,see  
[Global Reuse: Centralized Component Recycling and Reuse](../../../ui/state-management/arkts-global-reuse-pool.md).

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-UIUtils-static getCustomComponentContext<T extends BaseCustomComponent>(customComponent: T): CustomComponentContext--><!--Device-UIUtils-static getCustomComponentContext<T extends BaseCustomComponent>(customComponent: T): CustomComponentContext-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| customComponent | T | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [CustomComponentContext](arkts-arkui-arkui-statemanagement-customcomponentcontext-i.md) |

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

Obtains the [lifecycle of a custom component](ComponentInit).

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-UIUtils-static getLifecycle<T extends BaseCustomComponent>(customComponent: T): CustomComponentLifecycle--><!--Device-UIUtils-static getLifecycle<T extends BaseCustomComponent>(customComponent: T): CustomComponentLifecycle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| customComponent | T | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [CustomComponentLifecycle](arkts-arkui-arkui-statemanagement-customcomponentlifecycle-i.md) |

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

Obtains the original object from a proxy object wrapped by the state management framework. For details, see  
[getTarget API: Obtaining Original Objects](../../../ui/state-management/arkts-new-getTarget.md).

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-UIUtils-static getTarget<T extends object>(source: T): T--><!--Device-UIUtils-static getTarget<T extends object>(source: T): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| source | T | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

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

Creates a read-only one-way data binding instance, which is used to construct the arguments of the **Binding** type in the [\@Builder](../../../ui/state-management/arkts-builder.md) function.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-UIUtils-static makeBinding<T>(getter: GetterCallback<T>): Binding<T>--><!--Device-UIUtils-static makeBinding<T>(getter: GetterCallback<T>): Binding<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| getter | [GetterCallback](arkts-arkui-gettercallback-t.md)&lt;T&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Binding](arkts-arkui-arkui-statemanagement-binding-c.md)&lt;T&gt; |

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

Creates a mutable two-way data binding instance, which is used to construct the argument of the **MutableBinding**type in the \@Builder function.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-UIUtils-static makeBinding<T>(getter: GetterCallback<T>, setter: SetterCallback<T>): MutableBinding<T>--><!--Device-UIUtils-static makeBinding<T>(getter: GetterCallback<T>, setter: SetterCallback<T>): MutableBinding<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| getter | [GetterCallback](arkts-arkui-gettercallback-t.md)&lt;T&gt; | Yes |
| setter | [SetterCallback](arkts-arkui-settercallback-t.md)&lt;T&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [MutableBinding](arkts-arkui-arkui-statemanagement-mutablebinding-c.md)&lt;T&gt; |

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

Converts ordinary unobservable data into observable data. For details, see  
[makeObserved API: Changing Unobservable Data to Observable Data](../../../ui/state-management/arkts-new-makeObserved.md).

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-UIUtils-static makeObserved<T extends object>(source: T): T--><!--Device-UIUtils-static makeObserved<T extends object>(source: T): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| source | T | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

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

Wraps an unobservable object into an object that is observable by V1 state management. This API is equivalent to @Observed and can be used to initialize @ObjectLink.

This API can be used together with [enableV2Compatibility](arkts-arkui-arkui-statemanagement-uiutils-c.md#enablev2compatibility) in scenarios where state management V1 and V2 are used together. For details, see  
[Mixed Use of State Management V1 and V2 (API Version 19 and Later)](../../../ui/state-management/arkts-v1-v2-mixusage.md).

**Since:** 19

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-UIUtils-static makeV1Observed<T extends object>(source: T): T--><!--Device-UIUtils-static makeV1Observed<T extends object>(source: T): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| source | T | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

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
