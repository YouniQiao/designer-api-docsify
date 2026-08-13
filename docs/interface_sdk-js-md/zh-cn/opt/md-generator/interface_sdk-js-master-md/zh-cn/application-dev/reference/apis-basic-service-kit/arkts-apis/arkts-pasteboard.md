# @ohos.pasteboard

本模块提供管理系统剪贴板的能力，支持系统复制、粘贴功能。系统剪贴板支持对文本、HTML、URI、Want、PixelMap等内容的操作。

**起始版本：** 23

**废弃版本：** -1

<!--Device-unnamed-declare namespace pasteboard--><!--Device-unnamed-declare namespace pasteboard-End-->

**系统能力：** SystemCapability.MiscServices.Pasteboard

## 汇总

### 函数

| 名称 |
| --- |
| [createData](arkts-basicservices-pasteboard-createdata-f.md#createData) |
| [createData](arkts-basicservices-pasteboard-createdata-f.md#createData) |
| [createHtmlData](arkts-basicservices-pasteboard-createhtmldata-f.md#createHtmlData) |
| [createHtmlTextRecord](arkts-basicservices-pasteboard-createhtmltextrecord-f.md#createHtmlTextRecord) |
| [createPlainTextData](arkts-basicservices-pasteboard-createplaintextdata-f.md#createPlainTextData) |
| [createPlainTextRecord](arkts-basicservices-pasteboard-createplaintextrecord-f.md#createPlainTextRecord) |
| [createRecord](arkts-basicservices-pasteboard-createrecord-f.md#createRecord) |
| [createUriData](arkts-basicservices-pasteboard-createuridata-f.md#createUriData) |
| [createUriRecord](arkts-basicservices-pasteboard-createurirecord-f.md#createUriRecord) |
| [createWantData](arkts-basicservices-pasteboard-createwantdata-f.md#createWantData) |
| [createWantRecord](arkts-basicservices-pasteboard-createwantrecord-f.md#createWantRecord) |
| [getSystemPasteboard](arkts-basicservices-pasteboard-getsystempasteboard-f.md#getSystemPasteboard) |

### 类

| 名称 |
| --- |
| [ProgressSignal](arkts-basicservices-pasteboard-progresssignal-c.md) |

### 接口

| 名称 |
| --- |
| [GetDataParams](arkts-basicservices-pasteboard-getdataparams-i.md) |
| [PasteData](arkts-basicservices-pasteboard-pastedata-i.md) |
| [PasteDataProperty](arkts-basicservices-pasteboard-pastedataproperty-i.md) |
| [PasteDataRecord](arkts-basicservices-pasteboard-pastedatarecord-i.md) |
| [ProgressInfo](arkts-basicservices-pasteboard-progressinfo-i.md) |
| [SystemPasteboard](arkts-basicservices-pasteboard-systempasteboard-i.md) |

<!--Del-->
### 接口（系统接口）

| 名称 |
| --- |
| [SystemPasteboard](arkts-basicservices-pasteboard-systempasteboard-i-sys.md) |
<!--DelEnd-->

### 枚举

| 名称 |
| --- |
| [FileConflictOptions](arkts-basicservices-pasteboard-fileconflictoptions-e.md) |
| [Pattern](arkts-basicservices-pasteboard-pattern-e.md) |
| [ProgressIndicator](arkts-basicservices-pasteboard-progressindicator-e.md) |
| [ShareOption](arkts-basicservices-pasteboard-shareoption-e.md) |

### 类型

| 名称 |
| --- |
| [ProgressListener](arkts-basicservices-pasteboard-progresslistener-t.md) |
| [UpdateCallback](arkts-basicservices-pasteboard-updatecallback-t.md) |
| [ValueType](arkts-basicservices-pasteboard-valuetype-t.md) |

### 常量

| 名称 |
| --- |
| [MAX_RECORD_NUM](arkts-basicservices-pasteboard-con.md#MAX_RECORD_NUM) |
| [MIMETYPE_PIXELMAP](arkts-basicservices-pasteboard-con.md#MIMETYPE_PIXELMAP) |
| [MIMETYPE_TEXT_HTML](arkts-basicservices-pasteboard-con.md#MIMETYPE_TEXT_HTML) |
| [MIMETYPE_TEXT_PLAIN](arkts-basicservices-pasteboard-con.md#MIMETYPE_TEXT_PLAIN) |
| [MIMETYPE_TEXT_URI](arkts-basicservices-pasteboard-con.md#MIMETYPE_TEXT_URI) |
| [MIMETYPE_TEXT_WANT](arkts-basicservices-pasteboard-con.md#MIMETYPE_TEXT_WANT) |
