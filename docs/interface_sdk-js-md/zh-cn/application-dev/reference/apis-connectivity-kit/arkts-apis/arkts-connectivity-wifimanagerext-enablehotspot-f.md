# enableHotspot

## 导入模块

```TypeScript
import { wifiManagerExt } from 'kits/@kit.ConnectivityKit';
```

## enableHotspot

```TypeScript
function enableHotspot(): void
```

Enable Wi-Fi hotspot function.This method is asynchronous. After the Wi-Fi hotspot is enabled, Wi-Fi may be disabled.

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为9。

**废弃版本：** 10

**需要权限：** ohos.permission.MANAGE_WIFI_HOTSPOT_EXT

<!--Device-wifiManagerExt-function enableHotspot(): void--><!--Device-wifiManagerExt-function enableHotspot(): void-End-->

**系统能力：** SystemCapability.Communication.WiFi.AP.Extension

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| 2701000 | Operation failed. |
| 201 | Permission denied. |

## 示例

```TypeScript
import { wifiManagerExt } from '@kit.ConnectivityKit';

  try {
      wifiManagerExt.enableHotspot();
  }catch(error){
      console.error("failed: " + JSON.stringify(error));
  }
```

