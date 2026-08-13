# tag

Provides methods to operate or manage NFC tag.

**Since:** 23

**Deprecated since:** -1

<!--Device-unnamed-declare namespace tag--><!--Device-unnamed-declare namespace tag-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

## Modules to Import

```TypeScript
import { tag } from '@kit.ConnectivityKit';
```

## Summary

### Namespaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ndef](arkts-connectivity-tag-ndef-n.md) |

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [getNfcATag](arkts-connectivity-tag-getnfcatag-f.md#getNfcATag) |
| [getNfcA](arkts-connectivity-tag-getnfca-f.md#getNfcA) |
| [getNfcBTag](arkts-connectivity-tag-getnfcbtag-f.md#getNfcBTag) |
| [getNfcB](arkts-connectivity-tag-getnfcb-f.md#getNfcB) |
| [getNfcFTag](arkts-connectivity-tag-getnfcftag-f.md#getNfcFTag) |
| [getNfcF](arkts-connectivity-tag-getnfcf-f.md#getNfcF) |
| [getNfcVTag](arkts-connectivity-tag-getnfcvtag-f.md#getNfcVTag) |
| [getNfcV](arkts-connectivity-tag-getnfcv-f.md#getNfcV) |
| [getIsoDep](arkts-connectivity-tag-getisodep-f.md#getIsoDep) |
| [getNdef](arkts-connectivity-tag-getndef-f.md#getNdef) |
| [getMifareClassic](arkts-connectivity-tag-getmifareclassic-f.md#getMifareClassic) |
| [getMifareUltralight](arkts-connectivity-tag-getmifareultralight-f.md#getMifareUltralight) |
| [getNdefFormatable](arkts-connectivity-tag-getndefformatable-f.md#getNdefFormatable) |
| [getBarcodeTag](arkts-connectivity-tag-getbarcodetag-f.md#getBarcodeTag) |
| [getTagInfo](arkts-connectivity-tag-gettaginfo-f.md#getTagInfo) |
| [registerForegroundDispatch](arkts-connectivity-tag-registerforegrounddispatch-f.md#registerForegroundDispatch) |
| [unregisterForegroundDispatch](arkts-connectivity-tag-unregisterforegrounddispatch-f.md#unregisterForegroundDispatch) |
| [on_readerMode](arkts-connectivity-tag-onreadermode-f.md) |
| [onReaderMode](arkts-connectivity-tag-onreadermode-f.md#onReaderMode) |
| [off_readerMode](arkts-connectivity-tag-offreadermode-f.md) |
| [offReaderMode](arkts-connectivity-tag-offreadermode-f.md#offReaderMode) |
| [on_readerModeWithInterval](arkts-connectivity-tag-onreadermodewithinterval-f.md) |
| [onReaderModeWithInterval](arkts-connectivity-tag-onreadermodewithinterval-f.md#onReaderModeWithInterval) |
| [off_readerModeWithInterval](arkts-connectivity-tag-offreadermodewithinterval-f.md) |
| [offReaderModeWithInterval](arkts-connectivity-tag-offreadermodewithinterval-f.md#offReaderModeWithInterval) |

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [TagInfo](arkts-connectivity-tag-taginfo-i.md) |
| [NdefRecord](arkts-connectivity-tag-ndefrecord-i.md) |

<!--Del-->
### Interfaces（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [TagInfo](arkts-connectivity-tag-taginfo-i-sys.md) |
<!--DelEnd-->

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [TnfType](arkts-connectivity-tag-tnftype-e.md) |
| [NfcForumType](arkts-connectivity-tag-nfcforumtype-e.md) |
| [MifareClassicType](arkts-connectivity-tag-mifareclassictype-e.md) |
| [MifareClassicSize](arkts-connectivity-tag-mifareclassicsize-e.md) |
| [MifareUltralightType](arkts-connectivity-tag-mifareultralighttype-e.md) |

### Types

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [NfcATag](arkts-connectivity-tag-nfcatag-t.md) |
| [NfcBTag](arkts-connectivity-tag-nfcbtag-t.md) |
| [NfcFTag](arkts-connectivity-tag-nfcftag-t.md) |
| [NfcVTag](arkts-connectivity-tag-nfcvtag-t.md) |
| [IsoDepTag](arkts-connectivity-tag-isodeptag-t.md) |
| [NdefTag](arkts-connectivity-tag-ndeftag-t.md) |
| [MifareClassicTag](arkts-connectivity-tag-mifareclassictag-t.md) |
| [MifareUltralightTag](arkts-connectivity-tag-mifareultralighttag-t.md) |
| [NdefFormatableTag](arkts-connectivity-tag-ndefformatabletag-t.md) |
| [BarcodeTag](arkts-connectivity-tag-barcodetag-t.md) |
| [NdefMessage](arkts-connectivity-tag-ndefmessage-t.md) |
| [TagSession](arkts-connectivity-tag-tagsession-t.md) |

### Constants

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [NFC_A](arkts-connectivity-tag-con.md#NFC_A) |
| [NFC_B](arkts-connectivity-tag-con.md#NFC_B) |
| [ISO_DEP](arkts-connectivity-tag-con.md#ISO_DEP) |
| [NFC_F](arkts-connectivity-tag-con.md#NFC_F) |
| [NFC_V](arkts-connectivity-tag-con.md#NFC_V) |
| [NDEF](arkts-connectivity-tag-con.md#NDEF) |
| [NDEF_FORMATABLE](arkts-connectivity-tag-con.md#NDEF_FORMATABLE) |
| [MIFARE_CLASSIC](arkts-connectivity-tag-con.md#MIFARE_CLASSIC) |
| [MIFARE_ULTRALIGHT](arkts-connectivity-tag-con.md#MIFARE_ULTRALIGHT) |
| [NFC_BARCODE](arkts-connectivity-tag-con.md#NFC_BARCODE) |
| [RTD_TEXT](arkts-connectivity-tag-con.md#RTD_TEXT) |
| [RTD_URI](arkts-connectivity-tag-con.md#RTD_URI) |
| [SKIP_NDEF](arkts-connectivity-tag-con.md#SKIP_NDEF) |
