# createRecord

## Modules to Import

```TypeScript
import { pasteboard } from 'kits/@kit.BasicServicesKit';
```

## createRecord

```TypeScript
function createRecord(mimeType: string, value: ValueType): PasteDataRecord
```

创建一条指定类型的数据内容条目，将数据内容封装为PasteDataRecord对象。调用此方法后，系统将根据MIME类型封装数据内容，返回可添加到PasteData中的条目对象。参数mimeType长度不能超过1024字节，value类型需与mimeType对应（如mimeType为MIMETYPE_TEXT_PLAIN，则value类型必须是string），参数不能为空。

- 创建的条目通常需要通过[addRecord](arkts-basicservices-pasteboard-pastedata-i.md#addrecord)方法添加到  
 [PasteData](arkts-basicservices-pasteboard-pastedata-i.md)对象中才能生效。  
- 典型使用流程：先通过[createData](arkts-basicservices-pasteboard-createdata-f.md#createdata)创建PasteData对象，  
 再使用createRecord创建条目，最后通过addRecord添加条目。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-pasteboard-function createRecord(mimeType: string, value: ValueType): PasteDataRecord--><!--Device-pasteboard-function createRecord(mimeType: string, value: ValueType): PasteDataRecord-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mimeType | string | Yes | 剪贴板数据对应的MIME类型，可以是 [常量](../../../reference/apis-basic-services-kit/js-apis-pasteboard.md#常量)中已定义的类型， 包括HTML类型，Want类型，纯文本类型，URI类型，PixelMap类型；也可以是自定义的MIME类型，开发者可自定义此参数值，mimeType长度不能超过1024字节。 |
| value | [ValueType](arkts-basicservices-pasteboard-valuetype-t.md) | Yes | 指定类型对应的数据内容。建议根据实际场景选择合适的数据类型，避免使用过大的数据对象以免影响剪贴板性能和内存占用。 对于ArrayBuffer类型，建议合理设置数据大小；对于PixelMap类型，建议及时释放不再使用的对象。 |

**Return value:**

| Type | Description |
| --- | --- |
| [PasteDataRecord](arkts-basicservices-pasteboard-pastedatarecord-i.md) | 一条新建的指定类型的数据内容条目。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |

