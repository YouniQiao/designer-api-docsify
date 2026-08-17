# NfcVTag

Provides methods for creating an NFC-V tag, obtaining tag information, and controlling tag read and write. &lt;p&gt;This class inherits from the TagSession abstract class and provides interfaces to create an {@code NfcVTag} and obtain the tag information.

**Inheritance/Implementation:** NfcVTag extends TagSession

**Since:** 23

<!--Device-unnamed-export interface NfcVTag--><!--Device-unnamed-export interface NfcVTag-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

## getDsfId

```TypeScript
getDsfId(): int
```

Obtains the response flags from this {@code NfcVTag} instance.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-NfcVTag-getDsfId(): int--><!--Device-NfcVTag-getDsfId(): int-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Return value:**

| Type | Description |
| --- | --- |
| int | Returns the response flags. |

**Examples**

```TypeScript
import { tag } from '@kit.ConnectivityKit';

// Obtain the correct nfcV tag by using the tag.TagInfo API in @ohos.nfc.tag.
let dsfId : number = nfcV.getDsfId();
console.info("nfcV dsfId: " + dsfId);
```

## getResponseFlags

```TypeScript
getResponseFlags(): int
```

Obtains the response flags from this {@code NfcVTag} instance.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-NfcVTag-getResponseFlags(): int--><!--Device-NfcVTag-getResponseFlags(): int-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Return value:**

| Type | Description |
| --- | --- |
| int | Returns the response flags. |

**Examples**

```TypeScript
import { tag } from '@kit.ConnectivityKit';

// Obtain the correct nfcV tag by using the tag.TagInfo API in @ohos.nfc.tag.
let responseFlags : number = nfcV.getResponseFlags();
console.info("nfcV responseFlags: " + responseFlags);
```

