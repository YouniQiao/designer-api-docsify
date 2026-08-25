# FieldNode

表示 Schema 实例的节点，提供定义存储在数据库中的值的方法。

**起始版本：** 9

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

## 导入模块

```TypeScript
import { distributedKVStore } from 'kits/@kit.ArkData';
```

## appendChild

```TypeScript
appendChild(child: FieldNode): boolean
```

在当前 FieldNode 中添加一个子节点。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [child](../../apis-arkui/arkts-components/arkts-arkui-nestedscrollinfo-i.md) | [FieldNode](arkts-arkdata-distributeddata-fieldnode-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## constructor

```TypeScript
constructor(name: string)
```

用于创建带有string字段FieldNode实例的构造函数。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## default

```TypeScript
default: string
```

表示FieldNode的默认值。default需传入type对应类型可解析的字符串字面量，确保内容类型与type字段类型一致。

**类型：** string

**起始版本：** 9

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

## nullable

```TypeScript
set nullable(isnullable: boolean)
```

设置数据库字段是否为空.

**类型：** boolean

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

## type

```TypeScript
set type(type: number)
```

设置节点对应的数据类型。

**类型：** number

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore
