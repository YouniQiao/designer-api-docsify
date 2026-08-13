# OnMenuItemClickWithTextCallback

```TypeScript
export type OnMenuItemClickWithTextCallback = (menuItem: TextMenuItem, value: string) => boolean
```

点击菜单项时触发，可拦截系统默认菜单项（如复制、粘贴菜单项）的执行行为。

**起始版本：** 26.0.0

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-unnamed-export type OnMenuItemClickWithTextCallback = (menuItem: TextMenuItem, value: string) => boolean--><!--Device-unnamed-export type OnMenuItemClickWithTextCallback = (menuItem: TextMenuItem, value: string) => boolean-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| menuItem | [TextMenuItem](arkts-arkui-textmenuitem-i.md) | 是 |
| value | string | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |
