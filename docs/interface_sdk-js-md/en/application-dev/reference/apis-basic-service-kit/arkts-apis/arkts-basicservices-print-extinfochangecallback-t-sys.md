# ExtInfoChangeCallback (System API)

```TypeScript
type ExtInfoChangeCallback = (extensionId: string, info: string) => void
```

Defines the callback type used in registering to listen for extension change.The value of extensionId indicates the print extension id.The value of info indicates the connect info.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-print-type ExtInfoChangeCallback = (extensionId: string, info: string) => void--><!--Device-print-type ExtInfoChangeCallback = (extensionId: string, info: string) => void-End-->

**System capability:** SystemCapability.Print.PrintFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| extensionId | string | Yes | the printer extension id  |
| info | string | Yes | the information of printer  |

