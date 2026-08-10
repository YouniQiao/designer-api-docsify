# decodeURIComponent

## decodeURIComponent

```TypeScript
export function decodeURIComponent(uriComponent: string): string
```

The decodeURIComponent() function decodes a Uniform Resource Identifier (URI) component previously created by encodeURIComponent() or by a similar routine.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function decodeURIComponent(uriComponent: string): string--><!--Device-unnamed-export function decodeURIComponent(uriComponent: string): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uriComponent | string | 是 | URI that needs to be decoded |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | The decoded URI component |

