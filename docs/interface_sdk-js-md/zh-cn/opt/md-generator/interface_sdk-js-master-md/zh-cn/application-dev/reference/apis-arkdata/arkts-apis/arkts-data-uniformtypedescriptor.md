# @ohos.data.uniformTypeDescriptor(标准化数据定义与描述)

本模块对标准化数据类型进行了抽象定义与描述，用于统一表示和管理各类数据类型的层级与归属关系（如JPEG归属于IMAGE、IMAGE归属于MEDIA等），便于跨模块/跨应用的一致化数据交互。详细设计原理参见  
[UTD预置列表](../../../database/uniform-data-type-list.md)。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-declare namespace uniformTypeDescriptor--><!--Device-unnamed-declare namespace uniformTypeDescriptor-End-->

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

## 汇总

### 函数

| 名称 |
| --- |
| [getTypeDescriptor](arkts-arkdata-uniformtypedescriptor-gettypedescriptor-f.md#gettypedescriptor) |
| [getUniformDataTypeByFilenameExtension](arkts-arkdata-uniformtypedescriptor-getuniformdatatypebyfilenameextension-f.md#getuniformdatatypebyfilenameextension) |
| [getUniformDataTypeByMIMEType](arkts-arkdata-uniformtypedescriptor-getuniformdatatypebymimetype-f.md#getuniformdatatypebymimetype) |
| [getUniformDataTypesByFilenameExtension](arkts-arkdata-uniformtypedescriptor-getuniformdatatypesbyfilenameextension-f.md#getuniformdatatypesbyfilenameextension) |
| [getUniformDataTypesByMIMEType](arkts-arkdata-uniformtypedescriptor-getuniformdatatypesbymimetype-f.md#getuniformdatatypesbymimetype) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [registerTypeDescriptors](arkts-arkdata-uniformtypedescriptor-registertypedescriptors-f-sys.md#registertypedescriptors) |
| [unregisterTypeDescriptors](arkts-arkdata-uniformtypedescriptor-unregistertypedescriptors-f-sys.md#unregistertypedescriptors) |
<!--DelEnd-->

### 类

| 名称 |
| --- |
| [TypeDescriptor](arkts-arkdata-uniformtypedescriptor-typedescriptor-c.md) |

### 枚举

| 名称 |
| --- |
| [UniformDataType](arkts-arkdata-uniformtypedescriptor-uniformdatatype-e.md) |
