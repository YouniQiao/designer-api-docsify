# StringDecoder

提供将二进制流解码为字符串的能力。支持以下编码类型：utf-8、iso-8859-2、koi8-r、macintosh、windows-1250、 windows-1251、gbk、gb18030、big5、utf-16be 和 UTF-16le。

**起始版本：** 12

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
import { util } from 'kits/@kit.ArkTS';
```

## constructor

```TypeScript
constructor(encoding?: string)
```

用于创建 **StringDecoder** 实例的构造函数。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| encoding | string | 否 |

## end

```TypeScript
end(chunk?: string | Uint8Array): string
```

结束解码过程，并将内部缓存中存储的任何剩余输入作为字符串返回。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| chunk | string \| Uint8Array | 否 |

**返回值：**

| 类型 |
| --- |
| string |

## write

```TypeScript
write(chunk: string | Uint8Array): string
```

解码字符串。Uint8Array 末尾的任何不完整多字节字符都会从返回的字符串中过滤掉，并存储在内部缓存中以供下次调用使用。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| chunk | string \| Uint8Array | 是 |

**返回值：**

| 类型 |
| --- |
| string |
