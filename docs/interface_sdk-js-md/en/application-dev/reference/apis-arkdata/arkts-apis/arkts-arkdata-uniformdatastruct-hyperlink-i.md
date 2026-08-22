# Hyperlink

Represents data of the hyperlink type.

**Since:** 23

<!--Device-uniformDataStruct-interface Hyperlink--><!--Device-uniformDataStruct-interface Hyperlink-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## Modules to Import

```TypeScript
import { uniformDataStruct } from '@kit.ArkData';
```

## description

```TypeScript
description?: string
```

Description of the linked content. This parameter is optional. By default, it is an empty string.

**Type:** string

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-Hyperlink-description?: string--><!--Device-Hyperlink-description?: string-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## details

```TypeScript
details?: Record<string, string>
```

Object of the dictionary type used to describe the attributes of the hyperlink. Both the key and value of the object are of the string type. For example, the following is a **details** object used to describe the properties of a file:

{

"title":"Title of the file",

"content":"Content of the file"

}

By default, it is an empty dictionary object.

**Type:** Record&lt;string, string&gt;

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-Hyperlink-details?: Record<string, string>--><!--Device-Hyperlink-details?: Record<string, string>-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## uniformDataType

```TypeScript
readonly uniformDataType: 'general.hyperlink'
```

Uniform data type, which has a fixed value of **general.hyperlink**. For details, see [UniformDataType](arkts-arkdata-uniformtypedescriptor-uniformdatatype-e.md).

**Type:** 'general.hyperlink'

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-Hyperlink-readonly uniformDataType: 'general.hyperlink'--><!--Device-Hyperlink-readonly uniformDataType: 'general.hyperlink'-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## url

```TypeScript
url: string
```

URL.

**Type:** string

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-Hyperlink-url: string--><!--Device-Hyperlink-url: string-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

**Examples**

```TypeScript
import { unifiedDataChannel, uniformTypeDescriptor } from '@kit.ArkData';
let hyperlinkDetails : Record<string, string> = {
  'attr1': 'value1',
  'attr2': 'value2'
}
let hyperlink : uniformDataStruct.Hyperlink = {
  uniformDataType:'general.hyperlink',
  url : 'www.XXX.com',
  description : 'This is the description of this hyperlink',
  details : hyperlinkDetails
}
console.info('hyperlink.uniformDataType: ' + hyperlink.uniformDataType);
let record = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.HYPERLINK, hyperlink);
```

