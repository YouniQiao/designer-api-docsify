# apiAvailable

## Modules to Import

```TypeScript
import { deviceInfo } from 'kits/@kit.BasicServicesKit';
```

## apiAvailable

```TypeScript
function apiAvailable(version: string | number): boolean
```

检查指定的API版本在当前设备上是否可用。此方法提供跨不同OpenHarmony/发行版系统版本的兼容性检查。它会根据输入格式和API版本范围自动选择合适的版本检查方法。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-deviceInfo-function apiAvailable(version: string | number): boolean--><!--Device-deviceInfo-function apiAvailable(version: string | number): boolean-End-->

**System capability:** SystemCapability.Startup.SystemInfo

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| version | string \| number | Yes | 需要校验的API版本号，支持整数格式版本号和字符串格式版本号。 - 字符串采用M.S.F格式（如 "26.0.0","5.0.1"）： - 对于API 26及以上版本（version >= 26.0.0）：代表OpenHarmony和发行版系统API版本。 - 对于API 26以下版本（version < 26.0.0）：代表发行版系统API版本。 - 整数格式（如 13）：代表OpenHarmony SDK API版本。（仅支持API 26以下） |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 布尔值。返回true表示当前设备API版本大于等于入参版本号；返回false代表当前设备API版本小于入参版本号，或传入的版本号格式非法、该版本不存在。 |

## Examples

```TypeScript
import { deviceInfo } from '@kit.BasicServicesKit';

// Check whether the API version is 26.0.0 or later. If true is returned, the API version of the current device meets the requirements.
if (deviceInfo.apiAvailable("26.0.0")) {
   // Method that requires version isolation
}


// Check API 5.0.1 (Distribution OS version, API 26.0.0-)
if (deviceInfo.apiAvailable("5.0.1")) {
   // Method that requires version isolation
}


// Check API 13 (OpenHarmony SDK version, API 26.0.0-)
if (deviceInfo.apiAvailable(13)) {
   // Method that requires version isolation
}
```

