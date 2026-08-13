# isTokenizerSupported

## isTokenizerSupported

```TypeScript
function isTokenizerSupported(tokenizer: Tokenizer): boolean
```

判断当前平台是否支持传入的分词器，此为同步接口。 如果当前平台支持传入的分词器时，此接口返回值为true；反之，返回值为false。

**起始版本：** 23

**废弃版本：** -1

<!--Device-relationalStore-function isTokenizerSupported(tokenizer: Tokenizer): boolean--><!--Device-relationalStore-function isTokenizerSupported(tokenizer: Tokenizer): boolean-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [tokenizer](arkts-arkdata-relationalstore-storeconfig-i.md) | [Tokenizer](arkts-arkdata-relationalstore-tokenizer-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## 示例

```TypeScript
let customType = relationalStore.Tokenizer.CUSTOM_TOKENIZER;
let customTypeSupported = relationalStore.isTokenizerSupported(customType);
console.info("custom tokenizer supported on current platform: " + customTypeSupported);
```
