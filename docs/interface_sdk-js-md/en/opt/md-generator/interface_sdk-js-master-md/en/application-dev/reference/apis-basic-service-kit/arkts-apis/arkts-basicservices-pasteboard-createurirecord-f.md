# createUriRecord

## Modules to Import

```TypeScript
import { pasteboard } from '@kit.BasicServicesKit';
```

## createUriRecord

```TypeScript
function createUriRecord(uri: string): PasteDataRecord
```

Creates a **PasteDataRecord** object of the URI type.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [createRecord](arkts-basicservices-pasteboard-createrecord-f.md#createRecord)(mimeType: string, value: ValueType)

<!--Device-pasteboard-function createUriRecord(uri: string): PasteDataRecord--><!--Device-pasteboard-function createUriRecord(uri: string): PasteDataRecord-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [PasteDataRecord](arkts-basicservices-pasteboard-pastedatarecord-i.md) |

## Examples

```TypeScript
let record: pasteboard.PasteDataRecord = pasteboard.createUriRecord('dataability:///com.example.myapplication1/user.txt');
```
