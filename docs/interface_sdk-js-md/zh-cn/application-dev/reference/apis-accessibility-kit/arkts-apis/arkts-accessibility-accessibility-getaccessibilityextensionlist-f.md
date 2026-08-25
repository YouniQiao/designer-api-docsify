# getAccessibilityExtensionList

## 导入模块

```TypeScript
import { accessibility } from 'kits/@kit.AccessibilityKit';
import { AccessibilityEventType, AccessibilityAction, FocusMoveResultCode, InjectActionType, AccessibilityFocusScene, FocusRuleType, OperateVirtualNodeResult, AccessibilitySourceType } from 'kits/@kit.AccessibilityKit';
```

## getAccessibilityExtensionList

```TypeScript
function getAccessibilityExtensionList(abilityType: AbilityType, stateType: AbilityState): Promise<Array<AccessibilityAbilityInfo>>
```

查询辅助应用列表。使用Promise异步回调。

**起始版本：** 9

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
| Promise&lt;Array&lt;[AccessibilityAbilityInfo](arkts-accessibility-accessibility-accessibilityabilityinfo-i.md)&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |


## getAccessibilityExtensionList

```TypeScript
function getAccessibilityExtensionList(abilityType: AbilityType, stateType: AbilityState, callback: AsyncCallback<Array<AccessibilityAbilityInfo>>): void
```

查询辅助应用列表。使用callback异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本23开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [abilityType](../../apis-ability-kit/arkts-apis/arkts-ability-abilitystatedata-c.md) | [AbilityType](arkts-accessibility-accessibility-abilitytype-t.md) | 是 |
| [stateType](../../apis-background-tasks-kit/arkts-apis/arkts-backgroundtasks-bundlestate-bundleactivestate-i.md) | [AbilityState](arkts-accessibility-accessibility-abilitystate-t.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[AccessibilityAbilityInfo](arkts-accessibility-accessibility-accessibilityabilityinfo-i.md)&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
