# Storage (System API)

持久化存储后端接口，提供基于键值对（key-value）的数据持久化能力，包括数据的读取、写入、清除和删除。PersistentStorage通过该接口实现AppStorage数据的本地持久化，适用于需要对应用数据进行灵活本地持久化存储的场景。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

<!--Device-unnamed-declare class Storage--><!--Device-unnamed-declare class Storage-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## clear

```TypeScript
clear(): void
```

清除所有存储数据。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

<!--Device-Storage-clear(): void--><!--Device-Storage-clear(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## constructor

```TypeScript
constructor(needCrossThread?: boolean, file?: string)
```

创建Storage实例的构造函数。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

<!--Device-Storage-constructor(needCrossThread?: boolean, file?: string)--><!--Device-Storage-constructor(needCrossThread?: boolean, file?: string)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| needCrossThread | boolean | No | 是否需要跨线程访问存储。预留接口，暂不提供具体功能。 |
| file | string | No | 指定存储文件名。预留接口，暂不提供具体功能。默认使用应用文件目录下的persistent_storage作为存储文件。 |

## delete

```TypeScript
delete(key: string): void
```

删除指定key对应的存储数据。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

<!--Device-Storage-delete(key: string): void--><!--Device-Storage-delete(key: string): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes | 要删除的存储key名称。 |

## get

```TypeScript
get(key: string): string | undefined
```

根据指定key从磁盘中读取对应的存储数据。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

<!--Device-Storage-get(key: string): string | undefined--><!--Device-Storage-get(key: string): string | undefined-End-->

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes | 要获取的存储key名称。 |

**Return value:**

| Type | Description |
| --- | --- |
| string | key对应的值；key不存在时返回undefined。 |

## set

```TypeScript
set(key: string, val: any): void
```

将指定key对应的数据持久化存储到磁盘。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

<!--Device-Storage-set(key: string, val: any): void--><!--Device-Storage-set(key: string, val: any): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes | 要设置的存储key名称。 |
| val | any | Yes | 要存储的数据，支持string、number、boolean等基本类型以及可序列化的对象和数组，数据将被序列化后持久化到存储文件中。 |

