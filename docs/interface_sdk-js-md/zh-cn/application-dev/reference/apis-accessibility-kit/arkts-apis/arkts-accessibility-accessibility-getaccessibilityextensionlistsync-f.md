# getAccessibilityExtensionListSync

## 导入模块

```TypeScript
import { accessibility } from 'kits/@kit.AccessibilityKit';
import { AccessibilityEventType, AccessibilityAction, FocusMoveResultCode, InjectActionType, AccessibilityFocusScene, FocusRuleType, OperateVirtualNodeResult, AccessibilitySourceType } from 'kits/@kit.AccessibilityKit';
```

## getAccessibilityExtensionListSync

```TypeScript
function getAccessibilityExtensionListSync(
    abilityType: AbilityType,
    stateType: AbilityState
  ): Array<AccessibilityAbilityInfo>
```

查询当前系统内辅助应用列表，支持按条件查询。本接口为同步版本，与[accessibility.getAccessibilityExtensionList](arkts-accessibility-accessibility-getaccessibilityextensionlist-f.md)（异步版本）功能相 同，如需立即获取结果可使用本接口，如需在非阻塞场景下查询建议使用异步版本。

**起始版本：** 12

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本23开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [abilityType](../../apis-ability-kit/arkts-apis/arkts-ability-abilitystatedata-c.md) | [AbilityType](arkts-accessibility-accessibility-abilitytype-t.md) | 是 |
| [stateType](../../apis-background-tasks-kit/arkts-apis/arkts-backgroundtasks-bundlestate-bundleactivestate-i.md) | [AbilityState](arkts-accessibility-accessibility-abilitystate-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Array&lt;[AccessibilityAbilityInfo](arkts-accessibility-accessibility-accessibilityabilityinfo-i.md)&gt; |
