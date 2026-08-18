# CommonController

Implements a common controller for managing components related to **promptAction**.

**Since:** 18

<!--Device-promptAction-class CommonController--><!--Device-promptAction-class CommonController-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## close

```TypeScript
close(): void
```

Closes the custom dialog box. If the dialog box is already closed, this API has no effect.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-CommonController-close(): void--><!--Device-CommonController-close(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor()
```

A constructor used to create a controller instance.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-CommonController-constructor()--><!--Device-CommonController-constructor()-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## getState

```TypeScript
getState(): CommonState
```

Obtains the state of the custom dialog box.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-CommonController-getState(): CommonState--><!--Device-CommonController-getState(): CommonState-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [CommonState](arkts-arkui-promptaction-commonstate-e.md) |
