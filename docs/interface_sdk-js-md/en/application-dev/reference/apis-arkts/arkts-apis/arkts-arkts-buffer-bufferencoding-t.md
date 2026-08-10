# BufferEncoding

```TypeScript
type BufferEncoding = 'ascii' | 'utf8' | 'utf-8' | 'utf16le' | 'ucs2' | 'ucs-2' | 'base64' | 'base64url' | 'latin1' | 'binary' | 'hex'
```

表示支持的编码格式类型。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-buffer-type BufferEncoding = 'ascii' | 'utf8' | 'utf-8' | 'utf16le' | 'ucs2' | 'ucs-2' | 'base64' | 'base64url' | 'latin1' | 'binary' | 'hex'--><!--Device-buffer-type BufferEncoding = 'ascii' | 'utf8' | 'utf-8' | 'utf16le' | 'ucs2' | 'ucs-2' | 'base64' | 'base64url' | 'latin1' | 'binary' | 'hex'-End-->

**System capability:** SystemCapability.Utils.Lang

| Type | Description |
| --- | --- |
| 'ascii' | 表示ascii格式。 |
| 'utf8' | 表示utf8格式。 |
| 'utf-8' | 表示utf8格式。 |
| 'utf16le' | 表示utf16小端序格式。 |
| 'ucs2' | utf16le的别名。 |
| 'ucs-2' | utf16le的别名。 |
| 'base64' | 表示base64格式。 |
| 'base64url' | 表示base64url格式。 |
| 'latin1' | iso-8859-1的别名，向下兼容ascii格式。 |
| 'binary' | 表示二进制格式。 |
| 'hex' | 表示十六进制格式。 |

