# OnGetStartIndexByOffsetCallback（系统接口）

```TypeScript
export type OnGetStartIndexByOffsetCallback = (totalOffset: double) => StartLineInfo
```

根据Grid的总偏移量，计算当前页面起始行的位置，用于快速滑动或反向滑动场景。 **系统接口：** 此接口为系统接口。 **模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| totalOffset | double | 是 |

**返回值：**

| 类型 |
| --- |
| [StartLineInfo](arkts-arkui-grid-startlineinfo-i-sys.md) |
