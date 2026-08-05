# NfcVTag

Provides methods for creating an NFC-V tag, obtaining tag information, and controlling tag read and write. \_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_This class inherits from the \_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ abstract class and provides interfaces to create an {@code NfcVTag} and obtain the tag information.

**Inheritance/Implementation:** NfcVTag extends [TagSession](tagsession-tagsession-i.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-unnamed-export interface NfcVTag extends TagSession--><!--Device-unnamed-export interface NfcVTag extends TagSession-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

## getDsfId

ArkTS-Dyn:
```TypeScript
getDsfId(): number
```

ArkTS-Sta:
```TypeScript
getDsfId(): int
```

Obtains the response flags from this {@code NfcVTag} instance.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NfcVTag-getDsfId(): int--><!--Device-NfcVTag-getDsfId(): int-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | Returns the response flags. |

## getResponseFlags

ArkTS-Dyn:
```TypeScript
getResponseFlags(): number
```

ArkTS-Sta:
```TypeScript
getResponseFlags(): int
```

Obtains the response flags from this {@code NfcVTag} instance.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NfcVTag-getResponseFlags(): int--><!--Device-NfcVTag-getResponseFlags(): int-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | Returns the response flags. |

