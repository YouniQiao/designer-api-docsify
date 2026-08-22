# SyncedPropertyTwoWay (System API)

Inherits from [SubscribedAbstractProperty&lt;T&gt;](arkts-arkui-subscribedabstractproperty-c.md). Represents a property with two-way synchronization.

**Inheritance/Implementation:** SyncedPropertyTwoWay extends SubscribedAbstractProperty<T> and implements ISinglePropertyChangeSubscriber<T>

**Since:** 7

<!--Device-unnamed-declare class SyncedPropertyTwoWay--><!--Device-unnamed-declare class SyncedPropertyTwoWay-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## Modules to Import

```TypeScript
```

## aboutToBeDeleted

```TypeScript
aboutToBeDeleted(unsubscribeMe?: IPropertySubscriber): void
```

Called when the object is about to be destroyed.

**Since:** 7

<!--Device-SyncedPropertyTwoWay-aboutToBeDeleted(unsubscribeMe?: IPropertySubscriber): void--><!--Device-SyncedPropertyTwoWay-aboutToBeDeleted(unsubscribeMe?: IPropertySubscriber): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| unsubscribeMe | [IPropertySubscriber](arkts-arkui-ipropertysubscriber-i-sys.md) | No | Subscriber to remove. |

**Examples**

```TypeScript
AppStorage.setOrCreate('PropA', 47);
let link = AppStorage.setAndLink('PropB', 49); // PropA -> 47, PropB -> 49
link.aboutToBeDeleted();
```

## constructor

```TypeScript
constructor(source: SubscribedAbstractProperty<T>, subscribeMe?: IPropertySubscriber, info?: string)
```

Constructor.

**Since:** 7

<!--Device-SyncedPropertyTwoWay-constructor(source: SubscribedAbstractProperty<T>, subscribeMe?: IPropertySubscriber, info?: string)--><!--Device-SyncedPropertyTwoWay-constructor(source: SubscribedAbstractProperty<T>, subscribeMe?: IPropertySubscriber, info?: string)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| source | [SubscribedAbstractProperty](arkts-arkui-subscribedabstractproperty-c.md)&lt;T&gt; | Yes | Data source for the two-way synchronized property. |
| subscribeMe | [IPropertySubscriber](arkts-arkui-ipropertysubscriber-i-sys.md) | No | Subscriber. |
| info | string | No | Additional information about the subscriber. |

**Examples**

```TypeScript
let para: Record<string, number> = { 'PropA': 47 };
let storage: LocalStorage = new LocalStorage(para);
```

## get

```TypeScript
get(): T
```

Obtains the current value of the property.

**Since:** 7

<!--Device-SyncedPropertyTwoWay-get(): T--><!--Device-SyncedPropertyTwoWay-get(): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| T | Instance of the T type. |

**Examples**

```TypeScript
AppStorage.setOrCreate('PropA', 47);
let value: number = AppStorage.get('PropA') as number; // 47
```

```TypeScript
let para: Record<string, number> = { 'PropA': 47 };
let storage: LocalStorage = new LocalStorage(para);
let value: number = storage.get('PropA') as number; // 47
```

```TypeScript
AppStorage.setOrCreate('PropA', 47);
let ref1: AbstractProperty<number> | undefined = AppStorage.ref('PropA');
ref1?.get(); //  ref1.get()=47
```

```TypeScript
AppStorage.setOrCreate('PropA', 47); 
let prop1: SubscribedAbstractProperty<number> = AppStorage.prop('PropA');    
prop1.get(); //  prop1.get()=47
```

## hasChanged

```TypeScript
hasChanged(newValue: T): void
```

Notifies subscribers that the property value has changed.

**Since:** 7

<!--Device-SyncedPropertyTwoWay-hasChanged(newValue: T): void--><!--Device-SyncedPropertyTwoWay-hasChanged(newValue: T): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| newValue | T | Yes | Instance of the T type. |

## set

```TypeScript
set(newValue: T): void
```

Sets a new value for the property.

**Since:** 7

<!--Device-SyncedPropertyTwoWay-set(newValue: T): void--><!--Device-SyncedPropertyTwoWay-set(newValue: T): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| newValue | T | Yes | Instance of the T type. |

**Examples**

```TypeScript
AppStorage.setOrCreate('PropA', 48);
let res: boolean = AppStorage.set('PropA', 47) // true
let res1: boolean = AppStorage.set('PropB', 47) // false
```

```TypeScript
let para: Record<string, number> = { 'PropA': 47 };
let storage: LocalStorage = new LocalStorage(para);
let res: boolean = storage.set('PropA', 47); // true
let res1: boolean = storage.set('PropB', 47); // false
```

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

## source_

```TypeScript
private source_
```

Data source for the two-way synchronized property.

**Since:** 7

<!--Device-SyncedPropertyTwoWay-private source_--><!--Device-SyncedPropertyTwoWay-private source_-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

