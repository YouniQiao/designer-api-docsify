# create

## 导入模块

```TypeScript
import { distributedDataObject } from 'kits/@kit.ArkData';
```

## create

```TypeScript
function create(context: Context, source: object): DataObject
```

创建一个分布式数据对象。对象属性支持基本类型（数字类型、布尔类型和字符串类型）以及复杂类型（数组、基本类型嵌套）。

**起始版本：** 9

**系统能力：** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-arkui/arkts-components/arkts-arkui-context-t.md) | 是 |
| source | object | 是 |

**返回值：**

| 类型 |
| --- |
| [DataObject](arkts-arkdata-distributeddataobject-dataobject-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
