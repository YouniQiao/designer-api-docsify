# parse

## Modules to Import

```TypeScript
```

## parse

```TypeScript
function parse(text: string, reviver?: Transformer, options?: ParseOptions): Object | null
```

Parses a JSON string into an ArkTS object or null.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-json-function parse(text: string, reviver?: Transformer, options?: ParseOptions): Object | null--><!--Device-json-function parse(text: string, reviver?: Transformer, options?: ParseOptions): Object | null-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| text | string | Yes |
| reviver | [Transformer](arkts-arkts-ason-transformer-t.md) | No |
| options | [ParseOptions](arkts-arkts-json-parseoptions-i.md) | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Object |
