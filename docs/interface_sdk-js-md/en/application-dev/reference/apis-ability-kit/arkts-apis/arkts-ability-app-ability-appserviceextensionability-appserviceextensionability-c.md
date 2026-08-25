# AppServiceExtensionAbility

The AppServiceExtensionAbility module provides extended capabilities for background services, including lifecycle callbacks for creating, destroying, connecting, and disconnecting background services.

**Inheritance/Implementation:** AppServiceExtensionAbility extends ExtensionAbility

**Since:** 20

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## Modules to Import

```TypeScript
import { AppServiceExtensionAbility } from 'kits/@kit.AbilityKit';
```

## onConnect

```TypeScript
onConnect(want: Want): rpc.RemoteObject
```

Called when an AppServiceExtensionAbility instance is connected by calling [connectAppServiceExtensionAbility()](arkts-ability-uiabilitycontext-c.md#connectappserviceextensionability).

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| rpc.RemoteObject |

## onCreate

```TypeScript
onCreate(want: Want): void
```

Called when an AppServiceExtensionAbility instance is created. Applications can perform initialization operations, such as registering common event listeners, in this callback.

> **NOTE：**&gt;
> If an AppServiceExtensionAbility instance has already been created, the **onCreate()** callback is not invoked
> again when the instance is started or connected.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes |

## onDestroy

```TypeScript
onDestroy(): void
```

Called when an AppServiceExtensionAbility instance is destroyed. Applications can perform resource cleanup operations, such as unregistering listeners, in this callback.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## onDisconnect

```TypeScript
onDisconnect(want: Want): void
```

Called when all connections to an AppServiceExtensionAbility instance are interrupted.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes |

## onRequest

```TypeScript
onRequest(want: Want, startId: number): void
```

Called each time an AppServiceExtensionAbility instance is started by calling [startAppServiceExtensionAbility()](arkts-ability-uiabilitycontext-c.md#startappserviceextensionability).

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes |
| startId | number | Yes |

## context

```TypeScript
context: AppServiceExtensionContext
```

Context environment for an AppServiceExtensionAbility. This context inherits from [ExtensionContext](arkts-ability-extensioncontext-c.md).

**Type:** [AppServiceExtensionContext](arkts-ability-appserviceextensioncontext-c.md)

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AbilityRuntime.Core
