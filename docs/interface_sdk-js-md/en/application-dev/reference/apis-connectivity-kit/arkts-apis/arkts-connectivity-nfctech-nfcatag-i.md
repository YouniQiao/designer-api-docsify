# NfcATag

Provides APIs to access NFC-A (ISO 14443-3A) properties and perform I/O operations on a tag. This class inherits from **[TagSession](arkts-connectivity-tagsession-tagsession-i.md)**.  
**TagSession** is the base class of all NFC tag technologies. It provides common interfaces for establishing connections and transferring data. For more details, see [TagSession](arkts-connectivity-tagsession-tagsession-i.md).For details about how to obtain an **NfcATag** object, see [NFC Tag Read/Write Development](../../../connectivity/nfc/nfc-tag-access-guide.md).The following describes the unique APIs of **NfcATag**.

**Inheritance/Implementation:** NfcATag extends TagSession

**Since:** 7

**System capability:** SystemCapability.Communication.NFC.Tag

## getAtqa

```TypeScript
getAtqa(): number[]
```

Obtains the ATQA value of this NFC-A tag.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Communication.NFC.Tag

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number[] |

## getSak

```TypeScript
getSak(): number
```

Obtains the SAK value of this NFC-A tag.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Communication.NFC.Tag

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |
