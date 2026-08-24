# ConnectOptionsCollections

Defines the parameter type for the globalConnect API. **ConnectOptionsCollections** is inherited from [ConnectOptions\&lt;T\&gt;](arkts-arkui-arkui-statemanagement-connectoptions-c.md). You can use the **ConnectOptionsCollections** input parameter to persist container data (such as **Array\&lt;S&gt;**).The following shows the examples of **StorageDefaultCreator\&lt;T&gt;** and **StorageDefaultCreator\&lt;S&gt;**:

**Inheritance/Implementation:** ConnectOptionsCollections extends ConnectOptions<T>

**Since:** 23

<!--Device-unnamed-export class ConnectOptionsCollections--><!--Device-unnamed-export class ConnectOptionsCollections-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { AppStorageV2, PersistenceV2, Type, UIUtils, ConnectOptions, Binding, MutableBinding, CustomComponentLifecycle, CustomComponentLifecycleObserver, CustomComponentLifecycleState, ComponentInit, ComponentAppear, ComponentBuilt, ComponentReuse, ComponentActive, ComponentInactive, ComponentRecycle, ComponentDisappear, CollectionType, ConnectOptionsCollections, CustomComponentContext, IReusePool, IReusableInfo } from '@kit.ArkUI';
```

## defaultCreator

```TypeScript
defaultCreator?: StorageDefaultCreator<T>
```

Persists container data. **defaultSubCreator** should be provided together with **defaultCreator**; otherwise, the container data cannot be persisted. The collection item type **S** must be the same as the return type of **defaultSubCreator**. If **defaultSubCreator** is provided but **defaultCreator** is not, the persistence fails.

**Type:** [StorageDefaultCreator](arkts-arkui-storagedefaultcreator-t.md)&lt;T&gt;

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-ConnectOptionsCollections-defaultCreator?: StorageDefaultCreator<T>--><!--Device-ConnectOptionsCollections-defaultCreator?: StorageDefaultCreator<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## defaultSubCreator

```TypeScript
defaultSubCreator?: StorageDefaultCreator<S>
```

Persists container data. If the return value of **defaultSubCreator** is **undefined** or **null**, the persistence fails. When a user-defined class collection (such as **Array&lt;ClassA&gt;**) is persisted, the generic type **T** in **defaultCreator** is **Array&lt;ClassA&gt;**, and **S** in **defaultSubCreator** is **ClassA**.

**Type:** [StorageDefaultCreator](arkts-arkui-storagedefaultcreator-t.md)&lt;S&gt;

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-ConnectOptionsCollections-defaultSubCreator?: StorageDefaultCreator<S>--><!--Device-ConnectOptionsCollections-defaultSubCreator?: StorageDefaultCreator<S>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Examples**

```TypeScript
class ClassA {
  propA: number;
  // ...
}

@ComponentV2
struct Page {
  // The default creator of StorageDefaultCreator<T> is `() => UIUtils.makeObserved(new Array<ClassA>())`, in which the `T` type is `Array<ClassA>`
  // The default creator of StorageDefaultCreator<S> is `() =>UIUtils.makeObserved(new ClassA())`, in which the `S` type is `ClassA`.
  @Local arr: Array<ClassA> = PersistenceV2.globalConnect({
    type: Array<ClassA>,
    defaultCreator: () => UIUtils.makeObserved(new Array<ClassA>()),
    // Add defaultSubCreator to notify the state management framework of how to create ClassA objects.
    // Add makeObserved to the persistent data. Otherwise, the persistence will fail.
    defaultSubCreator: () => UIUtils.makeObserved(new ClassA())
  })!
  // ...
}
```

If the return value of StorageDefaultCreator<S> is undefined or null, the persistence fails. If StorageDefaultCreator<S> is directly set to undefined or null, the state management framework persists data based on the original type (such as Object), but will lose the methods in the class object. In the following example, if StorageDefaultCreator<S> is directly set to undefined or null, the report method in the ClassA object will be lost during persistence.

```TypeScript
import { PersistenceV2, UIUtils } from '@kit.ArkUI';
import { hilog } from '@kit.PerformanceAnalysisKit';

@ObservedV2
class ClassA {
  @Trace public propA: string = '';
  @Trace public propB: string = '';

  public report(): string {
    return `${this.propA} - ${this.propB}`;
  }
}

@Entry
@ComponentV2
struct Comp {
  // Persist the top-level data whose type is Array<ClassA>.
  @Local arr: Array<ClassA> = PersistenceV2.globalConnect({
    type: Array<ClassA>,
    defaultCreator: () => UIUtils.makeObserved(new Array<ClassA>()),
    // The return value of defaultSubCreator is set to `undefined` or `null` (defaultSubCreator: () => undefined), and the persistence fails.
    // defaultSubCreator is directly set to `undefined` or `null` (defaultSubCreator: undefined), and the methods in ClassA will be lost during persistence.
    defaultSubCreator: undefined
  })!;

  aboutToAppear(): void {
    if (this.arr.length) {
      // Step 3: Access the application again. During the persistence, the method in `ClassA` is lost. When the `report` method in the `ClassA` object is called, the error message "undefined is not callable" is displayed.
      hilog.info(0xFF00, 'testTag', '%{public}s', this.arr[0].report());
    }
  }
  build() {
    Column() {
      Repeat(this.arr)
        .each(ri => {
          Row() {
            Text(`propA '${ri.item.propA}'`)
            Text(`propB '${ri.item.propB}'`)
            Text(`report?.() '${ri.item.report?.()}'`)
          }
        })
      // Step 1: Click "add item". The message `propA 'a' propB 'b'report?.'a' - 'b'` is displayed.
      // Step 2: Close the application.
      Button('add item')
        .onClick(() => {
          let temp: ClassA = new ClassA();
          temp.propA = 'a';
          temp.propB = 'b';
          this.arr.push(temp);
        })
    }
  }
}
```

