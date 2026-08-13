# Record

A Map subclass with keys restricted to numbers, strings, or enums

**Inheritance/Implementation:** Record extends Map<K, V>

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Deprecated since:** -1

<!--Device-unnamed-export class Record--><!--Device-unnamed-export class Record-End-->

**System capability:** SystemCapability.Utils.Lang

## $_get

```TypeScript
$_get(k : K) : V | undefined
```

Gets a value from the Record by key

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Record-$_get(k : K) : V | undefined--><!--Device-Record-$_get(k : K) : V | undefined-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| k | K | Yes | The key to get |

**Return value:**

| Type | Description |
| --- | --- |
| V | The value associated with the key, or undefined if not found |

## $_set

```TypeScript
$_set(k: K, v: V) : void
```

Sets a value in the Record by key

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Record-$_set(k: K, v: V) : void--><!--Device-Record-$_set(k: K, v: V) : void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| k | K | Yes | The key to set |
| v | V | Yes | The value to set |

