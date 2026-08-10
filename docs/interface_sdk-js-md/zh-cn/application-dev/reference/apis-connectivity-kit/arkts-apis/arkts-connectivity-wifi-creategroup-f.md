# createGroup

## 导入模块

```TypeScript
import { wifi } from 'kits/@kit.ConnectivityKit';
```

## createGroup

```TypeScript
function createGroup(config: WifiP2PConfig): boolean
```

Creates a P2P group.

**起始版本：** 8

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为8。

**废弃版本：** 9

**替代接口：** ohos.wifiManager/wifiManager.createP2pGroup

**需要权限：** ohos.permission.GET_WIFI_INFO

<!--Device-wifi-function createGroup(config: WifiP2PConfig): boolean--><!--Device-wifi-function createGroup(config: WifiP2PConfig): boolean-End-->

**系统能力：** SystemCapability.Communication.WiFi.P2P

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| config | [WifiP2PConfig](arkts-connectivity-wifimanager-wifip2pconfig-i.md) | 是 | Indicates the configuration for creating a group. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | Returns { |

## 示例

```TypeScript
import wifi from '@ohos.wifi';

try {
  let config:wifi.WifiP2PConfig = {
    deviceAddress: "****",
    netId: 0,
    passphrase: "*****",
    groupName: "****",
    goBand: 0
  }
  wifi.createGroup(config);  
  
}catch(error){
  console.error("failed:" + JSON.stringify(error));
}
```

