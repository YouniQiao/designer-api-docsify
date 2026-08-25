# getSeniorModeStateForSelf

## 导入模块

```TypeScript
import { accessibility } from 'kits/@kit.AccessibilityKit';
import { AccessibilityEventType, AccessibilityAction, FocusMoveResultCode, InjectActionType, AccessibilityFocusScene, FocusRuleType, OperateVirtualNodeResult, AccessibilitySourceType } from 'kits/@kit.AccessibilityKit';
```

## getSeniorModeStateForSelf

```TypeScript
function getSeniorModeStateForSelf(): Promise<boolean>
```

判断应用是否开启“长辈模式”。使用Promise异步回调。与[accessibility.isSeniorModeEnabled](arkts-accessibility-accessibility-isseniormodeenabled-f.md)（判断系统关怀模式是否开启）对应不同作用范围，本接口仅查询应用自身状态。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [9300000](../errorcode-accessibility.md#9300000-无障碍系统服务工作异常) |
