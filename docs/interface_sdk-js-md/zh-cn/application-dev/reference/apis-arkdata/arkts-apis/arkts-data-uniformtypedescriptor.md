# @ohos.data.uniformTypeDescriptor(标准化数据定义与描述)

本模块对标准化数据类型进行了抽象定义与描述，用于统一表示和管理各类数据类型的层级与归属关系（如JPEG归属于IMAGE、IMAGE归属于MEDIA等），便于跨模块/跨应用的一致化数据交互。详细设计原理参见 [UTD预置列表](../../../database/uniform-data-type-list.md)。

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

## 导入模块

```TypeScript
import { uniformTypeDescriptor } from '@kit.ArkData';
```

## 汇总

### 函数

| 名称 |
| --- |
| [getTypeDescriptor(标准化数据定义与描述)](arkts-arkdata-uniformtypedescriptor-gettypedescriptor-f.md) |
| [getTypeDescriptor(标准化数据定义与描述)](arkts-arkdata-uniformtypedescriptor-gettypedescriptor-f.md) |
| [getUniformDataTypeByFilenameExtension(标准化数据定义与描述)](arkts-arkdata-uniformtypedescriptor-getuniformdatatypebyfilenameextension-f.md) |
| [getUniformDataTypeByMIMEType(标准化数据定义与描述)](arkts-arkdata-uniformtypedescriptor-getuniformdatatypebymimetype-f.md) |
| [getUniformDataTypesByFilenameExtension(标准化数据定义与描述)](arkts-arkdata-uniformtypedescriptor-getuniformdatatypesbyfilenameextension-f.md) |
| [getUniformDataTypesByMIMEType(标准化数据定义与描述)](arkts-arkdata-uniformtypedescriptor-getuniformdatatypesbymimetype-f.md) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [registerTypeDescriptors(标准化数据定义与描述)](arkts-arkdata-uniformtypedescriptor-registertypedescriptors-f-sys.md) |
| [unregisterTypeDescriptors(标准化数据定义与描述)](arkts-arkdata-uniformtypedescriptor-unregistertypedescriptors-f-sys.md) |
<!--DelEnd-->

### 类

| 名称 |
| --- |
| [TypeDescriptor(标准化数据定义与描述)](arkts-arkdata-uniformtypedescriptor-typedescriptor-c.md) |

### 枚举

| 名称 |
| --- |
| [UniformDataType(标准化数据定义与描述)](arkts-arkdata-uniformtypedescriptor-uniformdatatype-e.md) |
