# getWifiDetailState（系统接口）

## 导入模块

```TypeScript
import { wifiManager } from 'kits/@kit.ConnectivityKit';
```

## getWifiDetailState

```TypeScript
function getWifiDetailState(): WifiDetailState
```

Obtains information about a Wi-Fi detail state.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.GET_WIFI_INFO and ohos.permission.MANAGE_WIFI_CONNECTION

<!--Device-wifiManager-function getWifiDetailState(): WifiDetailState--><!--Device-wifiManager-function getWifiDetailState(): WifiDetailState-End-->

**系统能力：** SystemCapability.Communication.WiFi.STA

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [WifiDetailState](arkts-connectivity-wifimanager-wifidetailstate-e-sys.md) | Returns information about wifi state. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| 201 | Permission denied. |
| 202 | System API is not allowed called by Non-system application. |
| 2501000 | Operation failed. |

## 示例

```TypeScript
import { wifiManager } from '@kit.ConnectivityKit';

try {
    let ret = wifiManager.getWifiDetailState();
    console.info("wifiDetailState:" + ret);
} catch (error) {
    console.error("failed:" + JSON.stringify(error));
}
```

