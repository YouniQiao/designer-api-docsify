# NfcVTag

Provides methods for creating an NFC-V tag, obtaining tag information, and controlling tag read and write.&lt;p&gt;This class inherits from the {@link TagSession} abstract class and provides interfaces to create an{@code NfcVTag} and obtain the tag information.

**Inheritance/Implementation:** NfcVTag extends [TagSession](arkts-connectivity-tagsession-tagsession-i.md)

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
| ArkTS-Dyn: number  <br>ArkTS-Sta：int | Returns the response flags. |

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
| ArkTS-Dyn: number  <br>ArkTS-Sta：int | Returns the response flags. |

