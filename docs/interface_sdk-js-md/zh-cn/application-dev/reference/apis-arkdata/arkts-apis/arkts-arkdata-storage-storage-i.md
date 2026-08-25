# Storage

提供获取和修改存储数据的接口。下列接口都需先使用[data_storage.getStorage](arkts-arkdata-storage-getstorage-f.md)或 [data_storage.getStorageSync](arkts-arkdata-storage-getstoragesync-f.md)获取到Storage实例，再通过此实例调用对应接口。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** preferences

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

## 导入模块

```TypeScript
```

## clear

```TypeScript
clear(callback: AsyncCallback<void>): void
```

清除此存储对象中的所有存储。使用callback方式返回结果，此方法为异步方法。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** clear

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## clear

```TypeScript
clear(): Promise<void>
```

清除此存储对象中的所有存储。使用Promise方式返回结果，此方法为异步方法。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** clear

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## clearSync

```TypeScript
clearSync(): void
```

清除此存储对象中的所有存储。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** clear

## delete

```TypeScript
delete(key: string, callback: AsyncCallback<void>): void
```

从存储对象中删除名为给定key的存储。使用callback方式返回结果，此方法为异步方法。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** delete

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## delete

```TypeScript
delete(key: string): Promise<void>
```

从存储对象删除名为给定key的存储。使用Promise方式返回结果，此方法为异步方法。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** delete

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## deleteSync

```TypeScript
deleteSync(key: string): void
```

从存储对象中删除名为给定key的存储。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** delete

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | string | 是 |

## flush

```TypeScript
flush(callback: AsyncCallback<void>): void
```

将当前storage对象中的修改保存到当前的storage，并异步存储到文件中。使用callback方式返回结果，此方法为异步方法。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** flush

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## flush

```TypeScript
flush(): Promise<void>
```

将当前storage对象中的修改保存到当前的storage，并异步存储到文件中。使用Promise方式返回结果，此方法为异步方法。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** flush

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## flushSync

```TypeScript
flushSync(): void
```

将当前storage对象中的修改保存到当前的storage，并同步存储到文件中。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** flush

## get

```TypeScript
get(key: string, defValue: ValueType, callback: AsyncCallback<ValueType>): void
```

获取键对应的值，如果值为null或者非默认值类型，返回默认数据defValue。使用callback方式返回结果，此方法为异步方法。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** get

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | string | 是 |
| defValue | [ValueType](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;ValueType&gt; | 是 |

## get

```TypeScript
get(key: string, defValue: ValueType): Promise<ValueType>
```

获取键对应的值，如果值为null或者非默认值类型，返回默认数据defValue。使用Promise方式返回结果，此方法为异步方法。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** get

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | string | 是 |
| defValue | [ValueType](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;ValueType & gt; |

## getSync

```TypeScript
getSync(key: string, defValue: ValueType): ValueType
```

获取键对应的值，如果值为null或者非默认值类型，返回默认数据defValue。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** get

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | string | 是 |
| defValue | [ValueType](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [ValueType](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) |

## has

```TypeScript
has(key: string, callback: AsyncCallback<boolean>): boolean
```

检查存储对象是否包含名为给定key的存储。使用callback方式返回结果，此方法为异步方法。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** has

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## has

```TypeScript
has(key: string): Promise<boolean>
```

检查存储对象是否包含名为给定key的存储。使用Promise方式返回结果，此方法为异步方法。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** has

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

## hasSync

```TypeScript
hasSync(key: string): boolean
```

检查存储对象是否包含名为给定key的存储。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** has

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | string | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## off('change')

```TypeScript
off(type: 'change', callback: Callback<StorageObserver>): void
```

当不再进行订阅数据变更时，使用此接口取消订阅。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** off

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'change' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[StorageObserver](arkts-arkdata-storage-storageobserver-i.md)&gt; | 是 |

## on('change')

```TypeScript
on(type: 'change', callback: Callback<StorageObserver>): void
```

订阅数据变更者类需要实现StorageObserver接口，订阅的key的值发生变更后，在执行flush/flushSync方法后，callback方法会被回调。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** on

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'change' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[StorageObserver](arkts-arkdata-storage-storageobserver-i.md)&gt; | 是 |

## put

```TypeScript
put(key: string, value: ValueType, callback: AsyncCallback<void>): void
```

首先获取指定文件对应的Storage实例，然后借助Storage API将数据写入Storage实例，通过flush或者flushSync将Storage实例持久化。使用callback方式返回结果，此方法为异步方法。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** put

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | string | 是 |
| value | [ValueType](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## put

```TypeScript
put(key: string, value: ValueType): Promise<void>
```

首先获取指定文件对应的Storage实例，然后借助Storage API将数据写入Storage实例，通过flush或者flushSync将Storage实例持久化。使用Promise方式返回结果，此方法为异步方法。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** put

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | string | 是 |
| value | [ValueType](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## putSync

```TypeScript
putSync(key: string, value: ValueType): void
```

首先获取指定文件对应的Storage实例，然后借助Storage API将数据写入Storage实例，通过flush或者flushSync将Storage实例持久化。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** put

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | string | 是 |
| value | [ValueType](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) | 是 |
