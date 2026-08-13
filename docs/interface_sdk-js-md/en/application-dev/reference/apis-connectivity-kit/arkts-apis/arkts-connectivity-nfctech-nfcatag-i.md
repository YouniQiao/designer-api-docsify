# NfcATag

Provides interfaces to control the read and write of tags that support the NFC-A technology. &lt;p&gt;This class is inherited from the TagSession abstract class, and provides methods to create {@code NfcATag} objects and obtain the ATQA and SAK.

**Inheritance/Implementation:** NfcATag extends TagSession

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-export interface NfcATag--><!--Device-unnamed-export interface NfcATag-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

## getAtqa

```TypeScript
getAtqa(): int[]
```

Obtains the ATQA of an NFC-A tag.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-NfcATag-getAtqa(): int[]--><!--Device-NfcATag-getAtqa(): int[]-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Return value:**

| Type | Description |
| --- | --- |
| int[] | Returns the ATQA of the NFC-A tag. |

## Examples

```TypeScript
import { tag } from '@kit.ConnectivityKit';

// Obtain the correct nfcA tag by using the tag.TagInfo API in @ohos.nfc.tag.
let atqa : number[] = nfcA.getAtqa();
console.info("nfcA atqa: " + atqa);
```

## getSak

```TypeScript
getSak(): int
```

Obtains the SAK of an NFC-A tag.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-NfcATag-getSak(): int--><!--Device-NfcATag-getSak(): int-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Return value:**

| Type | Description |
| --- | --- |
| int | Returns the SAK of the NFC-A tag. |

## Examples

```TypeScript
import { tag } from '@kit.ConnectivityKit';

// Obtain the correct nfcA tag by using the tag.TagInfo API in @ohos.nfc.tag.
let sak : number = nfcA.getSak();
console.info("nfcA sak: " + sak);
```

