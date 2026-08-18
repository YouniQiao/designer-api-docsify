# AppStorage(System API)

For details about how to use AppStorage, see [AppStorage: Storing Application-wide UI State](../../../ui/state-management/arkts-appstorage.md).

**Since:** 7

<!--Device-unnamed-declare class AppStorage--><!--Device-unnamed-declare class AppStorage-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## Clear

```TypeScript
static Clear(): boolean
```

Deletes all properties from [AppStorage](../../../ui/state-management/arkts-appstorage.md). The deletion is only successful if none of the properties in AppStorage have any subscribers. If there are subscribers, this API does not take effect and **false** is returned. If there are no subscribers, the deletion is successful and **true** is returned. For details about the subscriber, see [delete](#delete).

**Since:** 9

**Deprecated since:** 10

**Substitutes:** [clear](#clear)

<!--Device-AppStorage-static Clear(): boolean--><!--Device-AppStorage-static Clear(): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Examples**

```TypeScript
let clearResult = AppStorage.staticClear();
```

```TypeScript
AppStorage.SetOrCreate('PropA', 47);
let res: boolean = AppStorage.Clear(); // true: There are no subscribers.
```

## Delete

```TypeScript
static Delete(propName: string): boolean
```

Deletes the property corresponding to **propName** from [AppStorage](../../../ui/state-management/arkts-appstorage.md). The deletion is only successful if the property has no subscribers. If there is a subscriber, the deletion fails and **false** is returned. If there are no subscribers, the deletion is successful and **true** is returned. Subscribers include properties bound using [Link](#link) and [Prop](#prop) APIs, as well as those decorated with [\@StorageLink('propName')](../../../ui/state-management/arkts-appstorage.md#storagelink) and [\@StorageProp('propName')](../../../ui/state-management/arkts-appstorage.md#storageprop). This means that if \@StorageLink('propName') and \@StorageProp('propName') are used in a custom component or if there is still a **SubscribedAbstractProperty** instance in a synchronization relationship with the property, the property cannot be deleted from AppStorage.

**Since:** 7

**Deprecated since:** 10

**Substitutes:** [delete](#delete)

<!--Device-AppStorage-static Delete(propName: string): boolean--><!--Device-AppStorage-static Delete(propName: string): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| propName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Examples**

```TypeScript
AppStorage.SetOrCreate('PropA', 47);
AppStorage.Link('PropA');
let res: boolean = AppStorage.Delete('PropA'); // false: PropA still has subscribers.

AppStorage.SetOrCreate('PropB', 48);
let res1: boolean = AppStorage.Delete('PropB'); // true: PropB is successfully deleted from AppStorage.
```

## Get

```TypeScript
static Get<T>(propName: string): T | undefined
```

Obtains the value of the property corresponding to **propName** from [AppStorage](../../../ui/state-management/arkts-appstorage.md). If the property does not exist, this API returns **undefined**.

**Since:** 7

**Deprecated since:** 10

**Substitutes:** [get](#get)

<!--Device-AppStorage-static Get<T>(propName: string): T | undefined--><!--Device-AppStorage-static Get<T>(propName: string): T | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| propName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

**Examples**

```TypeScript
AppStorage.SetOrCreate('PropA', 47);
let value: number = AppStorage.Get('PropA') as number; // 47
```

## Has

```TypeScript
static Has(propName: string): boolean
```

Checks whether the property corresponding to **propName** exists in [AppStorage](../../../ui/state-management/arkts-appstorage.md).

**Since:** 7

**Deprecated since:** 10

**Substitutes:** [has](#has)

<!--Device-AppStorage-static Has(propName: string): boolean--><!--Device-AppStorage-static Has(propName: string): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| propName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Examples**

```TypeScript
AppStorage.Has('simpleProp');
```

## IsMutable

```TypeScript
static IsMutable(propName: string): boolean
```

Checks whether the property corresponding to **propName** in [AppStorage](../../../ui/state-management/arkts-appstorage.md) is mutable.

**Since:** 7

**Deprecated since:** 10

<!--Device-AppStorage-static IsMutable(propName: string): boolean--><!--Device-AppStorage-static IsMutable(propName: string): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| propName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Examples**

```TypeScript
AppStorage.SetOrCreate('PropA', 47);
let res: boolean = AppStorage.IsMutable('PropA');
```

## Keys

```TypeScript
static Keys(): IterableIterator<string>
```

Obtains all property names in [AppStorage](../../../ui/state-management/arkts-appstorage.md).

**Since:** 7

**Deprecated since:** 10

**Substitutes:** [keys](#keys)

<!--Device-AppStorage-static Keys(): IterableIterator<string>--><!--Device-AppStorage-static Keys(): IterableIterator<string>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [IterableIterator](../../apis-na/arkts-apis/arkts-na-lib-es2015-iterable-iterableiterator-i.md)&lt;string&gt; |

**Examples**

```TypeScript
AppStorage.SetOrCreate('PropB', 48);
let keys: IterableIterator<string> = AppStorage.Keys();
```

## Link

```TypeScript
static Link(propName: string): any
```

Establishes a two-way data binding with the property corresponding to **propName** in [AppStorage](../../../ui/state-management/arkts-appstorage.md). If the given property exists in AppStorage, the two-way bound data of the property in AppStorage is returned. Any update of the data is synchronized back to AppStorage, which then synchronizes the update to all data and custom components bound to the property. If the given property does not exist in AppStorage, **undefined** is returned.

**Since:** 7

**Deprecated since:** 10

**Substitutes:** [link](#link)

<!--Device-AppStorage-static Link(propName: string): any--><!--Device-AppStorage-static Link(propName: string): any-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| propName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| any |

**Examples**

```TypeScript
AppStorage.SetOrCreate('PropA', 47);
let linkToPropA1: SubscribedAbstractProperty<number> = AppStorage.Link('PropA');
let linkToPropA2: SubscribedAbstractProperty<number> = AppStorage.Link('PropA'); // linkToPropA2.get() == 47
linkToPropA1.set(48); // Two-way synchronization: linkToPropA1.get() == linkToPropA2.get() == 48
```

## Prop

```TypeScript
static Prop(propName: string): any
```

Establishes a one-way data binding with the property corresponding to **propName** in [AppStorage](../../../ui/state-management/arkts-appstorage.md). If the given property exists in AppStorage, the one-way bound data of the property in AppStorage is returned. If the given property does not exist in AppStorage, **undefined** is returned. Updates of the one-way bound data are not synchronized back to AppStorage. > **NOTE：**> Prop supports only simple types.

**Since:** 7

**Deprecated since:** 10

**Substitutes:** [prop](#prop)

<!--Device-AppStorage-static Prop(propName: string): any--><!--Device-AppStorage-static Prop(propName: string): any-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| propName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| any |

**Examples**

```TypeScript
AppStorage.SetOrCreate('PropA', 47);
let prop1: SubscribedAbstractProperty<number> = AppStorage.Prop('PropA');
let prop2: SubscribedAbstractProperty<number> = AppStorage.Prop('PropA');
prop1.set(1); // One-way synchronization: prop1.get() returns 1, while prop2.get() returns 47.
```

## Set

```TypeScript
static Set<T>(propName: string, newValue: T): boolean
```

Sets the value of the property corresponding to **propName** in [AppStorage](../../../ui/state-management/arkts-appstorage.md). If the value of **newValue** is the same as the current value of the property, no assignment is performed, and the state variable does not instruct the UI to update the value of the property. Starting from API version 12, **newValue** can be **null** or **undefined**.

**Since:** 7

**Deprecated since:** 10

**Substitutes:** [set](#set)

<!--Device-AppStorage-static Set<T>(propName: string, newValue: T): boolean--><!--Device-AppStorage-static Set<T>(propName: string, newValue: T): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| propName | string | Yes |
| newValue | T | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Examples**

```TypeScript
AppStorage.SetOrCreate('PropA', 48);
let res: boolean = AppStorage.Set('PropA', 47); // true
let res1: boolean = AppStorage.Set('PropB', 47); // false
```

## SetAndLink

```TypeScript
static SetAndLink<T>(propName: string, defaultValue: T): SubscribedAbstractProperty<T>
```

Similar to the [Link](#link) API, establishes a two-way data binding with the property corresponding to **propName** in [AppStorage](../../../ui/state-management/arkts-appstorage.md). If the given property exists in AppStorage, this API returns the two-way bound data for the property. If the given property does not exist, this API creates and initializes the property in AppStorage using **defaultValue** and returns its two- way bound data. The value of **defaultValue** must be of the **T** type and cannot be **null** or **undefined**.

**Since:** 7

**Deprecated since:** 10

**Substitutes:** [setAndLink](#setandlink)

<!--Device-AppStorage-static SetAndLink<T>(propName: string, defaultValue: T): SubscribedAbstractProperty<T>--><!--Device-AppStorage-static SetAndLink<T>(propName: string, defaultValue: T): SubscribedAbstractProperty<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| propName | string | Yes |
| defaultValue | T | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SubscribedAbstractProperty](arkts-arkui-subscribedabstractproperty-c.md)&lt;T&gt; |

**Examples**

```TypeScript
AppStorage.SetOrCreate('PropA', 47);
let link1: SubscribedAbstractProperty<number> = AppStorage.SetAndLink('PropB', 49); // Create PropB with the default value 49.
let link2: SubscribedAbstractProperty<number> = AppStorage.SetAndLink('PropA', 50); // PropA already exists with the value 47.
```

## SetAndProp

```TypeScript
static SetAndProp<S>(propName: string, defaultValue: S): SubscribedAbstractProperty<S>
```

Similar to the [Prop](#prop) API, establishes a one-way data binding with the property corresponding to **propName** in [AppStorage](../../../ui/state-management/arkts-appstorage.md). If the given property exists in AppStorage, this API returns the one-way bound data for the property. If the given property does not exist, this API creates and initializes the property in AppStorage using **defaultValue** and returns its one- way bound data. The value of **defaultValue** must be of the **S** type and cannot be **null** or **undefined**.

**Since:** 7

**Deprecated since:** 10

**Substitutes:** [setAndProp](#setandprop)

<!--Device-AppStorage-static SetAndProp<S>(propName: string, defaultValue: S): SubscribedAbstractProperty<S>--><!--Device-AppStorage-static SetAndProp<S>(propName: string, defaultValue: S): SubscribedAbstractProperty<S>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| propName | string | Yes |
| defaultValue | S | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SubscribedAbstractProperty](arkts-arkui-subscribedabstractproperty-c.md)&lt;S&gt; |

**Examples**

```TypeScript
AppStorage.SetOrCreate('PropA', 47);
let prop: SubscribedAbstractProperty<number> = AppStorage.SetAndProp('PropB', 49); // PropA -> 47, PropB -> 49
```

## SetOrCreate

```TypeScript
static SetOrCreate<T>(propName: string, newValue: T): void
```

Sets the value of the property corresponding to **propName** in [AppStorage](../../../ui/state-management/arkts-appstorage.md) to a new value, if the property exists. If the property does not exist, this API creates it with the value of **newValue**. The value of **newValue** cannot be **null** or **undefined**.

**Since:** 7

**Deprecated since:** 10

**Substitutes:** [setOrCreate](#setorcreate)

<!--Device-AppStorage-static SetOrCreate<T>(propName: string, newValue: T): void--><!--Device-AppStorage-static SetOrCreate<T>(propName: string, newValue: T): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| propName | string | Yes |
| newValue | T | Yes |

**Examples**

```TypeScript
AppStorage.SetOrCreate('simpleProp', 121);
```

## Size

```TypeScript
static Size(): number
```

Obtains the number of properties in [AppStorage](../../../ui/state-management/arkts-appstorage.md).

**Since:** 7

**Deprecated since:** 10

**Substitutes:** [size](#size)

<!--Device-AppStorage-static Size(): number--><!--Device-AppStorage-static Size(): number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Examples**

```TypeScript
AppStorage.SetOrCreate('PropB', 48);
let res: number = AppStorage.Size(); // 1
```

## clear

```TypeScript
static clear(): boolean
```

Deletes all properties from [AppStorage](../../../ui/state-management/arkts-appstorage.md). The deletion is only successful if none of the properties in AppStorage have any subscribers. If there are subscribers, this API does not take effect and **false** is returned. If there are no subscribers, the deletion is successful and **true** is returned. For details about the subscriber, see [delete](#delete).

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AppStorage-static clear(): boolean--><!--Device-AppStorage-static clear(): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Examples**

```TypeScript
AppStorage.setOrCreate('PropA', 47);
let res: boolean = AppStorage.clear(); // true: There are no subscribers.
```

## delete

```TypeScript
static delete(propName: string): boolean
```

Deletes the property corresponding to **propName** from [AppStorage](../../../ui/state-management/arkts-appstorage.md). The deletion is only successful if the property has no subscribers. If there is a subscriber, the deletion fails and **false** is returned. If there are no subscribers, the deletion is successful and **true** is returned. The property subscribers include the following: 1. Variables decorated by [\@StorageLink](../../../ui/state-management/arkts-appstorage.md#storagelink) or [\@StorageProp](../../../ui/state-management/arkts-appstorage.md#storageprop) 2. Instances of SubscribedAbstractProperty returned by [link](#link), [prop](#prop), [setAndLink](#setandlink), or [setAndProp](#setandprop) To delete these subscribers: 1. Remove the custom component containing \@StorageLink or \@StorageProp. For details, see [Custom Component Deletion](../../../ui/state-management/arkts-page-custom-components-lifecycle.md#custom-component-deletion). 2. Call the [aboutToBeDeleted](arkts-arkui-subscribedabstractproperty-c.md#abouttobedeleted) API on instances of **SubscribedAbstractProperty** returned by **link**, **prop**, **setAndLink**, or **setAndProp**.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AppStorage-static delete(propName: string): boolean--><!--Device-AppStorage-static delete(propName: string): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| propName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Examples**

```TypeScript
AppStorage.setOrCreate('PropA', 47);
AppStorage.link<number>('PropA');
let res: boolean = AppStorage.delete('PropA'); // false: PropA still has subscribers.

AppStorage.setOrCreate('PropB', 48);
let res1: boolean = AppStorage.delete('PropB'); // true: PropB is successfully deleted from AppStorage.
```

## get

```TypeScript
static get<T>(propName: string): T | undefined
```

Obtains the value of the property corresponding to **propName** from [AppStorage](../../../ui/state-management/arkts-appstorage.md). If the property does not exist, this API returns **undefined**.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AppStorage-static get<T>(propName: string): T | undefined--><!--Device-AppStorage-static get<T>(propName: string): T | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| propName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

**Examples**

```TypeScript
AppStorage.setOrCreate('PropA', 47);
let value: number = AppStorage.get('PropA') as number; // 47
```

## has

```TypeScript
static has(propName: string): boolean
```

Checks whether the property corresponding to **propName** exists in [AppStorage](../../../ui/state-management/arkts-appstorage.md).

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AppStorage-static has(propName: string): boolean--><!--Device-AppStorage-static has(propName: string): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| propName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Examples**

```TypeScript
AppStorage.has('simpleProp');
```

## keys

```TypeScript
static keys(): IterableIterator<string>
```

Obtains all property names in [AppStorage](../../../ui/state-management/arkts-appstorage.md).

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AppStorage-static keys(): IterableIterator<string>--><!--Device-AppStorage-static keys(): IterableIterator<string>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [IterableIterator](../../apis-na/arkts-apis/arkts-na-lib-es2015-iterable-iterableiterator-i.md)&lt;string&gt; |

**Examples**

```TypeScript
AppStorage.setOrCreate('PropB', 48);
let keys: IterableIterator<string> = AppStorage.keys();
```

## link

```TypeScript
static link<T>(propName: string): SubscribedAbstractProperty<T>
```

Establishes a two-way data binding with the property corresponding to **propName** in [AppStorage](../../../ui/state-management/arkts-appstorage.md). If the given property exists in AppStorage, the two-way bound data of the property in AppStorage is returned. Any update of the data is synchronized back to AppStorage, which then synchronizes the update to all data and custom components bound to the property. If the given property does not exist in AppStorage, **undefined** is returned.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AppStorage-static link<T>(propName: string): SubscribedAbstractProperty<T>--><!--Device-AppStorage-static link<T>(propName: string): SubscribedAbstractProperty<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| propName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SubscribedAbstractProperty](arkts-arkui-subscribedabstractproperty-c.md)&lt;T&gt; |

**Examples**

```TypeScript
AppStorage.setOrCreate('PropA', 47);
let linkToPropA1: SubscribedAbstractProperty<number> = AppStorage.link('PropA');
let linkToPropA2: SubscribedAbstractProperty<number> = AppStorage.link('PropA'); // linkToPropA2.get() == 47
linkToPropA1.set(48); // Two-way synchronization: linkToPropA1.get() == linkToPropA2.get() == 48.
```

## prop

```TypeScript
static prop<T>(propName: string): SubscribedAbstractProperty<T>
```

Establishes a one-way data binding with the property corresponding to **propName** in [AppStorage](../../../ui/state-management/arkts-appstorage.md). If the given property exists in AppStorage, the one-way bound data of the property in AppStorage is returned. If the given property does not exist in AppStorage, **undefined** is returned. Updates of the one-way bound data are not synchronized back to AppStorage.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AppStorage-static prop<T>(propName: string): SubscribedAbstractProperty<T>--><!--Device-AppStorage-static prop<T>(propName: string): SubscribedAbstractProperty<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| propName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SubscribedAbstractProperty](arkts-arkui-subscribedabstractproperty-c.md)&lt;T&gt; |

**Examples**

```TypeScript
AppStorage.setOrCreate('PropA', 47);
let prop1: SubscribedAbstractProperty<number> = AppStorage.prop('PropA');
let prop2: SubscribedAbstractProperty<number> = AppStorage.prop('PropA');
prop1.set(1); // One-way synchronization: prop1.get() returns 1, while prop2.get() returns 47.
```

## ref

```TypeScript
static ref<T>(propName: string): AbstractProperty<T> | undefined
```

Returns a reference to the property corresponding to **propName** in [AppStorage](../../../ui/state-management/arkts-appstorage.md). If the provided **propName** does not exist, this API returns **undefined**. This API is similar to [link](#link) but does not require manually releasing the returned variable of the [AbstractProperty](arkts-arkui-abstractproperty-i.md#abstractproperty) type.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AppStorage-static ref<T>(propName: string): AbstractProperty<T> | undefined--><!--Device-AppStorage-static ref<T>(propName: string): AbstractProperty<T> | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| propName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [AbstractProperty](arkts-arkui-abstractproperty-i.md)&lt;T&gt; |

**Examples**

```TypeScript
AppStorage.setOrCreate('PropA', 47);
let refToPropA1: AbstractProperty<number> | undefined = AppStorage.ref('PropA');
let refToPropA2: AbstractProperty<number> | undefined = AppStorage.ref('PropA'); // refToPropA2.get() == 47
refToPropA1?.set(48); // Synchronously modify AppStorage: refToPropA1.get() == refToPropA2.get() == 48.
```

## set

```TypeScript
static set<T>(propName: string, newValue: T): boolean
```

Sets the value of the property corresponding to **propName** in [AppStorage](../../../ui/state-management/arkts-appstorage.md). If the value of **newValue** is the same as the current value of the property, no assignment is performed, and the state variable does not instruct the UI to update the value of the property. > **NOTE：**> Since API version 12, AppStorage supports > [Map](../../../ui/state-management/arkts-appstorage.md#decorating-variables-of-the-map-type), > [Set](../../../ui/state-management/arkts-appstorage.md#decorating-variables-of-the-set-type), > [Date](../../../ui/state-management/arkts-appstorage.md#decorating-variables-of-the-date-type), **null**, > **undefined**, and [union](../../../ui/state-management/arkts-appstorage.md#using-union-types-in-appstorage) > types.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AppStorage-static set<T>(propName: string, newValue: T): boolean--><!--Device-AppStorage-static set<T>(propName: string, newValue: T): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| propName | string | Yes |
| newValue | T | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Examples**

```TypeScript
AppStorage.setOrCreate('PropA', 48);
let res: boolean = AppStorage.set('PropA', 47); // true
let res1: boolean = AppStorage.set('PropB', 47); // false
```

## setAndLink

```TypeScript
static setAndLink<T>(propName: string, defaultValue: T): SubscribedAbstractProperty<T>
```

Similar to the [link](#link) API, establishes a two-way data binding with the property corresponding to **propName** in [AppStorage](../../../ui/state-management/arkts-appstorage.md). If the given property exists in AppStorage, this API returns the two-way bound data for the property. If the given property does not exist, this API creates and initializes the property in AppStorage using **defaultValue** and returns its two- way bound data. > **NOTE：**> Since API version 12, AppStorage supports > [Map](../../../ui/state-management/arkts-appstorage.md#decorating-variables-of-the-map-type), > [Set](../../../ui/state-management/arkts-appstorage.md#decorating-variables-of-the-set-type), > [Date](../../../ui/state-management/arkts-appstorage.md#decorating-variables-of-the-date-type), **null**, > **undefined**, and [union](../../../ui/state-management/arkts-appstorage.md#using-union-types-in-appstorage) > types.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AppStorage-static setAndLink<T>(propName: string, defaultValue: T): SubscribedAbstractProperty<T>--><!--Device-AppStorage-static setAndLink<T>(propName: string, defaultValue: T): SubscribedAbstractProperty<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| propName | string | Yes |
| defaultValue | T | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SubscribedAbstractProperty](arkts-arkui-subscribedabstractproperty-c.md)&lt;T&gt; |

**Examples**

```TypeScript
AppStorage.setOrCreate('PropA', 47);
let link1: SubscribedAbstractProperty<number> = AppStorage.setAndLink('PropB', 49); // Create PropB with the default value 49.
let link2: SubscribedAbstractProperty<number> = AppStorage.setAndLink('PropA', 50); // PropA already exists with the value 47.
```

## setAndProp

```TypeScript
static setAndProp<T>(propName: string, defaultValue: T): SubscribedAbstractProperty<T>
```

Similar to the [prop](#prop) API, establishes a one-way data binding with the property corresponding to **propName** in [AppStorage](../../../ui/state-management/arkts-appstorage.md). If the given property exists in AppStorage, this API returns the one-way bound data for the property. If the given property does not exist, this API creates and initializes the property in AppStorage using **defaultValue** and returns its one- way bound data. > **NOTE：**> Since API version 12, AppStorage supports > [Map](../../../ui/state-management/arkts-appstorage.md#decorating-variables-of-the-map-type), > [Set](../../../ui/state-management/arkts-appstorage.md#decorating-variables-of-the-set-type), > [Date](../../../ui/state-management/arkts-appstorage.md#decorating-variables-of-the-date-type), **null**, > **undefined**, and [union](../../../ui/state-management/arkts-appstorage.md#using-union-types-in-appstorage) > types.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AppStorage-static setAndProp<T>(propName: string, defaultValue: T): SubscribedAbstractProperty<T>--><!--Device-AppStorage-static setAndProp<T>(propName: string, defaultValue: T): SubscribedAbstractProperty<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| propName | string | Yes |
| defaultValue | T | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SubscribedAbstractProperty](arkts-arkui-subscribedabstractproperty-c.md)&lt;T&gt; |

**Examples**

```TypeScript
AppStorage.setOrCreate('PropA', 47);
let prop: SubscribedAbstractProperty<number> = AppStorage.setAndProp('PropB', 49); // PropA -> 47, PropB -> 49
```

## setAndRef

```TypeScript
static setAndRef<T>(propName: string, defaultValue: T): AbstractProperty<T>
```

Similar to the [ref](#ref) API, returns a reference to the property corresponding to **propName** in [AppStorage](../../../ui/state-management/arkts-appstorage.md). If the given property does not exist, this API creates and initializes the property in AppStorage using **defaultValue** and returns its reference. This API is similar to [setAndLink](#setandlink) but does not require manually releasing the returned variable of the [AbstractProperty](arkts-arkui-abstractproperty-i.md#abstractproperty) type. > **NOTE：**> Since API version 12, AppStorage supports > [Map](../../../ui/state-management/arkts-appstorage.md#decorating-variables-of-the-map-type), > [Set](../../../ui/state-management/arkts-appstorage.md#decorating-variables-of-the-set-type), > [Date](../../../ui/state-management/arkts-appstorage.md#decorating-variables-of-the-date-type), **null**, > **undefined**, and [union](../../../ui/state-management/arkts-appstorage.md#using-union-types-in-appstorage) > types.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AppStorage-static setAndRef<T>(propName: string, defaultValue: T): AbstractProperty<T>--><!--Device-AppStorage-static setAndRef<T>(propName: string, defaultValue: T): AbstractProperty<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| propName | string | Yes |
| defaultValue | T | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [AbstractProperty](arkts-arkui-abstractproperty-i.md)&lt;T&gt; |

**Examples**

```TypeScript
AppStorage.setOrCreate('PropA', 47);
let ref1: AbstractProperty<number> = AppStorage.setAndRef('PropB', 49); // Create PropB with the default value 49.
let ref2: AbstractProperty<number> = AppStorage.setAndRef('PropA', 50); // PropA already exists with the value 47.
```

## setOrCreate

```TypeScript
static setOrCreate<T>(propName: string, newValue: T): void
```

Sets the value of the property corresponding to **propName** in [AppStorage](../../../ui/state-management/arkts-appstorage.md) to a new value, if the property exists and the new value is different from the current value. If the new value is the same as the current value of the property, no assignment is performed, and the state variable does not instruct the UI to update the value of the property. If the property does not exist, this API creates it with the value of **newValue**. This **setOrCreate** API can create only one AppStorage key-value pair each time. To create multiple key-value pairs, call this API multiple times. > **NOTE：**> Since API version 12, AppStorage supports > [Map](../../../ui/state-management/arkts-appstorage.md#decorating-variables-of-the-map-type), > [Set](../../../ui/state-management/arkts-appstorage.md#decorating-variables-of-the-set-type), > [Date](../../../ui/state-management/arkts-appstorage.md#decorating-variables-of-the-date-type), **null**, > **undefined**, and [union](../../../ui/state-management/arkts-appstorage.md#using-union-types-in-appstorage) > types.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AppStorage-static setOrCreate<T>(propName: string, newValue: T): void--><!--Device-AppStorage-static setOrCreate<T>(propName: string, newValue: T): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| propName | string | Yes |
| newValue | T | Yes |

**Examples**

```TypeScript
AppStorage.setOrCreate('simpleProp', 121);
```

## size

```TypeScript
static size(): number
```

Obtains the number of properties in [AppStorage](../../../ui/state-management/arkts-appstorage.md).

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AppStorage-static size(): number--><!--Device-AppStorage-static size(): number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Examples**

```TypeScript
AppStorage.setOrCreate('PropB', 48);
let res: number = AppStorage.size(); // 1
```

## staticClear

```TypeScript
static staticClear(): boolean
```

Deletes all properties.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [Clear](#clear)

<!--Device-AppStorage-static staticClear(): boolean--><!--Device-AppStorage-static staticClear(): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Examples**

```TypeScript
let clearResult = AppStorage.staticClear();
```

```TypeScript
AppStorage.SetOrCreate('PropA', 47);
let res: boolean = AppStorage.Clear(); // true: There are no subscribers.
```
