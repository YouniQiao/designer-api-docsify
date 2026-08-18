# encodeURI

## Modules to Import

```TypeScript
```

## encodeURI

```TypeScript
export function encodeURI(uri: string): string
```

The encodeURI() function encodes a URI by replacing each instance of certain characters by one, two, three, or four escape sequences representing the UTF-8 encoding of the character (will only be four escape sequences for characters composed of two surrogate characters). Compared to encodeURIComponent(), this function encodes fewer characters, preserving those that are part of the URI syntax.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export function encodeURI(uri: string): string--><!--Device-unnamed-export function encodeURI(uri: string): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uri | string | Yes | URI that needs to be encoded |

**Return value:**

| Type | Description |
| --- | --- |
| string | The encoded result |

