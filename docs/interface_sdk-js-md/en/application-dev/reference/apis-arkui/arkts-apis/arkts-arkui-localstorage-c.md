# LocalStorage

For details about how to use LocalStorage on the UI, see [LocalStorage: UI State Storage](../../../ui/state-management/arkts-localstorage.md).

**Since:** 9

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## clear

```TypeScript
clear(): boolean
```

Deletes all properties from [LocalStorage](../../../ui/state-management/arkts-localstorage.md). The deletion is only successful if none of the properties in LocalStorage have any subscribers. If there are subscribers, this API does not take effect and **false** is returned. If there are no subscribers, the deletion is successful and **true** is returned.For details about the subscriber, see [delete](#delete).

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## constructor

```TypeScript
constructor(initializingProperties?: Object)
```

Creates a [LocalStorage](../../../ui/state-management/arkts-localstorage.md) instance and initializes it using the properties and values returned by **Object.keys(initializingProperties)**.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| initializingProperties | Object | No |

## delete

```TypeScript
delete(propName: string): boolean
```

Deletes the property corresponding to **propName** from [LocalStorage](../../../ui/state-management/arkts-localstorage.md). The deletion is only successful if the property has no subscribers. If there is a subscriber, the deletion fails and **false** is returned. If there are no subscribers, the deletion is successful and **true** is returned.The property subscribers include the following:
1. Variables decorated by  
[\@LocalStorageLink](../../../ui/state-management/arkts-localstorage.md#localstoragelink) or [\@LocalStorageProp](../../../ui/state-management/arkts-localstorage.md#localstorageprop)
2. Instances of [SubscribedAbstractProperty](arkts-arkui-subscribedabstractproperty-c.md)
returned by [link](#link), [prop](#prop), [setAndLink](#setandlink), or [setAndProp](#setandprop)To delete these subscribers:
1. Remove the custom component containing \@LocalStorageLink or \@LocalStorageProp.
For details, see [Custom Component Deletion](../../../ui/state-management/arkts-page-custom-components-lifecycle.md#custom-component-deletion).
2. Call the [aboutToBeDeleted](arkts-arkui-subscribedabstractproperty-c.md#abouttobedeleted) API on instances
of **SubscribedAbstractProperty** returned by **link**, **prop**, **setAndLink**, or **setAndProp**.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| propName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## get

```TypeScript
get<T>(propName: string): T | undefined
```

Obtains the value of the property corresponding to **propName** from [LocalStorage](../../../ui/state-management/arkts-localstorage.md).

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| propName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T \| undefined |

## GetShared

```TypeScript
static GetShared(): LocalStorage
```

Obtains the [LocalStorage](../../../ui/state-management/arkts-localstorage.md) instance shared across the current stage.

**Since:** 9

**Deprecated since:** 10

**Substitutes:** [getShared](#getshared)

**Model restriction:** This API can be used only in the stage model.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [LocalStorage](arkts-arkui-localstorage-c.md) |

## getShared

```TypeScript
static getShared(): LocalStorage
```

Obtains the [LocalStorage](../../../ui/state-management/arkts-localstorage.md) instance shared across the current stage.

> **NOTE：**

> Since API version 12, you can use the
> [getSharedLocalStorage](arkts-arkui-arkui-uicontext-uicontext-c.md#getsharedlocalstorage)
> API in [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) to specify the UI execution context.

**Since:** 10

**Deprecated since:** 18

**Substitutes:** [getSharedLocalStorage](arkts-arkui-arkui-uicontext-uicontext-c.md#getsharedlocalstorage)

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 10.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [LocalStorage](arkts-arkui-localstorage-c.md) |

## has

```TypeScript
has(propName: string): boolean
```

Checks whether the property corresponding to **propName** exists in [LocalStorage](../../../ui/state-management/arkts-localstorage.md).

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| propName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## keys

```TypeScript
keys(): IterableIterator<string>
```

Obtains all property names in [LocalStorage](../../../ui/state-management/arkts-localstorage.md).

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [IterableIterator](../../apis-default/arkts-apis/arkts-lib-es2015-iterable-iterableiterator-i.md)&lt;string&gt; |

## link

```TypeScript
link<T>(propName: string): SubscribedAbstractProperty<T>
```

Establishes a two-way data binding with the property corresponding to **propName** in [LocalStorage](../../../ui/state-management/arkts-localstorage.md). If the given property exists in LocalStorage, this API returns the two-way bound data for the property.Any update of the data is synchronized back to LocalStorage, which then synchronizes the update to all data and components bound to the property.If the given property does not exist in LocalStorage, **undefined** is returned.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| propName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SubscribedAbstractProperty](arkts-arkui-subscribedabstractproperty-c.md)&lt;T&gt; |

## prop

```TypeScript
prop<S>(propName: string): SubscribedAbstractProperty<S>
```

Establishes a one-way data binding with the property corresponding to **propName** in [LocalStorage](../../../ui/state-management/arkts-localstorage.md). If the given property exists in LocalStorage, this API returns the one-way bound data for the property. If the given property does not exist in LocalStorage, **undefined** is returned. Updates of the one-way bound data are not synchronized back to LocalStorage.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| propName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SubscribedAbstractProperty](arkts-arkui-subscribedabstractproperty-c.md)&lt;S&gt; |

## ref

```TypeScript
public ref<T>(propName: string): AbstractProperty<T> | undefined
```

Returns a reference to the property corresponding to **propName** in [LocalStorage](../../../ui/state-management/arkts-localstorage.md). If the provided **propName** does not exist, this API returns **undefined**.This API is similar to [link](#link) but does not require manually releasing the returned variable of the [AbstractProperty](arkts-arkui-abstractproperty-i.md) type.

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

## set

```TypeScript
set<T>(propName: string, newValue: T): boolean
```

Sets the value of the property corresponding to **propName** in [LocalStorage](../../../ui/state-management/arkts-localstorage.md). If the value of **newValue** is the same as the current value of the property, no assignment is performed, and the state variable does not instruct the UI to update the value of the property.

> **NOTE：**

> Since API version 12, LocalStorage supports
> [Map](../../../ui/state-management/arkts-localstorage.md#decorating-variables-of-the-map-type),
> [Set](../../../ui/state-management/arkts-localstorage.md#decorating-variables-of-the-set-type),
> [Date](../../../ui/state-management/arkts-localstorage.md#decorating-variables-of-the-date-type), **null**,
> **undefined**, and [union](../../../ui/state-management/arkts-localstorage.md#using-union-types-in-localstorage)
> types.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

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

## setAndLink

```TypeScript
setAndLink<T>(propName: string, defaultValue: T): SubscribedAbstractProperty<T>
```

Similar to the [link](#link) API, establishes a two-way data binding with the property corresponding to **propName** in [LocalStorage](../../../ui/state-management/arkts-localstorage.md). If the given property exists in LocalStorage, this API returns the two-way bound data for the property. If the given property does not exist, this API creates and initializes the property in LocalStorage using **defaultValue** and returns its two-way bound data.

> **NOTE：**

> Since API version 12, LocalStorage supports
> [Map](../../../ui/state-management/arkts-localstorage.md#decorating-variables-of-the-map-type),
> [Set](../../../ui/state-management/arkts-localstorage.md#decorating-variables-of-the-set-type),
> [Date](../../../ui/state-management/arkts-localstorage.md#decorating-variables-of-the-date-type), **null**,
> **undefined**, and [union](../../../ui/state-management/arkts-localstorage.md#using-union-types-in-localstorage)
> types.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

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

## setAndProp

```TypeScript
setAndProp<S>(propName: string, defaultValue: S): SubscribedAbstractProperty<S>
```

Similar to the [prop](#prop) API, establishes a one-way data binding with the property corresponding to **propName** in [LocalStorage](../../../ui/state-management/arkts-localstorage.md). If the given property exists in LocalStorage, this API returns the one-way bound data for the property. If the given property does not exist, this API creates and initializes the property in LocalStorage using **defaultValue** and returns its one-way bound data.

> **NOTE：**

> Since API version 12, LocalStorage supports
> [Map](../../../ui/state-management/arkts-localstorage.md#decorating-variables-of-the-map-type),
> [Set](../../../ui/state-management/arkts-localstorage.md#decorating-variables-of-the-set-type),
> [Date](../../../ui/state-management/arkts-localstorage.md#decorating-variables-of-the-date-type), **null**,
> **undefined**, and [union](../../../ui/state-management/arkts-localstorage.md#using-union-types-in-localstorage)
> types.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

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

## setAndRef

```TypeScript
public setAndRef<T>(propName: string, defaultValue: T): AbstractProperty<T>
```

Similar to the [ref](arkts-arkui-appstorage-c.md#ref) API, returns a reference to the property corresponding to **propName** in [LocalStorage](../../../ui/state-management/arkts-localstorage.md). If the given property does not exist, this API creates and initializes the property in LocalStorage using **defaultValue** and returns its reference.This API is similar to [setAndLink](#setandlink) but does not require manually releasing the returned variable of the [AbstractProperty](arkts-arkui-abstractproperty-i.md) type.

> **NOTE：**

> Since API version 12, LocalStorage supports
> [Map](../../../ui/state-management/arkts-localstorage.md#decorating-variables-of-the-map-type),
> [Set](../../../ui/state-management/arkts-localstorage.md#decorating-variables-of-the-set-type),
> [Date](../../../ui/state-management/arkts-localstorage.md#decorating-variables-of-the-date-type), **null**,
> **undefined**, and [union](../../../ui/state-management/arkts-localstorage.md#using-union-types-in-localstorage)
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

## setOrCreate

```TypeScript
setOrCreate<T>(propName: string, newValue: T): boolean
```

Sets the value of the property corresponding to **propName** in [LocalStorage](../../../ui/state-management/arkts-localstorage.md) to a new value, if the property exists and the new value is different from the current value. If the new value is the same as the current value of the property, no assignment is performed, and the state variable does not instruct the UI to update the value of the property.If the property does not exist, this API creates it with the value of **newValue**. This **setOrCreate** API can create only one LocalStorage key-value pair each time. To create multiple key-value pairs, call this API multiple times.

> **NOTE：**

> Since API version 12, LocalStorage supports
> [Map](../../../ui/state-management/arkts-localstorage.md#decorating-variables-of-the-map-type),
> [Set](../../../ui/state-management/arkts-localstorage.md#decorating-variables-of-the-set-type),
> [Date](../../../ui/state-management/arkts-localstorage.md#decorating-variables-of-the-date-type), **null**,
> **undefined**, and [union](../../../ui/state-management/arkts-localstorage.md#using-union-types-in-localstorage)
> types.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

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

## size

```TypeScript
size(): number
```

Obtains the number of properties in [LocalStorage](../../../ui/state-management/arkts-localstorage.md).

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |
