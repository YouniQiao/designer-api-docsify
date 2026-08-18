# startDiscoverDevices

## 导入模块

```TypeScript
```

## startDiscoverDevices

```TypeScript
function startDiscoverDevices(): boolean
```

发现WLAN P2P设备。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** startDiscoverP2pDevices

**需要权限：** ohos.permission.GET_WIFI_INFO and ohos.permission.LOCATION

<!--Device-wifi-function startDiscoverDevices(): boolean--><!--Device-wifi-function startDiscoverDevices(): boolean-End-->

**系统能力：** SystemCapability.Communication.WiFi.P2P

**返回值：**

| 类型 |
| --- |
| boolean |

**示例**

```TypeScript
import wifi from '@ohos.wifi';

try {
  wifi.startDiscoverDevices();  
}catch(error){
  console.error("failed:" + JSON.stringify(error));
}
```
