# NfcATag

Provides interfaces to control the read and write of tags that support the NFC-A technology. &lt;p&gt;This class is inherited from the TagSession abstract class, and provides methods to create {@code NfcATag} objects and obtain the ATQA and SAK.

**Inheritance/Implementation:** NfcATag extends TagSession

**Since:** 23

<!--Device-unnamed-export interface NfcATag--><!--Device-unnamed-export interface NfcATag-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

## getAtqa

```TypeScript
getAtqa(): number[]
```

Obtains the ATQA of an NFC-A tag.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-NfcATag-getAtqa(): int[]--><!--Device-NfcATag-getAtqa(): int[]-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number[] |

**Examples**

```TypeScript
import { tag } from '@kit.ConnectivityKit';

// Obtain the correct nfcA tag by using the tag.TagInfo API in @ohos.nfc.tag.
let atqa : number[] = nfcA.getAtqa();
console.info("nfcA atqa: " + atqa);
```

## getSak

```TypeScript
getSak(): number
```

Obtains the SAK of an NFC-A tag.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-NfcATag-getSak(): int--><!--Device-NfcATag-getSak(): int-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Examples**

```TypeScript
import { tag } from '@kit.ConnectivityKit';

// Obtain the correct nfcA tag by using the tag.TagInfo API in @ohos.nfc.tag.
let sak : number = nfcA.getSak();
console.info("nfcA sak: " + sak);
```
