# getUniformDataTypeByFilenameExtension

## getUniformDataTypeByFilenameExtension

```TypeScript
function getUniformDataTypeByFilenameExtension(filenameExtension: string, belongsTo?: string): string
```

根据给定的文件后缀名和所归属的标准化数据类型查询标准化数据类型ID，若有多个符合条件的标准化数据类型ID，则返回第一个。

**起始版本：** 23

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-uniformTypeDescriptor-function getUniformDataTypeByFilenameExtension(filenameExtension: string, belongsTo?: string): string--><!--Device-uniformTypeDescriptor-function getUniformDataTypeByFilenameExtension(filenameExtension: string, belongsTo?: string): string-End-->

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| filenameExtension | string | 是 |
| [belongsTo](arkts-arkdata-uniformtypedescriptor-typedescriptor-c.md) | string | 否 |

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## 示例

```TypeScript
import { uniformTypeDescriptor } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let typeId = uniformTypeDescriptor.getUniformDataTypeByFilenameExtension('.ts', 'general.source-code');
  if (typeId) {
    console.info('typeId is general.type-script');
  }
} catch (e) {
  let error: BusinessError = e as BusinessError;
  console.error(`getUniformDataTypeByFilenameExtension throws an exception. code is ${error.code}, message is ${error.message} `);
}

// 根据“.myts”，“general.plain-text”查不到预置数据类型则按返回根据入参信息生成的动态类型。
try {
  let typeId = uniformTypeDescriptor.getUniformDataTypeByFilenameExtension('.myts', 'general.plain-text');
  if (typeId) {
    console.info('typeId is flex.************');
  }
} catch (e) {
  let error: BusinessError = e as BusinessError;
  console.error(`getUniformDataTypeByFilenameExtension throws an exception. code is ${error.code}, message is ${error.message} `);
}
```
