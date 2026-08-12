# PatternLockController

Provides methods for control pattern lock component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class PatternLockController--><!--Device-unnamed-export declare class PatternLockController-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor()
```

A constructor used to create a PatternLockController instance.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PatternLockController-constructor()--><!--Device-PatternLockController-constructor()-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## reset

```TypeScript
reset(): void
```

Reset pattern lock.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PatternLockController-reset(): void--><!--Device-PatternLockController-reset(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## setChallengeResult

```TypeScript
setChallengeResult(result: PatternLockChallengeResult): void
```

Sets the authentication challenge result for the pattern password.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PatternLockController-setChallengeResult(result: PatternLockChallengeResult): void--><!--Device-PatternLockController-setChallengeResult(result: PatternLockChallengeResult): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| result | [PatternLockChallengeResult](arkts-arkui-patternlock-patternlockchallengeresult-e.md) | Yes | Authentication challenge result of the pattern password. |

