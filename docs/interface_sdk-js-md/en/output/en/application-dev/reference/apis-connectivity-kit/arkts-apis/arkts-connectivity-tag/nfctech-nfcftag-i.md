# NfcFTag

Provides methods for creating an NFC-F tag, obtaining tag information, and controlling tag read and write. \_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_This class inherits from the \_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ abstract class and provides interfaces to create an {@code NfcFTag} and obtain the tag information.

**Inheritance/Implementation:** NfcFTag extends [TagSession](tagsession-tagsession-i.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-unnamed-export interface NfcFTag extends TagSession--><!--Device-unnamed-export interface NfcFTag extends TagSession-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

## getPmm

ArkTS-Dyn:
```TypeScript
getPmm(): number[]
```

ArkTS-Sta:
```TypeScript
getPmm(): int[]
```

Obtains the PMm (consisting of the IC code and manufacturer parameters) from this {@code NfcFTag} instance.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NfcFTag-getPmm(): int[]--><!--Device-NfcFTag-getPmm(): int[]-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number[]  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int[] | Returns the PMm. |

## getSystemCode

ArkTS-Dyn:
```TypeScript
getSystemCode(): number[]
```

ArkTS-Sta:
```TypeScript
getSystemCode(): int[]
```

Obtains the system code from this {@code NfcFTag} instance.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NfcFTag-getSystemCode(): int[]--><!--Device-NfcFTag-getSystemCode(): int[]-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number[]  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int[] | Returns the system code. |

