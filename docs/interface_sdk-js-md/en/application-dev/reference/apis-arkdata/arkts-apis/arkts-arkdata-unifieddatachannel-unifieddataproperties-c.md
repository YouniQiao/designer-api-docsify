# UnifiedDataProperties

Defines the properties of the data records in the unified data object, including the timestamp, tag, pasting range, and additional data.

**Since:** 23

<!--Device-unifiedDataChannel-class UnifiedDataProperties--><!--Device-unifiedDataChannel-class UnifiedDataProperties-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## Modules to Import

```TypeScript
import { unifiedDataChannel } from '@kit.ArkData';
```

## extras

```TypeScript
extras?: Record<string, RecordData>
```

extra property data. key-value pairs.

**Type:** Record&lt;string, [RecordData](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-recorddata-t.md)&gt;

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-UnifiedDataProperties-extras?: Record<string, RecordData>--><!--Device-UnifiedDataProperties-extras?: Record<string, RecordData>-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## getDelayData

```TypeScript
getDelayData?: GetDelayData
```

Callback for obtaining the deferred data. Currently, it can be used only in the pasteboard application of the same device. The default value is **undefined**.

**Type:** [GetDelayData](arkts-arkdata-unifieddatachannel-getdelaydata-t.md)

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-UnifiedDataProperties-getDelayData?: GetDelayData--><!--Device-UnifiedDataProperties-getDelayData?: GetDelayData-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## shareOptions

```TypeScript
shareOptions?: ShareOptions
```

Range, in which [UnifiedData](#unifieddataproperties) can be used. The default value is **CROSS_APP**.

**Type:** [ShareOptions](arkts-arkdata-unifieddatachannel-shareoptions-e.md)

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-UnifiedDataProperties-shareOptions?: ShareOptions--><!--Device-UnifiedDataProperties-shareOptions?: ShareOptions-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## tag

```TypeScript
tag?: string
```

Customized tag. The default value is an empty string.

**Type:** string

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-UnifiedDataProperties-tag?: string--><!--Device-UnifiedDataProperties-tag?: string-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## timestamp

```TypeScript
readonly timestamp?: Date
```

Timestamp when [UnifiedData](#unifieddataproperties) is generated. The default value is January 1, 1970 (UTC).

**Type:** Date

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-UnifiedDataProperties-readonly timestamp?: Date--><!--Device-UnifiedDataProperties-readonly timestamp?: Date-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## uriAuthorizationPolicies

```TypeScript
uriAuthorizationPolicies?: Array<UriPermission>
```

Defines URI authorization policies for drag intention.

**Type:** Array&lt;[UriPermission](arkts-arkdata-unifieddatachannel-uripermission-e.md)&gt;

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-UnifiedDataProperties-uriAuthorizationPolicies?: Array<UriPermission>--><!--Device-UnifiedDataProperties-uriAuthorizationPolicies?: Array<UriPermission>-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

**Examples**

```TypeScript
import { uniformDataStruct, uniformTypeDescriptor } from '@kit.ArkData';

let properties = new unifiedDataChannel.UnifiedDataProperties();
properties.extras = {
  key: {
    title: 'MyTitle',
    content: 'MyContent'
  }
};
properties.tag = "This is a tag of properties";
properties.shareOptions = unifiedDataChannel.ShareOptions.CROSS_APP;
properties.getDelayData = ((type: string) => {
  if (type == uniformTypeDescriptor.UniformDataType.PLAIN_TEXT) {
    let plainTextDetails : Record<string, string> = {
      'attr1': 'value1',
      'attr2': 'value2'
    }
    let plainText : uniformDataStruct.PlainText = {
      uniformDataType: 'general.plain-text',
      textContent : 'This is a plain text example',
      abstract : 'This is abstract',
      details : plainTextDetails
    }
    let text = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT, plainText);
    let textData = new unifiedDataChannel.UnifiedData(text);
    return textData;
  }
  return new unifiedDataChannel.UnifiedData();
});
```

