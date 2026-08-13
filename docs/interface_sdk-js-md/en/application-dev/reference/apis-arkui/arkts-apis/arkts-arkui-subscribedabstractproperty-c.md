# SubscribedAbstractProperty (System API)

Represents a synchronized property from [AppStorage](../../../ui/state-management/arkts-appstorage.md) or [LocalStorage](../../../ui/state-management/arkts-localstorage.md).

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** -1

<!--Device-unnamed-declare abstract class SubscribedAbstractProperty--><!--Device-unnamed-declare abstract class SubscribedAbstractProperty-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## aboutToBeDeleted

```TypeScript
abstract aboutToBeDeleted(): void
```

Cancels the synchronization relationship between the [SubscribedAbstractProperty](#SubscribedAbstractProperty-(System-API)) instance and [AppStorage](../../../ui/state-management/arkts-appstorage.md) or [LocalStorage](../../../ui/state-management/arkts-localstorage.md), whether it is a one-way or two-way binding. After **aboutToBeDeleted** is called, the **SubscribedAbstractProperty** instance is invalidated, meaning it can no longer be used to call the [set](arkts-arkui-localstorage-c.md#set) or [get](arkts-arkui-localstorage-c.md#get) API.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SubscribedAbstractProperty-abstract aboutToBeDeleted(): void--><!--Device-SubscribedAbstractProperty-abstract aboutToBeDeleted(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Examples

```TypeScript
AppStorage.setOrCreate('PropA', 47);
let link = AppStorage.setAndLink('PropB', 49); // PropA -> 47, PropB -> 49
link.aboutToBeDeleted();
```

## get

```TypeScript
abstract get(): T
```

Reads the data of the synchronized property from [AppStorage](../../../ui/state-management/arkts-appstorage.md) or [LocalStorage](../../../ui/state-management/arkts-localstorage.md).

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-SubscribedAbstractProperty-abstract get(): T--><!--Device-SubscribedAbstractProperty-abstract get(): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| T | Data of the synchronized property in AppStorage or LocalStorage. |

## Examples

```TypeScript
AppStorage.setOrCreate('PropA', 47); 
let prop1: SubscribedAbstractProperty<number> = AppStorage.prop('PropA');    
prop1.get(); //  prop1.get()=47
```

## info

```TypeScript
info(): string
```

Property name.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SubscribedAbstractProperty-info(): string--><!--Device-SubscribedAbstractProperty-info(): string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| string | Property name. |

## Examples

```TypeScript
AppStorage.setOrCreate('PropA', 47); 
let prop1: SubscribedAbstractProperty<number> = AppStorage.prop('PropA');
prop1.info(); // prop1.info() = 'PropA'
```

## set

```TypeScript
abstract set(newValue: T): void
```

Sets the data of the synchronized property in [AppStorage](../../../ui/state-management/arkts-appstorage.md) or [LocalStorage](../../../ui/state-management/arkts-localstorage.md). The value of **newValue** must be of the **T** type. Since API version 12, it can be **null** or **undefined**. > **NOTE：**> Since API version 12, AppStorage and LocalStorage support the Map, Set, Date types, as well as **null**, > **undefined**, and union types.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-SubscribedAbstractProperty-abstract set(newValue: T): void--><!--Device-SubscribedAbstractProperty-abstract set(newValue: T): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| newValue | T | Yes | Data to set. Since API version 12, the value can be **null** or **undefined**. |

## Examples

```TypeScript
AppStorage.setOrCreate('PropA', 47);
let prop1: SubscribedAbstractProperty<number> = AppStorage.prop('PropA');
prop1.set(1); //  prop1.get()=1
// Since API version 12, the Map, Set, Date types, as well as null, undefined, and union types are supported.
let a: Map<string, number> = new Map([['1', 0]]);
let prop2 = AppStorage.setAndProp('MapA', a);
prop2.set(a);
let b: Set<string> = new Set('1');
let prop3 = AppStorage.setAndProp('SetB', b);
prop3.set(b);
let c: Date = new Date('2024');
let prop4 = AppStorage.setAndProp('DateC', c);
prop4.set(c);
prop2.set(null);
prop3.set(undefined);
```

