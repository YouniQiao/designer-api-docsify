# NfcATag

Provides interfaces to control the read and write of tags that support the NFC-A technology.\_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_This class is inherited from the \_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ abstract class, and provides methods to create{@code NfcATag} objects and obtain the ATQA and SAK.

**Inheritance/Implementation:** NfcATag extends [TagSession](tagsession-tagsession-i.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-unnamed-export interface NfcATag extends TagSession--><!--Device-unnamed-export interface NfcATag extends TagSession-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

## getAtqa

ArkTS-Dyn:
```TypeScript
getAtqa(): number[]
```

ArkTS-Sta:
```TypeScript
getAtqa(): int[]
```

Obtains the ATQA of an NFC-A tag.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NfcATag-getAtqa(): int[]--><!--Device-NfcATag-getAtqa(): int[]-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number[]  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int[] | Returns the ATQA of the NFC-A tag. |

## getSak

ArkTS-Dyn:
```TypeScript
getSak(): number
```

ArkTS-Sta:
```TypeScript
getSak(): int
```

Obtains the SAK of an NFC-A tag.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NfcATag-getSak(): int--><!--Device-NfcATag-getSak(): int-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | Returns the SAK of the NFC-A tag. |

