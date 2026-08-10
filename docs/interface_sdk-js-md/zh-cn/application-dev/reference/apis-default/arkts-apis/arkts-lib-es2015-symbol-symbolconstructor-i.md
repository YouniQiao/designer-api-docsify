# SymbolConstructor

**ArkTS模式：** 仅支持ArkTS-Dyn

## [[Call]]

```TypeScript
(description?: string | number): symbol
```

Returns a new unique Symbol value.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-SymbolConstructor-(description?: string | number): symbol--><!--Device-SymbolConstructor-(description?: string | number): symbol-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| description | string \| number | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| symbol |  |

## for

```TypeScript
for(key: string): symbol
```

Returns a Symbol object from the global symbol registry matching the given key if found.Otherwise, returns a new symbol with this key.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-SymbolConstructor-for(key: string): symbol--><!--Device-SymbolConstructor-for(key: string): symbol-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| symbol |  |

## keyFor

```TypeScript
keyFor(sym: symbol): string | undefined
```

Returns a key from the global symbol registry matching the given Symbol if found.Otherwise, returns a undefined.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-SymbolConstructor-keyFor(sym: symbol): string | undefined--><!--Device-SymbolConstructor-keyFor(sym: symbol): string | undefined-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sym | symbol | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string |  |

## prototype

```TypeScript
readonly prototype: Symbol
```

A reference to the prototype.

**类型：** Symbol

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-SymbolConstructor-readonly prototype: Symbol--><!--Device-SymbolConstructor-readonly prototype: Symbol-End-->

