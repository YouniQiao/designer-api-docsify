# PersistenceV2

PersistenceV2具体UI使用说明，详见  
[PersistenceV2(持久化存储UI状态)](../../../ui/state-management-static/arkts-static-new-persistencev2.md)。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export declare class PersistenceV2--><!--Device-unnamed-export declare class PersistenceV2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## connect

```TypeScript
static connect<T extends object>(
    ttype: Class,
    defaultCreator?: StorageDefaultCreator<T>,
    connectOptions?: BaseConnectOptions<T>
  ): T | undefined
```

将键值对数据储存在应用磁盘中。如果给定的key已经存在于PersistenceV2中，返回对应的值；否则，会通过获取默认值的构造器构造默认值，并返回。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PersistenceV2-static connect<T extends object>(    ttype: Class,    defaultCreator?: StorageDefaultCreator<T>,    connectOptions?: BaseConnectOptions<T>  ): T | undefined--><!--Device-PersistenceV2-static connect<T extends object>(    ttype: Class,    defaultCreator?: StorageDefaultCreator<T>,    connectOptions?: BaseConnectOptions<T>  ): T | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| ttype | [Class](../../apis-arkts/arkts-apis/arkts-arkts-class-c.md) | Yes | class type of the stored value. |
| defaultCreator | [StorageDefaultCreator](arkts-arkui-storagedefaultcreator-t.md)&lt;T&gt; | No | the function generating the default value |
| connectOptions | [BaseConnectOptions](arkts-arkui-persistencev2-baseconnectoptions-i.md)&lt;T&gt; | No | additional connect options. |

**Return value:**

| Type | Description |
| --- | --- |
| T | the value of the existing key or the default value. returns undefined when defaultCreator is not set and there is no data with matching type. |

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

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PersistenceV2-static connect<T extends object>(    ttype: Class,    key: string,    defaultCreator?: StorageDefaultCreator<T>,    connectOptions?: BaseConnectOptions<T>  ): T | undefined--><!--Device-PersistenceV2-static connect<T extends object>(    ttype: Class,    key: string,    defaultCreator?: StorageDefaultCreator<T>,    connectOptions?: BaseConnectOptions<T>  ): T | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| ttype | [Class](../../apis-arkts/arkts-apis/arkts-arkts-class-c.md) | Yes | class type of the stored value. |
| key | string | Yes | alias name of the key. |
| defaultCreator | [StorageDefaultCreator](arkts-arkui-storagedefaultcreator-t.md)&lt;T&gt; | No | the function generating the default value |
| connectOptions | [BaseConnectOptions](arkts-arkui-persistencev2-baseconnectoptions-i.md)&lt;T&gt; | No | additional connect options. |

**Return value:**

| Type | Description |
| --- | --- |
| T | the value of the existed key or the default value. returns undefined when defaultCreator is not set and there is no data with matching type and key. |

## globalConnect

```TypeScript
static globalConnect<T extends object>(params: ConnectOptions<T>): T | undefined
```

将键值对数据储存在应用磁盘中。如果给定的key已经存在于[PersistenceV2](../../../ui/state-management-static/arkts-static-new-persistencev2.md)中，返回对应的值；否则，会通过获取默认值的构造器构造默认值，并返回。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PersistenceV2-static globalConnect<T extends object>(params: ConnectOptions<T>): T | undefined--><!--Device-PersistenceV2-static globalConnect<T extends object>(params: ConnectOptions<T>): T | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| params | [ConnectOptions](../../apis-ability-kit/arkts-apis/arkts-ability-common-connectoptions-t.md)&lt;T&gt; | Yes | application-level storage parameters. |

**Return value:**

| Type | Description |
| --- | --- |
| T | the value of the existed key or the default value |

## keys

```TypeScript
static keys(): string[]
```

获取PersistenceV2中所有的key。

> **说明：**
> 
> key在Array中的顺序是无序的，与key插入到PersistenceV2中的顺序无关。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PersistenceV2-static keys(): string[]--><!--Device-PersistenceV2-static keys(): string[]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| string[] | the array of all keys. |

## notifyOnError

```TypeScript
static notifyOnError(callback: PersistenceErrorCallback | undefined): void
```

在持久化失败时调用。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PersistenceV2-static notifyOnError(callback: PersistenceErrorCallback | undefined): void--><!--Device-PersistenceV2-static notifyOnError(callback: PersistenceErrorCallback | undefined): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [PersistenceErrorCallback](arkts-arkui-persistenceerrorcallback-t.md) \| undefined | Yes | 持久化失败时调用。 |

## remove

```TypeScript
static remove(keyOrType: string | Class): void
```

将指定的键值对数据从PersistenceV2里面删除。如果指定的键值不存在于PersistenceV2中，将删除失败。

> **说明：**
> 
> 删除PersistenceV2中不存在的key会打印warn日志警告。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PersistenceV2-static remove(keyOrType: string | Class): void--><!--Device-PersistenceV2-static remove(keyOrType: string | Class): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| keyOrType | string \| Class | Yes | 需要删除的key。如果传入的是Class类型，则删除的key为Class类型入参的name。 |

## save

```TypeScript
static save(keyOrType: string | Class): void
```

手动持久化指定的键值对数据。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PersistenceV2-static save(keyOrType: string | Class): void--><!--Device-PersistenceV2-static save(keyOrType: string | Class): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| keyOrType | string \| Class | Yes | 需要持久化的key；如果指定的是Class类型，持久化的key为Class的name。 |

