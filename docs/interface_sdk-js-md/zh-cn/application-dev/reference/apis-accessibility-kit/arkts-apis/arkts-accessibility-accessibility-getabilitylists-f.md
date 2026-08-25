# getAbilityLists

## 导入模块

```TypeScript
import { accessibility } from 'kits/@kit.AccessibilityKit';
import { AccessibilityEventType, AccessibilityAction, FocusMoveResultCode, InjectActionType, AccessibilityFocusScene, FocusRuleType, OperateVirtualNodeResult, AccessibilitySourceType } from 'kits/@kit.AccessibilityKit';
```

## getAbilityLists

```TypeScript
function getAbilityLists(
    abilityType: AbilityType,
    stateType: AbilityState,
    callback: AsyncCallback<Array<AccessibilityAbilityInfo>>
  ): void
```

查询辅助应用列表。使用callback异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [getAccessibilityExtensionList](arkts-accessibility-accessibility-getaccessibilityextensionlist-f.md)(abilityType: AbilityType, stateType: AbilityState, callback: AsyncCallback&lt;Array&lt;AccessibilityAbilityInfo&gt;&gt;)

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [abilityType](../../apis-ability-kit/arkts-apis/arkts-ability-abilitystatedata-c.md) | [AbilityType](arkts-accessibility-accessibility-abilitytype-t.md) | 是 |
| [stateType](../../apis-background-tasks-kit/arkts-apis/arkts-backgroundtasks-bundlestate-bundleactivestate-i.md) | [AbilityState](arkts-accessibility-accessibility-abilitystate-t.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[AccessibilityAbilityInfo](arkts-accessibility-accessibility-accessibilityabilityinfo-i.md)&gt;&gt; | 是 |


## getAbilityLists

```TypeScript
function getAbilityLists(abilityType: AbilityType, stateType: AbilityState): Promise<Array<AccessibilityAbilityInfo>>
```

查询辅助应用列表。使用Promise异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [getAccessibilityExtensionList](arkts-accessibility-accessibility-getaccessibilityextensionlist-f.md)(abilityType: AbilityType, stateType: AbilityState)

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
