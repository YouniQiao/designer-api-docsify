# tag

Provides methods to operate or manage NFC tag.

@namespace tag

**Since:** 23

<!--Device-unnamed-declare namespace tag--><!--Device-unnamed-declare namespace tag-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

## Modules to Import

```TypeScript
import { tag } from '@kit.ConnectivityKit';
```

## Summary

### Namespaces

| Name | Description |
| --- | --- |
| [ndef](arkts-connectivity-tag-ndef-n.md) | Provides methods for accessing NDEF tag. |

### Functions

| Name | Description |
| --- | --- |
| [getNfcATag](arkts-connectivity-tag-getnfcatag-f.md) | Obtains an [NfcATag](arkts-connectivity-tag-nfcatag-t.md) object based on the tag information. &lt;p&gt;During tag reading, if the tag supports the NFC-A technology, an [NfcATag](arkts-connectivity-tag-nfcatag-t.md) object will be created based on the tag information. |
| [getNfcA](arkts-connectivity-tag-getnfca-f.md) | Obtains an [NfcATag](arkts-connectivity-tag-nfcatag-t.md) object based on the tag information. During tag reading, if the tag supports the NFC-A technology, an [NfcATag](arkts-connectivity-tag-nfcatag-t.md) object will be created based on the tag information. |
| [getNfcBTag](arkts-connectivity-tag-getnfcbtag-f.md) | Obtains an [NfcBTag](arkts-connectivity-tag-nfcbtag-t.md) object based on the tag information. &lt;p&gt;During tag reading, if the tag supports the NFC-B technology, an [NfcBTag](arkts-connectivity-tag-nfcbtag-t.md) object will be created based on the tag information. |
| [getNfcB](arkts-connectivity-tag-getnfcb-f.md) | Obtains an [NfcBTag](arkts-connectivity-tag-nfcbtag-t.md) object based on the tag information. During tag reading, if the tag supports the NFC-B technology, an [NfcBTag](arkts-connectivity-tag-nfcbtag-t.md) object will be created based on the tag information. |
| [getNfcFTag](arkts-connectivity-tag-getnfcftag-f.md) | Obtains an [NfcFTag](arkts-connectivity-tag-nfcftag-t.md) object based on the tag information. &lt;p&gt;During tag reading, if the tag supports the NFC-F technology, an [NfcFTag](arkts-connectivity-tag-nfcftag-t.md) object will be created based on the tag information. |
| [getNfcF](arkts-connectivity-tag-getnfcf-f.md) | Obtains an [NfcFTag](arkts-connectivity-tag-nfcftag-t.md) object based on the tag information. During tag reading, if the tag supports the NFC-F technology, an [NfcFTag](arkts-connectivity-tag-nfcftag-t.md) object will be created based on the tag information. |
| [getNfcVTag](arkts-connectivity-tag-getnfcvtag-f.md) | Obtains an [NfcVTag](arkts-connectivity-tag-nfcvtag-t.md) object based on the tag information. &lt;p&gt;During tag reading, if the tag supports the NFC-V technology, an [NfcVTag](arkts-connectivity-tag-nfcvtag-t.md) object will be created based on the tag information. |
| [getNfcV](arkts-connectivity-tag-getnfcv-f.md) | Obtains an [NfcVTag](arkts-connectivity-tag-nfcvtag-t.md) object based on the tag information. During tag reading, if the tag supports the NFC-V technology, an [NfcVTag](arkts-connectivity-tag-nfcvtag-t.md) object will be created based on the tag information. |
| [getIsoDep](arkts-connectivity-tag-getisodep-f.md) | Obtains an [IsoDepTag](arkts-connectivity-tag-isodeptag-t.md) object based on the tag information. During tag reading, if the tag supports the IsoDep technology, an [IsoDepTag](arkts-connectivity-tag-isodeptag-t.md) object will be created based on the tag information. |
| [getNdef](arkts-connectivity-tag-getndef-f.md) | Obtains an [NdefTag](arkts-connectivity-tag-ndeftag-t.md) object based on the tag information. During tag reading, if the tag supports the NDEF technology, an [NdefTag](arkts-connectivity-tag-ndeftag-t.md) object will be created based on the tag information. |
| [getMifareClassic](arkts-connectivity-tag-getmifareclassic-f.md) | Obtains an [MifareClassicTag](arkts-connectivity-tag-mifareclassictag-t.md) object based on the tag information. During tag reading, if the tag supports the MIFARE Classic technology, an [MifareClassicTag](arkts-connectivity-tag-mifareclassictag-t.md) object will be created based on the tag information. |
| [getMifareUltralight](arkts-connectivity-tag-getmifareultralight-f.md) | Obtains an [MifareUltralightTag](arkts-connectivity-tag-mifareultralighttag-t.md) object based on the tag information. During tag reading, if the tag supports the MIFARE Ultralight technology, an [MifareUltralightTag](arkts-connectivity-tag-mifareultralighttag-t.md) object will be created based on the tag information. |
| [getNdefFormatable](arkts-connectivity-tag-getndefformatable-f.md) | Obtains an [NdefFormatableTag](arkts-connectivity-tag-ndefformatabletag-t.md) object based on the tag information. During tag reading, if the tag supports the NDEF Formatable technology, an [NdefFormatableTag](arkts-connectivity-tag-ndefformatabletag-t.md) object will be created based on the tag information. |
| [getBarcodeTag](arkts-connectivity-tag-getbarcodetag-f.md) | Obtains an [BarcodeTag](arkts-connectivity-tag-barcodetag-t.md) object based on the tag information. During tag reading, if the tag supports the NfcBarcode technology, an [BarcodeTag](arkts-connectivity-tag-barcodetag-t.md) object will be created. |
| [getTagInfo](arkts-connectivity-tag-gettaginfo-f.md) | Parse a [TagInfo](arkts-connectivity-tag-taginfo-i.md) object from Want. |
| [registerForegroundDispatch](arkts-connectivity-tag-registerforegrounddispatch-f.md) | Register tag foreground dispatch. Dispatches to this application only if a tag discovered. |
| [unregisterForegroundDispatch](arkts-connectivity-tag-unregisterforegrounddispatch-f.md) | Unregister tag foreground dispatch. |
| [on_readerMode](arkts-connectivity-tag-onreadermode-f.md) | Set reader mode enabled when the specific application is foreground. Dispatches to this application only if a tag discovered. |
| [onReaderMode](arkts-connectivity-tag-onreadermode-f.md) | Set reader mode enabled when the specific application is foreground. Dispatches to this application only if a tag discovered. |
| [off_readerMode](arkts-connectivity-tag-offreadermode-f.md) | Disable foreground reader mode settings explicitly. |
| [offReaderMode](arkts-connectivity-tag-offreadermode-f.md) | Disable foreground reader mode settings explicitly. |
| [on_readerModeWithInterval](arkts-connectivity-tag-onreadermodewithinterval-f.md) | Set reader mode enabled when the specific application is on foreground and set card presence interval. Tag infomation will be dispatched to the application only if a NFC tag is discovered. |
| [onReaderModeWithInterval](arkts-connectivity-tag-onreadermodewithinterval-f.md) | Set reader mode enabled when the specific application is on foreground and set card presence interval. Tag infomation will be dispatched to the application only if a NFC tag is discovered. |
| [off_readerModeWithInterval](arkts-connectivity-tag-offreadermodewithinterval-f.md) | Disable foreground reader mode settings explicitly. |
| [offReaderModeWithInterval](arkts-connectivity-tag-offreadermodewithinterval-f.md) | Disable foreground reader mode settings explicitly. |

