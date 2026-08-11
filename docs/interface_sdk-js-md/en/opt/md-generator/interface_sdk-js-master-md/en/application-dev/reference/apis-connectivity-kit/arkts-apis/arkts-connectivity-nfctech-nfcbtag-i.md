# NfcBTag

Provides interfaces to create an {@code NfcBTag} and perform I/O operations on the tag.&lt;p&gt;This class inherits from the {@link TagSession} abstract class and provides interfaces to create an{@code NfcBTag} and obtain the tag information.

**Inheritance/Implementation:** NfcBTag extends [TagSession](arkts-connectivity-tagsession-tagsession-i.md)

**Since:** 12

<!--Device-unnamed-export interface NfcBTag extends TagSession--><!--Device-unnamed-export interface NfcBTag extends TagSession-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

## getRespAppData

```TypeScript
getRespAppData(): number[]
```

Obtains the application data of a tag.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NfcBTag-getRespAppData(): int[]--><!--Device-NfcBTag-getRespAppData(): int[]-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number[] |

## getRespProtocol

```TypeScript
getRespProtocol(): number[]
```

Obtains the protocol information of a tag.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NfcBTag-getRespProtocol(): int[]--><!--Device-NfcBTag-getRespProtocol(): int[]-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number[] |
