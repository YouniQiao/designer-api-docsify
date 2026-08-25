# getErrorString

## 导入模块

```TypeScript
import { util } from 'kits/@kit.ArkTS';
```

## getErrorString

```TypeScript
function getErrorString(errno: number): string
```

获取系统错误码的详细信息。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [errnoToString](arkts-arkts-util-errnotostring-f.md)

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [errno](../../apis-universal-keystore-kit/arkts-apis/arkts-universalkeystore-huksexternalcrypto-huksexternalerrorinfo-i.md) | number | 是 |

**返回值：**

| 类型 |
| --- |
| string |
