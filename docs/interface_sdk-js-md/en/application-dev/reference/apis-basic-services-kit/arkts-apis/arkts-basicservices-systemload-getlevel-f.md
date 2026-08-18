# getLevel

## Modules to Import

```TypeScript
import { systemLoad } from '@kit.BasicServicesKit';
```

## getLevel

```TypeScript
function getLevel(): Promise<SystemLoadLevel>
```

Obtains the system load level. This API uses a promise to return the result.

**Since:** 23

<!--Device-systemLoad-function getLevel(): Promise<SystemLoadLevel>--><!--Device-systemLoad-function getLevel(): Promise<SystemLoadLevel>-End-->

**System capability:** SystemCapability.ResourceSchedule.SystemLoad

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[SystemLoadLevel](arkts-basicservices-systemload-systemloadlevel-e.md)&gt; | Promise used to return the system load level. |

