# createPlainTextRecord

## Modules to Import

```TypeScript
import { pasteboard } from 'pasteboard';
```

## createPlainTextRecord

```TypeScript
function createPlainTextRecord(text: string): PasteDataRecord
```

Creates a **PasteDataRecord** object of the plain text type.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [createRecord](arkts-basicservices-pasteboard-createrecord-f.md#createRecord)(mimeType: string, value: ValueType)

<!--Device-pasteboard-function createPlainTextRecord(text: string): PasteDataRecord--><!--Device-pasteboard-function createPlainTextRecord(text: string): PasteDataRecord-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| text | string | Yes | Plain text. |

**Return value:**

| Type | Description |
| --- | --- |
| [PasteDataRecord](arkts-basicservices-pasteboard-pastedatarecord-i.md) | New **PasteDataRecord** object of the plain text type. |

## Examples

```TypeScript
let record: pasteboard.PasteDataRecord = pasteboard.createPlainTextRecord('hello');
```

