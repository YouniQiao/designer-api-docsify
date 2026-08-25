# DistributedExtensionAbility

The **DistributedExtensionAbility** module provides distributed extension capabilities and lifecycle callbacks for distributed ability creation, destruction, and connection.

**Since:** 20

**System capability:** SystemCapability.DistributedSched.AppCollaboration

## Modules to Import

```TypeScript
import { DistributedExtensionAbility } from 'kits/@kit.DistributedServiceKit';
```

## onCollaborate

```TypeScript
onCollaborate(wantParam: Record<string, Object>): AbilityConstant.CollaborateResult
```

Callback invoked to return the collaboration result in multi-device collaboration scenarios.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedSched.AppCollaboration

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| wantParam | Record & lt;string, Object & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| AbilityConstant.CollaborateResult |

## onCreate

```TypeScript
onCreate(want: Want): void
```

Callback invoked to initialize the service logic when a **DistributedExtensionAbility** instance is created.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedSched.AppCollaboration

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |

## onDestroy

```TypeScript
onDestroy(): void
```

Callback invoked to clear resources when a **ServiceExtensionAbility** instance is destroyed.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedSched.AppCollaboration

## context

```TypeScript
context: DistributedExtensionContext
```

Context of the **DistributedExtension**. This context inherits from **ExtensionContext**.

**Type:** [DistributedExtensionContext](arkts-distributedservice-application-distributedextensioncontext-distributedextensioncontext-c.md)

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedSched.AppCollaboration
