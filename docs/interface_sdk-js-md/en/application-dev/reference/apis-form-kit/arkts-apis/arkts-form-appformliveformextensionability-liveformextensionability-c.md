# LiveFormExtensionAbility

Interactive widget extension class. It provides APIs for the widget provider to receive notifications about widget creation and destruction.

**Inheritance/Implementation:** LiveFormExtensionAbility extends ExtensionAbility

**Since:** 23

<!--Device-unnamed-declare class LiveFormExtensionAbility--><!--Device-unnamed-declare class LiveFormExtensionAbility-End-->

**System capability:** SystemCapability.Ability.Form

## Modules to Import

```TypeScript
import { LiveFormExtensionAbility, LiveFormInfo } from '@kit.FormKit';
```

## onLiveFormCreate

```TypeScript
onLiveFormCreate(liveFormInfo: LiveFormInfo, session: UIExtensionContentSession): void
```

Called after the UI content of **LiveFormExtensionAbility** is created.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-LiveFormExtensionAbility-onLiveFormCreate(liveFormInfo: LiveFormInfo, session: UIExtensionContentSession): void--><!--Device-LiveFormExtensionAbility-onLiveFormCreate(liveFormInfo: LiveFormInfo, session: UIExtensionContentSession): void-End-->

**System capability:** SystemCapability.Ability.Form

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| liveFormInfo | [LiveFormInfo](arkts-form-appformliveformextensionability-liveforminfo-i.md) | Yes | Interactive widget information, including the widget ID. |
| session | [UIExtensionContentSession](../../apis-ability-kit/arkts-apis/arkts-ability-appabilityuiextensioncontentsession-uiextensioncontentsession-c.md) | Yes | UI information. |

**Examples**

```TypeScript
import { UIExtensionContentSession } from '@kit.AbilityKit';
import { LiveFormExtensionAbility, LiveFormInfo } from '@kit.FormKit';

const TAG: string = '[testTag] LiveFormExtAbility';

export default class LiveFormExtAbility extends LiveFormExtensionAbility {
  onLiveFormCreate(liveFormInfo: LiveFormInfo, session: UIExtensionContentSession) {
    console.info(TAG, `onLiveFormCreate, formId: ${liveFormInfo.formId}`);
  }
}
```

## onLiveFormDestroy

```TypeScript
onLiveFormDestroy(liveFormInfo: LiveFormInfo): void
```

Called to clear resources when this **LiveFormExtensionAbility** is destroyed.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-LiveFormExtensionAbility-onLiveFormDestroy(liveFormInfo: LiveFormInfo): void--><!--Device-LiveFormExtensionAbility-onLiveFormDestroy(liveFormInfo: LiveFormInfo): void-End-->

**System capability:** SystemCapability.Ability.Form

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| liveFormInfo | [LiveFormInfo](arkts-form-appformliveformextensionability-liveforminfo-i.md) | Yes | Interactive widget information, including the widget ID. |

**Examples**

```TypeScript
import { LiveFormExtensionAbility, LiveFormInfo } from '@kit.FormKit';

const TAG: string = '[testTag] LiveFormExtAbility';

export default class LiveFormExtAbility extends LiveFormExtensionAbility {
  onLiveFormDestroy(liveFormInfo: LiveFormInfo) {
    console.info(TAG, `onLiveFormDestroy, liveFormInfo: ${liveFormInfo.formId}`);
  }
}
```

## context

```TypeScript
context: LiveFormExtensionContext
```

Context of the **LiveFormExtensionAbility**. This context is inherited from [ExtensionContext](../../apis-ability-kit/arkts-apis/arkts-ability-extensioncontext-c.md).

**Type:** [LiveFormExtensionContext](arkts-form-liveformextensioncontext-c.md)

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-LiveFormExtensionAbility-context: LiveFormExtensionContext--><!--Device-LiveFormExtensionAbility-context: LiveFormExtensionContext-End-->

**System capability:** SystemCapability.Ability.Form

## liveFormContext

```TypeScript
liveFormContext: LiveFormExtensionContext
```

Context of the **LiveFormExtensionAbility**. This context is inherited from [ExtensionContext](../../apis-ability-kit/arkts-apis/arkts-ability-extensioncontext-c.md).

**Type:** [LiveFormExtensionContext](arkts-form-liveformextensioncontext-c.md)

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-LiveFormExtensionAbility-liveFormContext: LiveFormExtensionContext--><!--Device-LiveFormExtensionAbility-liveFormContext: LiveFormExtensionContext-End-->

**System capability:** SystemCapability.Ability.Form

