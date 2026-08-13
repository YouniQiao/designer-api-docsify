# createWantRecord

## Modules to Import

```TypeScript
import { pasteboard } from '@kit.BasicServicesKit';
```

## createWantRecord

```TypeScript
function createWantRecord(want: Want): PasteDataRecord
```

Creates a **PasteDataRecord** object of the Want type.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [createRecord](arkts-basicservices-pasteboard-createrecord-f.md#createRecord)(mimeType: string, value: ValueType)

<!--Device-pasteboard-function createWantRecord(want: Want): PasteDataRecord--><!--Device-pasteboard-function createWantRecord(want: Want): PasteDataRecord-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [PasteDataRecord](arkts-basicservices-pasteboard-pastedatarecord-i.md) |

## Examples

```TypeScript
import { Want } from '@kit.AbilityKit';

let object: Want = {
    bundleName: "com.example.aafwk.test",
    abilityName: "com.example.aafwk.test.TwoAbility"
};
let record: pasteboard.PasteDataRecord = pasteboard.createWantRecord(object);
```
