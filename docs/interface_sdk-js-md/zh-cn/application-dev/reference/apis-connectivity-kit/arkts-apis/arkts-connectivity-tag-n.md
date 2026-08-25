# tag(标准NFC-Tag)

本模块主要用于操作及管理NFC Tag，提供后台读卡和前台应用优先分发两种读卡模式。 后台读卡是指不需要打开应用程序，电子设备通过NFC读取标签卡片后，根据标签卡片的类型匹配到一个或多个应用程序。如果仅匹配到一个，则直接拉起应用程序的读卡页面；如果是多个则弹出应用选择器，让用户选择指定的读卡应用。后台读卡不涉及tag相 关接口，示例参考[nfc-tag开发指南](../../../connectivity/nfc/nfc-tag-access-guide.md#后台读取标签)。 前台读卡是指提前打开应用程序，并进入对应的NFC读卡页面后读卡，只会把读到的标签卡片信息分发给前台应用程序。

> **说明：**&gt;
> 2. 从API版本26.0.0开始请使用[canIUse("SystemCapability.Communication.NFC.Tag")](../../../reference/common/init.md#caniuse)
> && [nfcController.isNfcSupported](arkts-connectivity-nfccontroller-isnfcsupported-f.md)共同判断设备是否支持NFC能力更加准确，否则可能导
> 致应用运行稳定性问题，参考[nfc-tag开发指南](../../../connectivity/nfc/nfc-tag-access-guide.md)。&gt;
> 3. 导入tag模块编辑器报错，在某个具体设备型号上能力可能超出工程默认设备定义的能力集范围，如需要使用此部分能力需额外配置自定义syscap，参考
> [syscap开发指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/syscap)。

**起始版本：** 7

**系统能力：** SystemCapability.Communication.NFC.Tag

## 导入模块

```TypeScript
import { tag } from 'kits/@kit.ConnectivityKit';
```

## 汇总

### 命名空间

| 名称 |
| --- |
| [ndef(标准NFC-Tag)](arkts-connectivity-tag-ndef-n.md) |

### 函数

| 名称 |
| --- |
| [getNfcATag(标准NFC-Tag)](arkts-connectivity-tag-getnfcatag-f.md) |
| [getNfcA(标准NFC-Tag)](arkts-connectivity-tag-getnfca-f.md) |
| [getNfcBTag(标准NFC-Tag)](arkts-connectivity-tag-getnfcbtag-f.md) |
| [getNfcB(标准NFC-Tag)](arkts-connectivity-tag-getnfcb-f.md) |
| [getNfcFTag(标准NFC-Tag)](arkts-connectivity-tag-getnfcftag-f.md) |
| [getNfcF(标准NFC-Tag)](arkts-connectivity-tag-getnfcf-f.md) |
| [getNfcVTag(标准NFC-Tag)](arkts-connectivity-tag-getnfcvtag-f.md) |
| [getNfcV(标准NFC-Tag)](arkts-connectivity-tag-getnfcv-f.md) |
| [getIsoDep(标准NFC-Tag)](arkts-connectivity-tag-getisodep-f.md) |
| [getNdef(标准NFC-Tag)](arkts-connectivity-tag-getndef-f.md) |
| [getMifareClassic(标准NFC-Tag)](arkts-connectivity-tag-getmifareclassic-f.md) |
| [getMifareUltralight(标准NFC-Tag)](arkts-connectivity-tag-getmifareultralight-f.md) |
| [getNdefFormatable(标准NFC-Tag)](arkts-connectivity-tag-getndefformatable-f.md) |
| [getTagInfo(标准NFC-Tag)](arkts-connectivity-tag-gettaginfo-f.md) |
| [registerForegroundDispatch(标准NFC-Tag)](arkts-connectivity-tag-registerforegrounddispatch-f.md) |
| [unregisterForegroundDispatch(标准NFC-Tag)](arkts-connectivity-tag-unregisterforegrounddispatch-f.md) |
| [on(标准NFC-Tag)](arkts-connectivity-tag-on-f.md#onreadermode) |
| [off(标准NFC-Tag)](arkts-connectivity-tag-off-f.md#offreadermode) |
| [on(标准NFC-Tag)](arkts-connectivity-tag-on-f.md#onreadermodewithinterval) |
| [off(标准NFC-Tag)](arkts-connectivity-tag-off-f.md#offreadermodewithinterval) |
| [getBarcodeTag(标准NFC-Tag)](arkts-connectivity-tag-getbarcodetag-f.md) |

### 接口

| 名称 |
| --- |
| [TagInfo(标准NFC-Tag)](arkts-connectivity-tag-taginfo-i.md) |
| [NdefRecord(标准NFC-Tag)](arkts-connectivity-tag-ndefrecord-i.md) |

<!--Del-->
### 接口（系统接口）

| 名称 |
| --- |
| [TagInfo(标准NFC-Tag)](arkts-connectivity-tag-taginfo-i-sys.md) |
<!--DelEnd-->

### 枚举

| 名称 |
| --- |
| [TnfType(标准NFC-Tag)](arkts-connectivity-tag-tnftype-e.md) |
| [NfcForumType(标准NFC-Tag)](arkts-connectivity-tag-nfcforumtype-e.md) |
| [MifareClassicType(标准NFC-Tag)](arkts-connectivity-tag-mifareclassictype-e.md) |
| [MifareClassicSize(标准NFC-Tag)](arkts-connectivity-tag-mifareclassicsize-e.md) |
| [MifareUltralightType(标准NFC-Tag)](arkts-connectivity-tag-mifareultralighttype-e.md) |

### 类型

| 名称 |
| --- |
| [NfcATag(标准NFC-Tag)](arkts-connectivity-tag-nfcatag-t.md) |
| [NfcBTag(标准NFC-Tag)](arkts-connectivity-tag-nfcbtag-t.md) |
| [NfcFTag(标准NFC-Tag)](arkts-connectivity-tag-nfcftag-t.md) |
| [NfcVTag(标准NFC-Tag)](arkts-connectivity-tag-nfcvtag-t.md) |
| [IsoDepTag(标准NFC-Tag)](arkts-connectivity-tag-isodeptag-t.md) |
| [NdefTag(标准NFC-Tag)](arkts-connectivity-tag-ndeftag-t.md) |
| [MifareClassicTag(标准NFC-Tag)](arkts-connectivity-tag-mifareclassictag-t.md) |
| [MifareUltralightTag(标准NFC-Tag)](arkts-connectivity-tag-mifareultralighttag-t.md) |
| [NdefFormatableTag(标准NFC-Tag)](arkts-connectivity-tag-ndefformatabletag-t.md) |
| [NdefMessage(标准NFC-Tag)](arkts-connectivity-tag-ndefmessage-t.md) |
| [TagSession(标准NFC-Tag)](arkts-connectivity-tag-tagsession-t.md) |
| [BarcodeTag(标准NFC-Tag)](arkts-connectivity-tag-barcodetag-t.md) |

### 常量

| 名称 |
| --- |
| [NFC_A(标准NFC-Tag)](arkts-connectivity-tag-con.md#nfc_a) |
| [NFC_B(标准NFC-Tag)](arkts-connectivity-tag-con.md#nfc_b) |
| [ISO_DEP(标准NFC-Tag)](arkts-connectivity-tag-con.md#iso_dep) |
| [NFC_F(标准NFC-Tag)](arkts-connectivity-tag-con.md#nfc_f) |
| [NFC_V(标准NFC-Tag)](arkts-connectivity-tag-con.md#nfc_v) |
| [NDEF(标准NFC-Tag)](arkts-connectivity-tag-con.md#ndef) |
| [NDEF_FORMATABLE(标准NFC-Tag)](arkts-connectivity-tag-con.md#ndef_formatable) |
| [MIFARE_CLASSIC(标准NFC-Tag)](arkts-connectivity-tag-con.md#mifare_classic) |
| [MIFARE_ULTRALIGHT(标准NFC-Tag)](arkts-connectivity-tag-con.md#mifare_ultralight) |
| [RTD_TEXT(标准NFC-Tag)](arkts-connectivity-tag-con.md#rtd_text) |
| [RTD_URI(标准NFC-Tag)](arkts-connectivity-tag-con.md#rtd_uri) |
| [NFC_BARCODE(标准NFC-Tag)](arkts-connectivity-tag-con.md#nfc_barcode) |
| [SKIP_NDEF(标准NFC-Tag)](arkts-connectivity-tag-con.md#skip_ndef) |
