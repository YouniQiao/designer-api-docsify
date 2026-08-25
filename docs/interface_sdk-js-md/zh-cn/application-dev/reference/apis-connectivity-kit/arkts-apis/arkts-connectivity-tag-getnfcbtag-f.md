# getNfcBTag

## 导入模块

```TypeScript
import { tag } from '@kit.ConnectivityKit';
```

## getNfcBTag

```TypeScript
function getNfcBTag(tagInfo: TagInfo): NfcBTag
```

获取NFC B类型Tag对象，通过该对象可访问NfcB技术类型的Tag。

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为7。

**废弃版本：** 9

**替代接口：** [getNfcB](arkts-connectivity-tag-getnfcb-f.md)

**系统能力：** SystemCapability.Communication.NFC.Tag

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| tagInfo | [TagInfo](arkts-connectivity-tag-taginfo-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [NfcBTag](arkts-connectivity-tag-nfcbtag-t.md) |
