# getNfcVTag

## 导入模块

```TypeScript
import { tag } from 'kits/@kit.ConnectivityKit';
```

## getNfcVTag

```TypeScript
function getNfcVTag(tagInfo: TagInfo): NfcVTag
```

Obtains an {@link NfcVTag} object based on the tag information.&lt;p&gt;During tag reading, if the tag supports the NFC-V technology, an {@link NfcVTag} object will be created based on the tag information.

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为7。

**废弃版本：** 9

**替代接口：** ohos.nfc.tag/tag#getNfcV

<!--Device-tag-function getNfcVTag(tagInfo: TagInfo): NfcVTag--><!--Device-tag-function getNfcVTag(tagInfo: TagInfo): NfcVTag-End-->

**系统能力：** SystemCapability.Communication.NFC.Tag

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tagInfo | [TagInfo](arkts-connectivity-tag-taginfo-i.md) | 是 | Indicates the tag information. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [NfcVTag](arkts-connectivity-tag-nfcvtag-t.md) | The { |

