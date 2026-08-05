# PersistenceV2

Inherits from [AppStorageV2]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_. For details, see \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_.

**Inheritance/Implementation:** PersistenceV2 extends [AppStorageV2](arkts-arkui-arkui-statemanagement-appstoragev2-c.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-export declare class PersistenceV2 extends AppStorageV2--><!--Device-unnamed-export declare class PersistenceV2 extends AppStorageV2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## globalConnect

```TypeScript
static globalConnect<T extends object>(
    type: ConnectOptions<T>
  ): T | undefined
```

Stores key-value pair data on the application disk. If the given key already exists in \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_, the corresponding value is returned. Otherwise, a default value is constructed using the default value constructor and returned. If **globalConnect** is used for an \_\_\_MD\_LINK\_DESC\_USD\_1\_\_\_ decorated object, changes to the object's \_\_\_MD\_LINK\_DESC\_USD\_2\_\_\_ properties will trigger automatic refresh of the associated object, while changes to non-@Trace properties will not. If necessary, the [PersistenceV2.save]\_\_\_JSDOC\_LINK\_DESC\_USD\_3\_\_\_ API can be called to store the data manually.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-PersistenceV2-static globalConnect<T extends object>(    type: ConnectOptions<T>  ): T | undefined--><!--Device-PersistenceV2-static globalConnect<T extends object>(    type: ConnectOptions<T>  ): T | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;T&gt; | Yes | Connection settings. |

**Return value:**

| Type | Description |
| --- | --- |
| T | Returns the data if creation or acquisition is successful; otherwise, returns |

## globalConnect

```TypeScript
static globalConnect<T extends CollectionType<S>, S extends object>(
    type: ConnectOptionsCollections<T, S> | ConnectOptions<T>
  ): T | undefined
```

Stores key-value pair data on the application disk. Supports the persistence of the following collection types: \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_. Note that when persisting data of the **Array\_\_\_ESCAPED\_UNDERSCORE\_DESC\_\_\_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_** type, you need to call [makeObserved]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ to make the returned object observed. Multi-level nested sets are not supported. For example, **Array&lt;Array\_\_\_ESCAPED\_UNDERSCORE\_DESC\_\_\_\_\_HTML\_TAG\_DESC\_USD\_3\_\_\_&gt;** persistence is not supported.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-PersistenceV2-static globalConnect<T extends CollectionType<S>, S extends object>(    type: ConnectOptionsCollections<T, S> | ConnectOptions<T>  ): T | undefined--><!--Device-PersistenceV2-static globalConnect<T extends CollectionType<S>, S extends object>(    type: ConnectOptionsCollections<T, S> | ConnectOptions<T>  ): T | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;T, S&gt; \| ConnectOptions&lt;T&gt; | Yes | Passed **globalConnect** parameters. For details, see the description of **ConnectOptions** and **ConnectOptionsCollections**.\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_If **defaultSubCreator** is provided in **ConnectOptionsCollections**, **defaultCreator** must be provided.Otherwise, the persistence fails. The collection item type S must be the same as the return type of **defaultSubCreator**. If the return types are inconsistent, an error will be reported during compilation. |

**Return value:**

| Type | Description |
| --- | --- |
| T | Returns the data if creation or acquisition is successful; otherwise, returns |

## notifyOnError

```TypeScript
static notifyOnError(callback: PersistenceErrorCallback | undefined): void
```

Called when persistence fails.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PersistenceV2-static notifyOnError(callback: PersistenceErrorCallback | undefined): void--><!--Device-PersistenceV2-static notifyOnError(callback: PersistenceErrorCallback | undefined): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_ \| undefined | Yes | Callback called when persistence fails. |

## save

```TypeScript
static save<T>(keyOrType: string | TypeConstructorWithArgs<T>): void
```

Persists the specified key-value pair data once.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PersistenceV2-static save<T>(keyOrType: string | TypeConstructorWithArgs<T>): void--><!--Device-PersistenceV2-static save<T>(keyOrType: string | TypeConstructorWithArgs<T>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| keyOrType | string \| TypeConstructorWithArgs&lt;T&gt; | Yes | Key to be persisted. If a type is specified, the key for persistence is the name of the type. |

