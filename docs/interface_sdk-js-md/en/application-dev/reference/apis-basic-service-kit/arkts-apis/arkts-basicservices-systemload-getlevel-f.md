# getLevel

## Modules to Import

```TypeScript
import { systemLoad } from 'kits/@kit.BasicServicesKit';
```

## getLevel

```TypeScript
function getLevel(): Promise<SystemLoadLevel>
```

获取系统负载融合档位，使用promise异步回调。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-systemLoad-function getLevel(): Promise<SystemLoadLevel>--><!--Device-systemLoad-function getLevel(): Promise<SystemLoadLevel>-End-->

**System capability:** SystemCapability.ResourceSchedule.SystemLoad

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;SystemLoadLevel&gt; | Promise对象，返回系统负载融合档位。 |

