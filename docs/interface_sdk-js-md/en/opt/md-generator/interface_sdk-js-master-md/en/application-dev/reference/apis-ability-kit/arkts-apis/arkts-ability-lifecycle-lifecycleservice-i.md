# LifecycleService

interface of service lifecycle.

**Since:** 7

<!--Device-unnamed-export declare interface LifecycleService--><!--Device-unnamed-export declare interface LifecycleService-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.FAModel

## onCommand

```TypeScript
onCommand?(want: Want, startId: number): void
```

Called back when Service is started.

**Since:** 7

**Model restriction:** This API can be used only in the FA model.

<!--Device-LifecycleService-onCommand?(want: Want, startId: number): void--><!--Device-LifecycleService-onCommand?(want: Want, startId: number): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.FAModel

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes |
| startId | number | Yes |

## onConnect

```TypeScript
onConnect?(want: Want): rpc.RemoteObject
```

Called back when a Service ability is first connected to an ability.

**Since:** 7

**Model restriction:** This API can be used only in the FA model.

<!--Device-LifecycleService-onConnect?(want: Want): rpc.RemoteObject--><!--Device-LifecycleService-onConnect?(want: Want): rpc.RemoteObject-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.FAModel

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| rpc.RemoteObject |

## onDisconnect

```TypeScript
onDisconnect?(want: Want): void
```

Called back when all abilities connected to a Service ability are disconnected.

**Since:** 7

**Model restriction:** This API can be used only in the FA model.

<!--Device-LifecycleService-onDisconnect?(want: Want): void--><!--Device-LifecycleService-onDisconnect?(want: Want): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.FAModel

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes |

## onReconnect

```TypeScript
onReconnect?(want: Want): void
```

Called when a new client attempts to connect to a Service ability after all previous client connections to it are disconnected.&lt;p&gt;The Service ability must have been started but not been destroyed, that is, [startAbility](#startAbility) has been called but [terminateSelf](#terminateSelf) has not.&lt;/p&gt;

**Since:** 7

**Model restriction:** This API can be used only in the FA model.

<!--Device-LifecycleService-onReconnect?(want: Want): void--><!--Device-LifecycleService-onReconnect?(want: Want): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.FAModel

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes |

## onStart

```TypeScript
onStart?(): void
```

Called back when an ability is started for initialization (it can be called only once in the entire lifecycle of an ability).

**Since:** 7

**Model restriction:** This API can be used only in the FA model.

<!--Device-LifecycleService-onStart?(): void--><!--Device-LifecycleService-onStart?(): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.FAModel

## onStop

```TypeScript
onStop?(): void
```

Called back before an ability is destroyed.

**Since:** 7

**Model restriction:** This API can be used only in the FA model.

<!--Device-LifecycleService-onStop?(): void--><!--Device-LifecycleService-onStop?(): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.FAModel
