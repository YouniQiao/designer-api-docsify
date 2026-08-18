# NfcBTag

Provides interfaces to create an {@code NfcBTag} and perform I/O operations on the tag. &lt;p&gt;This class inherits from the TagSession abstract class and provides interfaces to create an {@code NfcBTag} and obtain the tag information.

**Inheritance/Implementation:** NfcBTag extends TagSession

**Since:** 23

<!--Device-unnamed-export interface NfcBTag--><!--Device-unnamed-export interface NfcBTag-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

## getRespAppData

```TypeScript
getRespAppData(): number[]
```

Obtains the application data of a tag.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-NfcBTag-getRespAppData(): int[]--><!--Device-NfcBTag-getRespAppData(): int[]-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number[] |

**Examples**

```TypeScript
import { tag } from '@kit.ConnectivityKit';

// Obtain the correct nfcB tag by using the tag.TagInfo API in @ohos.nfc.tag.
let respAppData : number[] = nfcB.getRespAppData();
console.info("nfcB respAppData: " + respAppData);
```

## getRespProtocol

```TypeScript
getRespProtocol(): number[]
```

Obtains the protocol information of a tag.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-NfcBTag-getRespProtocol(): int[]--><!--Device-NfcBTag-getRespProtocol(): int[]-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number[] |

**Examples**

```TypeScript
import { tag } from '@kit.ConnectivityKit';

// Obtain the correct nfcB tag by using the tag.TagInfo API in @ohos.nfc.tag.
let respProtocol : number[] = nfcB.getRespProtocol();
console.info("nfcB respProtocol: " + respProtocol);
```
