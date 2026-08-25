# AutoFillExtensionAbility (System API)

The AutoFillExtensionAbility module provides APIs for automatically filling in and saving accounts and passwords. It inherits from [ExtensionAbility](arkts-ability-app-ability-extensionability-extensionability-c.md).

**Inheritance/Implementation:** AutoFillExtensionAbility extends ExtensionAbility

**Since:** 11

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { AutoFillExtensionAbility } from 'kits/@kit.AbilityKit';
```

## onBackground

```TypeScript
onBackground(): void
```

Called when this AutoFillExtensionAbility is switched from the foreground to the background.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**System API:** This is a system API.

## onCreate

```TypeScript
onCreate(): void
```

Called when an AutoFillExtensionAbility is created.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**System API:** This is a system API.

## onDestroy

```TypeScript
onDestroy(): void | Promise<void>
```

Called to clear resources when this AutoFillExtensionAbility is destroyed. This API either returns the result directly or uses a promise to return the result.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**System API:** This is a system API.

## onFillRequest

```TypeScript
onFillRequest(session: UIExtensionContentSession, request: FillRequest, callback: FillRequestCallback): void
```

Called when an auto-fill request is initiated or a password is generated.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| session | [UIExtensionContentSession](arkts-ability-app-ability-uiextensioncontentsession-uiextensioncontentsession-c.md) | Yes |
| request | [FillRequest](arkts-ability-autofillrequest-fillrequest-i.md) | Yes |
| callback | [FillRequestCallback](arkts-ability-autofillrequest-fillrequestcallback-i-sys.md) | Yes |

## onForeground

```TypeScript
onForeground(): void
```

Called when this AutoFillExtensionAbility is switched from the background to the foreground.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**System API:** This is a system API.

## onSaveRequest

```TypeScript
onSaveRequest(session: UIExtensionContentSession, request: SaveRequest, callback: SaveRequestCallback): void
```

Called when automatic or manual saving is initiated.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| session | [UIExtensionContentSession](arkts-ability-app-ability-uiextensioncontentsession-uiextensioncontentsession-c.md) | Yes |
| request | [SaveRequest](arkts-ability-autofillrequest-saverequest-i.md) | Yes |
| callback | [SaveRequestCallback](arkts-ability-autofillrequest-saverequestcallback-i-sys.md) | Yes |

## onSessionDestroy

```TypeScript
onSessionDestroy(session: UIExtensionContentSession): void
```

Called when a UIExtensionContentSession instance is destroyed for this AutoFillExtensionAbility.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| session | [UIExtensionContentSession](arkts-ability-app-ability-uiextensioncontentsession-uiextensioncontentsession-c.md) | Yes |

## onUpdateRequest

```TypeScript
onUpdateRequest(request: UpdateRequest): void
```

Called when an update request is received.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| request | [UpdateRequest](arkts-ability-autofillrequest-updaterequest-i-sys.md) | Yes |

## context

```TypeScript
context: AutoFillExtensionContext
```

Context of the AutoFillExtensionAbility. This context inherits from **ExtensionContext**.

**Type:** [AutoFillExtensionContext](arkts-ability-autofillextensioncontext-c-sys.md)

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**System API:** This is a system API.
