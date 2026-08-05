# NfcBTag

Provides interfaces to create an {@code NfcBTag} and perform I/O operations on the tag. \_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_This class inherits from the \_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ abstract class and provides interfaces to create an {@code NfcBTag} and obtain the tag information.

**Inheritance/Implementation:** NfcBTag extends [TagSession](tagsession-tagsession-i.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-unnamed-export interface NfcBTag extends TagSession--><!--Device-unnamed-export interface NfcBTag extends TagSession-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

## getRespAppData

ArkTS-Dyn:
```TypeScript
getRespAppData(): number[]
```

ArkTS-Sta:
```TypeScript
getRespAppData(): int[]
```

Obtains the application data of a tag.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NfcBTag-getRespAppData(): int[]--><!--Device-NfcBTag-getRespAppData(): int[]-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number[]  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int[] | Returns the application data of the tag. |

## getRespProtocol

ArkTS-Dyn:
```TypeScript
getRespProtocol(): number[]
```

ArkTS-Sta:
```TypeScript
getRespProtocol(): int[]
```

Obtains the protocol information of a tag.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NfcBTag-getRespProtocol(): int[]--><!--Device-NfcBTag-getRespProtocol(): int[]-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number[]  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int[] | Returns the protocol information of the tag. |

