# Binding

Represents the generic class for read-only data binding, which can bind data of any type.

**Since:** 20

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { AppStorageV2, PersistenceV2, Type, UIUtils, ConnectOptions, Binding, MutableBinding, CustomComponentLifecycle, CustomComponentLifecycleObserver, CustomComponentLifecycleState, ComponentInit, ComponentAppear, ComponentBuilt, ComponentReuse, ComponentActive, ComponentInactive, ComponentRecycle, ComponentDisappear, CollectionType, ConnectOptionsCollections, CustomComponentContext, IReusePool, IReusableInfo, StorageDefaultCreator, TypeConstructorWithArgs, PersistenceErrorCallback, TypeConstructor, TypeDecorator, MonitorCallback, MonitorOptions, GetterCallback, SetterCallback, ObservedResult, DecoratorInfo, ElementInfo } from '@kit.ArkUI';
```

## value

```TypeScript
get value(): T
```

Obtains a bound value.

**Type:** T

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Examples**

```TypeScript
import { Binding, UIUtils } from '@kit.ArkUI';

@Builder
function CustomButton(num1: Binding<number>) {
  // The first parameter of CustomButton is Binding, which is a generic class for read-only data binding.
  Row() {
    // num1.value Binding can use the bound value.
    Button(`Custom Button: ${num1.value}`)
      .onClick(() => {
        // num1.value += 1; will throw an error because the generic class bound to the read-only data does not support modification.
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
        UIUtils.makeBinding<number>(
          () => this.number1 // GetterCallback
        )
      )
    }
  }
}
```

```TypeScript
import { MutableBinding, UIUtils } from '@kit.ArkUI';

@Builder
function CustomButton(num1: MutableBinding<number>) {
  // The second parameter of CustomButton is MutableBinding, which is a generic class of mutable data binding.
  Row() {
    Button(`Custom Button: ${num1.value}`)
      .onClick(() => {
        // The generic class of mutable data binding can be used to modify the bound value.
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
        UIUtils.makeBinding<number>(
          () => this.number1, // GetterCallback
          (val: number) => {
            this.number1 = val;
          }) // SetterCallback is mandatory. Otherwise, a runtime error will be thrown.
      )
    }
  }
}
```
