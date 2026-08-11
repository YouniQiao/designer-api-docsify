# OnErrorFn (System API)

```TypeScript
type OnErrorFn = (code: number, name: string, message: string) => void
```

Defines a OnError function.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-type OnErrorFn = (code: number, name: string, message: string) => void--><!--Device-unnamed-type OnErrorFn = (code: number, name: string, message: string) => void-End-->

**System capability:** SystemCapability.Ability.AppExtension.VerticalPanel

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| code | number | Yes |
| name | string | Yes |
| message | string | Yes |
