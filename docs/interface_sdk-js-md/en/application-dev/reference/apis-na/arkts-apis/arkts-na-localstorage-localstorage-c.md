# LocalStorage

LocalStorage Class implements a Map of ObservableObjectBase UI state variables. Instances can be created to manage UI state within a limited "local" access, and life cycle as defined by the app. AppStorage singleton is sub-class of LocalStorage for UI state of app-wide access and same life cycle as the app.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare class LocalStorage--><!--Device-unnamed-export declare class LocalStorage-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## clear

```TypeScript
public clear(): boolean
```

Delete all properties from the LocalStorage instance Precondition is that there are no subscribers. method returns false and deletes no properties if there is any property that still has subscribers

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LocalStorage-public clear(): boolean--><!--Device-LocalStorage-public clear(): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| boolean |  |

## constructor

```TypeScript
public constructor(initializingProperties?: RecordData)
```

Construct new instance of LocalStorage initialize with all properties and their values that Object.keys(params) returns Property values must not be undefined.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LocalStorage-public constructor(initializingProperties?: RecordData)--><!--Device-LocalStorage-public constructor(initializingProperties?: RecordData)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| initializingProperties | [RecordData](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-recorddata-t.md) | No | initializing Properties |

## delete

```TypeScript
public delete(propName: string): boolean
```

Delete property from StorageBase Use with caution: Before deleting a prop from LocalStorage all its subscribers need to unsubscribe from the property. This method fails and returns false if given property still has subscribers Another reason for failing is unknown property. Developer advise: Subscribers are created with see link(), see prop() and also via @LocalStorageLink and @LocalStorageProp state variable decorators. That means as long as their is a @Component instance that uses such decorated variable or a sync relationship with a SubscribedAbstractProperty variable the property can nit (and also should not!) be deleted from LocalStorage.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LocalStorage-public delete(propName: string): boolean--><!--Device-LocalStorage-public delete(propName: string): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| propName | string | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | false if method failed |

## get

```TypeScript
public get<T>(propName: string): T | undefined
```

Returns value of given property return undefined if no property with this name

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LocalStorage-public get<T>(propName: string): T | undefined--><!--Device-LocalStorage-public get<T>(propName: string): T | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| propName | string | Yes | property name |

**Return value:**

| Type | Description |
| --- | --- |
| T | property value if found or undefined |

## has

```TypeScript
public has(propName: string): boolean
```

Check if LocalStorage has a property with given name return true if property with given name exists same as ES6 Map.prototype.has()

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LocalStorage-public has(propName: string): boolean--><!--Device-LocalStorage-public has(propName: string): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| propName | string | Yes | searched property |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if property with such name exists in LocalStorage |

## keys

```TypeScript
public keys(): IterableIterator<string>
```

Provide names of all properties in LocalStorage same as ES6 Map.prototype.keys()

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LocalStorage-public keys(): IterableIterator<string>--><!--Device-LocalStorage-public keys(): IterableIterator<string>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| IterableIterator&lt;string&gt; | return a Map Iterator |

## link

```TypeScript
public link<T>(propName: string): SubscribedAbstractProperty<T> | undefined
```

Create and return a two-way sync "(link") to named property

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LocalStorage-public link<T>(propName: string): SubscribedAbstractProperty<T> | undefined--><!--Device-LocalStorage-public link<T>(propName: string): SubscribedAbstractProperty<T> | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| propName | string | Yes | name of source property in LocalStorage |

**Return value:**

| Type | Description |
| --- | --- |
| [SubscribedAbstractProperty](../../apis-arkui/arkts-apis/arkts-arkui-storageproperty-subscribedabstractproperty-i.md)&lt;T&gt; | instance of SubscribedAbstractProperty&lt;T&gt;, return undefined if named property does not already exist in LocalStorage. |

## ref

```TypeScript
public ref<T>(propName: string): AbstractProperty<T> | undefined
```

Obtain a handler or an alias to LocalStorage property with given name.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LocalStorage-public ref<T>(propName: string): AbstractProperty<T> | undefined--><!--Device-LocalStorage-public ref<T>(propName: string): AbstractProperty<T> | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| propName | string | Yes | LocalStorage property name |

**Return value:**

| Type | Description |
| --- | --- |
| [AbstractProperty](../../apis-arkui/arkts-apis/arkts-arkui-storageproperty-abstractproperty-i.md)&lt;T&gt; | AbstractProperty object if property with given name exists return undefined otherwise. |

## set

```TypeScript
public set<T>(propName: string, newValue: T): boolean
```

Set value of given property in LocalStorage Method sets nothing and returns false if property with this name does not exist in LocalStorage newValue can be undefined or null from API 20.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LocalStorage-public set<T>(propName: string, newValue: T): boolean--><!--Device-LocalStorage-public set<T>(propName: string, newValue: T): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| propName | string | Yes |  |
| newValue | T | Yes | must be of type T, can be undefined or null |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true on success, i.e. when above conditions are satisfied, otherwise false |

## setAndLink

```TypeScript
public setAndLink<T>(propName: string, defaultValue: T): SubscribedAbstractProperty<T>
```

Like see link(), but will create and initialize a new source property in LocalStorage if missing

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LocalStorage-public setAndLink<T>(propName: string, defaultValue: T): SubscribedAbstractProperty<T>--><!--Device-LocalStorage-public setAndLink<T>(propName: string, defaultValue: T): SubscribedAbstractProperty<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| propName | string | Yes | name of source property in LocalStorage |
| defaultValue | T | Yes | value to be used for initializing new property in LocalStorage default value must be of type T, can be undefined or null. |

**Return value:**

| Type | Description |
| --- | --- |
| [SubscribedAbstractProperty](../../apis-arkui/arkts-apis/arkts-arkui-storageproperty-subscribedabstractproperty-i.md)&lt;T&gt; | instance of SubscribedAbstractProperty&lt;T&gt; Apps can use SDK functions of base class SubscribedAbstractProperty&lt;T&gt; |

## setAndRef

```TypeScript
public setAndRef<T>(propName: string, defaultValue: T): AbstractProperty<T>
```

Obtain a handler or an alias to LocalStorage property with given name. If property does not exist in LocalStorage, create it with given default value.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LocalStorage-public setAndRef<T>(propName: string, defaultValue: T): AbstractProperty<T>--><!--Device-LocalStorage-public setAndRef<T>(propName: string, defaultValue: T): AbstractProperty<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| propName | string | Yes | LocalStorage property name |
| defaultValue | T | Yes | If property does not exist in LocalStorage, create it with given default value. |

**Return value:**

| Type | Description |
| --- | --- |
| [AbstractProperty](../../apis-arkui/arkts-apis/arkts-arkui-storageproperty-abstractproperty-i.md)&lt;T&gt; | AbstractProperty object |

## setOrCreate

```TypeScript
public setOrCreate<T>(propName: string, newValue: T): boolean
```

Set value of given property, if it exists, see set() . Add property if no property with given name and initialize with given value. newValue can be undefined or null from API 12

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LocalStorage-public setOrCreate<T>(propName: string, newValue: T): boolean--><!--Device-LocalStorage-public setOrCreate<T>(propName: string, newValue: T): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| propName | string | Yes |  |
| newValue | T | Yes | must be of type T, can be undefined or null |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true on success, i.e. when above conditions are satisfied, otherwise false |

## size

```TypeScript
public size(): int
```

Returns number of properties in LocalStorage same as Map.prototype.size()

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LocalStorage-public size(): int--><!--Device-LocalStorage-public size(): int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| int | return number of properties |

