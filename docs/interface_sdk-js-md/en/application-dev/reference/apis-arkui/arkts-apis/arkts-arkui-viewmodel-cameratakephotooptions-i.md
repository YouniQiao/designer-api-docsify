# CameraTakePhotoOptions

CameraTakePhotoOptions

**Since:** 6

<!--Device-unnamed-export interface CameraTakePhotoOptions--><!--Device-unnamed-export interface CameraTakePhotoOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## complete

```TypeScript
complete?: (result: Object) => void
```

Callback function at the end of the interface invoking (executed both successfully and unsuccessfully).

**Type:** (result: Object) =&gt; void

**Since:** 6

**Model restriction:** This API can be used only in the FA model.

<!--Device-CameraTakePhotoOptions-complete?: (result: Object) => void--><!--Device-CameraTakePhotoOptions-complete?: (result: Object) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fail

```TypeScript
fail?: (result: Object) => void
```

Callback function for interface invocation failure.

**Type:** (result: Object) =&gt; void

**Since:** 6

**Model restriction:** This API can be used only in the FA model.

<!--Device-CameraTakePhotoOptions-fail?: (result: Object) => void--><!--Device-CameraTakePhotoOptions-fail?: (result: Object) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## quality

```TypeScript
quality: "high" | "normal" | "low"
```

Picture quality.

**Type:** "high" \| "normal" \| "low"

**Since:** 6

**Model restriction:** This API can be used only in the FA model.

<!--Device-CameraTakePhotoOptions-quality: "high" | "normal" | "low"--><!--Device-CameraTakePhotoOptions-quality: "high" | "normal" | "low"-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## success

```TypeScript
success?: (result: Object) => void
```

Callback function for successful interface invocation.

**Type:** (result: Object) =&gt; void

**Since:** 6

**Model restriction:** This API can be used only in the FA model.

<!--Device-CameraTakePhotoOptions-success?: (result: Object) => void--><!--Device-CameraTakePhotoOptions-success?: (result: Object) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

