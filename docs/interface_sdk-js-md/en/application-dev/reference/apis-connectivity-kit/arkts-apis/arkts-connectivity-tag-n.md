# tag(Standard NFC Tags)

The **tag** module provides APIs for operating and managing NFC tags. The following tag read modes are available:Background mode: The device reads the tag by using NFC without starting any application, and then searches for applications based on the tag type. If only one application is matched, the card reading page of that application will be started. If multiple applications are matched, an application selector will be started, asking the user to select an application. Background mode does not involve tag-related APIs. For details, see [nfc-tag Read/Write Development](../../../connectivity/nfc/nfc-tag-access-guide.md#accessing-an-nfc-tag-without-starting-an-application).Foreground mode: A foreground application has priority to read the NFC tag discovered.

> **NOTE：**&gt;
> 2. Since API version 26.0.0, it is more accurate to determine whether a device supports NFC by calling both
> [canIUse("SystemCapability.Communication.NFC.Tag")](../../../reference/common/init.md#caniuse) and
> [nfcController.isNfcSupported](arkts-connectivity-nfccontroller-isnfcsupported-f.md). If the device does not
> support NFC, the application stability may be affected. For details, see
> [NFC Tag Read/Write Development](../../../connectivity/nfc/nfc-tag-access-guide.md).&gt;
> 3. If an error is reported while importing the tag module editor, the capabilities of a specific device model may
> exceed the capability set defined for the default device. To use these capabilities, configure a custom SysCap by
> following instructions in
> [SystemCapability](https://developer.huawei.com/consumer/en/doc/harmonyos-references/syscap).

**Since:** 7

**System capability:** SystemCapability.Communication.NFC.Tag

## Modules to Import

```TypeScript
import { tag } from 'kits/@kit.ConnectivityKit';
```

## Summary

### Namespaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ndef(Standard NFC Tags)](arkts-connectivity-tag-ndef-n.md) |

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [getNfcATag(Standard NFC Tags)](arkts-connectivity-tag-getnfcatag-f.md) |
| [getNfcA(Standard NFC Tags)](arkts-connectivity-tag-getnfca-f.md) |
| [getNfcBTag(Standard NFC Tags)](arkts-connectivity-tag-getnfcbtag-f.md) |
| [getNfcB(Standard NFC Tags)](arkts-connectivity-tag-getnfcb-f.md) |
| [getNfcFTag(Standard NFC Tags)](arkts-connectivity-tag-getnfcftag-f.md) |
| [getNfcF(Standard NFC Tags)](arkts-connectivity-tag-getnfcf-f.md) |
| [getNfcVTag(Standard NFC Tags)](arkts-connectivity-tag-getnfcvtag-f.md) |
| [getNfcV(Standard NFC Tags)](arkts-connectivity-tag-getnfcv-f.md) |
| [getIsoDep(Standard NFC Tags)](arkts-connectivity-tag-getisodep-f.md) |
| [getNdef(Standard NFC Tags)](arkts-connectivity-tag-getndef-f.md) |
| [getMifareClassic(Standard NFC Tags)](arkts-connectivity-tag-getmifareclassic-f.md) |
| [getMifareUltralight(Standard NFC Tags)](arkts-connectivity-tag-getmifareultralight-f.md) |
| [getNdefFormatable(Standard NFC Tags)](arkts-connectivity-tag-getndefformatable-f.md) |
| [getTagInfo(Standard NFC Tags)](arkts-connectivity-tag-gettaginfo-f.md) |
| [registerForegroundDispatch(Standard NFC Tags)](arkts-connectivity-tag-registerforegrounddispatch-f.md) |
| [unregisterForegroundDispatch(Standard NFC Tags)](arkts-connectivity-tag-unregisterforegrounddispatch-f.md) |
| [on(Standard NFC Tags)](arkts-connectivity-tag-on-f.md#onreadermode) |
| [off(Standard NFC Tags)](arkts-connectivity-tag-off-f.md#offreadermode) |
| [on(Standard NFC Tags)](arkts-connectivity-tag-on-f.md#onreadermodewithinterval) |
| [off(Standard NFC Tags)](arkts-connectivity-tag-off-f.md#offreadermodewithinterval) |
| [getBarcodeTag(Standard NFC Tags)](arkts-connectivity-tag-getbarcodetag-f.md) |

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [TagInfo(Standard NFC Tags)](arkts-connectivity-tag-taginfo-i.md) |
| [NdefRecord(Standard NFC Tags)](arkts-connectivity-tag-ndefrecord-i.md) |

<!--Del-->
### Interfaces(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [TagInfo(Standard NFC Tags)](arkts-connectivity-tag-taginfo-i-sys.md) |
<!--DelEnd-->

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [TnfType(Standard NFC Tags)](arkts-connectivity-tag-tnftype-e.md) |
| [NfcForumType(Standard NFC Tags)](arkts-connectivity-tag-nfcforumtype-e.md) |
| [MifareClassicType(Standard NFC Tags)](arkts-connectivity-tag-mifareclassictype-e.md) |
| [MifareClassicSize(Standard NFC Tags)](arkts-connectivity-tag-mifareclassicsize-e.md) |
| [MifareUltralightType(Standard NFC Tags)](arkts-connectivity-tag-mifareultralighttype-e.md) |

### Types

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [NfcATag(Standard NFC Tags)](arkts-connectivity-tag-nfcatag-t.md) |
| [NfcBTag(Standard NFC Tags)](arkts-connectivity-tag-nfcbtag-t.md) |
| [NfcFTag(Standard NFC Tags)](arkts-connectivity-tag-nfcftag-t.md) |
| [NfcVTag(Standard NFC Tags)](arkts-connectivity-tag-nfcvtag-t.md) |
| [IsoDepTag(Standard NFC Tags)](arkts-connectivity-tag-isodeptag-t.md) |
| [NdefTag(Standard NFC Tags)](arkts-connectivity-tag-ndeftag-t.md) |
| [MifareClassicTag(Standard NFC Tags)](arkts-connectivity-tag-mifareclassictag-t.md) |
| [MifareUltralightTag(Standard NFC Tags)](arkts-connectivity-tag-mifareultralighttag-t.md) |
| [NdefFormatableTag(Standard NFC Tags)](arkts-connectivity-tag-ndefformatabletag-t.md) |
| [NdefMessage(Standard NFC Tags)](arkts-connectivity-tag-ndefmessage-t.md) |
| [TagSession(Standard NFC Tags)](arkts-connectivity-tag-tagsession-t.md) |
| [BarcodeTag(Standard NFC Tags)](arkts-connectivity-tag-barcodetag-t.md) |

### Constants

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [NFC_A(Standard NFC Tags)](arkts-connectivity-tag-con.md#nfc_a) |
| [NFC_B(Standard NFC Tags)](arkts-connectivity-tag-con.md#nfc_b) |
| [ISO_DEP(Standard NFC Tags)](arkts-connectivity-tag-con.md#iso_dep) |
| [NFC_F(Standard NFC Tags)](arkts-connectivity-tag-con.md#nfc_f) |
| [NFC_V(Standard NFC Tags)](arkts-connectivity-tag-con.md#nfc_v) |
| [NDEF(Standard NFC Tags)](arkts-connectivity-tag-con.md#ndef) |
| [NDEF_FORMATABLE(Standard NFC Tags)](arkts-connectivity-tag-con.md#ndef_formatable) |
| [MIFARE_CLASSIC(Standard NFC Tags)](arkts-connectivity-tag-con.md#mifare_classic) |
| [MIFARE_ULTRALIGHT(Standard NFC Tags)](arkts-connectivity-tag-con.md#mifare_ultralight) |
| [RTD_TEXT(Standard NFC Tags)](arkts-connectivity-tag-con.md#rtd_text) |
| [RTD_URI(Standard NFC Tags)](arkts-connectivity-tag-con.md#rtd_uri) |
| [NFC_BARCODE(Standard NFC Tags)](arkts-connectivity-tag-con.md#nfc_barcode) |
| [SKIP_NDEF(Standard NFC Tags)](arkts-connectivity-tag-con.md#skip_ndef) |
