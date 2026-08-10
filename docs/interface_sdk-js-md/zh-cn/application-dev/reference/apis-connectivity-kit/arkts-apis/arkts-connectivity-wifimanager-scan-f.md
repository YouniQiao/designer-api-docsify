# scan

## 导入模块

```TypeScript
import { wifiManager } from 'kits/@kit.ConnectivityKit';
```

## scan

```TypeScript
function scan(): void
```

Scan Wi-Fi hotspot.

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为9。

**废弃版本：** 10

**替代接口：** [wifiManager.startScan](arkts-connectivity-wifimanager-startscan-f.md#startscan)

**需要权限：** ohos.permission.SET_WIFI_INFO and ohos.permission.LOCATION and ohos.permission.APPROXIMATELY_LOCATION

<!--Device-wifiManager-function scan(): void--><!--Device-wifiManager-function scan(): void-End-->

**系统能力：** SystemCapability.Communication.WiFi.STA

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| 201 | Permission denied. |
| 2501000 | Operation failed. |

## 示例

```TypeScript
import { wifiManager } from '@kit.ConnectivityKit';

  try {
    wifiManager.scan();
  }catch(error){
    console.error("failed:" + JSON.stringify(error));
  }
```

