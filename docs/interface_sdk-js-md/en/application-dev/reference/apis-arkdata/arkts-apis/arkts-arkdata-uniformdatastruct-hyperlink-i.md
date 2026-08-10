# Hyperlink

超链接类型数据，用于描述和管理超链接信息。创建Hyperlink对象后，可用于拖拽、分享等场景，实现跨应用的超链接数据传递和跳转。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-uniformDataStruct-interface Hyperlink--><!--Device-uniformDataStruct-interface Hyperlink-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## Modules to Import

```TypeScript
import { uniformDataStruct } from 'kits/@kit.ArkData';
```

## description

```TypeScript
description?: string
```

链接内容描述，非必填字段。当需要为超链接提供文字描述时传入此参数（如用于可访问性、链接预览等场景），不传入时默认值为空字符串，不提供描述信息。

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Hyperlink-description?: string--><!--Device-Hyperlink-description?: string-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## details

```TypeScript
details?: Record<string, string>
```

字典类型对象，key和value均为string类型，用于描述Hyperlink的详细属性内容。非必填字段，默认值为空字典对象。例如，可生成一个details内容为

{

"title":"标题",

"content":"内容"

}

的数据对象。当需要存储额外的超链接属性信息时传入此参数，不传入时默认值为空字典对象，不提供额外属性。

**Type:** [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, string&gt;

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Hyperlink-details?: Record<string, string>--><!--Device-Hyperlink-details?: Record<string, string>-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## uniformDataType

```TypeScript
readonly uniformDataType: 'general.hyperlink'
```

统一数据类型标识为超链接类型数据，固定为“general.hyperlink”，数据类型描述信息见  
[UniformDataType](arkts-arkdata-uniformtypedescriptor-uniformdatatype-e.md)。

**Type:** 'general.hyperlink'

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Hyperlink-readonly uniformDataType: 'general.hyperlink'--><!--Device-Hyperlink-readonly uniformDataType: 'general.hyperlink'-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## url

```TypeScript
url: string
```

链接URL地址，支持http、https等协议，需符合标准URL格式。例如：`https://www.example.com`或`file:///path/to/file`。

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Hyperlink-url: string--><!--Device-Hyperlink-url: string-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

