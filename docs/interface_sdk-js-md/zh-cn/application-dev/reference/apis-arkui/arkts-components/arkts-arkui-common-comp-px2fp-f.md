# px2fp

## px2fp

```TypeScript
declare function px2fp(value: number): number
```

将px单位的数值转换为以fp为单位的数值。

**起始版本：** 11

**废弃版本：** 18

**替代接口：** [px2fp](../arkts-apis/arkts-arkui-arkui-uicontext-uicontext-c.md#px2fp)

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务中使用。

**卡片能力：** 从API版本11开始，该接口支持在ArkTS卡片中使用。

<!--Device-unnamed-declare function px2fp(value: number): number--><!--Device-unnamed-declare function px2fp(value: number): number-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 将px单位的数值转换为以fp为单位的数值。<br>取值范围：(-∞, +∞) |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 转换后的数值，单位：fp。<br>取值范围：(-∞, +∞) |
