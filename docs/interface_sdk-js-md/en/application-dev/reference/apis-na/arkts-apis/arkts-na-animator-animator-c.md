# Animator

**Since:** -1

**ArkTS mode:** ArkTS-Sta only, since version -1.

**Deprecated since:** -1

<!--Device-unnamed-class Animator--><!--Device-unnamed-class Animator-End-->

## create

```TypeScript
static create(options: AnimatorOptions | SimpleAnimatorOptions): AnimatorResult
```

Create an animator object for custom animation. This interface depends on the UI context and cannot be used when the UI context is unclear. It is recommended to use createAnimator.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Animator-static create(options: AnimatorOptions | SimpleAnimatorOptions): AnimatorResult--><!--Device-Animator-static create(options: AnimatorOptions | SimpleAnimatorOptions): AnimatorResult-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [AnimatorOptions](../../apis-arkui/arkts-apis/arkts-arkui-animator-animatoroptions-i.md) \| [SimpleAnimatorOptions](../../apis-arkui/arkts-apis/arkts-arkui-animator-simpleanimatoroptions-c.md) | Yes | Options. |

**Return value:**

| Type | Description |
| --- | --- |
| [AnimatorResult](../../apis-arkui/arkts-apis/arkts-arkui-animator-animatorresult-i.md) | animator result |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. @static |

