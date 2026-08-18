# ModifierUtils

ModifierUtils provides utility methods for modifier and attribute operations.

**Since:** 26.0.0

<!--Device-unnamed-export declare class ModifierUtils--><!--Device-unnamed-export declare class ModifierUtils-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## isInstanceOf

```TypeScript
static isInstanceOf<T extends CommonMethod<T>>(instance: T, componentName: string): boolean
```

Checks if the given instance is of the specified component type.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ModifierUtils-static isInstanceOf<T extends CommonMethod<T>>(instance: T, componentName: string): boolean--><!--Device-ModifierUtils-static isInstanceOf<T extends CommonMethod<T>>(instance: T, componentName: string): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| instance | T | Yes |
| componentName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |
