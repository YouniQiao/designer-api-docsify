# Preferences

首选项实例，提供获取和修改存储数据的接口。下列接口都需先使用[preferences.getPreferences](arkts-arkdata-preferences-getpreferences-f.md)获取到Preferences实例，再通过此实例调用对应接口。

**起始版本：** 9

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

## 导入模块

```TypeScript
import { preferences } from 'kits/@kit.ArkData';
```

## clear

```TypeScript
clear(callback: AsyncCallback<void>): void
```

清除缓存的Preferences实例中的所有数据，可通过[flush](#flush)将 Preferences实例持久化，使用callback异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15500000](../errorcode-preferences.md#15500000-内部错误) |

## clear

```TypeScript
clear(): Promise<void>
```

清除缓存的Preferences实例中的所有数据，可通过[flush](#flush)将 Preferences实例持久化，使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [15500000](../errorcode-preferences.md#15500000-内部错误) |

## clearSync

```TypeScript
clearSync(): void
```

清除缓存的Preferences实例中的所有数据，可通过[flush](#flush)将 Preferences实例持久化，此为同步接口。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

## delete

```TypeScript
delete(key: string, callback: AsyncCallback<void>): void
```

从缓存的Preferences实例中删除名为给定Key的存储键值对，可通过[flush](#flush)将 Preferences实例持久化，使用callback异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15500000](../errorcode-preferences.md#15500000-内部错误) |

## delete

```TypeScript
delete(key: string): Promise<void>
```

从缓存的Preferences实例中删除名为给定Key的存储键值对，可通过[flush](#flush)将 Preferences实例持久化，使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15500000](../errorcode-preferences.md#15500000-内部错误) |

## deleteSync

```TypeScript
deleteSync(key: string): void
```

从缓存的Preferences实例中删除名为给定Key的存储键值对，可通过[flush](#flush)将 Preferences实例持久化，此为同步接口。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15500000](../errorcode-preferences.md#15500000-内部错误) |

## flush

```TypeScript
flush(callback: AsyncCallback<void>): void
```

将缓存的Preferences实例中的数据异步存储到用户首选项的持久化文件中，使用callback异步回调。

> **说明：**&gt;
> 当数据未修改或修改后的数据与缓存数据一致时，不会刷新持久化文件。&gt;
> 只在XML存储模式下使用，在GSKV存储模式下无需调用，因为当选择该模式时首选项对数据的操作会实时落盘。Preferences存储模式可见
> [存储模式说明](../../../database/data-persistence-by-preferences.md#存储模式说明)。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15500000](../errorcode-preferences.md#15500000-内部错误) |

## flush

```TypeScript
flush(): Promise<void>
```

将缓存的Preferences实例中的数据异步存储到用户首选项的持久化文件中，使用Promise异步回调。

> **说明：**&gt;
> 当数据未修改或修改后的数据与缓存数据一致时，不会刷新持久化文件。&gt;
> 只在XML存储模式下使用，在GSKV存储模式下无需调用，因为当选择该模式时首选项对数据的操作会实时落盘。Preferences存储模式可见
> [存储模式说明](../../../database/data-persistence-by-preferences.md#存储模式说明)。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [15500000](../errorcode-preferences.md#15500000-内部错误) |

## flushSync

```TypeScript
flushSync(): void
```

将缓存的Preferences实例中的数据存储到用户首选项的持久化文件中。

> **说明：**&gt;
> 当数据未修改或修改后的数据与缓存数据一致时，不会刷新持久化文件。

**起始版本：** 14

**原子化服务API：** 从API版本14开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**错误码：**

| 错误码ID |
| --- |
| [15500000](../errorcode-preferences.md#15500000-内部错误) |

## get

```TypeScript
get(key: string, defValue: ValueType, callback: AsyncCallback<ValueType>): void
```

从缓存的Preferences实例中获取键对应的值，如果值为null或者非默认值类型，返回默认数据defValue，使用callback异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | string | 是 |
| defValue | [ValueType](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;ValueType&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15500000](../errorcode-preferences.md#15500000-内部错误) |

## get

```TypeScript
get(key: string, defValue: ValueType): Promise<ValueType>
```

从缓存的Preferences实例中获取键对应的值，如果值为null或者非默认值类型，返回默认数据defValue，使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | string | 是 |
| defValue | [ValueType](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;ValueType & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15500000](../errorcode-preferences.md#15500000-内部错误) |

## getAll

```TypeScript
getAll(callback: AsyncCallback<Object>): void
```

获取缓存的Preferences实例中的所有键值数据。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Object&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15500000](../errorcode-preferences.md#15500000-内部错误) |

## getAll

```TypeScript
getAll(): Promise<Object>
```

获取缓存的Preferences实例中的所有键值数据，使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;Object & gt; |

**错误码：**

| 错误码ID |
| --- |
| [15500000](../errorcode-preferences.md#15500000-内部错误) |

## getAllSync

```TypeScript
getAllSync(): Object
```

获取缓存的Preferences实例中的所有键值数据，此为同步接口。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**返回值：**

| 类型 |
| --- |
| Object |

**错误码：**

| 错误码ID |
| --- |
| [15500000](../errorcode-preferences.md#15500000-内部错误) |

## getSync

```TypeScript
getSync(key: string, defValue: ValueType): ValueType
```

从缓存的Preferences实例中获取键对应的值，如果值为null或者非默认值类型，返回默认数据defValue，此为同步接口。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | string | 是 |
| defValue | [ValueType](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [ValueType](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15500000](../errorcode-preferences.md#15500000-内部错误) |

## has

```TypeScript
has(key: string, callback: AsyncCallback<boolean>): void
```

检查缓存的Preferences实例中是否包含指定Key的存储键值对，使用callback异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15500000](../errorcode-preferences.md#15500000-内部错误) |

## has

```TypeScript
has(key: string): Promise<boolean>
```

检查缓存的Preferences实例中是否包含指定Key的存储键值对，使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15500000](../errorcode-preferences.md#15500000-内部错误) |

## hasSync

```TypeScript
hasSync(key: string): boolean
```

检查缓存的Preferences实例中是否包含指定Key的存储键值对，此为同步接口。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | string | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15500000](../errorcode-preferences.md#15500000-内部错误) |

## off('change')

```TypeScript
off(type: 'change', callback?: Callback<string>): void
```

取消订阅数据变更。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'change' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;string&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15500000](../errorcode-preferences.md#15500000-内部错误) |

## off('multiProcessChange')

```TypeScript
off(type: 'multiProcessChange', callback?: Callback<string>): void
```

取消订阅进程间数据变更。本接口提供给申请了[dataGroupId](arkts-arkdata-preferences-options-i.md)的应用进行使用，未申请的应用不推荐使用（监听不到数据变更），多进程操作可能会损坏持久化文件，导致数据丢失。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'multiProcessChange' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;string&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15500000](../errorcode-preferences.md#15500000-内部错误) |

## off('dataChange')

```TypeScript
off(type: 'dataChange', keys: Array<string>, callback?: Callback<Record<string, ValueType>>): void
```

取消精确订阅数据变更。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'dataChange' | 是 |
| keys | Array & lt;string & gt; | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Record&lt;string, ValueType&gt;&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15500000](../errorcode-preferences.md#15500000-内部错误) |

## on('change')

```TypeScript
on(type: 'change', callback: Callback<string>): void
```

订阅数据变更，订阅的Key的值发生变更后，并且在执行[flush](#flush)方法后，触发 callback回调。

> **不同订阅方法的对比：**&gt;
> - on('change')：订阅所有Key变化，适合全局数据变化感知需求。&gt;
> - on('dataChange')：精确订阅指定Key的变化，适合关注特定数据场景，可回调返回具体值。&gt;
> - on('multiProcessChange')：订阅多进程数据变化，适合多进程共享同一首选项文件的场景。&gt;
> **选取建议：** 单进程应用推荐使用on('change')或on('dataChange')；多进程数据同步时使用on('multiProcessChange')；需要精确知道特定Key变化并获取新值时使用on('
> dataChange')。
> 
> **说明：**&gt;
> 当调用[removePreferencesFromCache](arkts-arkdata-preferences-removepreferencesfromcache-f.md)或
> [deletePreferences](arkts-arkdata-preferences-deletepreferences-f.md)后，订阅的数据变更会主动取消订阅，在重新
> [getPreferences](arkts-arkdata-preferences-getpreferences-f.md)后需要重新订阅数据变更。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'change' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;string&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15500000](../errorcode-preferences.md#15500000-内部错误) |

## on('multiProcessChange')

```TypeScript
on(type: 'multiProcessChange', callback: Callback<string>): void
```

订阅进程间数据变更，多个进程持有同一个首选项文件时，在任意一个进程（包括本进程）执行 [flush](#flush)方法，持久化文件发生变更后，触发callback回调。本接口提供给申请了[dataGroupId](arkts-arkdata-preferences-options-i.md)的应用进行使用，未申请的应用不推荐使用（监听不到数据变更），多进程操作可能会损坏持久化文件，导致数据丢失。

> **说明：**&gt;
> 同一持久化文件在当前进程对多进程数据变更订阅的最大数量为50次，超过最大限制后订阅会失败。建议在触发callback回调后及时取消订阅。&gt;
> 当调用[removePreferencesFromCache](arkts-arkdata-preferences-removepreferencesfromcache-f.md)或
> [deletePreferences](arkts-arkdata-preferences-deletepreferences-f.md)后，订阅的数据变更会主动取消订阅，在重新
> [getPreferences](arkts-arkdata-preferences-getpreferences-f.md)后需要重新订阅数据变更。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'multiProcessChange' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;string&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15500019](../errorcode-preferences.md#15500019-获取订阅服务失败) |
| [15500000](../errorcode-preferences.md#15500000-内部错误) |

## on('dataChange')

```TypeScript
on(type: 'dataChange', keys: Array<string>, callback: Callback<Record<string, ValueType>>): void
```

精确订阅数据变更，只有被订阅的Key值发生变更后，在执行[flush](#flush)方法后，触发 callback回调。

> **说明：**&gt;
> 当调用[removePreferencesFromCache](arkts-arkdata-preferences-removepreferencesfromcache-f.md)或
> [deletePreferences](arkts-arkdata-preferences-deletepreferences-f.md)后，订阅的数据变更会主动取消订阅，在重新
> [getPreferences](arkts-arkdata-preferences-getpreferences-f.md)后需要重新订阅数据变更。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'dataChange' | 是 |
| keys | Array & lt;string & gt; | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Record&lt;string, ValueType&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15500000](../errorcode-preferences.md#15500000-内部错误) |

## put

```TypeScript
put(key: string, value: ValueType, callback: AsyncCallback<void>): void
```

将数据写入缓存的Preferences实例中，可通过[flush](#flush)将Preferences 实例持久化，使用callback异步回调。

> **说明：**&gt;
> 当value中包含非UTF-8格式的字符串时，请使用Uint8Array类型存储，否则会造成持久化文件出现格式错误造成文件损坏。&gt;
> 当对应的键已经存在时，put()方法会覆盖其值。可以使用hasSync()方法检查是否存在对应键值对。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | string | 是 |
| value | [ValueType](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15500000](../errorcode-preferences.md#15500000-内部错误) |

## put

```TypeScript
put(key: string, value: ValueType): Promise<void>
```

将数据写入缓存的Preferences实例中，可通过[flush](#flush)将Preferences 实例持久化，使用Promise异步回调。

> **说明：**&gt;
> 当value中包含非UTF-8格式的字符串时，请使用Uint8Array类型存储，否则会造成持久化文件出现格式错误造成文件损坏。&gt;
> 当对应的键已经存在时，put()方法会覆盖其值。可以使用hasSync()方法检查是否存在对应键值对。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | string | 是 |
| value | [ValueType](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15500000](../errorcode-preferences.md#15500000-内部错误) |

## putSync

```TypeScript
putSync(key: string, value: ValueType): void
```

将数据写入缓存的Preferences实例中，可通过[flush](#flush)将Preferences 实例持久化，此为同步接口。

> **说明：**&gt;
> 当value中包含非UTF-8格式的字符串时，请使用Uint8Array类型存储，否则会造成持久化文件出现格式错误造成文件损坏。&gt;
> 当对应的键已经存在时，putSync()方法会覆盖其值。可以使用hasSync()方法检查是否存在对应键值对。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | string | 是 |
| value | [ValueType](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15500000](../errorcode-preferences.md#15500000-内部错误) |
