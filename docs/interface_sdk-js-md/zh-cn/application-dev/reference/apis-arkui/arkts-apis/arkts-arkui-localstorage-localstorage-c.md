# LocalStorage

LocalStorage Class implements a Map of ObservableObjectBase UI state variables. Instances can be created to manage UI state within a limited "local"access, and life cycle as defined by the app. AppStorage singleton is sub-class of LocalStorage for UI state of app-wide access and same life cycle as the app.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## clear

```TypeScript
public clear(): boolean
```

Delete all properties from the LocalStorage instance Precondition is that there are no subscribers. method returns false and deletes no properties if there is any property that still has subscribers

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| boolean |

## constructor

```TypeScript
public constructor(initializingProperties?: RecordData)
```

Construct new instance of LocalStorage initialize with all properties and their values that Object.keys(params) returns Property values must not be undefined.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| initializingProperties | [RecordData](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-recorddata-t.md) | 否 |

## delete

```TypeScript
public delete(propName: string): boolean
```

Delete property from StorageBase Use with caution: Before deleting a prop from LocalStorage all its subscribers need to unsubscribe from the property. This method fails and returns false if given property still has subscribers Another reason for failing is unknown property. Developer advise: Subscribers are created with see link(), see prop() and also via @LocalStorageLink and @LocalStorageProp state variable decorators. That means as long as their is a @Component instance that uses such decorated variable or a sync relationship with a SubscribedAbstractProperty variable the property can nit (and also should not!) be deleted from LocalStorage.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| propName | string | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## get

```TypeScript
public get<T>(propName: string): T | undefined
```

Returns value of given property return undefined if no property with this name

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| propName | string | 是 |

**返回值：**

| 类型 |
| --- |
| T \| undefined |

## has

```TypeScript
public has(propName: string): boolean
```

Check if LocalStorage has a property with given name return true if property with given name exists same as ES6 Map.prototype.has()

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| propName | string | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## keys

```TypeScript
public keys(): IterableIterator<string>
```

Provide names of all properties in LocalStorage same as ES6 Map.prototype.keys()

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [IterableIterator](../../apis-arkts/arkts-apis/arkts-arkts-iterator-iterableiterator-i.md)&lt;string&gt; |

## link

```TypeScript
public link<T>(propName: string): SubscribedAbstractProperty<T> | undefined
```

Create and return a two-way sync "(link") to named property

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| propName | string | 是 |

**返回值：**

| 类型 |
| --- |
| [SubscribedAbstractProperty](arkts-arkui-storageproperty-subscribedabstractproperty-i.md)&lt;T&gt; \| undefined |

## ref

```TypeScript
public ref<T>(propName: string): AbstractProperty<T> | undefined
```

Obtain a handler or an alias to LocalStorage property with given name.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| propName | string | 是 |

**返回值：**

| 类型 |
| --- |
| [AbstractProperty](arkts-arkui-storageproperty-abstractproperty-i.md)&lt;T&gt; \| undefined |

## set

```TypeScript
public set<T>(propName: string, newValue: T): boolean
```

Set value of given property in LocalStorage Method sets nothing and returns false if property with this name does not exist in LocalStorage newValue can be undefined or null from API 20.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| propName | string | 是 |
| newValue | T | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## setAndLink

```TypeScript
public setAndLink<T>(propName: string, defaultValue: T): SubscribedAbstractProperty<T>
```

Like see link(), but will create and initialize a new source property in LocalStorage if missing

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| propName | string | 是 |
| defaultValue | T | 是 |

**返回值：**

| 类型 |
| --- |
| [SubscribedAbstractProperty](arkts-arkui-storageproperty-subscribedabstractproperty-i.md)&lt;T&gt; |

## setAndRef

```TypeScript
public setAndRef<T>(propName: string, defaultValue: T): AbstractProperty<T>
```

Obtain a handler or an alias to LocalStorage property with given name.If property does not exist in LocalStorage, create it with given default value.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| propName | string | 是 |
| defaultValue | T | 是 |

**返回值：**

| 类型 |
| --- |
| [AbstractProperty](arkts-arkui-storageproperty-abstractproperty-i.md)&lt;T&gt; |

## setOrCreate

```TypeScript
public setOrCreate<T>(propName: string, newValue: T): boolean
```

Set value of given property, if it exists, see set() . Add property if no property with given name and initialize with given value. newValue can be undefined or null from API 12

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| propName | string | 是 |
| newValue | T | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## size

```TypeScript
public size(): int
```

Returns number of properties in LocalStorage same as Map.prototype.size()

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| int |
