# getTypeDescriptor

## getTypeDescriptor

```TypeScript
function getTypeDescriptor(typeId: string): TypeDescriptor
```

按给定的标准化数据类型ID查询并返回对应的标准化数据类型描述类对象。

**起始版本：** 11

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-uniformTypeDescriptor-function getTypeDescriptor(typeId: string): TypeDescriptor--><!--Device-uniformTypeDescriptor-function getTypeDescriptor(typeId: string): TypeDescriptor-End-->

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| typeId | string | 是 |

**返回值：**

| 类型 |
| --- |
| [TypeDescriptor](arkts-arkdata-uniformtypedescriptor-typedescriptor-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## 示例

```TypeScript
import { uniformTypeDescriptor } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  // 获取指定类型的TypeDescriptor对象
  let typeObj: uniformTypeDescriptor.TypeDescriptor =
    uniformTypeDescriptor.getTypeDescriptor('com.adobe.photoshop-image');
  if (typeObj) {
    let typeId = typeObj.typeId;
    let belongingToTypes = typeObj.belongingToTypes;
    let description = typeObj.description;
    let referenceURL = typeObj.referenceURL;
    let iconFile = typeObj.iconFile;
    let filenameExtensions = typeObj.filenameExtensions;
    let mimeTypes = typeObj.mimeTypes;
    console.info(`typeId: ${typeId}, belongingToTypes: ${belongingToTypes}, description: ${description}, referenceURL: ${referenceURL}, iconFile: ${iconFile}, filenameExtensions: ${filenameExtensions}, mimeTypes: ${mimeTypes}`);
  } else {
    console.info('type com.adobe.photoshop-image does not exist');
  }
} catch (e) {
  let error: BusinessError = e as BusinessError;
  console.error(`getTypeDescriptor throws an exception. code is ${error.code}, message is ${error.message} `);
}
```


## getTypeDescriptor

```TypeScript
function getTypeDescriptor(typeId: string): TypeDescriptor | null
```

按给定的标准化数据类型ID查询并返回对应的标准化数据类型描述类对象。

**起始版本：** 23

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-uniformTypeDescriptor-function getTypeDescriptor(typeId: string): TypeDescriptor | null--><!--Device-uniformTypeDescriptor-function getTypeDescriptor(typeId: string): TypeDescriptor | null-End-->

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| typeId | string | 是 |

**返回值：**

| 类型 |
| --- |
| [TypeDescriptor](arkts-arkdata-uniformtypedescriptor-typedescriptor-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
