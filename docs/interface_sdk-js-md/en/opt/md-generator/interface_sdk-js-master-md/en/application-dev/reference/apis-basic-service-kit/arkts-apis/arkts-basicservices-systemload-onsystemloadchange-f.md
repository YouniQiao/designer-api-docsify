# onSystemLoadChange

## Modules to Import

```TypeScript
import { systemLoad } from '@kit.BasicServicesKit';
```

## onSystemLoadChange

```TypeScript
function onSystemLoadChange(callback: Callback<SystemLoadLevel>): void
```

Register system load callback for perception system load change

**Since:** 23

**Deprecated since:** -1

<!--Device-systemLoad-function onSystemLoadChange(callback: Callback<SystemLoadLevel>): void--><!--Device-systemLoad-function onSystemLoadChange(callback: Callback<SystemLoadLevel>): void-End-->

**System capability:** SystemCapability.ResourceSchedule.SystemLoad

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[SystemLoadLevel](arkts-basicservices-systemload-systemloadlevel-e.md)&gt; | Yes |
