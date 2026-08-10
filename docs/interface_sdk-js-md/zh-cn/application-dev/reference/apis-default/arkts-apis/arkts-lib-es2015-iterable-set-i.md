# Set

**ArkTS模式：** 仅支持ArkTS-Dyn

## [Symbol.iterator]

```TypeScript
[Symbol.iterator](): IterableIterator<T>
```

Iterates over values in the set.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Set-[Symbol.iterator](): IterableIterator<T>--><!--Device-Set-[Symbol.iterator](): IterableIterator<T>-End-->

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IterableIterator](../../apis-arkts/arkts-apis/arkts-arkts-iterator-iterableiterator-i.md)&lt;T&gt; |  |

## entries

```TypeScript
entries(): IterableIterator<[T, T]>
```

Returns an iterable of [v,v] pairs for every value `v` in the set.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Set-entries(): IterableIterator<[T, T]>--><!--Device-Set-entries(): IterableIterator<[T, T]>-End-->

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IterableIterator](../../apis-arkts/arkts-apis/arkts-arkts-iterator-iterableiterator-i.md)&lt;[T, T]&gt; |  |

## keys

```TypeScript
keys(): IterableIterator<T>
```

Despite its name, returns an iterable of the values in the set.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Set-keys(): IterableIterator<T>--><!--Device-Set-keys(): IterableIterator<T>-End-->

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IterableIterator](../../apis-arkts/arkts-apis/arkts-arkts-iterator-iterableiterator-i.md)&lt;T&gt; |  |

## values

```TypeScript
values(): IterableIterator<T>
```

Returns an iterable of values in the set.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Set-values(): IterableIterator<T>--><!--Device-Set-values(): IterableIterator<T>-End-->

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IterableIterator](../../apis-arkts/arkts-apis/arkts-arkts-iterator-iterableiterator-i.md)&lt;T&gt; |  |

