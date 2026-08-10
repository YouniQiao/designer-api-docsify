# UnifiedRecord

对UDMF支持的数据内容的抽象定义，称为数据记录。一个统一数据对象内包含一条或多条数据记录，例如一条文本记录、一条图片记录、一条HTML记录等。从API version 15开始，支持往数据记录中增加同一内容的不同数据格式（例如同一文本可同时以纯文本、HTML或超链接等格式存储），数据使用方根据业务需要通过getEntry方法获取对应格式。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-unifiedDataChannel-class UnifiedRecord--><!--Device-unifiedDataChannel-class UnifiedRecord-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## Modules to Import

```TypeScript
import { unifiedDataChannel } from 'kits/@kit.ArkData';
```

## addEntry

```TypeScript
addEntry(type: string, value: ValueType): void
```

在当前数据记录中添加一条指定数据类型和内容的数据，通过该方法增加的数据类型和内容为同一内容的不同表现样式。调用成功后，指定的数据类型和内容被添加到当前数据记录中。

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-UnifiedRecord-addEntry(type: string, value: ValueType): void--><!--Device-UnifiedRecord-addEntry(type: string, value: ValueType): void-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | string | Yes | 要创建的数据类型，见 [UniformDataType](arkts-arkdata-uniformtypedescriptor-uniformdatatype-e.md)。 |
| value | [ValueType](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) | Yes | 要创建的数据的值。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes:1.Mandatory parameters are left unspecified; &lt;br&gt;2.Incorrect parameter types; &lt;br&gt;3. Parameter verification failed. |

## Examples

```TypeScript
import { uniformDataStruct, uniformTypeDescriptor } from '@kit.ArkData';

let fileUriDetails: Record<string, string> = {
  'attr1': 'value1',
  'attr2': 'value2'
};
let fileUri: uniformDataStruct.FileUri = {
  uniformDataType: 'general.file-uri',
  oriUri: 'file://data/image/1.png',
  fileType: 'general.image',
  details: fileUriDetails
};
let hyperlink: uniformDataStruct.Hyperlink = {
  uniformDataType: 'general.hyperlink',
  url: 'file://data/image/1.png',
  description: 'This is the description of the hyperlink'
};

let unifiedData = new unifiedDataChannel.UnifiedData();
let record = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.HYPERLINK, hyperlink);
record.addEntry(uniformTypeDescriptor.UniformDataType.FILE_URI, fileUri);
unifiedData.addRecord(record);
```

## constructor

```TypeScript
constructor()
```

用于创建数据记录。调用成功后，返回一个空的UnifiedRecord对象。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-UnifiedRecord-constructor()--><!--Device-UnifiedRecord-constructor()-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## Examples

```TypeScript
let unifiedRecord = new unifiedDataChannel.UnifiedRecord();
```

## constructor

```TypeScript
constructor(type: string, value: ValueType)
```

用于创建指定类型和值的数据记录。调用成功后，返回包含指定类型和值的UnifiedRecord对象。

当参数value为[image.PixelMap](../../apis-image-kit/arkts-apis/arkts-image-image-pixelmap-i.md/arkts-image-image-pixelmap-i.md)类型时，参数type必须对应为  
[UniformDataType](arkts-arkdata-uniformtypedescriptor-uniformdatatype-e.md)中OPENHARMONY_PIXEL_MAP的值；

当参数value为[Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md/arkts-ability-app-ability-want-want-c.md)类型时，参数type必须对应为  
[UniformDataType](arkts-arkdata-uniformtypedescriptor-uniformdatatype-e.md)中OPENHARMONY_WANT的值。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-UnifiedRecord-constructor(type: string, value: ValueType)--><!--Device-UnifiedRecord-constructor(type: string, value: ValueType)-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | string | Yes | 要创建的数据记录的类型，用于标识数据记录的具体类型。取值见 [UniformDataType](arkts-arkdata-uniformtypedescriptor-uniformdatatype-e.md)，如 'general.plain-text'、'general.hyperlink'等。 |
| value | [ValueType](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) | Yes | 要创建的数据记录的值。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes:1.Mandatory parameters are left unspecified; &lt;br&gt;2.Incorrect parameter types; &lt;br&gt;3.Parameter verification failed. |

## Examples

```TypeScript
import { uniformDataStruct, uniformTypeDescriptor } from '@kit.ArkData';
import { image } from '@kit.ImageKit';

let hyperlink: uniformDataStruct.Hyperlink = {
  uniformDataType: 'general.hyperlink',
  url: 'www.XXX.com',
  description: 'This is the description of the hyperlink'
};
let hyperlinkRecord = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.HYPERLINK, hyperlink);

let plainText: uniformDataStruct.PlainText = {
  uniformDataType: 'general.plain-text',
  textContent: 'This is a plain text example',
  abstract: 'This is abstract'
};
let text = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT, plainText);

let arrayBuffer = new ArrayBuffer(4 * 200 * 200);
let opt: image.InitializationOptions = {
  editable: true,
  pixelFormat: 3,
  size: { height: 200, width: 200 },
  alphaType: 3
};
let pixelMap: uniformDataStruct.PixelMap = {
  uniformDataType: 'openharmony.pixel-map',
  pixelMap: image.createPixelMapSync(arrayBuffer, opt)
};
let pixelMapRecord =
  new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.OPENHARMONY_PIXEL_MAP, pixelMap);
```

