# setTimeout

## setTimeout

```TypeScript
export declare function setTimeout(
  handler: Function,
  delay?: number,
  ...arguments: any[]
): number
```

Sets a timer after which a function will be executed.

**起始版本：** 5

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为5。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-unnamed-export declare function setTimeout(  handler: Function,  delay?: number,  ...arguments: any[]): number--><!--Device-unnamed-export declare function setTimeout(  handler: Function,  delay?: number,  ...arguments: any[]): number-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Lite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handler | Function | 是 | Indicates the function to be called after the timer goes off. |
| delay | number | 否 | Indicates the delay (in milliseconds) after which the function will be called. If this parameter is left empty, default value "0" will be used, which means that the function will be called immediately or as soon as possible. |
| arguments | any[] | 是 | Indicates additional arguments to pass to "handler" when the timer goes off. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | Returns the timer ID. |

