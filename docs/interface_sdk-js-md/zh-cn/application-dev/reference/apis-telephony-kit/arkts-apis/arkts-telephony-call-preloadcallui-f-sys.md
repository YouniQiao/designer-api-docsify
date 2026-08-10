# preloadCallUI（系统接口）

## 导入模块

```TypeScript
import { call } from 'kits/@kit.TelephonyKit';
```

## preloadCallUI

```TypeScript
function preloadCallUI(): Promise<boolean>
```

Preload callUI.

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**需要权限：** ohos.permission.SET_TELEPHONY_STATE

<!--Device-call-function preloadCallUI(): Promise<boolean>--><!--Device-call-function preloadCallUI(): Promise<boolean>-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;boolean&gt; | The promise returned by the preloadCallUI. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 8400001 | Invalid parameter value. |
| 8400002 | Operation failed. Cannot connect to service. |
| 8400003 | System internal error. |
| 8400999 | Unknown error code. |
| 201 | Permission denied. |
| 202 | Non-system applications use system APIs. |