## getEntries

```TypeScript
getEntries(): Record<string, ValueType>
```

获取当前数据记录中所有数据的类型和内容。

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-UnifiedRecord-getEntries(): Record<string, ValueType>--><!--Device-UnifiedRecord-getEntries(): Record<string, ValueType>-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

**Return value:**

| Type | Description |
| --- | --- |
| [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, ValueType&gt; | 当前数据记录对应的类型和内容。 |

## Examples

```TypeScript
import { uniformDataStruct, uniformTypeDescriptor } from '@kit.ArkData';

let fileUriDetails : Record<string, string> = {
  'attr1': 'value1',
  'attr2': 'value2'
};
let fileUri : uniformDataStruct.FileUri = {
  uniformDataType : 'general.file-uri',
  oriUri : 'file://data/image/1.png',
  fileType : 'general.image',
  details : fileUriDetails
};
let formDetails : Record<string, string> = {
  'attr1': 'value1',
  'attr2': 'value2'
};
let form : uniformDataStruct.Form = {
  uniformDataType : 'openharmony.form',
  formId : 1,
  formName : 'form',
  bundleName : 'com.xx.app',
  abilityName : 'ability',
  module : 'module',
  details : formDetails
};

let unifiedData = new unifiedDataChannel.UnifiedData();
let record = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.OPENHARMONY_FORM, form);
record.addEntry(uniformTypeDescriptor.UniformDataType.FILE_URI, fileUri);
unifiedData.addRecord(record);

let records = unifiedData.getRecords();
for (let i = 0; i < records.length; i++) {
  let unifiedDataRecord = records[i] as unifiedDataChannel.UnifiedRecord;
  let entries : Record<string, unifiedDataChannel.ValueType> = unifiedDataRecord.getEntries();
  let formRead : uniformDataStruct.Form = entries[uniformTypeDescriptor.UniformDataType.OPENHARMONY_FORM] as uniformDataStruct.Form;
  if (formRead != undefined) {
    console.info(`formName: ${formRead.formName}`);
  }
  let fileUriRead : uniformDataStruct.FileUri = entries[uniformTypeDescriptor.UniformDataType.FILE_URI] as uniformDataStruct.FileUri;
  if (fileUriRead != undefined) {
    console.info(`oriUri: ${fileUriRead.oriUri}`);
  }
}
```

## getEntry

```TypeScript
getEntry(type: string): ValueType
```

通过数据类型获取数据记录中的数据内容。

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-UnifiedRecord-getEntry(type: string): ValueType--><!--Device-UnifiedRecord-getEntry(type: string): ValueType-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | string | Yes | 要获取数据的类型，见 [UniformDataType](arkts-arkdata-uniformtypedescriptor-uniformdatatype-e.md)。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ValueType](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) | 当前数据记录对应的值。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes:1.Mandatory parameters are left unspecified; &lt;br&gt;2.Incorrect parameter types; &lt;br&gt;3. Parameter verification failed. |

## Examples

```TypeScript
import { uniformDataStruct, uniformTypeDescriptor } from '@kit.ArkData';

let fileUriDetails: Record<string, string> = {
  'attr1': 'value1',
  'attr2': 'value2'
};
let fileUri: uniformDataStruct.FileUri = {
  uniformDataType: 'general.file-uri',
  oriUri: 'file://data/image/1.png',
  fileType: 'general.image',
  details: fileUriDetails
};
let formDetails: Record<string, string> = {
  'attr1': 'value1',
  'attr2': 'value2'
};
let form: uniformDataStruct.Form = {
  uniformDataType: 'openharmony.form',
  formId: 1,
  formName: 'form',
  bundleName: 'com.xx.app',
  abilityName: 'ability',
  module: 'module',
  details: formDetails
};

let unifiedData = new unifiedDataChannel.UnifiedData();
let record = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.OPENHARMONY_FORM, form);
record.addEntry(uniformTypeDescriptor.UniformDataType.FILE_URI, fileUri);
unifiedData.addRecord(record);

let records = unifiedData.getRecords();
for (let i = 0; i < records.length; i++) {
  let unifiedDataRecord = records[i] as unifiedDataChannel.UnifiedRecord;
  let fileUriRead: uniformDataStruct.FileUri =
    unifiedDataRecord.getEntry(uniformTypeDescriptor.UniformDataType.FILE_URI) as uniformDataStruct.FileUri;
  if (fileUriRead != undefined) {
    console.info(`oriUri: ${fileUriRead.oriUri}`);
  }
  let formRead =
    unifiedDataRecord.getEntry(uniformTypeDescriptor.UniformDataType.OPENHARMONY_FORM) as uniformDataStruct.Form;
  if (formRead != undefined) {
    console.info(`formName: ${formRead.formName}`);
  }
}
```

