# onAdd

## Modules to Import

```TypeScript
import { display } from 'display';
```

## onAdd

```TypeScript
function onAdd(callback: Callback<long>): void
```

Register the callback for display add events.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-display-function onAdd(callback: Callback<long>): void--><!--Device-display-function onAdd(callback: Callback<long>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;long&gt; | Yes | the display id of changed |

