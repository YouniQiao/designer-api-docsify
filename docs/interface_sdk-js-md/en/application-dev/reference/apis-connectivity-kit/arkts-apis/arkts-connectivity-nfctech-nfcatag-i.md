# NfcATag

Provides interfaces to control the read and write of tags that support the NFC-A technology.&lt;p&gt;This class is inherited from the [TagSession](TagSession) abstract class, and provides methods to create{@code NfcATag} objects and obtain the ATQA and SAK.

**Inheritance/Implementation:** NfcATag extends [TagSession](TagSession)

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
| ArkTS-Dyn: number[]  <br>ArkTS-Sta：int[] | Returns the ATQA of the NFC-A tag. |

## Examples

```TypeScript
import { tag } from '@kit.ConnectivityKit';

// Obtain the correct nfcA tag by using the tag.TagInfo API in @ohos.nfc.tag.
let atqa : number[] = nfcA.getAtqa();
console.info("nfcA atqa: " + atqa);
```

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
| ArkTS-Dyn: number  <br>ArkTS-Sta：int | Returns the SAK of the NFC-A tag. |

## Examples

```TypeScript
import { tag } from '@kit.ConnectivityKit';

// Obtain the correct nfcA tag by using the tag.TagInfo API in @ohos.nfc.tag.
let sak : number = nfcA.getSak();
console.info("nfcA sak: " + sak);
```

