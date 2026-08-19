# onChange

## Modules to Import

```TypeScript
import { display } from '@kit.ArkUI';
```

## onChange

```TypeScript
function onChange(callback: Callback<long>): void
```

Register the callback for display changes.

**Since:** 23

<!--Device-display-function onChange(callback: Callback<long>): void--><!--Device-display-function onChange(callback: Callback<long>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;long&gt; | Yes | the display id of changed |

