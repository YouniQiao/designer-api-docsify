# ndef

Provides methods for accessing NDEF tag.

**Since:** 23

<!--Device-tag-namespace ndef--><!--Device-tag-namespace ndef-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

## Modules to Import

```TypeScript
import { tag } from '@kit.ConnectivityKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [makeUriRecord](arkts-connectivity-ndef-makeurirecord-f.md) | Creates an NDEF record based on the specified URI. |
| [makeTextRecord](arkts-connectivity-ndef-maketextrecord-f.md) | Creates an NDEF record based on the specified text data and language type. |
| [makeMimeRecord](arkts-connectivity-ndef-makemimerecord-f.md) | Creates an NDEF record based on the specified MIME data and type. |
| [makeExternalRecord](arkts-connectivity-ndef-makeexternalrecord-f.md) | Creates an NDEF record based on application-specific data. |
| [createNdefMessage](arkts-connectivity-ndef-createndefmessage-f.md) | Creates an NDEF message from raw byte data. The data must comply with the NDEF record format. Otherwise, the NDEF record list contained in the **NdefMessage** object will be empty. |
| [createNdefMessageByData](arkts-connectivity-ndef-createndefmessagebydata-f.md) | Creates an NDEF message with raw bytes. |
| [createNdefMessage](arkts-connectivity-ndef-createndefmessage-f.md) | Creates an NDEF message from the NDEF records list. |
| [createNdefMessageByRecords](arkts-connectivity-ndef-createndefmessagebyrecords-f.md) | Creates an NDEF message with record list. |
| [messageToBytes](arkts-connectivity-ndef-messagetobytes-f.md) | Converts an NDEF message to bytes. |
| [makeApplicationRecord](arkts-connectivity-ndef-makeapplicationrecord-f.md) | Creates an NDEF record based on the specified application bundle name. |

