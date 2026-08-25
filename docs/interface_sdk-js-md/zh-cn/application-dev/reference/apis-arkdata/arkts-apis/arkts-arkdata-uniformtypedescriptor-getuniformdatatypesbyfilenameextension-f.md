# getUniformDataTypesByFilenameExtension

## 导入模块

```TypeScript
import { uniformTypeDescriptor } from 'kits/@kit.ArkData';
```

## getUniformDataTypesByFilenameExtension

```TypeScript
function getUniformDataTypesByFilenameExtension(filenameExtension: string, belongsTo?: string): Array<string>
```

根据给定的文件后缀名和所归属的标准化数据类型查询标准化数据类型ID列表。

**起始版本：** 13

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| filenameExtension | string | 是 |
| [belongsTo](arkts-arkdata-uniformtypedescriptor-typedescriptor-c.md) | string | 否 |

**返回值：**

| 类型 |
| --- |
| Array & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
