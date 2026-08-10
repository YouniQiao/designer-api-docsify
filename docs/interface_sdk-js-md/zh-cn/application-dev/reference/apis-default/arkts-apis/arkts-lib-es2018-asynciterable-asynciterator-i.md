# AsyncIterator

**ArkTS模式：** 仅支持ArkTS-Dyn

## next

```TypeScript
next(...args: [] | [TNext]): Promise<IteratorResult<T, TReturn>>
```

**ArkTS模式：** 仅支持ArkTS-Dyn

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| args | [] \| [TNext] | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;IteratorResult&lt;T, TReturn&gt;&gt; |  |

## return

```TypeScript
return?(value?: TReturn | PromiseLike<TReturn>): Promise<IteratorResult<T, TReturn>>
```

**ArkTS模式：** 仅支持ArkTS-Dyn

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | TReturn \| PromiseLike&lt;TReturn&gt; | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;IteratorResult&lt;T, TReturn&gt;&gt; |  |

## throw

```TypeScript
throw?(e?: any): Promise<IteratorResult<T, TReturn>>
```

**ArkTS模式：** 仅支持ArkTS-Dyn

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| e | any | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;IteratorResult&lt;T, TReturn&gt;&gt; |  |

