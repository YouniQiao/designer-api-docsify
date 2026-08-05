# format

## format

```TypeScript
function format(format: string, ...args: Object[]): string
```

%s: String will be used to convert all values except BigInt, Object and -0. BigInt values will be represented with an n and Objects that have no user defined toString function are inspected using util.inspect() with options { depth: 0, colors: false, compact: 3 }. %d: Number will be used to convert all values except BigInt and Symbol. %i: parseInt(value, 10) is used for all values except BigInt and Symbol. %f: parseFloat(value) is used for all values except Bigint and Symbol. %j: JSON. Replaced with the string '[Circular]' if the argument contains circular references. %o: Object. A string representation of an object with generic JavaScript object formatting.Similar to util.inspect() with options { showHidden: true, showProxy: true}. This will show the full object including non-enumerable properties and proxies. %O: Object. A string representation of an object with generic JavaScript object formatting. %O: Object. A string representation of an object with generic JavaScript object formatting.Similar to util.inspect() without options. This will show the full object not including non-enumerable properties and proxies. %c: CSS. This specifier is ignored and will skip any CSS passed in. %%: single percent sign ('%'). This does not consume an argument.Returns: \_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_ The formatted string.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-util-function format(format: string, ...args: Object[]): string--><!--Device-util-function format(format: string, ...args: Object[]): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| format | string | Yes | Styled string |
| args | Object[] | Yes | Data to be formatted |

**Return value:**

| Type | Description |
| --- | --- |
| string | a string formatted in a specific format. |

