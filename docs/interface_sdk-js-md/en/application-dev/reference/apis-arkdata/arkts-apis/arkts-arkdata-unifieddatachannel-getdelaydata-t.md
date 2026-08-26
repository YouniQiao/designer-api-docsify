# GetDelayData

```TypeScript
type GetDelayData = (type: string) => UnifiedData
```

Defines a function used to obtain a deferred **UnifiedData** object. Currently, it can be used only in the pasteboard application of the same device.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | string | Yes | Identifier of the deferred encapsulation. |

**Return value:**

| Type | Description |
| --- | --- |
| [UnifiedData](../../apis-arkui/arkts-components/arkts-arkui-unifieddata-t.md) | UnifiedData** object. |

**Examples**

```TypeScript
import { uniformDataStruct, uniformTypeDescriptor } from '@kit.ArkData';

let getDelayData: unifiedDataChannel.GetDelayData = ((type: string) => {
  if (type == uniformTypeDescriptor.UniformDataType.PLAIN_TEXT) {
    let plainTextDetails: Record<string, string> = {
      'attr1': 'value1',
      'attr2': 'value2'
    };
    let plainText: uniformDataStruct.PlainText = {
      uniformDataType: 'general.plain-text',
      textContent: 'This is a plain text example',
      abstract: 'This is abstract',
      details: plainTextDetails
    };
    let text = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT, plainText);
    let textData = new unifiedDataChannel.UnifiedData(text);
    return textData;
  }
  return new unifiedDataChannel.UnifiedData();
});
```
