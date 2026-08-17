# apiAvailable

## apiAvailable

```TypeScript
function apiAvailable(version: string | int): boolean
```

Checks whether a specified API version is available on the current device. This API provides compatibility check across different OpenHarmony/Distribution OS versions. A suitable version check method is automatically selected based on the input format and supported API versions.

**Since:** 26.1.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-deviceInfo-function apiAvailable(version: string | int): boolean--><!--Device-deviceInfo-function apiAvailable(version: string | int): boolean-End-->

**System capability:** SystemCapability.Startup.SystemInfo

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| version | string \| int | Yes | API version number to be verified. The value can be an integer or in the dotted format. - String format shall be in M.S.F (e.g., "26.0.0", "5.0.1"): - For API 26.0.0 & 26.0.0+ (version >= 26.0.0): Represents both OpenHarmony and Distribution OS API versions - For API 26.0.0- (version &lt; 26.0.0): Represents Distribution OS API version - Number format (e.g., 13): Represents OpenHarmony SDK API version (API 26- only) M&gt;=26,0&lt;=S&lt;=99,0&lt;=F&lt;=99. A compilation error occurs when an invalid literal is input. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Boolean value. The value **true** indicates that the current version number is later than or equal to the input parameter version number; **false** indicates that the current device's API version is lower than the input version number, or the input version number is in an invalid format, or the specified version does not exist. |

