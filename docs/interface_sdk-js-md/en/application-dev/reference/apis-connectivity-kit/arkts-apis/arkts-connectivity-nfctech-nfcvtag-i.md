# NfcVTag

Provides APIs to access NFC-V (ISO 15693) properties and perform I/O operations on a tag. This class inherits from **TagSession**.  
**TagSession** is the base class of all NFC tag technologies. It provides common interfaces for establishing connections and transferring data. For more details, see [TagSession](arkts-connectivity-tagsession-tagsession-i.md).For details about how to obtain an **NfcVTag** object, see [NFC Tag Read/Write Development](../../../connectivity/nfc/nfc-tag-access-guide.md).The following describes the unique APIs of **NfcVTag**.

**Inheritance/Implementation:** NfcVTag extends TagSession

**Since:** 7

**System capability:** SystemCapability.Communication.NFC.Tag

## getDsfId

```TypeScript
getDsfId(): number
```

Obtains the data storage format identifier (DSFID) from this NFC-V tag.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Communication.NFC.Tag

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getResponseFlags

```TypeScript
getResponseFlags(): number
```

Obtains the response flags from this NFC-V tag.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Communication.NFC.Tag

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |
