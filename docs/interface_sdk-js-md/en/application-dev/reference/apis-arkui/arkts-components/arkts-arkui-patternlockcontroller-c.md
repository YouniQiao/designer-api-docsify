# PatternLockController

PatternLock组件的控制器，用于重置组件状态和设置图案密码状态。

## 导入对象

```ts patternLockController: PatternLockController = new PatternLockController();```

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-unnamed-declare class PatternLockController--><!--Device-unnamed-declare class PatternLockController-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor()
```

PatternLockController的构造函数。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PatternLockController-constructor()--><!--Device-PatternLockController-constructor()-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## reset

```TypeScript
reset()
```

重置组件状态。需要在PatternLock组件构造时传入对应的controller参数才可生效，未传入时调用不生效。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PatternLockController-reset()--><!--Device-PatternLockController-reset()-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## setChallengeResult

```TypeScript
setChallengeResult(result: PatternLockChallengeResult): void
```

设置图案密码的正确或错误状态。需要在PatternLock组件构造时传入对应的controller参数才可生效，未传入时调用不生效。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PatternLockController-setChallengeResult(result: PatternLockChallengeResult): void--><!--Device-PatternLockController-setChallengeResult(result: PatternLockChallengeResult): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| result | [PatternLockChallengeResult](arkts-arkui-patternlockchallengeresult-e.md) | Yes | 图案密码状态。包括正确和错误状态。 |

