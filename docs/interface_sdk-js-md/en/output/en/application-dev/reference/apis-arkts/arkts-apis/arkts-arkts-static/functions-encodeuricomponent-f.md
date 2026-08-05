# encodeURIComponent

## encodeURIComponent

```TypeScript
export function encodeURIComponent(uriComponent: string | double | boolean): string
```

The encodeURIComponent() function encodes a URI by replacing each instance of certain characters by one, two, three, or four escape sequences representing the UTF-8 encoding of the character (will only be four escape sequences for characters composed of two surrogate characters). Compared to encodeURI(), this function encodes more characters, including those that are part of the URI syntax.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export function encodeURIComponent(uriComponent: string | double | boolean): string--><!--Device-unnamed-export function encodeURIComponent(uriComponent: string | double | boolean): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uriComponent | string \| double \| boolean | Yes | a string to be encoded as a URI component. (a path, query string, fragment,etc.). Other values are converted to strings. |

**Return value:**

| Type | Description |
| --- | --- |
| string | A new string representing the provided |

