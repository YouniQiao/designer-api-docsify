# PromiseLike

表示一个thenable对象。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
```

## then

```TypeScript
then<U = T, E = never>(onFulfilled: (value: T) => PromiseLike<U> | U,
        onRejected?: (error: Error) => PromiseLike<E> | E): PromiseLike<Awaited<U | E>>
```

为Promise的解析和/或拒绝添加回调函数。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| onFulfilled | (value: T) = & gt; PromiseLike & lt;U & gt; \ | U | 是 |
| onRejected | (error: Error) = & gt; PromiseLike & lt;E & gt; \ | E | 否 |

**返回值：**

| 类型 |
| --- |
| PromiseLike & lt;Awaited & lt;U \ | E & gt; & gt; |
