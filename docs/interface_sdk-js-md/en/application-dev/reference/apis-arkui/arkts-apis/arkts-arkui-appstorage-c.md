# AppStorage

For details about how to use AppStorage, see [AppStorage: Storing Application-wide UI State](../../../ui/state-management/arkts-appstorage.md).

**Since:** 7

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## Clear

```TypeScript
static Clear(): boolean
```

Deletes all properties from [AppStorage](../../../ui/state-management/arkts-appstorage.md). The deletion is only successful if none of the properties in AppStorage have any subscribers. If there are subscribers, this API does not take effect and **false** is returned. If there are no subscribers, the deletion is successful and **true** is returned.For details about the subscriber, see [delete](#delete).

**Since:** 9

**Deprecated since:** 10

**Substitutes:** [clear](#clear)

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## clear

```TypeScript
static clear(): boolean
```

Deletes all properties from [AppStorage](../../../ui/state-management/arkts-appstorage.md). The deletion is only successful if none of the properties in AppStorage have any subscribers. If there are subscribers, this API does not take effect and **false** is returned. If there are no subscribers, the deletion is successful and **true** is returned.For details about the subscriber, see [delete](#delete).

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## Delete

```TypeScript
static Delete(propName: string): boolean
```

Deletes the property corresponding to **propName** from [AppStorage](../../../ui/state-management/arkts-appstorage.md).The deletion is only successful if the property has no subscribers. If there is a subscriber, the deletion fails and **false** is returned. If there are no subscribers, the deletion is successful and **true** is returned.Subscribers include properties bound using [Link](#link) and [Prop](#prop) APIs, as well as those decorated with [\@StorageLink('propName')](../../../ui/state-management/arkts-appstorage.md#storagelink) and [\@StorageProp('propName')](../../../ui/state-management/arkts-appstorage.md#storageprop). This means that if \@StorageLink('propName') and \@StorageProp('propName') are used in a custom component or if there is still a **SubscribedAbstractProperty** instance in a synchronization relationship with the property, the property cannot be deleted from AppStorage.

**Since:** 7

**Deprecated since:** 10

**Substitutes:** [delete](#delete)

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| propName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## delete

```TypeScript
static delete(propName: string): boolean
```

Deletes the property corresponding to **propName** from [AppStorage](../../../ui/state-management/arkts-appstorage.md).The deletion is only successful if the property has no subscribers. If there is a subscriber, the deletion fails and **false** is returned. If there are no subscribers, the deletion is successful and **true** is returned.The property subscribers include the following:
1. Variables decorated by [\@StorageLink](../../../ui/state-management/arkts-appstorage.md#storagelink) or  
[\@StorageProp](../../../ui/state-management/arkts-appstorage.md#storageprop)
2. Instances of [SubscribedAbstractProperty](arkts-arkui-subscribedabstractproperty-c.md) returned by  
[link](#link), [prop](#prop), [setAndLink](#setandlink), or [setAndProp](#setandprop)To delete these subscribers:
1. Remove the custom component containing \@StorageLink or \@StorageProp. For details, see  
[Custom Component Deletion](../../../ui/state-management/arkts-page-custom-components-lifecycle.md#custom-component-deletion).
2. Call the [aboutToBeDeleted](arkts-arkui-subscribedabstractproperty-c.md#abouttobedeleted) API on instances of  
**SubscribedAbstractProperty** returned by **link**, **prop**, **setAndLink**, or **setAndProp**.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| propName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## Get

```TypeScript
static Get<T>(propName: string): T | undefined
```

Obtains the value of the property corresponding to **propName** from [AppStorage](../../../ui/state-management/arkts-appstorage.md). If the property does not exist, this API returns **undefined**.

**Since:** 7

**Deprecated since:** 10

**Substitutes:** [get](#get)

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| propName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T \| undefined |

## get

```TypeScript
static get<T>(propName: string): T | undefined
```

Obtains the value of the property corresponding to **propName** from [AppStorage](../../../ui/state-management/arkts-appstorage.md). If the property does not exist, this API returns **undefined**.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| propName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T \| undefined |

## Has

```TypeScript
static Has(propName: string): boolean
```

Checks whether the property corresponding to **propName** exists in [AppStorage](../../../ui/state-management/arkts-appstorage.md).

**Since:** 7

**Deprecated since:** 10

**Substitutes:** [has](#has)

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| propName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## has

```TypeScript
static has(propName: string): boolean
```

Checks whether the property corresponding to **propName** exists in [AppStorage](../../../ui/state-management/arkts-appstorage.md).

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| propName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## IsMutable

```TypeScript
static IsMutable(propName: string): boolean
```

Checks whether the property corresponding to **propName** in [AppStorage](../../../ui/state-management/arkts-appstorage.md) is mutable.

**Since:** 7

**Deprecated since:** 10

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| propName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## Keys

```TypeScript
static Keys(): IterableIterator<string>
```

Obtains all property names in [AppStorage](../../../ui/state-management/arkts-appstorage.md).

**Since:** 7

**Deprecated since:** 10

**Substitutes:** [keys](#keys)

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [IterableIterator](../../apis-default/arkts-apis/arkts-lib-es2015-iterable-iterableiterator-i.md)&lt;string&gt; |

## keys

```TypeScript
static keys(): IterableIterator<string>
```

Obtains all property names in [AppStorage](../../../ui/state-management/arkts-appstorage.md).

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [IterableIterator](../../apis-default/arkts-apis/arkts-lib-es2015-iterable-iterableiterator-i.md)&lt;string&gt; |

## Link

```TypeScript
static Link(propName: string): any
```

Establishes a two-way data binding with the property corresponding to **propName** in [AppStorage](../../../ui/state-management/arkts-appstorage.md). If the given property exists in AppStorage, the two-way bound data of the property in AppStorage is returned.Any update of the data is synchronized back to AppStorage, which then synchronizes the update to all data and custom components bound to the property.If the given property does not exist in AppStorage, **undefined** is returned.

**Since:** 7

**Deprecated since:** 10

**Substitutes:** [link](#link)

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| propName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| any |

## link

```TypeScript
static link<T>(propName: string): SubscribedAbstractProperty<T>
```

Establishes a two-way data binding with the property corresponding to **propName** in [AppStorage](../../../ui/state-management/arkts-appstorage.md). If the given property exists in AppStorage, the two-way bound data of the property in AppStorage is returned.Any update of the data is synchronized back to AppStorage, which then synchronizes the update to all data and custom components bound to the property.If the given property does not exist in AppStorage, **undefined** is returned.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| propName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SubscribedAbstractProperty](arkts-arkui-subscribedabstractproperty-c.md)&lt;T&gt; |

## Prop

```TypeScript
static Prop(propName: string): any
```

Establishes a one-way data binding with the property corresponding to **propName** in [AppStorage](../../../ui/state-management/arkts-appstorage.md). If the given property exists in AppStorage, the one-way bound data of the property in AppStorage is returned. If the given property does not exist in AppStorage, **undefined** is returned. Updates of the one-way bound data are not synchronized back to AppStorage.

> **NOTE：**

> Prop supports only simple types.

**Since:** 7

**Deprecated since:** 10

**Substitutes:** [prop](#prop)

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| propName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| any |

## prop

```TypeScript
static prop<T>(propName: string): SubscribedAbstractProperty<T>
```

Establishes a one-way data binding with the property corresponding to **propName** in [AppStorage](../../../ui/state-management/arkts-appstorage.md). If the given property exists in AppStorage, the one-way bound data of the property in AppStorage is returned. If the given property does not exist in AppStorage, **undefined** is returned. Updates of the one-way bound data are not synchronized back to AppStorage.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| propName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SubscribedAbstractProperty](arkts-arkui-subscribedabstractproperty-c.md)&lt;T&gt; |

## ref

```TypeScript
static ref<T>(propName: string): AbstractProperty<T> | undefined
```

Returns a reference to the property corresponding to **propName** in [AppStorage](../../../ui/state-management/arkts-appstorage.md). If the provided **propName** does not exist, this API returns **undefined**.This API is similar to [link](#link) but does not require manually releasing the returned variable of the [AbstractProperty](arkts-arkui-abstractproperty-i.md) type.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| propName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [AbstractProperty](arkts-arkui-abstractproperty-i.md)&lt;T&gt; \| undefined |

## Set

```TypeScript
static Set<T>(propName: string, newValue: T): boolean
```

Sets the value of the property corresponding to **propName** in [AppStorage](../../../ui/state-management/arkts-appstorage.md). If the value of **newValue** is the same as the current value of the property, no assignment is performed, and the state variable does not instruct the UI to update the value of the property. Starting from API version 12, **newValue** can be **null** or **undefined**.

**Since:** 7

**Deprecated since:** 10

**Substitutes:** [set](#set)

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

## set

```TypeScript
static set<T>(propName: string, newValue: T): boolean
```

Sets the value of the property corresponding to **propName** in [AppStorage](../../../ui/state-management/arkts-appstorage.md). If the value of **newValue** is the same as the current value of the property, no assignment is performed, and the state variable does not instruct the UI to update the value of the property.

> **NOTE：**

> Since API version 12, AppStorage supports
> [Map](../../../ui/state-management/arkts-appstorage.md#decorating-variables-of-the-map-type),
> [Set](../../../ui/state-management/arkts-appstorage.md#decorating-variables-of-the-set-type),
> [Date](../../../ui/state-management/arkts-appstorage.md#decorating-variables-of-the-date-type), **null**,
> **undefined**, and [union](../../../ui/state-management/arkts-appstorage.md#using-union-types-in-appstorage)
> types.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

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

## SetAndLink

```TypeScript
static SetAndLink<T>(propName: string, defaultValue: T): SubscribedAbstractProperty<T>
```

Similar to the [Link](#link) API, establishes a two-way data binding with the property corresponding to **propName** in [AppStorage](../../../ui/state-management/arkts-appstorage.md). If the given property exists in AppStorage, this API returns the two-way bound data for the property. If the given property does not exist, this API creates and initializes the property in AppStorage using **defaultValue** and returns its two- way bound data. The value of **defaultValue** must be of the **T** type and cannot be **null** or **undefined**.

**Since:** 7

**Deprecated since:** 10

**Substitutes:** [setAndLink](#setandlink)

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

## setAndLink

```TypeScript
static setAndLink<T>(propName: string, defaultValue: T): SubscribedAbstractProperty<T>
```

Similar to the [link](#link) API, establishes a two-way data binding with the property corresponding to **propName** in [AppStorage](../../../ui/state-management/arkts-appstorage.md). If the given property exists in AppStorage, this API returns the two-way bound data for the property. If the given property does not exist, this API creates and initializes the property in AppStorage using **defaultValue** and returns its two- way bound data.

> **NOTE：**

> Since API version 12, AppStorage supports
> [Map](../../../ui/state-management/arkts-appstorage.md#decorating-variables-of-the-map-type),
> [Set](../../../ui/state-management/arkts-appstorage.md#decorating-variables-of-the-set-type),
> [Date](../../../ui/state-management/arkts-appstorage.md#decorating-variables-of-the-date-type), **null**,
> **undefined**, and [union](../../../ui/state-management/arkts-appstorage.md#using-union-types-in-appstorage)
> types.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

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

## SetAndProp

```TypeScript
static SetAndProp<S>(propName: string, defaultValue: S): SubscribedAbstractProperty<S>
```

Similar to the [Prop](#prop) API, establishes a one-way data binding with the property corresponding to **propName** in [AppStorage](../../../ui/state-management/arkts-appstorage.md). If the given property exists in AppStorage, this API returns the one-way bound data for the property. If the given property does not exist, this API creates and initializes the property in AppStorage using **defaultValue** and returns its one- way bound data. The value of **defaultValue** must be of the **S** type and cannot be **null** or **undefined**.

**Since:** 7

**Deprecated since:** 10

**Substitutes:** [setAndProp](#setandprop)

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

## setAndProp

```TypeScript
static setAndProp<T>(propName: string, defaultValue: T): SubscribedAbstractProperty<T>
```

Similar to the [prop](#prop) API, establishes a one-way data binding with the property corresponding to **propName** in [AppStorage](../../../ui/state-management/arkts-appstorage.md). If the given property exists in AppStorage, this API returns the one-way bound data for the property. If the given property does not exist, this API creates and initializes the property in AppStorage using **defaultValue** and returns its one- way bound data.

> **NOTE：**

> Since API version 12, AppStorage supports
> [Map](../../../ui/state-management/arkts-appstorage.md#decorating-variables-of-the-map-type),
> [Set](../../../ui/state-management/arkts-appstorage.md#decorating-variables-of-the-set-type),
> [Date](../../../ui/state-management/arkts-appstorage.md#decorating-variables-of-the-date-type), **null**,
> **undefined**, and [union](../../../ui/state-management/arkts-appstorage.md#using-union-types-in-appstorage)
> types.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

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

## setAndRef

```TypeScript
static setAndRef<T>(propName: string, defaultValue: T): AbstractProperty<T>
```

Similar to the [ref](#ref) API, returns a reference to the property corresponding to **propName** in [AppStorage](../../../ui/state-management/arkts-appstorage.md). If the given property does not exist, this API creates and initializes the property in AppStorage using **defaultValue** and returns its reference.This API is similar to [setAndLink](#setandlink) but does not require manually releasing the returned variable of the [AbstractProperty](arkts-arkui-abstractproperty-i.md) type.

> **NOTE：**

> Since API version 12, AppStorage supports
> [Map](../../../ui/state-management/arkts-appstorage.md#decorating-variables-of-the-map-type),
> [Set](../../../ui/state-management/arkts-appstorage.md#decorating-variables-of-the-set-type),
> [Date](../../../ui/state-management/arkts-appstorage.md#decorating-variables-of-the-date-type), **null**,
> **undefined**, and [union](../../../ui/state-management/arkts-appstorage.md#using-union-types-in-appstorage)
> types.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

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

## SetOrCreate

```TypeScript
static SetOrCreate<T>(propName: string, newValue: T): void
```

Sets the value of the property corresponding to **propName** in [AppStorage](../../../ui/state-management/arkts-appstorage.md) to a new value, if the property exists. If the property does not exist, this API creates it with the value of **newValue**.The value of **newValue** cannot be **null** or **undefined**.

**Since:** 7

**Deprecated since:** 10

**Substitutes:** [setOrCreate](#setorcreate)

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| propName | string | Yes |
| newValue | T | Yes |

## setOrCreate

```TypeScript
static setOrCreate<T>(propName: string, newValue: T): void
```

Sets the value of the property corresponding to **propName** in [AppStorage](../../../ui/state-management/arkts-appstorage.md) to a new value, if the property exists and the new value is different from the current value. If the new value is the same as the current value of the property, no assignment is performed, and the state variable does not instruct the UI to update the value of the property.If the property does not exist, this API creates it with the value of **newValue**. This **setOrCreate** API can create only one AppStorage key-value pair each time. To create multiple key-value pairs, call this API multiple times.

> **NOTE：**

> Since API version 12, AppStorage supports
> [Map](../../../ui/state-management/arkts-appstorage.md#decorating-variables-of-the-map-type),
> [Set](../../../ui/state-management/arkts-appstorage.md#decorating-variables-of-the-set-type),
> [Date](../../../ui/state-management/arkts-appstorage.md#decorating-variables-of-the-date-type), **null**,
> **undefined**, and [union](../../../ui/state-management/arkts-appstorage.md#using-union-types-in-appstorage)
> types.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| propName | string | Yes |
| newValue | T | Yes |

## Size

```TypeScript
static Size(): number
```

Obtains the number of properties in [AppStorage](../../../ui/state-management/arkts-appstorage.md).

**Since:** 7

**Deprecated since:** 10

**Substitutes:** [size](#size)

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## size

```TypeScript
static size(): number
```

Obtains the number of properties in [AppStorage](../../../ui/state-management/arkts-appstorage.md).

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## staticClear

```TypeScript
static staticClear(): boolean
```

Deletes all properties.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [Clear](#clear)

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |
