# MenuElement

The &lt;menu&gt; component provides menus as temporary pop-up windows to display operations that can be performed by users.

**继承/实现关系：** MenuElement extends [Element](arkts-arkui-viewmodel-element-i.md)

**起始版本：** 4

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为4。

<!--Device-unnamed-export interface MenuElement extends Element--><!--Device-unnamed-export interface MenuElement extends Element-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## show

```TypeScript
show(position: { x: number; y: number }): void
```

Displays the menu.x and y specify the position of the displayed menu.x indicates the X-axis coordinate from the left edge of the visible area, and does not include any scrolling offset.y indicates the Y-axis coordinate from the upper edge of the visible area, and does not include any scrolling offset or a status bar.The menu is preferentially displayed in the lower right corner.When the visible space on the right is insufficient, the menu is moved leftward.When the visible space in the lower part is insufficient, the menu is moved upward.

**起始版本：** 4

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为4。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-MenuElement-show(position: { x: number; y: number }): void--><!--Device-MenuElement-show(position: { x: number; y: number }): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| position | { x: number; y: number } | 是 |  |

