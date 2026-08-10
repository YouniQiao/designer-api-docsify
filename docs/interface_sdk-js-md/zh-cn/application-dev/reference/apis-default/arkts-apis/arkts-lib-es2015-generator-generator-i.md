# Generator

**ArkTS模式：** 仅支持ArkTS-Dyn

## [Symbol.iterator]

```TypeScript
[Symbol.iterator](): Generator<T, TReturn, TNext>
```

**ArkTS模式：** 仅支持ArkTS-Dyn

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Generator&lt;T, TReturn, TNext&gt; |  |

## next

```TypeScript
next(...args: [] | [TNext]): IteratorResult<T, TReturn>
```

**ArkTS模式：** 仅支持ArkTS-Dyn

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| args | [] \| [TNext] | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IteratorResult](../../apis-arkts/arkts-apis/arkts-arkts-iterator-iteratorresult-c.md)&lt;T, TReturn&gt; |  |

## return

```TypeScript
return(value: TReturn): IteratorResult<T, TReturn>
```

**ArkTS模式：** 仅支持ArkTS-Dyn

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | TReturn | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IteratorResult](../../apis-arkts/arkts-apis/arkts-arkts-iterator-iteratorresult-c.md)&lt;T, TReturn&gt; |  |

## throw

```TypeScript
throw(e: any): IteratorResult<T, TReturn>
```

**ArkTS模式：** 仅支持ArkTS-Dyn

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| e | any | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IteratorResult](../../apis-arkts/arkts-apis/arkts-arkts-iterator-iteratorresult-c.md)&lt;T, TReturn&gt; |  |

