# Promise

Represents the completion of an asynchronous operation

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-unnamed-interface Promise<T>--><!--Device-unnamed-interface Promise<T>-End-->

## finally

```TypeScript
finally(onfinally?: (() => void) | undefined | null): Promise<T>
```

Attaches a callback that is invoked when the Promise is settled (fulfilled or rejected). The resolved value cannot be modified from the callback.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Promise-finally(onfinally?: (() => void) | undefined | null): Promise<T>--><!--Device-Promise-finally(onfinally?: (() => void) | undefined | null): Promise<T>-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| onfinally | (() =&gt; void) \| undefined \| null | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;T&gt; |  |

