# TransitionHierarchyStrategy（系统接口）

共享元素动画过程中in/out组件层级位置移动策略枚举。  
| 名称 | 值 | 说明 | | ------ | - | ---- | | [NONE](#none) | 0 | 无层级提拉，in/out组件保持原来的层级位置，受父组件scale、position影响。 | | [ADAPTIVE](#adaptive) | 1 |

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为12。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

## NONE

```TypeScript
NONE = 0
```

None mode. Source and target staty in the original level in the hierarchy during geometry transition.

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为12。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12 - 12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

## ADAPTIVE

```TypeScript
ADAPTIVE = 1
```

ADAPTIVE mode. Lower level one of source and target is elevated to higher level of both, indicating that two elements are in same high level.

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为12。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12 - 12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。
