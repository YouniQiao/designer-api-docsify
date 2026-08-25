# getNfcATag

## 导入模块

```TypeScript
import { tag } from '@kit.ConnectivityKit';
```

## getNfcATag

```TypeScript
function getNfcATag(tagInfo: TagInfo): NfcATag
```

获取NFC A类型Tag对象，通过该对象可访问NfcA技术类型的Tag。

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为7。

**废弃版本：** 9

**替代接口：** [getNfcA](arkts-connectivity-tag-getnfca-f.md)

**系统能力：** SystemCapability.Communication.NFC.Tag

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| tagInfo | [TagInfo](arkts-connectivity-tag-taginfo-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [NfcATag](arkts-connectivity-tag-nfcatag-t.md) |
