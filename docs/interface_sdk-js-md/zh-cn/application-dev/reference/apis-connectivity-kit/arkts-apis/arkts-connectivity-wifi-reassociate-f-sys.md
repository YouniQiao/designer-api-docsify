# reassociate（系统接口）

## 导入模块

```TypeScript
import { wifi } from 'kits/@kit.ConnectivityKit';
```

## reassociate

```TypeScript
function reassociate(): boolean
```

Re-associate to current network.

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为7。

**废弃版本：** 9

**替代接口：** ohos.wifiManager/wifiManager.reassociate

**需要权限：** ohos.permission.SET_WIFI_INFO and ohos.permission.MANAGE_WIFI_CONNECTION

<!--Device-wifi-function reassociate(): boolean--><!--Device-wifi-function reassociate(): boolean-End-->

**系统能力：** SystemCapability.Communication.WiFi.STA

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | { |

## 示例

```TypeScript
import wifi from '@ohos.wifi';

try {
    wifi.reassociate();
}catch(error){
    console.error("failed:" + JSON.stringify(error));
}
```

