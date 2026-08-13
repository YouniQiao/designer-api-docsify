# AttributeWithTagCb

```TypeScript
type AttributeWithTagCb = (tagName: string, key: string, value: string) => boolean
```

The type of ParseOptions attributeWithTagCallbackFunction.

**Since:** 24

**ArkTS mode:** ArkTS-Dyn only, since version 24.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-xml-type AttributeWithTagCb = (tagName: string, key: string, value: string) => boolean--><!--Device-xml-type AttributeWithTagCb = (tagName: string, key: string, value: string) => boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| tagName | string | Yes | The tag in xml parse node |
| key | string | Yes | The key in xml parse node |
| value | string | Yes | The value in xml parse node |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | whether continue to parse xml data |

