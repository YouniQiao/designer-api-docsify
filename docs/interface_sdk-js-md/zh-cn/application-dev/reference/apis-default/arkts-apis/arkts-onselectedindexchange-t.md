# OnSelectedIndexChange

```TypeScript
export type OnSelectedIndexChange = (selectedIndex: int) => void
```

单选分段按钮选中项变更时调用的回调函数类型。

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export type OnSelectedIndexChange = (selectedIndex: int) => void--><!--Device-unnamed-export type OnSelectedIndexChange = (selectedIndex: int) => void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| selectedIndex | int | 是 | 分段按钮选项下标。 <br>取值限定为整数。 |

