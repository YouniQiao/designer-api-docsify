# getTypeDescriptor

## 导入模块

```TypeScript
import { uniformTypeDescriptor } from 'kits/@kit.ArkData';
```

## getTypeDescriptor

```TypeScript
function getTypeDescriptor(typeId: string): TypeDescriptor
```

按给定的标准化数据类型ID查询并返回对应的标准化数据类型描述类对象。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [typeId](arkts-arkdata-uniformtypedescriptor-typedescriptor-c.md) | string | 是 |

**返回值：**

| 类型 |
| --- |
| [TypeDescriptor](arkts-arkdata-uniformtypedescriptor-typedescriptor-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
