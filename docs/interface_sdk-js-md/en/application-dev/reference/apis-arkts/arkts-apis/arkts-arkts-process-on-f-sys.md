# on (System API)

## Modules to Import

```TypeScript
import { process } from 'kits/@kit.ArkTS';
```

## on

```TypeScript
function on(type: string, listener: EventListener): void
```

注册事件。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

<!--Device-process-function on(type: string, listener: EventListener): void--><!--Device-process-function on(type: string, listener: EventListener): void-End-->

**System capability:** SystemCapability.Utils.Lang

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | string | Yes | 表示注册的事件类型。 |
| listener | [EventListener](arkts-arkts-worker-eventlistener-i.md) | Yes | 表示注册的事件函数。 |

