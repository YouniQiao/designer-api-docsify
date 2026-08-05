# AppStorage

For details about how to use AppStorage, see \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

<!--Device-unnamed-declare class AppStorage--><!--Device-unnamed-declare class AppStorage-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Clear

```TypeScript
static Clear(): boolean
```

Deletes all properties from \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_. The deletion is only successful if none of the properties in AppStorage have any subscribers. If there are subscribers, this API does not take effect and **false** is returned. If there are no subscribers, the deletion is successful and **true** is returned. For details about the subscriber, see [delete]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 10

**Substitutes:** [AppStorage#clear](arkts-arkui-appstorage-c.md#clear)

<!--Device-AppStorage-static Clear(): boolean--><!--Device-AppStorage-static Clear(): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns **true** if the operation is successful; returns **false** otherwise. |

## Delete

```TypeScript
static Delete(propName: string): boolean
```

Deletes the property corresponding to **propName** from \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_. The deletion is only successful if the property has no subscribers. If there is a subscriber, the deletion fails and **false** is returned. If there are no subscribers, the deletion is successful and **true** is returned. Subscribers include properties bound using [Link]\_\_\_JSDOC\_LINK\_DESC\_USD\_3\_\_\_ and [Prop]\_\_\_JSDOC\_LINK\_DESC\_USD\_4\_\_\_ APIs, as well as those decorated with \_\_\_MD\_LINK\_DESC\_USD\_1\_\_\_ and \_\_\_MD\_LINK\_DESC\_USD\_2\_\_\_. This means that if \@StorageLink('propName') and \@StorageProp('propName') are used in a custom component or if there is still a **SubscribedAbstractProperty** instance in a synchronization relationship with the property, the property cannot be deleted from AppStorage.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 10

**Substitutes:** [AppStorage#delete](arkts-arkui-appstorage-c.md#delete)

<!--Device-AppStorage-static Delete(propName: string): boolean--><!--Device-AppStorage-static Delete(propName: string): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| propName | string | Yes | Property name in AppStorage. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns **true** if the operation is successful; returns **false** if the operation fails. |

## Get

```TypeScript
static Get<T>(propName: string): T | undefined
```

Obtains the value of the property corresponding to **propName** from \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_. If the property does not exist, this API returns **undefined**.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 10

**Substitutes:** [AppStorage#get](arkts-arkui-appstorage-c.md#get)

<!--Device-AppStorage-static Get<T>(propName: string): T | undefined--><!--Device-AppStorage-static Get<T>(propName: string): T | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| propName | string | Yes | Property name in AppStorage. |

**Return value:**

| Type | Description |
| --- | --- |
| T | Value of the property corresponding to **propName** in AppStorage, or **undefined** if |

## Has

```TypeScript
static Has(propName: string): boolean
```

Checks whether the property corresponding to **propName** exists in \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 10

**Substitutes:** [AppStorage#has](arkts-arkui-appstorage-c.md#has)

<!--Device-AppStorage-static Has(propName: string): boolean--><!--Device-AppStorage-static Has(propName: string): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| propName | string | Yes | Property name in AppStorage. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns **true** if the property exists in AppStorage; returns **false** otherwise. |

## IsMutable

```TypeScript
static IsMutable(propName: string): boolean
```

Checks whether the property corresponding to **propName** in \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_ is mutable.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 10

<!--Device-AppStorage-static IsMutable(propName: string): boolean--><!--Device-AppStorage-static IsMutable(propName: string): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| propName | string | Yes | Property name in AppStorage. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Whether the property corresponding to **propName** is mutable. Currently, this return value is |

## Keys

```TypeScript
static Keys(): IterableIterator<string>
```

Obtains all property names in \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 10

**Substitutes:** [AppStorage#keys](arkts-arkui-appstorage-c.md#keys)

<!--Device-AppStorage-static Keys(): IterableIterator<string>--><!--Device-AppStorage-static Keys(): IterableIterator<string>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;string&gt; | All property names in AppStorage. |

## Link

```TypeScript
static Link(propName: string): any
```

Establishes a two-way data binding with the property corresponding to **propName** in \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_. If the given property exists in AppStorage, the two-way bound data of the property in AppStorage is returned. Any update of the data is synchronized back to AppStorage, which then synchronizes the update to all data and custom components bound to the property. If the given property does not exist in AppStorage, **undefined** is returned.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 10

**Substitutes:** [AppStorage#link](arkts-arkui-appstorage-c.md#link)

<!--Device-AppStorage-static Link(propName: string): any--><!--Device-AppStorage-static Link(propName: string): any-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| propName | string | Yes | Property name in AppStorage. |

**Return value:**

| Type | Description |
| --- | --- |
| any | Two-way bound data of the specified property in AppStorage, or **undefined** if the property does |

## Prop

```TypeScript
static Prop(propName: string): any
```

Establishes a one-way data binding with the property corresponding to **propName** in \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_. If the given property exists in AppStorage, the one-way bound data of the property in AppStorage is returned. If the given property does not exist in AppStorage, **undefined** is returned. Updates of the one-way bound data are not synchronized back to AppStorage. > **NOTE** > Prop supports only simple types.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 10

**Substitutes:** [AppStorage#prop](arkts-arkui-appstorage-c.md#prop)

<!--Device-AppStorage-static Prop(propName: string): any--><!--Device-AppStorage-static Prop(propName: string): any-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| propName | string | Yes | Property name in AppStorage. |

**Return value:**

| Type | Description |
| --- | --- |
| any | One-way bound data of the specified property in AppStorage, or **undefined** if the property does |

## Set

```TypeScript
static Set<T>(propName: string, newValue: T): boolean
```

Sets the value of the property corresponding to **propName** in \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_. If the value of **newValue** is the same as the current value of the property, no assignment is performed, and the state variable does not instruct the UI to update the value of the property. Starting from API version 12, **newValue** can be **null** or **undefined**.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 10

**Substitutes:** [AppStorage#set](arkts-arkui-appstorage-c.md#set)

<!--Device-AppStorage-static Set<T>(propName: string, newValue: T): boolean--><!--Device-AppStorage-static Set<T>(propName: string, newValue: T): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| propName | string | Yes | Property name in AppStorage. |
| newValue | T | Yes | Property value. Since API version 12, the value can be **null** or **undefined**. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns **false** if the property corresponding to **propName** does not exist in AppStorage. |

## SetAndLink

```TypeScript
static SetAndLink<T>(propName: string, defaultValue: T): SubscribedAbstractProperty<T>
```

Similar to the [Link]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ API, establishes a two-way data binding with the property corresponding to **propName** in \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_. If the given property exists in AppStorage, this API returns the two-way bound data for the property. If the given property does not exist, this API creates and initializes the property in AppStorage using **defaultValue** and returns its two- way bound data. The value of **defaultValue** must be of the **T** type and cannot be **null** or **undefined**.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 10

**Substitutes:** [AppStorage#setAndLink](arkts-arkui-appstorage-c.md#setandlink)

<!--Device-AppStorage-static SetAndLink<T>(propName: string, defaultValue: T): SubscribedAbstractProperty<T>--><!--Device-AppStorage-static SetAndLink<T>(propName: string, defaultValue: T): SubscribedAbstractProperty<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| propName | string | Yes | Property name in AppStorage. |
| defaultValue | T | Yes | Default value used to initialize the property corresponding to **propName** in AppStorage if **propName** does not exist. The value cannot be **null** or **undefined**. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;T&gt; | Instance of **SubscribedAbstractProperty\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_** and two-way bound data of |

## SetAndProp

```TypeScript
static SetAndProp<S>(propName: string, defaultValue: S): SubscribedAbstractProperty<S>
```

Similar to the [Prop]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ API, establishes a one-way data binding with the property corresponding to **propName** in \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_. If the given property exists in AppStorage, this API returns the one-way bound data for the property. If the given property does not exist, this API creates and initializes the property in AppStorage using **defaultValue** and returns its one- way bound data. The value of **defaultValue** must be of the **S** type and cannot be **null** or **undefined**.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 10

**Substitutes:** [AppStorage#setAndProp](arkts-arkui-appstorage-c.md#setandprop)

<!--Device-AppStorage-static SetAndProp<S>(propName: string, defaultValue: S): SubscribedAbstractProperty<S>--><!--Device-AppStorage-static SetAndProp<S>(propName: string, defaultValue: S): SubscribedAbstractProperty<S>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| propName | string | Yes | Property name in AppStorage. |
| defaultValue | S | Yes | Default value used to initialize the property corresponding to **propName** in AppStorage if **propName** does not exist. The value cannot be **null** or **undefined**. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;S&gt; | Instance of **SubscribedAbstractProperty\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_**. |

## SetOrCreate

```TypeScript
static SetOrCreate<T>(propName: string, newValue: T): void
```

Sets the value of the property corresponding to **propName** in \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_ to a new value, if the property exists. If the property does not exist, this API creates it with the value of **newValue**. The value of **newValue** cannot be **null** or **undefined**.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 10

**Substitutes:** [AppStorage#setOrCreate](arkts-arkui-appstorage-c.md#setorcreate)

<!--Device-AppStorage-static SetOrCreate<T>(propName: string, newValue: T): void--><!--Device-AppStorage-static SetOrCreate<T>(propName: string, newValue: T): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| propName | string | Yes | Property name in AppStorage. |
| newValue | T | Yes | Property value, which cannot be **null** or **undefined**. |

## Size

```TypeScript
static Size(): number
```

Obtains the number of properties in \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 10

**Substitutes:** [AppStorage#size](arkts-arkui-appstorage-c.md#size)

<!--Device-AppStorage-static Size(): number--><!--Device-AppStorage-static Size(): number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| number | Number of properties in AppStorage. |

## clear

```TypeScript
static clear(): boolean
```

Deletes all properties from \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_. The deletion is only successful if none of the properties in AppStorage have any subscribers. If there are subscribers, this API does not take effect and **false** is returned. If there are no subscribers, the deletion is successful and **true** is returned. For details about the subscriber, see [delete]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AppStorage-static clear(): boolean--><!--Device-AppStorage-static clear(): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns **true** if the properties in AppStorage have no subscribers and the deletion is |

## delete

```TypeScript
static delete(propName: string): boolean
```

Deletes the property corresponding to **propName** from \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_. The deletion is only successful if the property has no subscribers. If there is a subscriber, the deletion fails and **false** is returned. If there are no subscribers, the deletion is successful and **true** is returned. The property subscribers include the following: 1. Variables decorated by \_\_\_MD\_LINK\_DESC\_USD\_1\_\_\_ or \_\_\_MD\_LINK\_DESC\_USD\_2\_\_\_ 2. Instances of [SubscribedAbstractProperty]\_\_\_JSDOC\_LINK\_DESC\_USD\_4\_\_\_ returned by [link]\_\_\_JSDOC\_LINK\_DESC\_USD\_5\_\_\_, [prop]\_\_\_JSDOC\_LINK\_DESC\_USD\_6\_\_\_, [setAndLink]\_\_\_JSDOC\_LINK\_DESC\_USD\_7\_\_\_, or [setAndProp]\_\_\_JSDOC\_LINK\_DESC\_USD\_8\_\_\_ To delete these subscribers: 1. Remove the custom component containing \@StorageLink or \@StorageProp. For details, see \_\_\_MD\_LINK\_DESC\_USD\_3\_\_\_. 2. Call the [aboutToBeDeleted]\_\_\_JSDOC\_LINK\_DESC\_USD\_9\_\_\_ API on instances of **SubscribedAbstractProperty** returned by **link**, **prop**, **setAndLink**, or **setAndProp**.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AppStorage-static delete(propName: string): boolean--><!--Device-AppStorage-static delete(propName: string): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| propName | string | Yes | Property name in AppStorage. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns **true** if the operation is successful; returns **false** if the operation fails. |

## get

```TypeScript
static get<T>(propName: string): T | undefined
```

Obtains the value of the property corresponding to **propName** from \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_. If the property does not exist, this API returns **undefined**.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AppStorage-static get<T>(propName: string): T | undefined--><!--Device-AppStorage-static get<T>(propName: string): T | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| propName | string | Yes | Property name in AppStorage. |

**Return value:**

| Type | Description |
| --- | --- |
| T | Value of the property corresponding to **propName** in AppStorage, or **undefined** if |

## has

```TypeScript
static has(propName: string): boolean
```

Checks whether the property corresponding to **propName** exists in \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AppStorage-static has(propName: string): boolean--><!--Device-AppStorage-static has(propName: string): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| propName | string | Yes | Property name in AppStorage. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns **true** if the property exists in AppStorage; returns **false** otherwise. |

## keys

```TypeScript
static keys(): IterableIterator<string>
```

Obtains all property names in \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AppStorage-static keys(): IterableIterator<string>--><!--Device-AppStorage-static keys(): IterableIterator<string>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;string&gt; | All property names in AppStorage. |

## link

```TypeScript
static link<T>(propName: string): SubscribedAbstractProperty<T>
```

Establishes a two-way data binding with the property corresponding to **propName** in \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_. If the given property exists in AppStorage, the two-way bound data of the property in AppStorage is returned. Any update of the data is synchronized back to AppStorage, which then synchronizes the update to all data and custom components bound to the property. If the given property does not exist in AppStorage, **undefined** is returned.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AppStorage-static link<T>(propName: string): SubscribedAbstractProperty<T>--><!--Device-AppStorage-static link<T>(propName: string): SubscribedAbstractProperty<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| propName | string | Yes | Property name in AppStorage. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;T&gt; | Two-way bound data of the specified property in AppStorage, or |

## prop

```TypeScript
static prop<T>(propName: string): SubscribedAbstractProperty<T>
```

Establishes a one-way data binding with the property corresponding to **propName** in \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_. If the given property exists in AppStorage, the one-way bound data of the property in AppStorage is returned. If the given property does not exist in AppStorage, **undefined** is returned. Updates of the one-way bound data are not synchronized back to AppStorage.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AppStorage-static prop<T>(propName: string): SubscribedAbstractProperty<T>--><!--Device-AppStorage-static prop<T>(propName: string): SubscribedAbstractProperty<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| propName | string | Yes | Property name in AppStorage. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;T&gt; | One-way bound data of the specified property in AppStorage, or |

## ref

```TypeScript
static ref<T>(propName: string): AbstractProperty<T> | undefined
```

Returns a reference to the property corresponding to **propName** in \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_. If the provided **propName** does not exist, this API returns **undefined**. This API is similar to [link]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ but does not require manually releasing the returned variable of the [AbstractProperty]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_ type.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AppStorage-static ref<T>(propName: string): AbstractProperty<T> | undefined--><!--Device-AppStorage-static ref<T>(propName: string): AbstractProperty<T> | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| propName | string | Yes | Property name in AppStorage. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;T&gt; | A reference to the property in AppStorage, or **undefined** if the |

## set

```TypeScript
static set<T>(propName: string, newValue: T): boolean
```

Sets the value of the property corresponding to **propName** in \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_. If the value of **newValue** is the same as the current value of the property, no assignment is performed, and the state variable does not instruct the UI to update the value of the property. > **NOTE** > Since API version 12, AppStorage supports > \_\_\_MD\_LINK\_DESC\_USD\_1\_\_\_, > \_\_\_MD\_LINK\_DESC\_USD\_2\_\_\_, > \_\_\_MD\_LINK\_DESC\_USD\_3\_\_\_, **null**, > **undefined**, and \_\_\_MD\_LINK\_DESC\_USD\_4\_\_\_ > types.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AppStorage-static set<T>(propName: string, newValue: T): boolean--><!--Device-AppStorage-static set<T>(propName: string, newValue: T): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| propName | string | Yes | Property name in AppStorage. |
| newValue | T | Yes | Property value. Since API version 12, the value can be **null** or **undefined**. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns **false** if the property corresponding to **propName** does not exist in AppStorage |

## setAndLink

```TypeScript
static setAndLink<T>(propName: string, defaultValue: T): SubscribedAbstractProperty<T>
```

Similar to the [link]\_\_\_JSDOC\_LINK\_DESC\_USD\_5\_\_\_ API, establishes a two-way data binding with the property corresponding to **propName** in \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_. If the given property exists in AppStorage, this API returns the two-way bound data for the property. If the given property does not exist, this API creates and initializes the property in AppStorage using **defaultValue** and returns its two- way bound data. > **NOTE** > Since API version 12, AppStorage supports > \_\_\_MD\_LINK\_DESC\_USD\_1\_\_\_, > \_\_\_MD\_LINK\_DESC\_USD\_2\_\_\_, > \_\_\_MD\_LINK\_DESC\_USD\_3\_\_\_, **null**, > **undefined**, and \_\_\_MD\_LINK\_DESC\_USD\_4\_\_\_ > types.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AppStorage-static setAndLink<T>(propName: string, defaultValue: T): SubscribedAbstractProperty<T>--><!--Device-AppStorage-static setAndLink<T>(propName: string, defaultValue: T): SubscribedAbstractProperty<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| propName | string | Yes | Property name in AppStorage. |
| defaultValue | T | Yes | Default value used to initialize the property corresponding to **propName** in AppStorage if **propName** does not exist. Since API version 12, **defaultValue** can be **null** or **undefined**. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;T&gt; | Instance of **SubscribedAbstractProperty\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_**, which is two-way bound |

## setAndProp

```TypeScript
static setAndProp<T>(propName: string, defaultValue: T): SubscribedAbstractProperty<T>
```

Similar to the [prop]\_\_\_JSDOC\_LINK\_DESC\_USD\_5\_\_\_ API, establishes a one-way data binding with the property corresponding to **propName** in \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_. If the given property exists in AppStorage, this API returns the one-way bound data for the property. If the given property does not exist, this API creates and initializes the property in AppStorage using **defaultValue** and returns its one- way bound data. > **NOTE** > Since API version 12, AppStorage supports > \_\_\_MD\_LINK\_DESC\_USD\_1\_\_\_, > \_\_\_MD\_LINK\_DESC\_USD\_2\_\_\_, > \_\_\_MD\_LINK\_DESC\_USD\_3\_\_\_, **null**, > **undefined**, and \_\_\_MD\_LINK\_DESC\_USD\_4\_\_\_ > types.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AppStorage-static setAndProp<T>(propName: string, defaultValue: T): SubscribedAbstractProperty<T>--><!--Device-AppStorage-static setAndProp<T>(propName: string, defaultValue: T): SubscribedAbstractProperty<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| propName | string | Yes | Property name in AppStorage. |
| defaultValue | T | Yes | Default value used to initialize the property corresponding to **propName** in AppStorage if **propName** does not exist. Since API version 12, **defaultValue** can be **null** or **undefined**. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;T&gt; | Instance of **SubscribedAbstractProperty\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_**. |

## setAndRef

```TypeScript
static setAndRef<T>(propName: string, defaultValue: T): AbstractProperty<T>
```

Similar to the [ref]\_\_\_JSDOC\_LINK\_DESC\_USD\_5\_\_\_ API, returns a reference to the property corresponding to **propName** in \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_. If the given property does not exist, this API creates and initializes the property in AppStorage using **defaultValue** and returns its reference. This API is similar to [setAndLink]\_\_\_JSDOC\_LINK\_DESC\_USD\_6\_\_\_ but does not require manually releasing the returned variable of the [AbstractProperty]\_\_\_JSDOC\_LINK\_DESC\_USD\_7\_\_\_ type. > **NOTE** > Since API version 12, AppStorage supports > \_\_\_MD\_LINK\_DESC\_USD\_1\_\_\_, > \_\_\_MD\_LINK\_DESC\_USD\_2\_\_\_, > \_\_\_MD\_LINK\_DESC\_USD\_3\_\_\_, **null**, > **undefined**, and \_\_\_MD\_LINK\_DESC\_USD\_4\_\_\_ > types.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AppStorage-static setAndRef<T>(propName: string, defaultValue: T): AbstractProperty<T>--><!--Device-AppStorage-static setAndRef<T>(propName: string, defaultValue: T): AbstractProperty<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| propName | string | Yes | Property name in AppStorage. |
| defaultValue | T | Yes | Default value used to initialize the property corresponding to **propName** in AppStorage if **propName** does not exist. The value can be **null** or **undefined**. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;T&gt; | Instance of **AbstractProperty\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_**, which is a reference to the property in |

## setOrCreate

```TypeScript
static setOrCreate<T>(propName: string, newValue: T): void
```

Sets the value of the property corresponding to **propName** in \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_ to a new value, if the property exists and the new value is different from the current value. If the new value is the same as the current value of the property, no assignment is performed, and the state variable does not instruct the UI to update the value of the property. If the property does not exist, this API creates it with the value of **newValue**. This **setOrCreate** API can create only one AppStorage key-value pair each time. To create multiple key-value pairs, call this API multiple times. > **NOTE** > Since API version 12, AppStorage supports > \_\_\_MD\_LINK\_DESC\_USD\_1\_\_\_, > \_\_\_MD\_LINK\_DESC\_USD\_2\_\_\_, > \_\_\_MD\_LINK\_DESC\_USD\_3\_\_\_, **null**, > **undefined**, and \_\_\_MD\_LINK\_DESC\_USD\_4\_\_\_ > types.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AppStorage-static setOrCreate<T>(propName: string, newValue: T): void--><!--Device-AppStorage-static setOrCreate<T>(propName: string, newValue: T): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| propName | string | Yes | Property name in AppStorage. |
| newValue | T | Yes | Property value. Since API version 12, the value can be **null** or **undefined**. |

## size

```TypeScript
static size(): number
```

Obtains the number of properties in \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AppStorage-static size(): number--><!--Device-AppStorage-static size(): number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| number | Number of properties in AppStorage. |

## staticClear

```TypeScript
static staticClear(): boolean
```

Deletes all properties.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [AppStorage.Clear](arkts-arkui-appstorage-c.md#clear)

<!--Device-AppStorage-static staticClear(): boolean--><!--Device-AppStorage-static staticClear(): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Deletes all properties. Returns **true** if all properties are deleted; returns **false** if |

