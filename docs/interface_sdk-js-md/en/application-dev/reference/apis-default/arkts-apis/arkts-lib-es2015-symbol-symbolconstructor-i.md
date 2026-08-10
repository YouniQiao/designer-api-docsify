# SymbolConstructor

**ArkTS mode:** ArkTS-Dyn only

## [[Call]]

```TypeScript
(description?: string | number): symbol
```

Returns a new unique Symbol value.

**ArkTS mode:** ArkTS-Dyn only

<!--Device-SymbolConstructor-(description?: string | number): symbol--><!--Device-SymbolConstructor-(description?: string | number): symbol-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| description | string \| number | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| symbol |  |

## for

```TypeScript
for(key: string): symbol
```

Returns a Symbol object from the global symbol registry matching the given key if found.Otherwise, returns a new symbol with this key.

**ArkTS mode:** ArkTS-Dyn only

<!--Device-SymbolConstructor-for(key: string): symbol--><!--Device-SymbolConstructor-for(key: string): symbol-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| symbol |  |

## keyFor

```TypeScript
keyFor(sym: symbol): string | undefined
```

Returns a key from the global symbol registry matching the given Symbol if found.Otherwise, returns a undefined.

**ArkTS mode:** ArkTS-Dyn only

<!--Device-SymbolConstructor-keyFor(sym: symbol): string | undefined--><!--Device-SymbolConstructor-keyFor(sym: symbol): string | undefined-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sym | symbol | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| string |  |

## prototype

```TypeScript
readonly prototype: Symbol
```

A reference to the prototype.

**Type:** Symbol

**ArkTS mode:** ArkTS-Dyn only

<!--Device-SymbolConstructor-readonly prototype: Symbol--><!--Device-SymbolConstructor-readonly prototype: Symbol-End-->

