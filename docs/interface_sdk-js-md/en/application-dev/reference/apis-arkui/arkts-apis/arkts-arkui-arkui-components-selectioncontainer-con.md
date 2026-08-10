# Constants

## SelectionContainer

```TypeScript
export declare const SelectionContainer: SelectionContainerInterface
```

SelectionContainer组件用于为多个文本节点提供跨节点文本选中、复制及菜单扩展能力，支持统一配置选中文本的手柄颜色和底板颜色，支持灵活的文本拼接策略，支持自定义选择菜单和扩展菜单选项。适用于需要跨多个Text组件实现文本连续选中、统一复制、样式自定义及菜单扩展的场景，解决了多Text组件场景下文本选择体验割裂的问题，提升了用户在复杂文本布局中的交互体验。

> **说明：**
> 
> - 本组件中选中文本相关回调返回的文本内容，按照[Text](../../apis-arkui/arkts-components/arkts-arkui-text-i)组件的从上到下显示顺序进行拼接。
> 
> - 本组件默认布局走[Stack](../../apis-arkui/arkts-components/arkts-arkui-stack-i)，如有其他容器布局需求请在SelectionContainer内放置一个容器组件。
> 
> - SelectionContainer内跨节点选中文本时不显示放大镜，也不支持[getMagnifier](arkts-arkui-arkui-uicontext-uicontext-c.md#getmagnifier)主动设置放大镜。
> 
> - 仅Text组件中的文本内容参与跨节点选中与文本拼接。

### 子组件

可以包含子组件。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-unnamed-export declare const SelectionContainer: SelectionContainerInterface--><!--Device-unnamed-export declare const SelectionContainer: SelectionContainerInterface-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## SelectionContainerInstance

```TypeScript
export declare const SelectionContainerInstance: SelectionContainerAttribute
```

定义SelectionContainer组件实例。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-unnamed-export declare const SelectionContainerInstance: SelectionContainerAttribute--><!--Device-unnamed-export declare const SelectionContainerInstance: SelectionContainerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

