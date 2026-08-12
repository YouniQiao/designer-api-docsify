# Storage（系统接口）

持久化存储后端接口，提供基于键值对（key-value）的数据持久化能力，包括数据的读取、写入、清除和删除。PersistentStorage通过该接口实现AppStorage数据的本地持久化，适用于需要对应用数据进行灵活本地持久化存储的场景。

**起始版本：** 7

<!--Device-unnamed-declare class Storage--><!--Device-unnamed-declare class Storage-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

## clear

```TypeScript
clear(): void
```

清除所有存储数据。

**起始版本：** 7

<!--Device-Storage-clear(): void--><!--Device-Storage-clear(): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

## constructor

```TypeScript
constructor(needCrossThread?: boolean, file?: string)
```

创建Storage实例的构造函数。

**起始版本：** 7

<!--Device-Storage-constructor(needCrossThread?: boolean, file?: string)--><!--Device-Storage-constructor(needCrossThread?: boolean, file?: string)-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| needCrossThread | boolean | 否 |
| [file](../../apis-core-file-kit/arkts-apis/arkts-corefile-storagestatistics-storagestats-i-sys.md) | string | 否 |

## delete

```TypeScript
delete(key: string): void
```

删除指定key对应的存储数据。

**起始版本：** 7

<!--Device-Storage-delete(key: string): void--><!--Device-Storage-delete(key: string): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | string | 是 |

## get

```TypeScript
get(key: string): string | undefined
```

根据指定key从磁盘中读取对应的存储数据。

**起始版本：** 7

<!--Device-Storage-get(key: string): string | undefined--><!--Device-Storage-get(key: string): string | undefined-End-->

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | string | 是 |

**返回值：**

| 类型 |
| --- |
| string |

## set

```TypeScript
set(key: string, val: any): void
```

将指定key对应的数据持久化存储到磁盘。

**起始版本：** 7

<!--Device-Storage-set(key: string, val: any): void--><!--Device-Storage-set(key: string, val: any): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | string | 是 |
| val | any | 是 |
