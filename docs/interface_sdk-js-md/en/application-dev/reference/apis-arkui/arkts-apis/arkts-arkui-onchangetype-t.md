# OnChangeType

```TypeScript
export type OnChangeType<T> = (propertyName: string, newValue: T) => void
```

Defines the callback that is called when state variable with value is change

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type OnChangeType<T> = (propertyName: string, newValue: T) => void--><!--Device-unnamed-export type OnChangeType<T> = (propertyName: string, newValue: T) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| propertyName | string | Yes | property name |
| newValue | T | Yes | the new value of state variable |

