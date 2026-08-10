# setInterval

## setInterval

```TypeScript
export declare function setInterval(
  handler: Function,
  delay: number,
  ...arguments: any[]
): number
```

Sets the interval for repeatedly calling a function.

**起始版本：** 5

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为5。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-unnamed-export declare function setInterval(  handler: Function,  delay: number,  ...arguments: any[]): number--><!--Device-unnamed-export declare function setInterval(  handler: Function,  delay: number,  ...arguments: any[]): number-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Lite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handler | Function | 是 | Indicates the function to be called repeatedly at the interval. |
| delay | number | 是 | Indicates the interval between each two calls, in milliseconds. The function will be called after this delay. |
| arguments | any[] | 是 | Indicates additional arguments to pass to "handler" when the timer goes off. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | Returns the timer ID. |

