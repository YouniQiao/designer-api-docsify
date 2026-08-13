# getAccessibilityExtensionList

## Modules to Import

```TypeScript
import { accessibility } from '@kit.AccessibilityKit';
```

## getAccessibilityExtensionList

```TypeScript
function getAccessibilityExtensionList(
    abilityType: AbilityType,
    stateType: AbilityState
  ): Promise<Array<AccessibilityAbilityInfo>>
```

Obtains the accessibility application list. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

<!--Device-accessibility-function getAccessibilityExtensionList(    abilityType: AbilityType,    stateType: AbilityState  ): Promise<Array<AccessibilityAbilityInfo>>--><!--Device-accessibility-function getAccessibilityExtensionList(    abilityType: AbilityType,    stateType: AbilityState  ): Promise<Array<AccessibilityAbilityInfo>>-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| abilityType | [AbilityType](arkts-accessibility-accessibility-abilitytype-t.md) | Yes |
| [stateType](../../apis-background-tasks-kit/arkts-apis/arkts-backgroundtasks-bundlestate-bundleactivestate-i.md) | [AbilityState](arkts-accessibility-accessibility-abilitystate-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[AccessibilityAbilityInfo](arkts-accessibility-accessibility-accessibilityabilityinfo-i.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |


## getAccessibilityExtensionList

```TypeScript
function getAccessibilityExtensionList(
    abilityType: AbilityType,
    stateType: AbilityState,
    callback: AsyncCallback<Array<AccessibilityAbilityInfo>>
  ): void
```

Obtains the accessibility application list. This API uses an asynchronous callback to return the result.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

<!--Device-accessibility-function getAccessibilityExtensionList(    abilityType: AbilityType,    stateType: AbilityState,    callback: AsyncCallback<Array<AccessibilityAbilityInfo>>  ): void--><!--Device-accessibility-function getAccessibilityExtensionList(    abilityType: AbilityType,    stateType: AbilityState,    callback: AsyncCallback<Array<AccessibilityAbilityInfo>>  ): void-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| abilityType | [AbilityType](arkts-accessibility-accessibility-abilitytype-t.md) | Yes |
| [stateType](../../apis-background-tasks-kit/arkts-apis/arkts-backgroundtasks-bundlestate-bundleactivestate-i.md) | [AbilityState](arkts-accessibility-accessibility-abilitystate-t.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[AccessibilityAbilityInfo](arkts-accessibility-accessibility-accessibilityabilityinfo-i.md)&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
