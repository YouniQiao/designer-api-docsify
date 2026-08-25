# @ohos.app.ability.errorManager(Error Management Module)

The ErrorManager module provides capabilities for registering and unregistering error observers, which are primarily used to listen for errors such as JavaScript crashes and application freezes.

**Since:** 9

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## Modules to Import

```TypeScript
import { errorManager } from 'kits/@kit.AbilityKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [off(Error Management Module)](arkts-ability-errormanager-off-f.md#offerror) |
| [off(Error Management Module)](arkts-ability-errormanager-off-f.md#offerror) |
| [off(Error Management Module)](arkts-ability-errormanager-off-f.md#offloopobserver) |
| [off(Error Management Module)](arkts-ability-errormanager-off-f.md#offunhandledrejection) |
| [off(Error Management Module)](arkts-ability-errormanager-off-f.md#offglobalunhandledrejectiondetected) |
| [off(Error Management Module)](arkts-ability-errormanager-off-f.md#offfreeze) |
| [off(Error Management Module)](arkts-ability-errormanager-off-f.md#offglobalerroroccurred) |
| [on(Error Management Module)](arkts-ability-errormanager-on-f.md#onerror) |
| [on(Error Management Module)](arkts-ability-errormanager-on-f.md#onloopobserver) |
| [on(Error Management Module)](arkts-ability-errormanager-on-f.md#onunhandledrejection) |
| [on(Error Management Module)](arkts-ability-errormanager-on-f.md#onglobalunhandledrejectiondetected) |
| [on(Error Management Module)](arkts-ability-errormanager-on-f.md#onfreeze) |
| [on(Error Management Module)](arkts-ability-errormanager-on-f.md#onglobalerroroccurred) |
| [setDefaultErrorHandler(Error Management Module)](arkts-ability-errormanager-setdefaulterrorhandler-f.md) |
| [setDefaultFreezeObserver(Error Management Module)](arkts-ability-errormanager-setdefaultfreezeobserver-f.md) |
| [setDefaultResourceUsageObserver(Error Management Module)](arkts-ability-errormanager-setdefaultresourceusageobserver-f.md) |

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [GlobalError(Error Management Module)](arkts-ability-errormanager-globalerror-i.md) |

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [InstanceType(Error Management Module)](arkts-ability-errormanager-instancetype-e.md) |
| [ResourceType(Error Management Module)](arkts-ability-errormanager-resourcetype-e.md) |

### Types

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ErrorHandler(Error Management Module)](arkts-ability-errormanager-errorhandler-t.md) |
| [ErrorObserver(Error Management Module)](arkts-ability-errormanager-errorobserver-t.md) |
| [FreezeObserver(Error Management Module)](arkts-ability-errormanager-freezeobserver-t.md) |
| [GlobalObserver(Error Management Module)](arkts-ability-errormanager-globalobserver-t.md) |
| [LoopObserver(Error Management Module)](arkts-ability-errormanager-loopobserver-t.md) |
| [ResourceUsageObserver(Error Management Module)](arkts-ability-errormanager-resourceusageobserver-t.md) |
| [UnhandledRejectionObserver(Error Management Module)](arkts-ability-errormanager-unhandledrejectionobserver-t.md) |