### Interfaces

| Name | Description |
| --- | --- |
| [TagInfo](arkts-connectivity-tag-taginfo-i.md) | Provides tag information. &lt;p&gt;This class provides the technology a tag supports, for example, NFC-A. Applications can create different tags based on the supported technology. |
| [NdefRecord](arkts-connectivity-tag-ndefrecord-i.md) | NDEF records definition, see NFCForum-TS-NDEF_1.0. |

<!--Del-->
### Interfaces(System API)

| Name | Description |
| --- | --- |
| [TagInfo](arkts-connectivity-tag-taginfo-i-sys.md) | Provides tag information. &lt;p&gt;This class provides the technology a tag supports, for example, NFC-A. Applications can create different tags based on the supported technology. |
<!--DelEnd-->

### Enums

| Name | Description |
| --- | --- |
| [TnfType](arkts-connectivity-tag-tnftype-e.md) | TNF types definitions, see NFCForum-TS-NDEF_1.0. |
| [NfcForumType](arkts-connectivity-tag-nfcforumtype-e.md) | NfcForum Type definition. The NDEF tag may use one of them. |
| [MifareClassicType](arkts-connectivity-tag-mifareclassictype-e.md) | MifareClassic Type definition |
| [MifareClassicSize](arkts-connectivity-tag-mifareclassicsize-e.md) | MifareClassic Tag size. |
| [MifareUltralightType](arkts-connectivity-tag-mifareultralighttype-e.md) | MifareUltralight Type definition |

