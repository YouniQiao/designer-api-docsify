# processPluginCommand

## Modules to Import

```TypeScript
import { dlpPermission } from '@kit.DataProtectionKit';
```

## processPluginCommand

```TypeScript
function processPluginCommand(code: PluginCmd, message: string): Promise<string>
```

Process the plugin-related commands in the transparent encryption and decryption scenario.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.1.0.

**Deprecated since:** -1

**Required permissions:** ohos.permission.DLP_POLICY_MANAGER

**Model restriction:** This API can be used only in the stage model.

<!--Device-dlpPermission-function processPluginCommand(code: PluginCmd, message: string): Promise<string>--><!--Device-dlpPermission-function processPluginCommand(code: PluginCmd, message: string): Promise<string>-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| code | [PluginCmd](arkts-dataprotection-dlppermission-plugincmd-e.md) | Yes | Represents the command code for the plugin of an enterprise security application |
| message | string | Yes | Represents the messages associated with the given command &lt;br&gt;The maximum length is 4096. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;string&gt; | Promise used to return the result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [19100001](../errorcode-dlp.md#19100001-invalid-parameter) | Invalid parameter value. |
| [19100011](../errorcode-dlp.md#19100011-system-service-abnormal) | The system ability works abnormally. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| 19100025 | The file is invalid. |

