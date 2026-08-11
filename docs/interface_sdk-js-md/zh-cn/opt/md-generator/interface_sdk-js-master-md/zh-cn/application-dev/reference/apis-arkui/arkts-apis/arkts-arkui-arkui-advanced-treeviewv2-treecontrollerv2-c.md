# TreeControllerV2

树视图组件的控制器，可以将此对象绑定至树视图组件，然后通过它控制树的节点信息，同一个控制器不可以控制多个树视图组件。

**起始版本：** 26.0.0

<!--Device-unnamed-export declare class TreeControllerV2--><!--Device-unnamed-export declare class TreeControllerV2-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## addNode

```TypeScript
addNode(nodeParam?: NodeParamV2): TreeControllerV2
```

点击某个节点后，调用该方法可以触发新增子节点。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-TreeControllerV2-addNode(nodeParam?: NodeParamV2): TreeControllerV2--><!--Device-TreeControllerV2-addNode(nodeParam?: NodeParamV2): TreeControllerV2-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| nodeParam | [NodeParamV2](arkts-arkui-arkui-advanced-treeviewv2-nodeparamv2-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [TreeControllerV2](arkts-arkui-arkui-advanced-treeviewv2-treecontrollerv2-c.md) |

## buildDone

```TypeScript
buildDone(): void
```

建立树视图。节点增加完毕后，必须调用该方法，触发树信息的保存。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-TreeControllerV2-buildDone(): void--><!--Device-TreeControllerV2-buildDone(): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## modifyNode

```TypeScript
modifyNode(): void
```

点击某个节点后，调用该方法可以触发修改该节点，该节点进入编辑态。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-TreeControllerV2-modifyNode(): void--><!--Device-TreeControllerV2-modifyNode(): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## refreshNode

```TypeScript
refreshNode(parentId: number, parentSubTitle: ResourceStr, currentSubtitle: ResourceStr): void
```

更新树视图。调用该方法，更新当前节点的信息。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-TreeControllerV2-refreshNode(parentId: number, parentSubTitle: ResourceStr, currentSubtitle: ResourceStr): void--><!--Device-TreeControllerV2-refreshNode(parentId: number, parentSubTitle: ResourceStr, currentSubtitle: ResourceStr): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| parentId | number | 是 |
| parentSubTitle | [ResourceStr](arkts-arkui-resourcestr-t.md) | 是 |
| currentSubtitle | [ResourceStr](arkts-arkui-resourcestr-t.md) | 是 |

## removeNode

```TypeScript
removeNode(): void
```

点击某个节点后，调用该方法可以触发删除该节点。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-TreeControllerV2-removeNode(): void--><!--Device-TreeControllerV2-removeNode(): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full
