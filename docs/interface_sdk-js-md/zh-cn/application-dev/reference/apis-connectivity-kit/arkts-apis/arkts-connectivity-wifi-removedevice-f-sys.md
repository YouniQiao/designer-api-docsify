# removeDevice（系统接口）

## 导入模块

```TypeScript
import { wifi } from 'kits/@kit.ConnectivityKit';
```

## removeDevice

```TypeScript
function removeDevice(id: number): boolean
```

Deletes a Wi-Fi network with a specified ID.

&lt;p&gt;After a Wi-Fi network is deleted, its configuration will be deleted from the list of Wi-Fi configurations.If the Wi-Fi network is being connected, the connection will be interrupted.The application can only delete Wi-Fi networks it has created.

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为7。

**废弃版本：** 9

**替代接口：** ohos.wifiManager/wifiManager.removeDeviceConfig

**需要权限：** ohos.permission.SET_WIFI_INFO and ohos.permission.MANAGE_WIFI_CONNECTION

<!--Device-wifi-function removeDevice(id: number): boolean--><!--Device-wifi-function removeDevice(id: number): boolean-End-->

**系统能力：** SystemCapability.Communication.WiFi.STA

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | number | 是 | Indicates the ID of the Wi-Fi network, which can be obtained using the { |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | Returns { |

## 示例

```TypeScript
import wifi from '@ohos.wifi';

try {
    let id = 0;
    wifi.removeDevice(id);        
}catch(error){
    console.error("failed:" + JSON.stringify(error));
}
```

