# ArrayListReplaceCb

```TypeScript
export type ArrayListReplaceCb<T> =  (value: T, index: number, arrlist: ArrayList<T>) => T
```

ArrayList中replaceAllElements方法的回调函数。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-unnamed-export type ArrayListReplaceCb<T> =  (value: T, index: int, arrlist: ArrayList<T>) => T--><!--Device-unnamed-export type ArrayListReplaceCb<T> =  (value: T, index: int, arrlist: ArrayList<T>) => T-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | T | 是 |
| index | number | 是 |
| arrlist | [ArrayList](arkts-arkts-util-arraylist-arraylist-c.md)&lt;T&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| T |
