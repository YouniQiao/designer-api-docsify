# DivElement

The &lt;div&gt; component provides a div container.

**继承/实现关系：** DivElement extends [Element](arkts-arkui-viewmodel-element-i.md)

**起始版本：** 6

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为6。

<!--Device-unnamed-export interface DivElement extends Element--><!--Device-unnamed-export interface DivElement extends Element-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## getScrollOffset

```TypeScript
getScrollOffset(): ScrollOffset
```

Returns the offset of the current scrolling. The return value type is Object.

**起始版本：** 6

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为6。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-DivElement-getScrollOffset(): ScrollOffset--><!--Device-DivElement-getScrollOffset(): ScrollOffset-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ScrollOffset](arkts-arkui-viewmodel-scrolloffset-i.md) |  |

## scrollBy

```TypeScript
scrollBy(data: ScrollParam): void
```

Scrolls the div for a certain distance.

**起始版本：** 6

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为6。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-DivElement-scrollBy(data: ScrollParam): void--><!--Device-DivElement-scrollBy(data: ScrollParam): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | [ScrollParam](arkts-arkui-viewmodel-scrollparam-i.md) | 是 |  |

