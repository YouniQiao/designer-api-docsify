# PersistenceV2

PersistenceV2具体UI使用说明，详见 PersistenceV2(持久化存储UI状态)。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## connect

```TypeScript
static connect<T extends object>(
    ttype: Class,
    defaultCreator?: StorageDefaultCreator<T>,
    connectOptions?: BaseConnectOptions<T>
  ): T | undefined
```

将键值对数据储存在应用磁盘中。如果给定的key已经存在于PersistenceV2中，返回对应的值；否则，会通过获取默认值的构造器构造默认值，并返回。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| ttype | [Class](../../apis-arkts/arkts-apis/arkts-arkts-class-c.md) | 是 |
| defaultCreator | [StorageDefaultCreator](arkts-arkui-storagedefaultcreator-t.md)&lt;T&gt; | 否 |
| connectOptions | [BaseConnectOptions](arkts-arkui-persistencev2-baseconnectoptions-i.md)&lt;T&gt; | 否 |

**返回值：**

| 类型 |
| --- |
| T \| undefined |

## connect

```TypeScript
static connect<T extends object>(
    ttype: Class,
    key: string,
    defaultCreator?: StorageDefaultCreator<T>,
    connectOptions?: BaseConnectOptions<T>
  ): T | undefined
```

将键值对数据储存在应用磁盘中。如果给定的key已经存在于PersistenceV2中，返回对应的值；否则，会通过获取默认值的构造器构造默认值，并返回。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| ttype | [Class](../../apis-arkts/arkts-apis/arkts-arkts-class-c.md) | 是 |
| key | string | 是 |
| defaultCreator | [StorageDefaultCreator](arkts-arkui-storagedefaultcreator-t.md)&lt;T&gt; | 否 |
| connectOptions | [BaseConnectOptions](arkts-arkui-persistencev2-baseconnectoptions-i.md)&lt;T&gt; | 否 |

**返回值：**

| 类型 |
| --- |
| T \| undefined |

## globalConnect

```TypeScript
static globalConnect<T extends object>(params: ConnectOptions<T>): T | undefined
```

将键值对数据储存在应用磁盘中。如果给定的key已经存在于PersistenceV2 中，返回对应的值；否则，会通过获取默认值的构造器构造默认值，并返回。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| params | [ConnectOptions](arkts-arkui-persistencev2-connectoptions-i.md)&lt;T&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| T \| undefined |

## keys

```TypeScript
static keys(): string[]
```

获取PersistenceV2中所有的key。

> **说明：**&gt;
> key在Array中的顺序是无序的，与key插入到PersistenceV2中的顺序无关。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| string[] |

## notifyOnError

```TypeScript
static notifyOnError(callback: PersistenceErrorCallback | undefined): void
```

在持久化失败时调用。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [PersistenceErrorCallback](arkts-arkui-persistenceerrorcallback-t.md) \| undefined | 是 |

## remove

```TypeScript
static remove(keyOrType: string | Class): void
```

将指定的键值对数据从PersistenceV2里面删除。如果指定的键值不存在于PersistenceV2中，将删除失败。

> **说明：**&gt;
> 删除PersistenceV2中不存在的key会打印warn日志警告。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| keyOrType | string \| [Class](../../apis-arkts/arkts-apis/arkts-arkts-class-c.md) | 是 |

## save

```TypeScript
static save(keyOrType: string | Class): void
```

手动持久化指定的键值对数据。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| keyOrType | string \| [Class](../../apis-arkts/arkts-apis/arkts-arkts-class-c.md) | 是 |
