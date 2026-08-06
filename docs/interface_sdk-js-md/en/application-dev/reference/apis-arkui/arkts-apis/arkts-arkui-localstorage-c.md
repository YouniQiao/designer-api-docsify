# LocalStorage

For details about how to use LocalStorage on the UI, see  
\_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-unnamed-declare class LocalStorage--><!--Device-unnamed-declare class LocalStorage-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## GetShared

```TypeScript
static GetShared(): LocalStorage
```

Obtains the \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_ instance shared across the current stage.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 10

**Substitutes:** [LocalStorage#getShared](arkts-arkui-localstorage-c.md#getshared)

**Model restriction:** This API can be used only in the stage model.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-LocalStorage-static GetShared(): LocalStorage--><!--Device-LocalStorage-static GetShared(): LocalStorage-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | LocalStorage** instance. |

## clear

```TypeScript
clear(): boolean
```

Deletes all properties from \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_. The deletion is only successful if none of the properties in LocalStorage have any subscribers. If there are subscribers, this API does not take effect and **false** is returned. If there are no subscribers, the deletion is successful and  
**true** is returned.

For details about the subscriber, see [delete]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-LocalStorage-clear(): boolean--><!--Device-LocalStorage-clear(): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns **true** if the operation is successful; returns **false** otherwise. |

## constructor

```TypeScript
constructor(initializingProperties?: Object)
```

Creates a \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_ instance and initializes it using the properties and values returned by **Object.keys(initializingProperties)**.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-LocalStorage-constructor(initializingProperties?: Object)--><!--Device-LocalStorage-constructor(initializingProperties?: Object)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| initializingProperties | Object | No | Properties and values used to initialize the **LocalStorage** instance. **initializingProperties** cannot be set to **undefined**. The default value is an empty object, meaning no properties are added to LocalStorage during initialization. |

## delete

```TypeScript
delete(propName: string): boolean
```

Deletes the property corresponding to **propName** from  
\_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_. The deletion is only successful if the property has no subscribers. If there is a subscriber, the deletion fails and **false** is returned. If there are no subscribers, the deletion is successful and **true** is returned.

The property subscribers include the following:

1. Variables decorated by  
\_\_\_MD\_LINK\_DESC\_USD\_1\_\_\_ or  
\_\_\_MD\_LINK\_DESC\_USD\_2\_\_\_

2. Instances of [SubscribedAbstractProperty]\_\_\_JSDOC\_LINK\_DESC\_USD\_4\_\_\_returned by [link]\_\_\_JSDOC\_LINK\_DESC\_USD\_5\_\_\_, [prop]\_\_\_JSDOC\_LINK\_DESC\_USD\_6\_\_\_,  
[setAndLink]\_\_\_JSDOC\_LINK\_DESC\_USD\_7\_\_\_, or [setAndProp]\_\_\_JSDOC\_LINK\_DESC\_USD\_8\_\_\_

To delete these subscribers:

1. Remove the custom component containing \@LocalStorageLink or \@LocalStorageProp.For details, see  
\_\_\_MD\_LINK\_DESC\_USD\_3\_\_\_.

2. Call the [aboutToBeDeleted]\_\_\_JSDOC\_LINK\_DESC\_USD\_9\_\_\_ API on instances of **SubscribedAbstractProperty** returned by **link**, **prop**, **setAndLink**, or **setAndProp**.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-LocalStorage-delete(propName: string): boolean--><!--Device-LocalStorage-delete(propName: string): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| propName | string | Yes | Property name in LocalStorage. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns **true** if the operation is successful; returns **false** if the operation fails. |

## get

```TypeScript
get<T>(propName: string): T | undefined
```

Obtains the value of the property corresponding to **propName** from  
\_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-LocalStorage-get<T>(propName: string): T | undefined--><!--Device-LocalStorage-get<T>(propName: string): T | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| propName | string | Yes | Property name in LocalStorage. |

**Return value:**

| Type | Description |
| --- | --- |
| T | Value of the property corresponding to **propName** in LocalStorage, or **undefined** if it does not exist. |

## getShared

```TypeScript
static getShared(): LocalStorage
```

Obtains the \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_ instance shared across the current stage.
    **NOTE**
    Since API version 12, you can use the  
    \_\_\_MD\_LINK\_DESC\_USD\_1\_\_\_  
    API in [UIContext]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_ to specify the UI execution context.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** 18

**Substitutes:** ohos.arkui.UIContext.UIContext#getSharedLocalStorage

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 10.

<!--Device-LocalStorage-static getShared(): LocalStorage--><!--Device-LocalStorage-static getShared(): LocalStorage-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | LocalStorage** instance. |

## has

```TypeScript
has(propName: string): boolean
```

Checks whether the property corresponding to **propName** exists in  
\_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-LocalStorage-has(propName: string): boolean--><!--Device-LocalStorage-has(propName: string): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| propName | string | Yes | Property name in LocalStorage. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns **true** if the property exists in LocalStorage; returns **false** otherwise. |

## keys

```TypeScript
keys(): IterableIterator<string>
```

Obtains all property names in \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-LocalStorage-keys(): IterableIterator<string>--><!--Device-LocalStorage-keys(): IterableIterator<string>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;string&gt; | All property names in LocalStorage. |

## link

```TypeScript
link<T>(propName: string): SubscribedAbstractProperty<T>
```

Establishes a two-way data binding with the property corresponding to **propName** in  
\_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_. If the given property exists in LocalStorage,this API returns the two-way bound data for the property.

Any update of the data is synchronized back to LocalStorage, which then synchronizes the update to all data and components bound to the property.

If the given property does not exist in LocalStorage, **undefined** is returned.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-LocalStorage-link<T>(propName: string): SubscribedAbstractProperty<T>--><!--Device-LocalStorage-link<T>(propName: string): SubscribedAbstractProperty<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| propName | string | Yes | Property name in LocalStorage. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;T&gt; | Returns the **SubscribedAbstractProperty\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_** instance if the given property exists in LocalStorage; returns **undefined** otherwise. |

## prop

```TypeScript
prop<S>(propName: string): SubscribedAbstractProperty<S>
```

Establishes a one-way data binding with the property corresponding to **propName** in  
\_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_. If the given property exists in LocalStorage,this API returns the one-way bound data for the property. If the given property does not exist in LocalStorage,  
**undefined** is returned. Updates of the one-way bound data are not synchronized back to LocalStorage.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-LocalStorage-prop<S>(propName: string): SubscribedAbstractProperty<S>--><!--Device-LocalStorage-prop<S>(propName: string): SubscribedAbstractProperty<S>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| propName | string | Yes | Property name in LocalStorage. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;S&gt; | Instance of **SubscribedAbstractProperty\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_** and one-way bound data of the given property in LocalStorage. If the given property does not exist in LocalStorage, **undefined** is returned. |

## ref

```TypeScript
public ref<T>(propName: string): AbstractProperty<T> | undefined
```

Returns a reference to the property corresponding to **propName** in  
\_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_. If the provided **propName** does not exist,this API returns **undefined**.

This API is similar to [link]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ but does not require manually releasing the returned variable of the [AbstractProperty]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_ type.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LocalStorage-public ref<T>(propName: string): AbstractProperty<T> | undefined--><!--Device-LocalStorage-public ref<T>(propName: string): AbstractProperty<T> | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| propName | string | Yes | Property name in LocalStorage. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;T&gt; | A reference to the property in LocalStorage, or **undefined** if the property does not exist. |

## set

```TypeScript
set<T>(propName: string, newValue: T): boolean
```

Sets the value of the property corresponding to **propName** in  
\_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_. If the value of **newValue** is the same as the current value of the property, no assignment is performed, and the state variable does not instruct the UI to update the value of the property.
    **NOTE**
    Since API version 12, LocalStorage supports  
    \_\_\_MD\_LINK\_DESC\_USD\_1\_\_\_,  
    \_\_\_MD\_LINK\_DESC\_USD\_2\_\_\_,  
    \_\_\_MD\_LINK\_DESC\_USD\_3\_\_\_, **null**,  
    **undefined**, and \_\_\_MD\_LINK\_DESC\_USD\_4\_\_\_  
    types.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-LocalStorage-set<T>(propName: string, newValue: T): boolean--><!--Device-LocalStorage-set<T>(propName: string, newValue: T): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| propName | string | Yes | Property name in LocalStorage. |
| newValue | T | Yes | Property value. Since API version 12, the value can be **null** or **undefined**. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns **false** if the property corresponding to **propName** does not exist in LocalStorage. Returns **true** if the operation is successful. |

## setAndLink

```TypeScript
setAndLink<T>(propName: string, defaultValue: T): SubscribedAbstractProperty<T>
```

Similar to the [link]\_\_\_JSDOC\_LINK\_DESC\_USD\_5\_\_\_ API, establishes a two-way data binding with the property corresponding to **propName** in \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_. If the given property exists in LocalStorage, this API returns the two-way bound data for the property. If the given property does not exist, this API creates and initializes the property in LocalStorage using **defaultValue** and returns its two-way bound data.
    **NOTE**
    Since API version 12, LocalStorage supports  
    \_\_\_MD\_LINK\_DESC\_USD\_1\_\_\_,  
    \_\_\_MD\_LINK\_DESC\_USD\_2\_\_\_,  
    \_\_\_MD\_LINK\_DESC\_USD\_3\_\_\_, **null**,  
    **undefined**, and \_\_\_MD\_LINK\_DESC\_USD\_4\_\_\_  
    types.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-LocalStorage-setAndLink<T>(propName: string, defaultValue: T): SubscribedAbstractProperty<T>--><!--Device-LocalStorage-setAndLink<T>(propName: string, defaultValue: T): SubscribedAbstractProperty<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| propName | string | Yes | Property name in LocalStorage. |
| defaultValue | T | Yes | Default value used to initialize the property corresponding to **propName** in LocalStorage if **propName** does not exist. Since API version 12, **defaultValue** can be **null** or **undefined**. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;T&gt; | Instance of **SubscribedAbstractProperty\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_** and two-way bound data of the given property in LocalStorage. |

## setAndProp

```TypeScript
setAndProp<S>(propName: string, defaultValue: S): SubscribedAbstractProperty<S>
```

Similar to the [prop]\_\_\_JSDOC\_LINK\_DESC\_USD\_5\_\_\_ API, establishes a one-way data binding with the property corresponding to **propName** in \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_. If the given property exists in LocalStorage, this API returns the one-way bound data for the property. If the given property does not exist, this API creates and initializes the property in LocalStorage using **defaultValue** and returns its one-way bound data.
    **NOTE**
    Since API version 12, LocalStorage supports  
    \_\_\_MD\_LINK\_DESC\_USD\_1\_\_\_,  
    \_\_\_MD\_LINK\_DESC\_USD\_2\_\_\_,  
    \_\_\_MD\_LINK\_DESC\_USD\_3\_\_\_, **null**,  
    **undefined**, and \_\_\_MD\_LINK\_DESC\_USD\_4\_\_\_  
    types.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-LocalStorage-setAndProp<S>(propName: string, defaultValue: S): SubscribedAbstractProperty<S>--><!--Device-LocalStorage-setAndProp<S>(propName: string, defaultValue: S): SubscribedAbstractProperty<S>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| propName | string | Yes | Property name in LocalStorage. |
| defaultValue | S | Yes | Default value used to initialize the property corresponding to **propName** in LocalStorage if **propName** does not exist. Since API version 12, **defaultValue** can be **null** or **undefined**. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;S&gt; | Instance of **SubscribedAbstractProperty\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_** and one-way bound data of the given property in LocalStorage. |

## setAndRef

```TypeScript
public setAndRef<T>(propName: string, defaultValue: T): AbstractProperty<T>
```

Similar to the [ref]\_\_\_JSDOC\_LINK\_DESC\_USD\_5\_\_\_ API, returns a reference to the property corresponding to **propName**  
in \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_. If the given property does not exist, this API creates and initializes the property in LocalStorage using **defaultValue** and returns its reference.

This API is similar to [setAndLink]\_\_\_JSDOC\_LINK\_DESC\_USD\_6\_\_\_ but does not require manually releasing the returned variable of the [AbstractProperty]\_\_\_JSDOC\_LINK\_DESC\_USD\_7\_\_\_ type.
    **NOTE**
    Since API version 12, LocalStorage supports  
    \_\_\_MD\_LINK\_DESC\_USD\_1\_\_\_,  
    \_\_\_MD\_LINK\_DESC\_USD\_2\_\_\_,  
    \_\_\_MD\_LINK\_DESC\_USD\_3\_\_\_, **null**,  
    **undefined**, and \_\_\_MD\_LINK\_DESC\_USD\_4\_\_\_  
    types.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LocalStorage-public setAndRef<T>(propName: string, defaultValue: T): AbstractProperty<T>--><!--Device-LocalStorage-public setAndRef<T>(propName: string, defaultValue: T): AbstractProperty<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| propName | string | Yes | Property name in LocalStorage. |
| defaultValue | T | Yes | Default value used to initialize the property corresponding to **propName** in LocalStorage if **propName** does not exist. The value can be **null** or **undefined**. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;T&gt; | Instance of **AbstractProperty\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_**, which is a reference to the property in LocalStorage corresponding to **propName**. |

## setOrCreate

```TypeScript
setOrCreate<T>(propName: string, newValue: T): boolean
```

Sets the value of the property corresponding to **propName** in  
\_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_ to a new value, if the property exists and the new value is different from the current value. If the new value is the same as the current value of the property,no assignment is performed, and the state variable does not instruct the UI to update the value of the property.

If the property does not exist, this API creates it with the value of **newValue**. This **setOrCreate** API can create only one LocalStorage key-value pair each time. To create multiple key-value pairs, call this API multiple times.
    **NOTE**
    Since API version 12, LocalStorage supports  
    \_\_\_MD\_LINK\_DESC\_USD\_1\_\_\_,  
    \_\_\_MD\_LINK\_DESC\_USD\_2\_\_\_,  
    \_\_\_MD\_LINK\_DESC\_USD\_3\_\_\_, **null**,  
    **undefined**, and \_\_\_MD\_LINK\_DESC\_USD\_4\_\_\_  
    types.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-LocalStorage-setOrCreate<T>(propName: string, newValue: T): boolean--><!--Device-LocalStorage-setOrCreate<T>(propName: string, newValue: T): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| propName | string | Yes | Property name in LocalStorage. |
| newValue | T | Yes | Property value. Since API version 12, the value can be **null** or **undefined**. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns **true** if the property corresponding to **propName** exists and its value is updated to the value of **newValue**, \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_or if **propName** is created with the value of **newValue**. |

## size

```TypeScript
size(): number
```

Obtains the number of properties in \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-LocalStorage-size(): number--><!--Device-LocalStorage-size(): number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| number | Number of properties in LocalStorage. |

