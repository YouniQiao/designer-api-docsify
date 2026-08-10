# ReadonlyArray

**ArkTS模式：** 仅支持ArkTS-Dyn

## [Symbol.iterator]

```TypeScript
[Symbol.iterator](): IterableIterator<T>
```

Iterator of values in the array.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-ReadonlyArray-[Symbol.iterator](): IterableIterator<T>--><!--Device-ReadonlyArray-[Symbol.iterator](): IterableIterator<T>-End-->

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IterableIterator](../../apis-arkts/arkts-apis/arkts-arkts-iterator-iterableiterator-i.md)&lt;T&gt; |  |

## entries

```TypeScript
entries(): IterableIterator<[number, T]>
```

Returns an iterable of key, value pairs for every entry in the array

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-ReadonlyArray-entries(): IterableIterator<[number, T]>--><!--Device-ReadonlyArray-entries(): IterableIterator<[number, T]>-End-->

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IterableIterator](../../apis-arkts/arkts-apis/arkts-arkts-iterator-iterableiterator-i.md)&lt;[number, T]&gt; |  |

## keys

```TypeScript
keys(): IterableIterator<number>
```

Returns an iterable of keys in the array

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-ReadonlyArray-keys(): IterableIterator<number>--><!--Device-ReadonlyArray-keys(): IterableIterator<number>-End-->

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IterableIterator](../../apis-arkts/arkts-apis/arkts-arkts-iterator-iterableiterator-i.md)&lt;number&gt; |  |

## values

```TypeScript
values(): IterableIterator<T>
```

Returns an iterable of values in the array

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-ReadonlyArray-values(): IterableIterator<T>--><!--Device-ReadonlyArray-values(): IterableIterator<T>-End-->

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IterableIterator](../../apis-arkts/arkts-apis/arkts-arkts-iterator-iterableiterator-i.md)&lt;T&gt; |  |

