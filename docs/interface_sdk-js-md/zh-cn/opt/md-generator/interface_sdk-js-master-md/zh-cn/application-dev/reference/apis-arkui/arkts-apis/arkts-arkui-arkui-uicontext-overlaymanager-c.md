# OverlayManager

class OverlayManager

**起始版本：** 12

**废弃版本：** -1

<!--Device-unnamed-export class OverlayManager--><!--Device-unnamed-export class OverlayManager-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## addComponentContent

```TypeScript
addComponentContent(content: ComponentContent, index?: number): void
```

Adds a specified ComponentContent node to the OverlayManager.

**起始版本：** 12

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-OverlayManager-addComponentContent(content: ComponentContent, index?: number): void--><!--Device-OverlayManager-addComponentContent(content: ComponentContent, index?: number): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| content | [ComponentContent](../../apis-na/arkts-apis/arkts-na-componentcontent-c.md) | 是 |
| index | number | 否 |

## addComponentContentWithOrder

```TypeScript
addComponentContentWithOrder(content: ComponentContent, levelOrder?: LevelOrder): void
```

Creates a floating layer node with the specified display order. This API allows you to define the stacking order of the nodes when they are created.

**起始版本：** 18

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-OverlayManager-addComponentContentWithOrder(content: ComponentContent, levelOrder?: LevelOrder): void--><!--Device-OverlayManager-addComponentContentWithOrder(content: ComponentContent, levelOrder?: LevelOrder): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| content | [ComponentContent](../../apis-na/arkts-apis/arkts-na-componentcontent-c.md) | 是 |
| levelOrder | [LevelOrder](arkts-arkui-promptaction-levelorder-c.md) | 否 |

## hideAllComponentContents

```TypeScript
hideAllComponentContents(): void
```

Hide all ComponentContents on the OverlayManager.

**起始版本：** 12

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-OverlayManager-hideAllComponentContents(): void--><!--Device-OverlayManager-hideAllComponentContents(): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## hideComponentContent

```TypeScript
hideComponentContent(content: ComponentContent): void
```

Hide the ComponentContent.

**起始版本：** 12

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-OverlayManager-hideComponentContent(content: ComponentContent): void--><!--Device-OverlayManager-hideComponentContent(content: ComponentContent): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| content | [ComponentContent](../../apis-na/arkts-apis/arkts-na-componentcontent-c.md) | 是 |

## openOrderOverlay

```TypeScript
openOrderOverlay(content: ComponentContent, options?: OrderOverlayOptions): Promise<void>
```

打开具有指定ComponentContent和选项的浮层。

**起始版本：** 26.0.0

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-OverlayManager-openOrderOverlay(content: ComponentContent, options?: OrderOverlayOptions): Promise<void>--><!--Device-OverlayManager-openOrderOverlay(content: ComponentContent, options?: OrderOverlayOptions): Promise<void>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| content | [ComponentContent](../../apis-na/arkts-apis/arkts-na-componentcontent-c.md) | 是 |
| options | [OrderOverlayOptions](arkts-arkui-arkui-uicontext-orderoverlayoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [103307](../errorcode-promptAction.md#103307-系统弹出窗口导致无法打开浮层) |

## removeComponentContent

```TypeScript
removeComponentContent(content: ComponentContent): void
```

Removes a specified ComponentContent node from the OverlayManager

**起始版本：** 12

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-OverlayManager-removeComponentContent(content: ComponentContent): void--><!--Device-OverlayManager-removeComponentContent(content: ComponentContent): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| content | [ComponentContent](../../apis-na/arkts-apis/arkts-na-componentcontent-c.md) | 是 |

## showAllComponentContents

```TypeScript
showAllComponentContents(): void
```

Show all ComponentContents on the OverlayManager.

**起始版本：** 12

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-OverlayManager-showAllComponentContents(): void--><!--Device-OverlayManager-showAllComponentContents(): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## showComponentContent

```TypeScript
showComponentContent(content: ComponentContent): void
```

Show the ComponentContent.

**起始版本：** 12

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-OverlayManager-showComponentContent(content: ComponentContent): void--><!--Device-OverlayManager-showComponentContent(content: ComponentContent): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| content | [ComponentContent](../../apis-na/arkts-apis/arkts-na-componentcontent-c.md) | 是 |
