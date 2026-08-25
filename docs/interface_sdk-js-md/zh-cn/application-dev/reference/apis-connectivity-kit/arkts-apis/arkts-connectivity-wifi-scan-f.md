# scan

## 导入模块

```TypeScript
import { wifi } from '@kit.ConnectivityKit';
```

## scan

```TypeScript
function scan(): boolean
```

启动WLAN扫描。<p>该接口工作在异步模式。</p>

**起始版本：** 6

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为6。

**废弃版本：** 9

**替代接口：** [scan](arkts-connectivity-wifimanager-scan-f.md)

**需要权限：** ohos.permission.SET_WIFI_INFO and ohos.permission.LOCATION

**系统能力：** SystemCapability.Communication.WiFi.STA

**返回值：**

| 类型 |
| --- |
| boolean |

**示例**

```TypeScript
import wifi from '@ohos.wifi';

try {
  wifi.scan();
}catch(error){
  console.error("failed:" + JSON.stringify(error));
}
```
