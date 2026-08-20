# Animator

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-unnamed-class Animator--><!--Device-unnamed-class Animator-End-->

## Modules to Import

```TypeScript
```

## create

```TypeScript
static create(options: AnimatorOptions | SimpleAnimatorOptions): AnimatorResult
```

Create an animator object for custom animation. This interface depends on the UI context and cannot be used when the UI context is unclear. It is recommended to use createAnimator.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Animator-static create(options: AnimatorOptions | SimpleAnimatorOptions): AnimatorResult--><!--Device-Animator-static create(options: AnimatorOptions | SimpleAnimatorOptions): AnimatorResult-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [AnimatorOptions](arkts-animator-animatoroptions-i.md) \| [SimpleAnimatorOptions](arkts-animator-simpleanimatoroptions-c.md) | Yes | Options. |

**Return value:**

| Type | Description |
| --- | --- |
| [AnimatorResult](arkts-animator-animatorresult-i.md) | animator result |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br> 1. Mandatory parameters are left unspecified. <br> 2. Incorrect parameters types. <br> 3. Parameter verification failed. @static |

