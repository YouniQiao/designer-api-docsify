# PatternLock

## PatternLock

```TypeScript
export declare function PatternLock(
    controller?: PatternLockController
): PatternLockAttribute
```

创建图案密码锁组件。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function PatternLock(    controller?: PatternLockController): PatternLockAttribute--><!--Device-unnamed-export declare function PatternLock(    controller?: PatternLockController): PatternLockAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| controller | [PatternLockController](arkts-arkui-patternlock-patternlockcontroller-c.md) | No | 设置PatternLock组件控制器，可用于重置组件状态和设置图案密码的正确或错误状态。 |

**Return value:**

| Type | Description |
| --- | --- |
| [PatternLockAttribute](arkts-arkui-patternlock-patternlockattribute-i.md) | The attribute of the PatternLock. |


## PatternLock

```TypeScript
export declare function PatternLock(
    style: CustomBuilderT<PatternLockAttribute>,
): PatternLockAttribute
```

定义PatternLock组件。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function PatternLock(    style: CustomBuilderT<PatternLockAttribute>,): PatternLockAttribute--><!--Device-unnamed-export declare function PatternLock(    style: CustomBuilderT<PatternLockAttribute>,): PatternLockAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [CustomBuilderT](../arkts-components/arkts-arkui-custombuildert-t.md)&lt;PatternLockAttribute&gt; | Yes | PatternLock属性实例。 |

**Return value:**

| Type | Description |
| --- | --- |
| [PatternLockAttribute](arkts-arkui-patternlock-patternlockattribute-i.md) |  |

