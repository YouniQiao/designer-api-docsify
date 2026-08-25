# convertRecordsToEntries

## Modules to Import

```TypeScript
import { unifiedDataChannel } from 'kits/@kit.ArkData';
```

## convertRecordsToEntries

```TypeScript
function convertRecordsToEntries(data: UnifiedData): void
```

Converts the provided data into a multi-style data structure, which is useful when the original data uses multiple records to represent different styles of the same data.This API is used only when the following rules are met:
1. The number of records in data is greater than 1.
2. The value of **unifiedData.properties.tag** is **records_to_entries_data_format**.

**Since:** 17

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 17.

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| data | [UnifiedData](../../apis-arkui/arkts-components/arkts-arkui-unifieddata-t.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
