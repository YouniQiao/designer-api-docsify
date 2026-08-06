# SubscribedAbstractProperty

SubscribedAbstractProperty\_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_ is the return value of

- AppStorage static functions Link(), Prop(), SetAndLink(), and SetAndProp()  
- LocalStorage member methods link(), prop(), setAndLink(), and setAndProp()  
'T' can be boolean, string, number or custom class.Main functions see get() reads the linked AppStorage/LocalStorage property value,see set(newValue) write a new value to the synched AppStorage/LocalStorage property see aboutToBeDeleted() ends the sync relationship with the AppStorage/LocalStorage property The app must call this function before the SubscribedAbstractProperty\_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_ object goes out of scope.

**Inheritance/Implementation:** SubscribedAbstractProperty extends [AbstractProperty<T>](AbstractProperty<T>)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface SubscribedAbstractProperty<T> extends AbstractProperty<T>--><!--Device-unnamed-export declare interface SubscribedAbstractProperty<T> extends AbstractProperty<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## aboutToBeDeleted

```TypeScript
default aboutToBeDeleted(): void
```

An app needs to call this function before the instance of SubscribedAbstractProperty goes out of scope / is subject to garbage collection. Its purpose is to unregister the variable from the two-way/one-way sync relationship that AppStorage/LocalStorage.link()/prop()and related functions create.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SubscribedAbstractProperty-default aboutToBeDeleted(): void--><!--Device-SubscribedAbstractProperty-default aboutToBeDeleted(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

