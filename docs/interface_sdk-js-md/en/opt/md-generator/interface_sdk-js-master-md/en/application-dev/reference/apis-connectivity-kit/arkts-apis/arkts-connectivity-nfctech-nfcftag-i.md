# NfcFTag

Provides methods for creating an NFC-F tag, obtaining tag information, and controlling tag read and write. &lt;p&gt;This class inherits from the TagSession abstract class and provides interfaces to create an {@code NfcFTag} and obtain the tag information.

**Inheritance/Implementation:** NfcFTag extends TagSession

**Since:** 23

<!--Device-unnamed-export interface NfcFTag--><!--Device-unnamed-export interface NfcFTag-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

## getPmm

```TypeScript
getPmm(): number[]
```

Obtains the PMm (consisting of the IC code and manufacturer parameters) from this {@code NfcFTag} instance.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-NfcFTag-getPmm(): int[]--><!--Device-NfcFTag-getPmm(): int[]-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number[] |

**Examples**

```TypeScript
import { tag } from '@kit.ConnectivityKit';

// Obtain the correct nfcF tag by using the tag.TagInfo API in @ohos.nfc.tag.
let pmm : number[] = nfcF.getPmm();
console.info("nfcF pmm: " + pmm);
```

## getSystemCode

```TypeScript
getSystemCode(): number[]
```

Obtains the system code from this {@code NfcFTag} instance.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-NfcFTag-getSystemCode(): int[]--><!--Device-NfcFTag-getSystemCode(): int[]-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number[] |

**Examples**

```TypeScript
import { tag } from '@kit.ConnectivityKit';

// Obtain the correct nfcF tag by using the tag.TagInfo API in @ohos.nfc.tag.
let systemCode : number[] = nfcF.getSystemCode();
console.info("nfcF systemCode: " + systemCode);
```
