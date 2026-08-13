# getAccessibilityExtensionListSync

## getAccessibilityExtensionListSync

```TypeScript
function getAccessibilityExtensionListSync(
    abilityType: AbilityType,
    stateType: AbilityState
  ): Array<AccessibilityAbilityInfo>
```

查询当前系统内辅助应用列表，支持按条件查询。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本23开始，该接口支持在ArkTS卡片中使用。

<!--Device-accessibility-function getAccessibilityExtensionListSync(    abilityType: AbilityType,    stateType: AbilityState  ): Array<AccessibilityAbilityInfo>--><!--Device-accessibility-function getAccessibilityExtensionListSync(    abilityType: AbilityType,    stateType: AbilityState  ): Array<AccessibilityAbilityInfo>-End-->

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

## 示例

查询所有已安装的辅助应用。

```TypeScript
import { accessibility } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let abilityType: accessibility.AbilityType = 'all'; // 辅助应用类型为所有类型。
let abilityState: accessibility.AbilityState = 'install'; // 辅助应用状态为已安装。
let data: accessibility.AccessibilityAbilityInfo[];

try {
  data = accessibility.getAccessibilityExtensionListSync(abilityType, abilityState);
  console.info(`succeeded in getting accessibility extension list, ${JSON.stringify(data)}`);
} catch (error) {
  let err = error as BusinessError;
  console.error(`Failed to get accessibility extension list. Code: ${err.code}, message: ${err.message}`);
}

// 例如：系统内安装一个包名为com.example.myaccessibilityapp的辅助应用。
// 日志打印结果为：
// [{"id":"com.example.myaccessibilityapp/AccessibilityExtAbility","name":"AccessibilityExtAbility",
// "bundleName":"com.example.myaccessibilityapp","abilityTypes":[],
// "capabilities":["retrieve","gesture"],"description":"$string:MainAbility_desc",
// "eventTypes":["click","longClick","select","focus","textUpdate","hoverEnter","hoverExit","scroll",
// "textSelectionUpdate","accessibilityFocus","accessibilityFocusClear","requestFocusForAccessibility",
// "announceForAccessibility","announceForAccessibilityNotInterrupt",
// "requestFocusForAccessibilityNotInterrupt","scrolling","pageActive"],"targetBundleNames":[],"needHide":false}}]
```

查询所有已启用的具有语音反馈的辅助应用。

```TypeScript
import { accessibility } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let abilityType: accessibility.AbilityType = 'spoken'; // 辅助应用类型为具有语音反馈类型。
let abilityState: accessibility.AbilityState = 'enable'; // 辅助应用状态为已启用。
let data: accessibility.AccessibilityAbilityInfo[];

try {
  data = accessibility.getAccessibilityExtensionListSync(abilityType, abilityState);
  console.info(`succeeded in getting accessibility extension list, ${JSON.stringify(data)}`);
} catch (error) {
  let err = error as BusinessError;
  console.error(`Failed to get accessibility extension list. Code: ${err.code}, message: ${err.message}`);
}
```
