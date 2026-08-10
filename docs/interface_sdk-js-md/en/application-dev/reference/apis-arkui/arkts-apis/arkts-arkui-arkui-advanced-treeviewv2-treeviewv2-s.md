# TreeViewV2

树视图V2组件。树视图作为一种分层显示的列表，适合显示嵌套结构。拥有父列表项和子列表项，可展开或折叠。

用于效率型应用，如备忘录、电子邮件、图库中的侧边导航栏。

该组件基于[状态管理（V2）](../../../ui/state-management/arkts-state-management-overview.md#状态管理v2)实现，相较于  
[状态管理（V1）](../../../ui/state-management/arkts-state-management-overview.md#状态管理v1)，状态管理（V2）增强了对数据对象的深度观察与管理能力，不再局限于组件层级。借助状态管理（V2），开发者可以通过该组件更灵活地控制树视图的数据和状态，实现更高效的用户界面刷新。

> **说明：**
> 
> - 如果TreeViewV2设置[通用属性](../../apis-arkui/arkts-components/arkts-arkui-common-attribute.md)和[通用事件](../../apis-arkui/arkts-components/arkts-arkui-common-attribute.md)，编译工具链
> 会额外生成节点__Common__，并将通用属性或通用事件挂载在__Common__上，而不是直接应用到TreeViewV2本身。这可能导致开发者设置的通用属性或通用事件不生效或不符合预期，因此，不建议TreeViewV2设置通用
> 属性和通用事件。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Decorator:** @ComponentV2

<!--Device-unnamed-export declare struct TreeViewV2--><!--Device-unnamed-export declare struct TreeViewV2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { TreeListenerManagerV2, NodeParamV2, CallbackParamV2, TreeControllerV2, TreeViewV2, TreeListenerV2 } from 'kits/@kit.ArkUI';
```

## build

```TypeScript
build(): void
```

构建组件的方法。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-TreeViewV2-build(): void--><!--Device-TreeViewV2-build(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## treeControllerV2

```TypeScript
treeControllerV2: TreeControllerV2
```

树视图节点控制器。

**Type:** [TreeControllerV2](arkts-arkui-arkui-advanced-treeviewv2-treecontrollerv2-c.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Decorator:** @Param

**Model restriction:** This API can be used only in the stage model.

<!--Device-TreeViewV2-treeControllerV2: TreeControllerV2--><!--Device-TreeViewV2-treeControllerV2: TreeControllerV2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

