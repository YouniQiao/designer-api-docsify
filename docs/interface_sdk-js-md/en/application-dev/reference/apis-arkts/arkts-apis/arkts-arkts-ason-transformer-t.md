# Transformer

```TypeScript
type Transformer = (this: ISendable, key: string,
      value: ISendable | undefined | null) => ISendable | undefined | null
```

用于转换结果函数的类型。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ASON-type Transformer = (this: ISendable, key: string,      value: ISendable | undefined | null) => ISendable | undefined | null--><!--Device-ASON-type Transformer = (this: ISendable, key: string,      value: ISendable | undefined | null) => ISendable | undefined | null-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| this | [ISendable](../../apis-image-kit/arkts-apis/arkts-image-sendableimage-isendable-t.md) | Yes | 所解析的键值对所属的对象。 |
| key | string | Yes | 属性名。 |
| value | [ISendable](../../apis-image-kit/arkts-apis/arkts-image-sendableimage-isendable-t.md) \| undefined \| null | Yes | 所解析的键值对的值。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ISendable](../../apis-image-kit/arkts-apis/arkts-image-sendableimage-isendable-t.md) \| undefined \| null | 返回转换结果后的ISendable对象或undefined或null。 |

