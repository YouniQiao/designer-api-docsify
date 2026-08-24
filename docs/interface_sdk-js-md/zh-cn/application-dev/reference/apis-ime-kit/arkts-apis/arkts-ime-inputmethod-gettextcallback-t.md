# GetTextCallback

```TypeScript
export type GetTextCallback = (length: int) => string
```

获取编辑框最新状态下光标左侧指定长度的文本内容。

**起始版本：** 23

<!--Device-inputMethod-export type GetTextCallback = (length: int) => string--><!--Device-inputMethod-export type GetTextCallback = (length: int) => string-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| length | int | 是 | 需要获取光标左侧文本内容的长度。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 光标左侧指定长度的文本内容。 |

