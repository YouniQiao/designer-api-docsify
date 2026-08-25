# ChildProcess

ChildProcess is the base class for you to customize child processes. When starting a child process through [childProcessManager](arkts-app-ability-childprocessmanager.md), you must inherit this class and override the entrypoint method.

**Since:** 11

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## Modules to Import

```TypeScript
import { ChildProcess } from 'kits/@kit.AbilityKit';
```

## onStart

```TypeScript
onStart(args?: ChildProcessArgs): void
```

Entrypoint method of the child process. This callback is triggered when the child process is started through [childProcessManager](arkts-app-ability-childprocessmanager.md).

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [args](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-sqlinfo-i.md) | [ChildProcessArgs](arkts-ability-app-ability-childprocessargs-childprocessargs-i.md) | No |
