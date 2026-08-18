# LevelOrder

弹窗层级，可以控制弹窗显示的顺序。

**起始版本：** 18

<!--Device-unnamed-export class LevelOrder--><!--Device-unnamed-export class LevelOrder-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## clamp

```TypeScript
static clamp(order: number): LevelOrder
```

创建指定顺序的弹窗层级。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-LevelOrder-static clamp(order: number): LevelOrder--><!--Device-LevelOrder-static clamp(order: number): LevelOrder-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| order | number | 是 |

**返回值：**

| 类型 |
| --- |
| [LevelOrder](arkts-arkui-promptaction-levelorder-c.md) |

## getOrder

```TypeScript
getOrder(): number
```

获取弹窗显示顺序。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-LevelOrder-getOrder(): number--><!--Device-LevelOrder-getOrder(): number-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| number |
