# OnErrorFn (System API)

```TypeScript
type OnErrorFn = (code: number, name: string, message: string) => void
```

Defines a OnError function.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-type OnErrorFn = (code: number, name: string, message: string) => void--><!--Device-unnamed-type OnErrorFn = (code: number, name: string, message: string) => void-End-->

**System capability:** SystemCapability.Ability.AppExtension.VerticalPanel

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| code | number | Yes | The code returned if the UIAbility or UIExtensionAbility failed to start.  |
| name | string | Yes | The name returned if the UIAbility or UIExtensionAbility failed to start.  |
| message | string | Yes | The message returned if the UIAbility or UIExtensionAbility failed to start.  |

