# FileUri

Represents data of the file URI type.

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

<!--Device-uniformDataStruct-interface FileUri--><!--Device-uniformDataStruct-interface FileUri-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## Modules to Import

```TypeScript
import { uniformDataStruct } from 'kits/@kit.ArkData';
```

## details

```TypeScript
details?: Record<string, int | long | double | string | Uint8Array>
```

Object of the dictionary type used to describe the icon. The key is of the string type, and the value can be a number, a string, or a Uint8Array. By default, it is an empty dictionary object.

**Type:** ArkTS-Dyn: [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, number \| number \| number \| string \| Uint8Array&gt;  <br>ArkTS-Sta：[Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, int \| long \| double \| string \| Uint8Array&gt;

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FileUri-details?: Record<string, int | long | double | string | Uint8Array>--><!--Device-FileUri-details?: Record<string, int | long | double | string | Uint8Array>-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## fileType

```TypeScript
fileType: string
```

File type, which must be UTD. For details, see [Prebuilt UTDs]. The maximum length of the value is 1024 bytes.

**Type:** string

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FileUri-fileType: string--><!--Device-FileUri-fileType: string-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## oriUri

```TypeScript
oriUri: string
```

File path.

**Type:** string

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FileUri-oriUri: string--><!--Device-FileUri-oriUri: string-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## uniformDataType

```TypeScript
readonly uniformDataType: 'general.file-uri'
```

Uniform data type, which has a fixed value of **general.file-uri**. For details, see   
[UniformDataType](arkts-arkdata-uniformtypedescriptor-uniformdatatype-e.md).

**Type:** 'general.file-uri'

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FileUri-readonly uniformDataType: 'general.file-uri'--><!--Device-FileUri-readonly uniformDataType: 'general.file-uri'-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## uriAuthorizationPolicies

```TypeScript
uriAuthorizationPolicies?: Array<int>
```

Defines URI authorization policies for drag intention.

**Type:** ArkTS-Dyn: Array&lt;number&gt;  <br>ArkTS-Sta：Array&lt;int&gt;

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FileUri-uriAuthorizationPolicies?: Array<int>--><!--Device-FileUri-uriAuthorizationPolicies?: Array<int>-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

