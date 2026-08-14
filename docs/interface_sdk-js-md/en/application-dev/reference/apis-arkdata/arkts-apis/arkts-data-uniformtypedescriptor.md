# @ohos.data.uniformTypeDescriptor

/*
 Copyright (c) 2023-2026 Huawei Device Co., Ltd.
 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at
 http://www.apache.org/licenses/LICENSE-2.0
 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
 /


**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare namespace uniformTypeDescriptor--><!--Device-unnamed-declare namespace uniformTypeDescriptor-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## Modules to Import

```TypeScript
import { uniformTypeDescriptor } from 'uniformTypeDescriptor';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [getTypeDescriptor](arkts-arkdata-uniformtypedescriptor-gettypedescriptor-f.md#getTypeDescriptor) | Obtains the **TypeDescriptor** object based on the uniform data type ID. |
| [getTypeDescriptor](arkts-arkdata-uniformtypedescriptor-gettypedescriptor-f.md#getTypeDescriptor) | Queries and returns the uniform type descriptor by the given uniform data type ID. |
| [getUniformDataTypeByFilenameExtension](arkts-arkdata-uniformtypedescriptor-getuniformdatatypebyfilenameextension-f.md#getUniformDataTypeByFilenameExtension) | Obtains the uniform data type ID based on the given file name extension and data type. If there are multiple uniform data type IDs matching the conditions, the first one is returned. |
| [getUniformDataTypeByMIMEType](arkts-arkdata-uniformtypedescriptor-getuniformdatatypebymimetype-f.md#getUniformDataTypeByMIMEType) | Obtains the uniform data type ID based on the given MIME type and data type. If there are multiple uniform data type IDs matching the conditions, the first one is returned. |
| [getUniformDataTypesByFilenameExtension](arkts-arkdata-uniformtypedescriptor-getuniformdatatypesbyfilenameextension-f.md#getUniformDataTypesByFilenameExtension) | Obtains the uniform data type IDs based on the given file name extension and data type. |
| [getUniformDataTypesByMIMEType](arkts-arkdata-uniformtypedescriptor-getuniformdatatypesbymimetype-f.md#getUniformDataTypesByMIMEType) | Obtains the uniform data type IDs based on the given MIME type and data type. |

<!--Del-->
### Functions（系统接口）

| Name | Description |
| --- | --- |
| [registerTypeDescriptors](arkts-arkdata-uniformtypedescriptor-registertypedescriptors-f-sys.md#registerTypeDescriptors) | Register type descriptors into the system. |
| [unregisterTypeDescriptors](arkts-arkdata-uniformtypedescriptor-unregistertypedescriptors-f-sys.md#unregisterTypeDescriptors) | Unregister one or more type descriptors from the system by the given type IDs. |
<!--DelEnd-->

### Classes

| Name | Description |
| --- | --- |
| [TypeDescriptor](arkts-arkdata-uniformtypedescriptor-typedescriptor-c.md) | Represents a class for defining a uniform data type. It provides properties and methods for describing a uniform data type and its relationship with other uniform data types. |

### Enums

| Name | Description |
| --- | --- |
| [UniformDataType](arkts-arkdata-uniformtypedescriptor-uniformdatatype-e.md) | Enumerates the uniform data types. Some data types are related. For example, the JPEG type belongs to the IMAGE type. For more preset data types, see [Preset UTD List]. The following table lists the common uniform data types. |

