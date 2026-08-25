# PhotoEditorExtensionAbility

Class of the photo editor ExtensionAbility, which provides APIs for you to edit photos.@extends ExtensionAbility

**Inheritance/Implementation:** PhotoEditorExtensionAbility extends ExtensionAbility

**Since:** 12

**System capability:** SystemCapability.Ability.AppExtension.PhotoEditorExtension

## Modules to Import

```TypeScript
import { PhotoEditorExtensionAbility } from 'kits/@kit.AbilityKit';
```

## onBackground

```TypeScript
onBackground(): void
```

Called back when the state of an UI extension changes to background.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

## onCreate

```TypeScript
onCreate(): void
```

Called back when an UI extension is started for initialization.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AppExtension.PhotoEditorExtension

## onDestroy

```TypeScript
onDestroy(): void | Promise<void>
```

Called back before an UI extension is destroyed.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AppExtension.PhotoEditorExtension

## onForeground

```TypeScript
onForeground(): void
```

Called back when the state of an UI extension changes to foreground.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

## onStartContentEditing

```TypeScript
onStartContentEditing(uri: string, want: Want, session: UIExtensionContentSession): void
```

Called back when an UI extension session is created and original image is ready.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AppExtension.PhotoEditorExtension

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes |
| session | [UIExtensionContentSession](arkts-ability-app-ability-uiextensioncontentsession-uiextensioncontentsession-c.md) | Yes |

## context

```TypeScript
context: PhotoEditorExtensionContext
```

Indicates configuration information about an Photo editor extension ability context.

**Type:** [PhotoEditorExtensionContext](arkts-ability-photoeditorextensioncontext-c.md)

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AppExtension.PhotoEditorExtension