## getType

```TypeScript
getType(): string
```

获取当前数据记录的类型。由于从统一数据对象中调用[getRecords](arkts-arkdata-unifieddatachannel-unifieddata-c.md#getrecords)所取出的数据是UnifiedRecord对象，因此需要通过本接口查询此记录的具体类型，再将该UnifiedRecord对象转换为其子类，调用子类接口。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-UnifiedRecord-getType(): string--><!--Device-UnifiedRecord-getType(): string-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

**Return value:**

| Type | Description |
| --- | --- |
| string | 当前数据记录对应的具体数据类型，见 [UniformDataType]{ |

## Examples

```TypeScript
import { uniformDataStruct, uniformTypeDescriptor } from '@kit.ArkData';

let plainText: uniformDataStruct.PlainText = {
  uniformDataType: 'general.plain-text',
  textContent: 'This is a plain text example',
  abstract: 'This is abstract'
};
let text = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT, plainText);
let unifiedData = new unifiedDataChannel.UnifiedData(text);

let records = unifiedData.getRecords();
if (records[0].getType() == uniformTypeDescriptor.UniformDataType.PLAIN_TEXT) {
  let plainText = records[0] as unifiedDataChannel.PlainText;
  console.info(`textContent: ${plainText.textContent}`);
}
```

## getTypes

```TypeScript
getTypes(): Array<string>
```

获取数据记录中数据的所有类型集合。可通过UnifiedRecord数据记录对象调用本接口，查询出此记录中数据的所有类型集合，包括使用  
[addEntry](arkts-arkdata-unifieddatachannel-unifiedrecord-c.md#addentry)函数添加的数据类型。

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-UnifiedRecord-getTypes(): Array<string>--><!--Device-UnifiedRecord-getTypes(): Array<string>-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;string&gt; | [UniformDataType]{ |

## Examples

```TypeScript
import { uniformDataStruct, uniformTypeDescriptor } from '@kit.ArkData';

let fileUriDetails: Record<string, string> = {
  'attr1': 'value1',
  'attr2': 'value2'
};
let fileUri: uniformDataStruct.FileUri = {
  uniformDataType: 'general.file-uri',
  oriUri: 'file://data/image/1.png',
  fileType: 'general.image',
  details: fileUriDetails
};
let formDetails: Record<string, string> = {
  'attr1': 'value1',
  'attr2': 'value2'
};
let form: uniformDataStruct.Form = {
  uniformDataType: 'openharmony.form',
  formId: 1,
  formName: 'form',
  bundleName: 'com.xx.app',
  abilityName: 'ability',
  module: 'module',
  details: formDetails
};

let unifiedData = new unifiedDataChannel.UnifiedData();
let record = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.OPENHARMONY_FORM, form);
record.addEntry(uniformTypeDescriptor.UniformDataType.FILE_URI, fileUri);
unifiedData.addRecord(record);

let records = unifiedData.getRecords();
for (let i = 0; i < records.length; i++) {
  let unifiedDataRecord = records[i] as unifiedDataChannel.UnifiedRecord;
  let types: Array<string> = unifiedDataRecord.getTypes();
  if (types.includes(uniformTypeDescriptor.UniformDataType.OPENHARMONY_FORM)) {
    console.info(`Types include: ${uniformTypeDescriptor.UniformDataType.OPENHARMONY_FORM}`);
  }
};
```

## getValue

```TypeScript
getValue(): ValueType
```

获取当前数据记录的值。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-UnifiedRecord-getValue(): ValueType--><!--Device-UnifiedRecord-getValue(): ValueType-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

**Return value:**

| Type | Description |
| --- | --- |
| [ValueType](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) | 当前数据记录对应的值。 |

## Examples

```TypeScript
import { uniformDataStruct, uniformTypeDescriptor } from '@kit.ArkData';

let text =
  new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT, 'this is value of text');
let value = text.getValue();

let hyperlinkDetails: Record<string, string> = {
  'attr1': 'value1',
  'attr2': 'value2'
};
let hyperlink: uniformDataStruct.Hyperlink = {
  uniformDataType: 'general.hyperlink',
  url: 'www.XXX.com',
  description: 'This is the description of the hyperlink',
  details: hyperlinkDetails
};
let hyperlinkRecord = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.HYPERLINK, hyperlink);
let hyperlinkValue = hyperlinkRecord.getValue();
```

