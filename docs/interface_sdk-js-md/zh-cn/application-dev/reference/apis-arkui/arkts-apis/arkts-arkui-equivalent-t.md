# Equivalent

```TypeScript
export type Equivalent<T> = (oldV: T, newV: T) => boolean
```

Determine whether two values are equal.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| oldV | T | 是 |
| newV | T | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |
