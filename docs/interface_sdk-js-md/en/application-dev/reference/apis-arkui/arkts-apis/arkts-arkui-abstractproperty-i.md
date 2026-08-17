# AbstractProperty(System API)

Provides a reference to properties stored in [AppStorage](../../../ui/state-management/arkts-appstorage.md) or [LocalStorage](../../../ui/state-management/arkts-localstorage.md).

**Since:** 12

<!--Device-unnamed-declare interface AbstractProperty--><!--Device-unnamed-declare interface AbstractProperty-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## get

```TypeScript
get(): T
```

Reads data of the referenced property from [AppStorage](../../../ui/state-management/arkts-appstorage.md) or [LocalStorage](../../../ui/state-management/arkts-localstorage.md).

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AbstractProperty-get(): T--><!--Device-AbstractProperty-get(): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| T | Data of the referenced property in AppStorage or LocalStorage. |

**Examples**

```TypeScript
AppStorage.setOrCreate('PropA', 47);
let ref1: AbstractProperty<number> | undefined = AppStorage.ref('PropA');
ref1?.get(); //  ref1.get()=47
```

## info

```TypeScript
info(): string
```

Reads the property name of the referenced property from [AppStorage](../../../ui/state-management/arkts-appstorage.md) or [LocalStorage](../../../ui/state-management/arkts-localstorage.md).

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AbstractProperty-info(): string--><!--Device-AbstractProperty-info(): string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| string | Property name of the referenced property in AppStorage or LocalStorage. |

**Examples**

```TypeScript
AppStorage.setOrCreate('PropA', 47);
let ref1: AbstractProperty<number> | undefined = AppStorage.ref('PropA');
ref1?.info(); //  ref1.info()='PropA'
```

## set

```TypeScript
set(newValue: T): void
```

Updates the data of the referenced property in [AppStorage](../../../ui/state-management/arkts-appstorage.md) or [LocalStorage](../../../ui/state-management/arkts-localstorage.md). The value of **newValue** must be of the **T** type and can be **null** or **undefined**. > **NOTE：**> Since API version 12, AppStorage and LocalStorage support the Map, Set, Date types, as well as **null**, > **undefined**, and union types.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AbstractProperty-set(newValue: T): void--><!--Device-AbstractProperty-set(newValue: T): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| newValue | T | Yes | New data to update. The value can be **null** or **undefined**. |

**Examples**

```TypeScript
AppStorage.setOrCreate('PropA', 47);
let ref1: AbstractProperty<number> | undefined = AppStorage.ref('PropA');
ref1?.set(1); //  ref1.get()=1
let a: Map<string, number> = new Map([['1', 0]]);
let ref2 = AppStorage.setAndRef('MapA', a);
ref2.set(a);
let b: Set<string> = new Set('1');
let ref3 = AppStorage.setAndRef('SetB', b);
ref3.set(b);
let c: Date = new Date('2024');
let ref4 = AppStorage.setAndRef('DateC', c);
ref4.set(c);
ref2.set(null);
ref3.set(undefined);
```

