# encodeURI

## encodeURI

```TypeScript
export function encodeURI(uri: string): string
```

The encodeURI() function encodes a URI by replacing each instance of certain characters by one, two, three, or four escape sequences representing the UTF-8 encoding of the character (will only be four escape sequences for characters composed of two surrogate characters). Compared to encodeURIComponent(), this function encodes fewer characters, preserving those that are part of the URI syntax.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function encodeURI(uri: string): string--><!--Device-unnamed-export function encodeURI(uri: string): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | URI that needs to be encoded |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | The encoded result |

