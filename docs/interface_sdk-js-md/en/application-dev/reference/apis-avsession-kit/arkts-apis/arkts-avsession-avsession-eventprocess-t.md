# EventProcess

```TypeScript
type EventProcess = (event: string, args: Record<string, Object>) => void
```

The general process funcation with an event and arguments.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Dyn since version 26.1.0; ArkTS-Sta since version 23.

<!--Device-avSession-type EventProcess = (event: string, args: Record<string, Object>) => void--><!--Device-avSession-type EventProcess = (event: string, args: Record<string, Object>) => void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | string | Yes | request event  |
| args | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;string, Object&gt; | Yes | arguments associated with event  |

