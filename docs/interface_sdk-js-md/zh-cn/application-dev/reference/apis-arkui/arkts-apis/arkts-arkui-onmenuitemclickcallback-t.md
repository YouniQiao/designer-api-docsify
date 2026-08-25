# OnMenuItemClickCallback

```TypeScript
export type OnMenuItemClickCallback = (menuItem: TextMenuItem, range: TextRange) => boolean
```

菜单项功能函数。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| menuItem | [TextMenuItem](arkts-arkui-textcommon-textmenuitem-i.md) | 是 |
| range | [TextRange](arkts-arkui-textcommon-textrange-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |
