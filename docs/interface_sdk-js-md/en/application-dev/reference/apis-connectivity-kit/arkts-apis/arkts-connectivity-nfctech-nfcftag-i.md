# NfcFTag

Provides methods for creating an NFC-F tag, obtaining tag information, and controlling tag read and write. &lt;p&gt;This class inherits from the TagSession abstract class and provides interfaces to create an {@code NfcFTag} and obtain the tag information.

**Inheritance/Implementation:** NfcFTag extends TagSession

**Since:** 23

<!--Device-unnamed-export interface NfcFTag--><!--Device-unnamed-export interface NfcFTag-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

## getPmm

```TypeScript
getPmm(): int[]
```

Obtains the PMm (consisting of the IC code and manufacturer parameters) from this {@code NfcFTag} instance.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-NfcFTag-getPmm(): int[]--><!--Device-NfcFTag-getPmm(): int[]-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Return value:**

| Type | Description |
| --- | --- |
| int[] | Returns the PMm. |

**Examples**

```TypeScript
import { tag } from '@kit.ConnectivityKit';

// Obtain the correct nfcF tag by using the tag.TagInfo API in @ohos.nfc.tag.
let pmm : number[] = nfcF.getPmm();
console.info("nfcF pmm: " + pmm);
```

## getSystemCode

```TypeScript
getSystemCode(): int[]
```

Obtains the system code from this {@code NfcFTag} instance.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-NfcFTag-getSystemCode(): int[]--><!--Device-NfcFTag-getSystemCode(): int[]-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Return value:**

| Type | Description |
| --- | --- |
| int[] | Returns the system code. |

**Examples**

```TypeScript
import { tag } from '@kit.ConnectivityKit';

// Obtain the correct nfcF tag by using the tag.TagInfo API in @ohos.nfc.tag.
let systemCode : number[] = nfcF.getSystemCode();
console.info("nfcF systemCode: " + systemCode);
```

