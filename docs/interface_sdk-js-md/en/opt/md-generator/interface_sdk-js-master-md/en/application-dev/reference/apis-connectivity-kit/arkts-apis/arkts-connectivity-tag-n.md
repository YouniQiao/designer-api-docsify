# tag

Provides methods to operate or manage NFC tag.

**Since:** 12

<!--Device-unnamed-declare namespace tag--><!--Device-unnamed-declare namespace tag-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

## Modules to Import

```TypeScript
import { tag } from 'kits/@kit.ConnectivityKit';
```

## Summary

### Namespaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ndef](arkts-connectivity-tag-ndef-n.md) |

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [getNfcATag](arkts-connectivity-tag-getnfcatag-f.md#getnfcatag) |
| [getNfcA](arkts-connectivity-tag-getnfca-f.md#getnfca) |
| [getNfcBTag](arkts-connectivity-tag-getnfcbtag-f.md#getnfcbtag) |
| [getNfcB](arkts-connectivity-tag-getnfcb-f.md#getnfcb) |
| [getNfcFTag](arkts-connectivity-tag-getnfcftag-f.md#getnfcftag) |
| [getNfcF](arkts-connectivity-tag-getnfcf-f.md#getnfcf) |
| [getNfcVTag](arkts-connectivity-tag-getnfcvtag-f.md#getnfcvtag) |
| [getNfcV](arkts-connectivity-tag-getnfcv-f.md#getnfcv) |
| [getIsoDep](arkts-connectivity-tag-getisodep-f.md#getisodep) |
| [getNdef](arkts-connectivity-tag-getndef-f.md#getndef) |
| [getMifareClassic](arkts-connectivity-tag-getmifareclassic-f.md#getmifareclassic) |
| [getMifareUltralight](arkts-connectivity-tag-getmifareultralight-f.md#getmifareultralight) |
| [getNdefFormatable](arkts-connectivity-tag-getndefformatable-f.md#getndefformatable) |
| [getBarcodeTag](arkts-connectivity-tag-getbarcodetag-f.md#getbarcodetag) |
| [getTagInfo](arkts-connectivity-tag-gettaginfo-f.md#gettaginfo) |
| [registerForegroundDispatch](arkts-connectivity-tag-registerforegrounddispatch-f.md#registerforegrounddispatch) |
| [unregisterForegroundDispatch](arkts-connectivity-tag-unregisterforegrounddispatch-f.md#unregisterforegrounddispatch) |
| [on](arkts-connectivity-tag-on-f.md#on) |
| [off](arkts-connectivity-tag-off-f.md#off) |
| [on](arkts-connectivity-tag-on-f.md#on-1) |
| [off](arkts-connectivity-tag-off-f.md#off-1) |

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
| [NFC_A](arkts-connectivity-tag-con.md#nfc_a) |
| [NFC_B](arkts-connectivity-tag-con.md#nfc_b) |
| [ISO_DEP](arkts-connectivity-tag-con.md#iso_dep) |
| [NFC_F](arkts-connectivity-tag-con.md#nfc_f) |
| [NFC_V](arkts-connectivity-tag-con.md#nfc_v) |
| [NDEF](arkts-connectivity-tag-con.md#ndef) |
| [NDEF_FORMATABLE](arkts-connectivity-tag-con.md#ndef_formatable) |
| [MIFARE_CLASSIC](arkts-connectivity-tag-con.md#mifare_classic) |
| [MIFARE_ULTRALIGHT](arkts-connectivity-tag-con.md#mifare_ultralight) |
| [NFC_BARCODE](arkts-connectivity-tag-con.md#nfc_barcode) |
| [RTD_TEXT](arkts-connectivity-tag-con.md#rtd_text) |
| [RTD_URI](arkts-connectivity-tag-con.md#rtd_uri) |
| [SKIP_NDEF](arkts-connectivity-tag-con.md#skip_ndef) |
