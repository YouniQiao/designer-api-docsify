# AttributeUpdater

**AttributeUpdater** directly set attributes to a component to trigger UI re-renders, without marking them as state variables.

**Inheritance/Implementation:** AttributeUpdater implements AttributeModifier<T>

**Since:** 12

<!--Device-unnamed-export declare class AttributeUpdater--><!--Device-unnamed-export declare class AttributeUpdater-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## applyNormalAttribute

```TypeScript
applyNormalAttribute?(instance: T): void
```

Defines the function for updating attributes in normal state.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AttributeUpdater-applyNormalAttribute?(instance: T): void--><!--Device-AttributeUpdater-applyNormalAttribute?(instance: T): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| instance | T | Yes | Component attribute class, which identifies the type of component to which attributes will be applied, for example, **ButtonAttribute** for the **Button** component and **TextAttribute** for the **Text** component. |

## initializeModifier

```TypeScript
initializeModifier(instance: T): void
```

Initializes the component's attributes to the default values defined in this **AttributeUpdater**.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AttributeUpdater-initializeModifier(instance: T): void--><!--Device-AttributeUpdater-initializeModifier(instance: T): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| instance | T | Yes | Component attribute class, which identifies the type of component to which attributes will be applied, for example, **ButtonAttribute** for the **Button** component and **TextAttribute** for the **Text** component. |

**Examples**

This example shows how to use initializeModifier to initialize attribute values.

```TypeScript
// xxx.ets
import { AttributeUpdater } from '@kit.ArkUI';

class MyButtonModifier extends AttributeUpdater<ButtonAttribute> {
  // Triggered when the AttributeUpdater object is used for the first time.
  initializeModifier(instance: ButtonAttribute): void {
    instance.backgroundColor('#ffd5d5d5')
      .labelStyle({ maxLines: 3 })
      .width('80%')
  }

  // Triggered when the AttributeUpdater object is applied or updated.
  applyNormalAttribute(instance: ButtonAttribute): void {
    instance.borderWidth(1);
  }
}

@Entry
@Component
struct Index {
  modifier: MyButtonModifier = new MyButtonModifier();
  @State flushTheButton: string = 'Button';

  build() {
    Row() {
      Column() {
        Button(this.flushTheButton)
          .attributeModifier(this.modifier)
          .onClick(() => {
            // Update component attributes via AttributeUpdater's attribute property.
            // Note: The component must be bound to the AttributeUpdater via its attributeModifier attribute method.
            this.modifier.attribute?.backgroundColor('#ff2787d9').labelStyle({ maxLines: 5 });
          })
          .margin('10%')
        Button('Trigger Button Update')
          .width('80%')
          .labelStyle({ maxLines: 2 })
          .onClick(() => {
            this.flushTheButton = this.flushTheButton + ' Updated';
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

## onComponentChanged

```TypeScript
onComponentChanged(component: T): void
```

Invoked to notify the application that the component bound to the same custom **Modifier** object changes.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AttributeUpdater-onComponentChanged(component: T): void--><!--Device-AttributeUpdater-onComponentChanged(component: T): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| component | T | Yes | Component attribute class, which identifies the type of component to which attributes will be applied, for example, **ButtonAttribute** for the **Button** component and **TextAttribute** for the **Text** component. |

**Examples**

```TypeScript
// xxx.ets
import { AttributeUpdater } from '@kit.ArkUI';

class MyButtonModifier extends AttributeUpdater<ButtonAttribute> {
  initializeModifier(instance: ButtonAttribute): void {
    instance.backgroundColor('#ff2787d9')
      .width('50%')
      .height(30);
  }

  onComponentChanged(instance: ButtonAttribute): void {
    instance.backgroundColor('#ff519db4')
      .width('50%')
      .height(30);
  }
}

@Entry
@Component
struct updaterDemo4 {
  @State btnState: boolean = false;
  modifier: MyButtonModifier = new MyButtonModifier();

  build() {
    Row() {
      Column() {
        Button("Test")
          .onClick(() => {
            this.btnState = !this.btnState;
          }).margin({ bottom: 20 })

        if (this.btnState) {
          Button("Button")
            .attributeModifier(this.modifier)
        } else {
          Button("Button")
            .attributeModifier(this.modifier)
        }
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

## updateConstructorParams

```TypeScript
updateConstructorParams: C
```

**C** indicates the constructor type of the component, for example, **TextInterface** of the **Text** component and **ImageInterface** of the **Image** component. The type is used to change the constructor input parameters of the component.

**Type:** C

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AttributeUpdater-updateConstructorParams: C--><!--Device-AttributeUpdater-updateConstructorParams: C-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

