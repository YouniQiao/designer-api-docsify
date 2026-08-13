# SymbolConstructor

**Since:** -1

**Deprecated since:** -1

<!--Device-unnamed-interface SymbolConstructor--><!--Device-unnamed-interface SymbolConstructor-End-->

## constructor

```TypeScript
(description?: string | number): symbol
```

Returns a new unique Symbol value.

**Since:** -1

**Deprecated since:** -1

<!--Device-SymbolConstructor-(description?: string | number): symbol--><!--Device-SymbolConstructor-(description?: string | number): symbol-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| description | string \| number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| symbol |

## for

```TypeScript
for(key: string): symbol
```

Returns a Symbol object from the global symbol registry matching the given key if found. Otherwise, returns a new symbol with this key.

**Since:** -1

**Deprecated since:** -1

<!--Device-SymbolConstructor-for(key: string): symbol--><!--Device-SymbolConstructor-for(key: string): symbol-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| symbol |

## keyFor

```TypeScript
keyFor(sym: symbol): string | undefined
```

Returns a key from the global symbol registry matching the given Symbol if found. Otherwise, returns a undefined.

**Since:** -1

**Deprecated since:** -1

<!--Device-SymbolConstructor-keyFor(sym: symbol): string | undefined--><!--Device-SymbolConstructor-keyFor(sym: symbol): string | undefined-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sym | symbol | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## prototype

```TypeScript
readonly prototype: Symbol
```

A reference to the prototype.

**Type:** Symbol

**Since:** -1

**Deprecated since:** -1

<!--Device-SymbolConstructor-readonly prototype: Symbol--><!--Device-SymbolConstructor-readonly prototype: Symbol-End-->