### Types

| Name | Description |
| --- | --- |
| [NfcATag](arkts-connectivity-tag-nfcatag-t.md) | Exports type NfcATag. |
| [NfcBTag](arkts-connectivity-tag-nfcbtag-t.md) | Exports type NfcBTag. |
| [NfcFTag](arkts-connectivity-tag-nfcftag-t.md) | Exports type NfcFTag. |
| [NfcVTag](arkts-connectivity-tag-nfcvtag-t.md) | Exports type NfcVTag. |
| [IsoDepTag](arkts-connectivity-tag-isodeptag-t.md) | Exports type IsoDepTag. |
| [NdefTag](arkts-connectivity-tag-ndeftag-t.md) | Exports type NdefTag. |
| [MifareClassicTag](arkts-connectivity-tag-mifareclassictag-t.md) | Exports type MifareClassicTag. |
| [MifareUltralightTag](arkts-connectivity-tag-mifareultralighttag-t.md) | Exports type MifareUltralightTag. |
| [NdefFormatableTag](arkts-connectivity-tag-ndefformatabletag-t.md) | Exports type NdefFormatableTag. |
| [BarcodeTag](arkts-connectivity-tag-barcodetag-t.md) | Exports type BarcodeTag. |
| [NdefMessage](arkts-connectivity-tag-ndefmessage-t.md) | Exports type NdefMessage. |
| [TagSession](arkts-connectivity-tag-tagsession-t.md) | Exports type TagSession. |

### Constants

| Name | Description |
| --- | --- |
| [NFC_A](arkts-connectivity-tag-con.md#nfc_a) | Indicates an NFC-A tag. The value should be an integer. |
| [NFC_B](arkts-connectivity-tag-con.md#nfc_b) | Indicates an NFC-B tag. The value should be an integer. |
| [ISO_DEP](arkts-connectivity-tag-con.md#iso_dep) | Indicates an ISO_DEP tag. The value should be an integer. |
| [NFC_F](arkts-connectivity-tag-con.md#nfc_f) | Indicates an NFC-F tag. The value should be an integer. |
| [NFC_V](arkts-connectivity-tag-con.md#nfc_v) | Indicates an NFC-V tag. The value should be an integer. |
| [NDEF](arkts-connectivity-tag-con.md#ndef) | Indicates an NDEF tag. The value should be an integer. |
| [NDEF_FORMATABLE](arkts-connectivity-tag-con.md#ndef_formatable) | Indicates an NDEF Formatable tag. The value should be an integer. |
| [MIFARE_CLASSIC](arkts-connectivity-tag-con.md#mifare_classic) | Indicates an MIFARE CLASSIC tag. The value should be an integer. |
| [MIFARE_ULTRALIGHT](arkts-connectivity-tag-con.md#mifare_ultralight) | Indicates an MIFARE ULTRALIGHT tag. The value should be an integer. |
| [NFC_BARCODE](arkts-connectivity-tag-con.md#nfc_barcode) | Indicates an NfcBarcode tag. The value should be an integer. |
| [RTD_TEXT](arkts-connectivity-tag-con.md#rtd_text) | RTD type TEXT, see NFC Record Type Definition (RTD) Specification. |
| [RTD_URI](arkts-connectivity-tag-con.md#rtd_uri) | RTD type URI, see NFC Record Type Definition (RTD) Specification. |
| [SKIP_NDEF](arkts-connectivity-tag-con.md#skip_ndef) | Skip NDEF when app is reading a card in the foreground. The value range is all integers. |

